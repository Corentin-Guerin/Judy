#Debut du jour J-1


# Debut du code principal.
label jour1:

    scene chambre
    show damedecompagnie at right
    princesse "Je ne sais vraiment plus quoi faire..."
    princesse "En plus mon père arrive aujourd'hui, il va forcément être déçu..."
    damedecompagnie "Je sais bien... Cependant c'est l'heure"
    damedecompagnie "il faut qu'on aille dans la salle de réception pour discuter avec Josh des derniers préparatifs"
    hide damedecompagnie
    narrateur "Vous partez donc dans la salle de réception"

    scene chateau #salledemariage
    show pere_neutre at right
    show orga at center
    narrateur "Votre père est en train de discuter avec Josh de l'organisation du mariage"

    menu:
        princesse "..."
        "Rejoindre la discussion":
            jump rejoindrej1

        "Les interrompre et avouer son mépris pour James":
            jump reponsej1

        "Refuser le mariage":
            jump reponse2j1

    label reponsej1:
        princesse "James me répugne, c'est un homme ignoble"
        jump engueulade_perej1

    label reponse2j1:
        princesse "JE REFUSE CE MARIAGE PERE !"
        jump engueulade_perej1

    label engueulade_perej1:

        show pere_enerve at right with dissolve
        hide pere_neutre
        pere_mariee "Comment ça ? Tu te rends compte de tout le cinéma que tu nous fait là?"
        pere_mariee "Ce mariage représente énormément pour nous tous !"
        pere_mariee "Alors tu vas arrêter ton cirque et tu vas te marier avec James ! C'est NON négociable !"
        hide pere_enerve
        narrateur "Le père s'en va énervé"

    menu:
        "Avouer le danger":
            jump dangerjoshj1

        "Demander de l'aide à Josh":
            jump aidejoshj1

    label aidejoshj1:
        princesse "M'aideriez vous m'enfuir de cet endroit ?"
        orga "Oui, je vais le faire mais attendons demain... je vais essayer de trouver une solution"
        jump findejourneej1

    label dangerjoshj1:
        princesse "Aidez moi Josh s'il vous plaît"
        princesse "James est dangereux et violent avec moi..."
        orga "Très bien... Je ne peux pas laisser tout ceci continuer en restant indifférent"
        orga "Nous trouverons une solution demain, je l'espère..."
        jump findejourneej1

    label rejoindrej1:
        princesse "J'arrive à point nommé à ce que je vois, vous parlez de l'organisation du mariage c'est ça?"
        show pere_heureux at right with dissolve 
        hide pere_neutre      
        pere_mariee "en effet, bonjour ma fille, nous parlions du plan de table pour le repas"

    menu:
        princesse "..."
        "Ne rien dire et regarder Josh":
            jump dialogue_perej1

        "cacher sa tristesse":
            jump dialogue_perej1

    label dialogue_perej1:

        show pere_heureux at right with dissolve
        pere_mariee "Es-tu prête pour demain ma fille?"

    menu:
        princesse "..."
        "Mentir":
            jump mensongeperej1
                        
        "Avouer":
            jump avouerperej1
                        
    label mensongeperej1:
        princesse "Oui je suis prête père..."
        jump findejourneej1
                        
    label avouerperej1:
        princesse "Non je ne suis pas prête... Je ne veux pas de ce mariage"
        jump engueulade_perej1

    label findejourneej1:
    # Fin de la Journée.
    # J-1

    return