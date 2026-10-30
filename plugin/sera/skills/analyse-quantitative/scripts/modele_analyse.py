# %% [markdown]
# # TITRE DE L'ANALYSE
#
# **Évaluation** : ...
# **Questions de la matrice traitées** : Q?.?, Q?.?
# **Données** : `NOM_DU_FICHIER`, N lignes.
#
# Ce notebook a été préparé et exécuté par SERA. Chaque chiffre du rapport vient d'une cellule ci-dessous.
# Pour le rouvrir sans rien installer : Google Colab, menu Fichier, Importer le notebook, puis exécuter
# les cellules dans l'ordre. Colab demandera le fichier de données.

# %%
# Chargement des données
import pandas as pd

FICHIER = "../donnees/NOM_DU_FICHIER.xlsx"
try:
    from google.colab import files  # présent seulement dans Google Colab
    print("Google Colab : choisissez le fichier de données sur votre ordinateur.")
    FICHIER = next(iter(files.upload()))
except ImportError:
    pass

df_brut = pd.read_excel(FICHIER) if FICHIER.endswith((".xlsx", ".xls")) else pd.read_csv(FICHIER)
print(f"{len(df_brut)} lignes, {df_brut.shape[1]} variables")
df_brut.head()

# %%
# Outils d'analyse : chaque fonction calcule, vérifie ses conditions et écrit la phrase d'interprétation.
import numpy as np
from scipy import stats

RESULTATS = []


def qualifier(valeur, seuils):
    v = abs(valeur)
    return "négligeable" if v < seuils[0] else "faible" if v < seuils[1] else "moyen" if v < seuils[2] else "fort"


def fr(x, decimales=2):
    return f"{x:.{decimales}f}".replace(".", ",")


def ecrire_p(p):
    return "p < 0,001" if p < 0.001 else f"p = {fr(p, 3)}"


def ic_ecart(a, b):
    """Intervalle de confiance à 95 % de la différence des moyennes a - b (Welch)."""
    va, vb = a.var(ddof=1) / len(a), b.var(ddof=1) / len(b)
    ddl = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
    marge = stats.t.ppf(0.975, ddl) * np.sqrt(va + vb)
    ecart = a.mean() - b.mean()
    return ecart - marge, ecart + marge


def croiser(df, ligne, colonne, question=""):
    """Deux variables catégorielles : tableau croisé, khi-deux (ou Fisher), V de Cramér.
    Pour un tableau 2 x 2, donne aussi l'intervalle de l'écart de proportions. Renvoie la p-valeur."""
    d = df[[ligne, colonne]].dropna()
    tab = pd.crosstab(d[ligne], d[colonne])
    pct = pd.crosstab(d[ligne], d[colonne], normalize="index").mul(100).round(1)
    chi2, p, ddl, attendus = stats.chi2_contingency(tab, correction=False)
    part_faibles = (attendus < 5).mean()
    test = "khi-deux"
    if part_faibles > 0.2 and tab.shape == (2, 2):
        p = stats.fisher_exact(tab)[1]
        test = "test exact de Fisher"
    v = np.sqrt(chi2 / (len(d) * (min(tab.shape) - 1)))
    effet = qualifier(v, (0.1, 0.3, 0.5))
    effectifs = " et ".join(str(int(n)) for n in tab.sum(axis=1))
    ic = ""
    if tab.shape == (2, 2):
        modalite = tab.columns[-1]
        n1, n2 = tab.sum(axis=1)
        p1, p2 = tab.iloc[0, -1] / n1, tab.iloc[1, -1] / n2
        marge = 1.96 * np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
        ic = f"{fr(100 * (p1 - p2 - marge), 0)} à {fr(100 * (p1 - p2 + marge), 0)} points"
    if p < 0.05:
        phrase = (f"{colonne} selon {ligne} (n = {len(d)}) : différence significative ({test}, {ecrire_p(p)}), "
                  f"lien {effet} (V de Cramér = {fr(v)}).")
    else:
        phrase = (f"{colonne} selon {ligne} : aucune différence détectable avec ces effectifs (n = {effectifs}) "
                  f"({test}, {ecrire_p(p)}, V de Cramér = {fr(v)}).")
        if ic:
            phrase += f" L'écart réel sur « {modalite} » peut aller de {ic} : ce n'est pas une preuve d'absence d'écart."
    if part_faibles > 0.2 and tab.shape != (2, 2):
        phrase += " Attention : effectifs attendus trop faibles, regrouper des modalités."
    RESULTATS.append({"Question": question, "Analyse": f"{colonne} x {ligne}", "Test": test, "n": len(d),
                      "p": round(p, 4), "Taille de l'effet": f"V = {fr(v)} ({effet})", "IC de l'écart": ic,
                      "Interprétation": phrase})
    print(phrase)
    display(tab)
    display(pct.rename(columns=lambda c: f"{c} (% en ligne)"))
    return p


