# Find the Sum of Unit Digit and Tenth Digit in Given number

n=int(input())

Unit=n%10            # Identify Unit value

Ten=(n//10)%10        # Identify Tenth Value

print("Ten:",Ten)
print("Unit:",Unit)
print("Sum:", Unit+Ten)