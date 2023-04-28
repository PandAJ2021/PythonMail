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


m1 = Menu_item('m1', children=[Menu_item('m11', children=[Menu_item('m111', function=lambda: print(2))], condition=True),
                               Menu_item('m12', function=lambda: print(2) ,condition=False)], condition=True)


Menu.run_menu(m1)
