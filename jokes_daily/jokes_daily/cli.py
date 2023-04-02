import argparse
import jokes as j


def main():
    # create an instance of the ArgumentParser class
    parser = argparse.ArgumentParser(description='A CLI for joke_daily')

    # add arguments to the parser
    parser.add_argument('--single', '-s', type=bool, default=False, help='Type of Joke Single or Twopart [default: False]')

    # parse the arguments
    args = parser.parse_args()
    joke = j.get_joke(args.single)
    response = j.parse_joke(joke=joke)
    print(response)


if __name__ == "__main__":
    main()