---
title: "pcre2sample(3)"
name: "pcre2sample"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2sample/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Pcre2 Sample Program</h2>
<p>A simple, complete demonstration program to get you started with using PCRE2 is supplied in the file <i>pcre2demo.c</i> in the <code>src</code> directory in the PCRE2 distribution. A listing of this program is given in the <code>pcre2demo</code> documentation. If you do not have a copy of the PCRE2 distribution, you can save this listing to re-create the contents of <i>pcre2demo.c</i>. </p>
<p> The demonstration program compiles the regular expression that is its first argument, and matches it against the subject string in its second argument. No PCRE2 options are set, and default character tables are used. If matching succeeds, the program outputs the portion of the subject that matched, together with the contents of any captured substrings. </p>
<p> If the -g option is given on the command line, the program then goes on to check for further matches of the same regular expression in the same subject string. The logic is a little bit tricky because of the possibility of matching an empty string. Comments in the code explain what is going on. </p>
<p> The code in <code>pcre2demo.c</code> is an 8-bit program that uses the PCRE2 8-bit library. It handles strings and characters that are stored in 8-bit code units. By default, one character corresponds to one code unit, but if the pattern starts with &quot;(*UTF)&quot;, both it and the subject are treated as UTF-8 strings, where characters may occupy multiple code units. </p>
<p> If PCRE2 is installed in the standard include and library directories for your operating system, you should be able to compile the demonstration program using a command like this: </p>
<p>&nbsp;<wbr>&nbsp;cc -o pcre2demo pcre2demo.c -lpcre2-8 </p>
<p> If PCRE2 is installed elsewhere, you may need to add additional options to the command line. For example, on a Unix-like system that has PCRE2 installed in <i>/usr/local</i>, you can compile the demonstration program using a command like this: </p>
<p>&nbsp;<wbr>&nbsp;cc -o pcre2demo -I/usr/local/include pcre2demo.c&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-L/usr/local/lib -lpcre2-8 </p>
<p> Once you have built the demonstration program, you can run simple tests like this: </p>
<p>&nbsp;<wbr>&nbsp;./pcre2demo&nbsp;&#8216;cat|dog&#8217;&nbsp;&#8216;the cat sat on the mat&#8217;<br />
&nbsp;<wbr>&nbsp;./pcre2demo -g&nbsp;&#8216;cat|dog&#8217;&nbsp;&#8216;the dog sat on the cat&#8217; </p>
<p> Note that there is a much more comprehensive test program, called <code>pcre2test</code>, which supports many more facilities for testing regular expressions using all three PCRE2 libraries (8-bit, 16-bit, and 32-bit, though not all three need be installed). The <code>pcre2demo</code> program is provided as a relatively simple coding example. </p>
<p> If you try to run <code>pcre2demo</code> when PCRE2 is not installed in the standard library directory, you may get an error like this on some operating systems (e.g. Solaris): </p>
<p>&nbsp;<wbr>&nbsp;ld.so.1: pcre2demo: fatal: libpcre2-8.so.0: open failed: No such file or directory </p>
<p> This is caused by the way shared library support works on those systems. You need to add </p>
<p>&nbsp;<wbr>&nbsp;-R/usr/local/lib </p>
<p> (for example) to the compile command to get round this problem.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 02 February 2016
Copyright (c) 1997-2016 University of Cambridge.</pre>
