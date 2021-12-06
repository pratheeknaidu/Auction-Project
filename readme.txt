-Run the server.py file to set up the server
- Run the client.py file to interact with the server

The project is still in development, and currently it only registers users.

Upcoming Road Map-

Functions on client side:

Common functions:
- login()


admin class (gets triggered by special username and password):
- check_items()
- finance_account()


bidder class:
- place_bid()
- view_items()
- check_bid()

seller class:
- sell_item()
- view_high_bid()

Functions on server side:

-notify()
-store_users()
-items_details()
-show_item() [polymorphed depending on the type of user]
-remove_item()
- start_time()
