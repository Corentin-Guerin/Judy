#Debut du jour J-5


# Debut du code principal.
label jour5 :
    
    
    scene jardin

    show damedecompagnie at right

    damedecompagnie "Comment vous sentez vous mademoiselle ?"


# Choix 1 -------------------

    menu:
        princesse "..."
        "Donner un avis positif.":
            jump j5_Rep1_choix1

        "Donner un avis négatif.":
            jump j5_Rep2_choix1


# Choix 1 Reponce 1 ...
    label j5_Rep1_choix1:

        princesse "Super je me sens très bien !"
        damedecompagnie "Je suppose que c'est grâce au beau jeune homme de l'organisation."
        jump j5_choix_1_1

# Choix 1 Reponce 2 ...
    label j5_Rep2_choix1:

        princesse "Non je ne me sens pas très bien."
        damedecompagnie "Pourquoi cela ?"
        jump j5_choix_1_2


        
# Choix 1.1 --------------
    label j5_choix_1_1:

    menu:
        princesse "..."
        "Reprendre Susan.":
            jump j5_Rep1_choix1_1

        "Nier les fait.":
            jump j5_Rep2_choix1_1

# Choix 1_1 Reponce 1 ...
    label j5_Rep1_choix1_1:

        princesse "Comment osez-vous dire cela ?!"
        princesse "Je vais bientôt me marier voyons !"
        princesse "Mais effectivement oui..."

        damedecompagnie "Je m'en doutais bien mademoiselle."
        damedecompagnie "J'ai discuté avec lui."

        jump j5_choix1_1_1

# Choix 1_1 Reponce 2 ...
    label j5_Rep2_choix1_1:

        princesse "Non voyons ! Pourquoi dites-vous cela?"
        damedecompagnie "J'étais pourtant sûr qu'il vous intéressait."
        damedecompagnie "OH! A ce propos !"
        damedecompagnie "Je l'ai fait venir."
        damedecompagnie "Je vous laisse avec lui."

        hide damedecompagnie

        jump j5_arrive_orga

# Choix 1.2 -------------
    label j5_choix_1_2:

    menu:
        princesse "..." 
        "Refuser le mariage.":
            jump j5_Rep1_choix1_2

        "Grosse fatigue.":
            jump j5_Rep2_choix1_2


# Choix 1_2 Reponce 1 ...
    label j5_Rep1_choix1_2:

        princesse "Je ne veux pas me marier à cet homme."
        princesse "Je le refuse je ne l'aime pas."
        princesse "C'est seulement par intérêt que je me marie."
        princesse "Je ne suis qu'une marchandise !"

        jump j5_arrive_orga_2


# Choix 1_2 Reponce 2 ...
    label j5_Rep2_choix1_2:

        princesse "J'ai mal dormi je me sens fatiqué."
        damedecompagnie "J'espère que ca vous passera la journée est loin d'être finie."
        
        jump j5_arrive_orga_2


# Choix 1.1.1 --------------

    label j5_choix1_1_1:

        menu:
            princesse "..."
            "En savoir plus.":
                jump j5_Rep1_choix1_1_1

            "Changer de sujet":
                jump j5_Rep2_choix1_1_1

# Choix 1_1_1 Reponce 1 ...
    label j5_Rep1_choix1_1_1:

        princesse "Ah bon? Et qu'a-ttil dit ?"
        damedecompagnie "Ho! Regarder l'organisateur arrive."
        damedecompagnie "Je vous le dirais plus tard."
        damedecompagnie "Je vous laisse !"

        hide damedecompagnie

        jump j5_arrive_orga



# Choix 1_1_1 Reponce 2 ...
    label j5_Rep2_choix1_1_1:
        
        princesse "Passons si vous voulez-bien."
        princesse "Comment se passe les préparatifs. ?."
        damedecompagnie "Regarder l'organisateur arrive."
        damedecompagnie "Je vous laisse voir sa avec lui."

        hide damedecompagnie

# Arrivée de L'orga
    label j5_arrive_orga:

        narrateur "Susan s'en vas..."
        jump j5_choix_2


    label j5_arrive_orga_2:

        damedecompagnie "Ho c'est l'organisateur !" 
        damedecompagnie "Il vient surement vous parler du mariage"
        damedecompagnie "je vais vous laissez."

        hide damedecompagnie

        narrateur "Susan s'en vas..."

        hide damedecompagnie

        jump j5_choix_2

# Choix 2 --------

    label j5_choix_2:

        show orga at right

        orga "Comment allez-vous mademoiselle ?"
        orga "Vous vouliez me voir ?"

    menu:
        princesse "Très bien merci ..."
        "... Ou en sont les préparatifs ?":
            jump j5_Rep1_choix2

        "... Les préparatifs ne vous surchargent pas trop ?":
            jump j5_Rep2_choix2


# Choix 2 Reponce 1 ...
    label j5_Rep1_choix2:
        princesse "Très bien merci. Ou en sont les préparatifs ?"
        orga "Tout avance comme prévu ne vous en faites pas."



# Choix 2 Reponce 2 ...
    label j5_Rep2_choix2:
        princesse "Très bien merci, et vous ? Les préparatifs ne vous surchargent pas trop ?"
        orga "Parfaitement bien merci. Ne vous en faites pas je suis un solide garçon !"

        hide orga


    # Fin de la Journée.
    # J-5
    jump carnetj5
    return
