# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("old world mc")
define mc2 = Character("new world mc")


# The game starts here.

label start: 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mcdo

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.


    mc "Fuck, I'm so tired, can't wait to get home."
    show mc happy at right

    "" "I am a bit hungry, though."

    mc "I ultimately decide to grab a quick takeout at Mcdonald's"
    scene bg mcdo

    mc2 "adsasdasdasdsasdasd"

    mc2 "test2"

    mc2 "hey whats up?dasdasdasdaddsadsd"

    # This ends the game.
#     const commitDetailsUrl = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/commits/${commitSha}`;
#   const commitDetails = JSON.parse(UrlFetchApp.fetch(commitDetailsUrl, { headers }).getContentText());
#   const files = commitDetails.files;

#   let content = `📦 **New Commit by ${author}**\n` +
#                 `**Message:** ${message}\n` +
#                 `**Branch:** ${BRANCH}\n` +
#                 `**View Commit:** ${commitUrl}\n\n`;

#   // Loop through changed files
#   for (const file of files) {
#     if (!file.filename.startsWith(FOLDER_PATH)) continue; // only watch your folder
#     if (!file.patch) continue;

#     const filename = file.filename;
#     const patch = file.patch;

#     // Format diff
#     const formattedPatch = patch
#       .split('\n')
#       .map(line => {
#         if (line.startsWith('+')) return '```diff\n+ ' + line.slice(1) + '\n```';
#         else if (line.startsWith('-')) return '```diff\n- ' + line.slice(1) + '\n```';
#         return '';

    return