def comparer(df, variable, groupe, question=""):
    """Variable numérique selon un groupe : moyennes, test de Welch (t ou ANOVA), taille de l'effet.
    Pour deux groupes, donne l'intervalle de confiance de l'écart. Renvoie la p-valeur."""
    d = df[[variable, groupe]].dropna()
    desc = d.groupby(groupe)[variable].agg(["count", "mean", "median", "std"]).round(2)
    desc.columns = ["Effectif", "Moyenne", "Médiane", "Écart-type"]
    noms, groupes = zip(*[(nom, g[variable].values) for nom, g in d.groupby(groupe)])
    asymetrie = max(abs(stats.skew(g)) for g in groupes)
    ic = ""
    if len(groupes) == 2:
        a, b = groupes
        t, p = stats.ttest_ind(a, b, equal_var=False)
        ecart = np.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
        taille = (a.mean() - b.mean()) / ecart
        nom_effet, effet = "d de Cohen", qualifier(taille, (0.2, 0.5, 0.8))
        test = "test t de Welch"
        robuste = stats.mannwhitneyu(a, b)[1]
        bas, haut = ic_ecart(a, b)
        ic = f"{fr(bas, 1)} à {fr(haut, 1)} ({noms[0]} moins {noms[1]})"
    else:
        from statsmodels.stats.oneway import anova_oneway
        res = anova_oneway(groupes, use_var="unequal")
        p = res.pvalue
        tout = np.concatenate(groupes)
        taille = sum(len(g) * (g.mean() - tout.mean()) ** 2 for g in groupes) / ((tout - tout.mean()) ** 2).sum()
        nom_effet, effet = "eta carré", qualifier(taille, (0.01, 0.06, 0.14))
        test = "ANOVA de Welch"
        robuste = stats.kruskal(*groupes)[1]
    moyennes = " ; ".join(f"{n} : {fr(g.mean(), 1)} (n = {len(g)})" for n, g in zip(noms, groupes))
    if p < 0.05:
        phrase = (f"{variable} selon {groupe}, moyennes {moyennes}. Différence significative "
                  f"({test}, {ecrire_p(p)}), écart {effet} ({nom_effet} = {fr(taille)}).")
        if ic:
            phrase += f" Écart estimé entre {ic}."
    else:
        phrase = (f"{variable} selon {groupe}, moyennes {moyennes}. Aucune différence détectable avec ces effectifs "
                  f"({test}, {ecrire_p(p)}, {nom_effet} = {fr(taille)}).")
        if ic:
            phrase += f" L'écart réel peut aller de {ic} : ce n'est pas une preuve d'absence d'écart."
    if (robuste < 0.05) != (p < 0.05):
        phrase += f" Attention : le test non paramétrique ({ecrire_p(robuste)}) ne conclut pas de la même façon, prudence."
    if asymetrie > 2:
        phrase += " Distribution très asymétrique : comparer aussi les médianes."
    RESULTATS.append({"Question": question, "Analyse": f"{variable} selon {groupe}", "Test": test, "n": len(d),
                      "p": round(p, 4), "Taille de l'effet": f"{nom_effet} = {fr(taille)} ({effet})",
                      "IC de l'écart": ic, "Interprétation": phrase})
    print(phrase)
    display(desc)
    return p


