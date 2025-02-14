# March Madness Kaggle Competition

## Overview
This project contains my work for the March Madness Kaggle competition. The datasets are divided into several sections, each providing different types of information.

## Data Sections

### Data Section 1 - The Basics
This section provides everything you need to build a simple prediction model and submit predictions.

- **MTeams.csv and WTeams.csv**: Identifies the different college teams.
- **MSeasons.csv and WSeasons.csv**: Identifies the different seasons included in the historical data.
- **MNCAATourneySeeds.csv and WNCAATourneySeeds.csv**: Identifies the seeds for all teams in each NCAA® tournament.
- **MRegularSeasonCompactResults.csv and WRegularSeasonCompactResults.csv**: Game-by-game results for regular seasons.
- **MNCAATourneyCompactResults.csv and WNCAATourneyCompactResults.csv**: Game-by-game NCAA® tournament results.
- **SampleSubmissionStage1.csv**: Example submission file for stage 1.

### Data Section 2 - Team Box Scores
Provides game-by-game stats at a team level for all regular season, conference tournament, and NCAA® tournament games.

- **MRegularSeasonDetailedResults.csv and WRegularSeasonDetailedResults.csv**: Team-level box scores for regular seasons.
- **MNCAATourneyDetailedResults.csv and WNCAATourneyDetailedResults.csv**: Team-level box scores for NCAA® tournaments.

### Data Section 3 - Geography
Provides city locations of all regular season, conference tournament, and NCAA® tournament games.

- **Cities.csv**: Master list of cities that have been locations for games played.
- **MGameCities.csv and WGameCities.csv**: Identifies all games along with the city that the game was played in.

### Data Section 4 - Public Rankings
Provides weekly team rankings for dozens of top rating systems since the 2003 season.

- **MMasseyOrdinals.csv**: Lists ordinal rankings of men's teams under different ranking system methodologies.

### Data Section 5 - Supplements
Contains additional supporting information, including coaches, conference affiliations, alternative team name spellings, bracket structure, and game results for NIT and other postseason tournaments.

- **MTeamCoaches.csv**: Indicates the head coach for each team in each season.
- **Conferences.csv**: Indicates the Division I conferences that have existed over the years.
- **MTeamConferences.csv and WTeamConferences.csv**: Indicates the conference affiliations for each team during each season.
- **MConferenceTourneyGames.csv and WConferenceTourneyGames.csv**: Indicates which games were part of each year's post-season conference tournaments.
- **MSecondaryTourneyTeams.csv and WSecondaryTourneyTeams.csv**: Identifies the teams that participated in post-season tournaments other than the NCAA® Tournament.
- **MSecondaryTourneyCompactResults.csv and WSecondaryTourneyCompactResults.csv**: Indicates the final scores for the tournament games of "secondary" post-season tournaments.
- **MTeamSpellings.csv and WTeamSpellings.csv**: Indicates alternative spellings of many team names.
- **MNCAATourneySlots.csv and WNCAATourneySlots.csv**: Identifies the mechanism by which teams are paired against each other in the tournament.
- **MNCAATourneySeedRoundSlots.csv**: Represents the men's bracket structure in any given year.

## Notes
- When identifying a particular season, we reference the year that the season ends in, not the year that it starts in.
- The men's team IDs range from 1000-1999, whereas all of the women's team IDs range from 3000-3999.

## Getting Started
1. **Load the Data**: Use the provided scripts to load and preprocess the data.
2. **Exploratory Data Analysis (EDA)**: Perform EDA to understand the data and identify important features.
3. **Feature Engineering**: Create new features that might help improve model performance.
4. **Model Training**: Train and evaluate different models to make predictions.
5. **Submission**: Generate predictions and submit them to Kaggle.