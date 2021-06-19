def ks(W, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return ks(W, n-1)
    else:
        return max(val[n-1] + ks(W-wt[n-1], n-1), ks(W, n-1))

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(ks(W, n))

v = 0
n = 2
while (n >= 0) and W >= wt[n]:
    print(W, v, n)
    v += val[n]
    W -= wt[n]
    n -= 1

print(v)


for n in N:
    bar_s[n] = tilde_s[n]

while B > 0:
    n_prime, _ = max((obj_f(n), n) for n in N if f_i*P_ij < Q_ij*S_n(i, j))

    if b[n] < B:
        bar_s[n_prime] = max((obj_f(n), S_n) for S_n in co(fancy_s) for n in N if f_i*P_ij < Q_ij*S_n(i, j))
        B = B - b[n]        
