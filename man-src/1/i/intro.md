---
title: "intro(1)"
name: "intro"
section: "1"
letter: "i"
url: "/docs/linux/man/1-intro/"
description: "intro – introduction to user commands"
---

<h2 class="name">NAME</h2>
<p> intro &#8211; introduction to user commands </p>
<h2>DESCRIPTION</h2>
<p> Section 1 of the manual describes user commands and tools, for example, file manipulation tools, shells, compilers, web browsers, file and image viewers and editors, and so on.</p>
<h2>NOTES</h2>
<p> Linux is a flavor of UNIX, and as a first approximation all user commands under UNIX work precisely the same under Linux (and FreeBSD and lots of other UNIX-like systems). </p>
<p> Under Linux, there are GUIs (graphical user interfaces), where you can point and click and drag, and hopefully get work done without first reading lots of documentation. The traditional UNIX environment is a CLI (command line interface), where you type commands to tell the computer what to do. That is faster and more powerful, but requires finding out what the commands are. Below a bare minimum, to get started.</p>
<h3>Login</h3>
<p> In order to start working, you probably first have to open a session by giving your username and password. The program <code><a href="/docs/linux/man/1-login/">login</a></code>(1) now starts a <i>shell</i> (command interpreter) for you. In case of a graphical login, you get a screen with menus or icons and a mouse click will start a shell in a window. See also <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1).</p>
<h3>The shell</h3>
<p> One types commands to the <i>shell</i>, the command interpreter. It is not built-in, but is just a program and you can change your shell. Everybody has their own favorite one. The standard one is called <i>sh</i>. See also <code><a href="/docs/linux/man/1-ash/">ash</a></code>(1), <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-dash/">dash</a></code>(1), <code><a href="/docs/linux/man/1-ksh/">ksh</a></code>(1), <code><a href="/docs/linux/man/1-zsh/">zsh</a></code>(1). </p>
<p> A session might go like: </p>
<p> knuth login: <code>aeb</code> Password: <code>********</code> $ <code>date</code> Tue Aug 6 23:50:44 CEST 2002 $ <code>cal</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;August 2002 Su Mo Tu We Th Fr Sa<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;3<br />
&nbsp;4&nbsp;<wbr>&nbsp;5&nbsp;<wbr>&nbsp;6&nbsp;<wbr>&nbsp;7&nbsp;<wbr>&nbsp;8&nbsp;<wbr>&nbsp;9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 </p>
<p> $ <code>ls</code> bin tel $ <code>ls -l</code> total 2 drwxrwxr-x 2 aeb 1024 Aug 6 23:51 bin -rw-rw-r&#8211; 1 aeb 37 Aug 6 23:52 tel $ <code>cat tel</code> maja 0501-1136285 peter 0136-7399214 $ <code>cp tel tel2</code> $ <code>ls -l</code> total 3 drwxr-xr-x 2 aeb 1024 Aug 6 23:51 bin -rw-r&#8211;r&#8211; 1 aeb 37 Aug 6 23:52 tel -rw-r&#8211;r&#8211; 1 aeb 37 Aug 6 23:53 tel2 $ <code>mv tel tel1</code> $ <code>ls -l</code> total 3 drwxr-xr-x 2 aeb 1024 Aug 6 23:51 bin -rw-r&#8211;r&#8211; 1 aeb 37 Aug 6 23:52 tel1 -rw-r&#8211;r&#8211; 1 aeb 37 Aug 6 23:53 tel2 $ <code>diff tel1 tel2</code> $ <code>rm tel1</code> $ <code>grep maja tel2</code> maja 0501-1136285 $ </p>
<p> Here typing Control-D ended the session. </p>
<p> The <code>$</code> here was the command prompt&#8212;it is the shell&#8217;s way of indicating that it is ready for the next command. The prompt can be customized in lots of ways, and one might include stuff like username, machine name, current directory, time, and so on. An assignment PS1=&quot;What next, master? &quot; would change the prompt as indicated. </p>
<p> We see that there are commands <i>date</i> (that gives date and time), and <i>cal</i> (that gives a calendar). </p>
<p> The command <i>ls</i> lists the contents of the current directory&#8212;it tells you what files you have. With a <i>-l</i> option it gives a long listing, that includes the owner and size and date of the file, and the permissions people have for reading and/or changing the file. For example, the file &quot;tel&quot; here is 37 bytes long, owned by aeb and the owner can read and write it, others can only read it. Owner and permissions can be changed by the commands <i>chown</i> and <i>chmod</i>. </p>
<p> The command <i>cat</i> will show the contents of a file. (The name is from &quot;concatenate and print&quot;: all files given as parameters are concatenated and sent to &quot;standard output&quot; (see <code><a href="/docs/linux/man/3-stdout/">stdout</a></code>(3)), here the terminal screen.) </p>
<p> The command <i>cp</i> (from &quot;copy&quot;) will copy a file. </p>
<p> The command <i>mv</i> (from &quot;move&quot;), on the other hand, only renames it. </p>
<p> The command <i>diff</i> lists the differences between two files. Here there was no output because there were no differences. </p>
<p> The command <i>rm</i> (from &quot;remove&quot;) deletes the file, and be careful! it is gone. No wastepaper basket or anything. Deleted means lost. </p>
<p> The command <i>grep</i> (from &quot;g/re/p&quot;) finds occurrences of a string in one or more files. Here it finds Maja&#8217;s telephone number.</p>
<h3>Pathnames and the current directory</h3>
<p> Files live in a large tree, the file hierarchy. Each has a <i>pathname</i> describing the path from the root of the tree (which is called <i>/</i>) to the file. For example, such a full pathname might be <i>/home/aeb/tel</i>. Always using full pathnames would be inconvenient, and the name of a file in the current directory may be abbreviated by giving only the last component. That is why <i>/home/aeb/tel</i> can be abbreviated to <i>tel</i> when the current directory is <i>/home/aeb</i>. </p>
<p> The command <i>pwd</i> prints the current directory. </p>
<p> The command <i>cd</i> changes the current directory. </p>
<p> Try alternatively <i>cd</i> and <i>pwd</i> commands and explore <i>cd</i> usage: &quot;cd&quot;, &quot;cd .&quot;, &quot;cd ..&quot;, &quot;cd /&quot; and &quot;cd ~&quot;.</p>
<h3>Directories</h3>
<p> The command <i>mkdir</i> makes a new directory. </p>
<p> The command <i>rmdir</i> removes a directory if it is empty, and complains otherwise. </p>
<p> The command <i>find</i> (with a rather baroque syntax) will find files with given name or other properties. For example, &quot;find . -name tel&quot; would find the file <i>tel</i> starting in the present directory (which is called <i>.</i>). And &quot;find / -name tel&quot; would do the same, but starting at the root of the tree. Large searches on a multi-GB disk will be time-consuming, and it may be better to use <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1).</p>
<h3>Disks and filesystems</h3>
<p> The command <i>mount</i> will attach the filesystem found on some disk (or floppy, or CDROM or so) to the big filesystem hierarchy. And <i>umount</i> detaches it again. The command <i>df</i> will tell you how much of your disk is still free.</p>
<h3>Processes</h3>
<p> On a UNIX system many user and system processes run simultaneously. The one you are talking to runs in the <i>foreground</i>, the others in the <i>background</i>. The command <i>ps</i> will show you which processes are active and what numbers these processes have. The command <i>kill</i> allows you to get rid of them. Without option this is a friendly request: please go away. And &quot;kill -9&quot; followed by the number of the process is an immediate kill. Foreground processes can often be killed by typing Control-C.</p>
<h3>Getting information</h3>
<p> There are thousands of commands, each with many options. Traditionally commands are documented on <i>man pages</i>, (like this one), so that the command &quot;man kill&quot; will document the use of the command &quot;kill&quot; (and &quot;man man&quot; document the command &quot;man&quot;). The program <i>man</i> sends the text through some <i>pager</i>, usually <i>less</i>. Hit the space bar to get the next page, hit q to quit. </p>
<p> In documentation it is customary to refer to man pages by giving the name and section number, as in <code><a href="/docs/linux/man/1-man/">man</a></code>(1). Man pages are terse, and allow you to find quickly some forgotten detail. For newcomers an introductory text with more examples and explanations is useful. </p>
<p> A lot of GNU/FSF software is provided with info files. Type &quot;info info&quot; for an introduction on the use of the program <i>info</i>. </p>
<p> Special topics are often treated in HOWTOs. Look in <i>/usr/share/doc/howto/en</i> and use a browser if you find HTML files there.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ash/">ash</a></code>(1), <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-dash/">dash</a></code>(1), <code><a href="/docs/linux/man/1-ksh/">ksh</a></code>(1), <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1), <code><a href="/docs/linux/man/1-zsh/">zsh</a></code>(1), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/3-stdout/">stdout</a></code>(3), <code><a href="/docs/linux/man/7-man-pages/">man-pages</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
