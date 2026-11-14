---
title: "ikiwiki-makerepo(1)"
name: "ikiwiki-makerepo"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ikiwiki-makerepo/"
---

<h2>NAME</h2>

 ikiwiki-makerepo - check an ikiwiki srcdir into revision control 

<h2>SYNOPSIS</h2>

 ikiwiki-makerepo git|svn|monotone|darcs|cvs srcdir repository 

 ikiwiki-makerepo bzr|mercurial srcdir 

<h2>DESCRIPTION</h2>

 ikiwiki-makerepo injects a srcdir directory, containing an ikiwiki wiki, into a repository that it creates. The repository can be created using any of a variety of revision control systems. 

 Note that for mercurial and bzr, the srcdir is converted into a repository. There is no need to have a separate repository with mercurial or bzr. 

 For darcs, the master repo's apply hook will be preconfigured to call a ikiwiki wrapper. 

 Note that for monotone, you are assumed to already have run &quot;mtn genkey&quot; to generate a key. 

<h2>EXAMPLE</h2>

 ikiwiki-makerepo git /var/www/wiki /home/user/wiki/ 

 The above command creates a new git repo in /home/user/wiki as well as a new git repo in the /var/www/wiki directory. It then initializes the /home/user/wiki git repo and makes the /var/www/wiki a clone. 

<h2>AUTHOR</h2>

 Joey Hess &lt;joey [at] ikiwiki.info&gt; 

 

 

 

<h2>Index</h2>


