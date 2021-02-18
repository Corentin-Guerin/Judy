#Debut du jour J-4


# Debut du code principal.
label jour4 :

    scene chambre
    narrateur "Après votre réveil. Vous sortez de votre chambre."

    scene salon
    show prince at right 
    prince "VICTORIA !"
    prince "Je vous ai vue hier avec l'organisateur du mariage, Vous aviez l'air très heureuse."
    prince "N'oublier pas que vous m'êtes promises !!"

    #choix1 --------------
    menu :
        princesse"..."
        "Lui rentrer dedans.":
            jump reponce_1_c1
        "Lui dire que vous souhaitiez en apprendre plus sur lui .":
            princesse "Je me suis renseigné sur lui et je désirais le connaître."
            jump reponce_2_c1
        "Lui dire que vous vous renseignez sur l'organisation du mariage.":
            jump reponce_3_c1

    #reponce choix1 ----------
    label reponce_1_c1 :
        princesse "Comment osez-vous ? Je ne suis pas votre propriété."
        jump gifle 

    #reponce choix2 ----------
    label reponce_2_c1 :
        prince "Quel affront !!"

        #choix3 --------------
        menu :
            princesse "..."
            "Refuser le mariage." :
                princesse "Je veux que vous le sachiez James... je refuse de me mariez avec vous."
                jump gifle
            "Le reprendre sur son comportement.":
                princesse "Respectez-moi, je ne suis pas un objet."
                jump gifle
            "S'excuser.":
                jump reponce_3_c3

    label reponce_3_c3 :
        
        princesse "Oui veuillez m'excuser"
        prince "Je préfère cela !"
        jump finj4

    #reponce choix3 ----------
    label reponce_3_c1 :
        princesse "Je me renseignais sur l'organisation du mariage."
        prince "Me mentez-vous ?"
        #choix2 --------------
        menu :
            princesse "..."
            "Dire oui.":
                jump reponce_2_c1
            "Dire non.":
                jump reponce_2_c2
    #reponce 2 choix2 ----------
    label reponce_2_c2 :
        princesse "Mais non voyons je n'oserais pas..."
        prince "Les préparatifs du mariage avancent-ils ma chère ?"
        princesse "Oui en effet. L'organisateur m'a affirmé que tout se passait comme prévu."
        prince "Très bien ! Sur ce, je vous laisse, bonne journée."
        jump finj4
    
    # Gifle ---------
    label gifle :
        prince "Quel honte !"

        #-Song de gifle ------------------------------------------------------------------------------------------------------------------
        #play music "sunflower-slow-drag.ogg" fadeout 1
        #---------------------------------------------------------------------------------------------------------------------------------
        narrateur "Le prince vous gifle !"
        princesse "..."
        prince "Reprenez-vous ! Vous serrez ma femme comme convenu."
        narrateur "Le prince s'en va en colère."
        
        hide prince
        jump finj4


    label finj4 :




    # Fin de la Journée.

    # J-4
    jump carnetj4

    return
