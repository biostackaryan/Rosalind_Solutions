# %%
from Bio import motifs
from Bio.Seq import SeqIO

records=list(SeqIo.parse("example.fasta","fasta")
instances=[record.seq for record in records]
m=motifs.create(instances)
print(m.consensus)
print(m.counts)
print(len(m))
