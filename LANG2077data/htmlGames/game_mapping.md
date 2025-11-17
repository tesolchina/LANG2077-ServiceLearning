# HTML Games Mapping - LANG 2077 Summer 2025

This document maps game links to student groups and individual students based on the CSV data and old links.

## Game to Student/Group Mapping

| Game Name | Group | Students | Game Link | Expected File Path |
|-----------|-------|----------|-----------|-------------------|
| MUSICGAME | Art team 1 | CAO Beiyu, CHEUNG Ka Yi, LIANG Hoi Ki, LO Tsz Yu Georgina | https://gamesbe.asia:3000/GamePlay/MUSICGAME | `Games_backend/upload/MUSICGAME/MUSICGAME.html` |
| Tetris | Art team 2 | BAI Yuchen, LI Mingqing, LI Shuming, WONG Pui Hei | https://gamesbe.asia:3000/GamePlay/Tetris | `Games_backend/upload/Tetris/Tetris.html` |
| droneHTMLgame | Drone | CHEN Cindy, QIN Yangyu | https://gamesbe.asia:3000/GamePlay/droneHTMLgame | `Games_backend/upload/droneHTMLgame/droneHTMLgame.html` |
| SentenceUnscramble | English | LI Mengxi, ZANG Xiaoqi, ZHAO Sijie | https://gamesbe.asia:3000/GamePlay/SentenceUnscramble | `Games_backend/upload/SentenceUnscramble/SentenceUnscramble.html` |
| WordSearch | English | ZANG Xiaoqi | https://gamesbe.asia:3000/GamePlay/WordSearch | `Games_backend/upload/WordSearch/WordSearch.html` |
| PoetryStar | lower- Chinese | LI Xingzhuo, ZENG Qikai, HUANG Shiyao | https://gamesbe.asia:3000/GamePlay/PoetryStar | `Games_backend/upload/PoetryStar/PoetryStar.html` |
| Time_game | Math | MA Ling, SHI Longyu, ZHAO Haoran | https://gamesbe.asia:3000/GamePlay/Time_game | `Games_backend/upload/Time_game/Time_game.html` |
| pingpongskills | PE team 1 | NG Ho Fung, TIAN Ruowen, YANG Shuran | https://gamesbe.asia:3000/GamePlay/pingpongskills | `Games_backend/upload/pingpongskills/pingpongskills.html` |
| PE2_Game_Quiz | PE team 2 | LYU Jingjing, MA Wenbo, ZUO Yue | https://gamesbe.asia:3000/GamePlay/PE2_Game_Quiz | `Games_backend/upload/PE2_Game_Quiz/PE2_Game_Quiz.html` |
| PoetryRecitationGame | upper- Chinese | YUE Xintian, LI Renyanchun, LI Jiahan | https://gamesbe.asia:3000/GamePlay/PoetryRecitationGame | `Games_backend/upload/PoetryRecitationGame/PoetryRecitationGame.html` |

## Export Instructions

### Step 1: Locate HTML Files
HTML files are stored in the backend repository at:
- **Path:** `Games_backend/upload/{GameName}/{GameName}.html`
- **Note:** The `upload/` directory is gitignored, so files may need to be accessed from the server or a local deployment

### Step 2: Export Structure
Create the following folder structure in `LANG2077data/htmlGames/`:
```
htmlGames/
├── Art_team_1/
│   └── MUSICGAME.html
├── Art_team_2/
│   └── Tetris.html
├── Drone/
│   └── droneHTMLgame.html
├── English/
│   ├── SentenceUnscramble.html
│   └── WordSearch.html
├── lower_Chinese/
│   └── PoetryStar.html
├── Math/
│   └── Time_game.html
├── PE_team_1/
│   └── pingpongskills.html
├── PE_team_2/
│   └── PE2_Game_Quiz.html
└── upper_Chinese/
    └── PoetryRecitationGame.html
```

### Step 3: Copy Files
For each game:
1. Locate the HTML file in `Games_backend/upload/{GameName}/`
2. Copy to `LANG2077data/htmlGames/{Group}/{GameName}.html`
3. Ensure file names match the game names exactly (case-sensitive)

## Notes
- Game names are case-sensitive
- Some games may have different file naming conventions
- Verify file existence before copying
- The `upload/` directory may need to be accessed from the production server

