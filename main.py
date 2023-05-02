import user

luke_data= {
    "first_name": "Luke",
    "last_name": "Jech",
    "email" : "Luke@gmail.com",
    "initial_deposit" : 100,
    "int_rate" : .03
}
steve_data= {
    "first_name": "Steve",
    "last_name": "Rogers",
    "email": "that1Captain@hotmail.com",
    "initial_deposit" : 569645,
    "int_rate" : .09
}

luke = user.User(luke_data)

luke.display_user_balance("savings")
luke.make_deposit(250, "savings")
luke.display_user_balance("savings")

luke.add_account("checking", luke_data)
luke.display_user_balance("checking")
luke.make_deposit(50000,"checking")
luke.display_user_balance("checking")
luke.add_account("kitchen_remodel", luke_data)
luke.display_user_balance("kitchen_remodel")

steve = user.User(steve_data)
steve.display_user_balance("savings")
steve.add_account("investments", steve_data)

steve.transfer_money("investments", 250000, luke, "kitchen_remodel")
luke.display_user_balance("kitchen_remodel")
luke.transfer_money("kitchen_remodel", 200000, luke, "savings")
luke.display_user_balance("savings")