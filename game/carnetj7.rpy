

label carnetj7 :
    show carnet
    princesse "Il est temps d'ouvrir mon carnet !"


    if amour<=5 and amour<=colere :
        $place1 = "prince"
        show screen prince
    elif amour<5 and amour>=colere :
        $place1 = "demence"
        show screen demence
    elif amour>5 and amour<=colere :
        $place1 = "amant"
        show screen amant 
    elif amour>5 and amour>=colere :
        $place1 = "colere"
        show screen colere
    
    if amour<=5 and amour<=colere :
        $place2 = "demence"
        show screen demence
    elif amour<5 and amour>=colere :
        $place2 = "prince"
        show screen prince
    elif amour>5 and amour>=colere :
        $place2 = "colere"
        show screen colere 
    elif amour>5 and amour<=colere :
        $place2 = "amant"
        show screen amant

    call screen Terminerj7

    label carnetj7_terminer :
        princesse "Super J'AI FINI  ."
    
    jump jour6