def comparer_apparie(df, avant, apres, question=""):
    """Même mesure prise deux fois chez les mêmes personnes (par exemple guichet avant, en ligne maintenant).
    Test de Wilcoxon apparié, médianes, et corrélation bisériale de rangs comme taille de l'effet."""
    d = df[[avant, apres]].dropna()
    diff = (d[apres] - d[avant]).values
    non_nuls = diff[diff != 0]
    rangs = stats.rankdata(np.abs(non_nuls))
    w_plus, w_moins = rangs[non_nuls > 0].sum(), rangs[non_nuls < 0].sum()
    taille = (w_plus - w_moins) / (w_plus + w_moins) if len(non_nuls) else 0.0
    p = stats.wilcoxon(d[avant], d[apres]).pvalue if len(non_nuls) else 1.0
    effet = qualifier(taille, (0.1, 0.3, 0.5))
    medianes = f"médiane {fr(d[avant].median(), 1)} pour « {avant} », {fr(d[apres].median(), 1)} pour « {apres} »"
    if p < 0.05:
        phrase = (f"{avant} puis {apres} (n = {len(d)}, mêmes personnes) : {medianes}. Différence significative "
                  f"(Wilcoxon apparié, {ecrire_p(p)}), effet {effet} (corrélation bisériale = {fr(taille)}). "
                  f"Écart médian : {fr(np.median(diff), 1)}.")
    else:
        phrase = (f"{avant} puis {apres} (n = {len(d)}, mêmes personnes) : {medianes}. Aucune différence détectable "
                  f"avec cet effectif (Wilcoxon apparié, {ecrire_p(p)}).")
    RESULTATS.append({"Question": question, "Analyse": f"{avant} puis {apres}", "Test": "Wilcoxon apparié",
                      "n": len(d), "p": round(p, 4), "Taille de l'effet": f"r = {fr(taille)} ({effet})",
                      "IC de l'écart": "", "Interprétation": phrase})
    print(phrase)
    return p


def stratifier(df, ligne, colonne, strate, question="", effectif_min=10):
    """Refait croiser(ligne, colonne) dans chaque modalité de la strate, pour repérer un effet de composition.
    Les strates de moins de effectif_min personnes sont signalées mais pas testées."""
    tient, testees = 0, 0
    for modalite, sous in df.groupby(strate):
        print(f"--- {strate} = {modalite} ({len(sous)} personnes)")
        if len(sous) < effectif_min or sous[ligne].nunique() < 2 or sous[colonne].nunique() < 2:
            print("Effectif ou variété insuffisants pour tester dans cette strate.")
            continue
        testees += 1
        tient += croiser(sous, ligne, colonne, question=f"{question} | {strate} = {modalite}") < 0.05
    print(f"Le lien {colonne} x {ligne} reste significatif dans {tient} strate(s) sur {testees} testée(s).")
    if testees and tient == 0:
        print("Il disparaît à l'intérieur des strates : l'écart global vient peut-être d'un effet de composition.")


def synthese_resultats(chemin="06-resultats.xlsx"):
    """Tableau final : ajoute la p-valeur corrigée (Holm) pour les tests multiples, et l'exporte."""
    from statsmodels.stats.multitest import multipletests
    synthese = pd.DataFrame(RESULTATS)
    testes = synthese["p"].notna()
    synthese["p corrigé (Holm)"] = np.nan
    synthese["Résiste à la correction"] = ""
    if testes.sum() > 1:
        rejet, p_corr, _, _ = multipletests(synthese.loc[testes, "p"], method="holm")
        synthese.loc[testes, "p corrigé (Holm)"] = p_corr.round(4)
        synthese.loc[testes, "Résiste à la correction"] = np.where(
            synthese.loc[testes, "p"] < 0.05, np.where(rejet, "oui", "non"), "-")
    fragiles = synthese[synthese["Résiste à la correction"] == "non"]
    print(f"{int(testes.sum())} tests réalisés. Résultats significatifs qui ne résistent pas à la correction "
          f"pour tests multiples : {len(fragiles)}.")
    for analyse in fragiles["Analyse"]:
        print(f"  - {analyse} : à présenter comme indicatif.")
    synthese.to_excel(chemin, index=False)
    return synthese

# %% [markdown]
# ## 1. Nettoyage
#
# Les décisions ci-dessous ont été validées par l'évaluateur. La base d'origine n'est jamais modifiée :
# on travaille sur une copie `df`.

# %%
df = df_brut.copy()
# ... une opération par bloc, avec print du nombre de lignes concernées

# %% [markdown]
# ## 2. Description de l'échantillon

# %% [markdown]
# ## 3. Analyses par question de la matrice
#
# Chaque résultat est ventilé par composante de l'objet évalué quand il y en a plusieurs.

# %% [markdown]
# ## 3 bis. Vérification des effets de composition
#
# Pour chaque différence entre groupes qui pourrait venir d'une autre variable, `stratifier()` refait
# la comparaison à l'intérieur de chaque modalité de cette variable.

# %% [markdown]
# ## 4. Synthèse des résultats et limites

# %%
synthese_resultats()
