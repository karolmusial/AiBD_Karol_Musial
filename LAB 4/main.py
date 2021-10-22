import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category_id:int)->pd.DataFrame:
    if type(category_id) != int:
        return None

    df = pd.read_sql("SELECT film.title, language.name languge, category.name category FROM category " + 
    "INNER JOIN film_category ON category.category_id = film_category.category_id " + 
    "INNER JOIN film ON film_category.film_id = film.film_id " + 
    "INNER JOIN language ON film.language_id = language.language_id " + 
    "WHERE category.category_id = {a} ".format(a=category_id) + 
    "ORDER BY film.title, language.name;", con=connection)

    return df
    


def number_films_in_category(category_id:int)->pd.DataFrame:

    if type(category_id) != int:
        return None

    df = pd.read_sql("SELECT category.name category, count(category.name) FROM category INNER JOIN film_category ON category.category_id = film_category.category_id " + 
    "INNER JOIN film ON film_category.film_id = film.film_id WHERE category.category_id = {a} GROUP BY category.name;".format(a=category_id), con=connection)

    return df



def number_film_by_length(min_length: Union[int,float] = 0, max_length: Union[int,float] = 1e6 ) :
    if (type(min_length) != int and type(min_length) != float) or (type(max_length) != int and type(max_length) != float):
        return None
    if min_length > max_length:
        return None

    df = pd.read_sql("SELECT film.length length, COUNT(film.length) FROM film WHERE film.length " +
    "BETWEEN '{a}' and '{b}' GROUP BY film.length".format(a=min_length, b=max_length), con=connection)

    return df



def client_from_city(city:str)->pd.DataFrame:
    if type(city) != str:
        return None

    df = pd.read_sql("SELECT city.city, customer.first_name, customer.last_name FROM city INNER JOIN address ON city.city_id = address.city_id " +
                     "INNER JOIN customer ON address.address_id = customer.address_id WHERE city.city = '{a}';".format(a=city), con=connection)

    return df


def avg_amount_by_length(length:Union[int,float])->pd.DataFrame:
    if type(length) != int and type(length) != float:
        return None

    df = pd.read_sql("SELECT film.length, avg(payment.amount) FROM film INNER JOIN inventory ON film.film_id = inventory.film_id "
                     "INNER JOIN rental ON inventory.inventory_id = rental.inventory_id "
                     "INNER JOIN payment ON rental.rental_id = payment.rental_id WHERE film.length = {a} GROUP BY film.length;".format(a=length), con=connection)

    return df



def client_by_sum_length(sum_min:Union[int,float])->pd.DataFrame:
    if type(sum_min) != int and type(sum_min) != float:
        return None

    df = pd.read_sql("SELECT customer.first_name, customer.last_name, SUM(film.length) FROM film " +
                     "INNER JOIN inventory ON film.film_id = inventory.film_id " +
                     "INNER JOIN rental ON inventory.inventory_id = rental.inventory_id " +
                     "INNER JOIN customer ON rental.customer_id = customer.customer_id " +
                     "GROUP BY customer.first_name, customer.last_name " +
                     "HAVING SUM(film.length) >= '{a}' ".format(a=sum_min) +
                     "ORDER BY SUM(film.length), customer.last_name, customer.first_name;", con=connection)

    return df



def category_statistic_length(name:str)->pd.DataFrame:
    if type(name) != str:
        return None

    df = pd.read_sql("SELECT category.name category, AVG(film.length), SUM(film.length), MIN(film.length), MAX(film.length) " +
                     "FROM category INNER JOIN film_category ON category.category_id = film_category.category_id " +
                     "INNER JOIN film ON film_category.film_id = film.film_id WHERE category.name = '{a}' ".format(a=name) +
                     "GROUP BY category.name;", con=connection)

    return df