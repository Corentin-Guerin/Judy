#Debut du jour J-7 


# Debut du code principal.
label jour7 :

    scene chambre

    show lettre at right

    bellemere "Bonjour Victoria. j'espere que tu vas bien."
    bellemere "Ce mariage est extrêmement important, l'avenir de la famille repose sur tes épaules."
    bellemere "En tant que future princesse, tu te dois d'être parfaite pour le mariage."
    bellemere "Il aura lieu dans 7 jours, ne l'oublie pas."
    bellemere "Tu devrais croiser Suaan, elle est ta nouvelle servante."
    bellemere "Elle devrais te pla..."

    show damedecompagnie 

    damedecompagnie "Bonsoir madame."
    damedecompagnie "Je m'appel Susan je suis votre servante."
    damedecompagnie "Vous pouvez me demandez ce que vous voulez, je suis à votre entière disposition."

    princesse " euh.. Merci Susan."

    

    bellemere "Bon je te laisse te familiariser avec ton nouvelle environnement."
    bellemere "Passe une bonne Journée! Au-revoir."

    hide lettre
    hide damedecompagnie
    show damedecompagnie at right

# Choix 1.1 -------------------
    label decouvert :

    menu:
        princesse "..."
        "Sortir de la chambre.":
            jump j7_visite

        "Rester dans la chambre. ":
            jump j7_chambre

    label j7_visite:

        princesse " Je vais visiter le chateau."
        damedecompagnie "Avec un peut de chance vous allez rencontrer le prince."
        damedecompagnie "Bonne route !"

        hide damedecompagnie

        scene salon

        narrateur "Vous croisez le Prince..."

        show prince at right

        prince "Bonsoir princesse Victoria."
        prince "Il me tardait de vous rencontrez, je souhaitais faire votre connaissance au plus vite."
        prince "J’ai entendu de nombreuses qualités à votre sujet."

        jump j7_Questionduprinces


    label j7_chambre:
        princesse "je vais rester ici pour le moment."


        damedecompagnie "Avez-vous besoin de quelque chose?."

# Choix 1.2 -------------------

    menu:

        princesse "..."
        "Evoquer des doutes au sujet du mariage.":
            jump j7_seconfier_oui

        "Très bien merci, vous pouvez disposer !":
            jump j7_seconfier_non

    label j7_seconfier_oui:
               
        princesse "Je ne suis pas rassu..."

        hide damedecompagnie

    label j7_seconfier_non:
          
        damedecompagnie "Bonne soirée Madame ! Appelez moi au besoin."
        hide bellemere
        hide damedecompagnie

    label j7_dialogueSusan_done:

        porte "Toc Toc ..."
    
        show prince at right

        prince "Bonsoir Princesse Victoria !"
        prince "Il me tardait de vous rencontrez, je souhaitais faire votre connaissance au plus vite."
        prince "j’ai entendu de nombreuses qualités à votre sujet."

    label j7_Questionduprinces:
# Choix 2 -------------------
    menu:

        princesse "..."
        "Rester poli.":
            jump j7_poli

        "Ne pas lui repondre.":
            $ colere += 1
            jump j7_pasRepondre

        "Cacher son enthousiasme.":
            jump j7_non
    
    # Rep 1 -------------   
    label j7_poli:

        show prince heureux at right with dissolve
         
        princesse "Enchanté de faire votre connaisance Prince James."
        jump j7_dialogue_princej7

    # Rep 2  -------------          
    label j7_pasRepondre :

        princesse "..."
        princesse "..."

        show prince triste at right with dissolve

        prince "Vous ne m'avez pas l'air très bavarde."
        prince "Cepandant vous êtes magnifique."
        princesse "Mer.. Merci."
        jump j7_dialogue_princej7

    # Rep 3 -------------  
    label j7_non :
        princesse "Je .."
        princesse "euh.."
        princesse "Enchanté."
        jump j7_dialogue_princej7
    

# Dialogue de fin ------------
    label j7_dialogue_princej7 :
        prince "Tout le plaisir est pour moi, bonne soirée Victoria."



    # Fin de la Journée.
    # J-7
    jump carnetj7 

    return
