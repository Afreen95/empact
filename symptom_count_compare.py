# Author: David Senter
# Given a list of symptom context variables, generates the minimum comparisons
# needed to determine if they exceed the given threshold count (5 in this case).
# Necessary because Watson Assistant apparently can't maintain a count variable.

def symptom_count_compare(*argv):
    threshold = argv[0]
    start = argv[1:len(argv)]
    set_start = frozenset(start)
    result = set([])
    for item1 in set_start:
        for item2 in set_start:
            for item3 in set_start:
                for item4 in set_start:
                    for item5 in set_start:
                        test_list = [item1, item2, item3, item4, item5]
                        test_set = frozenset(test_list)
                        if len(test_set) == 5 and not (test_set in result):
                            result.add(test_set)
    count2 = 1
    for thing in result:
        result_string = str(count2) + " "
        counter = 0
        for issue in thing:
            if counter < 4:
                result_string += issue + " == true && "
            else:
                result_string += issue + " == true"
            counter += 1
        print result_string
        count2 += 1

symptom_count_compare(5, "$thoughts", "$digestion", "$emotions", "$frustration", "$interests", "$pain", "$sleeping")
