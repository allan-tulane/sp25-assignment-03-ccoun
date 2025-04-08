import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, memo=None):
    # TODO -  implement top-down memoization
    if memo is None:
        memo = {}
    if (S, T) in memo:
        return memo[(S, T)]

    if not S:
        return len(T)
    if not T:
        return len(S)

    if S[0] == T[0]:
        memo[(S, T)] = fast_MED(S[1:], T[1:], memo)
    else:
        insert = fast_MED(S, T[1:], memo) + 1
        delete = fast_MED(S[1:], T, memo) + 1
        memo[(S, T)] = min(insert, delete)

    return memo[(S, T)]


def fast_align_MED(S, T, memo=None):
    if memo is None:
        memo = {}

    if (S, T) in memo:
        return memo[(S, T)][1:]  # return only alignments

    if S == "":
        result = (len(T), "-" * len(T), T)
    elif T == "":
        result = (len(S), S, "-" * len(S))
    elif S[0] == T[0]:
        dist, align_S, align_T = fast_align_MED(S[1:], T[1:], memo)
        result = (dist, S[0] + align_S, T[0] + align_T)
    else:
        sub_dist, sub_S, sub_T = fast_align_MED(S[1:], T[1:], memo)
        sub = (1 + sub_dist, S[0] + sub_S, T[0] + sub_T)
        ins_dist, ins_S, ins_T = fast_align_MED(S, T[1:], memo)
        ins = (1 + ins_dist, "-" + ins_S, T[0] + ins_T)
        del_dist, del_S, del_T = fast_align_MED(S[1:], T, memo)
        delete = (1 + del_dist, S[0] + del_S, "-" + del_T)

        result = min([sub, ins, delete], key=lambda x: x[0])

    memo[(S, T)] = result
    return result[1:]

