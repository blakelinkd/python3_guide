#!/usr/bin/env python

from concurrent import futures


def approximate_pi(n):
    pi_half = 1
    numerator, denominator = 2.0, 1.0
    for i in range(n):
        pi_half *= numerator / denominator
        if i % 2:
            numerator += 2
        else:
            denominator += 2
    return 2*pi_half


if __name__ == "__main__":
    N = (123456789, 123456, 1234, 12)
    with futures.ThreadPoolExecutor(max_workers=4) as e:
        fs = {e.submit(approximate_pi, n): n for n in N}
        done = False
        while not done:
            res = futures.wait(fs, timeout=1.0)
            for f in res.done:
                print(f"n={fs[f]:10}: {f.result()}")
                del fs[f]
            done = (len(res.not_done) == 0)