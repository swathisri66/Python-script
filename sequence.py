#Task 1
class Sequence: 

  def __init__(self, dna_sequence):
    self.dna_sequence = dna_sequence.upper() #TASK 11 to make input dna data case insensitive

  #TASK 2
  #counting dna bases in a dna string
  def count_dna(self): 
    #checking if given sequence for counting bases is valid or not
    if self.is_dna == False:
      print('Given sequence is not valid DNA')
    else:
	    dna_count = 0
	    for base in self.dna_sequence:
		    dna_count = dna_count + 1
	    return dna_count

  #TASK 3
  #finding dna sequence is valid or return
  def is_dna(self):
	  valid = 'ACGT'
    #returning true is all bases in sequence are one of the bases in valid i.e A C G or T
	  return (all(i in valid for i in self.dna_sequence))

  #task 4
  #testing instance equality
  def __eq__(self, obj1):
    #chhecking for both class instance and for similarity between sequence as well
    return (isinstance(obj1,Sequence) and (self.dna_sequence==obj1.dna_sequence))
     
	
  #TASK 5
  #finding dna complement
  def dna_complement(self):
    #mapping introduced for mapping using : in the list
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    new_seq = []
    for character in self.dna_sequence:
      new_seq.append(basecomplement[character])
    #converting list to string
    str1 = ''.join(new_seq)
    return str1
  

  #TASK 6
  #comparing dna sequences and finding first non-matching base pair
  def compare_seq(self,seq2):
      print('\nThe DNA sequences being compared are: ',self.dna_sequence,'and ',seq2.dna_sequence)
      count = -1
      val = 0
      for i in range(len(self.dna_sequence)):
        if (self.dna_sequence[i] == seq2.dna_sequence[i]):
          val = val + 1
        else:
          count = 0
          break
      if (count == -1):
        print('The two DNA sequences are equal and return value is: ',count)
      else:
        print('Zero-based index of first non-matching base pair: ',val,'\n')

  #TASK 8
  #separating genes in genome based on a separator codon AAAAAAAAAATTTTTTTTTT
  def geneMatch(self):
    match = (self.dna_sequence).split('AAAAAAAAAATTTTTTTTTT')#splits the sequence at each place whenever it finds the given separator
    return match

#TASK 7
#readGenomic function to read genomic file and return its bases as Sequence class instance.
def readGenomic(filename):
    f = open(filename, 'r', encoding = 'ASCII')
    f.readline() #read header line and ignore it
    item = f.readline() #read dna bases in genome data
    f.close()
    new_obj = Sequence(item)
    return new_obj
