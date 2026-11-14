---
title: "ncftp(1)"
name: "ncftp"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncftp/"
description: "ncftp – Browser program for the File Transfer Protocol"
---

<h2>NAME</h2>
<p> ncftp &#8211; Browser program for the File Transfer Protocol</p>
<h2>SYNOPSIS</h2>
<p> <code>ncftp</code> [<i>host</i>] </p>
<p> <code>ncftp</code> [<i><a href="ftp://host.name/directory/">ftp://host.name/directory/</a></i>]</p>
<h2>DESCRIPTION</h2>
<p> The purpose of <i>ncftp</i> is to provide a powerful and flexible interface to the Internet standard <i>File Transfer Protocol</i>. It is intended to replace the stock <i>ftp</i> program that comes with the system. </p>
<p> Although the program appears to be rather spartan, you&#8217;ll find that <i>ncftp</i> has a wealth of valuable performance and usage features. The program was designed with an emphasis on usability, and it does as much as it can for you automatically so you can do what you expect to do with a file transfer program, which is transfer files between two interconnected systems. </p>
<p> Some of the cooler features include progress meters, filename completion, command-line editing, background processing, auto-resume downloads, bookmarking, cached directory listings, host redialing, working with firewalls and proxies, downloading entire directory trees, etc., etc. </p>
<p> The <i>ncftp</i> distribution comes with the useful utility programs <i><a href="/docs/linux/man/1-ncftpget/">ncftpget</a></i>(1) and <i><a href="/docs/linux/man/1-ncftpput/">ncftpput</a></i>(1) which were designed to do command-line FTP. In particular, they are very handy for shell scripts. This version of <i>ncftp</i> no longer does command-line FTP, since the main <i>ncftp</i> program is more of a browser-type program.</p>
<h3>OPTIONS</h3>
<p> The program allows you to specify a host or directory URL on the command line. This is a synonym for running <i>ncftp</i> and then using the <i>open</i> command. A few command-line flags are allowed with this mode:</p>
<dl>
<dt><code>-u </code><i>XX</i></p>
<dd> Use username <i>XX</i> instead of anonymous.</p>
<dt><code>-p </code><i>XX</i></p>
<dd> Use password <i>XX</i> with the username.</p>
<dt><code>-j </code><i>XX</i></p>
<dd> Use account <i>XX</i> in supplement to the username and password (deprecated).</p>
<dt><code>-P </code><i>XX</i></p>
<dd> Use port number <i>XX</i> instead of the default FTP service port (21).</dl>
<h3>INTRODUCTION TO THE COMMAND SHELL</h3>
<p> Upon running the program you are presented a command prompt where you type commands to the program&#8217;s shell. Usually you will want to open a remote filesystem to transfer files to and from your local machine&#8217;s filesystem. To do that, you need to know the symbolic name of the remote system, or its <i>Internet Protocol </i> (IP) address. For example, a symbolic name might be &#8220;typhoon.unl.edu,&#8221; and its IP address could be &#8220;129.93.33.24.&#8221; To open a connection to that system, you use the program&#8217;s <i>open</i> command: </p>
<pre>
open typhoon.unl.edu
open 129.93.33.24
</pre>
<p> Both of these try to open the machine called typhoon at the <i>University of Nebraska</i>. Using the symbolic name is the preferred way, because IP addresses may change without notice, while the symbolic names usually stay the same. </p>
<p> When you open a remote filesystem, you need to have permission. The <i>FTP Protocol</i>&#8216;s authentication system is very similar to that of logging in to your account. You have to give an account name, and its password for access to that account&#8217;s files. However, most remote systems that have anything you might be interested in don&#8217;t require an account name for use. You can often get anonymous access to a remote filesystem and exchange files that have been made publicly accessible. The program attempts to get anonymous permission to a remote system by default. What actually happens is that the program tries to use &#8220;anonymous&#8221; as the account name, and when prompted for a password, uses your E-mail address as a courtesy to the remote system&#8217;s maintainer. You can have the program try to use a specific account also. That will be explained later. </p>
<p> After the <i>open</i> command completes successfully, you are connected to the remote system and logged in. You should now see the command prompt change to reflect the name of the current remote directory. To see what&#8217;s in the current remote directory, you can use the program&#8217;s <i>ls</i> and <i>dir</i> commands. The former is terse, preferring more remote files in less screen space, and the latter is more verbose, giving detailed information about each item in the directory. </p>
<p> You can use the program&#8217;s <i>cd</i> command to move to other directories on the remote system. The cd command behaves very much like the command of the same name in the <i>Bourne</i> and <i>Korn</i> shell. </p>
<p> The purpose of the program is to exchange data with other systems. You can use the program&#8217;s <i>get</i> command to copy a file from the remote system to your local system: </p>
<pre>
get README.txt
</pre>
<p> The program will display the progress of the transfer on the screen, so you can tell how much needs to be done before the transfer finishes. When the transfer does finish, then you can enter more commands to the program&#8217;s command shell. </p>
<p> You can use the program&#8217;s <i>put</i> command to copy a file from your system to the remote system: </p>
<pre>
put something.tar
</pre>
<p> When you are finished using the remote system, you can open another one or use the <i>quit</i> </p>
<p> Before quitting, you may want to save the current FTP session&#8217;s settings for later. You can use the <i>bookmark</i> command to save an entry into your $HOME/.ncftp/bookmarks file. When you use the <i>bookmark</i> command, you also specify a bookmark name, so the next time instead of opening the full hostname you can use the name of the bookmark. A bookmark acts just like one for your web browser, so it saves the remote directory you were in, the account name you used, etc., and other information it learned so that the next time you use the bookmark it should require as little effort from you as possible.</p>
<h3>COMMAND REFERENCE</h3>
<dl>
<dt>help</p>
<dd> The first command to know is <i>help</i>. If you just type</p>
<dt>
<dd>
<pre>
help
</pre>
<dt>
<dd> from the command shell, the program prints the names of all of the supported commands. From there, you can get specific help for a command by typing the command after, for example:</p>
<dt>
<dd>
<pre>
help open
</pre>
<dt>
<dd> prints information about the <i>open</i> command.</p>
<dt>ascii</p>
<dd> This command sets the transfer type to ASCII text. This is useful for text-only transfers because the concept of text files differs between operating systems. For example on UNIX, a text file denotes line breaks with the linefeed character, while on MS-DOS a line break is denoted by both a carriage return character and a line feed character. Therefore, for data transfers that you consider the data as text you can use <i>ascii</i> to ensure that both the remote system and local system translate accordingly. The default transfer type that <i>ncftp</i> uses is not ASCII, but straight binary.</p>
<dt>bgget and bgput</p>
<dd> These commands correspond to the <i>get</i> and <i>put</i> commands explained below, except that they do the job in the background. Normally when you do a <i>get</i> then the program does the download immediately, and does not return control to you until the download completes. The background transfers are nice because you can continue browsing the remote filesystem and even open other systems. In fact, they are done by a daemon process, so even if you log off your UNIX host the daemon should still do your transfers. The daemon will also automatically continue to retry the transfers until they finish. To tell when background jobs have finished, you have to examine the <i>$HOME/.ncftp/spool/log</i> file, or run the <i>jobs</i> command from within <i>NcFTP</i>.</p>
<dt>
<dd> Both the <i>bgget</i> and <i>bgput</i> commands allow you to schedule when to do the transfers. They take a &#8220;-@&#8221; parameter, whose argument is a date of the form YYYYMMDDhhmmss (four digit year, month, day, hour, minute, second). For example, to schedule a download at 3 AM on November 6, you could try:</p>
<dt>
<dd>
<pre>
bgget -@ 19971106030000 /pub/idstuff/quake/q2_100.zip
</pre>
<dt>bgstart</p>
<dd> This command tells <i>ncftp</i> to immediately start the background transfers you&#8217;ve requested, which simply runs a copy of the <i>ncftpbatch</i> program which is responsible for the background jobs. Normally the program will start the background job as soon as you close the current site, open a new site, or quit the program. The reason for this is because since so many users still use slow dialup links that starting the transfers would slow things to a crawl, making it difficult to browse the remote system. An added bonus of starting the background job when you close the site is that <i>ncftp</i> can pass off that open connection to the <i>ncftpbatch</i> program. That is nice when the site is always busy, so that the background job doesn&#8217;t have to wait and get re-logged on to do its job.</p>
<dt>binary</p>
<dd> Sets the transfer type to raw binary, so that no translation is done on the data transferred. This is the default anyway, since most files are in binary.</p>
<dt>bookmark</p>
<dd> Saves the current session settings for later use. This is useful to save the remote system and remote working directory so you can quickly resume where you left off some other time. The bookmark data is stored in your <i>$HOME/.ncftp/bookmarks</i> file.</p>
<dt>bookmarks</p>
<dd> Lists the contents of your <i>$HOME/.ncftp/bookmarks</i> file in a human-readable format. You can use this command to recall the bookmark name of a previously saved bookmark, so that you can use the <i>open</i> command with it.</p>
<dt>cat</p>
<dd> Acts like the &#8220;/bin/cat&#8221; <i>UNIX</i> command, only for remote files. This downloads the file you specify and dumps it directly to the screen. You will probably find the <i>page</i> command more useful, since that lets you view the file one screen at a time instead of printing the entire file at once.</p>
<dt>cd</p>
<dd> Changes the working directory on the remote host. Use this command to move to different areas on the remote server. If you just opened a new site, you might be in the root directory. Perhaps there was a directory called &#8220;/pub/news/comp.sources.d&#8221; that someone told you about. From the root directory, you could:</p>
<dt>
<dd>
<pre>
cd pub
cd news
cd comp.sources.d
</pre>
<dt>
<dd> or, more concisely,</p>
<dt>
<dd>
<pre>
cd /pub/news/comp.sources.d
</pre>
<dt>
<dd> Then, commands such as <i>get</i>, <i>put</i>, and <i>ls</i> could be used to refer to items in that directory.</p>
<dt>
<dd> Some shells in the <i>UNIX</i> environment have a feature I like, which is switching to the previous directory. Like those shells, you can do:</p>
<dt>
<dd>
<pre>
cd -
</pre>
<dt>
<dd> to change to the last directory you were in.</p>
<dt>chmod</p>
<dd> Acts like the &#8220;/bin/chmod&#8221; <i>UNIX</i> command, only for remote files. However, this is not a standard command, so remote FTP servers may not support it.</p>
<dt>close</p>
<dd> Disconnects you from the remote server. The program does this for you automatically when needed, so you can simply open other sites or quit the program without worrying about closing the connection by hand.</p>
<dt>debug</p>
<dd> This command is mostly for internal testing. You could type</p>
<dt>
<dd>
<pre>
debug 1
</pre>
<dt>
<dd> to turn debugging mode on. Then you could see all messages between the program and the remote server, and things that are only printed in debugging mode. However, this information is also available in the <i>$HOME/.ncftp/trace</i> file, which is created each time you run <i>ncftp</i>. If you need to report a bug, send a <i>trace</i> file if you can.</p>
<dt>dir</p>
<dd> Prints a detailed directory listing. It tries to behave like <i>UNIX</i>&#8216;s &#8220;/bin/ls -l&#8221; command. If the remote server seems to be a <i>UNIX</i> host, you can also use the same flags you would with <i>ls</i>, for instance</p>
<dt>
<dd>
<pre>
dir -rt
</pre>
<dt>
<dd> would try to act like</p>
<dt>
<dd>
<pre>
/bin/ls -lrt
</pre>
<dt>
<dd> would on <i>UNIX</i>.</p>
<dt>edit</p>
<dd> Downloads into a temporary file for editing on the local host, then uploads the changed file back to the remote host.</p>
<dt>get</p>
<dd> Copies files from the current working directory on the remote host to your machine&#8217;s current working directory. To place a copy of &#8220;README&#8221; and &#8220;README.too&#8221; in your local directory, you could try:</p>
<dt>
<dd>
<pre>
get README README.too
</pre>
<dt>
<dd> You could also accomplish that by using a wildcard expression, such as:</p>
<dt>
<dd>
<pre>
get README*
</pre>
<dt>
<dd> This command is similar to the behavior of other FTP programs&#8217; <i>mget</i> command. To retrieve a remote file but give it a different name on your host, you can use the &#8220;-z&#8221; flag. This example shows how to download a file called <i>ReadMe.txt</i> but name it locally as <i>README</i>:</p>
<dt>
<dd>
<pre>
get -z ReadMe.txt README
</pre>
<dt>
<dd> The program tries to &#8220;resume&#8221; downloads by default. This means that if the remote FTP server lost the connection and was only able to send 490 kilobytes of a 500 kilobyte file, you could reconnect to the FTP server and do another <i>get</i> on the same file name and it would get the last 10 kilobytes, instead of retrieving the entire file again. There are some occasions where you may not want that behavior. To turn it off you can use the &#8220;-f&#8221; flag.</p>
<dt>
<dd> There are also times where you want to append to an existing file. You can do this by using the &#8220;-A&#8221; flag, for example</p>
<dt>
<dd>
<pre>
get -A log.11
</pre>
<dt>
<dd> would append to a file named &#8220;log.11&#8221; if it existed locally.</p>
<dt>
<dd> Another thing you can do is delete a remote file after you download it. This can be useful when a remote host expects a file to be removed when it has been retrieved. Use the double-D flag, such as &#8220;get -DD&#8221; to do this.</p>
<dt>
<dd> The <i>get</i> command lets you retrieve entire directory trees, too. Although it may not work with some remote systems, you can try &#8220;get -R&#8221; with a directory to download the directory and its contents.</p>
<dt>
<dd> When using the &#8220;-R&#8221; flag, you can also use the &#8220;-T&#8221; flag to disable automatic on-the-fly TAR mode for downloading whole directory trees. The program uses TAR whenever possible since this usually preserves symbolic links and file permissions. TAR mode can also result in faster transfers for directories containing many small files, since a single data connection can be used rather than an FTP data connection for each small file. The downside to using TAR is that it forces downloading of the whole directory, even if you had previously downloaded a portion of it earlier, so you may want to use this option if you want to resume downloading of a directory.</p>
<dt>jobs</p>
<dd> Views the list of currently executing <i>NcFTP</i> background tasks. This actually just runs <i>ncftpbatch -l</i> for you.</p>
<dt>lcd</p>
<dd> The <i>lcd</i> command is the first of a few &#8220;l&#8221; commands that work with the local host. This changes the current working directory on the local host. If you want to download files into a different local directory, you could use <i>lcd</i> to change to that directory and then do your downloads.</p>
<dt>lchmod</p>
<dd> Runs &#8220;/bin/chmod&#8221; on the local host.</p>
<dt>lls</p>
<dd> Another local command that comes in handy is the <i>lls</i> command, which runs &#8220;/bin/ls&#8221; on the local host and displays the results in the program&#8217;s window. You can use the same flags with <i>lls</i> as you would in your command shell, so you can do things like:</p>
<dt>
<dd>
<pre>
lcd ~/doc
lls -lrt p*.txt
</pre>
<dt>lmkdir</p>
<dd> Runs &#8220;/bin/mkdir&#8221; on the local host.</p>
<dt>lookup</p>
<dd> The program also has a built-in interface to the name service via the <i>lookup</i> command. This means you can lookup entries for remote hosts, like:</p>
<dt>
<dd>
<pre>
lookup cse.unl.edu <a href="ftp://ftp.cs.unl.edu">ftp.cs.unl.edu</a> sphygmomanometer.unl.edu
</pre>
<dt>
<dd> prints:</p>
<dt>
<dd>
<pre><code>
cse.unl.edu &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
129.93.33.1 typhoon.unl.edu &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
129.93.33.24 sphygmomanometer.unl.edu &amp;nbsp;
&amp;nbsp;
129.93.33.126
</code></pre>
<dt>
<dd> There is also a more detailed option, enabled with &#8220;-v,&#8221; i.e.:</p>
<dt>
<dd>
<pre>
lookup -v cse.unl.edu <a href="ftp://ftp.cs.unl.edu">ftp.cs.unl.edu</a>
</pre>
<dt>
<dd> prints:</p>
<dt>
<dd>
cse.unl.edu : &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
Name : &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
cse.unl.edu<br />
    &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
Address : &amp;nbsp;<br />
&amp;nbsp;<br />
129.93.33.1 ftp.cs.unl.edu : &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
Name : &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
typhoon.unl.edu<br />
    &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
Alias : &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
ftp.cs.unl.edu<br />
    &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
Address : &amp;nbsp;<br />
&amp;nbsp;<br />
129.93.33.24</p>
<dt>
<dd> You can also give <i>IP</i> addresses, so this would work too:</p>
<dt>
<dd>
<pre>
lookup 129.93.33.24
</pre>
<dt>
<dd> prints:</p>
<dt>
<dd>
<pre><code>
typhoon.unl.edu &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
129.93.33.24
</code></pre>
<dt>lpage</p>
<dd> Views a local file one page at a time, with your preferred $PAGER program.</p>
<dt>lpwd</p>
<dd> Prints the current local directory. Use this command when you forget where you are on your local machine.</p>
<dt>lrename</p>
<dd> Runs &#8220;/bin/mv&#8221; on the local host.</p>
<dt>lrm</p>
<dd> Runs &#8220;/bin/rm&#8221; on the local host.</p>
<dt>lrmdir</p>
<dd> Runs &#8220;/bin/rmdir&#8221; on the local host.</p>
<dt>ls</p>
<dd> Prints a directory listing from the remote system. It tries to behave like <i>UNIX</i>&#8216;s &#8220;/bin/ls -CF&#8221; command. If the remote server seems to be a <i>UNIX</i> host, you can also use the same flags you would with <i>ls</i>, for instance</p>
<dt>
<dd>
<pre>
ls -rt
</pre>
<dt>
<dd> would try to act like</p>
<dt>
<dd>
<pre>
/bin/ls -CFrt
</pre>
<dt>
<dd> would on <i>UNIX</i>.</p>
<dt>
<dd> <i>ncftp</i> has a powerful built-in system for dealing with directory listings. It tries to cache each one, so if you list the same directory, odds are it will display instantly. Behind the scenes, <i>ncftp</i> always tries a long listing, and then reformats it as it needs to. So even if your first listing of a directory was a regular &#8220;ls&#8221; which displayed the files in columns, your next listing could be &#8220;ls -lrt&#8221; and <i>ncftp</i> would still use the cached directory listing to quickly display the information for you!</p>
<dt>mkdir</p>
<dd> Creates a new directory on the remote host. For many public archives, you won&#8217;t have the proper access permissions to do that.</p>
<dt>open</p>
<dd> Establishes an FTP control connection to a remote host. By default, <i>ncftp</i> logs in anonymously to the remote host. You may want to use a specific user account when you log in, so you can use the &#8220;-u&#8221; flag to specify which user. This example shows how to <i>open</i> the host &#8220;bowser.nintendo.co.jp&#8221; using the username &#8220;mario:&#8221;</p>
<dt>
<dd>
<pre>
open -u mario bowser.nintendo.co.jp
</pre>
<dt>
<dd> Here is a list of options available for use with the <i>open</i> command:</p>
<dt>
<dd> <code>-u </code><i>XX</i> Use username <i>XX</i> instead of anonymous.</p>
<dt>
<dd> <code>-p </code><i>XX</i> Use password <i>XX</i> with the username.</p>
<dt>
<dd> <code>-j </code><i>XX</i> Use account <i>XX</i> in supplement to the username and password (deprecated).</p>
<dt>
<dd> <code>-P </code><i>XX</i> Use port number <i>XX</i> instead of the default FTP service port (21).</p>
<dt>page</p>
<dd> Browses a remote file one page at a time, using your $PAGER program. This is useful for reading README&#8217;s on the remote host without downloading them first.</p>
<dt>pdir and pls</p>
<dd> These commands are equivalent to <i>dir</i> and <i>ls</i> respectively, only they feed their output to your pager. These commands are useful if the directory listing scrolls off your screen.</p>
<dt>put</p>
<dd> Copies files from the local host to the remote machine&#8217;s current working directory. To place a copy of &#8220;xx.zip&#8221; and &#8220;yy.zip&#8221; in the remote directory, you could try:</p>
<dt>
<dd>
<pre>
put xx.zip yy.zip
</pre>
<dt>
<dd> You could also accomplish that by using a wildcard expression, such as:</p>
<dt>
<dd>
<pre>
put *.zip
</pre>
<dt>
<dd> This command is similar to the behavior of other FTP programs&#8217; <i>mput</i> command. To send a remote file but give it a different name on your host, you can use the &#8220;-z&#8221; flag. This example shows how to upload a file called &#8220;ncftpd-2.0.6.tar.gz&#8221; but name it remotely as &#8220;NFTPD206.TGZ:&#8221;</p>
<dt>
<dd>
<pre>
put -z ncftpd-2.0.6.tar.gz NFTPD206.TGZ
</pre>
<dt>
<dd> The program <i>does not</i> try to &#8220;resume&#8221; uploads by default. If you do want to resume an upload, use the &#8220;-z&#8221; flag.</p>
<dt>
<dd> There are also times where you want to append to an existing remote file. You can do this by using the &#8220;-A&#8221; flag, for example</p>
<dt>
<dd>
<pre>
put -A log11.txt
</pre>
<dt>
<dd> would append to a file named &#8220;log11.txt&#8221; if it existed on the remote server.</p>
<dt>
<dd> Another thing you can do is delete a local file after you upload it. Use the double-D flag, such as &#8220;put -DD&#8221; to do this.</p>
<dt>
<dd> The <i>put</i> command lets you send entire directory trees, too. It should work on all remote systems, so you can try &#8220;put -R&#8221; with a directory to upload the directory and its contents.</p>
<dt>pwd</p>
<dd> Prints the current remote working directory. A portion of the pathname is also displayed in the shell&#8217;s prompt.</p>
<dt>quit</p>
<dd> Of course, when you finish using the program, type <i>quit</i> to end the program (You could also use <i>bye</i>, <i>exit</i>, or <i>^D</i>).</p>
<dt>quote</p>
<dd> This can be used to send a direct <i>FTP Protocol</i> command to the remote server. Generally this isn&#8217;t too useful to the average user.</p>
<dt>rename</p>
<dd> If you need to change the name of a remote file, you can use the <i>rename</i> command, like:</p>
<dt>
<dd>
<pre>
rename SPHYGMTR.TAR sphygmomanometer-2.3.1.tar
</pre>
<dt>rhelp</p>
<dd> Sends a help request to the remote server. The list of <i>FTP Protocol</i> commands is often printed, and sometimes some other information that is actually useful, like how to reach the site administrator.</p>
<dt>
<dd> Depending on the remote server, you may be able to give a parameter to the server also, like:</p>
<dt>
<dd>
<pre>
rhelp NLST
</pre>
<dt>
<dd> One server responded:</p>
<dt>
<dd>
<pre>
Syntax: NLST [ &lt;sp&gt; path-name ]
</pre>
<dt>rm</p>
<dd> If you need to delete a remote file you can try the <i>rm</i> command. Much of the time this won&#8217;t work because you won&#8217;t have the proper access permissions. This command doesn&#8217;t accept any flags, so you can&#8217;t nuke a whole tree by using &#8220;-rf&#8221; flags like you can on <i>UNIX</i>.</p>
<dt>rmdir</p>
<dd> Similarly, the <i>rmdir</i> command removes a directory. Depending on the remote server, you may be able to remove a non-empty directory, so be careful.</p>
<dt>set</p>
<dd> This lets you configure some program variables, which are saved between runs in the <i>$HOME/.ncftp/prefs</i> file. The basic syntax is:</p>
<dt>
<dd>
<pre>
set &lt;option&gt; &lt;value&gt;
</pre>
<dt>
<dd> For example, to change the value you use for the anonymous password, you might do:</p>
<dt>
<dd>
<pre>
set anon-password devnull [at] example.com
</pre>
<dt>
<dd> See the next section for a list of things you change.</p>
<dt>show</p>
<dd> This lets you display program variables. You can do &#8220;show all&#8221; to display all of them, or give a variable name to just display that one, such as:</p>
<dt>
<dd>
<pre>
show anon-password
</pre>
<dt>site</p>
<dd> One obscure command you may have to use someday is <i>site</i>. The <i>FTP Protocol</i> allows for &#8220;site specific&#8221; commands. These &#8220;site&#8221; commands vary of course, such as:</p>
<dt>
<dd>
<pre>
site chmod 644 README
</pre>
<dt>
<dd> Actually, <i>ncftp</i>&#8216;s <i>chmod</i> command really does the above.</p>
<dt>
<dd> Try doing one of these to see what the remote server supports, if any:</p>
<dt>
<dd>
<pre>
rhelp SITE
site help
</pre>
<dt>type</p>
<dd> You may need to change transfer types during the course of a session with a server. You can use the <i>type</i> command to do this. Try one of these:</p>
<dt>
<dd>
<pre>
type ascii
type binary
type image
</pre>
<dt>
<dd> The <i>ascii</i> command is equivalent to &#8220;type a&#8221;, and the <i>binary</i> command is equivalent to &#8220;type i&#8221; and &#8220;type b&#8221;.</p>
<dt>umask</p>
<dd> Sets the process&#8217; <i>umask</i> on the remote server, if it has any concept of a umask, i.e.:</p>
<dt>
<dd>
<pre>
umask 077
</pre>
<dt>
<dd> However, this is not a standard command, so remote FTP servers may not support it.</p>
<dt>version</p>
<dd> This command dumps some information about the particular edition of the program you are using, and how it was installed on your system.</dl>
<h3>VARIABLE REFERENCE</h3>
<dl>
<dt>anon-password</p>
<dd> Specifies what to use for the password when logging in anonymously. Internet convention has been to use your E-mail address as a courtesy to the site administrator. If you change this, be aware that some sites require (i.e. they check for) valid E-mail addresses.</p>
<dt>auto-resume</p>
<dd> <i>NcFTP</i> 3 now prompts the user by default when you try to download a file that already exists locally, or upload a file that already exists remotely. Older versions of the program automatically guessed whether to overwrite the existing file or attempt to resume where it left off, but sometimes the program would guess wrong. If you would prefer that the program always guess which action to take, set this variable to <i>yes</i>, otherwise, leave it set to <i>no</i> and the program will prompt you for which action to take.</p>
<dt>auto-ascii</p>
<dd> If set to a list of pipe-character delimited extensions, files with these extensions will be sent in ASCII mode even if binary mode is currently in effect. This option allows you to transfer most files in binary, with the exception of a few well-known file types that should be sent in ASCII. This option is enabled by default, and set to a list of common extensions (e.g., <i>.txt</i> and <i>.html</i>).</p>
<dt>autosave-bookmark-changes</p>
<dd> With the advent of version 3 of <i>NcFTP</i>, the program treats bookmarks more like they would with your web browser, which means that once you bookmark the site, the remote directory is static. If you set this variable to <i>yes</i>, then the program will automatically update the bookmark&#8217;s starting remote directory with the directory you were in when you closed the site. This behavior would be more like that of <i>NcFTP</i> version 2.</p>
<dt>confirm-close</p>
<dd> By default the program will ask you when a site you haven&#8217;t bookmarked is about to be closed. To turn this prompt off, you can set this variable to <i>no</i>.</p>
<dt>connect-timeout</p>
<dd> Previous versions of the program used a single timeout value for everything. You can now have different values for different operations. However, you probably do not need to change these from the defaults unless you have special requirements.</p>
<dt>
<dd> The <i>connect-timeout</i> variable controls how long to wait, in seconds, for a connection establishment to complete before considering it hopeless. You can choose to not use a timeout at all by setting this to -1.</p>
<dt>control-timeout</p>
<dd> This is the timer used when <i>ncftp</i> sends an FTP command over the control connection to the remote server. If the server hasn&#8217;t replied in that many seconds, it considers the session lost.</p>
<dt>logsize</p>
<dd> This is controls how large the transfer log ($HOME/.ncftp/log) can grow to, in kilobytes. The default is 200, for 200kB; if you don&#8217;t want a log, set this to 0.</p>
<dt>pager</p>
<dd> This is the external program to use to view a text file, and is <i>more</i> by default.</p>
<dt>passive</p>
<dd> This controls <i>ncftp</i>&#8216;s behavior for data connections, and can be set to one of <i>on</i>, <i>off</i>, or the default, <i>optional</i>. When passive mode is on, <i>ncftp</i> uses the FTP command primitive <i>PASV</i> to have the client establish data connections to the server. The default FTP protocol behavior is to use the FTP command primitive <i>PORT</i> which has the server establish data connections to the client. The default setting for this variable, <i>optional</i>, allows <i>ncftp</i> to choose whichever method it deems necessary.</p>
<dt>progress-meter</p>
<dd> You can change how the program reports file transfer status. Select from meter <i>2</i>, <i>1</i>, or <i>0</i>.</p>
<dt>redial-delay</p>
<dd> When a host is busy or unavailable, the program waits this number of seconds before trying again. The smallest you can set this is to 10 seconds &#8212; so if you were planning on being inconsiderate, think again.</p>
<dt>save-passwords</p>
<dd> If you set this variable to <i>yes</i>, the program will save passwords along with the bookmarks you save. While this makes non-anonymous logins more convenient, this can be very dangerous since your account information is now sitting in the $HOME/.ncftp/bookmarks file. The passwords aren&#8217;t in clear text, but it is still trivial to decode them if someone wants to make a modest effort.</p>
<dt>show-status-in-xterm-titlebar</p>
<dd> If set to <i>yes</i> and operating from within an xterm window, the program will change the window&#8217;s titlebar accordingly.</p>
<dt>so-bufsize</p>
<dd> If your operating system supports TCP Large Windows, you can try setting this variable to the number of bytes to set the TCP/IP socket buffer to. This option won&#8217;t be of much use unless the remote server also supports large window sizes and is pre-configured with them enabled.</p>
<dt>xfer-timeout</p>
<dd> This timer controls how long to wait for data blocks to complete. Don&#8217;t set this too low or else your transfers will timeout without completing.</dl>
<h3>FIREWALL AND PROXY CONFIGURATION</h3>
<p> You may find that your network administrator has placed a firewall between your machine and the Internet, and that you cannot reach external hosts. </p>
<p> The answer may be as simple as setting <i>ncftp</i> to use <i>passive</i> mode only, which you can do from a <i>ncftp</i> command prompt like this: </p>
<pre>
set passive on
</pre>
<p> The reason for this is because many firewalls do not allow incoming connections to the site, but do allow users to establish outgoing connections. A passive data connection is established by the client to the server, whereas the default is for the server to establish the connection to the client, which firewalls may object to. Of course, you now may have problems with sites whose primitive FTP servers do not support passive mode. </p>
<p> Otherwise, if you know you need to have <i>ncftp</i> communicate directly with a firewall or proxy, you can try editing the separate <i>$HOME/.ncftp/firewall</i> configuration file. This file is created automatically the first time you run the program, and contains all the information you need to get the program to work in this setup. </p>
<p> The basics of this process are configuring a firewall (proxy) host to go through, a user account and password for authentication on the firewall, and which type of firewall method to use. You can also setup an exclusion list, so that <i>ncftp</i> does not use the firewall for hosts on the local network.</p>
<h2>FILES</h2>
<dl>
<dt>$HOME/.ncftp/bookmarks</p>
<dd> Saves bookmark and host information.</p>
<dt>$HOME/.ncftp/firewall</p>
<dd> Firewall access configuration file.</p>
<dt>$HOME/.ncftp/prefs</p>
<dd> Program preferences.</p>
<dt>$HOME/.ncftp/trace</p>
<dd> Debugging output for entire program run.</p>
<dt>$HOME/.ncftp/v3init</p>
<dd> Used to tell if this version of the program has run before.</p>
<dt>$HOME/.ncftp/spool/</p>
<dd> Directory where background jobs are stored in the form of spool configuration files.</p>
<dt>$HOME/.ncftp/spool/log</p>
<dd> Information for background data transfer processes.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>PATH</p>
<dd> User&#8217;s search path, used to find the <i>ncftpbatch</i> program, pager, and some other system utilities.</p>
<dt>PAGER</p>
<dd> Program to use to view text files one page at a time.</p>
<dt>TERM</p>
<dd> If the program was compiled with support for <i>GNU Readline</i> it will need to know how to manipulate the terminal correctly for line-editing, etc. The pager program will also take advantage of this setting.</p>
<dt>HOME</p>
<dd> By default, the program writes its configuration data in a <i>.ncftp</i> subdirectory of the <i>HOME</i> directory.</p>
<dt>NCFTPDIR</p>
<dd> If set, the program will use this directory instead of <i>$HOME/.ncftp</i>. This variable is optional except for those users whose home directory is the root directory.</p>
<dt>COLUMNS</p>
<dd> Both the built-in <i>ls</i> command and the external <i>ls</i> command need this to determine how many screen columns the terminal has.</dl>
<h2>BUGS</h2>
<p> There are no such sites named <i>bowser.nintendo.co.jp</i> or <i>sphygmomanometer.unl.edu</i>. </p>
<p> Auto-resume should check the file timestamps instead of relying upon just the file sizes, but it is difficult to do this reliably within FTP. </p>
<p> Directory caching and recursive downloads depend on <i>UNIX</i>-like behavior of the remote host.</p>
<h2>AUTHOR</h2>
<p> Mike Gleason, NcFTP Software (<a rel="nofollow" href="http://www.ncftp.com">http://www.ncftp.com</a>).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ncftpput/">ncftpput</a></i>(1), <i><a href="/docs/linux/man/1-ncftpget/">ncftpget</a></i>(1), <i><a href="/docs/linux/man/1-ncftpbatch/">ncftpbatch</a></i>(1), <i><a href="/docs/linux/man/1-ftp/">ftp</a></i>(1), <i><a href="/docs/linux/man/1-rcp/">rcp</a></i>(1), <i><a href="/docs/linux/man/1-tftp/">tftp</a></i>(1). </p>
<p> <i>LibNcFTP</i> (<a rel="nofollow" href="http://www.ncftp.com/libncftp">http://www.ncftp.com/libncftp</a>). </p>
<p> <i>NcFTPd</i> (<a rel="nofollow" href="http://www.ncftp.com/ncftpd">http://www.ncftp.com/ncftpd</a>).</p>
<h2>THANKS</h2>
<p> Thanks to everyone who uses the program. Your support is what drives me to improve the program! </p>
<p> I thank Dale Botkin and Tim Russell at my former ISP, <i>Probe Technology</i>. </p>
<p> Ideas and some code contributed by my partner, Phil Dietz. </p>
<p> Thanks to Brad Mittelstedt and Chris Tjon, for driving and refining the development of the backbone of this project, <i>LibNcFTP</i>. </p>
<p> I&#8217;d like to thank my former system administrators, most notably Charles Daniel, for making testing on a variety of platforms possible, letting me have some extra disk space, and for maintaining the UNL FTP site. </p>
<p> For testing versions 1 and 2 above and beyond the call of duty, I am especially grateful to: Phil Dietz, Kok Hon Yin, and Andrey A. Chernov (ache [at] astral.msk.su). </p>
<p> Thanks to Tim MacKenzie (t.mackenzie [at] trl.oz.au) for the original filename completion code for version 2.3.0 and 2.4.2. </p>
<p> Thanks to DaviD W. Sanderson (dws [at] ora.com), for helping me out with the man page. </p>
<p> Thanks to those of you at UNL who appreciate my work. </p>
<p> Thanks to Red Hat Software for honoring my licensing agreement, but more importantly, thanks for providing a solid and affordable development platform.</p>
<h2>APOLOGIES</h2>
<p> To the users, for not being able to respond personally to most of your inquiries. </p>
<p> To Phil, for things not being the way they should be. </p>
<h2>Index</h2>
