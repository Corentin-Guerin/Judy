#Debut du jour J-3


# Debut du code principal.
label jour3:
    
    scene chambre 
    show damedecompagnie at right

    princesse "Le prince est un idiot !"
    princesse "Je veux partir de cet endroit et rentrer chez moi."
    princesse "Je ne veux pas de ce mariage..."
    
    hide damedecompagnie

    label josharrivej3:

        porte "La porte s'ouvre"
        
        show orga at right

        orga "Je me suis permis de rentrer puisque je vous ai entendu pleurer..."
        orga "Que se passe-t-il?"

#Choix 3.1 ------------------------

        menu:
            princesse "..."
            "Mentir et dire que tout va bien":
                jump mensongej3
            "Demander de l'aide":
                jump aidej3

        label mensongej3: 
            princesse "Tout va bien ne vous en faites pas..."
            orga "Êtes-vous sûre? On dirait vraiment qu'il se passe quelque chose..."

#Choix 3.2 -------------------------           
            menu : 
                princesse "..."
                "Continuer de mentir":
                    hide orga
                    jump bruit_de_pasj3

                "Avouer son malêtre":   
                    jump aidej3
        label aidej3: 

            princesse "Je ne veux pas de ce mariage, le prince est ignoble, je veux juste rentrer chez moi... vous m'aideriez ?"

            orga "Comment pourrais-je vous aider?"

#Choix 3.3 ---------------------------
            menu : 
                princesse "..."
                "Montrer son inquiétude":
                    jump dangerj3

                "Poser une question personnelle":
                    jump question_persoj3

        label dangerj3: 
            
            princesse "Je suis en danger"
            orga "oui je sens bien que quelque chose ne tourne pas rond..."

#Choix 3.4 ---------------------------
            menu : 
                princesse "..."
                "Montrer sa colère":
                    jump meurtrej3

                "Montrer son désespoir":
                    jump suicidej3

        label meurtrej3:
            princesse "A un certain point je serais même capable de le tuer"
            hide orga
            jump bruit_de_pasj3

        label suicidej3:
            princesse "Je veux en finir avec tout ça... Je n'en peux plus..."
            hide orga
            jump bruit_de_pasj3

        label question_persoj3:
            princesse "J'aurais aimé savoir quelque chose, que pensez-vous de moi ?"
            orga "Je dois vous avouez que je vous trouve très charmante... Vous me plaisez Victoria"
            hide orga
            jump bruit_de_pasj3

        label bruit_de_pasj3: 
            narrateur "*bruits de pas qui se rapprochent* le prince vient de rentrer de la chasse, Josh sort vite de la chambre"
            narrateur "Victoria saute sous la couette"
            jump fin_de_journeej3

        label fin_de_journeej3: 


    # Fin de la Journée.
    # J-3
    jump carnetj3
    return
 