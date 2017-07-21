How to upload content
===================

<p align="center"><img src="https://raw.githubusercontent.com/astro4dev/OAD-Data-Science-Toolkit/master/img/DST_logo_250px.png" alt="DST Logo"/></p>

## Get a GitHub account

It's required if you want to submit content to the toolkit which is hosted on GitHub. Get an account <a href="https://github.com/" target="_blank">here</a>.

## Install git on your computer
To use Git on the command line, you'll need to download, install, and configure Git on your computer.

On Ubuntu
```sh
sudo apt-get install git
```

There is also a GUI interface known as the
<a href="https://desktop.github.com/" target="_blank">Desktop version</a> which is available for Windows and for Mac OSX.

## Fork a respotisty
<a href="https://help.github.com/articles/fork-a-repo/" target="_blank">Instructions on GitHub</a>

## Making changes

Download all the latest changes to your local repository
```sh
git pull
```

Once you have made changes locally you can get an overview of the files you've alterned (relative to your online repository) by typing:
```sh
git status
```
Red coloured files means they have not been added. Green means they have.

To push a file to your repository clone on github type:
```sh
git add [name_of_file]
```

You then have to commit it (basically prepare it to be uploaded) by adding a comment describing what you did:
```sh
git commit -m 'I removed the bug causing...'
```

Finally push it to your online clone of the repository by typing:
```sh
git push
```

## Opening pull requests
If you are hoping to contribute back to the original repository, you can send a request to the original author to pull your fork into their repository by submitting a <a href="https://help.github.com/articles/about-pull-requests/" target="_blank">pull request</a>.

