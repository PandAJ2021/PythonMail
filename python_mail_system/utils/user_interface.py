from os import system as terminal, name as os_name


def clear():
    terminal("cls" if os_name.lower() == "nt" else "clear")


class Menu_item:

    def __init__(self, name, function=lambda: True, children=None, condition=None):
        self.name = name
        self.parent = None
        self.children = children
        self.condition = condition
        self.function = function
        self.set_parent()

    def set_parent(self):
        if children := self.children:
            for child in children:
                child.parent = self


class Menu:

    @staticmethod
    def run_menu(option=Menu_item):
        if option.children and option.condition:
            children = [child for child in option.children]
            clear()
            print(f"======== {option.name} ========")
            for child in children:
                print(f'\n{children.index(child)+1}) {child.name}')
            print(
                f'\n0) ' + ('Exit' if not option.parent else f'Back to {option.parent.name}'))

            index = int(input('\nchoose a number: '))
            if index:  # if index is not 0 run the child
                Menu.run_menu(children[index - 1])

            elif option.parent:  # if index is 0 run parent
                Menu.run_menu(option.parent)
            else:
                exit()
        else:
            option.function()


routers = Menu_item('Login or Register',condition =True ,  children = [
    Menu_item('Sign up' ,condition= True , ),
    Menu_item('Sign in' , condition= True , children=[
        Menu_item('User Panel' , condition= True , children=[
            Menu_item('Send massage'),
            Menu_item('Sent box'),
            Menu_item('inbox'),
            Menu_item('Draft'),
        ]) , 
        Menu_item('Logout')]),])


Menu.run_menu(routers)