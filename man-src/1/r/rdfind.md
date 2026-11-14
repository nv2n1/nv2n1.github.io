---
title: "rdfind(1)"
name: "rdfind"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdfind/"
description: "rdfind – finds duplicate files"
---

<h2>NAME</h2>
<p> rdfind &#8211; finds duplicate files</p>
<h2>SYNOPSIS</h2>
<p> <code>rdfind [ options ] </code> <i>directory1 | file1</i> <code>[</code> <i>directory2 | file2</i> <code>] &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>rdfind</code> finds duplicate files across and/or within several directories. It calculates checksum only if necessary. rdfind runs in O(Nlog(N)) time with N being the number of files. </p>
<p> If two (or more) equal files are found, the program decides which of them is the original and the rest are considered duplicates. This is done by ranking the files to each other and deciding which has the highest rank. See section RANKING for details. </p>
<p> If you need better control over the ranking than given, you can use some preprocessor which sorts the file names in desired order and then run the program using xargs. See examples below for how to use find and xargs in conjunction with rdfind. </p>
<p> To include files or directories that have names starting with -, use rdfind ./- to not confuse them with options. </p>
<h2>RANKING</h2>
<p> Given two or more equal files, the one with the highest rank is selected to be the original and the rest are duplicates. The rules of ranking are given below, where the rules are executed from start until an original has been found. Given two files A and B which have equal content, the ranking is as follows: </p>
<p> If A was found while scanning an input argument earlier than than B, A is higher ranked. </p>
<p> If A was found at a depth lower than B, A is higher ranked (A closer to the root) </p>
<p> If A was found earlier than B, A is higher ranked. </p>
<p> The last rule is needed when two files are found in the same directory (obviously not given in separate arguments, otherwise the first rule applies) and gives the same order between the files as the operating system delivers the files while listing the directory. This is operating system specific behaviour. </p>
<h2>OPTIONS</h2>
<p> <code>Searching options etc:</code></p>
<dl>
<dt>-ignoreempty true|false</p>
<dd> Ignore empty files. (default)</p>
<dt>-followsymlinks true|false</p>
<dd> Follow symlinks. Default is false.</p>
<dt>-removeidentinode true|false</p>
<dd> removes items found which have identical inode and device ID. Default is true.</p>
<dt>-checksum md5|sha1</p>
<dd> what type of checksum to be used: md5 or sha1. Default is md5.</dl>
<p> <code>Action options:</code></p>
<dl>
<dt>-makesymlinks true|false</p>
<dd> Replace duplicate files with symbolic links</p>
<dt>-makehardlinks true|false</p>
<dd> Replace duplicate files with hard links</p>
<dt>-makeresultsfile true|false</p>
<dd> Make a results file results.txt (default) in the current directory.</p>
<dt>-outputname name</p>
<dd> Make the results file name to be &quot;name&quot; instead of the default results.txt.</p>
<dt>-deleteduplicates true|false</p>
<dd> Delete (unlink) files.</dl>
<p> <code>General options:</code></p>
<dl>
<dt>-sleep Xms</p>
<dd> sleeps X milliseconds between reading each file, to reduce load. Default is 0 (no sleep). Note that only a few values are supported at present: 0,1-5,10,25,50,100 milliseconds.</p>
<dt>-n, -dryrun true|(false)</p>
<dd> displays what should have been done, don&#8217;t actually delete or link anything.</p>
<dt>-h, -help, &#8211;help</p>
<dd> displays brief help message.</p>
<dt>-v, -version, &#8211;version</p>
<dd> displays version number.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Search for duplicate files in home directory and a backup directory:</p>
<dd> <code>rdfind ~ /mnt/backup</code></p>
<dt>Delete duplicate in a backup directory:</p>
<dd> <code>rdfind -deleteduplicates true /mnt/backup</code></p>
<dt>Search for duplicate files in directories called foo:</p>
<dd> <code>find . -type d -name foo -print0 |xargs -0 rdfind</code></dl>
<h2>FILES</h2>
<p> <i>results.txt</i> (the default name is results.txt and can be changed with option outputname, see above) The results file results.txt will contain one row per duplicate file found, along with a header row explaining the columns. A text describes why the file is considered a duplicate: </p>
<p> DUPTYPE_UNKNOWN some internal error </p>
<p> DUPTYPE_FIRST_OCCURRENCE the file that is considered to be the original. </p>
<p> DUPTYPE_WITHIN_SAME_TREE files in the same tree (found when processing the directory in the same input argument as the original) </p>
<p> DUPTYPE_OUTSIDE_TREE the file is found during processing another input argument than the original.</p>
<h2>ENVIRONMENT</h2>
<h2>DIAGNOSTICS</h2>
<h2>EXIT VALUES</h2>
<p> 0 on success, nonzero otherwise.</p>
<h2>BUGS/FEATURES</h2>
<p> When specifying the same directory twice, it keeps the first encountered as the most important (original), and the rest as duplicates. This might not be what you want. </p>
<p> The symlink creates absolute links. This might not be what you want. To create relative links instead, you may use the symlinks (2) command, which is able to convert absolute links to relative links. </p>
<p> Older versions unfortunately contained a misspelling on the word occurrence. This is now corrected (since 1.3), which might affect user scripts parsing the output file written by rdfind. </p>
<p> There are lots of enhancements left to do. Please contribute!</p>
<h2>SECURITY CONSIDERATIONS</h2>
<p> Avoid manipulating the directories while rdfind is reading. rdfind is quite brittle in that case. Especially, when deleting or making links, rdfind can be subject to a symlink attack. Use with care!</p>
<h2>AUTHOR</h2>
<p> Paul Dreik 2006, reachable at rdfind [at] pauldreik.se Rdfind can be found at <a rel="nofollow" href="https://rdfind.pauldreik.se/">https://rdfind.pauldreik.se/</a> </p>
<p> Do you find rdfind useful? Drop me a line! It is always fun to hear from people who actually use it and what data collections they run it on.</p>
<h2>THANKS</h2>
<p> Several persons have helped with suggestions and improvements: Niels Möller, Carl Payne and Salvatore Ansani. Thanks also to you who tested the program and sent me feedback.</p>
<h2>VERSION</h2>
<p> 1.3.5 (release date 2017-01-04)</p>
<h2>COPYRIGHT</h2>
<p> This program is distributed under GPLv2 or later, at your option.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-md5sum/">md5sum</a></code>(1), <code><a href="/docs/linux/man/1-sha1sum/">sha1sum</a></code>(1), <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/2-symlinks/">symlinks</a>(2)</code> </p>
<h2>Index</h2>
