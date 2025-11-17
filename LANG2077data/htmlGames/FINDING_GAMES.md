# Finding HTML Game Files

## Current Status

The HTML game files are not currently in the repository. They need to be located and copied to the showcase.

## Search Locations

### 1. Games_backend Directory
Check for an `upload` directory:
- `/Users/simonwang/Documents/Usage/ObSync/Vault4sync/01-Courses/LANG2077/Games_backend/upload/`
- Expected structure: `upload/{GameName}/{GameName}.html`

### 2. Games.hkbu.life Directory
Check for HTML files:
- `/Users/simonwang/Documents/Usage/ObSync/Vault4sync/01-Courses/LANG2077/Games.hkbu.life/`
- Check `public/` directory
- Check `src/` directory for any game files

## Game Names to Search For

1. **MUSICGAME** - Art Team 1
2. **Tetris** - Art Team 2
3. **droneHTMLgame** or **drone** - Drone Team
4. **SentenceUnscramble** or **Sentence** - English Team
5. **WordSearch** or **Word** - English Team
6. **PoetryStar** or **Poetry** - Lower Chinese Team
7. **Time_game** or **Time** - Math Team
8. **pingpongskills** or **pingpong** - PE Team 1
9. **PE2_Game_Quiz** or **PE2** or **PE** - PE Team 2
10. **PoetryRecitationGame** or **Recitation** - Upper Chinese Team

## Search Script

Run the find script to search for files:
```bash
cd /Users/simonwang/Documents/Usage/ObSync/Vault4sync/01-Courses/LANG2077/LANG2077data/htmlGames
chmod +x find_games.sh
./find_games.sh
```

## File Naming Variations

Files may have different naming:
- Case variations: `MUSICGAME.html`, `musicgame.html`, `MusicGame.html`
- Different extensions: `.html`, `.htm`
- In subdirectories matching game names
- May be in zip files or archives

## Once Files Are Found

1. Copy HTML files to: `LANG2077showcase/public/games/`
2. Update `games.json` to set `status: "available"` for found games
3. Test that games load correctly in the showcase

## Expected File Structure

```
LANG2077showcase/public/games/
├── MUSICGAME.html
├── Tetris.html
├── droneHTMLgame.html
├── SentenceUnscramble.html
├── WordSearch.html
├── PoetryStar.html
├── Time_game.html
├── pingpongskills.html
├── PE2_Game_Quiz.html
└── PoetryRecitationGame.html
```



