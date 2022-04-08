Koding Challenge
=====================

Welcome to Klue's Koding Challenge. Before getting into details of the problem,
please be aware that the challenge is designed to identify the strongest skills of a software
engineer. As a result, it is an end-to-end problem. It also includes a few optional tasks
you can choose from based on your skills and interests. You may feel the project could use clearer
specifications. You are right, we intentionally defined it vaguely to see how you approach problem solving.
Please document your assumptions, approach and analysis.

You can use any language or framework you are most comfortable with. We expect you to spend **4-8 hours** on the assignment.
Within this time constraint, try to be as ambitious as you can.

Last but not least, please share your feedback on this exercise with us. What was the most enjoyable
and what was annoying? Let us know so we can improve. Good Luck!

Problem Definition
==================

The challenge is to build an API to interact with restaurants and their reviews. There are three entities in the system:
* Restaurants: we don't expect users to add a new restaurant. Assume it is a fixed list from the dataset (more below).
* Reviews: users can add reviews for restaurants.
* Users: make your own assumptions about what users can or cannot do.

We also need search capabilities:
* Given a category (Mexican, Burgers, Gastropubs, etc.), we want to list restaurants in that category sorted by most interesting.
  You can define what "interesting" means.
* Given a keyword, we want to search in reviews for that keyword.

## Optional Tasks

As previously stated, in addition to the API implementation, you can choose to work on one of the tasks below based on your interests and skills:
* We would like a solution that is stable, scalable and maintainable.
* We would like to have some kind of monitoring that helps us in identifying issues.
* We would like to deploy the service to a cloud provider and automate the deployment.

## Dataset

We included a subset of the Yelp reviews dataset from [here](https://www.yelp.com/dataset). Use this dataset to seed your database.

This subset includes 1000 restaurants and their 111632 reviews from 90760 users. The dataset can be found in `data/` folder. You can find
samples from each entity below:

### Restaurants
```json
{
   "business_id":"kXW31NcsNQDT8ZxwJGXEXg",
   "name":"IK2GO",
   "address":"1328 Hornby Street",
   "city":"Vancouver",
   "state":"BC",
   "postal_code":"V6Z 1W5",
   "latitude":49.2770574,
   "longitude":-123.129962,
   "stars":2.5,
   "review_count":5,
   "is_open":0,
   "attributes":{
      "Alcohol":"u'beer_and_wine'",
      "OutdoorSeating":"False",
      "BusinessParking":"{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}",
      "RestaurantsAttire":"'casual'",
      "Ambience":"{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': False}",
      "RestaurantsTakeOut":"True",
      "GoodForKids":"True",
      "NoiseLevel":"'average'",
      "RestaurantsPriceRange2":"1"
   },
   "categories":"Restaurants, Italian, American (New)",
   "hours":{
      "Monday":"8:0-18:0",
      "Tuesday":"8:0-18:0",
      "Wednesday":"8:0-18:0",
      "Thursday":"8:0-18:0",
      "Friday":"8:0-18:0"
   }
}
```

### Reviews
```json
{
   "review_id":"xEfx_P0n7J-WgmHwL8hMxg",
   "user_id":"FjNR5b4pOGRj_JjezCIddg",
   "business_id":"Rbt9i4IDFiIBsau020X_xQ",
   "stars":1.0,
   "useful":0,
   "funny":0,
   "cool":0,
   "text":"My partner and I ordered delivery- the food was over an hour late, one of our items wasn't what we ordered and the food was cold. Disappointed.",
   "date":"2020-10-04 00:34:04"
}
```

### Users
```json
{
   "user_id":"FjNR5b4pOGRj_JjezCIddg",
   "name":"Claire",
   "useful":0,
   "average_stars":1.0,
}
```

Evaluation Criteria
===================

We recognize that the problem can be solved with different degrees of fidelity due to time constraints and your skills.

We expect you to provide:
1. A working solution that returns API results. We have no specific expectations on the quality of the
   returned results, though we expect you to strive for as close to production quality as you can get.
1. Coding practices you would normally follow when writing code that you will have to maintain in a team,
   like good commit logs, regular check-ins, etc.
1. Notes on your goals, thought process, and areas for future work.
