---
title: "x86_64-linux-gnu-gcov-9(1)"
name: "x86_64-linux-gnu-gcov-9"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-linux-gnu-gcov-9/"
description: "gcov – coverage testing tool"
---

<h2 class="name">NAME</h2>
<p> gcov &#8211; coverage testing tool </p>
<h2>SYNOPSIS</h2>
<p> gcov [<code>-v</code>|<code>&#8211;version</code>] [<code>-h</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-a</code>|<code>&#8211;all-blocks</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-b</code>|<code>&#8211;branch-probabilities</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-c</code>|<code>&#8211;branch-counts</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-d</code>|<code>&#8211;display-progress</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-f</code>|<code>&#8211;function-summaries</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-i</code>|<code>&#8211;json-format</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-j</code>|<code>&#8211;human-readable</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-k</code>|<code>&#8211;use-colors</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-l</code>|<code>&#8211;long-file-names</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m</code>|<code>&#8211;demangled-names</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-n</code>|<code>&#8211;no-output</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-o</code>|<code>&#8211;object-directory</code>&nbsp;<i>directory|file</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-p</code>|<code>&#8211;preserve-paths</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-q</code>|<code>&#8211;use-hotness-colors</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-r</code>|<code>&#8211;relative-only</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-s</code>|<code>&#8211;source-prefix</code>&nbsp;<i>directory</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-t</code>|<code>&#8211;stdout</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-u</code>|<code>&#8211;unconditional-branches</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-x</code>|<code>&#8211;hash-filenames</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>files</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gcov</code> is a test coverage program. Use it in concert with <font SIZE="-1">GCC</font> to analyze your programs to help create more efficient, faster running code and to discover untested parts of your program. You can use <code>gcov</code> as a profiling tool to help discover where your optimization efforts will best affect your code. You can also use <code>gcov</code> along with the other profiling tool, <code>gprof</code>, to assess which parts of your code use the greatest amount of computing time. </p>
<p> Profiling tools help you analyze your code&#8217;s performance. Using a profiler such as <code>gcov</code> or <code>gprof</code>, you can find out some basic performance statistics, such as:</p>
<dl>
<dt>*</p>
<dd> how often each line of code executes</p>
<dt>*</p>
<dd> what lines of code are actually executed</p>
<dt>*</p>
<dd> how much computing time each section of code uses</dl>
<p> Once you know these things about how your code works when compiled, you can look at each module to see which modules should be optimized. <code>gcov</code> helps you determine where to work on optimization. </p>
<p> Software developers also use coverage testing in concert with testsuites, to make sure software is actually good enough for a release. Testsuites can verify that a program works as expected; a coverage program tests to see how much of the program is exercised by the testsuite. Developers can then determine what kinds of test cases need to be added to the testsuites to create both better testing and a better final product. </p>
<p> You should compile your code without optimization if you plan to use <code>gcov</code> because the optimization, by combining some lines of code into one function, may not give you as much information as you need to look for `hot spots&#8217; where the code is using a great deal of computer time. Likewise, because <code>gcov</code> accumulates statistics by line (at the lowest resolution), it works best with a programming style that places only one statement on each line. If you use complicated macros that expand to loops or to other control structures, the statistics are less helpful&#8212;they only report on the line where the macro call appears. If your complex macros behave like functions, you can replace them with inline functions to solve this problem. </p>
<p> <code>gcov</code> creates a logfile called <i>sourcefile.gcov</i> which indicates how many times each line of a source file <i>sourcefile.c</i> has executed. You can use these logfiles along with <code>gprof</code> to aid in fine-tuning the performance of your programs. <code>gprof</code> gives timing information you can use along with the information you get from <code>gcov</code>. </p>
<p> <code>gcov</code> works only on code compiled with <font SIZE="-1">GCC.</font> It is not compatible with any other profiling or test coverage mechanism.</p>
<h2>OPTIONS</h2>
<dl>
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
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;display-progress</code></p>
<dd> Display the progress on the standard output.</p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;function-summaries</code></p>
<dd> Output summaries for each function in addition to the file level summary.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Display help about using <code>gcov</code> (on the standard output), and exit without doing any further processing.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;json-format</code></p>
<dd> Output gcov file in an easy-to-parse <font SIZE="-1">JSON</font> intermediate format which does not require source code for generation. The <font SIZE="-1">JSON</font> file is compressed with gzip compression algorithm and the files have <i>.gcov.json.gz</i> extension. </p>
<p> Structure of the <font SIZE="-1">JSON</font> is following: </p>
<pre><code>
{
    "current_working_directory" : &lt;current_working_directory&gt;,
                                  "data_file" : &lt;data_file&gt;,
                                                "format_version" : &lt;format_version&gt;,
                                                                   "gcc_version" : &lt;gcc_version&gt; "files" : [&lt;file&gt;]
}
</code></pre>
<p> Fields of the root element have following semantics:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <i>current_working_directory</i>: working directory where a compilation unit was compiled</p>
<dt>*</p>
<dd> <i>data_file</i>: name of the data file (<font SIZE="-1">GCDA</font>)</p>
<dt>*</p>
<dd> <i>format_version</i>: semantic version of the format</p>
<dt>*</p>
<dd> <i>gcc_version</i>: version of the <font SIZE="-1">GCC</font> compiler</dl>
</dl>
<dl>
<dt>
<dd>
<p> Each <i>file</i> has the following form: </p>
<p>{<br />
    &#8220;file&#8221; : &lt;file_name&gt;,<br />
             &#8220;functions&#8221; : [&lt;function&gt;],<br />
                           &#8220;lines&#8221; : [&lt;line&gt;]<br />
}</p>
<p> Fields of the <i>file</i> element have following semantics:</p>
<dl>
<dt>*</p>
<dd> <i>file_name</i>: name of the source file</dl>
</dl>
<dl>
<dt>
<dd>
<p> Each <i>function</i> has the following form: </p>
<pre>
        {
          &quot;blocks&quot;: &lt;blocks&gt;,
          &quot;blocks_executed&quot;: &lt;blocks_executed&gt;,
          &quot;demangled_name&quot;: &quot;&lt;demangled_name&gt;,
          &quot;end_column&quot;: &lt;end_column&gt;,
          &quot;end_line&quot;: &lt;end_line&gt;,
          &quot;execution_count&quot;: &lt;execution_count&gt;,
          &quot;name&quot;: &lt;name&gt;,
          &quot;start_column&quot;: &lt;start_column&gt;
          &quot;start_line&quot;: &lt;start_line&gt;
        }
</pre>
<p> Fields of the <i>function</i> element have following semantics:</p>
<dl>
<dt>*</p>
<dd> <i>blocks</i>: number of blocks that are in the function</p>
<dt>*</p>
<dd> <i>blocks_executed</i>: number of executed blocks of the function</p>
<dt>*</p>
<dd> <i>demangled_name</i>: demangled name of the function</p>
<dt>*</p>
<dd> <i>end_column</i>: column in the source file where the function ends</p>
<dt>*</p>
<dd> <i>end_line</i>: line in the source file where the function ends</p>
<dt>*</p>
<dd> <i>execution_count</i>: number of executions of the function</p>
<dt>*</p>
<dd> <i>name</i>: name of the function</p>
<dt>*</p>
<dd> <i>start_column</i>: column in the source file where the function begins</p>
<dt>*</p>
<dd> <i>start_line</i>: line in the source file where the function begins</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note that line numbers and column numbers number from 1. In the current implementation, <i>start_line</i> and <i>start_column</i> do not include any template parameters and the leading return type but that this is likely to be fixed in the future. </p>
<p> Each <i>line</i> has the following form: </p>
<p>{<br />
    &#8220;branches&#8221; : [&lt;branch&gt;],<br />
                 &#8220;count&#8221; : &lt;count&gt;,<br />
                           &#8220;line_number&#8221; : &lt;line_number&gt;,<br />
                                           &#8220;unexecuted_block&#8221; : &lt;unexecuted_block&gt; &#8220;function_name&#8221; : &lt;function_name&gt;,<br />
}</p>
<p> Branches are present only with <i>-b</i> option. Fields of the <i>line</i> element have following semantics:</p>
<dl>
<dt>*</p>
<dd> <i>count</i>: number of executions of the line</p>
<dt>*</p>
<dd> <i>line_number</i>: line number</p>
<dt>*</p>
<dd> <i>unexecuted_block</i>: flag whether the line contains an unexecuted block (not all statements on the line are executed)</p>
<dt>*</p>
<dd> <i>function_name</i>: a name of a function this <i>line</i> belongs to (for a line with an inlined statements can be not set)</dl>
</dl>
<dl>
<dt>
<dd>
<p> Each <i>branch</i> has the following form: </p>
<pre>
        {
          &quot;count&quot;: &lt;count&gt;,
          &quot;fallthrough&quot;: &lt;fallthrough&gt;,
          &quot;throw&quot;: &lt;throw&gt;
        }
</pre>
<p> Fields of the <i>branch</i> element have following semantics:</p>
<dl>
<dt>*</p>
<dd> <i>count</i>: number of executions of the branch</p>
<dt>*</p>
<dd> <i>fallthrough</i>: true when the branch is a fall through branch</p>
<dt>*</p>
<dd> <i>throw</i>: true when the branch is an exceptional branch</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-j</code></p>
<dd>
<dt><code>&#8211;human-readable</code></p>
<dd> Write counts in human readable format (like 24.6k).</p>
<dt><code>-k</code></p>
<dd>
<dt><code>&#8211;use-colors</code></p>
<dd> Use colors for lines of code that have zero coverage. We use red color for non-exceptional lines and cyan for exceptional. Same colors are used for basic blocks with <code>-a</code> option.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;long-file-names</code></p>
<dd> Create long file names for included source files. For example, if the header file <i>x.h</i> contains code, and was included in the file <i>a.c</i>, then running <code>gcov</code> on the file <i>a.c</i> will produce an output file called <i>a.c##x.h.gcov</i> instead of <i>x.h.gcov</i>. This can be useful if <i>x.h</i> is included in multiple source files and you want to see the individual contributions. If you use the <code>-p</code> option, both the including and included file names will be complete path names.</p>
<dt><code>-m</code></p>
<dd>
<dt><code>&#8211;demangled-names</code></p>
<dd> Display demangled function names in output. The default is to show mangled function names.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;no-output</code></p>
<dd> Do not create the <code>gcov</code> output file.</p>
<dt><code>-o</code> <i>directory|file</i></p>
<dd>
<dt><code>&#8211;object-directory</code> <i>directory</i></p>
<dd>
<dt><code>&#8211;object-file</code> <i>file</i></p>
<dd> Specify either the directory containing the gcov data files, or the object path name. The <i>.gcno</i>, and <i>.gcda</i> data files are searched for using this option. If a directory is specified, the data files are in that directory and named after the input file name, without its extension. If a file is specified here, the data files are named after that file, without its extension.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;preserve-paths</code></p>
<dd> Preserve complete path information in the names of generated <i>.gcov</i> files. Without this option, just the filename component is used. With this option, all directories are used, with <code>/</code> characters translated to <code>#</code> characters, <i>.</i> directory components removed and unremoveable <i>..</i> components renamed to <code>^</code>. This is useful if sourcefiles are in several different directories.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;use-hotness-colors</code></p>
<dd> Emit perf-like colored output for hot lines. Legend of the color scale is printed at the very beginning of the output file.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;relative-only</code></p>
<dd> Only output information about source files with a relative pathname (after source prefix elision). Absolute paths are usually system header files and coverage of any inline functions therein is normally uninteresting.</p>
<dt><code>-s</code> <i>directory</i></p>
<dd>
<dt><code>&#8211;source-prefix</code> <i>directory</i></p>
<dd> A prefix for source file names to remove when generating the output coverage files. This option is useful when building in a separate directory, and the pathname to the source directory is not wanted when determining the output file names. Note that this prefix detection is applied before determining whether the source file is absolute.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;stdout</code></p>
<dd> Output to standard output instead of output files.</p>
<dt><code>-u</code></p>
<dd>
<dt><code>&#8211;unconditional-branches</code></p>
<dd> When branch probabilities are given, include those of unconditional branches. Unconditional branches are normally not interesting.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the <code>gcov</code> version number (on the standard output), and exit without doing any further processing.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Print verbose informations related to basic blocks and arcs.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;hash-filenames</code></p>
<dd> When using <i>&#8211;preserve-paths</i>, gcov uses the full pathname of the source files to create an output filename. This can lead to long filenames that can overflow filesystem limits. This option creates names of the form <i>source-file##md5.gcov</i>, where the <i>source-file</i> component is the final filename part and the <i>md5</i> component is calculated from the full mangled name that would have been used otherwise. The option is an alternative to the <i>&#8211;preserve-paths</i> on systems which have a filesystem limit.</dl>
<p> <code>gcov</code> should be run with the current directory the same as that when you invoked the compiler. Otherwise it will not be able to locate the source files. <code>gcov</code> produces files called <i>mangledname.gcov</i> in the current directory. These contain the coverage information of the source file they correspond to. One <i>.gcov</i> file is produced for each source (or header) file containing code, which was compiled to produce the data files. The <i>mangledname</i> part of the output file name is usually simply the source file name, but can be something more complicated if the <code>-l</code> or <code>-p</code> options are given. Refer to those options for details. </p>
<p> If you invoke <code>gcov</code> with multiple input files, the contributions from each input file are summed. Typically you would invoke it with the same list of files as the final link of your executable. </p>
<p> The <i>.gcov</i> files contain the <code>:</code> separated fields along with program source code. The format is </p>
<pre>
        &lt;execution_count&gt;:&lt;line_number&gt;:&lt;source line text&gt;
</pre>
<p> Additional block information may succeed each line, when requested by command line option. The <i>execution_count</i> is <code>&#8211;</code> for lines containing no code. Unexecuted lines are marked <code>#####</code> or <code>=====</code>, depending on whether they are reachable by non-exceptional paths or only exceptional paths such as C<font SIZE="-2">++</font> exception handlers, respectively. Given the <code>-a</code> option, unexecuted blocks are marked <code>$$$$$</code> or <code>%%%%%</code>, depending on whether a basic block is reachable via non-exceptional or exceptional paths. Executed basic blocks having a statement with zero <i>execution_count</i> end with <code>*</code> character and are colored with magenta color with the <code>-k</code> option. This functionality is not supported in Ada. </p>
<p> Note that <font SIZE="-1">GCC</font> can completely remove the bodies of functions that are not needed &#8212; for instance if they are inlined everywhere. Such functions are marked with <code>&#8211;</code>, which can be confusing. Use the <code>-fkeep-inline-functions</code> and <code>-fkeep-static-functions</code> options to retain these functions and allow gcov to properly show their <i>execution_count</i>. </p>
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
<p> When using <code>gcov</code>, you must first compile your program with a special <font SIZE="-1">GCC</font> option <code>&#8211;coverage</code>. This tells the compiler to generate additional information needed by gcov (basically a flow graph of the program) and also includes additional code in the object files for generating the extra profiling information needed by gcov. These additional files are placed in the directory where the object file is located. </p>
<p> Running the program will cause profile output to be generated. For each source file compiled with <code>-fprofile-arcs</code>, an accompanying <i>.gcda</i> file will be placed in the object file directory. </p>
<p> Running <code>gcov</code> with your program&#8217;s source file names as arguments will now produce a listing of the code along with frequency of execution for each line. For example, if your program is called <i>tmp.cpp</i>, this is what you see when you use the basic <code>gcov</code> facility: </p>
<pre>
        $ g++ --coverage tmp.cpp
        $ a.out
        $ gcov tmp.cpp -m
        File 'tmp.cpp'
        Lines executed:92.86% of 14
        Creating 'tmp.cpp.gcov'
</pre>
<p> The file <i>tmp.cpp.gcov</i> contains output from <code>gcov</code>. Here is a sample: </p>
<p>-:0 : Source : tmp.cpp &#8211; : 0 : Working directory : / home / gcc / testcase &#8211; : 0 : Graph : tmp.gcno &#8211; : 0 : Data : tmp.gcda &#8211; : 0 : Runs : 1 &#8211; : 0 : Programs : 1 &#8211; : 1 : #include&lt;stdio.h&gt; &#8211; : 2 : &#8211; : 3 : template &lt;class T&gt;<br />
                                                                                                                                                                                                            &#8211; : 4 : class Foo &#8211; : 5:<br />
{<br />
    &#8211; : 6 : public : 1 * : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;char&gt;::Foo()<br />
        :#### # : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;int&gt;::Foo() : 1 : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;2 * : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;char&gt;::inc()<br />
        :#### # : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;int&gt;::inc() : 2 : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; : 9 : &#8211; : 10 : private : &#8211; : 11 : int b;<br />
    &#8211; : 12:<br />
};<br />
-:13 : &#8211; : 14 : template class Foo&lt;int&gt;;<br />
-:15 : template class Foo&lt;char&gt;;<br />
-:16 : &#8211; : 17 : int 1 : 18 : main(void) &#8211; : 19:<br />
{<br />
    &#8211; : 20 : int i, total;<br />
    1 : 21 : Foo&lt;int&gt; counter;<br />
    &#8211; : 22 : 1 : 23 : counter.inc();<br />
    1 : 24 : counter.inc();<br />
    1 : 25 : total = 0;<br />
    &#8211; : 26 : 11 : 27 : for (i = 0; i &lt; 10; i++) 10 : 28 : total += i;<br />
    &#8211; : 29 : 1 * : 30 : int v = total &gt; 100 ? 1 : 2;<br />
    &#8211; : 31 : 1 : 32 : if (total != 45)#### # : 33 : printf(&#8220;Failure
&#8221;);<br />
    &#8211; : 34 : else 1 : 35 : printf(&#8220;Success
&#8221;);<br />
    1 : 36 : return 0;<br />
    &#8211; : 37:<br />
}</p>
<p> Note that line 7 is shown in the report multiple times. First occurrence presents total number of execution of the line and the next two belong to instances of class Foo constructors. As you can also see, line 30 contains some unexecuted basic blocks and thus execution count has asterisk symbol. </p>
<p> When you use the <code>-a</code> option, you will get individual block counts, and the output looks like this: </p>
<p>-:0 : Source : tmp.cpp &#8211; : 0 : Working directory : / home / gcc / testcase &#8211; : 0 : Graph : tmp.gcno &#8211; : 0 : Data : tmp.gcda &#8211; : 0 : Runs : 1 &#8211; : 0 : Programs : 1 &#8211; : 1 : #include&lt;stdio.h&gt; &#8211; : 2 : &#8211; : 3 : template &lt;class T&gt;<br />
                                                                                                                                                                                                            &#8211; : 4 : class Foo &#8211; : 5:<br />
{<br />
    &#8211; : 6 : public : 1 * : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;char&gt;::Foo()<br />
        :#### # : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;int&gt;::Foo() : 1 : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;2 * : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;char&gt;::inc()<br />
        :#### # : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;int&gt;::inc() : 2 : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; : 9 : &#8211; : 10 : private : &#8211; : 11 : int b;<br />
    &#8211; : 12:<br />
};<br />
-:13 : &#8211; : 14 : template class Foo&lt;int&gt;;<br />
-:15 : template class Foo&lt;char&gt;;<br />
-:16 : &#8211; : 17 : int 1 : 18 : main(void) &#8211; : 19:<br />
{<br />
    &#8211; : 20 : int i, total;<br />
    1 : 21 : Foo&lt;int&gt; counter;<br />
    1 : 21 &#8211; block 0 &#8211; : 22 : 1 : 23 : counter.inc();<br />
    1 : 23 &#8211; block 0 1 : 24 : counter.inc();<br />
    1 : 24 &#8211; block 0 1 : 25 : total = 0;<br />
    &#8211; : 26 : 11 : 27 : for (i = 0; i &lt; 10; i++) 1 : 27 &#8211; block 0 11 : 27 &#8211; block 1 10 : 28 : total += i;<br />
    10 : 28 &#8211; block 0 &#8211; : 29 : 1 * : 30 : int v = total &gt; 100 ? 1 : 2;<br />
    1 : 30 &#8211; block 0 % % % % % : 30 &#8211; block 1 1 : 30 &#8211; block 2 &#8211; : 31 : 1 : 32 : if (total != 45) 1 : 32 &#8211; block 0#### # : 33 : printf(&#8220;Failure
&#8221;);<br />
    % % % % % : 33 &#8211; block 0 &#8211; : 34 : else 1 : 35 : printf(&#8220;Success
&#8221;);<br />
    1 : 35 &#8211; block 0 1 : 36 : return 0;<br />
    1 : 36 &#8211; block 0 &#8211; : 37:<br />
}</p>
<p> In this mode, each basic block is only shown on one line &#8212; the last line of the block. A multi-line block will only contribute to the execution count of that last line, and other lines will not be shown to contain code, unless previous blocks end on those lines. The total execution count of a line is shown and subsequent lines show the execution counts for individual blocks that end on that line. After each block, the branch and call counts of the block will be shown, if the <code>-b</code> option is given. </p>
<p> Because of the way <font SIZE="-1">GCC</font> instruments calls, a call count can be shown after a line with no individual blocks. As you can see, line 33 contains a basic block that was not executed. </p>
<p> When you use the <code>-b</code> option, your output looks like this: </p>
<p>-:0 : Source : tmp.cpp &#8211; : 0 : Working directory : / home / gcc / testcase &#8211; : 0 : Graph : tmp.gcno &#8211; : 0 : Data : tmp.gcda &#8211; : 0 : Runs : 1 &#8211; : 0 : Programs : 1 &#8211; : 1 : #include&lt;stdio.h&gt; &#8211; : 2 : &#8211; : 3 : template &lt;class T&gt;<br />
                                                                                                                                                                                                            &#8211; : 4 : class Foo &#8211; : 5:<br />
{<br />
    &#8211; : 6 : public : 1 * : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;char&gt;::Foo()<br />
        : function Foo&lt;char&gt;::Foo() called 0 returned 0 %<br />
        blocks executed 0 %<br />
        #### # : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;int&gt;::Foo()<br />
        : function Foo&lt;int&gt;::Foo() called 1 returned 100 %<br />
        blocks executed 100 %<br />
        1 : 7 : Foo()<br />
        : b(1000)<br />
    {<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;2 * : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;char&gt;::inc()<br />
        : function Foo&lt;char&gt;::inc() called 0 returned 0 %<br />
        blocks executed 0 %<br />
        #### # : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Foo&lt;int&gt;::inc()<br />
        : function Foo&lt;int&gt;::inc() called 2 returned 100 %<br />
        blocks executed 100 %<br />
        2 : 8 : void inc()<br />
    {<br />
        b++;<br />
    }<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; : 9 : &#8211; : 10 : private : &#8211; : 11 : int b;<br />
    &#8211; : 12:<br />
};<br />
-:13 : &#8211; : 14 : template class Foo&lt;int&gt;;<br />
-:15 : template class Foo&lt;char&gt;;<br />
-:16 : &#8211; : 17 : int<br />
                    function main called 1 returned 100 %<br />
                blocks executed 81 %<br />
                1 : 18 : main(void) &#8211; : 19:<br />
{<br />
    &#8211; : 20 : int i, total;<br />
    1 : 21 : Foo&lt;int&gt; counter;<br />
    call 0 returned 100 %<br />
            branch 1 taken 100 % (fallthrough)branch 2 taken 0 % (throw) &#8211; : 22 : 1 : 23 : counter.inc();<br />
    call 0 returned 100 %<br />
        branch 1 taken 100 % (fallthrough)branch 2 taken 0 % (throw)1 : 24 : counter.inc();<br />
    call 0 returned 100 %<br />
        branch 1 taken 100 % (fallthrough)branch 2 taken 0 % (throw)1 : 25 : total = 0;<br />
    &#8211; : 26 : 11 : 27 : for (i = 0; i &lt; 10; i++)<br />
                           branch 0 taken 91 %<br />
        (fallthrough)<br />
            branch 1 taken 9 %<br />
        10 : 28 : total += i;<br />
    &#8211; : 29 : 1 * : 30 : int v = total &gt; 100 ? 1 : 2;<br />
    branch 0 taken 0 % (fallthrough)branch 1 taken 100 %<br />
        &#8211; : 31 : 1 : 32 : if (total != 45)<br />
                              branch 0 taken 0 %<br />
        (fallthrough)<br />
            branch 1 taken 100 %<br />
        #### # : 33 : printf(&#8220;Failure
&#8221;);<br />
    call 0 never executed<br />
            branch 1 never executed<br />
                branch 2 never executed &#8211; : 34 : else 1 : 35 : printf(&#8220;Success
&#8221;);<br />
    call 0 returned 100 %<br />
        branch 1 taken 100 % (fallthrough)branch 2 taken 0 % (throw)1 : 36 : return 0;<br />
    &#8211; : 37:<br />
}</p>
<p> For each function, a line is printed showing how many times the function is called, how many times it returns and what percentage of the function&#8217;s blocks were executed. </p>
<p> For each basic block, a line is printed after the last line of the basic block describing the branch or call that ends the basic block. There can be multiple branches and calls listed for a single source line if there are multiple basic blocks that end on that line. In this case, the branches and calls are each given a number. There is no simple way to map these branches and calls back to source constructs. In general, though, the lowest numbered branch or call will correspond to the leftmost construct on the source line. </p>
<p> For a branch, if it was executed at least once, then a percentage indicating the number of times the branch was taken divided by the number of times the branch was executed will be printed. Otherwise, the message &#8220;never executed&#8221; is printed. </p>
<p> For a call, if it was executed at least once, then a percentage indicating the number of times the call returned divided by the number of times the call was executed will be printed. This will usually be 100%, but may be less for functions that call <tt>&quot;exit&quot;</tt> or <tt>&quot;longjmp&quot;</tt>, and thus may not return every time they are called. </p>
<p> The execution counts are cumulative. If the example program were executed again without removing the <i>.gcda</i> file, the count for the number of times each line in the source was executed would be added to the results of the previous run(s). This is potentially useful in several ways. For example, it could be used to accumulate data over a number of program runs as part of a test verification suite, or to provide more accurate long-term information over a large number of program runs. </p>
<p> The data in the <i>.gcda</i> files is saved immediately before the program exits. For each source file compiled with <code>-fprofile-arcs</code>, the profiling code first attempts to read in an existing <i>.gcda</i> file; if the file doesn&#8217;t match the executable (differing number of basic block counts) it will ignore the contents of the file. It then adds in the new execution counts and finally writes the data to the file.</p>
<h3>Using <code>gcov</code> with <font SIZE="-1">GCC</font> Optimization</h3>
<p> If you plan to use <code>gcov</code> to help optimize your code, you must first compile your program with a special <font SIZE="-1">GCC</font> option <code>&#8211;coverage</code>. Aside from that, you can use any other <font SIZE="-1">GCC</font> options; but if you want to prove that every single line in your program was executed, you should not compile with optimization at the same time. On some machines the optimizer can eliminate some simple code lines by combining them with other lines. For example, code like this: </p>
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
<p> Long-running applications can use the <tt>&quot;__gcov_reset&quot;</tt> and <tt>&quot;__gcov_dump&quot;</tt> facilities to restrict profile collection to the program region of interest. Calling <tt>&quot;__gcov_reset(void)&quot;</tt> will clear all profile counters to zero, and calling <tt>&quot;__gcov_dump(void)&quot;</tt> will cause the profile information collected at that point to be dumped to <i>.gcda</i> output files. Instrumented applications use a static destructor with priority 99 to invoke the <tt>&quot;__gcov_dump&quot;</tt> function. Thus <tt>&quot;__gcov_dump&quot;</tt> is executed after all user defined static destructors, as well as handlers registered with <tt>&quot;atexit&quot;</tt>. If an executable loads a dynamic shared object via dlopen functionality, <code>-Wl,&#8211;dynamic-list-data</code> is needed to dump all profile data. </p>
<p> Profiling run-time library reports various errors related to profile manipulation and profile saving. Errors are printed into standard error output or <font SIZE="-1"><code>GCOV_ERROR_FILE</code></font> file, if environment variable is used. In order to terminate immediately after an errors occurs set <font SIZE="-1"><code>GCOV_EXIT_AT_ERROR</code></font> environment variable. That can help users to find profile clashing which leads to a misleading profile.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-gpl/">gpl</a></i>(7), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), <i><a href="/docs/linux/man/7-fsf-funding/">fsf-funding</a></i>(7), <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1) and the Info entry for <i>gcc</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1996-2019 Free Software Foundation, Inc. </p>
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
