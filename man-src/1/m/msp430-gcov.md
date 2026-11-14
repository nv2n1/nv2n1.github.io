---
title: "msp430-gcov(1)"
name: "msp430-gcov"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msp430-gcov/"
description: "gcov – coverage testing tool"
---

<h2 class="name">NAME</h2>
<p> gcov &#8211; coverage testing tool </p>
<h2>SYNOPSIS</h2>
<p> gcov [<code>-v</code>|<code>&#8212;version</code>] [<code>-h</code>|<code>&#8212;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-b</code>|<code>&#8212;branch-probabilities</code>]&nbsp;<wbr>[<code>-c</code>|<code>&#8212;branch-counts</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-n</code>|<code>&#8212;no-output</code>]&nbsp;<wbr>[<code>-l</code>|<code>&#8212;long-file-names</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-f</code>|<code>&#8212;function-summaries</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-o</code>|<code>&#8212;object-directory</code>&nbsp;<wbr><i>directory</i>]&nbsp;<wbr><i>sourcefile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gcov</code> is a test coverage program. Use it in concert with <font SIZE="-1">GCC</font> to analyze your programs to help create more efficient, faster running code. You can use <code>gcov</code> as a profiling tool to help discover where your optimization efforts will best affect your code. You can also use <code>gcov</code> along with the other profiling tool, <code>gprof</code>, to assess which parts of your code use the greatest amount of computing time. </p>
<p> Profiling tools help you analyze your code&#8217;s performance. Using a profiler such as <code>gcov</code> or <code>gprof</code>, you can find out some basic performance statistics, such as: </p>
<dl>
<dt>*</p>
<dd> how often each line of code executes </p>
<dt>*</p>
<dd> what lines of code are actually executed </p>
<dt>*</p>
<dd> how much computing time each section of code uses</dl>
<p> Once you know these things about how your code works when compiled, you can look at each module to see which modules should be optimized. <code>gcov</code> helps you determine where to work on optimization. </p>
<p> Software developers also use coverage testing in concert with testsuites, to make sure software is actually good enough for a release. Testsuites can verify that a program works as expected; a coverage program tests to see how much of the program is exercised by the testsuite. Developers can then determine what kinds of test cases need to be added to the testsuites to create both better testing and a better final product. </p>
<p> You should compile your code without optimization if you plan to use <code>gcov</code> because the optimization, by combining some lines of code into one function, may not give you as much information as you need to look for `hot spots&#8217; where the code is using a great deal of computer time. Likewise, because <code>gcov</code> accumulates statistics by line (at the lowest resolution), it works best with a programming style that places only one statement on each line. If you use complicated macros that expand to loops or to other control structures, the statistics are less helpful&#8212;they only report on the line where the macro call appears. If your complex macros behave like functions, you can replace them with inline functions to solve this problem. </p>
<p> <code>gcov</code> creates a logfile called <i>sourcefile.gcov</i> which indicates how many times each line of a source file <i>sourcefile.c</i> has executed. You can use these logfiles along with <code>gprof</code> to aid in fine-tuning the performance of your programs. <code>gprof</code> gives timing information you can use along with the information you get from <code>gcov</code>. </p>
<p> <code>gcov</code> works only on code compiled with <font SIZE="-1">GCC</font>. It is not compatible with any other profiling or test coverage mechanism.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8212;help</code></p>
<dd> Display help about using <code>gcov</code> (on the standard output), and exit without doing any further processing. </p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8212;version</code></p>
<dd> Display the <code>gcov</code> version number (on the standard output), and exit without doing any further processing. </p>
<dt><code>-b</code></p>
<dd>
<dt><code>&#8212;branch-probabilities</code></p>
<dd> Write branch frequencies to the output file, and write branch summary info to the standard output. This option allows you to see how often each branch in your program was taken. </p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8212;branch-counts</code></p>
<dd> Write branch frequencies as the number of branches taken, rather than the percentage of branches taken. </p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8212;no-output</code></p>
<dd> Do not create the <code>gcov</code> output file. </p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8212;long-file-names</code></p>
<dd> Create long file names for included source files. For example, if the header file <i>x.h</i> contains code, and was included in the file <i>a.c</i>, then running <code>gcov</code> on the file <i>a.c</i> will produce an output file called <i>a.c.x.h.gcov</i> instead of <i>x.h.gcov</i>. This can be useful if <i>x.h</i> is included in multiple source files. </p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8212;function-summaries</code></p>
<dd> Output summaries for each function in addition to the file level summary. </p>
<dt><code>-o</code> <i>directory</i></p>
<dd>
<dt><code>&#8212;object-directory</code> <i>directory</i></p>
<dd> The directory where the object files live. Gcov will search for <i>.bb</i>, <i>.bbg</i>, and <i>.da</i> files in this directory.</dl>
<p> When using <code>gcov</code>, you must first compile your program with two special <font SIZE="-1">GCC</font> options: <code>-fprofile-arcs -ftest-coverage</code>. This tells the compiler to generate additional information needed by gcov (basically a flow graph of the program) and also includes additional code in the object files for generating the extra profiling information needed by gcov. These additional files are placed in the directory where the source code is located. </p>
<p> Running the program will cause profile output to be generated. For each source file compiled with <code>-fprofile-arcs</code>, an accompanying <i>.da</i> file will be placed in the source directory. </p>
<p> Running <code>gcov</code> with your program&#8217;s source file names as arguments will now produce a listing of the code along with frequency of execution for each line. For example, if your program is called <i>tmp.c</i>, this is what you see when you use the basic <code>gcov</code> facility: </p>
<pre>
        $ gcc -fprofile-arcs -ftest-coverage tmp.c
        $ a.out
        $ gcov tmp.c
         87.50% of 8 source lines executed in file tmp.c
        Creating tmp.c.gcov.
</pre>
<p> The file <i>tmp.c.gcov</i> contains output from <code>gcov</code>. Here is a sample: </p>
<pre>
                        main()
                        {
                   1      int i, total;
</pre>
<pre>
                   1      total = 0;
</pre>
<pre><code>
11 for (i = 0; i &lt; 10; i++) 10 total += i;
</code></pre>
<p>1 if (total != 45)######printf(&#8220;Failure
&#8221;);<br />
else 1 printf(&#8220;Success
&#8221;);<br />
1<br />
}<br />
 When you use the <code>-b</code> option, your output looks like this: </p>
<pre>
        $ gcov -b tmp.c
         87.50% of 8 source lines executed in file tmp.c
         80.00% of 5 branches executed in file tmp.c
         80.00% of 5 branches taken at least once in file tmp.c
         50.00% of 2 calls executed in file tmp.c
        Creating tmp.c.gcov.
</pre>
<p> Here is a sample of a resulting <i>tmp.c.gcov</i> file: </p>
<pre>
                        main()
                        {
                   1      int i, total;
</pre>
<pre>
                   1      total = 0;
</pre>
<p>11 for (i = 0; i &lt; 10; i++)<br />
    branch 0 taken = 91 %<br />
                     branch 1 taken = 100 %<br />
                                      branch 2 taken = 100 %<br />
                                                       10 total += i;</p>
<p>1 if (total != 45)<br />
    branch 0 taken = 100 %<br />
                     ######printf(&#8220;Failure
&#8221;);<br />
call 0 never executed<br />
    branch 1 never executed else 1 printf(&#8220;Success
&#8221;);<br />
call 0 returns = 100 %<br />
                 1<br />
}<br />
 For each basic block, a line is printed after the last line of the basic block describing the branch or call that ends the basic block. There can be multiple branches and calls listed for a single source line if there are multiple basic blocks that end on that line. In this case, the branches and calls are each given a number. There is no simple way to map these branches and calls back to source constructs. In general, though, the lowest numbered branch or call will correspond to the leftmost construct on the source line. </p>
<p> For a branch, if it was executed at least once, then a percentage indicating the number of times the branch was taken divided by the number of times the branch was executed will be printed. Otherwise, the message &#8220;never executed&#8221; is printed. </p>
<p> For a call, if it was executed at least once, then a percentage indicating the number of times the call returned divided by the number of times the call was executed will be printed. This will usually be 100%, but may be less for functions call <tt>&quot;exit&quot;</tt> or <tt>&quot;longjmp&quot;</tt>, and thus may not return every time they are called. </p>
<p> The execution counts are cumulative. If the example program were executed again without removing the <i>.da</i> file, the count for the number of times each line in the source was executed would be added to the results of the previous <i>run</i>(s). This is potentially useful in several ways. For example, it could be used to accumulate data over a number of program runs as part of a test verification suite, or to provide more accurate long-term information over a large number of program runs. </p>
<p> The data in the <i>.da</i> files is saved immediately before the program exits. For each source file compiled with <code>-fprofile-arcs</code>, the profiling code first attempts to read in an existing <i>.da</i> file; if the file doesn&#8217;t match the executable (differing number of basic block counts) it will ignore the contents of the file. It then adds in the new execution counts and finally writes the data to the file.</p>
<h2>Using <code>gcov</code> with <font SIZE="-1">GCC</font> Optimization</h2>
<p> If you plan to use <code>gcov</code> to help optimize your code, you must first compile your program with two special <font SIZE="-1">GCC</font> options: <code>-fprofile-arcs -ftest-coverage</code>. Aside from that, you can use any other <font SIZE="-1">GCC</font> options; but if you want to prove that every single line in your program was executed, you should not compile with optimization at the same time. On some machines the optimizer can eliminate some simple code lines by combining them with other lines. For example, code like this: </p>
<p>if (a != b)<br />
    c = 1;<br />
else<br />
    c = 0;<br />
 can be compiled into one instruction on some machines. In this case, there is no way for <code>gcov</code> to calculate separate execution counts for each line because there isn&#8217;t separate code for each line. Hence the <code>gcov</code> output looks like this if you compiled the program with optimization: </p>
<pre><code>
100 if (a != b) 100 c = 1;
100 else 100 c = 0;
</code></pre>
<p> The output shows that this block of code, combined by optimization, executed 100 times. In one sense this result is correct, because there was only one instruction representing all four of these lines. However, the output does not indicate how many times the result was 0 and how many times the result was 1.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-gpl/">gpl</a></i>(7), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), <i><a href="/docs/linux/man/7-fsf-funding/">fsf-funding</a></i>(7), <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1) and the Info entry for <i>gcc</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1996, 1997, 1999, 2000, 2001 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; and &#8220;Funding Free Software&#8221;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7) man page. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre>
     A GNU Manual
</pre>
<p> (b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre>
     You have freedom to copy and modify this GNU Manual, like GNU
     software.  Copies published by the Free Software Foundation raise
     funds for GNU development.
</pre>
<h2>Index</h2>
