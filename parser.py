from Bio.seq import Seq
def reverse_complement(seq_str)
 seq=Seq(seq_str)
 return str(seq.reverse_complement())
if __name=='__main__':
 print(reverse_complement('ATGCATGC'))
