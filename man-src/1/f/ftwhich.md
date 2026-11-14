---
title: "ftwhich(1)"
name: "ftwhich"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftwhich/"
description: "ftwhich – fault tolerant search for a command name"
---

<h2 class="name">NAME</h2>
<p> ftwhich &#8211; fault tolerant search for a command name </p>
<h2>SYNOPSIS</h2>
<p> <code>ftwhich</code> [-#hIp][-t#] program_name</p>
<h2>DESCRIPTION</h2>
<p> <code>ftwhich </code> is a fault tolerant version of the <a href="/docs/linux/man/1-which/">which</a>(1) command. <code>ftwhich</code> searches for a given program in all directories included in your PATH environment variable and reports all files with a name that approximately matches the given <i>program_name.</i> </p>
<p> <code>ftwhich</code> achieves fault tolerance by calculating the so called Weighted Levenshtein Distance. The Levenshtein Distance is defined as the minimum number of character insertions, deletions and replacements that transform a string <i>A </i> into a string <i>B.</i> </p>
<p> <code>ftwhich</code> is similar to the <code>which</code> command with the following differences:</p>
<dl>
<dt>&#8211;</p>
<dd> ftwhich is by default NOT case sensitive</p>
<dt>&#8211;</p>
<dd> ftwhich is fault tolerant</p>
<dt>&#8211;</p>
<dd> Some shells have a build in <code>which</code> command that will also search aliases. <code>ftwhich</code> can naturally not search for aliases as it does not know about alias definitions.</p>
<dt>&#8211;</p>
<dd> <code>ftwhich </code> lists all files that approximately match. The files first shown take preference over files of the same name printed later as they are from directories listed earlier in the PATH.</p>
<dt>&#8211;</p>
<dd> The level of fault tolerance can be adjusted by specifying the optional parameter <code>tolerance.</code> A <code>tolerance</code> of 0 specifies exact match.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h</i></p>
<dd> Prints help/usage information.</p>
<dt><i>-I</i></p>
<dd> Do case sensitive search (default is case in-sensitive)</p>
<dt><i>-p</i></p>
<dd> print the actual distance value in front of the found filename. This value is equal to the number of insertions, deletions and replacements necessary to transform the name of the found program into the search key.</p>
<dt><i>-# or -t#</i></p>
<dd> Set the fault tolerance level to #. The fault tolerance level is an integer in the range 0-255. It specifies the maximum number of errors permitted in finding the approximate match. The default tolerance is (strlen(searchpattern) &#8211; number of wildcards)/6 + 1</dl>
<dl>
<dt><i>program_name</i></p>
<dd> The program file to search for. &#8216;*&#8217; and &#8216;?&#8217; can be used as wildcards.<br />
 &#8216;?&#8217; denotes one single character.<br />
 &#8216;*&#8217; denotes an arbitrary number of characters.</dl>
<p> The last argument to ftwhich is not parsed for options as the program needs at least one program_name argument. This means that <i>ftwhich -x</i> will not complain about a wrong option but search for the program named -x.</p>
<h2>EXAMPLE</h2>
<p> Search for all programs like gcc in your PATH:<br />
 <i>ftwhich gcc</i><br />
 This will e.g. find gcc or cc or CC &#8230; </p>
<p> To find all files that start with any prefix and end in <i>config </i> and differ in 2 letters from the word <i>config:</i><br />
 <i>ftwhich -2</i> &#8216;*config&#8217; </p>
<p> To find all files that exactly start with the prefix <i>if:</i><br />
 <i>ftwhich -0 </i> &#8216;if*&#8217; </p>
<p> To find all clock programs:<br />
 <i>ftwhich -0 &#8216;*clock*&#8217;</i> </p>
<h2>BUGS</h2>
<p> The wildcards <code>&#8216;?&#8217;</code> and <code>&#8216;*&#8217;</code> can not be escaped. These characters function always as wildcards. This is however not a big problem since there is normally hardly any command that has these characters in its name.</p>
<h2>AUTHOR</h2>
<p> Guido Socher (guido [at] linuxfocus.org)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-whichman/">whichman</a></code>(1), <code><a href="/docs/linux/man/1-ftff/">ftff</a></code>(1) </p>
<h2>Index</h2>
