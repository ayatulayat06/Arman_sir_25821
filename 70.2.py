def count_digits(number_str):
    digits_only = [char for char in number_str if char.isdigit()]
    return len(digits_only)

def main():
    try:
        user_input = input("input a number")
        
        if not user_input.strip():
            print("input a number")
            return
        
        temp_str = user_input.strip()
        if temp_str.startswith('-'):
            temp_str = temp_str[1:]
        
        temp_str = temp_str.replace('.', '', 1)
        
        if temp_str.isdigit():
            total_digits = count_digits(user_input)
            print(f"\n{user_input} number has {total_digits} digits")
        else:
            print("input a number")
            
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
