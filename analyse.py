from donnees import generer_ventes, calculer_montant_vente
import random

def chiffre_affaires_total(ventes):
    """
    Calcule le chiffre d'affaires total.

    Args:
    ventes : list[dict] Liste des ventes.

    Returns: 
    float Chiffre d'affaires total.
    """
    return sum(calculer_montant_vente(vente) for vente in ventes)


def chiffre_affaires_par_region(ventes):
    """
    Calcule le chiffre d'affaires réalisé dans chaque région.

    Args: 
    ventes : list[dict] Liste des ventes.

    Returns: 
    dict: Dictionnaire de la forme :
        { "Normandie": 12000, "Bretagne": 8500, ... }
    """
    ca_regions = {}
    for vente in ventes:
        regions = vente["region"]
        montant = calculer_montant_vente(vente)
        ca_regions[regions] = ca_regions.get(regions, 0) + montant
    return ca_regions


def produit_le_plus_vendu(ventes):
    """
    Détermine le produit vendu en plus grande quantité.

    Args:
    ventes : list[dict] Liste des ventes.

    Returns: Tuple contenant : (nom_du_produit, quantité_totale)
    Exemple: ("Ordinateur", 145)    
    """
    pass


def chiffre_affaires_par_mois(ventes):
    """
    Calcule le chiffre d'affaires de chaque mois.
    Les mois doivent être retournés dans l'ordre chronologique.

    Args: ventes : list[dict]

    Returns: 
    dict, Exemple :
        {
            "January": 12500,
            "February": 14300,
            ...
        }
    """
    pass


def meilleure_region(ventes):
    """
    Identifie la région générant le plus grand chiffre d'affaires.

    Args: 
    ventes : list[dict]

    Returns: 
    tuple, Exemple : ("Normandie", 25800)
    """
    pass


def montant_moyen_vente(ventes):
    """
    Calcule le montant moyen d'une vente.

    Args: 
    ventes : list[dict]

    Returns: 
    float, Montant moyen d'une vente.
    """
    pass


def generer_recommandation(ventes):
    """
    Produit une courte recommandation destinée au décideur.

    La recommandation doit utiliser les résultats des analyses
    précédentes.

    Exemple
    -------
    "La Normandie est la région la plus performante.
    Il peut être intéressant d'y renforcer les actions commerciales."

    Args: 
        ventes : list[dict]
        
    Returns
    str: Recommandation décisionnelle.
    """
    pass


if __name__ == "__main__":

    # Afin d'obtenir les mêmes données lors des démonstrations
    random.seed(42)

    ventes = generer_ventes(120)
    print(ventes)

    print("=" * 50)
    print("TABLEAU DE BORD COMMERCIAL")
    print("=" * 50)

    print(
        f"\nChiffre d'affaires total : "
        f"{chiffre_affaires_total(ventes):,.2f} €"
    )

    print("\nChiffre d'affaires par région :")
    print(chiffre_affaires_par_region(ventes))

    print("\nProduit le plus vendu :")
    print(produit_le_plus_vendu(ventes))

    print("\nChiffre d'affaires par mois :")
    print(chiffre_affaires_par_mois(ventes))

    print("\nMeilleure région :")
    print(meilleure_region(ventes))

    print("\nPanier moyen :")
    print(montant_moyen_vente(ventes))

    print("\nRecommandation :")
    print(generer_recommandation(ventes))