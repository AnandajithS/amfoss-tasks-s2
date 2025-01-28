# Step-1

Using git clone 'https://github.com/KshitijThareja/TheCommandLineCup.git', I cloned the respository to my local machine. Then, I created a new directory "codes" using the command 'mkdir codes'.Inside the codes folder, I created files Part_1.txt,Part_2.txt,Part_3.txt,Part_4.txt using the command 'touch filename.txt'.

# Step-2 (First Challenge)

First perfect number (x): 6
Differentiating x^2-7x, we get 2x-7. Substituting for x, we get 5, which is y.
So, the spell was located in file 'Spell_05' inside directory '06'.
I went into the directory using the command 'cd 06'. Using the command 'ls', I was able to see all the files inside the directory.
I read the content inside file using the 'cat' command, after which I went into the 'spellbooks' directory, to find the file with the same name.
I ran the file using 'python' command, which gave me the code for part 1.

# Step-3 (Second Challenge)

I found the values of x and y to be 3 and 2, respectively.
So, the spell is located inside 'Spell_03' of directory '02'.
As I did in the previous step, I found the spellname and went into the 'spellbook' to run the python file with the same name, thus completing the second challenge.

# Step-4 (Third Challenge)

Using 'git branch -a', I was able to see all the available branches. After googling, I found that Professor Lupin taught Defense Against The Dark Arts.
I saw the branch 'defenseAgainstTheDarkArts', which I moved into using 'git checkout defenseAgainstTheDarkArts' and found the name. 
I moved the file to the main branch using 'git checkout' and ran it to find the secret code.


# Step-5 (Fourth Challenge)

Using 'git log', I checked the commit logs of the repository.
In one of the commits, I found another puzzle which I solved to get the path to the last file. 
So the spell was inside Spell_04.txt which was inside the directory 07, but in the branch 'graveyard'.
Using git checkout, I went into the fbranch and found the file location, ran the file and found out the spell 
After that,I did the same steps in step-4, moving it to the main file and running it. 
Then, I saved the code in the Part_4.txt.

# Step-6 (End)

First, I created a new file called "finalcode.txt"
Using 'cat Part_1.txt Part_2.txt Part_3.txt Part_4.txt > finalcode.txt', I concatenated all the parts to a single file.
After that, I did 'echo <content in the finalcode.txt> | base64 --decode', which gave me a link.
The link led to me a GitHub repository, which cloned using 'git clone'.
Ran the python file and got the ending screen.

# Commands for pushing work to our GitHub repository

**git add**: Using 'git add <filename>', we can add the changes in the files to the staging area.
We can also use 'git add .' to include all the files to be staged.

**git commit**: 'git commit' helps us to track the changes made to the files. 
We create a commit using 'git commit -m "message". After committing, we can push the files to our repository

**git push**: 'git push' allows to us to push the commits we made to our remote Github repository.
