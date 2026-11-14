---
title: "mawk(1)"
name: "mawk"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mawk/"
description: "mawk – pattern scanning and text processing language"
---

<h2 class="name">NAME</h2>
<p> mawk &#8211; pattern scanning and text processing language </p>
<h2>SYNOPSIS</h2>
<p> <code>mawk</code> [-<code>W </code><i>option</i>] [-<code>F </code><i>value</i>] [-<code>v </code><i>var=value</i>] [&#8211;] &#8216;program text&#8217; [file &#8230;]<br />
 <code>mawk</code> [-<code>W </code><i>option</i>] [-<code>F </code><i>value</i>] [-<code>v </code><i>var=value</i>] [-<code>f </code><i>program-file</i>] [&#8211;] [file &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>mawk</code> is an interpreter for the AWK Programming Language. The AWK language is useful for manipulation of data files, text retrieval and processing, and for prototyping and experimenting with algorithms. <code>mawk</code> is a <i>new awk</i> meaning it implements the AWK language as defined in Aho, Kernighan and Weinberger, <i>The AWK Programming Language,</i> Addison-Wesley Publishing, 1988 (hereafter referred to as the AWK book.) <code>mawk</code> conforms to the POSIX 1003.2 (draft 11.3) definition of the AWK language which contains a few features not described in the AWK book, and <code>mawk</code> provides a small number of extensions. </p>
<p> An AWK program is a sequence of <i>pattern {action}</i> pairs and function definitions. Short programs are entered on the command line usually enclosed in &#8216; &#8216; to avoid shell interpretation. Longer programs can be read in from a file with the -f option. Data input is read from the list of files on the command line or from standard input when the list is empty. The input is broken into records as determined by the record separator variable, <code>RS</code>. Initially, <code>RS</code> = &#8220;
&#8221; and records are synonymous with lines. Each record is compared against each <i>pattern</i> and if it matches, the program text for <i>{action}</i> is executed.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;<code>F </code><i>value</i></p>
<dd> sets the field separator, <code>FS</code>, to <i>value</i>.</p>
<dt>&#8211;<code>f </code><i>file</p>
<dd> Program text is read from file</i> instead of from the command line. Multiple <code>-f</code> options are allowed.</p>
<dt>&#8211;<code>v </code><i>var=value</i></p>
<dd> assigns <i>value</i> to program variable <i>var</i>.</p>
<dt>&#8212;</p>
<dd> indicates the unambiguous end of options.</dl>
<p> The above options will be available with any POSIX compatible implementation of AWK. Implementation specific options are prefaced with <code>-W</code>. <code>mawk</code> provides these:</p>
<dl>
<dt>&#8211;<code>W </code>dump</p>
<dd> writes an assembler like listing of the internal representation of the program to stdout and exits 0 (on successful compilation).</p>
<dt>&#8211;<code>W </code>exec <i>file</p>
<dd> Program text is read from file</i> and this is the last option.</p>
<dt>
<dd> This is a useful alternative to &#8211;<code>f</code> on systems that support the <code>#!</code> &#8220;magic number&#8221; convention for executable scripts. Those implicitly pass the pathname of the script itself as the final parameter, and expect no more than one &#8220;-&#8221; option on the <code>#!</code> line. Because <code>mawk</code> can combine multiple &#8211;<code>W</code> options separated by commas, you can use this option when an additional &#8211;<code>W</code> option is needed.</p>
<dt>&#8211;<code>W </code>help</p>
<dd> prints a usage message to stderr and exits (same as &#8220;-<code>W&nbsp;</code>usage&#8221;).</p>
<dt>&#8211;<code>W </code>interactive</p>
<dd> sets unbuffered writes to stdout and line buffered reads from stdin. Records from stdin are lines regardless of the value of <code>RS</code>.</p>
<dt>&#8211;<code>W </code>posix_space</p>
<dd> forces <code>mawk</code> not to consider &#8216;
&#8217; to be space.</p>
<dt>&#8211;<code>W </code>random=<i>num</i></p>
<dd> calls <code>srand</code> with the given parameter (and overrides the auto-seeding behavior).</p>
<dt>&#8211;<code>W </code>sprintf=<i>num</i></p>
<dd> adjusts the size of <code>mawk</code>&#8216;s internal sprintf buffer to <i>num</i> bytes. More than rare use of this option indicates <code>mawk</code> should be recompiled.</p>
<dt>&#8211;<code>W </code>usage</p>
<dd> prints a usage message to stderr and exits (same as &#8220;-<code>W&nbsp;</code>help&#8221;).</p>
<dt>&#8211;<code>W </code>version</p>
<dd> <code>mawk</code> writes its version and copyright to stdout and compiled limits to stderr and exits 0.</dl>
<p> <code>mawk</code> accepts abbreviations for any of these options, e.g., &#8220;-<code>W&nbsp;</code>v&#8221; and &#8220;-<code>W</code>v&#8221; both tell <code>mawk</code> to show its version. </p>
<p> <code>mawk</code> allows multiple <code>-W</code> options to be combined by separating the options with commas, e.g., -Wsprint=2000,posix. This is useful for executable <code>#!</code> &#8220;magic number&#8221; invocations in which only one argument is supported, e.g., &#8211;<code>Winteractive,exec</code>.</p>
<h2>THE AWK LANGUAGE</h2>
<h3>1. Program structure</h3>
<p> An AWK program is a sequence of </code><i>pattern {action}</i> pairs and user function definitions. </p>
<p> A pattern can be: </p>
<pre>
<dl><dt><dd><code>BEGIN</code>
<code>END</code>
expression
expression , expression
</dl>
</pre>
<p> One, but not both, of <i>pattern {action}</i> can be omitted. If <i>{action}</i> is omitted it is implicitly { print }. If <i>pattern</i> is omitted, then it is implicitly matched. <code>BEGIN</code> and <code>END</code> patterns require an action. </p>
<p> Statements are terminated by newlines, semi-colons or both. Groups of statements such as actions or loop bodies are blocked via {&nbsp;&#8230;&nbsp;} as in C. The last statement in a block doesn&#8217;t need a terminator. Blank lines have no meaning; an empty statement is terminated with a semi-colon. Long statements can be continued with a backslash, \. A statement can be broken without a backslash after a comma, left brace, &amp;&amp;, ||, <code>do</code>, <code>else</code>, the right parenthesis of an <code>if</code>, <code>while</code> or <code>for</code> statement, and the right parenthesis of a function definition. A comment starts with # and extends to, but does not include the end of line. </p>
<p> The following statements control program flow inside blocks.</p>
<dl>
<dt>
<dd>
<p> <code>if</code> ( <i>expr</i> ) <i>statement</i> </p>
<p> <code>if</code> ( <i>expr</i> ) <i>statement</i> <code>else</code> <i>statement</i> </p>
<p> <code>while</code> ( <i>expr</i> ) <i>statement</i> </p>
<p> <code>do</code> <i>statement</i> <code>while</code> ( <i>expr</i> ) </p>
<p> <code>for</code> ( <i>opt_expr</i> ; <i>opt_expr</i> ; <i>opt_expr</i> ) <i>statement</i> </p>
<p> <code>for</code> ( <i>var </i><code>in </code><i>array</i> ) <i>statement</i> </p>
<p> <code>continue</code> </p>
<p> <code>break</code></dl>
<h3>2. Data types, conversion and comparison</h3>
<p> There are two basic data types, numeric and string. Numeric constants can be integer like -2, decimal like 1.08, or in scientific notation like -1.1e4 or .28E-3. All numbers are represented internally and all computations are done in floating point arithmetic. So for example, the expression 0.2e2 == 20 is true and true is represented as 1.0. </p>
<p> String constants are enclosed in double quotes. </p>
<p> <center> &quot;This is a string with a newline at the end.
&quot;<br />
 </center> </p>
<p> Strings can be continued across a line by escaping (\) the newline. The following escape sequences are recognized. </code></p>
<pre>
        \              \
        \&quot;              &quot;
                      alert, ascii 7
                      backspace, ascii 8
        	              tab, ascii 9
        
              newline, ascii 10
                      vertical tab, ascii 11
                      formfeed, ascii 12
                      carriage return, ascii 13
        \ddd            1, 2 or 3 octal digits for ascii ddd
        
