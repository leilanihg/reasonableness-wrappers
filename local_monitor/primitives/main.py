# TODO - Need verbose
from .representation import * 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence', nargs='+',
                    help='Sentence')
    parser.add_argument("-d", "--debug", action='store_true',
                        help='print debug messages to stderr')
    parser.add_argument("-v", "--verbose", action='store_true',
                        help='This is the same as debug right now')
    args = parser.parse_args()


    if args.debug:
        log.basicConfig(format="%(levelname)s: %(message)s",
                        level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")
    if args.verbose:
        print("INFO: Verbose OUTPUT\n")

    tree = parse_with_regex(args.sentence)
    (noun, noun_phrase) = get_noun_phrase(tree)
    (verb, object, context, phrase_dict) = get_verbs(tree, args.verbose)
    phrase_dict['noun'] = noun_phrase
    #long_context = phrase_dict['preposition'] 

    # get verb type
    act = get_verb_type(verb, noun, object, context, phrase_dict, args.verbose)
    consistent = act.check_constraints()
    act.print_summary(consistent)
if __name__ == "__main__":
    main()