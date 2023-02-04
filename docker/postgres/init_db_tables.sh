#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE TABLE IF NOT EXISTS public.raw_transfers (
    player_id INT NOT NULL,
    transfer_date TIMESTAMP NOT NULL,
    name VARCHAR NULL,
    position VARCHAR NULL,
    age SMALLINT NULL,
    portrait_url VARCHAR NULL,
    nationalities JSON NULL,
    left_club_url VARCHAR NULL,
    left_club_name VARCHAR NULL,
    left_club_name_alt VARCHAR NULL,
    left_club_league_country_url VARCHAR NULL,
    left_club_league_country_name VARCHAR NULL,
    left_club_league_name VARCHAR NULL,
    left_club_league_name_alt VARCHAR NULL,
    join_club_url VARCHAR NULL,
    join_club_name VARCHAR NULL,
    join_club_name_alt VARCHAR NULL,
    join_club_league_country_url VARCHAR NULL,
    join_club_league_country_name VARCHAR NULL,
    join_club_league_name VARCHAR NULL,
    join_club_league_name_alt VARCHAR NULL,
    market_value VARCHAR NULL,
    fee VARCHAR NULL,
    loan_fee VARCHAR NULL,
    transfer_url VARCHAR NULL
  );
EOSQL