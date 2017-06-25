# Bayesian learning for classifying netnews text articles:




Naive Bayes classifiers are among the most successful known algorithms for learning to classify text documents. We use a dataset containing 20,000 newsgroup messages drawn from the 20 newsgroups. The dataset contains 1000 documents from each of the 20 newsgroups. 

Download the data from http://www.cs.cmu.edu/afs/cs/project/theo-11/www/naive-bayes.html (Newsgroup Data)

# How to run the code:

The only variable that you need to give a value before running the code is ‘path’. You should give the whole path to the directory where the data is located. 

 
# Algorithm:
The project has three phases: Preprocessing, training, and testing. In the preprocessing phase, we clean the data. There are some characters that they need to either be removed or be replaced with space character.

We  consider two list remove_list and replace_list, and remove all the characters inside the remove_list from the data and replaced all character inside the replaced_list with space. 

- Replace_list = ["'",'!','/','\\','=',',',':', ‘\n’]

- Remove_list = ['<','>','?','.','"',')','(','|','-','#','*','+']

We convert all the uppercase letters to lowercase ones. clean_text function does this part and cleans the data.
In the training phase, We select first 500 files of each class, and split the file with character space. We count the number of occurrences of each word in class’s files and put them in a dictionary. After the training phase, we get totally around 170,000 different words in all classes (for 10,000 files).

In the testing phase: we pick files randomly from the remaining files from the training phase, function get_file gives us the files. The same as before, we clean the file with clean_text function, after that we comput the probability of each word in this file for all classes

```sh
  For each class c:
        Pc = 0
        For each word in cleaned_file:
                Pc = Pc + log(P(word| c))
       
```
Function get_probability gives us the probability for a given class. The predicated class would be the one has the highest probability Pc .

The accuracy rate for this code is 87%.
