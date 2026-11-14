---
title: "makedepf90(1)"
name: "makedepf90"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makedepf90/"
description: "makedepf90 – creates Makefile dependency list for Fortran source files."
---

<h2 class="name">NAME</h2>
<p> makedepf90 &#8211; creates Makefile dependency list for Fortran source files.</p>
<h2>SYNOPSIS</h2>
<p> <code>makedepf90 </code> [<code>-h</code>] [<code>-V</code>] [<code>-W</code>|<code>-Wmissing</code>] [<code>-Wconfused</code>] [<code>-m</code> <i>fmt</i>] [<code>-u</code> <i>modulename</i>] [<code>-d</code> <i>file</i>] [<code>-r</code> <i>rule</i>] [<code>-R</code> <i>file rule</i>] [<code>-fixed</code>|<code>-free</code>] [<code>-o</code> <i>name-of-executable</i>] [<code>-coco</code>] [<code>-D</code> <i>NAME</i>] [<code>-b</code> <i>path</i>] [<code>-I</code> <i>PATH1:PATH2:&#8230;</i>] [<code>-nosrc</code>] <i>sourcefile(s)</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>makedepf90</i> is a program for automatic creation of dependency lists and compilation rules for Makefiles. </p>
<p> The original idea was to provide the same functionality for Fortran as</p>
<dl>
<dt>
<dd>
<p> gcc -MM *.c</dl>
<p> does for C. Nowadays makedepf90 actually supersedes this functionality, making me wonder if I should extend makedepf90 to support C and C++ too ;-). </p>
<p> <i>makedepf90</i> supports both <code>modules</code>, <code>include</code>:s, <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) <code>#include</code>:s, <code><a href="/docs/linux/man/1-f90ppr/">f90ppr</a></code>(1) <code>$include</code>:s and <code><a href="/docs/linux/man/1-coco/">coco</a></code>(1) <code>??includes</code> and set-files. </p>
<p> <i>makedepf90</i> reads Fortran source files given on the command line, and writes a dependency list to stdout; for every file it writes a line with the following format:</p>
<dl>
<dt>
<dd>
<p> <i>targets</i> : <i>prerequisites</i></dl>
<p> <i>Targets</i> are the files that will be the result of compiling the file with the <code>-c</code> option, and <i>prerequisites</i> are files that are needed to compile the file. In addition, <i>makedepf90</i> can optionally create the dependency line and make-rule needed to link the final executable.</p>
<h3>Fortran dependencies</h3>
<p> The files needed to compile a file, i.e the <i>prerequisites</i> of the file are:</p>
<dl>
<dt><code>&#8212; </code></p>
<dd> The source file itself</p>
<dt><code>&#8212; </code></p>
<dd> Files with interface information about USEd modules, created by the compiler while compiling the modules (often named <i>modulename</i>.mod or something similar, hereafter called <i>mod-files</i>).</p>
<dt><code>&#8212; </code></p>
<dd> Include-files (including files included and mod-files of modules USEd from these include-files).</p>
<dt><code>&#8212;</code></p>
<dd> <code>Coco</code> set-files, if <code><a href="/docs/linux/man/1-coco/">coco</a></code>(1) is being used and set-files exist.</dl>
<p> Since different compilers use different naming conventions for the mod-files, listing them in the dependency list results in non-portable makefiles. Therefore it&#8217;s common practise to list the object file (<i>filename</i>.o) corresponding to the sourcefile containing the USEd modules instead. This is the default behaviour of <i>makedepf90</i>. To change this, use the <code>-m</code> option (e.g <code>-m &quot;%m.mod&quot;</code> if your compiler names the mod files <i>modulename</i>.mod) </p>
<p> Include files not found in the working directory will not be listed in the dependency list, assuming they are part of a (seldom changing) library not part of the program. Neither will mod-files of modules whose definitions aren&#8217;t found be listed by the same reason. </p>
<h2>OPTIONS</h2>
<p> These options may be given anywhere, in any order, on the command line. Space between an option and its argument is optional. Options may not be grouped (<code>-hW</code> is not the same thing as <code>-h -W</code>).</p>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> Print a short help message to stdout and quit.</p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd> Print version and copyright information to stdout and quit</p>
<dt><code>-W</code> or <code>-Wmissing</code></p>
<dd> Print warnings about missing modules and include files</p>
<dt><code>-Wconfused</code></p>
<dd> Print warnings when confused (either because of bugs in makedepf90 itself, or because of wierd things in your source files). If makedepf90 misses some dependencies, or do other wierd things, this option might give some idea on whats going on.</p>
<dt><code>-m</code><i> fmt</i></p>
<dd> Tell <i>makedepf90</i> that mod-files will have names of the format <i>fmt</i>. <i>fmt</i> may contain the modifiers <code>%f</code> for <i>filename</i> (without file name .suffix), <code>%m</code> for <i>modulename</i> (in lowercase), <code>%M</code> for <i>MODULENAME</i> (in uppercase) and <code>%%</code> for &#8216;%&#8217;. Default is &quot;%f.o&quot;.</p>
<dt><code>-u</code><i> modulename</i></p>
<dd> Ignore all modules named <i>modulename</i>.</p>
<dt><code>-d</code><i> file</i></p>
<dd> Make all targets dependent on <i>file</i>.</p>
<dt><code>-r</code><i> rule</i></p>
<dd> Add <i>rule</i> (indented by a tab) to all dependency lines except lines given rule(s) with the <code>-R</code> option.</dl>
<dl>
<dt>
<dd> <i>rule</i> may contains the following modifiers: <code>%f</code> for the name of the source file (without suffix) the dependency line is created for, and <code>%%</code> for &#8216;%&#8217;.</dl>
<dl>
<dt><code>-R</code><i> &#8216;pattern&#8217; &#8216;rule&#8217;</i></p>
<dd> Compile files matching the shell pattern <i>pattern</i> using the rule <i>rule</i>. In <i>pattern</i>, the following wildcards can be used: <code>*</code> = any number of any characters, <code>?</code> = any character and <code>[abc]</code> = any of <code>a</code>, <code>b</code> or <code>c</code>. Note that the patter-matching is to be performed by <i>makedepf90</i>, not the shell. Therefore <i>pattern</i> should be enclosed in quotes (<code>&quot;</code> or <code>&#8216;</code>). For <i>rule</i> applies the same rules as for <code>-r</code> above.</dl>
<dl>
<dt>
<dd> Note that there is a subtle difference between &quot;<code>-r</code> <i>rule</i>&quot; and &quot;<code>-R</code> &#8216;*&#8217; <i>rule</i>&quot;. In the former case <i>rule</i> will be applied only to lines not given any rule using <code>-R</code>, while in the latter case, <i>rule</i> will be applied to <i>all</i> lines.</dl>
<dl>
<dt><code>-fixed</code> / <code>-free</code></p>
<dd> Treat the files as fixed/free source format. If both options are given, the latter is used. Default: Files with suffixes <code>.f, .F, .for, .FOR </code>or<code> .ftn</code> are treated as fixed format and <code>.f90, .F90, .f95 </code>or<code> .F95</code> are treated as free format.</p>
<dt><code>-o</code><i> name</i></p>
<dd> This option will cause <i>makedepf90</i> to define the Makefile macro <code>FOBJ</code>=<i>objectfiles</i>, and a dependency line + rule for the final linking process to create the executable <i>name</i>. To set the linking rule, use the option <code>-l</code>.</p>
<dt><code>-l</code><i> rule</i></p>
<dd> Use <i>rule</i> when linking the executable. The default is<br />
 <code>$(FC) -o $@ $(FFLAGS) $(LDFLAGS) $(FOBJ) $(LIBS)</code>.<br />
 This option has no effect unless <code>-o</code> is used.</p>
<dt><code>-coco</code></p>
<dd> Look for <code><a href="/docs/linux/man/1-coco/">coco</a></code>(1) set-files (<code>coco</code> ??include:s are supported automatically). This option implies <code>-free</code>.</p>
<dt><code>-D</code><i> NAME</i></p>
<dd> Define the pre-processor symbol <i>NAME</i>.</p>
<dt><code>-b</code><i> path</i></p>
<dd> Dependency tree and link rule will assume objects are placed in <i>path</i>. This is useful if the build places object files in a different directory than the source files.</p>
<dt><code>-I</code><i> list-of-paths</i></p>
<dd> Look for source/include files in the <i>list-of-paths</i>, if not found in current working directory. Here, <i>list-of-paths</i> is a colon separated list of path names.</p>
<dt><code>-nosrc</code></p>
<dd> Don&#8217;t list the source file among the prerequisites. </p>
</dl>
<h2>EXAMPLES</h2>
<h3>Basic Usage</h3>
<p> Here&#8217;s an example of basic <i>makedepf90</i> usage together with <code><a href="/docs/linux/man/1-make/">make</a></code>(1). Create a file named <code>Makefile</code> with the following contents: </p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>FC&nbsp;<wbr>=&nbsp;<wbr>the compiler to use<br />
&nbsp;<wbr>FC=f90 </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Compiler options<br />
&nbsp;<wbr>FFLAGS=-O </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>List libraries used by the program here<br />
&nbsp;<wbr>LIBS= </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Suffix-rules:&nbsp;<wbr>&nbsp;<wbr>Begin by throwing away all old suffix-<br />
&nbsp;<wbr>#&nbsp;<wbr>rules, and then create new ones for compiling&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>*.f90-files.<br />
&nbsp;<wbr>.SUFFIXES:<br />
&nbsp;<wbr>.SUFFIXES: .f90 .o </p>
<p>&nbsp;<wbr>.f90.o:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$(FC) -c $(FFLAGS) $&lt;</p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Include the dependency-list created by makedepf90 below<br />
&nbsp;<wbr>include .depend </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>target&nbsp;<wbr>&#8216;clean&#8217;&nbsp;<wbr>for deleting object-&nbsp;<wbr>*.mod- and other&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>unwanted files<br />
&nbsp;<wbr>clean:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>rm -f *.o *.mod core</p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Create a dependency list using makedepf90.&nbsp;<wbr>&nbsp;<wbr>All files&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>that needs to be compiled to build the program,&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>i.e all source files except include files, should&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>be given on the command line to makedepf90.&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>#<br />
&nbsp;<wbr>#&nbsp;<wbr>The argument to the&nbsp;<wbr>&#8216;-o&#8217;&nbsp;<wbr>option will be the name of the<br />
&nbsp;<wbr>#&nbsp;<wbr>resulting program when running&nbsp;<wbr>&#8216;make&#8217;, in this case&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>&#8216;foobar&#8217;<br />
&nbsp;<wbr>depend .depend:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>makedepf90 -o foobar *.f90 &gt; .depend</p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211; </p>
<p> (Note that all the indented lines should be indented with tabs, not spaces) </p>
<p> With this makefile, the command <code>make</code> should perform all the commands needed to compile and link the program <i>foobar</i> out of all *.f90 files in the working directory. </p>
<p> The dependency list <i>.depend</i> will be (re)created if <i>.depend</i> doesn&#8217;t exist, or if the command <code>make depend</code> is run. This should be done every time changes has been made to the program that affect the dependencies of the files (e.g if new source files has been added to the project).</p>
<h3>Example With Coco</h3>
<p> If you are using a pre-processor, things might get more complicated. If you are lucky, your compiler supports your pre-processor and runs it on your code automatically, but if it doesn&#8217;t, you have to give the commands to run the pre-processor yourself. Below is an example of an Makefile for <code><a href="/docs/linux/man/1-coco/">coco</a></code>(1)-users. </p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>FC=f90 </p>
<p>&nbsp;<wbr>FFLAGS=-O </p>
<p>&nbsp;<wbr>PREPROCESSOR=coco </p>
<p>&nbsp;<wbr>.SUFFIXES:<br />
&nbsp;<wbr>.SUFFIXES: .f .f90 .o </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Files ending in .f90 are compiled directly &#8230;<br />
&nbsp;<wbr>.f90.o: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$(FC)&nbsp;<wbr>-c&nbsp;<wbr>$(FFLAGS)&nbsp;<wbr>$&lt; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>&#8230; while those ending in .f are preprocessed first.<br />
&nbsp;<wbr>.f.o: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$(PREPROCESSOR)&nbsp;<wbr>$*;&nbsp;<wbr>$(FC)&nbsp;<wbr>-c&nbsp;<wbr>$(FFLAGS)&nbsp;<wbr>$*.f90 </p>
<p>&nbsp;<wbr>include .depend </p>
<p>&nbsp;<wbr>clean:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>rm -f *.o *.mod core</p>
<p>&nbsp;<wbr>depend .depend: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>makedepf90 -coco -o foobar&nbsp;<wbr>*.f90&nbsp;<wbr>*.f&nbsp;<wbr>&gt;&nbsp;<wbr>.depend </p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211; </p>
<p> <code>NOTE:</code> Some implementations of <code><a href="/docs/linux/man/1-make/">make</a></code>(1) will not execute any commands &#8212; not even <code>make depend</code> &#8212; with the Makefiles above unless there exists a file named <i>.depend</i>. To overcome this problem, either run <i>makedepf90</i> manually, or begin by creating an empty <i>.depend</i> file with the command <code>touch .depend</code>. </p>
<h2>DIAGNOSTICS</h2>
<p> Most error and warning messages are self explanatory, but some of them might need some further explanations:</p>
<dl>
<dt><code>WARNING: recursion limit reached in file </code><i>filename</i></p>
<dd> When recursively parsing include files, makedepf90 has reached the recursion limit. Possible reasons are: either you have some <i>really</i> complicated systems of include files, or you have recursive includes (e.g an include file that includes itself). In the latter case; fix it, your Fortran compiler will not like it either. </p>
</dl>
<h2>BUGS AND LIMITATIONS</h2>
<p> Makedepf90&#8217;s support for pre processor conditionals and macro expension (#if:s, #define:s etc) is rather weak, but should work well enough for most cases. </p>
<p> The include file search algorithm is broken. I may fix it some day. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-make/">make</a></code>(1), <code><a href="/docs/linux/man/1-f90/">f90</a></code>(1), <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1), <code><a href="/docs/linux/man/1-fpp/">fpp</a></code>(1), <code><a href="/docs/linux/man/1-f90ppr/">f90ppr</a></code>(1), <code><a href="/docs/linux/man/1-coco/">coco</a></code>(1) </p>
<p> The makedepf90 web site is found at<br />
 <a rel="nofollow" href="http://www.iki.fi/erik.edelmann/makedepf90">http://www.iki.fi/erik.edelmann/makedepf90</a> </p>
<h2>COPYING</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software Foundation. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA </p>
<h2>AUTHOR</h2>
<p> Erik Edelmann &lt;Erik.Edelmann [at] iki.fi&gt; </p>
<h2>Index</h2>
