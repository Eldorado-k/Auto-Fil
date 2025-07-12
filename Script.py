class script(object):  
    START_TXT = """<b>✨ Bonjour {user}.
 Je suis <i>{bot}.</i> Je suis le cousin de @Marsh_Mello_Bot ✨ moi je suis là pour t'aider à retrouver uniquement tes Dessins animés🇨🇵 (Cartoons) et Manga préféré🎌. il suffit de rejoindre mon groupe de recherche et de taper le nom de ta demande puis tout est fait🤗\n\nPropulsé par <blockquote><a href='t.me/ZFlixTeam'>ZFlix-Team</a></blockquote>... ♻️</b>
"""

    HELP_TXT = "Salut {}\nVoici mon aide."

    ABOUT_TXT = """<b>✯ Mon nom : {}
✯ Développeur: <a href=https://t.me/Kingcey>Kingcey</a>
✯ Bibliothèque: <a href='pyrogram.org>Pyrogram</a>
✯ Base de données: MongoDB
✯ Serveur: <a href='heroku.com'>Heroku</a>
✯ Version : V4.6 (12-05-2025)</b>"""

    SOURCE_TXT = """<b>NOTE :</b>
- Code source disponible ici ◉› :<a href=https://github.com/MrMKN/PROFESSOR-BOT>𝐏𝐑𝐎𝐅𝐄𝐒𝐒𝐎𝐑-𝐁𝐎𝐓</a>

<b>Développeur : <a href=https://t.me/Mr_MKN>ᴍʀ.ᴍᴋɴ ᴛɢ</a></b>"""

    FILE_TXT = """<b>➤ Aide pour le stockage de fichiers</b>

<i>Avec ce module, vous pouvez stocker des fichiers dans ma base de données et je vous fournirai un lien permanent pour y accéder. Pour ajouter des fichiers depuis un canal public, envoyez simplement le lien. Pour un canal privé, vous devez me rendre administrateur.</i>

<b>⪼ Commandes et utilisation :</b>
➪ /link › Répondez à un média pour obtenir son lien 
➪ /batch › Créer un lien pour plusieurs médias

<b>⪼ Exemple :</b>
</code>/batch https://t.me/Maki_TECH/1 https://t.me/Maki_TECH/10</code>"""
  
    FILTER_TXT = "Sélectionnez ce que vous voulez...✨"

    GLOBALFILTER_TXT = """<b>Aide pour les filtres globaux</b>

<i>Les filtres permettent de configurer des réponses automatiques lorsqu'un mot-clé est détecté.</i>

<b>Note :</b>
Réservé aux administrateurs.

<b>Commandes :</b>
• /gfilter › Ajouter un filtre global
• /gfilters › Lister tous les filtres
• /delg › Supprimer un filtre spécifique
• /delallg › Tout supprimer

• /g_filter off › Activer/désactiver dans votre groupe"""

    MANUELFILTER_TXT = """<b>Aide pour les filtres</b>

<i>Configurez des réponses automatiques pour des mots-clés spécifiques.</i>

<b>Note :</b>
1. Nécessite les droits admin
2. Limitée aux admins
3. Boutons limités à 64 caractères

<b>Commandes :</b>
• /filter › Ajouter un filtre
• /filters › Lister les filtres
• /del › Supprimer un filtre
• /delall › Tout supprimer (propriétaire uniquement)

• /g_filter off › Gérer les filtres globaux"""

    BUTTON_TXT = """<b>Aide pour les boutons</b>

<i>Supporte les boutons URL et alertes.</i>

<b>Note :</b>
1. Un contenu est obligatoire
2. Compatible avec tous les médias
3. Format Markdown requis

<b>Boutons URL :</b>
[Texte](buttonurl:lien)

<b>Boutons d'alerte :</b>
[Texte](buttonalert:Message)"""

    AUTOFILTER_TXT = """<b>Aide pour l'auto-filtre</b>

<i>Filtre automatiquement les fichiers des canaux vers les groupes.</i>

• /autofilter on › Activer
• /autofilter off › Désactiver

<b>Autres commandes :</b>
• /set_template › Définir un template IMDb
• /get_template › Voir le template actuel"""

    CONNECTION_TXT = """<b>Aide pour les connexions</b>

<i>Connecte le bot en MP pour gérer les filtres et éviter le spam.</i>

<b>Note :</b>
• Réservé aux admins
• Envoyez /connect pour démarrer

<b>Commandes :</b>
• /connect › Lier un chat à votre MP
• /disconnect › Déconnecter
• /connections › Lister vos connexions
 Réservez au VIP 2nd"""

    ADMIN_TXT = """<b>Aide admin</b>
<i>Module réservé aux administrateurs</i>

<b>Commandes :</b>
• /logs › Voir les erreurs
• /delete › Supprimer un fichier
• /deleteall › Tout supprimer
• /users › Liste des utilisateurs
• /chats › Liste des chats
• /channel › Canaux connectés
• /broadcast › Diffuser un message
• /group_broadcast › Diffuser aux groupes
• /leave › Quitter un chat
• /disable › Désactiver un chat
• /invite › Obtenir un lien d'invitation
• /ban_user › Bannir un utilisateur
• /unban_user › Débannir
• /restart › Redémarrer le bot
• /clear_junk › Nettoyer la base de données
• /clear_junk_group › Nettoyer les groupes inactifs"""

    STATUS_TXT = """<b>◉ Fichiers totaux : <code>{}</code>
◉ Utilisateurs : <code>{}</code>  
◉ Chats : <code>{}</code>
◉ DB utilisée : <code>{}</code>
◉ DB libre : <code>{}</code></b>"""

    LOG_TEXT_G = """<b>#nouveau_groupe

◉ Groupe : {a}
◉ ID : <code>{b}</code>
◉ Lien : @{c}
◉ Membres : <code>{d}</code>
◉ Ajouté par : {e}

◉ Par : @{f}</b>"""
  
    LOG_TEXT_P = """#Nouvel_Utilisateur
    
◉ ID Utilisateur : <code>{}</code>
◉ Nom : {}
◉ Pseudonyme : @{}

◉ Par : @{}</b>"""

    GROUPMANAGER_TXT = """<b>Aide pour la Gestion de Groupe</b>

<i>Fonctionnalités réservées aux administrateurs de groupe</i>

<b>Commandes :</b>
• /inkick - Exclure des membres selon des critères
• /instatus - Voir le statut des membres
• /dkick - Exclure les comptes supprimés
• /ban - Bannir un utilisateur
• /unban - Débannir
• /tban - Bannissement temporaire
• /mute - Rendre muet
• /unmute - Rendre la parole
• /tmute - Muet temporaire (ex: <code>/tmute 2h</code>)
• /pin - Épingler un message
• /unpin - Désépingler
• /purge - Supprimer des messages"""

    EXTRAMOD_TXT = """<b>Modules Extra</b>

<i>Envoyez une image pour la modifier ✨</i>

<b>Commandes :</b>
• /id - Obtenir un ID utilisateur
• /info - Informations utilisateur
• /imdb - Infos film depuis IMDb
• /paste - Coller du texte sur Pasty
• /tts - Texte vers vocal
• /telegraph - Upload media (5MB max)
• /json - Infos techniques message
• /written - Générer un fichier texte
• /carbon - Créer une image Carbon
• /font - Changer la police du texte
• /share - Lien de partage texte
• /song - Rechercher musique YouTube
• /video - Télécharger vidéo YouTube"""

    CREATOR_REQUIRED = "❗<b>Vous devez être le créateur du groupe</b>"
    
    INPUT_REQUIRED = "❗ **Argument requis**"
    
    KICKED = "✔️ {} membres exclus avec succès"
    
    START_KICK = "Nettoyage des membres inactifs en cours..."
    
    ADMIN_REQUIRED = "❗<b>Je ne suis pas admin - merci de me réajouter avec tous les droits</b>"
    
    DKICK = "✔️ {} comptes supprimés exclus"
    
    FETCHING_INFO = "<b>Récupération des informations...</b>"

    SERVER_STATS = """Statistiques Serveur:
  
Uptime : {}
CPU : {}%
RAM : {}%
Stockage total : {}
Utilisé : {} ({}%)
Libre : {}"""
    BUTTON_LOCK_TEXT = "Hé {query}\nCeci n'est pas pour toi. Fais ta propre recherche."

FORCE_SUB_TEXT = "Désolé, vous n'êtes pas abonné à notre chaîne. Merci de cliquer sur le bouton 'Rejoindre' et de réessayer."

WELCOM_TEXT = """Salut {user} 💞

Bienvenue dans {chat}.

Partagez & soutenez, demandez les films que vous souhaitez"""

IMDB_TEMPLATE = """<b> Voici ta Demande: {query}</b>

🏷 Titre: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Année: <a href={url}/releaseinfo>{year}</a>
🌟 Note: <a href={url}/ratings>{rating}</a>/10
🎭 Genre: {genres}"""
   
  
 


   
  
 


