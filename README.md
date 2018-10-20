[![Build Status](https://travis-ci.com/scott-kenya/Api-store-manager.svg?branch=develop)](https://travis-ci.com/scott-kenya/Api-store-manager)


Configuration of Project Environment
*************************************

This is an API that manages the store(myStore) using Python3, Flask, and Flask_restful

Overview on How to Run this API
================================
1. Either install a Python IDE or create a Python virtual environment to install the packages required
2. Install packages required
3. Install Postman extension in Chrome 

Setup procedure
================

A. Configure project environment (Create a Virtual Environment)
------------------------------------------------------------------------------------------------

1. Create a Python Virtual Environment
    - Install virtualenv::

        sudo pip install virtualenv

    - Create virtialenv::

        virtualenv -p python3 <name of virtualenv>

    - Install requirements::

        pip install -r requirements.txt


B. Run app.py
---------------

    python app.py

C. Refer to app/api/v1/__init__.py on how to test the code 
---------------------------------------------------------------------------

Endpoints of the Teacher API
============================
1.Admin can add a product
2.Admin/store attendant can get all products
3.Admin/store attendant can get a specific product
4.Store attendant can add a sale order
5.Admin can get all sale order records
6.Admin can get sale order by id
7.Admin can delete sale order
8.Admin can delete product


Documentation
============================
