# %%
def mendel(k, m, n):
    total = k + m + n

    p_aa_aa = (n / total) * ((n - 1) / (total - 1))
    p_Aa_aa = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))
    p_Aa_Aa = (m / total) * ((m - 1) / (total - 1))

    p_recessive_trait = (
        p_aa_aa * 1 +
        p_Aa_aa * 0.5 +
        p_Aa_Aa * 0.25
    )

    return 1 - p_recessive_trait


with open("rosalind_iprb.txt") as f:
    k, m, n = map(int, f.read().split())

print(mendel(k, m, n))
# %%
