
## Backup database locally
backup docker file: docker exec -t firefly_iii_db pg_dump -U firefly -d firefly -b -v -f ./backup.sql

get data out of container: docker cp firefly_iii_db:backup.sql ./backup.sql



## Importing data from gold and plat cards

Gold card and plat have different expense column names, so you can't directly import the plat card using the gold categorize

## Setting up
localhost:80 for app, 81 for data importer

## TODO
1. should be an API call I can make to laod this up directly
2. Better categorize the categories
