from main_module import Main


def main():
    model = Main(input_1=False, input_2=False, time_1='100#MS', time_2='100#MS')
    model.generate()


if __name__ == '__main__':
    main()

