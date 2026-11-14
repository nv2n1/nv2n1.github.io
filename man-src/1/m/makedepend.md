---
title: "makedepend(1)"
name: "makedepend"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makedepend/"
description: "makedepend – create dependencies in makefiles"
---

<h2 class="name">NAME</h2>
<p> makedepend &#8211; create dependencies in makefiles </p>
<h2>SYNOPSIS</h2>
<p> <code>makedepend</code> [ <code>-D</code><i>name</i><code>=</code>def ] [ <code>-D</code><i>name</i> ] [ <code>-I</code><i>includedir</i> ] [ <code>-Y</code><i>includedir</i> ] [ <code>-a</code> ] [ <code>-f</code><i>makefile</i> ] [ <code>-include</code><i>&nbsp;<wbr>file</i> ] [ <code>-o</code><i>objsuffix</i> ] [ <code>-p</code><i>objprefix</i> ] [ <code>-s</code><i>string</i> ] [ <code>-w</code><i>width</i> ] [ <code>-v</code> ] [ <code>-m</code> ] [ &#8212; <i>otheroptions</i> &#8212; ] <i>sourcefile</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>makedepend</code> program reads each <i>sourcefile</i> in sequence and parses it like a C-preprocessor, processing all <i>#include,</i> <i>#define,</i> <i>#undef,</i> <i>#ifdef,</i> <i>#ifndef,</i> <i>#endif,</i> <i>#if,</i> <i>#elif</i> and <i>#else</i> directives so that it can correctly tell which <i>#include,</i> directives would be used in a compilation. Any <i>#include,</i> directives can reference files having other <i>#include</i> directives, and parsing will occur in these files as well. </p>
<p> Every file that a <i>sourcefile</i> includes, directly or indirectly, is what <code>makedepend</code> calls a <i>dependency.</i> These dependencies are then written to a <i>makefile</i> in such a way that <code><a href="/docs/linux/man/1-make/">make</a>(1)</code> will know which object files must be recompiled when a dependency has changed. </p>
<p> By default, <code>makedepend</code> places its output in the file named <i>makefile</i> if it exists, otherwise <i>Makefile.</i> An alternate makefile may be specified with the <code>-f</code> option. It first searches the makefile for the line </p>
<p> # DO NOT DELETE THIS LINE &#8212; make depend depends on it. </p>
<p> or one provided with the <code>-s</code> option, as a delimiter for the dependency output. If it finds it, it will delete everything following this to the end of the makefile and put the output after this line. If it doesn&#8217;t find it, the program will append the string to the end of the makefile and place the output following that. For each <i>sourcefile</i> appearing on the command line, <code>makedepend</code> puts lines in the makefile of the form </p>
<p>&nbsp;<wbr>&nbsp;<wbr>sourcefile.o: dfile &#8230; </p>
<p> Where <i>sourcefile.o</i> is the name from the command line with its suffix replaced with &#8220;.o&#8221;, and <i>dfile</i> is a dependency discovered in a <i>#include</i> directive while parsing <i>sourcefile</i> or one of the files it included.</p>
<h2>EXAMPLE</h2>
<p> Normally, <code>makedepend</code> will be used in a makefile target so that typing &#8220;make depend&#8221; will bring the dependencies up to date for the makefile. For example, </p>
<pre><code>
SRCS &amp;nbsp;
= &amp;nbsp;
file1.c file2.c... CFLAGS &amp;nbsp;
= &amp;nbsp;
- O - DHACK - I../ foobar - xyz
    depend:
        makedepend-- &amp;nbsp;
$(CFLAGS) &amp; nbsp;
--&amp;nbsp;
$(SRCS)
</code></pre>
<h2>OPTIONS</h2>
<p> The program will ignore any option that it does not understand so that you may use the same arguments that you would for <code><a href="/docs/linux/man/1-cc/">cc</a>(1).</code></p>
<dl>
<dt><code>-D</code><i>name</i>=<i>def</i> or -D<i>name</i></p>
<dd> Define. This places a definition for <i>name</i> in <code>makedepend&#8217;s</code> symbol table. Without <i>=def</i> the symbol becomes defined as &#8220;1&#8221;.</p>
<dt><code>-I</code><i>includedir</i></p>
<dd> Include directory. This option tells <code>makedepend</code> to prepend <i>includedir</i> to its list of directories to search when it encounters a <i>#include</i> directive. By default, <code>makedepend</code> only searches the standard include directories (usually /usr/include and possibly a compiler-dependent directory).</p>
<dt><code>-Y</code><i>includedir</i></p>
<dd> Replace all of the standard include directories with the single specified include directory; you can omit the <i>includedir</i> to simply prevent searching the standard include directories.</p>
<dt><code>-a</code></p>
<dd> Append the dependencies to the end of the file instead of replacing them.</p>
<dt><code>-f</code><i>makefile</i></p>
<dd> Filename. This allows you to specify an alternate makefile in which <code>makedepend</code> can place its output. Specifying &#8220;-&#8221; as the file name (i.e., <code>-f-</code>) sends the output to standard output instead of modifying an existing file.</p>
<dt><code>-include </code><i>file</i></p>
<dd> Process file as input, and include all the resulting output before processing the regular input file. This has the same affect as if the specified file is an include statement that appears before the very first line of the regular input file.</p>
<dt><code>-o</code><i>objsuffix</i></p>
<dd> Object file suffix. Some systems may have object files whose suffix is something other than &#8220;.o&#8221;. This option allows you to specify another suffix, such as &#8220;.b&#8221; with <i>-o.b</i> or &#8220;:obj&#8221; with <i>-o:obj</i> and so forth.</p>
<dt><code>-p</code><i>objprefix</i></p>
<dd> Object file prefix. The prefix is prepended to the name of the object file. This is usually used to designate a different directory for the object file. The default is the empty string.</p>
<dt><code>-s</code><i>string</i></p>
<dd> Starting string delimiter. This option permits you to specify a different string for <code>makedepend</code> to look for in the makefile.</p>
<dt><code>-w</code><i>width</i></p>
<dd> Line width. Normally, <code>makedepend</code> will ensure that every output line that it writes will be no wider than 78 characters for the sake of readability. This option enables you to change this width.</p>
<dt><code>-v</code></p>
<dd> Verbose operation. This option causes <code>makedepend</code> to emit the list of files included by each input file.</p>
<dt><code>-m</code></p>
<dd> Warn about multiple inclusion. This option causes <code>makedepend</code> to produce a warning if any input file includes another file more than once. In previous versions of <code>makedepend</code> this was the default behavior; the default has been changed to better match the behavior of the C compiler, which does not consider multiple inclusion to be an error. This option is provided for backward compatibility, and to aid in debugging problems related to multiple inclusion.</p>
<dt><code>&#8212; </code><i>options</i> &#8212;</p>
<dd> If <code>makedepend</code> encounters a double hyphen (&#8211;) in the argument list, then any unrecognized argument following it will be silently ignored; a second double hyphen terminates this special treatment. In this way, <code>makedepend</code> can be made to safely ignore esoteric compiler arguments that might normally be found in a CFLAGS <code>make</code> macro (see the <code>EXAMPLE</code> section above). All options that <code>makedepend</code> recognizes and appear between the pair of double hyphens are processed normally.</dl>
<h2>ALGORITHM</h2>
<p> The approach used in this program enables it to run an order of magnitude faster than any other &#8220;dependency generator&#8221; I have ever seen. Central to this performance are two assumptions: that all files compiled by a single makefile will be compiled with roughly the same <i>-I</i> and <i>-D</i> options; and that most files in a single directory will include largely the same files. </p>
<p> Given these assumptions, <code>makedepend</code> expects to be called once for each makefile, with all source files that are maintained by the makefile appearing on the command line. It parses each source and include file exactly once, maintaining an internal symbol table for each. Thus, the first file on the command line will take an amount of time proportional to the amount of time that a normal C preprocessor takes. But on subsequent files, if it encounters an include file that it has already parsed, it does not parse it again. </p>
<p> For example, imagine you are compiling two files, <i>file1.c</i> and <i>file2.c,</i> they each include the header file <i>header.h,</i> and the file <i>header.h</i> in turn includes the files <i>def1.h</i> and <i>def2.h.</i> When you run the command </p>
<p>&nbsp;<wbr>makedepend file1.c file2.c </p>
<p> <code>makedepend</code> will parse <i>file1.c</i> and consequently, <i>header.h</i> and then <i>def1.h</i> and <i>def2.h.</i> It then decides that the dependencies for this file are </p>
<p>&nbsp;<wbr>file1.o: header.h def1.h def2.h </p>
<p> But when the program parses <i>file2.c</i> and discovers that it, too, includes <i>header.h,</i> it does not parse the file, but simply adds <i>header.h,</i> <i>def1.h</i> and <i>def2.h</i> to the list of dependencies for <i>file2.o.</i></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cc/">cc</a>(1), <a href="/docs/linux/man/1-make/">make</a>(1)</p>
<h2>BUGS</h2>
<p> <code>makedepend</code> parses, but does not currently evaluate, the SVR4 #predicate(token-list) preprocessor expression; such expressions are simply assumed to be true. This may cause the wrong <i>#include</i> directives to be evaluated. </p>
<p> Imagine you are parsing two files, say <i>file1.c</i> and <i>file2.c,</i> each includes the file <i>def.h.</i> The list of files that <i>def.h</i> includes might truly be different when <i>def.h</i> is included by <i>file1.c</i> than when it is included by <i>file2.c.</i> But once <code>makedepend</code> arrives at a list of dependencies for a file, it is cast in concrete.</p>
<h2>AUTHOR</h2>
<p> Todd Brunhoff, Tektronix, Inc. and MIT Project Athena </p>
<h2>Index</h2>
