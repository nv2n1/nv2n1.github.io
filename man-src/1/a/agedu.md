---
title: "agedu(1)"
name: "agedu"
section: "1"
letter: "a"
url: "/docs/linux/man/1-agedu/"
description: "agedu – correlate disk usage with last-access times to identify large and disused data"
---

<h2>NAME</h2>
<p> <code>agedu</code> &#8211; correlate disk usage with last-access times to identify large and disused data</p>
<h2>SYNOPSIS</h2>
<pre><code>
agedu &amp;nbsp;
[&amp;nbsp; options &amp; nbsp;] &amp; nbsp;
action &amp;nbsp;
[action...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>agedu</code> scans a directory tree and produces reports about how much disk space is used in each directory and subdirectory, and also how that usage of disk space corresponds to files with last-access times a long time ago. </p>
<p> In other words, <code>agedu</code> is a tool you might use to help you free up disk space. It lets you see which directories are taking up the most space, as <code>du</code> does; but unlike <code>du</code>, it also distinguishes between large collections of data which are still in use and ones which have not been accessed in months or years &#8211; for instance, large archives downloaded, unpacked, used once, and never cleaned up. Where <code>du</code> helps you find what&#8217;s using your disk space, <code>agedu</code> helps you find what&#8217;s <i>wasting</i> your disk space. </p>
<p> <code>agedu</code> has several operating modes. In one mode, it scans your disk and builds an index file containing a data structure which allows it to efficiently retrieve any information it might need. Typically, you would use it in this mode first, and then run it in one of a number of `query&#8217; modes to display a report of the disk space usage of a particular directory and its subdirectories. Those reports can be produced as plain text (much like <code>du</code>) or as HTML. <code>agedu</code> can even run as a miniature web server, presenting each directory&#8217;s HTML report with hyperlinks to let you navigate around the file system to similar reports for other directories. </p>
<p> So you would typically start using <code>agedu</code> by telling it to do a scan of a directory tree and build an index. This is done with a command such as </p>
<pre>
$&nbsp;<wbr><code>agedu -s&nbsp;<wbr>/home/fred</code>
</pre>
<p> which will build a large data file called <code>agedu.dat</code> in your current directory. (If that current directory is <i>inside</i> <code>/home/fred</code>, don&#8217;t worry &#8211; <code>agedu</code> is smart enough to discount its own index file.) </p>
<p> Having built the index, you would now query it for reports of disk space usage. If you have a graphical web browser, the simplest and nicest way to query the index is by running <code>agedu</code> in web server mode: </p>
<pre>
$&nbsp;<wbr><code>agedu -w</code>
</pre>
<p> which will print (among other messages) a URL on its standard output along the lines of </p>
<pre>
URL:&nbsp;<wbr><a rel="nofollow" href="http://127.0.0.1:48638/">http://127.0.0.1:48638/</a>
</pre>
<p> (That URL will always begin with `<code>127.</code>&#8216;, meaning that it&#8217;s in the <code>localhost</code> address space. So only processes running on the same computer can even try to connect to that web server, and also there is access control to prevent other users from seeing it &#8211; see below for more detail.) </p>
<p> Now paste that URL into your web browser, and you will be shown a graphical representation of the disk usage in <code>/home/fred</code> and its immediate subdirectories, with varying colours used to show the difference between disused and recently-accessed data. Click on any subdirectory to descend into it and see a report for its subdirectories in turn; click on parts of the pathname at the top of any page to return to higher-level directories. When you&#8217;ve finished browsing, you can just press Ctrl-D to send an end-of-file indication to <code>agedu</code>, and it will shut down. </p>
<p> After that, you probably want to delete the data file <code>agedu.dat</code>, since it&#8217;s pretty large. In fact, the command <code>agedu -R</code> will do this for you; and you can chain <code>agedu</code> commands on the same command line, so that instead of the above you could have done </p>
<pre>
$&nbsp;<wbr><code>agedu -s&nbsp;<wbr>/home/fred -w -R</code>
</pre>
<p> for a single self-contained run of <code>agedu</code> which builds its index, serves web pages from it, and cleans it up when finished. </p>
<p> If you don&#8217;t have a graphical web browser, you can do text-based queries as well. Having scanned <code>/home/fred</code> as above, you might run </p>
<pre>
$&nbsp;<wbr><code>agedu -t&nbsp;<wbr>/home/fred</code>
</pre>
<p> which again gives a summary of the disk usage in <code>/home/fred</code> and its immediate subdirectories; but this time <code>agedu</code> will print it on standard output, in much the same format as <code>du</code>. If you then want to find out how much <i>old</i> data is there, you can add the <code>-a</code> option to show only files last accessed a certain length of time ago. For example, to show only files which haven&#8217;t been looked at in six months or more: </p>
<pre>
$&nbsp;<wbr><code>agedu -t&nbsp;<wbr>/home/fred -a 6m</code>
</pre>
<p> That&#8217;s the essence of what <code>agedu</code> does. It has other modes of operation for more complex situations, and the usual array of configurable options. The following sections contain a complete reference for all its functionality.</p>
<h2>OPERATING MODES</h2>
<p> This section describes the operating modes supported by <code>agedu</code>. Each of these is in the form of a command-line option, sometimes with an argument. Multiple operating-mode options may appear on the command line, in which case <code>agedu</code> will perform the specified actions one after another. For instance, as shown in the previous section, you might want to perform a disk scan and immediately launch a web server giving reports from that scan.</p>
<dl>
<dt><code>-s</code> <i>directory</i> or <code>&#8211;scan</code> <i>directory</i></p>
<dd> In this mode, <code>agedu</code> scans the file system starting at the specified directory, and indexes the results of the scan into a large data file which other operating modes can query.</p>
<dl>
<dt>
<dd>
<p> By default, the scan is restricted to a single file system (since the expected use of <code>agedu</code> is that you would probably use it because a particular disk partition was running low on space). You can remove that restriction using the <code>&#8211;cross-fs</code> option; other configuration options allow you to include or exclude files or entire subdirectories from the scan. See the next section for full details of the configurable options. </p>
<p> The index file is created with restrictive permissions, in case the file system you are scanning contains confidential information in its structure. </p>
<p> Index files are dependent on the characteristics of the CPU architecture you created them on. You should not expect to be able to move an index file between different types of computer and have it continue to work. If you need to transfer the results of a disk scan to a different kind of computer, see the <code>-D</code> and <code>-L</code> options below.</dl>
<dt><code>-w</code> or <code>&#8211;web</code></p>
<dd> In this mode, <code>agedu</code> expects to find an index file already written. It allocates a network port, and starts up a web server on that port which serves reports generated from the index file. By default it invents its own URL and prints it out.</p>
<dl>
<dt>
<dd>
<p> The web server runs until <code>agedu</code> receives an end-of-file event on its standard input. (The expected usage is that you run it from the command line, immediately browse web pages until you&#8217;re satisfied, and then press Ctrl-D.) </p>
<p> In case the index file contains any confidential information about your file system, the web server protects the pages it serves from access by other people. On Linux, this is done transparently by means of using <code>/proc/net/tcp</code> to check the owner of each incoming connection; failing that, the web server will require a password to view the reports, and <code>agedu</code> will print the password it invented on standard output along with the URL. </p>
<p> Configurable options for this mode let you specify your own address and port number to listen on, and also specify your own choice of authentication method (including turning authentication off completely) and a username and password of your choice.</dl>
<dt><code>-t</code> <i>directory</i> or <code>&#8211;text</code> <i>directory</i></p>
<dd> In this mode, <code>agedu</code> generates a textual report on standard output, listing the disk usage in the specified directory and all its subdirectories down to a fixed depth. By default that depth is 1, so that you see a report for <i>directory</i> itself and all of its immediate subdirectories. You can configure a different depth using <code>-d</code>, described in the next section.</p>
<dl>
<dt>
<dd>
<p> Used on its own, <code>-t</code> merely lists the <i>total</i> disk usage in each subdirectory; <code>agedu</code>&#8216;s additional ability to distinguish unused from recently-used data is not activated. To activate it, use the <code>-a</code> option to specify a minimum age. </p>
<p> The directory structure stored in <code>agedu</code>&#8216;s index file is treated as a set of literal strings. This means that you cannot refer to directories by synonyms. So if you ran <code>agedu -s .</code>, then all the path names you later pass to the <code>-t</code> option must be either `<code>.</code>&#8216; or begin with `<code>./</code>&#8216;. Similarly, symbolic links within the directory you scanned will not be followed; you must refer to each directory by its canonical, symlink-free pathname.</dl>
<dt><code>-R</code> or <code>&#8211;remove</code></p>
<dd> In this mode, <code>agedu</code> deletes its index file. Running just <code>agedu -R</code> on its own is therefore equivalent to typing <code>rm agedu.dat</code>. However, you can also put <code>-R</code> on the end of a command line to indicate that <code>agedu</code> should delete its index file after it finishes performing other operations.</p>
<dt><code>-D</code> or <code>&#8211;dump</code></p>
<dd> In this mode, <code>agedu</code> reads an existing index file and produces a dump of its contents on standard output. This dump can later be loaded into a new index file, perhaps on another computer.</p>
<dt><code>-L</code> or <code>&#8211;load</code></p>
<dd> In this mode, <code>agedu</code> expects to read a dump produced by the <code>-D</code> option from its standard input. It constructs an index file from that dump, exactly as it would have if it had read the same data from a disk scan in <code>-s</code> mode.</p>
<dt><code>-S</code> <i>directory</i> or <code>&#8211;scan-dump</code> <i>directory</i></p>
<dd> In this mode, <code>agedu</code> will scan a directory tree and convert the results straight into a dump on standard output, without generating an index file at all. So running <code>agedu -S /path</code> should produce equivalent output to that of <code>agedu -s /path -D</code>, except that the latter will produce an index file as a side effect whereas <code>-S</code> will not.</p>
<dl>
<dt>
<dd>
<p> (The output will not be exactly <i>identical</i>, due to a difference in treatment of last-access times on directories. However, it should be effectively equivalent for most purposes. See the documentation of the <code>&#8211;dir-atime</code> option in the next section for further detail.)</dl>
<dt><code>-H</code> <i>directory</i> or <code>&#8211;html</code> <i>directory</i></p>
<dd> In this mode, <code>agedu</code> will generate an HTML report of the disk usage in the specified directory and its immediate subdirectories, in the same form that it serves from its web server in <code>-w</code> mode. However, this time, a single HTML report will be generated and simply written to standard output, with no hyperlinks pointing to other similar pages.</dl>
<h2>OPTIONS</h2>
<p> This section describes the various configuration options that affect <code>agedu</code>&#8216;s operation in one mode or another. </p>
<p> The following option affects nearly all modes (except <code>-S</code>):</p>
<dl>
<dt><code>-f</code> <i>filename</i> or <code>&#8211;file</code> <i>filename</i></p>
<dd> Specifies the location of the index file which <code>agedu</code> creates, reads or removes depending on its operating mode. By default, this is simply `<code>agedu.dat</code>&#8216;, in whatever is the current working directory when you run <code>agedu</code>.</dl>
<p> The following options affect the disk-scanning modes, <code>-s</code> and <code>-S</code>:</p>
<dl>
<dt><code>&#8211;cross-fs</code> and <code>&#8211;no-cross-fs</code></p>
<dd> These configure whether or not the disk scan is permitted to cross between different file systems. The default is not to: <code>agedu</code> will normally skip over subdirectories on which a different file system is mounted. This makes it convenient when you want to free up space on a particular file system which is running low. However, in other circumstances you might wish to see general information about the use of space no matter which file system it&#8217;s on (for instance, if your real concern is your backup media running out of space, and if your backups do not treat different file systems specially); in that situation, use <code>&#8211;cross-fs</code>.</p>
<dl>
<dt>
<dd>
<p> (Note that this default is the opposite way round from the corresponding option in <code>du</code>.)</dl>
<dt><code>&#8211;prune</code> <i>wildcard</i> and <code>&#8211;prune-path</code> <i>wildcard</i></p>
<dd> These cause particular files or directories to be omitted entirely from the scan. If <code>agedu</code>&#8216;s scan encounters a file or directory whose name matches the wildcard provided to the <code>&#8211;prune</code> option, it will not include that file in its index, and also if it&#8217;s a directory it will skip over it and not scan its contents.</p>
<dl>
<dt>
<dd>
<p> Note that in most Unix shells, wildcards will probably need to be escaped on the command line, to prevent the shell from expanding the wildcard before <code>agedu</code> sees it. </p>
<p> <code>&#8211;prune-path</code> is similar to <code>&#8211;prune</code>, except that the wildcard is matched against the entire pathname instead of just the filename at the end of it. So whereas <code>&#8211;prune *a*b*</code> will match any file whose actual name contains an <code>a</code> somewhere before a <code>b</code>, <code>&#8211;prune-path *a*b*</code> will also match a file whose name contains <code>b</code> and which is inside a directory containing an <code>a</code>, or any file inside a directory of that form, and so on.</dl>
<dt><code>&#8211;exclude</code> <i>wildcard</i> and <code>&#8211;exclude-path</code> <i>wildcard</i></p>
<dd> These cause particular files or directories to be omitted from the index, but not from the scan. If <code>agedu</code>&#8216;s scan encounters a file or directory whose name matches the wildcard provided to the <code>&#8211;exclude</code> option, it will not include that file in its index &#8211; but unlike <code>&#8211;prune</code>, if the file in question is a directory it will still scan its contents and index them if they are not ruled out themselves by <code>&#8211;exclude</code> options.</p>
<dl>
<dt>
<dd>
<p> As above, <code>&#8211;exclude-path</code> is similar to <code>&#8211;exclude</code>, except that the wildcard is matched against the entire pathname.</dl>
<dt><code>&#8211;include</code> <i>wildcard</i> and <code>&#8211;include-path</code> <i>wildcard</i></p>
<dd> These cause particular files or directories to be re-included in the index and the scan, if they had previously been ruled out by one of the above exclude or prune options. You can interleave include, exclude and prune options as you wish on the command line, and if more than one of them applies to a file then the last one takes priority.</p>
<dl>
<dt>
<dd>
<p> For example, if you wanted to see only the disk space taken up by MP3 files, you might run </p>
<pre><code>
$ &amp;nbsp;
agedu - s.--exclude &amp;nbsp;
'*' &amp; nbsp;
--include &amp;nbsp;
'*.mp3'
</code></pre>
<p> which will cause everything to be omitted from the scan, but then the MP3 files to be put back in. If you then wanted only a subset of those MP3s, you could then exclude some of them again by adding, say, `<code>&#8211;exclude-path &#8216;./queen/*&#8217;</code>&#8216; (or, more efficiently, `<code>&#8211;prune ./queen</code>&#8216;) on the end of that command. </p>
<p> As with the previous two options, <code>&#8211;include-path</code> is similar to <code>&#8211;include</code> except that the wildcard is matched against the entire pathname.</dl>
<dt><code>&#8211;progress</code>, <code>&#8211;no-progress</code> and <code>&#8211;tty-progress</code></p>
<dd> When <code>agedu</code> is scanning a directory tree, it will typically print a one-line progress report every second showing where it has reached in the scan, so you can have some idea of how much longer it will take. (Of course, it can&#8217;t predict <i>exactly</i> how long it will take, since it doesn&#8217;t know which of the directories it hasn&#8217;t scanned yet will turn out to be huge.)</p>
<dl>
<dt>
<dd>
<p> By default, those progress reports are displayed on <code>agedu</code>&#8216;s standard error channel, if that channel points to a terminal device. If you need to manually enable or disable them, you can use the above three options to do so: <code>&#8211;progress</code> unconditionally enables the progress reports, <code>&#8211;no-progress</code> unconditionally disables them, and <code>&#8211;tty-progress</code> reverts to the default behaviour which is conditional on standard error being a terminal.</dl>
<dt><code>&#8211;dir-atime</code> and <code>&#8211;no-dir-atime</code></p>
<dd> In normal operation, <code>agedu</code> ignores the atimes (last access times) on the <i>directories</i> it scans: it only pays attention to the atimes of the <i>files</i> inside those directories. This is because directory atimes tend to be reset by a lot of system administrative tasks, such as <code>cron</code> jobs which scan the file system for one reason or another &#8211; or even other invocations of <code>agedu</code> itself, though it tries to avoid modifying any atimes if possible. So the literal atimes on directories are typically not representative of how long ago the data in question was last accessed with real intent to use that data in particular.</p>
<dl>
<dt>
<dd>
<p> Instead, <code>agedu</code> makes up a fake atime for every directory it scans, which is equal to the newest atime of any file in or below that directory (or the directory&#8217;s last <i>modification</i> time, whichever is newest). This is based on the assumption that all <i>important</i> accesses to directories are actually accesses to the files inside those directories, so that when any file is accessed all the directories on the path leading to it should be considered to have been accessed as well. </p>
<p> In unusual cases it is possible that a directory itself might embody important data which is accessed by reading the directory. In that situation, <code>agedu</code>&#8216;s atime-faking policy will misreport the directory as disused. In the unlikely event that such directories form a significant part of your disk space usage, you might want to turn off the faking. The <code>&#8211;dir-atime</code> option does this: it causes the disk scan to read the original atimes of the directories it scans. </p>
<p> The faking of atimes on directories also requires a processing pass over the index file after the main disk scan is complete. <code>&#8211;dir-atime</code> also turns this pass off. Hence, this option affects the <code>-L</code> option as well as <code>-s</code> and <code>-S</code>. </p>
<p> (The previous section mentioned that there might be subtle differences between the output of <code>agedu -s /path -D</code> and <code>agedu -S /path</code>. This is why. Doing a scan with <code>-s</code> and then dumping it with <code>-D</code> will dump the fully faked atimes on the directories, whereas doing a scan-to-dump with <code>-S</code> will dump only <i>partially</i> faked atimes &#8211; specifically, each directory&#8217;s last modification time &#8211; since the subsequent processing pass will not have had a chance to take place. However, loading either of the resulting dump files with <code>-L</code> will perform the atime-faking processing pass, leading to the same data in the index file in each case. In normal usage it should be safe to ignore all of this complexity.)</dl>
<dt><code>&#8211;mtime</code></p>
<dd> This option causes <code>agedu</code> to index files by their last modification time instead of their last access time. You might want to use this if your last access times were completely useless for some reason: for example, if you had recently searched every file on your system, the system would have lost all the information about what files you hadn&#8217;t recently accessed before then. Using this option is liable to be less effective at finding genuinely wasted space than the normal mode (that is, it will be more likely to flag things as disused when they&#8217;re not, so you will have more candidates to go through by hand looking for data you don&#8217;t need), but may be better than nothing if your last-access times are unhelpful.</dl>
<p> The following option affects all the modes that generate reports: the web server mode <code>-w</code>, the stand-alone HTML generation mode <code>-H</code> and the text report mode <code>-t</code>.</p>
<dl>
<dt><code>&#8211;files</code></p>
<dd> This option causes <code>agedu</code>&#8216;s reports to list the individual files in each directory, instead of just giving a combined report for everything that&#8217;s not in a subdirectory.</dl>
<p> The following options affect the web server mode <code>-w</code>, and in one case also the stand-alone HTML generation mode <code>-H</code>:</p>
<dl>
<dt><code>-r</code> <i>age range</i> or <code>&#8211;age-range</code> <i>age range</i></p>
<dd> The HTML reports produced by <code>agedu</code> use a range of colours to indicate how long ago data was last accessed, running from red (representing the most disused data) to green (representing the newest). By default, the lengths of time represented by the two ends of that spectrum are chosen by examining the data file to see what range of ages appears in it. However, you might want to set your own limits, and you can do this using <code>-r</code>.</p>
<dl>
<dt>
<dd>
<p> The argument to <code>-r</code> consists of a single age, or two ages separated by a minus sign. An age is a number, followed by one of `<code>y</code>&#8216; (years), `<code>m</code>&#8216; (months), `<code>w</code>&#8216; (weeks) or `<code>d</code>&#8216; (days). The first age in the range represents the oldest data, and will be coloured red in the HTML; the second age represents the newest, coloured green. If the second age is not specified, it will default to zero (so that green means data which has been accessed <i>just now</i>). </p>
<p> For example, <code>-r 2y</code> will mark data in red if it has been unused for two years or more, and green if it has been accessed just now. <code>-r 2y-3m</code> will similarly mark data red if it has been unused for two years or more, but will mark it green if it has been accessed three months ago or later.</dl>
<dt><code>&#8211;address</code> <i>addr</i>[<code>:</code><i>port</i>]</p>
<dd> Specifies the network address and port number on which <code>agedu</code> should listen when running its web server. If you want <code>agedu</code> to listen for connections coming in from any source, you should probably specify the special IP address <code>0.0.0.0</code>. If the port number is omitted, an arbitrary unused port will be chosen for you and displayed.</p>
<dl>
<dt>
<dd>
<p> If you specify this option, <code>agedu</code> will not print its URL on standard output (since you are expected to know what address you told it to listen to).</dl>
<dt><code>&#8211;auth</code> <i>auth-type</i></p>
<dd> Specifies how <code>agedu</code> should control access to the web pages it serves. The options are as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>magic</code></p>
<dd> This option only works on Linux, and only when the incoming connection is from the same machine that <code>agedu</code> is running on. On Linux, the special file <code>/proc/net/tcp</code> contains a list of network connections currently known to the operating system kernel, including which user id created them. So <code>agedu</code> will look up each incoming connection in that file, and allow access if it comes from the same user id under which <code>agedu</code> itself is running. Therefore, in <code>agedu</code>&#8216;s normal web server mode, you can safely run it on a multi-user machine and no other user will be able to read data out of your index file.</p>
<dt><code>basic</code></p>
<dd> In this mode, <code>agedu</code> will use HTTP Basic authentication: the user will have to provide a username and password via their browser. <code>agedu</code> will normally make up a username and password for the purpose, but you can specify your own; see below.</p>
<dt><code>none</code></p>
<dd> In this mode, the web server is unauthenticated: anyone connecting to it has full access to the reports generated by <code>agedu</code>. Do not do this unless there is nothing confidential at all in your index file, or unless you are certain that nobody but you can run processes on your computer.</p>
<dt><code>default</code></p>
<dd> This is the default mode if you do not specify one of the above. In this mode, <code>agedu</code> will attempt to use Linux magic authentication, but if it detects at startup time that <code>/proc/net/tcp</code> is absent or non-functional then it will fall back to using HTTP Basic authentication and invent a user name and password.</dl>
</dl>
<dt><code>&#8211;auth-file</code> <i>filename</i> or <code>&#8211;auth-fd</code> <i>fd</i></p>
<dd> When <code>agedu</code> is using HTTP Basic authentication, these options allow you to specify your own user name and password. If you specify <code>&#8211;auth-file</code>, these will be read from the specified file; if you specify <code>&#8211;auth-fd</code> they will instead be read from a given file descriptor which you should have arranged to pass to <code>agedu</code>. In either case, the authentication details should consist of the username, followed by a colon, followed by the password, followed <i>immediately</i> by end of file (no trailing newline, or else it will be considered part of the password).</dl>
<h2>LIMITATIONS</h2>
<p> The data file is pretty large. The core of <code>agedu</code> is the tree-based data structure it uses in its index in order to efficiently perform the queries it needs; this data structure requires <code>O(N log N)</code> storage. This is larger than you might expect; a scan of my own home directory, containing half a million files and directories and about 20Gb of data, produced an index file over 60Mb in size. Furthermore, since the data file must be memory-mapped during most processing, it can never grow larger than available address space, so a <i>really</i> big filesystem may need to be indexed on a 64-bit computer. (This is one reason for the existence of the <code>-D</code> and <code>-L</code> options: you can do the scanning on the machine with access to the filesystem, and the indexing on a machine big enough to handle it.) </p>
<p> The data structure also does not usefully permit access control within the data file, so it would be difficult &#8211; even given the willingness to do additional coding &#8211; to run a system-wide <code>agedu</code> scan on a <code>cron</code> job and serve the right subset of reports to each user. </p>
<p> In certain circumstances, <code>agedu</code> can report false positives (reporting files as disused which are in fact in use) as well as the more benign false negatives (reporting files as in use which are not). This arises when a file is, semantically speaking, `read&#8217; without actually being physically <i>read</i>. Typically this occurs when a program checks whether the file&#8217;s mtime has changed and only bothers re-reading it if it has; programs which do this include <code>rsync</code>(<i>1</i>) and <code>make</code>(<i>1</i>). Such programs will fail to update the atime of unmodified files despite depending on their continued existence; a directory full of such files will be reported as disused by <code>agedu</code> but deleting them will cause trouble.</p>
<h2>LICENCE</h2>
<p> <code>agedu</code> is free software, distributed under the MIT licence. Type <code>agedu &#8211;licence</code> to see the full licence text. </p>
<h2>Index</h2>
