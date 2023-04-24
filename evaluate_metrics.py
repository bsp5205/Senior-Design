# File contains the functions that evaluate an assignments metrics from 0 to 100
# To calculate how poor the assignments are we use a mix of percent error

# Object-Oriented Metrics
def mcgabe_cc(result, weight, SLOC):
    if weight == 0:
        return 100

    # where this equation is found
    # https://homepages.cwi.nl/~landman/docs/Landman2014-ccsloc-icsme2014-preprint.pdf
    median_complexity = .88 + (.16 * SLOC)
    target_complexity = median_complexity * (2 - (weight/100))

    # if the cc is lower than the desired the assignment is all good
    if result < target_complexity:
        return 100
    else:
        result = 100 * ((result - target_complexity) / target_complexity)
        return round(100 - result) if result < 100 else 0


def comment_percentage(result, weight):
    if weight == 0:
        return 100

    # based on the weight the upper/lower limit is decided
    percent_error = 0
    upper_limit = 30 + 30 * (1 - (weight/100))
    lower_limit = 30 - 30 * (1 - (weight/100))
    if result > upper_limit:
        # if the result it higher than the upper limit return percent error
        percent_error = 100 * ((upper_limit - result) / upper_limit)
    elif result < lower_limit:
        # if the result it lower than the lower limit return percent error
        percent_error = 100 * ((lower_limit - result) / lower_limit)
    else:
        # if the result is within the limit return 1
        return 100

    # in the future the sign will let us return if the CP is too high or too low
    # for now return 1 - absolute value
    return round(100 - abs(percent_error)) if abs(percent_error) < 100 else 0


def wmc(cc_evaluates):
    # return average of cc
    # If want worst cc for analysis look into cc_evaluates
    return round(sum(cc_evaluates) / len(cc_evaluates))


def cbo_dit(result, weight):
    if weight == 0:
        return 100
    # we want cbo to be as low as possible change the complexity based off weight
    # this is because the coupling in student assignments should not be too complexed
    # cbo and dit have almost identical desired values (2-4)
    # use this method for both for now
    desired = round(3 * (1.5 - (weight/100)))
    percent_error = 100 * ((result - desired) / desired)

    # too strong divide by 2
    percent_error /= 2
    if percent_error < 0:
        percent_error = 0
    return round(100 - percent_error) if percent_error < 100 else 0


# Mood Metrics
# Where I get them
# https://www.aivosto.com/project/help/pm-oo-mood.html
def mood_MHF(result, weight):
    result = result * 100
    if weight == 0:
        return 100
    percent_error = 0
    upper_limit = 25 + 25 * (1 - (weight / 100))
    lower_limit = 8 - 8 * (1 - (weight / 100))

    if result > upper_limit:
        # if the result it higher than the upper limit return percent error
        percent_error = 100 * ((upper_limit - result) / upper_limit)
    elif result < lower_limit:
        # if the result it lower than the lower limit return percent error
        percent_error = 100 * ((lower_limit - result) / lower_limit)
    else:
        # if the result is within the limit return 1
        return 100

    # in the future the sign will let us return if the CP is too high or too low
    # for now return 1 - absolute value
    return round(100 - abs(percent_error)) if abs(percent_error) < 100 else 0



def mood_AHF(result, weight):
    if weight == 0:
        return 100
    # all attributes should be hidden weight effects % error alone
    percent_error = 100 * ((1 - result) / 1)
    return round(100 - (percent_error * (2 * weight/100)))


def mood_MIF(result, weight):
    result = result * 100
    if weight == 0:
        return 100
    # Just make sure it is not extreme in either direction
    percent_error = 0
    upper_limit = 80 + 80 * (1 - (weight / 100))
    lower_limit = 20 - 20 * (1 - (weight / 100))

    if result > upper_limit:
        # if the result it higher than the upper limit return percent error
        percent_error = 100 * ((upper_limit - result) / upper_limit)
    elif result < lower_limit:
        # if the result it lower than the lower limit return percent error
        percent_error = 100 * ((lower_limit - result) / lower_limit)
    else:
        # if the result is within the limit return 1
        return 100

    # in the future the sign will let us return if the CP is too high or too low
    # for now return 1 - absolute value
    return round(100 - abs(percent_error)) if abs(percent_error) < 100 else 0

def mood_AIF(result, weight):
    if weight == 0:
        return 100
    # attribute inheritance should be less than 50% <-- very lenient
    limit = 48 + 24 * (.5 - (weight / 100))
    if result < limit:
        return 100
    percent_error = 100 * ((limit - result) / limit)
    return round(100 - percent_error) if percent_error < 100 else 0


def mood_CF(result, weight):
    if weight == 0:
        return 100
    # coupling factor should be less than 12%
    limit = 12 + 24 * (1 - (weight / 100))
    if result < limit:
        return 100
    percent_error = 100 * ((limit - result) / limit)
    return round(100 - percent_error) if percent_error < 100 else 0



def mood_PF(result, weight):
    if weight == 0:
        return 100
    # higher is more complex
    # complexity does not factor into quality for polynomial factor
    # return 100 until changes?
    # maybe change if we describe in the "help" section
    else:
        return 100

def sloc(result, weight):
    if weight == 0:
        return 100
    percent_error = 0
    upper_limit = 80 + 80 * (1 - (weight / 100))
    lower_limit = 20 - 20 * (1 - (weight / 100))

    if result > upper_limit:
        # if the result it higher than the upper limit return percent error
        percent_error = 100 * ((upper_limit - result) / upper_limit)
    elif result < lower_limit:
        # if the result it lower than the lower limit return percent error
        percent_error = 100 * ((lower_limit - result) / lower_limit)
    else:
        # if the result is within the limit return 1
        return 100
    return round(100 - abs(percent_error)) if abs(percent_error) < 100 else 0


def main():
    # test of the functions
    print("CP Result: ", comment_percentage(2, 50))
    print("CC Result: ", mcgabe_cc(26, 50, 100))
    print("CBO/DIT Result:", cbo_dit(4, 100))
    print("--Mood Results--")
    print("MHF: ", mood_MHF(50, 50))
    print("AHF: ", mood_AHF(90, 50))
    print("MIF: ", mood_MIF(50, 50))
    print("AIF: ", mood_AIF(50, 50))
    print("CF: ", mood_CF(50, 50))
    print("PF: ", mood_PF(50, 50))




if __name__ == "__main__":
    main()
