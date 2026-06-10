# %%
file = open("rosalind_subs.txt")

lines = file.readlines()

Rna_Seq = lines[0].strip()
motif = lines[1].strip()

positions = []

for i in range(0, len(Rna_Seq)-len(motif)+1):

    Motif = Rna_Seq[i:i+len(motif)]

    if Motif == motif:
        positions.append(str(i+1))

print(" ".join(positions))
# %%
