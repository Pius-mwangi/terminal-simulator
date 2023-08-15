# This is a sample Python script.

def terminal_window():
    user_input = input("pius@hex:$")
    if user_input == "ls":
        print("/first      /second    /third")
    elif user_input == "cd /first" or user_input == "cd first":
        print("pius@hex:first/$")
        print("/one    /two    /three")
    if user_input == "cd /one":
        print("pius@hex:first/one/")
        print("/hello   /mother  /screwer")
    if user_input == "help":
        commands = {"help": "1",   "ls": "2",   "cd": "3", "banner": "4"}
        for command in commands.keys():
            print(command)
        #print("Here is the list of commands:")
    elif user_input == "cd /second":
        print("/four   /five   /six")
    elif user_input == "cd /third":
        print("/seven   /eight    /nine")
    if user_input == "banner":
        banner_text = "TERMINAL SIMULATOR"
        banner_width = len(banner_text) + 4
        banner = f"{'*' * banner_width}\n * {banner_text} *\n{'*' * banner_width}"
        print(banner)

print("type help for all commands")


######################################################





def willno(a):
    while(True):
        terminal_window()

willno("hi")

