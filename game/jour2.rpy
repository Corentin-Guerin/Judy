#Debut du jour J-2


# Debut du code principal.
label jour2 :

    scene chambre
    show damedecompagnie at right

    damedecompagnie "Alors, de quoi avez-vous parlé avec Mr Josh hier ?"

    princesse "Nous avons......"
    
    hide damedecompagnie
    label princearrivej3:

        narrateur "La porte s'ouvre violemment, le prince rentre sans frapper, Susan sort de la chambre"

        show prince at right
        prince "ET VOILA LE TRAVAIL très chère ! Voici mon trophée de chasse"

        menu: 
            princesse "..."
            "S'offusquer":
                jump reponsenuj2

            "L'engueuler":
                jump reponsecriej2

        label reponsenuj2: 
            princesse "Comment osez-vous rentrer sans frapper ? Et si j'avais été nu ?"
            hide prince
            show prince_heureux at right
            prince "HAHA j'en aurais profité ! Par contre, veuillez me parler sur un autre ton, je suis votre futur mari et futur roi"
            jump question2j2

        label reponsecriej2:
            princesse "SORTEZ TOUT DE SUITE! OH! C'EST IMMONDE"
            prince "Comment osez-vous me parler sur ce ton ? Je suis votre futur mari et futur Roi"
            jump question2j2

        label question2j2:
            hide prince_heureux
            show prince at right
            menu:
                princesse "..."
                "S'excuser":
                    jump excusej2
                "Lui demander de sortir":
                    jump princessecriej2

        label princessecriej2:
            princesse "SORTEZ !"
            jump princesortj2
            
        label excusej2:
            princesse "Veuillez m'excuser mais je déteste la chasse... la vue du sang me répugne"
            prince "Eh bien il faut vous y habituer ! C'est une de mes passions, vous devrez même m'accompagner à l'occasion !"

            menu:
                princesse "..."
                "Refuser":
                    jump princeoffusquej2
                "Accepter":
                    jump princepreferej2
    
        label princeoffusquej2:
            princesse "C'est hors de question, jamais je ne participerais à une telle barbarie"
            hide prince
            show prince_heureux at right
            prince "Vous pensez vraiment avoir le choix ?"
            jump princesortj2
        
        label princepreferej2:
            princesse "D'accord..."
            prince "Je préfère ça."
            jump princesortj2

        label princesortj2:
            hide prince
            hide prince_heureux
            narrateur "Le prince sort de la chambre en claquant la porte"
            jump fin_de_journeej2

        label fin_de_journeej2:

    # Fin de la Journée.
    # J-2
    jump carnetj1
    return
