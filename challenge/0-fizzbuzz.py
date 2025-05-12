#!/usr/bin/python3

import sys

def fizzbuzz(n):


    for i in range(1, n + 1):
        # Vérifie d'abord si le nombre est divisible par 3 et 5 (priorité)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # Vérifie si le nombre est divisible par 3 uniquement
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Vérifie si le nombre est divisible par 5 uniquement
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # Si le nombre n'est divisible ni par 3 ni par 5, on l'affiche directement
        else:
            print(i, end=" ")
    # Ajouter une nouvelle ligne après l'affichage de la séquence
    print()

# Vérifie si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    # Vérifie si un seul argument est passé (en plus du nom du script)
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)

    try:
        # Convertit l'argument en entier
        number = int(sys.argv[1])
        # Appelle la fonction fizzbuzz avec le nombre en argument
        fizzbuzz(number)
    except ValueError:
        # Affiche un message d'erreur si l'argument n'est pas un entier valide
        print("Veuillez entrer un nombre valide.")
