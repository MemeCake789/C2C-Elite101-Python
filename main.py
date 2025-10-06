def main():
    print("=" * 50)
    print("Welcome to the Chatbot!")
    print("=" * 50)
    
    name = input("\nWhat is your name? ")
    age = input("What is your age? ")
    
    print(f"\nHello {name}! Nice to meet you.")
    print(f"How can I help you today?\n")
    
    while True:
        print("\n" + "=" * 50)
        print("MENU OPTIONS")
        print("=" * 50)
        print("1. Option 1 (Placeholder)")
        print("2. Option 2 (Placeholder)")
        print("3. Option 3 (Placeholder)")
        print("4. Exit")
        
        choice = input("\nPlease select an option (1-4): ")
        
        if choice == "1":
            print("\nYou selected Option 1.")
        elif choice == "2":
            print("\nYou selected Option 2.")
        elif choice == "3":
            print("\nYou selected Option 3.")
        elif choice == "4":
            print(f"\nThank you for chatting with me, {name}! Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
