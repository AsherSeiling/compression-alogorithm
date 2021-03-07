def regEX(ref, char_comp):
    test_passed = True
    for i in ref:
        if i == char_comp:
            test_passed = False
    return test_passed
