
def run_chatbot():
    print("Hello! Welcome to our customer service. I can help you with returns or exchanges.")
    
    while True:
        intent = input("Are you looking to (return) an item or (exchange) an item? Please type 'return' or 'exchange': ").lower().strip()
        if intent == "return" or "exchange":
            break
        else:
            print("I'm sorry, I didn't understand that. Please type 'return' or 'exchange'.")

    order_number = input("Please provide your order number: ").strip()
    items = input(f"Which item(s) would you like to {intent}? (e.g., 'Blue T-shirt, Size M'): ")
    reason = input(f"What is the reason for the {intent}? ")

    print(f"\n--- {intent} Request Summary ---")
    print("Order Number: {}".format(order_number))
    print("Item(s): {}".format(items))
    print("Reason: {}".format(reason))


    print("\nThank you for providing the information. We are now initiating your {} process.".format(intent))
    print("A customer service representative may contact you if more details are needed.")
    print("Have a great day!")

if __name__ == '__main__':
    run_chatbot()
