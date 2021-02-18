#Debut du jour J-7 

# Nom des Personages.
define bellemere = Character("Elisabeth")
define prince = Character("James Wheeler")
define damedecompagnie = Character("Susan")
define porte = Character("Porte")
define princesse = Character("Victoria Parker",image="princesse")
define narrateur = Character("")
define orga = Character("Josh Walker")
define pere_mariee = Character("Connor Parker")

# Debut du code principal.
label start:

    $ amour = 3
    $ colere = 2

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    jump jour7
    return
