
transform place1_zoom:
    zoom 0.4
transform place2_zoom:
    zoom 0.3
transform place3_zoom:
    zoom 0.2
transform place4_zoom:
    zoom 0.1


screen prince:
    imagemap:
        ground "prince.png"
        if place1 == "prince":
            xpos 300
            ypos 300
            at place1_zoom
        elif place2 == "prince":
            xpos 170
            ypos 0
            at place2_zoom
        elif place3 == "prince":
            xpos 170
            ypos 400
            at place3_zoom
        elif place4 == "prince":
            xpos 170
            ypos 400
            at place4_zoom

screen amant:
    imagemap:
        ground "amant.png"
        if place1 == "amant":
            xpos 300
            ypos 300
            at place1_zoom
        elif place2 == "amant":
            xpos 800
            ypos 150
            at place2_zoom
        elif place3 == "amant":
            xpos 170
            ypos 400
            at place3_zoom
        elif place4 == "amant":
            xpos 170
            ypos 400
            at place4_zoom

screen colere:
    imagemap:
        ground "colere.png"
        if place1 == "colere":
            xpos 300
            ypos 300
            at place1_zoom
        elif place2 == "colere":
            xpos 800
            ypos 150
            at place2_zoom
        elif place3 == "colere":
            xpos 170
            ypos 400
            at place3_zoom
        elif place4 == "colere":
            xpos 170
            ypos 400
            at place4_zoom

screen demence:
    imagemap:
        ground "demence.png"
        if place1 == "demence":
            xpos 300
            ypos 300
            at place1_zoom
        elif place2 == "demence":
            xpos 670
            ypos 200
            at place2_zoom
        elif place3 == "demence":
            xpos 170
            ypos 400
            at place3_zoom
        elif place4 == "demence":
            xpos 170
            ypos 400
            at place4_zoom

screen Terminerj7:
    imagebutton:
        xpos 850
        ypos 600
        idle "terminer.png"
        action [Jump("carnetj7_terminer")]

screen Terminerj6:
    imagebutton:
        xpos 850
        ypos 600
        idle "terminer.png"
        action [Jump("carnetj6_terminer")]

screen Terminerj5:
    imagebutton:
        xpos 850
        ypos 600
        idle "terminer.png"
        action [Jump("carnetj5_terminer")]

screen Terminerj4:
    imagebutton:
        xpos 850
        ypos 600
        idle "terminer.png"
        action [Jump("carnetj4_terminer")]

screen Terminerj3:
    imagebutton:
        xpos 850
        ypos 600
        idle "terminer.png"
        action [Jump("carnetj3_terminer")]

screen Terminerj2:
    imagebutton:
        xpos 850
        ypos 600
        idle "terminer.png"
        action [Jump("carnetj2_terminer")]


