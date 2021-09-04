![Header](https://github.com/mshafae-fall-2021/cpsc-120-solution-lab-00/actions/workflows/header.yml/badge.svg)
![Formatting](https://github.com/mshafae-fall-2021/cpsc-120-solution-lab-00/actions/workflows/format.yml/badge.svg)
![Linting](https://github.com/mshafae-fall-2021/cpsc-120-solution-lab-00/actions/workflows/lint.yml/badge.svg)
![Compiling](https://github.com/mshafae-fall-2021/cpsc-120-solution-lab-00/actions/workflows/compile.yml/badge.svg)

# Lab 00: Tuffix, Shell, and Github

The purpose of this lab is to get familiar with the Linux system,
[Tuffix](https://github.com/kevinwortman/tuffix), the BASH shell, and GitHub. As part of the
lab, you will get to compile and run a [hello world program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program).

## Background

### UNIX system

Before there was Linux there was UNIX.

You might be familiar with operating systems like Windows or macOS. UNIX is another operating system that was developed back in 1969 by AT&T Bell labs. Operating systems manage the computer resources such as the memory, hard-drives, keyboard, mouse, screen, etc. For example, whenever you are copying a photo from your camera SD card connected to your computer to the computer's hard-drive, the operating system is taking care of performing this action in the background.

Many operating systems have been developed as an extension, or very similar to the UNIX operating system. Some of these are Linux or macOS.

#### The UNIX Shell

There are many ways to interact with an operating system: you can see the visual screen of your phone and interact with it by touching it, or you can listen to a Google Home device and interact with it by talking to it. One of the most basic ways to interact with an operating system is by using the UNIX shell, which looks like this:

```bash
$
```

Maybe your shell prompt does not look exactly like the example given. The important part is that there is always a `$` (dollar sign) symbol. This is what is called a prompt. The prompt is where you enter commands for the shell to execute.

The UNIX shell is a program that expects the user (you) to input commands (using a keyboard in most cases) and then sends your commands to the operating system to be executed on your behalf. There are multiple types of UNIX shells which determine the format/style of commands it expects. In this class, we will be using the *Bash* UNIX shell.

In the remainder of this document, the prompt shall be represented by just the `$` character. When you want to type commands into your shell on your computer, remember to only type the command - not the `$`.

*Note: you might notice that whenever you type your password in the shell, nothing will show up. This is working as intended (security feature). The terminal does let you type your password whenever it is asked, but it does not show any hidden characters as you type it.*

### Git, GitHub & GitHub Classroom

When writing code for a program, it is extremely helpful to keep track of the changes that you have made to your code. Sometimes you realize that a piece of code you recently wrote is actually broken and you need to revert it to an older version. A software that allows you to keep track of your code changes is called a version control system.

In addition, when working in a project with multiple people, programmers might need to update the same file at the same time. A **distributed** version control system allows each member of a team to download a copy of the existing code so that they can work on it locally, and later integrate it with the code from other members of the team. This allows the team to implement a software faster.

Git is a free and open source distributed version control system and is widely used in academia as well as the industry. GitHub is a web-based service that provides an online server to host code online that can be updated using Git. You can think of GitHub the same way you think of Dropbox, but made specifically to integrate with the Git system.

GitHub Classroom is a service that GitHub offers specifically designed for implementing Git in a classroom environment, where students download some code, implement their assignments, and then submit the code through Git, allowing the instructor to see all the submissions. We will be using GitHub classroom in all of the coding assignments of this class (labs and projects).

Git is a extremely powerful tool that allows teams to work on multiple versions of code, and because of this, Git can also get very complicated. For the purposes of this course, we will be learning three basic Git operations that will allow you to submit your assignments:

1. `git clone`, which allows you to download a copy of the code stored in GitHub onto your local computer so that you can edit it locally.
1. `git commit`, which is used to store (or save) a current version of your code (think of it as clicking the save button on a document you are editing).
1. `git push`, which uploads all of the versions you have stored each time you execute `git commit`. You can *commit* your code multiple times, creating multiple versions of your code. For these assignments, we will always only grade the most recent *commit* of your code (which is the most recent version).

For this assignment, you must have a GitHub account linked to your university email.

If you have never had a GitHub account, you can create one by visiting the [GitHub](https://github.com/) website and filling up the form to sign up for GitHub. Make sure to use your university email when creating the account. Make sure you verify your email (you will get a verification email after creating your account).

If you already have a GitHub account, but it was created using a different email, you need to link your GitHub account to your university email. Log into your account on the GitHub website and then visit the [Email settings](https://github.com/settings/emails) page to add your university email. Once you add your university email, you will receive an email which will allow you to verify that the email belongs to you.

## Lab instructions

## Configuring Git

The `git` command communicates with the online service GitHub. Although you login to GitHub, `git` is a command line tool that does not know who you are. We must configure `git` to know your name and email address.

It is important that you have your CSUF email address as one of your email addresses in your GitHub account. If you have not added your CSUF email address already, please do so before continuing. Instructions are online on how to add an [email address to your GitHub account](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/adding-an-email-address-to-your-github-account).

Use the following commands to configure `git` with your full name and your CSUF email address. Remember to replace `youremail@csu.fullerton.edu` with your CSUF email address and `Your Name` with your full name. (Remember, do not type the `$` because that is the prompt.)

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email youremail@csu.fullerton.edu
```

You can type the command immediately at the prompt. You do not need to `ls` or `cd` first.

### Cloning the Git Repository

One you are logged into your GitHub account, open the assignment URL that your instructor has shared with you. It looks like this: https://classroom.github.com/a/some_random_code

After opening that link, GitHub will generate the your own repository that will contain the starter code of the lab. This is the same repository where you will be pushing (submitting) your code for grading. Once the repository is generated, a similar message will show:

> Your assignment has been created here: https://github.com/some-github-organization/cpsc-120-lab-00-your_user_name

Open the link to see the web-view of your GitHub repository. In there you will see two files:

1. `README.md`: an exact copy of the file you are reading right now.
1. `hello_world.cc`: the starter code for your lab assignment.

Now we need to clone your repository into your local computer so that you can start working with that code. To keep your files organized, we will first create a folder for this class, and in that folder we will clone your repository.

#### Creating a folder

By default, opening a terminal will take you straight to your home directory, which is usually referred as `~` (tilde). If you are using Tuffix, the location of your home directory is `/home/your_user_name` (you can check by running the `pwd` command).

Let's go ahead and create a folder in your home directory called `cpsc120` by running the following command:

```
$ mkdir cpsc120
```

After you press enter, the folder cpsc120 will be created, which you can verify by listing all the files and folder under your home directory:

```
$ ls
cpsc120 Desktop Documents ...
```

#### Accessing the folder (changing a directory)

Now, let's enter the folder so that you can clone your repository inside. We are going to use the `cd` command, which stands for *change directory*:

```
$ cd cpsc120
$
```

#### Cloning the git repository

Now we are ready to clone your repository. Go back to the web-view of your GitHub repository and click on the **Clone or download** green button on the top right, and then click on the copy button right next to the repository address. Then, go back to the terminal and run the following command:

```
$ git clone <paste repository URL>
```

The command will ask you to input your GitHub username and password. Once you enter that information, the repository is then downloaded (cloned) into your computer. The whole process will look similar to this:

```bash
$ git clone https://github.com/some-github-organization/cpsc-120-lab-00-your_user_name.git
Username for 'https://github.com': your_user_name
Password for 'https://github.con':
Cloning into 'cpsc-120-lab-00-your_user_name'...
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 1), reused 9 (delta 1), pack-reused 0
Unpacking objects: 100% (9/9), done.
```

When you type in your password, the computer will not show what you type. It will look as though you are not typing anything at all. This is a security precaution to make sure no one can see your password. Remember to type slowly and carefully so you do not make any typographical errors.

Once the command completes, you can notice that there is a new folder called `cpsc-120-lab-00-your_user_name`:

```
$ ls
cpsc-120-lab-00-your_user_name
```

Let's access that folder and look at the contents:

```
$ cd cpsc-120-lab-00-your_user_name
$ ls
README.md hello_world.cc
```

As you can see, a copy of the two files that you saw on the web-view of your GitHub repository have been downloaded (cloned) into your computer. You have successfully cloned your lab assignment's git repository.

### Compiling and executing code

The file `hello_world.cc` contains source code for the HelloWorld program, written in C++. Our program will print "Hello World!" in the terminal whenever it is executed. Source code must first be compiled so that it can be executed in the computer. Let's go ahead and compile the source code.

#### Compiling source code

Tuffix comes with the `clang++` compiler installed.

To compile the `hello_world.cc` source code, run the following command:

```
$ clang++ hello_world.cc
```

Now you will see that a new file `a.out` has been created:
```
$ ls
a.out hello_world.cc README.md
```

This file is the compiled version of the source code, which we call a binary file (you will learn more about this later). This file is also an executable file, which means that we can run/execute it. Let's go ahead and execute the code.

#### Executing code

To execute or run the code, you need to append the prefix `./` to the name of the binary file. Type `./a.out` in the terminal and press enter. That will run the code and print any outputs that the code generates. It should print the following:

```
$ ./a.out
Hello world!
```

Now you have successfully compiled and executed C++ code!

### Editing code

C++ source code is just a plain text file, which means that you could use a text editor to edit the contents of the file. However, because we have to make sure the contents are plain text (no different fonts, bold, underline, italics, etc), it is safer to use a code editor rather than a text editor (such as Microsoft Word or WordPad). There are many types of code editors, some are very basic and straight forward, while other comes with sophisticated features such as code coloring, code suggestions, auto-formatters, etc. [Microsoft VS Code](https://code.visualstudio.com/) is a very popular and flexible editor provided by Microsoft at no cost.

You can open VS Code by running the `code` command in the terminal. (If the shell reports `command not found` that means it is not installed. Ask your instructor for help.)

If you want to directly open the C++ source code file you want to edit, you can pass the name of the file as the first argument of the `code` command. In our case, it will be `hello_world.cc`:

```
$ code hello_world.cc
```

Now that VS Code is open, go ahead and edit the `hello_world.cc`. Make the following changes:

1. Add a header to the file using the format specified in Canvas.

1. Replace "world" with your name, so that when you run it, it will print out your name. Let's pretend our name is Tuffy Titan, instead of printing "Hello World!" the program will print "Hello Tuffy!" after the file is saved, compiled, and run again.

To help you visualize the changes, the original `hello_world.cc` is shown below with each line prefixed with a line number. In C++, never type out the line numbers - it is shown here to help us talk about the code by giving each line a number we can reference. The entire program is C++ source code (lines 2-9). There are no comments or headers.

```c++
   1  
   2  #include <iostream>
   3  
   4  using namespace std;
   5  
   6  int main(int argc, const char *argv[]) {
   7    cout << "Hello world!\n";
   8    return 0;
   9  }
  10  
```

The first step is to add a header to your file using the specified format given in Canvas. Let's imagine that our name is _Tuffy Titan_, our email address is _tuffy.titan@csu.fullerton.edu_, and our GitHub login is _tuffytitan_. Adding the header would make the file look like the following example.

```c++
   1  // Tuffy Titan
   2  // CPSC 120-01
   3  // 2050-01-01
   4  // tuffy.titan@csu.fullerton.edu
   5  // @tuffytitan
   6  //
   7  // Lab 00-00
   8  //
   9  // This my first program and it prints out Hello Tuffy!
  10  //
  11  
  12  #include <iostream>
  13  
  14  using namespace std;
  15  
  16  int main(int argc, const char *argv[]) {
  17    cout << "Hello world!\n";
  18    return 0;
  19  }
  20  
```

Notice that the header was inserted at the top of the file. No changes were made to the C++ source code (lines 12-19).

Everytime you make a change to you file, save your changes (File menu), re-compile (`clang++ hello_world.cc`), and run the new program (`./a.out`) with every change you make. Use the up-arrow on the keyboard to save yourself some typing.

*This is very, very important and it is worth repeating.* Everytime you make a change to you file, save your changes (File menu), re-compile (`clang++ hello_world.cc`), and run the new program (`./a.out`) with every change you make.

If your compiler gives you a warning or error, fix it before moving on. Never move on when there are warnings or errors.

The next step is to replace "world" with your name, so that when you run your program, it will print out your name.

Note that it prints out `Hello world!\n` on line 17 in the example above. We need to only change that line to complete this step. Again, let us assume our name is _Tuffy Titan_.

Change line 17 from:
```c++
  17    cout << "Hello world!\n";
```

to:
```c++
  17    cout << "Hello Tuffy!\n";
```

Next, save your changes (File menu), re-compile (`clang++ hello_world.cc`), and run the new program (`./a.out`).

If you have warnings, errors, or anything else that is not clear, seek assistance before moving on.


### Pushing code to GitHub (submitting your assignment)

To submit your work, you will need to add the files that you want to submit, commit your changes, and push them into the GitHub repository. This is all done using the `git` program. Your work is sent to GitHub where your instructor and view it.

#### Adding the files

From the time you cloned the repository to now, there are two changes to the folder:

1. A new file `a.out` exists
1. The `hello_world.cc` file was modified.

You can verify this by running `git status`, which should display the following:

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello_world.cc

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	a.out

no changes added to commit (use "git add" and/or "git commit -a")
```

That information is telling two things: there is a modification to the `hello_world.cc` file and there is a new (untracked) file `a.out` that didn't exist before when you cloned the repository.

When submitting lab assignments or your project in this class, you will never be asked to submit the compiled code (in this case, the file `a.out`). We will take care of compiling it for you and running it for you when grading your assignment. That means that you just need to submit the `hello_world.cc` file.

In Git, you can only submit *commits*. A commit can be composed of multiple actions such as modifying a file, adding a new file, deleting a file. In this case, we just want to commit the modification you made to `hello_world.cc`, so we first need to add `hello_world.cc` to the commit by running the following command:

```
$ git add hello_world.cc
```

Now when you run `git status`, you will notice that the `modified: hello_world.cc` line is under *Changes to be committed* rather than *Changes not staged for commit*.

#### Committing your changes

To commit your changes (which in this case is was due to a single file), you run the command `git commit -m "Some quick description here"`. The `-m` indicates that the next parameter will be a description of your commit. The description should always be a sentence explaining what your change is about, and should be readable and useful for other engineers/programmers to understand what your change did. Some examples of commit descriptions could be *"Fixed bug that was causing the camera app to crash."* or *"Implemented the search feature for the project."*

In our case, you can use the description *"Changed the hello world message to show my name."* by running the following command:

```
$ git commit -m "Changed the hello world message to show my name. This is so awesome! I even recompiled it and verified that it works."
```

That command will output a message similar to this one:

```
[main 7374384] Changed the hello world message to show my name. This is so awesome! I even recompiled it and verified that it works.
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Something to notice in there is the line that says `1 file changed, 1 insertion(+), 1 deletion(-)`. It is a summary of how much stuff has changed in this commit. As we know, we modified 1 file. However, it also says that there was 1 insertion and 1 deletion. Those two measures are referring to how many lines were inserted and how many lines were deleted respectively. Git doesn't measure how many lines were modified, that means that if you modify a line, it will treat it as deleting that line and adding a new one with your modification.

##### Commit Warning Message

If you did not configure `git` in the first step, you will see a warning message that will look something like the following:

````
[main 7374384] Changed the hello world message to show my name. This is so awesome! I even recompiled it and verified that it works.
 Committer: Tuffy Titan <tuffy.titan@1.1.168.192.in-addr.arpa>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
```

This means that `git` does not know who you are so it made the best guess possible. Sometimes these guess are pretty good and other times they can be really poor.

The best course of action is to make sure `git` is configured correctly. Use the following commands to do so replacing `youremail@csu.fullerton.edu` with your CSUF email address and `Your Name` with your full name. This is why it is important that you add your @csu.fullerton.edu [email address to your GitHub account](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/adding-an-email-address-to-your-github-account). (Remember, do not type the `$` because that is the prompt.)

```
$ git config --global user.name "Your Name"
$ git config --global user.email youremail@csu.fullerton.edu
```

#### Pushing your commit to GitHub

The last step is to push your commit to GitHub. Running the following command will upload your commit, which includes the files you added or edited, as well as the commit message:

```
$ git push
```

If everything went well, you should see a message similar to this one:

```
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 340 bytes | 340.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/some-github-organization/cpsc-120-lab-00-your_user_name
```

If you open the URL of your Git repository, you will see a blue row right above the list of files that shows your last commit. It will say something like this:

```
your_user_name Changed the hello world message to show my name. This is so awesome! I even recompiled it and verified that it works. Latest commit 7374384  1 minute ago
```

You can try clicking on the commit number (in the example above, that would be `7374384`) to open a web-view of the commit you made.

#### GitHub Actions
Every time you push your work to GitHub, a series of actions that your instructor created are run. It may take 10 seconds or a minute for these actions to complete after your push completes. You can see the output of these actions by viewing the _Actions_ tab on your repository's GitHub page. This is a link between _Pull Requests_ and _Projects_.

Click on the arrow icons to see if there were any errors. This is an excellent way to determine if your work is going to get high marks or low marks. 

## Grading Rubric (5 points)
1. (2 point): Your added a header
1. (2 point): Your changed the message in the program to print your name
1. (1 point): Your commit message describes the main point of what you changed.

If your program does not compile, you are missing your header, or if no changes were made, a score of zero shall be assigned.


## Acknowledgements
This lab was adapted from a lab by Jeff Li of Google.