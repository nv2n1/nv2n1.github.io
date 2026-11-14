---
title: "pcresample(3)"
name: "pcresample"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcresample/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Pcre Sample Program</h2>
<p>A simple, complete demonstration program, to get you started with using PCRE, is supplied in the file <i>pcredemo.c</i> in the PCRE distribution. A listing of this program is given in the <code>pcredemo</code> documentation. If you do not have a copy of the PCRE distribution, you can save this listing to re-create <i>pcredemo.c</i>. </p>
<p> The demonstration program, which uses the original PCRE 8-bit library, compiles the regular expression that is its first argument, and matches it against the subject string in its second argument. No PCRE options are set, and default character tables are used. If matching succeeds, the program outputs the portion of the subject that matched, together with the contents of any captured substrings. </p>
<p> If the -g option is given on the command line, the program then goes on to check for further matches of the same regular expression in the same subject string. The logic is a little bit tricky because of the possibility of matching an empty string. Comments in the code explain what is going on. </p>
<p> If PCRE is installed in the standard include and library directories for your operating system, you should be able to compile the demonstration program using this command: </p>
<p>&nbsp;<wbr>&nbsp;gcc -o pcredemo pcredemo.c -lpcre </p>
<p> If PCRE is installed elsewhere, you may need to add additional options to the command line. For example, on a Unix-like system that has PCRE installed in <i>/usr/local</i>, you can compile the demonstration program using a command like this: </p>
<p>&nbsp;<wbr>&nbsp;gcc -o pcredemo -I/usr/local/include pcredemo.c&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-L/usr/local/lib -lpcre </p>
<p> In a Windows environment, if you want to statically link the program against a non-dll <code>pcre.a</code> file, you must uncomment the line that defines PCRE_STATIC before including <code>pcre.h</code>, because otherwise the <code>pcre_malloc()</code> and <code>pcre_free()</code> exported functions will be declared <code>__declspec(dllimport)</code>, with unwanted results. </p>
<p> Once you have compiled and linked the demonstration program, you can run simple tests like this: </p>
<p>&nbsp;<wbr>&nbsp;./pcredemo&nbsp;&#8216;cat|dog&#8217;&nbsp;&#8216;the cat sat on the mat&#8217;<br />
&nbsp;<wbr>&nbsp;./pcredemo -g&nbsp;&#8216;cat|dog&#8217;&nbsp;&#8216;the dog sat on the cat&#8217; </p>
<p> Note that there is a much more comprehensive test program, called <code>pcretest</code>, which supports many more facilities for testing regular expressions and both PCRE libraries. The <code>pcredemo</code> program is provided as a simple coding example. </p>
<p> If you try to run <code>pcredemo</code> when PCRE is not installed in the standard library directory, you may get an error like this on some operating systems (e.g. Solaris): </p>
<p>&nbsp;<wbr>&nbsp;ld.so.1: a.out: fatal: libpcre.so.0: open failed: No such file or directory </p>
<p> This is caused by the way shared library support works on those systems. You need to add </p>
<p>&nbsp;<wbr>&nbsp;-R/usr/local/lib </p>
<p> (for example) to the compile command to get round this problem.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 10 January 2012
Copyright (c) 1997-2012 University of Cambridge.</pre>
