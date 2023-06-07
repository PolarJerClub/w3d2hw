class Get():
    def __init__(self):
        self.string = ''
        self.get_String()
        self.print_String()
        
    def get_String(self):
        self.string = input("Give me a sentence to capitalize: ")
   
    def print_String(self):
        print(self.string.upper())

obj = Get()
while True:
    ask = input(f"Do you still want to play?")
    if ask.lower() in ('y', 'yes', 'ok'):
        obj.get_String()
        obj.print_String()
    elif ask.lower() in ('n', 'no', 'nok'):
        print('Have a good one')
        break
    else:
        print("That's not a valid response")
