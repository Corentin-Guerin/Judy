#Debut du jour J-6 


# Debut du code principal.



label jour6 : 

   scene chambre 
   show damedecompagnie at right

#Dialogues  ------------------
   narrateur  "Vous vous faites réveiller par Susan."
   damedecompagnie "Princesse réveillez-vous ! Il est déjà 10h. L'organisateur du mariage a besoin de vous."
   hide damedecompagnie

#choix 1-1 -----------------
   menu:
        princesse "..."
        "Rester sous la couette.":
            jump lazyj6

        "Se réveiller pour rejoindre l'organisateur.":
            jump wakeupj6
   
   label lazyj6 :
      
      princesse"je préfère rester sous la couette pour le moment."

      porte "Toc toc."

      narrateur "L'organisateur du mariage rentre dans la chambre de manière maladroite, les bras remplis de notes et de maques pages colorés."
      
      show orga at right
      orga "Veuillez m'excuser princesse mais je n'ai pas trop de temps, je vais avoir besoin de votre avis pour le mariage."
      hide orga

      narrateur "L'organisateur s'étend vivement sur un long monologue sur des spécificités du mariage."  
      narrateur "Le prince profite de passer par là et que la porte soit ouverte pour intervenir."

      show prince at right
      prince "Comment oses-tu rentrer dans la chambre de ma future femme et  l'importuner avec tes problèmes !"
      hide prince

      show orga at right 
      orga "Excusez-moi monsieur je ne voulais pas..."
      hide orga

      show prince at right 
      prince "Ça m'est égal sortez."   
      hide prince   
   
   menu: 

      princesse "..."
      "Défendre Josh.":
         jump joshj6
      "Soutenir James.":
         jump jamesj6

   label joshj6 :

      princesse "James! Laissez le tranquille il est seulement venu car cet homme avait des questions au sujet du mariage, il souhaite mon avis."
      
      show prince at right
      prince "N'aurait t'il pas pu trouver un meilleur moment pour venir s'occuper de ça ?"
      hide prince

      narrateur "Le prince sort de la chambre d'un air vexer."

      show orga at right
      orga "Dites-moi Victoria, voulez vous vraiment de ce mariage ?"
      
   menu: 
      princesse "..."
      "Acquiescer.":
         jump agreedj6
      "Avouer que vous ne voulez pas vous marier.":
         jump disagreej6
      "Ne pas répondre":
         jump silentj6

   label agreedj6:
      princesse "Oui bien sûr que je le veux..."

      show orga at right 
      orga "Très bien, alors laisser moi vous parler des préparatifs."
      hide orga
      jump finj6

   label disagreej6:
      princesse "Pour être honnête non je ne le veux pas..."
      show orga at right 
      orga "Alors qu'est-ce que vous faites la mademoiselle. Si vous ne l'aimez pas allez-vous-en."
      hide orga
      
      princesse "Je le fais pour ma famille monsieur je n'ai pas le choix."

      jump finj6

   label silentj6: 
      princesse "..."

      show orga at right 
      orga "... Je vois, alors laissez-moi vous parlez des préparatifs."
      hide orga

      jump finj6

   label jamesj6: 
      princesse " Oui c'est inadmissible allez-vous-en !"

      show prince at right
      prince "Venez ma chère nous allons nous promener dans le jardin."
      hide prince

      narrateur "Vous partez avec James faire une longue ballade dans le jardin du château."

      jump finj6

   label wakeupj6 : 
      narrateur "Vous vous réveiller et rejoignez l'organisateur du mariage dans le salon, il occupe la table avec un lourd paquet de notes colorer de nombreux marque pages."

      show orga at right
      orga "Bonjour Princesse, je m'apprêtais à venir vous voir, je me présente je suis Josh je suis ici pour m'occuper de l'organisation de votre mariage."
      hide orga
      narrateur "L’organisateur s’étend sur un long monologue sur des spécificités du mariage. Après quelque minutes le prince arrive dans le salon."

      show prince at right 
      prince "Bonjour princesse, je souhaiterais vous parlez, pourriez-vous me rejoindre ?"
      hide prince
      hide damedecompagnie

   menu:
      princesse "..."
      "Rejoindre le prince.":
         jump followprincej6
      "Ne pas rejoindre le prince.":
         jump dontfollowprincej6
      
   label followprincej6:
      princesse "Je vous suis."

      show prince at right 
      prince "Comment allez-vous ma chère ? moi très bien, je n'ai pas eu l'occasion de vous demandez, avez-vous fait bon voyage ?"
      hide prince

   menu: 
      princesse "..."
      "Acquiescer.":
         jump acquieserj6
      "Ne pas répondre.":
         jump noanswerj6
      
   label acquieserj6:
      princesse "Oui j'ai fait bon voyage et j'ai bien dormi merci d'avoir demandé."

      jump carnetj6

   label noanswerj6:
      narrateur "Vous n'osez pas répondre."

      jump carnetj6

   label dontfollowprincej6:
      
      princesse "Excusez-moi James, je pense que Josh a encore besoin de mon aide."

      jump carnetj6
    # Fin de la Journée.
    # J-6
   label carnetj6: 
   
   return
