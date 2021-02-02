**_Git-Collaboration Definitions and Examples_**<br>

**repository** - Directory or storage space either on your computer or on Github where you can store your files.<br>
*Not an actual command* __Use:__ *$ git clone 'repositoryName'*

**clone** - Making a copy of a repository on Github onto your local computer.<br>
*$ git clone https://gitrepo.mysite.com/foobar.git*

**fork** - Creating a personal copy of someone else's project.<br>
*A concept and not a command* An example of a forked project is Bitcoin and its many forked coins such as Bitcoin Cash, Bitcoin Private, Bitcoin Gold, etc.<br> Another example is the reverse engineering framework, [radare2](https://github.com/radareorg) and its  developer community splitting, forking the repository and using it to create [Rizin](https://github.com/rizinorg).*

**branch** - Used to fix bugs and develop features.<br>
*$ git branch <'branchname'>*

**commit** - A change to one or more files in a branch; similar to saving a file.<br>
*$ git commit -m <'message'>*

**merge** - Git command that combines the commits made by others with your own commits.<br>
*$ git merge 'someWorkName'*

**checkout** - Command that lets you navigate between the branches created by git branch.<br>
*$ git checkout 'theBranch'*

**push** - Moving the commits made from a local branch to a remote repository.<br>
*$ git push 'remoteName'*

**pull** - Shortcut of the fetch and merge commands where you collect the changes from a remote repository and combine it with the local changes.<br>
*$ git pull 'remoteName'*

**remote add** - Command that adds a new remote.<br>
*$ git remote add 'remoteName' 'remoteURL'*

**remote remove** - Command that removes a remote URL from a repository.<br>
*$ git remote rm 'remoteName'*

**remote show** - Command that shows information about the remote.<br>
*$ git remote show 'remote'* 

**status** - Displays information of the current working repository; Whether all is up to date or missing files in either local or remote repositories.<br>
*$ git status*

**master branch** - Default branch name which points to the last made commit; Each commit increases the pointer of the master branch by one.<br>
*Not a command*; __Use:__ *$ git checkout master* 
