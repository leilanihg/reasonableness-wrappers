# TODO - Need verbose
from .representation import * 

def test_main(subject, verb, object=None, context=[], phrase_dict=[]):
    # get verb type
    act = get_verb_type(verb, subject, object, context, phrase_dict, False)
    consistent = act.check_constraints()
    return consistent

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

    print("args", args.sentence)
    tree = parse_with_regex(args.sentence)
    (noun, noun_phrase) = get_noun_phrase(tree)
    (verb, object, context, phrase_dict) = get_verbs(tree, args.verbose)
    phrase_dict['noun'] = noun_phrase
    #long_context = phrase_dict['preposition'] 

    # get verb type
    act = get_verb_type(verb, noun, object, context, phrase_dict, args.verbose)
    consistent = act.check_constraints()
    act.print_summary(consistent)
    return consistent

if __name__ == "__main__":
    main()