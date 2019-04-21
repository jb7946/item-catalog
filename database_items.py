from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Item, Base, User

engine = create_engine('sqlite:///myitemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
# Add my info
User1 = User(
    name="John Bitner",
    email="jorshiac@gmail.com")
session.add(User1)
session.commit()


# Add Category 1 for the item catalog project
category1 = Category(
    user_id=1,
    name="Mr Noodles")

session.add(category1)
session.commit()

# Add Item 1 under Catalog 1 for the item catalog project
itemc1i1 = Item(
    user_id=1,
    name="Beef Pho",
    description="Classic Pho with beef.",
    category=category1)

session.add(itemc1i1)
session.commit()

# Add Item 2 under Catalog 1 for the item catalog project
itemc1i2 = Item(
    user_id=1,
    name="Vegan Pho",
    description="Classic Pho with plant based ingredients.",
    category=category1)

session.add(itemc1i2)
session.commit()

itemc1i3 = Item(
    user_id=1,
    name="Eggrolls",
    description="Fried Eggrolls with pork and vegetables.",
    category=category1)

session.add(itemc1i3)
session.commit()


# Add Category 2 for the item catalog project
category2 = Category(
    user_id=1,
    name="Lincoln Steak House")

session.add(category2)
session.commit()

# Add Item 1 under Catalog 2 for the item catalog project
itemc2i1 = Item(
    user_id=1,
    name="Sirloin Steak",
    description="Top Sirloin 16oz with side of your choice.",
    category=category2)

session.add(itemc2i1)
session.commit()

# Add Item 2 under Catalog 2 for the item catalog project
itemc2i2 = Item(
    user_id=1,
    name="Filet Mignon",
    description="Succulent 8oz cut grilled to perfection.",
    category=category2)

session.add(itemc2i2)
session.commit()

# Add Item 3 under Catalog 2 for the item catalog project
itemc2i3 = Item(
    user_id=1,
    name="Rib Eye",
    description="Skillfully cut slice to gobble your hunger.",
    category=category2)

session.add(itemc2i3)
session.commit()


# Add Category 3 for the item catalog project
category3 = Category(
    user_id=1,
    name="Jax Grille")

session.add(category3)
session.commit()

# Add Item 1 under Catalog 3 for the item catalog project
itemc3i1 = Item(
    user_id=1,
    name="Hamburger",
    description="Classic Burger on bun.",
    category=category3)

session.add(itemc3i1)
session.commit()

# Add Item 2 under Catalog 3 for the item catalog project
itemc3i2 = Item(
    user_id=1,
    name="Cheeseburger",
    description="Classic Burger with cheese.",
    category=category3)

session.add(itemc3i2)
session.commit()

# Add Item 3 under Catalog 3 for the item catalog project
itemc3i3 = Item(
    user_id=1,
    name="Basic Salad",
    description="Quick and easy salad.",
    category=category3)

session.add(itemc3i3)
session.commit()

# Add Category 4 for the item catalog project
category4 = Category(
    user_id=1,
    name="Seafood Chest")

session.add(category4)
session.commit()

# Add Item 1 under Catalog 4 for the item catalog project
itemc4i1 = Item(
    user_id=1,
    name="Flounder",
    description="Fresh and cooked to perfection.",
    category=category4)

session.add(itemc4i1)
session.commit()

# Add Item 2 under Catalog 4 for the item catalog project
itemc4i2 = Item(
    user_id=1,
    name="Cod",
    description="Great taste for less.",
    category=category4)

session.add(itemc4i2)
session.commit()

# Add Item 3 under Catalog 4 for the item catalog project
itemc4i3 = Item(
    user_id=1,
    name="Salmon",
    description="Heart Healthy with every bite.",
    category=category4)

session.add(itemc4i3)
session.commit()

# Add Category 5 for the item catalog project
category5 = Category(
    user_id=1,
    name="American Buffet")

session.add(category5)
session.commit()

# Add Item 1 under Catalog 5 for the item catalog project
itemc5i1 = Item(
    user_id=1,
    name="Open Buffet",
    description="Get it all for one price.",
    category=category5)

session.add(itemc5i1)
session.commit()

# Add Item 2 under Catalog 5 for the item catalog project
itemc5i2 = Item(
    user_id=1,
    name="Steak",
    description="A delectable steak.",
    category=category5)

session.add(itemc5i2)
session.commit()

# Add Item 3 under Catalog 5 for the item catalog project
itemc5i3 = Item(
    user_id=1,
    name="Chicken",
    description="A delectable chicken.",
    category=category5)

session.add(itemc5i3)
session.commit()

# Add Category 6 for the item catalog project
category6 = Category(
    user_id=1,
    name="Simple Sandwiches")

session.add(category6)
session.commit()

# Add Item 1 under Catalog 6 for the item catalog project
itemc6i1 = Item(
    user_id=1,
    name="Ham and Cheese",
    description="Just the basics.",
    category=category6)

session.add(itemc6i1)
session.commit()

# Add Item 2 under Catalog 6 for the item catalog project
itemc6i2 = Item(
    user_id=1,
    name="Turkey on Rye",
    description="The meat of champions.",
    category=category6)

session.add(itemc6i2)
session.commit()

# Add Item 3 under Catalog 6 for the item catalog project
itemc6i3 = Item(
    user_id=1,
    name="Pimento and cheese",
    description="Simple and affordable.",
    category=category6)

session.add(itemc6i3)
session.commit()

# Add Category 7 for the item catalog project
category7 = Category(
    user_id=1,
    name="Pizza Plus")

session.add(category7)
session.commit()

# Add Item 1 under Catalog 7 for the item catalog project
itemc7i1 = Item(
    user_id=1,
    name="Cheese Pizza",
    description="Cheesiest of them all.",
    category=category7)

session.add(itemc7i1)
session.commit()

# Add Item 2 under Catalog 7 for the item catalog project
itemc7i2 = Item(
    user_id=1,
    name="Pepperoni Pizza",
    description="Most popular pie.",
    category=category1)

session.add(itemc7i2)
session.commit()

# report completion of database inserts
print "Item Catalog information added to database!"
