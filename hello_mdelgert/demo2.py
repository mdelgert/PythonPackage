import argparse

def main():
    parser = argparse.ArgumentParser(description='Description of your program')

    # Add a command with its own set of arguments
    subparsers = parser.add_subparsers(title='subcommands', dest='command')

    # Define a 'foo' command
    name_parser = subparsers.add_parser('name', help='Description of the foo command')
    name_parser.add_argument('name_arg', help='Description of the foo argument')

    args = parser.parse_args()

    # Access the arguments
    if args.command == 'name':
        print("hello " + args.name_arg)

if __name__ == "__main__":
	main()