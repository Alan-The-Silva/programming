def greet(input):
    if "Hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"

greeting = greet("Hello, computer")
print(greeting)