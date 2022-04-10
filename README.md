# Restaurant Project
This is a simple restaurant manager project. There are fixed list of restaurant, users and, reviews. Each user can add 
reviews. Also, the project has 2 endpoint for search restaurants.

## Development
- Install docker and docker-compose.
- Run `cp .env.sample .env` and fill `.env` file.
- Run `docker-compose -f docker-compose.dev.yml up --build`. It may take some time (because seeding initial data).
- The service is run under `0.0.0.0:8000` and update after each file changes.

## Deployment
- Install docker and docker-compose.
- Run `cp .env.sample .env` and fill `.env` file.
- Run `docker-compose -f docker-compose.prod.yml up --build`. It may take some time (because seeding initial data).
- The service is run under `yourserverip` or `domain`.

## Rest API Documents
- You can see api documentations under `/swagger` or `/redoc` urls.
- Also, the pdf file `rest_apis_doc.pdf` is in the root of project.

