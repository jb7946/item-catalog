## Item Catalog Project - Udacity Full Stack Web Developer Nanodegree

#### DESCRIPTION
Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

#### INSTALLING

  1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
  2. Install [Python 2.7](https://www.python.org/downloads/release/python-2716/)
  3. Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  4. Inside your cloned repository, launch vagrant (vagrant up).
  5. Once vagrant is running, issue the command `vagrant ssh` to access the vagrant shell.
  6. Change to the vagrant folder `cd /vagrant`
  7. Copy the contents of this repository into folder called `catalog` in your cloned fullstack-nanodegree-vm repository.

#### RUNNING THE PROGRAM
  1. Change to the catalog directory where the contents of this repository were copied from install step 7.
  2. Create the database file using command `python database_setup.py`
  3. Add entries to the database using command `python database_items.py`
  4. Start the web application using command `python application.py`
  5. Open browser to following URL:  `http://localhost:8000`

#### JSON Endpoints

  1. Return all categories of data:
      `http://localhost:8000/category/JSON`
  2. Return all items in category 1 of data:
      `http://localhost:8000/category/1/item/JSON`
  3. Return specific item 1 in category 1 of data:
      `http://localhost:8000/category/1/item/1/JSON`
  4. Return all users:
      `http://localhost:8000/users/JSON`
  5. Return Categories owned by user id 1:
      `http://localhost:8000/user/1/categories/JSON`
