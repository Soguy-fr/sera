"""Calcule la taille d'un échantillon d'enquête pour estimer une proportion.

Usage :
  python taille_echantillon.py [--marge 0.05] [--confiance 0.95] [--p 0.5] [--population N]
                               [--effet-plan 1.0] [--taux-reponse 1.0] [--groupes "Femmes,Hommes"]
                               [--tirage aleatoire|quotas]

--groupes : si l'on veut des résultats fiables pour CHAQUE groupe (et pas seulement pour l'ensemble),
            la taille calculée s'applique à chaque groupe. On donne soit les noms des groupes séparés
            par des virgules ("Femmes,Hommes"), soit leur nombre ("2").
Chaque étape du calcul est affichée, pour pouvoir l'expliquer et la reproduire.
"""
import argparse
import math
import sys

from scipy.stats import norm


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    a = argparse.ArgumentParser()
    a.add_argument("--marge", type=float, default=0.05, help="marge d'erreur, ex. 0.05 pour ±5 points")
    a.add_argument("--confiance", type=float, default=0.95)
    a.add_argument("--p", type=float, default=0.5, help="proportion attendue ; 0.5 donne la taille la plus prudente")
    a.add_argument("--population", type=int, help="taille de la population, si elle est connue")
    a.add_argument("--effet-plan", type=float, default=1.0, help="effet de plan, ex. 1.5 à 2 pour un tirage par grappes")
    a.add_argument("--taux-reponse", type=float, default=1.0, help="ex. 0.9 si 10 %% de non-réponses sont attendus")
    a.add_argument("--groupes", default="")
    a.add_argument("--tirage", choices=["aleatoire", "quotas"], default="aleatoire",
                   help="quotas ou choix raisonné : la taille est un repère, sans marge d'erreur")
    x = a.parse_args()

    if x.marge >= 1:
        print(f"Marge lue comme {x.marge:g} points, soit {x.marge / 100:g} (le script attend une proportion).")
        x.marge /= 100
    if x.confiance > 1:
        x.confiance /= 100
    z = norm.ppf(1 - (1 - x.confiance) / 2)
    n0 = z ** 2 * x.p * (1 - x.p) / x.marge ** 2
    print(f"1. Taille de base : z² x p x (1 - p) / marge² = {z:.2f}² x {x.p} x {1 - x.p:.2f} / {x.marge}² = {n0:.1f}")
    n = n0
    if x.population:
        n = n0 / (1 + (n0 - 1) / x.population)
        print(f"2. Correction pour une population de {x.population} : n0 / (1 + (n0 - 1) / N) = {n:.1f}")
    if x.effet_plan != 1:
        n *= x.effet_plan
        print(f"3. Effet de plan x {x.effet_plan} (tirage par grappes) : {n:.1f}")
    if x.taux_reponse < 1:
        n /= x.taux_reponse
        print(f"4. Majoration pour un taux de réponse de {x.taux_reponse:.0%} : {n:.1f}")
    n = math.ceil(n)
    if x.groupes.strip().isdigit():
        groupes = [f"groupe {i + 1}" for i in range(int(x.groupes))]
    else:
        groupes = [g.strip() for g in x.groupes.split(",") if g.strip()]
    if groupes:
        print(f"\nRésultat : {n} personnes PAR groupe ({', '.join(groupes)}), soit {n * len(groupes)} au total.")
    else:
        print(f"\nRésultat : {n} personnes.")
    if x.tirage == "quotas":
        print("ATTENTION : tirage par quotas. Cette taille n'est qu'un repère. Pas de marge d'erreur : "
              "les résultats seront indicatifs et ne s'extrapolent pas à la population.")
    else:
        print(f"Avec cet échantillon, une proportion de {x.p:.0%} est estimée à ± {x.marge * 100:.0f} points, "
              f"avec une confiance de {x.confiance:.0%}.")


if __name__ == "__main__":
    main()
