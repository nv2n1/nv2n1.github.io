---
title: "x86_64-w64-mingw32-gcov(1)"
name: "x86_64-w64-mingw32-gcov"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-w64-mingw32-gcov/"
description: "gcov – coverage testing tool"
---

<h2 class="name">NAME</h2>
<p> gcov &#8211; coverage testing tool </p>
<h2>SYNOPSIS</h2>
<p> gcov [<code>-v</code>|<code>&#8211;version</code>] [<code>-h</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-a</code>|<code>&#8211;all-blocks</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-b</code>|<code>&#8211;branch-probabilities</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-c</code>|<code>&#8211;branch-counts</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-d</code>|<code>&#8211;display-progress</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-f</code>|<code>&#8211;function-summaries</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-i</code>|<code>&#8211;intermediate-format</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-l</code>|<code>&#8211;long-file-names</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-m</code>|<code>&#8211;demangled-names</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-n</code>|<code>&#8211;no-output</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-o</code>|<code>&#8211;object-directory</code>&nbsp;<wbr><i>directory|file</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;preserve-paths</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-r</code>|<code>&#8211;relative-only</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-s</code>|<code>&#8211;source-prefix</code>&nbsp;<wbr><i>directory</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-u</code>|<code>&#8211;unconditional-branches</code>]<br />
&nbsp;<wbr>&nbsp;<wbr><i>files</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gcov</code> is a test coverage program. Use it in concert with <font SIZE="-1">GCC</font> to analyze your programs to help create more efficient, faster running code and to discover untested parts of your program. You can use <code>gcov</code> as a profiling tool to help discover where your optimization efforts will best affect your code. You can also use <code>gcov</code> along with the other profiling tool, <code>gprof</code>, to assess which parts of your code use the greatest amount of computing time. </p>
<p> Profiling tools help you analyze your code&#8217;s performance. Using a profiler such as <code>gcov</code> or <code>gprof</code>, you can find out some basic performance statistics, such as:</p>
<dl>
<dt>&bull;</p>
<dd> how often each line of code executes</p>
<dt>&bull;</p>
<dd> what lines of code are actually executed</p>
<dt>&bull;</p>
<dd> how much computing time each section of code uses</dl>
<p> Once you know these things about how your code works when compiled, you can look at each module to see which modules should be optimized. <code>gcov</code> helps you determine where to work on optimization. </p>
<p> Software developers also use coverage testing in concert with testsuites, to make sure software is actually good enough for a release. Testsuites can verify that a program works as expected; a coverage program tests to see how much of the program is exercised by the testsuite. Developers can then determine what kinds of test cases need to be added to the testsuites to create both better testing and a better final product. </p>
<p> You should compile your code without optimization if you plan to use <code>gcov</code> because the optimization, by combining some lines of code into one function, may not give you as much information as you need to look for `hot spots&#8217; where the code is using a great deal of computer time. Likewise, because <code>gcov</code> accumulates statistics by line (at the lowest resolution), it works best with a programming style that places only one statement on each line. If you use complicated macros that expand to loops or to other control structures, the statistics are less helpful&#8212;they only report on the line where the macro call appears. If your complex macros behave like functions, you can replace them with inline functions to solve this problem. </p>
<p> <code>gcov</code> creates a logfile called <i>sourcefile.gcov</i> which indicates how many times each line of a source file <i>sourcefile.c</i> has executed. You can use these logfiles along with <code>gprof</code> to aid in fine-tuning the performance of your programs. <code>gprof</code> gives timing information you can use along with the information you get from <code>gcov</code>. </p>
<p> <code>gcov</code> works only on code compiled with <font SIZE="-1">GCC. </font> It is not compatible with any other profiling or test coverage mechanism.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Display help about using <code>gcov</code> (on the standard output), and exit without doing any further processing.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the <code>gcov</code> version number (on the standard output), and exit without doing any further processing.</p>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;all-blocks</code></p>
<dd> Write individual execution counts for every basic block. Normally gcov outputs execution counts only for the main blocks of a line. With this option you can determine if blocks within a single line are not being executed.</p>
<dt><code>-b</code></p>
<dd>
<dt><code>&#8211;branch-probabilities</code></p>
<dd> Write branch frequencies to the output file, and write branch summary info to the standard output. This option allows you to see how often each branch in your program was taken. Unconditional branches will not be shown, unless the <code>-u</code> option is given.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;branch-counts</code></p>
<dd> Write branch frequencies as the number of branches taken, rather than the percentage of branches taken.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;no-output</code></p>
<dd> Do not create the <code>gcov</code> output file.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;long-file-names</code></p>
<dd> Create long file names for included source files. For example, if the header file <i>x.h</i> contains code, and was included in the file <i>a.c</i>, then running <code>gcov</code> on the file <i>a.c</i> will produce an output file called <i>a.c##x.h.gcov</i> instead of <i>x.h.gcov</i>. This can be useful if <i>x.h</i> is included in multiple source files and you want to see the individual contributions. If you use the <code>-p</code> option, both the including and included file names will be complete path names.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;preserve-paths</code></p>
<dd> Preserve complete path information in the names of generated <i>.gcov</i> files. Without this option, just the filename component is used. With this option, all directories are used, with <code>/</code> characters translated to <code>#</code> characters, <i>.</i> directory components removed and unremoveable <i>..</i> components renamed to <code>^</code>. This is useful if sourcefiles are in several different directories.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;relative-only</code></p>
<dd> Only output information about source files with a relative pathname (after source prefix elision). Absolute paths are usually system header files and coverage of any inline functions therein is normally uninteresting.</p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;function-summaries</code></p>
<dd> Output summaries for each function in addition to the file level summary.</p>
<dt><code>-o</code> <i>directory|file</i></p>
<dd>
<dt><code>&#8211;object-directory</code> <i>directory</i></p>
<dd>
<dt><code>&#8211;object-file</code> <i>file</i></p>
<dd> Specify either the directory containing the gcov data files, or the object path name. The <i>.gcno</i>, and <i>.gcda</i> data files are searched for using this option. If a directory is specified, the data files are in that directory and named after the input file name, without its extension. If a file is specified here, the data files are named after that file, without its extension.</p>
<dt><code>-s</code> <i>directory</i></p>
<dd>
<dt><code>&#8211;source-prefix</code> <i>directory</i></p>
<dd> A prefix for source file names to remove when generating the output coverage files. This option is useful when building in a separate directory, and the pathname to the source directory is not wanted when determining the output file names. Note that this prefix detection is applied before determining whether the source file is absolute.</p>
<dt><code>-u</code></p>
<dd>
<dt><code>&#8211;unconditional-branches</code></p>
<dd> When branch probabilities are given, include those of unconditional branches. Unconditional branches are normally not interesting.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;display-progress</code></p>
<dd> Display the progress on the standard output.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;intermediate-format</code></p>
<dd> Output gcov file in an easy-to-parse intermediate text format that can be used by <code>lcov</code> or other tools. The output is a single <i>.gcov</i> file per <i>.gcda</i> file. No source code is required. </p>
<p> The format of the intermediate <i>.gcov</i> file is plain text with one entry per line </p>
<pre>
        file:&lt;source_file_name&gt;
        function:&lt;line_number&gt;,&lt;execution_count&gt;,&lt;function_name&gt;
        lcount:&lt;line number&gt;,&lt;execution_count&gt;
        branch:&lt;line_number&gt;,&lt;branch_coverage_type&gt;
        
        Where the &lt;branch_coverage_type&gt; is
           notexec (Branch not executed)
           taken (Branch executed and taken)
           nottaken (Branch executed, but not taken)
        
        There can be multiple &lt;file&gt; entries in an intermediate gcov
        file. All entries following a &lt;file&gt; pertain to that source file
        until the next &lt;file&gt; entry.
</pre>
<p> Here is a sample when <code>-i</code> is used in conjunction with <code>-b</code> option: </p>
<pre>
        file:array.cc
        function:11,1,_Z3sumRKSt6vectorIPiSaIS0_EE
        function:22,1,main
        lcount:11,1
        lcount:12,1
        lcount:14,1
        branch:14,taken
        lcount:26,1
        branch:28,nottaken
</pre>
<dt><code>-m</code></p>
<dd>
<dt><code>&#8211;demangled-names</code></p>
<dd> Display demangled function names in output. The default is to show mangled function names.</dl>
<p> <code>gcov</code> should be run with the current directory the same as that when you invoked the compiler. Otherwise it will not be able to locate the source files. <code>gcov</code> produces files called <i>mangledname.gcov</i> in the current directory. These contain the coverage information of the source file they correspond to. One <i>.gcov</i> file is produced for each source (or header) file containing code, which was compiled to produce the data files. The <i>mangledname</i> part of the output file name is usually simply the source file name, but can be something more complicated if the <code>-l</code> or <code>-p</code> options are given. Refer to those options for details. </p>
<p> If you invoke <code>gcov</code> with multiple input files, the contributions from each input file are summed. Typically you would invoke it with the same list of files as the final link of your executable. </p>
<p> The <i>.gcov</i> files contain the <code>:</code> separated fields along with program source code. The format is </p>
<pre>
        &lt;execution_count&gt;:&lt;line_number&gt;:&lt;source line text&gt;
</pre>
<p> Additional block information may succeed each line, when requested by command line option. The <i>execution_count</i> is <code>&#8211;</code> for lines containing no code. Unexecuted lines are marked <code>#####</code> or <code>====</code>, depending on whether they are reachable by non-exceptional paths or only exceptional paths such as C<font SIZE="-2">++</font> exception handlers, respectively. </p>
<p> Some lines of information at the start have <i>line_number</i> of zero. These preamble lines are of the form </p>
<pre>
        -:0:&lt;tag&gt;:&lt;value&gt;
</pre>
<p> The ordering and number of these preamble lines will be augmented as <code>gcov</code> development progresses &#8212; do not rely on them remaining unchanged. Use <i>tag</i> to locate a particular preamble line. </p>
<p> The additional block information is of the form </p>
<pre>
        &lt;tag&gt; &lt;information&gt;
</pre>
<p> The <i>information</i> is human readable, but designed to be simple enough for machine parsing too. </p>
<p> When printing percentages, 0% and 100% are only printed when the values are <i>exactly</i> 0% and 100% respectively. Other values which would conventionally be rounded to 0% or 100% are instead printed as the nearest non-boundary value. </p>
<p> When using <code>gcov</code>, you must first compile your program with two special <font SIZE="-1">GCC</font> options: <code>-fprofile-arcs -ftest-coverage</code>. This tells the compiler to generate additional information needed by gcov (basically a flow graph of the program) and also includes additional code in the object files for generating the extra profiling information needed by gcov. These additional files are placed in the directory where the object file is located. </p>
<p> Running the program will cause profile output to be generated. For each source file compiled with <code>-fprofile-arcs</code>, an accompanying <i>.gcda</i> file will be placed in the object file directory. </p>
<p> Running <code>gcov</code> with your program&#8217;s source file names as arguments will now produce a listing of the code along with frequency of execution for each line. For example, if your program is called <i>tmp.c</i>, this is what you see when you use the basic <code>gcov</code> facility: </p>
<pre>
        $ gcc -fprofile-arcs -ftest-coverage tmp.c
        $ a.out
        $ gcov tmp.c
        90.00% of 10 source lines executed in file tmp.c
        Creating tmp.c.gcov.
</pre>
<p> The file <i>tmp.c.gcov</i> contains output from <code>gcov</code>. Here is a sample: </p>
<pre><code>
-:0 : Source : tmp.c - : 0 : Graph : tmp.gcno - : 0 : Data : tmp.gcda - : 0 : Runs : 1 - : 0 : Programs : 1 - : 1 : #include&lt;stdio.h&gt; - : 2 : - : 3 : int main(void) 1 : 4:
{
    1 : 5 : int i, total;
    - : 6 : 1 : 7 : total = 0;
    - : 8 : 11 : 9 : for (i = 0; i &lt; 10; i++) 10 : 10 : total += i;
    - : 11 : 1 : 12 : if (total != 45)#### # : 13 : printf("Failure
");
    - : 14 : else 1 : 15 : printf("Success
");
    1 : 16 : return 0;
    - : 17:
}
</code></pre>
<p> When you use the <code>-a</code> option, you will get individual block counts, and the output looks like this: </p>
<p>-:0 : Source : tmp.c &#8211; : 0 : Graph : tmp.gcno &#8211; : 0 : Data : tmp.gcda &#8211; : 0 : Runs : 1 &#8211; : 0 : Programs : 1 &#8211; : 1 : #include&lt;stdio.h&gt; &#8211; : 2 : &#8211; : 3 : int main(void) 1 : 4:<br />
{<br />
    1 : 4 &#8211; block 0 1 : 5 : int i, total;<br />
    &#8211; : 6 : 1 : 7 : total = 0;<br />
    &#8211; : 8 : 11 : 9 : for (i = 0; i &lt; 10; i++) 11 : 9 &#8211; block 0 10 : 10 : total += i;<br />
    10 : 10 &#8211; block 0 &#8211; : 11 : 1 : 12 : if (total != 45) 1 : 12 &#8211; block 0#### # : 13 : printf(&#8220;Failure
&#8221;);<br />
$$$$$:<br />
    13 &#8211; block 0 &#8211; : 14 : else 1 : 15 : printf(&#8220;Success
&#8221;);<br />
    1 : 15 &#8211; block 0 1 : 16 : return 0;<br />
    1 : 16 &#8211; block 0 &#8211; : 17:<br />
}</p>
<p> In this mode, each basic block is only shown on one line &#8212; the last line of the block. A multi-line block will only contribute to the execution count of that last line, and other lines will not be shown to contain code, unless previous blocks end on those lines. The total execution count of a line is shown and subsequent lines show the execution counts for individual blocks that end on that line. After each block, the branch and call counts of the block will be shown, if the <code>-b</code> option is given. </p>
<p> Because of the way <font SIZE="-1">GCC</font> instruments calls, a call count can be shown after a line with no individual blocks. As you can see, line 13 contains a basic block that was not executed. </p>
<p> When you use the <code>-b</code> option, your output looks like this: </p>
<pre>
        $ gcov -b tmp.c
        90.00% of 10 source lines executed in file tmp.c
        80.00% of 5 branches executed in file tmp.c
        80.00% of 5 branches taken at least once in file tmp.c
        50.00% of 2 calls executed in file tmp.c
        Creating tmp.c.gcov.
</pre>
<p> Here is a sample of a resulting <i>tmp.c.gcov</i> file: </p>
<p>-:0 : Source : tmp.c &#8211; : 0 : Graph : tmp.gcno &#8211; : 0 : Data : tmp.gcda &#8211; : 0 : Runs : 1 &#8211; : 0 : Programs : 1 &#8211; : 1 : #include&lt;stdio.h&gt; &#8211; : 2 : &#8211; : 3 : int main(void) function main called 1 returned 1 blocks executed 75 % 1 : 4:<br />
{<br />
    1 : 5 : int i, total;<br />
    &#8211; : 6 : 1 : 7 : total = 0;<br />
    &#8211; : 8 : 11 : 9 : for (i = 0; i &lt; 10; i++)<br />
                         branch 0 taken 91 %<br />
        (fallthrough)<br />
            branch 1 taken 9 %<br />
        10 : 10 : total += i;<br />
    &#8211; : 11 : 1 : 12 : if (total != 45)<br />
                          branch 0 taken 0 %<br />
        (fallthrough)<br />
            branch 1 taken 100 %<br />
        #### # : 13 : printf(&#8220;Failure
&#8221;);<br />
    call 0 never executed &#8211; : 14 : else 1 : 15 : printf(&#8220;Success
&#8221;);<br />
    call 0 called 1 returned 100 %<br />
        1 : 16 : return 0;<br />
    &#8211; : 17:<br />
}</p>
<p> For each function, a line is printed showing how many times the function is called, how many times it returns and what percentage of the function&#8217;s blocks were executed. </p>
<p> For each basic block, a line is printed after the last line of the basic block describing the branch or call that ends the basic block. There can be multiple branches and calls listed for a single source line if there are multiple basic blocks that end on that line. In this case, the branches and calls are each given a number. There is no simple way to map these branches and calls back to source constructs. In general, though, the lowest numbered branch or call will correspond to the leftmost construct on the source line. </p>
<p> For a branch, if it was executed at least once, then a percentage indicating the number of times the branch was taken divided by the number of times the branch was executed will be printed. Otherwise, the message &#8220;never executed&#8221; is printed. </p>
<p> For a call, if it was executed at least once, then a percentage indicating the number of times the call returned divided by the number of times the call was executed will be printed. This will usually be 100%, but may be less for functions that call <tt>&quot;exit&quot;</tt> or <tt>&quot;longjmp&quot;</tt>, and thus may not return every time they are called. </p>
<p> The execution counts are cumulative. If the example program were executed again without removing the <i>.gcda</i> file, the count for the number of times each line in the source was executed would be added to the results of the previous run(s). This is potentially useful in several ways. For example, it could be used to accumulate data over a number of program runs as part of a test verification suite, or to provide more accurate long-term information over a large number of program runs. </p>
<p> The data in the <i>.gcda</i> files is saved immediately before the program exits. For each source file compiled with <code>-fprofile-arcs</code>, the profiling code first attempts to read in an existing <i>.gcda</i> file; if the file doesn&#8217;t match the executable (differing number of basic block counts) it will ignore the contents of the file. It then adds in the new execution counts and finally writes the data to the file.</p>
<h3>Using <code>gcov</code> with <font SIZE="-1">GCC</font> Optimization</h3>
<p> If you plan to use <code>gcov</code> to help optimize your code, you must first compile your program with two special <font SIZE="-1">GCC</font> options: <code>-fprofile-arcs -ftest-coverage</code>. Aside from that, you can use any other <font SIZE="-1">GCC</font> options; but if you want to prove that every single line in your program was executed, you should not compile with optimization at the same time. On some machines the optimizer can eliminate some simple code lines by combining them with other lines. For example, code like this: </p>
<p>if (a != b)<br />
    c = 1;<br />
else<br />
    c = 0;</p>
<p> can be compiled into one instruction on some machines. In this case, there is no way for <code>gcov</code> to calculate separate execution counts for each line because there isn&#8217;t separate code for each line. Hence the <code>gcov</code> output looks like this if you compiled the program with optimization: </p>
<pre><code>
100 : 12 : if (a != b) 100 : 13 : c = 1;
100 : 14 : else 100 : 15 : c = 0;
</code></pre>
<p> The output shows that this block of code, combined by optimization, executed 100 times. In one sense this result is correct, because there was only one instruction representing all four of these lines. However, the output does not indicate how many times the result was 0 and how many times the result was 1. </p>
<p> Inlineable functions can create unexpected line counts. Line counts are shown for the source code of the inlineable function, but what is shown depends on where the function is inlined, or if it is not inlined at all. </p>
<p> If the function is not inlined, the compiler must emit an out of line copy of the function, in any object file that needs it. If <i>fileA.o</i> and <i>fileB.o</i> both contain out of line bodies of a particular inlineable function, they will also both contain coverage counts for that function. When <i>fileA.o</i> and <i>fileB.o</i> are linked together, the linker will, on many systems, select one of those out of line bodies for all calls to that function, and remove or ignore the other. Unfortunately, it will not remove the coverage counters for the unused function body. Hence when instrumented, all but one use of that function will show zero counts. </p>
<p> If the function is inlined in several places, the block structure in each location might not be the same. For instance, a condition might now be calculable at compile time in some instances. Because the coverage of all the uses of the inline function will be shown for the same source lines, the line counts themselves might seem inconsistent. </p>
<p> Long-running applications can use the <tt>&quot;_gcov_reset&quot;</tt> and <tt>&quot;_gcov_dump&quot;</tt> facilities to restrict profile collection to the program region of interest. Calling <tt>&quot;_gcov_reset(void)&quot;</tt> will clear all profile counters to zero, and calling <tt>&quot;_gcov_dump(void)&quot;</tt> will cause the profile information collected at that point to be dumped to <i>.gcda</i> output files.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-gpl/">gpl</a></i>(7), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), <i><a href="/docs/linux/man/7-fsf-funding/">fsf-funding</a></i>(7), <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1) and the Info entry for <i>gcc</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1996-2015 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; and &#8220;Funding Free Software&#8221;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7) man page. </p>
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
<dt><a href="#lbAG">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAH">COPYRIGHT</a></p>
<dd></dl>
