---
title: "ftff(1)"
name: "ftff"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftff/"
description: "ftff – fault tolerant file find utility"
---

<h2 class="name">NAME</h2>
<p> ftff &#8211; fault tolerant file find utility </p>
<h2>SYNOPSIS</h2>
<p> <code>ftff</code> [-#fFhIpq][-t#][start_directory] file_to_find</p>
<h2>DESCRIPTION</h2>
<p> <code>ftff</code> recursively descends the directory hierarchy and reports all objects in the file system with a name that approximately matches the given filename. </p>
<p> <code>ftff</code> achieves fault tolerance by calculating the so called Weighted Levenshtein Distance. The Levenshtein Distance is defined as the minimum number of character insertions, deletions and replacements that transform a string <i>A </i> into a string <i>B.</i> </p>
<p> <code>ftff</code> behaves like </p>
<p> &#8216;find start_directory -name file_to_find -print&#8217; </p>
<p> with the following differences:</p>
<dl>
<dt>&#8211;</p>
<dd> ftff is fault tolerant</p>
<dt>&#8211;</p>
<dd> ftff is NOT case sensitive</p>
<dt>&#8211;</p>
<dd> the level of fault tolerance can be adjusted by specifying the optional parameter <code>tolerance.</code> A <code>tolerance</code> of 0 specifies exact match.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h</i></p>
<dd> Prints a little help/usage information.</p>
<dt><i>-f</i></p>
<dd> Follow symbolic links on directories. Note: a symbolic link like &quot;somewhere -&gt; ..&quot; causes naturally an endless loop. By default <code>ftff</code> does not follow symbolic links to directories.</p>
<dt><i>-F</i></p>
<dd> Classify the file type by appending a character to each file name. This character is:<br />
 <i>&#8216;*&#8217; </i> for regular files that are executable<br />
 <i>&#8216;/&#8217; </i> for directories<br />
 <i>&#8216;@&#8217; </i> for symbolic links<br />
 <i>&#8216;|&#8217; </i> for FIFOs<br />
 <i>&#8216;=&#8217; </i> for sockets</p>
<dt><i>-p</i></p>
<dd> print the actual distance value in front of the filename. This value is equal to the number of insertions, deletions and replacements necessary to transform the file that was found into the search key (the file_to_find).</p>
<dt><i>-q</i></p>
<dd> keep quiet and do not print any warning about non readable directories.</p>
<dt><i>-# or -t#</i></p>
<dd> Set the fault tolerance level to #. The fault tolerance level is an integer in the range 0-255. It specifies the maximum number of errors permitted in finding the approximate match. The default tolerance is (strlen(searchpattern) &#8211; number of wildcards)/6 + 1</p>
<dt><i>-I</i></p>
<dd> Do case sensitive search (default is case in-sensitive)</dl>
<dl>
<dt><i>file_to_find</i></p>
<dd> The filename to search for. &#8216;*&#8217; and &#8216;?&#8217; can be used as wildcards.<br />
 &#8216;?&#8217; denotes one single character.<br />
 &#8216;*&#8217; denotes an arbitrary number of characters.</p>
<dt><i>start_directory</i></p>
<dd> The directory to start the search. The current directory is the default.</dl>
<p> The last argument to ftff is not parsed for options as the program needs at least one file-name argument. This means that <i>ftff -x</i> will not complain about a wrong option but search for the file named -x.</p>
<h2>EXAMPLE</h2>
<p> <i>ftff </i> samething </p>
<p> This will e.g. find a file called something or sameting or sum-thing or &#8230; </p>
<p> To find all files that start with any prefix, have something like IOComm in between and end on a two letter suffix: </p>
<p> <i>ftff </i> &#8216;*iocomm.??&#8217; </p>
<p> To find all files that exactly start with the prefix DuPeg: </p>
<p> <i>ftff -0 </i> &#8216;dupeg*&#8217; </p>
<h2>BUGS</h2>
<p> The wildcards <code>&#8216;?&#8217;</code> and <code>&#8216;*&#8217;</code> can not be escaped. These characters function always as wildcards. This is however not a big problem since there is normally hardly any file that has these characters in its name.</p>
<h2>AUTHOR</h2>
<p> Guido Socher (guido [at] linuxfocus.org)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-whichman/">whichman</a></code>(1), <code><a href="/docs/linux/man/1-find/">find</a></code>(1) </p>
<h2>Index</h2>
