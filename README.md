# code-challenge-Restraunt-ph3


## Yelp-Style Domain - Python Implementation

## Overview

This repository contains a Python implementation for a Yelp-style domain. It consists of three main classes: Review, Restaurant, and Customer. These classes model the relationships between customers, restaurants, and reviews in a Yelp-like system.

## Classes

## Review Class

Attributes:

customer: Represents the customer who wrote the review.
restaurant: Represents the restaurant being reviewed.
rating: Represents the rating given by the customer for the restaurant.
Methods:

get_rating(): Retrieves the rating for the review.
customer: Property to access the customer who wrote the review.
restaurant: Property to access the restaurant being reviewed.
all(): Class method to retrieve all reviews.

## Restaurant Class
Attributes:

name: Represents the name of the restaurant.
Methods:

add_review(review): Adds a review for the restaurant.
get_reviews(): Retrieves all reviews for the restaurant.
get_customers(): Retrieves a list of unique customers who reviewed the restaurant.
average_star_rating(): Calculates the average star rating based on reviews.


## Customer Class
Attributes:

given_name: Represents the given name of the customer.
family_name: Represents the family name of the customer.
Methods:

full_name(): Retrieves the full name of the customer.
restaurants(): Retrieves a list of unique restaurants reviewed by the customer.
add_review(restaurant, review): Adds a review for a specific restaurant by the customer.
num_reviews(): Retrieves the total number of reviews authored by the customer.
find_by_name(name): Class method to find the first customer by full name.
find_all_by_given_name(name): Class method to find all customers with a given name.

## Usage
To use these classes, import them into your Python scripts or interpreter and instantiate objects accordingly.