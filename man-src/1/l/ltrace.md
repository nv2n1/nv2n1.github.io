---
title: "ltrace(1)"
name: "ltrace"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ltrace/"
description: "ltrace – A library call tracer"
---

<h2 class="name">NAME</h2>
<p> ltrace &#8211; A library call tracer</p>
<h2>SYNOPSIS</h2>
<p> <code>ltrace</code> [-e <i>filter</i>|-L] [-l|&#8211;library=<i>library_pattern</i>] [-x <i>filter</i>] [-S] [-b|&#8211;no-signals] [-i] [-w|&#8211;where=<i>nr</i>] [-r|-t|-tt|-ttt] [-T] [-F <i>filename</i>] [-A <i>maxelts</i>] [-s <i>strsize</i>] [-C|&#8211;demangle] [-a|&#8211;align <i>column</i>] [-n|&#8211;indent <i>nr</i>] [-o|&#8211;output <i>filename</i>] [-D|&#8211;debug <i>mask</i>] [-u <i>username</i>] [-f] [-p <i>pid</i>] [[&#8211;] <i>command [arg &#8230;]</i>] </p>
<p> <code>ltrace</code> -c [-e <i>filter</i>|-L] [-l|&#8211;library=<i>library_pattern</i>] [-x <i>filter</i>] [-S] [-o|&#8211;output <i>filename</i>] [-f] [-p <i>pid</i>] [[&#8211;] <i>command [arg &#8230;]</i>] </p>
<p> <code>ltrace</code> -V|&#8211;version </p>
<p> <code>ltrace</code> -h|&#8211;help </p>
<h2>DESCRIPTION</h2>
<p> <code>ltrace</code> is a program that simply runs the specified <i>command</i> until it exits. It intercepts and records the dynamic library calls which are called by the executed process and the signals which are received by that process. It can also intercept and print the system calls executed by the program. </p>
<p> Its use is very similar to <code><a href="/docs/linux/man/1-strace/">strace</a>(1)</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-a, &#8211;align <i>column</p>
<dd> Align return values in a specific column</i> (default column is 5/8 of screen width).</p>
<dt>-A <i>maxelts</p>
<dd> Maximum number of array elements to print before suppressing the rest with an ellipsis (&quot;&#8230;&quot;). This also limits number of recursive structure expansions.</p>
<dt>-b, &#8211;no-signals</p>
<dd> Disable printing of signals recieved by the traced process.</p>
<dt>-c</p>
<dd> Count time and calls for each library call and report a summary on program exit.</p>
<dt>-C, &#8211;demangle</p>
<dd> Decode (demangle) low-level symbol names into user-level names. Besides removing any initial underscore prefix used by the system, this makes C++ function names readable.</p>
<dt>-D, &#8211;debug </i>mask<i></p>
<dd> Show debugging output of </i><code>ltrace</code> itself. <i>mask</i> is a number with internal meaning that&#8217;s not really well defined at all. <i>mask</i> of 77 shows all debug messages, which is what you usually need.</p>
<dt>-e <i>filter</p>
<dd> A qualifying expression which modifies which library calls to trace. The format of the filter expression is described in the section </i><code>FILTER EXPRESSIONS</code>. If more than one -e option appears on the command line, the library calls that match any of them are traced. If no -e is given, <code>@MAIN</code> is assumed as a default.</p>
<dt>-f</p>
<dd> Trace child processes as they are created by currently traced processes as a result of the <a href="/docs/linux/man/2-fork/">fork</a>(2) or <a href="/docs/linux/man/2-clone/">clone</a>(2) system calls. The new process is attached immediately.</p>
<dt>-F <i>filename</p>
<dd> Load an alternate config file. Normally, /etc/ltrace.conf and ~/.ltrace.conf will be read (the latter only if it exists). Use this option to load the given file or files instead of those two default files. See <a href="/docs/linux/man/5-ltrace-conf/">ltrace.conf</a>(5) for details on the syntax of ltrace configuration files.</p>
<dt>-h, &#8211;help</p>
<dd> Show a summary of the options to ltrace and exit.</p>
<dt>-i</p>
<dd> Print the instruction pointer at the time of the library call.</p>
<dt>-l, &#8211;library library_pattern</p>
<dd> Display only calls to functions implemented by libraries that match library_pattern.</i> Multiple library patters can be specified with several instances of this option. Syntax of library_pattern is described in section <code>FILTER EXPRESSIONS</code>. </p>
<p> Note that while this option selects calls that might be directed to the selected libraries, there&#8217;s no actual guarantee that the call won&#8217;t be directed elsewhere due to e.g. LD_PRELOAD or simply dependency ordering. If you want to make sure that symbols in given library are actually called, use <code>-x @</code><i>library_pattern</i> instead.</p>
<dt>-L</p>
<dd> When no -e option is given, don&#8217;t assume the default action of <code>@MAIN</code>.</p>
<dt>-n, &#8211;indent <i>nr</p>
<dd> Indent trace output by nr</i> spaces for each level of call nesting. Using this option makes the program flow visualization easy to follow. This indents uselessly also functions that never return, such as service functions for throwing exceptions in the C++ runtime.</p>
<dt>-o, &#8211;output <i>filename</p>
<dd> Write the trace output to the file filename</i> rather than to stderr.</p>
<dt>-p <i>pid</p>
<dd> Attach to the process with the process ID pid</i> and begin tracing. This option can be used together with passing a command to execute. It is possible to attach to several processes by passing more than one option -p.</p>
<dt>-r</p>
<dd> Print a relative timestamp with each line of the trace. This records the time difference between the beginning of successive lines.</p>
<dt>-s <i>strsize</p>
<dd> Specify the maximum string size to print (the default is 32).</p>
<dt>-S</p>
<dd> Display system calls as well as library calls</p>
<dt>-t</p>
<dd> Prefix each line of the trace with the time of day.</p>
<dt>-tt</p>
<dd> If given twice, the time printed will include the microseconds.</p>
<dt>-ttt</p>
<dd> If given thrice, the time printed will include the microseconds and the leading portion will be printed as the number of seconds since the epoch.</p>
<dt>-T</p>
<dd> Show the time spent inside each call. This records the time difference between the beginning and the end of each call.</p>
<dt>-u username</p>
<dd> Run command with the userid, groupid and supplementary groups of username</i>. This option is only useful when running as root and enables the correct execution of setuid and/or setgid binaries.</p>
<dt>-w, &#8211;where <i>nr</p>
<dd> Show backtrace of nr</i> stack frames for each traced function. This option enabled only if libunwind support was enabled at compile time.</p>
<dt>-x <i>filter</p>
<dd> A qualifying expression which modifies which symbol table entry points to trace. The format of the filter expression is described in the section </i><code>FILTER EXPRESSIONS</code>. If more than one -x option appears on the command line, the symbols that match any of them are traced. No entry points are traced if no -x is given.</p>
<dt>-V, &#8211;version</p>
<dd> Show the version number of ltrace and exit. </p>
</dl>
<h2>FILTER EXPRESSIONS</h2>
<p> Filter expression is a chain of glob- or regexp-based rules that are used to pick symbols for tracing from libraries that the process uses. Most of it is intuitive, so as an example, the following would trace calls to malloc and free, except those done by libc: </p>
<p> -e malloc+free- [at] libc.so* </p>
<p> This reads: trace malloc and free, but don&#8217;t trace anything that comes from libc. Semi-formally, the syntax of the above example looks approximately like this: </p>
<p> {[+-][<i>symbol_pattern</i>][@<i>library_pattern</i>]} </p>
<p> <i>Symbol_pattern</i> is used to match symbol names, <i>library_pattern</i> to match library SONAMEs. Both are implicitly globs, but can be regular expressions as well (see below). The glob syntax supports meta-characters <code>*</code> and <code>?</code> and character classes, similarly to what basic bash globs support. <code>^</code> and <code>$</code> are recognized to mean, respectively, start and end of given name. </p>
<p> Both <i>symbol_pattern</i> and <i>library_pattern</i> have to match the whole name. If you want to match only part of the name, surround it with one or two *&#8217;s as appropriate. The exception is if the pattern is not mentioned at all, in which case it&#8217;s as if the corresponding pattern were <code>*</code>. (So <code>malloc</code> is really <code>malloc@*</code> and <code>@libc.*</code> is really <code>*@libc.*</code>.) </p>
<p> In libraries that don&#8217;t have an explicit SONAME, basename is taken for SONAME. That holds for main binary as well: <code>/bin/echo</code> has an implicit SONAME of <code>echo</code>. In addition to that, special library pattern <code>MAIN</code> always matches symbols in the main binary and never a library with actual SONAME <code>MAIN</code> (use e.g. <code>^MAIN</code> or <code>[M]AIN</code> for that). </p>
<p> If the symbol or library pattern is surrounded in slashes (/like this/), then it is considered a regular expression instead. As a shorthand, instead of writing <code>/x/@/y/</code>, you can write <code>/x@y/</code>. </p>
<p> If the library pattern starts with a slash, it is not a SONAME expression, but a path expression, and is matched against the library path name. </p>
<p> The first rule may lack a sign, in which case <code>+</code> is assumed. If, on the other hand, the first rule has a <code>&#8211;</code> sign, it is as if there was another rule <code>@</code> in front of it, which has the effect of tracing complement of given rule. </p>
<p> The above rules are used to construct the set of traced symbols. Each candidate symbol is passed through the chain of above rules. Initially, the symbol is <i>unmarked</i>. If it matches a <code>+</code> rule, it becomes <i>marked</i>, if it matches a <code>&#8211;</code> rule, it becomes <i>unmarked</i> again. If, after applying all rules, the symbol is <i>marked</i>, it will be traced. </p>
<h2>BUGS</h2>
<p> It has most of the bugs stated in <code><a href="/docs/linux/man/1-strace/">strace</a>(1)</code>. </p>
<p> It only works on Linux and in a small subset of architectures. </p>
<p> If you would like to report a bug, send a message to the mailing list (ltrace-devel [at] lists.alioth.debian.org), or use the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a>(1)</code> program if you are under the Debian GNU/Linux distribution. </p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/ltrace.conf</i></p>
<dd> System configuration file</p>
<dt><i>~/.ltrace.conf</i></p>
<dd> Personal config file, overrides <i>/etc/ltrace.conf</i> </p>
</dl>
<h2>AUTHOR</h2>
<p> Juan Cespedes &lt;cespedes [at] debian.org&gt;<br />
 Petr Machata &lt;pmachata [at] redhat.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ltrace-conf/">ltrace.conf</a>(5),</code> <code><a href="/docs/linux/man/1-strace/">strace</a>(1)</code>, <code><a href="/docs/linux/man/2-ptrace/">ptrace</a>(2)</code> </p>
<h2>Index</h2>
