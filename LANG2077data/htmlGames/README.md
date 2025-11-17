# HTML Games Export - LANG 2077 Summer 2025

This folder contains instructions and tools for exporting HTML educational games created by students.

## Contents

- `instructions.md` - Original instructions for the export process
- `oldLinks.md` - List of game links from the old system
- `LANG 2077 summer 2025 - Sheet1.csv` - Student data with game assignments
- `game_mapping.md` - Complete mapping of games to students and groups
- `extract_games.js` - Node.js script to extract and map games
- `export_games.sh` - Bash script to export HTML files from backend

## Quick Start

### Option 1: Using the Export Script (Recommended)

1. Ensure you have access to `Games_backend/upload/` directory
2. Run the export script:
   ```bash
   cd /Users/simonwang/Documents/Usage/ObSync/Vault4sync/01-Courses/LANG2077/LANG2077data/htmlGames
   chmod +x export_games.sh
   ./export_games.sh
   ```

### Option 2: Manual Export

1. Refer to `game_mapping.md` for the complete list of games and their locations
2. Copy HTML files from `Games_backend/upload/{GameName}/{GameName}.html`
3. Place them in the appropriate group folder:
   - `Art_team_1/` - MUSICGAME.html
   - `Art_team_2/` - Tetris.html
   - `Drone/` - droneHTMLgame.html
   - `English/` - SentenceUnscramble.html, WordSearch.html
   - `lower_Chinese/` - PoetryStar.html
   - `Math/` - Time_game.html
   - `PE_team_1/` - pingpongskills.html
   - `PE_team_2/` - PE2_Game_Quiz.html
   - `upper_Chinese/` - PoetryRecitationGame.html

## Game List

Total: 10 games

1. **MUSICGAME** - Art team 1
2. **Tetris** - Art team 2
3. **droneHTMLgame** - Drone team
4. **SentenceUnscramble** - English team
5. **WordSearch** - English team
6. **PoetryStar** - lower- Chinese team
7. **Time_game** - Math team
8. **pingpongskills** - PE team 1
9. **PE2_Game_Quiz** - PE team 2
10. **PoetryRecitationGame** - upper- Chinese team

## Notes

- HTML files are stored in `Games_backend/upload/` which is gitignored
- Files may need to be accessed from the production server
- Game names are case-sensitive
- See `game_mapping.md` for detailed student assignments

