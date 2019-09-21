from SequenceClass import Sequence
from SequenceClass import readGenomic
import matplotlib.pyplot as plt
 
#code for testing and demonstrating functionality
#dna_sequence1 = input('Enter a dna sequence')
#can use above statement if we want the user to give dna string as an input
dna_sequence1 = 'atgctcgaactcgctctgct'
sequence_1 = Sequence(dna_sequence1)
print('First sequence given is ',sequence_1.dna_sequence,' with ',sequence_1.count_dna(),' number of bases')
validate1 = sequence_1.is_dna()
print(sequence_1.dna_sequence, 'is',validate1,'DNA and its Complement is ',sequence_1.dna_complement())
if sequence_1.dna_complement()=='TACGAGCTTGAGCGAGACGA':
  print('Tested manually for complement and Test successful')
else:
  print('Function needs modification')

sequence_2 = Sequence('atugctacstcu')
validate2 = sequence_2.is_dna()
print('\nSecond sequence ',sequence_2.dna_sequence, 'is',validate2,'DNA')

print('\n__eq__ function result for first set of objects is',sequence_1==sequence_2)
assert sequence_1==sequence_1
#assert sequence_1==sequence_2
#will throw an AssertionError

comp_seq1 = Sequence('ACGTGCG')
comp_seq2 = Sequence('ACGUGCG')
if(comp_seq1.count_dna() == comp_seq2.count_dna()):
  comp_seq1.compare_seq(comp_seq2)
else:
  raise Exception('cannot compare sequences of different lengths')

new_obj1 = readGenomic("genome_01.dat")
print(new_obj1.count_dna(),' bases in genome_01.dat file')

#TASK 8 example
obj1 = Sequence('CCGATCGAAAAAAAAAAATTTTTTTTTT')
gene_match = obj1.geneMatch()
print("\nLength of first gene in CCGATCGAAAAAAAAAAATTTTTTTTTT is ",len(gene_match[0]))

#TASK 9
gene_list = new_obj1.geneMatch()
len_list= []
for i in range(len(gene_list)):
  len_list.append(len(gene_list[i]))
#plotting gene lengths in genome_01.dat 
plt.figure()
plt.hist(len_list)
plt.title("Gene Lengths - Genome_01")
plt.xlabel("Length of gene")
plt.ylabel("Gene Number in the Genome")
plt.savefig("gene_length.png")

#TASK 10
new_obj2 = readGenomic("genome_02.dat")
gene_list2 = new_obj2.geneMatch()
#catching gene swap mutations and storing in a list mutations[]
mutations= []
for i in range(len(gene_list)):
  counter= 0
  for j in range(len(gene_list[i])):
    if (gene_list[i][j]!=gene_list2[i][j]):
      counter= counter+1
  mutations.append(counter)  
print('\nTotal mutations in corresponding genes of two given genomes are: ',sum(mutations))
#plotting mutations against gene lengths
plt.figure(2)
plt.scatter(mutations,len_list)
plt.title("Scatter Plot - Swap Mutations")
plt.xlabel("Number of mutations")
plt.ylabel("Gene Length")
plt.savefig("mutations.png")
