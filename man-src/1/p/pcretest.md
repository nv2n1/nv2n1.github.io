---

title: "pcretest(1)"
name: "pcretest"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcretest/"
description: "pcretest – a program for testing Perl-compatible regular expressions."
---

<h2>NAME</h2>
<p> pcretest &#8211; a program for testing Perl-compatible regular expressions.</p>
<p> <code>pcretest [options] [input file [output file]]</code> </p>
<p> <code>pcretest</code> was written as a test program for the PCRE regular expression library itself, but it can also be used for experimenting with regular expressions. This document describes the features of the test program; for details of the regular expressions themselves, see the <code>pcrepattern</code> documentation. For details of the PCRE library function calls and their options, see the <code>pcreapi</code> , <code>pcre16</code> and <code>pcre32</code> documentation. </p>
<p> The input for <code>pcretest</code> is a sequence of regular expression patterns and strings to be matched, as described below. The output shows the result of each match. Options on the command line and the patterns control PCRE options and exactly what is output. </p>
<p> As PCRE has evolved, it has acquired many different features, and as a result, <code>pcretest</code> now has rather a lot of obscure options for testing every possible feature. Some of these options are specifically designed for use in conjunction with the test script and data files that are distributed as part of PCRE, and are unlikely to be of use otherwise. They are all documented here, but without much justification.</p>
<h2>PCRE&#8217;s 8-BIT, 16-BIT AND 32-BIT LIBRARIES</h2>
<p> From release 8.30, two separate PCRE libraries can be built. The original one supports 8-bit character strings, whereas the newer 16-bit library supports character strings encoded in 16-bit units. From release 8.32, a third library can be built, supporting character strings encoded in 32-bit units. The <code>pcretest</code> program can be used to test all three libraries. However, it is itself still an 8-bit program, reading 8-bit input and writing 8-bit output. When testing the 16-bit or 32-bit library, the patterns and data strings are converted to 16- or 32-bit format before being passed to the PCRE library functions. Results are converted to 8-bit for output. </p>
<p> References to functions and structures of the form <code>pcre[16|32]_xx</code> below mean &quot;<code>pcre_xx</code> when using the 8-bit library or <code>pcre16_xx</code> when using the 16-bit library&quot;.</p>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt><code>-8</code></dt>
<dd> If both the 8-bit library has been built, this option causes the 8-bit library to be used (which is the default); if the 8-bit library has not been built, this option causes an error.</dd>
<dt><code>-16</code></dt>
<dd> If both the 8-bit or the 32-bit, and the 16-bit libraries have been built, this option causes the 16-bit library to be used. If only the 16-bit library has been built, this is the default (so has no effect). If only the 8-bit or the 32-bit library has been built, this option causes an error.</dd>
<dt><code>-32</code></dt>
<dd> If both the 8-bit or the 16-bit, and the 32-bit libraries have been built, this option causes the 32-bit library to be used. If only the 32-bit library has been built, this is the default (so has no effect). If only the 8-bit or the 16-bit library has been built, this option causes an error.</dd>
<dt><code>-b</code></dt>
<dd> Behave as if each pattern has the <code>/B</code> (show byte code) modifier; the internal form is output after compilation.</dd>
<dt><code>-C</code></dt>
<dd> Output the version number of the PCRE library, and all available information about the optional features that are included, and then exit. All other options are ignored.</dd>
<dt><code>-C</code> <i>option</i></dt>
<dd> Output information about a specific build-time option, then exit. This functionality is intended for use in scripts such as <code>RunTest</code>. The following options output the value indicated: </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>ebcdic-nl&nbsp;<wbr>&nbsp;<wbr>the code for LF&nbsp;<wbr>(=&nbsp;<wbr>NL)&nbsp;<wbr>in an EBCDIC environment:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x15 or 0x25<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 if used in an ASCII environment<br />
&nbsp;<wbr>&nbsp;<wbr>linksize&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the internal link size&nbsp;<wbr>(2, 3, or 4)<br />
&nbsp;<wbr>&nbsp;<wbr>newline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the default newline setting:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CR, LF, CRLF, ANYCRLF, or ANY </p>
<p> The following options output 1 for true or zero for false: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ebcdic&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compiled for an EBCDIC environment<br />
&nbsp;<wbr>&nbsp;<wbr>jit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>just-in-time support is available<br />
&nbsp;<wbr>&nbsp;<wbr>pcre16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 16-bit library was built<br />
&nbsp;<wbr>&nbsp;<wbr>pcre32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 32-bit library was built<br />
&nbsp;<wbr>&nbsp;<wbr>pcre8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 8-bit library was built<br />
&nbsp;<wbr>&nbsp;<wbr>ucp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Unicode property support is available<br />
&nbsp;<wbr>&nbsp;<wbr>utf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>UTF-8 and/or UTF-16 and/or UTF-32 support is available</p>
<dt><code>-d</code></dt>
<dd> Behave as if each pattern has the <code>/D</code> (debug) modifier; the internal form and information about the compiled pattern is output after compilation; <code>-d</code> is equivalent to <code>-b -i</code>.</dd>
<dt><code>-dfa</code></dt>
<dd> Behave as if each data line contains the \D escape sequence; this causes the alternative matching function, <code>pcre[16|32]_dfa_exec()</code>, to be used instead of the standard <code>pcre[16|32]_exec()</code> function (more detail is given below).</dd>
<dt><code>-help</code></dt>
<dd> Output a brief summary these options and then exit.</dd>
<dt><code>-i</code></dt>
<dd> Behave as if each pattern has the <code>/I</code> modifier; information about the compiled pattern is given after compilation.</dd>
<dt><code>-M</code></dt>
<dd> Behave as if each data line contains the \M escape sequence; this causes PCRE to discover the minimum MATCH_LIMIT and MATCH_LIMIT_RECURSION settings by calling <code>pcre[16|32]_exec()</code> repeatedly with different limits.</dd>
<dt><code>-m</code></dt>
<dd> Output the size of each compiled pattern after it has been compiled. This is equivalent to adding <code>/M</code> to each regular expression. The size is given in bytes for both libraries.</dd>
<dt><code>-o</code> <i>osize</i></dt>
<dd> Set the number of elements in the output vector that is used when calling <code>pcre[16|32]_exec()</code> or <code>pcre[16|32]_dfa_exec()</code> to be <i>osize</i>. The default value is 45, which is enough for 14 capturing subexpressions for <code>pcre[16|32]_exec()</code> or 22 different matches for <code>pcre[16|32]_dfa_exec()</code>. The vector size can be changed for individual matching calls by including \O in the data line (see below).</dd>
<dt><code>-p</code></dt>
<dd> Behave as if each pattern has the <code>/P</code> modifier; the POSIX wrapper API is used to call PCRE. None of the other options has any effect when <code>-p</code> is set. This option can be used only with the 8-bit library.</dd>
<dt><code>-q</code></dt>
<dd> Do not output the version number of <code>pcretest</code> at the start of execution.</dd>
<dt><code>-S</code> <i>size</i></dt>
<dd> On Unix-like systems, set the size of the run-time stack to <i>size</i> megabytes.</dd>
<dt><code>-s</code> or <code>-s+</code></dt>
<dd> Behave as if each pattern has the <code>/S</code> modifier; in other words, force each pattern to be studied. If <code>-s+</code> is used, all the JIT compile options are passed to <code>pcre[16|32]_study()</code>, causing just-in-time optimization to be set up if it is available, for both full and partial matching. Specific JIT compile options can be selected by following <code>-s+</code> with a digit in the range 1 to 7, which selects the JIT compile modes as follows: </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>normal match only<br />
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>soft partial match only<br />
&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>normal match and soft partial match<br />
&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>hard partial match only<br />
&nbsp;<wbr>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>soft and hard partial match<br />
&nbsp;<wbr>&nbsp;<wbr>7&nbsp;<wbr>&nbsp;<wbr>all three modes&nbsp;<wbr>(default) </p>
<p> If <code>-s++</code> is used instead of <code>-s+</code> (with or without a following digit), the text &quot;(JIT)&quot; is added to the first output line after a match or no match when JIT-compiled code was actually used. </p>
<p> Note that there are pattern options that can override <code>-s</code>, either specifying no studying at all, or suppressing JIT compilation. </p>
<p> If the <code>/I</code> or <code>/D</code> option is present on a pattern (requesting output about the compiled pattern), information about the result of studying is not included when studying is caused only by <code>-s</code> and neither <code>-i</code> nor <code>-d</code> is present on the command line. This behaviour means that the output from tests that are run with and without <code>-s</code> should be identical, except when options that output information about the actual running of a match are set. </p>
<p> The <code>-M</code>, <code>-t</code>, and <code>-tm</code> options, which give information about resources used, are likely to produce different output with and without <code>-s</code>. Output may also differ if the <code>/C</code> option is present on an individual pattern. This uses callouts to trace the the matching process, and this may be different between studied and non-studied patterns. If the pattern contains (*MARK) items there may also be differences, for the same reason. The <code>-s</code> command line option can be overridden for specific patterns that should never be studied (see the <code>/S</code> pattern modifier below).</p>
<dt><code>-t</code></dt>
<dd> Run each compile, study, and match many times with a timer, and output resulting time per compile or match (in milliseconds). Do not set <code>-m</code> with <code>-t</code>, because you will then get the size output a zillion times, and the timing will be distorted. You can control the number of iterations that are used for timing by following <code>-t</code> with a number (as a separate item on the command line). For example, &quot;-t 1000&quot; would iterate 1000 times. The default is to iterate 500000 times.</dd>
<dt><code>-tm</code></dt>
<dd> This is like <code>-t</code> except that it times only the matching phase, not the compile or study phases.</dd></dl>
<p> If <code>pcretest</code> is given two filename arguments, it reads from the first and writes to the second. If it is given only one filename argument, it reads from that file and writes to stdout. Otherwise, it reads from stdin and writes to stdout, and prompts for each line of input, using &quot;re&gt;&quot; to prompt for regular expressions, and &quot;data&gt;&quot; to prompt for data lines. </p>
<p> When <code>pcretest</code> is built, a configuration option can specify that it should be linked with the <code>libreadline</code> library. When this is done, if the input is from a terminal, it is read using the <code>readline()</code> function. This provides line-editing and history facilities. The output from the <code>-help</code> option states whether or not <code>readline()</code> will be used. </p>
<p> The program handles any number of sets of input on a single input file. Each set starts with a regular expression, and continues with any number of data lines to be matched against the pattern. </p>
<p> Each data line is matched separately and independently. If you want to do multi-line matches, you have to use the 
 escape sequence (or 
 or 
, etc., depending on the newline setting) in a single line of input to encode the newline sequences. There is no limit on the length of data lines; the input buffer is automatically extended if it is too small. </p>
<p> An empty line signals the end of the data lines, at which point a new regular expression is read. The regular expressions are given enclosed in any non-alphanumeric delimiters other than backslash, for example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/(a|bc)x+yz/ </p>
<p> White space before the initial delimiter is ignored. A regular expression may be continued over several input lines, in which case the newline characters are included within it. It is possible to include the delimiter within the pattern by escaping it, for example </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/abc\/def/ </p>
<p> If you do so, the escape and the delimiter form part of the pattern, but since delimiters are always non-alphanumeric, this does not affect its interpretation. If the terminating delimiter is immediately followed by a backslash, for example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/abc/\ </p>
<p> then a backslash is added to the end of the pattern. This is done to provide a way of testing the error condition that arises if a pattern finishes with a backslash, because </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/abc\/ </p>
<p> is interpreted as the first line of a pattern that starts with &quot;abc/&quot;, causing pcretest to read the next line as a continuation of the regular expression.</p>
<h2>PATTERN MODIFIERS</h2>
<p> A pattern may be followed by any number of modifiers, which are mostly single characters, though some of these can be qualified by further characters. Following Perl usage, these are referred to below as, for example, &quot;the <code>/i</code> modifier&quot;, even though the delimiter of the pattern need not always be a slash, and no slash is used when writing modifiers. White space may appear between the final pattern delimiter and the first modifier, and between the modifiers themselves. For reference, here is a complete list of modifiers. They fall into several groups that are described in detail in the following sections. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>/8</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set UTF mode<br />
&nbsp;<wbr>&nbsp;<wbr><code>/?</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disable UTF validity check<br />
&nbsp;<wbr>&nbsp;<wbr><code>/+</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show remainder of subject after match<br />
&nbsp;<wbr>&nbsp;<wbr><code>/=</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show all captures&nbsp;<wbr>(not just those that are set) </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>/A</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_ANCHORED<br />
&nbsp;<wbr>&nbsp;<wbr><code>/B</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show compiled code<br />
&nbsp;<wbr>&nbsp;<wbr><code>/C</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_AUTO_CALLOUT<br />
&nbsp;<wbr>&nbsp;<wbr><code>/D</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>same as&nbsp;<wbr><code>/B</code>&nbsp;<wbr>plus&nbsp;<wbr><code>/I</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>/E</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_DOLLAR_ENDONLY<br />
&nbsp;<wbr>&nbsp;<wbr><code>/F</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>flip byte order in compiled pattern<br />
&nbsp;<wbr>&nbsp;<wbr><code>/f</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_FIRSTLINE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/G</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>find all matches&nbsp;<wbr>(shorten string)<br />
&nbsp;<wbr>&nbsp;<wbr><code>/g</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>find all matches&nbsp;<wbr>(use startoffset)<br />
&nbsp;<wbr>&nbsp;<wbr><code>/I</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show information about pattern<br />
&nbsp;<wbr>&nbsp;<wbr><code>/i</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_CASELESS<br />
&nbsp;<wbr>&nbsp;<wbr><code>/J</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_DUPNAMES<br />
&nbsp;<wbr>&nbsp;<wbr><code>/K</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show backtracking control names<br />
&nbsp;<wbr>&nbsp;<wbr><code>/L</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set locale<br />
&nbsp;<wbr>&nbsp;<wbr><code>/M</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show compiled memory size<br />
&nbsp;<wbr>&nbsp;<wbr><code>/m</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_MULTILINE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/N</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_NO_AUTO_CAPTURE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/P</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the POSIX wrapper<br />
&nbsp;<wbr>&nbsp;<wbr><code>/S</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>study the pattern after compilation<br />
&nbsp;<wbr>&nbsp;<wbr><code>/s</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_DOTALL<br />
&nbsp;<wbr>&nbsp;<wbr><code>/T</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>select character tables<br />
&nbsp;<wbr>&nbsp;<wbr><code>/U</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_UNGREEDY<br />
&nbsp;<wbr>&nbsp;<wbr><code>/W</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_UCP<br />
&nbsp;<wbr>&nbsp;<wbr><code>/X</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_EXTRA<br />
&nbsp;<wbr>&nbsp;<wbr><code>/x</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_EXTENDED<br />
&nbsp;<wbr>&nbsp;<wbr><code>/Y</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_NO_START_OPTIMIZE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/Z</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>don&#8217;t show lengths in&nbsp;<wbr><code>/B</code>&nbsp;<wbr>output </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>/&lt;any&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_NEWLINE_ANY<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;anycrlf&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_NEWLINE_ANYCRLF<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;cr&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_NEWLINE_CR<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;crlf&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_NEWLINE_CRLF<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;lf&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_NEWLINE_LF<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;bsr_anycrlf&gt;</code>&nbsp;<wbr>&nbsp;<wbr>set PCRE_BSR_ANYCRLF<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;bsr_unicode&gt;</code>&nbsp;<wbr>&nbsp;<wbr>set PCRE_BSR_UNICODE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;JS&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE_JAVASCRIPT_COMPAT </p>
<h3>Perl-compatible modifiers</h3>
<p> The <code>/i</code>, <code>/m</code>, <code>/s</code>, and <code>/x</code> modifiers set the PCRE_CASELESS, PCRE_MULTILINE, PCRE_DOTALL, or PCRE_EXTENDED options, respectively, when <code>pcre[16|32]_compile()</code> is called. These four modifier letters have the same effect as they do in Perl. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/caseless/i </p>
<h3>Modifiers for other PCRE options</h3>
<p> The following table shows additional modifiers for setting PCRE compile-time options that do not correspond to anything in Perl: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>/8</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_UTF8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>when using the 8-bit<br />
&nbsp;<wbr>&nbsp;<wbr><code>/?</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NO_UTF8_CHECK&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>library </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>/8</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_UTF16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>when using the 16-bit<br />
&nbsp;<wbr>&nbsp;<wbr><code>/?</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NO_UTF16_CHECK&nbsp;<wbr>)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>library </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>/8</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_UTF32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>when using the 32-bit<br />
&nbsp;<wbr>&nbsp;<wbr><code>/?</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NO_UTF32_CHECK&nbsp;<wbr>)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>library </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>/A</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_ANCHORED<br />
&nbsp;<wbr>&nbsp;<wbr><code>/C</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_AUTO_CALLOUT<br />
&nbsp;<wbr>&nbsp;<wbr><code>/E</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_DOLLAR_ENDONLY<br />
&nbsp;<wbr>&nbsp;<wbr><code>/f</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_FIRSTLINE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/J</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_DUPNAMES<br />
&nbsp;<wbr>&nbsp;<wbr><code>/N</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NO_AUTO_CAPTURE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/U</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_UNGREEDY<br />
&nbsp;<wbr>&nbsp;<wbr><code>/W</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_UCP<br />
&nbsp;<wbr>&nbsp;<wbr><code>/X</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_EXTRA<br />
&nbsp;<wbr>&nbsp;<wbr><code>/Y</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NO_START_OPTIMIZE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;any&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NEWLINE_ANY<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;anycrlf&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NEWLINE_ANYCRLF<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;cr&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NEWLINE_CR<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;crlf&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NEWLINE_CRLF<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;lf&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NEWLINE_LF<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;bsr_anycrlf&gt;</code>&nbsp;<wbr>&nbsp;<wbr>PCRE_BSR_ANYCRLF<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;bsr_unicode&gt;</code>&nbsp;<wbr>&nbsp;<wbr>PCRE_BSR_UNICODE<br />
&nbsp;<wbr>&nbsp;<wbr><code>/&lt;JS&gt;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_JAVASCRIPT_COMPAT </p>
<p> The modifiers that are enclosed in angle brackets are literal strings as shown, including the angle brackets, but the letters within can be in either case. This example sets multiline matching with CRLF as the line ending sequence: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/^abc/m&lt;CRLF&gt; </p>
<p> As well as turning on the PCRE_UTF8/16/32 option, the <code>/8</code> modifier causes all non-printing characters in output strings to be printed using the \x{hh...} notation. Otherwise, those less than 0x100 are output in hex without the curly brackets. </p>
<p> Full details of the PCRE options are given in the <code>pcreapi</code> documentation.  </p>
<h3>Finding all matches in a string</h3>
<p> Searching for all possible matches within each subject string can be requested by the <code>/g</code> or <code>/G</code> modifier. After finding a match, PCRE is called again to search the remainder of the subject string. The difference between <code>/g</code> and <code>/G</code> is that the former uses the <i>startoffset</i> argument to <code>pcre[16|32]_exec()</code> to start searching at a new point within the entire string (which is in effect what Perl does), whereas the latter passes over a shortened substring. This makes a difference to the matching process if the pattern begins with a lookbehind assertion (including \b or \B). </p>
<p> If any call to <code>pcre[16|32]_exec()</code> in a <code>/g</code> or <code>/G</code> sequence matches an empty string, the next call is done with the PCRE_NOTEMPTY_ATSTART and PCRE_ANCHORED flags set in order to search for another, non-empty, match at the same point. If this second match fails, the start offset is advanced, and the normal match is retried. This imitates the way Perl handles such cases when using the <code>/g</code> modifier or the <code>split()</code> function. Normally, the start offset is advanced by one character, but if the newline convention recognizes CRLF as a newline, and the current character is CR followed by LF, an advance of two is used.  </p>
<h3>Other modifiers</h3>
<p> There are yet more modifiers for controlling the way <code>pcretest</code> operates. </p>
<p> The <code>/+</code> modifier requests that as well as outputting the substring that matched the entire pattern, <code>pcretest</code> should in addition output the remainder of the subject string. This is useful for tests where the subject contains multiple copies of the same substring. If the <code>+</code> modifier appears twice, the same action is taken for captured substrings. In each case the remainder is output on the following line with a plus character following the capture number. Note that this modifier must not immediately follow the /S modifier because /S+ and /S++ have other meanings. </p>
<p> The <code>/=</code> modifier requests that the values of all potential captured parentheses be output after a match. By default, only those up to the highest one actually used in the match are output (corresponding to the return code from <code>pcre[16|32]_exec()</code>). Values in the offsets vector corresponding to higher numbers should be set to -1, and these are output as &quot;&lt;unset&gt;&quot;. This modifier gives a way of checking that this is happening. </p>
<p> The <code>/B</code> modifier is a debugging feature. It requests that <code>pcretest</code> output a representation of the compiled code after compilation. Normally this information contains length and offset values; however, if <code>/Z</code> is also present, this data is replaced by spaces. This is a special feature for use in the automatic test scripts; it ensures that the same output is generated for different internal link sizes. </p>
<p> The <code>/D</code> modifier is a PCRE debugging feature, and is equivalent to <code>/BI</code>, that is, both the <code>/B</code> and the <code>/I</code> modifiers. </p>
<p> The <code>/F</code> modifier causes <code>pcretest</code> to flip the byte order of the 2-byte and 4-byte fields in the compiled pattern. This facility is for testing the feature in PCRE that allows it to execute patterns that were compiled on a host with a different endianness. This feature is not available when the POSIX interface to PCRE is being used, that is, when the <code>/P</code> pattern modifier is specified. See also the section about saving and reloading compiled patterns below. </p>
<p> The <code>/I</code> modifier requests that <code>pcretest</code> output information about the compiled pattern (whether it is anchored, has a fixed first character, and so on). It does this by calling <code>pcre[16|32]_fullinfo()</code> after compiling a pattern. If the pattern is studied, the results of that are also output. </p>
<p> The <code>/K</code> modifier requests <code>pcretest</code> to show names from backtracking control verbs that are returned from calls to <code>pcre[16|32]_exec()</code>. It causes <code>pcretest</code> to create a <code>pcre[16|32]_extra</code> block if one has not already been created by a call to <code>pcre[16|32]_study()</code>, and to set the PCRE_EXTRA_MARK flag and the <code>mark</code> field within it, every time that <code>pcre[16|32]_exec()</code> is called. If the variable that the <code>mark</code> field points to is non-NULL for a match, non-match, or partial match, <code>pcretest</code> prints the string to which it points. For a match, this is shown on a line by itself, tagged with &quot;MK:&quot;. For a non-match it is added to the message. </p>
<p> The <code>/L</code> modifier must be followed directly by the name of a locale, for example, </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/pattern/Lfr_FR </p>
<p> For this reason, it must be the last modifier. The given locale is set, <code>pcre[16|32]_maketables()</code> is called to build a set of character tables for the locale, and this is then passed to <code>pcre[16|32]_compile()</code> when compiling the regular expression. Without an <code>/L</code> (or <code>/T</code>) modifier, NULL is passed as the tables pointer; that is, <code>/L</code> applies only to the expression on which it appears. </p>
<p> The <code>/M</code> modifier causes the size in bytes of the memory block used to hold the compiled pattern to be output. This does not include the size of the <code>pcre[16|32]</code> block; it is just the actual compiled data. If the pattern is successfully studied with the PCRE_STUDY_JIT_COMPILE option, the size of the JIT compiled code is also output. </p>
<p> The <code>/S</code> modifier causes <code>pcre[16|32]_study()</code> to be called after the expression has been compiled, and the results used when the expression is matched. There are a number of qualifying characters that may follow <code>/S</code>. They may appear in any order. </p>
<p> If <code>S</code> is followed by an exclamation mark, <code>pcre[16|32]_study()</code> is called with the PCRE_STUDY_EXTRA_NEEDED option, causing it always to return a <code>pcre_extra</code> block, even when studying discovers no useful information. </p>
<p> If <code>/S</code> is followed by a second S character, it suppresses studying, even if it was requested externally by the <code>-s</code> command line option. This makes it possible to specify that certain patterns are always studied, and others are never studied, independently of <code>-s</code>. This feature is used in the test files in a few cases where the output is different when the pattern is studied. </p>
<p> If the <code>/S</code> modifier is followed by a + character, the call to <code>pcre[16|32]_study()</code> is made with all the JIT study options, requesting just-in-time optimization support if it is available, for both normal and partial matching. If you want to restrict the JIT compiling modes, you can follow <code>/S+</code> with a digit in the range 1 to 7: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>normal match only <br />
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>soft partial match only <br />
&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>normal match and soft partial match <br />
&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>hard partial match only <br />
&nbsp;<wbr>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>soft and hard partial match <br />
&nbsp;<wbr>&nbsp;<wbr>7&nbsp;<wbr>&nbsp;<wbr>all three modes&nbsp;<wbr>(default) </p>
<p> If <code>/S++</code> is used instead of <code>/S+</code> (with or without a following digit), the text &quot;(JIT)&quot; is added to the first output line after a match or no match when JIT-compiled code was actually used. </p>
<p> Note that there is also an independent <code>/+</code> modifier; it must not be given immediately after <code>/S</code> or <code>/S+</code> because this will be misinterpreted. </p>
<p> If JIT studying is successful, the compiled JIT code will automatically be used when <code>pcre[16|32]_exec()</code> is run, except when incompatible run-time options are specified. For more details, see the <code>pcrejit</code> documentation. See also the <code>\J</code> escape sequence below for a way of setting the size of the JIT stack. </p>
<p> Finally, if <code>/S</code> is followed by a minus character, JIT compilation is suppressed, even if it was requested externally by the <code>-s</code> command line option. This makes it possible to specify that JIT is never to be used for certain patterns. </p>
<p> The <code>/T</code> modifier must be followed by a single digit. It causes a specific set of built-in character tables to be passed to <code>pcre[16|32]_compile()</code>. It is used in the standard PCRE tests to check behaviour with different character tables. The digit specifies the tables as follows: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the default ASCII tables, as distributed in <br />
&nbsp;<wbr>&nbsp;<wbr>pcre_chartables.c.dist <br />
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a set of tables defining ISO 8859 characters </p>
<p> In table 1, some characters whose codes are greater than 128 are identified as letters, digits, spaces, etc.  </p>
<h3>Using the POSIX wrapper API</h3>
<p> The <code>/P</code> modifier causes <code>pcretest</code> to call PCRE via the POSIX wrapper API rather than its native API. This supports only the 8-bit library. When <code>/P</code> is set, the following modifiers set options for the <code>regcomp()</code> function: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_ICASE <br />
&nbsp;<wbr>&nbsp;<wbr>/m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_NEWLINE <br />
&nbsp;<wbr>&nbsp;<wbr>/N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_NOSUB <br />
&nbsp;<wbr>&nbsp;<wbr>/s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_DOTALL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>) <br />
&nbsp;<wbr>&nbsp;<wbr>/U&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_UNGREEDY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>These options are not part of <br />
&nbsp;<wbr>&nbsp;<wbr>/W&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_UCP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the POSIX standard <br />
&nbsp;<wbr>&nbsp;<wbr>/8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_UTF8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>) </p>
<p> The <code>/+</code> modifier works as described above. All other modifiers are ignored.  </p>
<h2>DATA LINES</h2>
<p> Before each data line is passed to <code>pcre[16|32]_exec()</code>, leading and trailing white space is removed, and it is then scanned for \ escapes. Some of these are pretty esoteric features, intended for checking out some of the more complicated features of PCRE. If you are just testing &quot;ordinary&quot; regular expressions, you probably don&#8217;t need any of these. The following escapes are recognized: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>\a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>alarm&nbsp;<wbr>(BEL,&nbsp;<wbr>\x07) <br />
&nbsp;<wbr>&nbsp;<wbr>\b&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>backspace&nbsp;<wbr>(\x08) <br />
&nbsp;<wbr>&nbsp;<wbr>\e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>escape&nbsp;<wbr>(\x27) <br />
&nbsp;<wbr>&nbsp;<wbr>\f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>form feed&nbsp;<wbr>(\x0c) <br />
&nbsp;<wbr>&nbsp;<wbr>\n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>newline&nbsp;<wbr>(\x0a) <br />
&nbsp;<wbr>&nbsp;<wbr>\qdd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set the PCRE_MATCH_LIMIT limit to dd <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(any number of digits) <br />
&nbsp;<wbr>&nbsp;<wbr>\r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>carriage return&nbsp;<wbr>(\x0d) <br />
&nbsp;<wbr>&nbsp;<wbr>\t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tab&nbsp;<wbr>(\x09) <br />
&nbsp;<wbr>&nbsp;<wbr>\v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>vertical tab&nbsp;<wbr>(\x0b) <br />
&nbsp;<wbr>&nbsp;<wbr>\nnn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>octal character&nbsp;<wbr>(up to 3 octal digits);&nbsp;<wbr>always <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a byte unless&nbsp;<wbr>&gt;&nbsp;<wbr>255 in UTF-8 or 16-bit or 32-bit mode <br />
&nbsp;<wbr>&nbsp;<wbr>\xhh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hexadecimal byte&nbsp;<wbr>(up to 2 hex digits) <br />
&nbsp;<wbr>&nbsp;<wbr>\x{hh...}&nbsp;<wbr>&nbsp;<wbr>hexadecimal character&nbsp;<wbr>(any number of hex digits) <br />
&nbsp;<wbr>&nbsp;<wbr>\A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_ANCHORED option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NOTBOL option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\Cdd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>call pcre[16|32]_copy_substring()&nbsp;<wbr>for substring dd <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>after a successful match&nbsp;<wbr>(number less than 32) <br />
&nbsp;<wbr>&nbsp;<wbr>\Cname&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>call pcre[16|32]_copy_named_substring()&nbsp;<wbr>for substring <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;name&quot;&nbsp;<wbr>after a successful match&nbsp;<wbr>(name terminated <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by next non alphanumeric character) <br />
&nbsp;<wbr>&nbsp;<wbr>\C+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show the current captured substrings at callout <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>time <br />
&nbsp;<wbr>&nbsp;<wbr>\C-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not supply a callout function <br />
&nbsp;<wbr>&nbsp;<wbr>\C!n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>return 1 instead of 0 when callout number n is <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reached <br />
&nbsp;<wbr>&nbsp;<wbr>\C!n!m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>return 1 instead of 0 when callout number n is <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reached for the nth time <br />
&nbsp;<wbr>&nbsp;<wbr>\C*n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the number n&nbsp;<wbr>(may be negative)&nbsp;<wbr>as callout <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data;&nbsp;<wbr>this is used as the callout return value <br />
&nbsp;<wbr>&nbsp;<wbr>\D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code>&nbsp;<wbr>match function <br />
&nbsp;<wbr>&nbsp;<wbr>\F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only shortest match for&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\Gdd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>call pcre[16|32]_get_substring()&nbsp;<wbr>for substring dd <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>after a successful match&nbsp;<wbr>(number less than 32) <br />
&nbsp;<wbr>&nbsp;<wbr>\Gname&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>call pcre[16|32]_get_named_substring()&nbsp;<wbr>for substring <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;name&quot;&nbsp;<wbr>after a successful match&nbsp;<wbr>(name terminated <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>by next non-alphanumeric character) <br />
&nbsp;<wbr>&nbsp;<wbr>\Jdd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set up a JIT stack of dd kilobytes maximum&nbsp;<wbr>(any <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>number of digits) <br />
&nbsp;<wbr>&nbsp;<wbr>\L&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>call pcre[16|32]_get_substringlist()&nbsp;<wbr>after a <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>successful match <br />
&nbsp;<wbr>&nbsp;<wbr>\M&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>discover the minimum MATCH_LIMIT and <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MATCH_LIMIT_RECURSION settings <br />
&nbsp;<wbr>&nbsp;<wbr>\N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NOTEMPTY option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code>;&nbsp;<wbr>if used twice, pass the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_NOTEMPTY_ATSTART option <br />
&nbsp;<wbr>&nbsp;<wbr>\Odd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set the size of the output vector passed to <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>pcre[16|32]_exec()</code>&nbsp;<wbr>to dd&nbsp;<wbr>(any number of digits) <br />
&nbsp;<wbr>&nbsp;<wbr>\P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_PARTIAL_SOFT option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code>;&nbsp;<wbr>if used twice, pass the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE_PARTIAL_HARD option <br />
&nbsp;<wbr>&nbsp;<wbr>\Qdd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set the PCRE_MATCH_LIMIT_RECURSION limit to dd <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(any number of digits) <br />
&nbsp;<wbr>&nbsp;<wbr>\R&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_DFA_RESTART option to&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>output details of memory get/free calls during matching <br />
&nbsp;<wbr>&nbsp;<wbr>\Y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NO_START_OPTIMIZE option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\Z&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NOTEOL option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NO_UTF[8|16|32]_CHECK option to <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>pcre[16|32]_exec()</code>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\&gt;dd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>start the match at offset dd&nbsp;<wbr>(optional&nbsp;<wbr>&quot;-&quot;;&nbsp;<wbr>then <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>any number of digits);&nbsp;<wbr>this sets the&nbsp;<wbr><i>startoffset</i> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>argument for&nbsp;<wbr><code>pcre[16|32]_exec()</code>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\&lt;cr&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NEWLINE_CR option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\&lt;lf&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NEWLINE_LF option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\&lt;crlf&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NEWLINE_CRLF option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\&lt;anycrlf&gt;&nbsp;<wbr>pass the PCRE_NEWLINE_ANYCRLF option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>\&lt;any&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the PCRE_NEWLINE_ANY option to&nbsp;<wbr><code>pcre[16|32]_exec()</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr><code>pcre[16|32]_dfa_exec()</code> </p>
<p> The use of \x{hh...} is not dependent on the use of the <code>/8</code> modifier on the pattern. It is recognized always. There may be any number of hexadecimal digits inside the braces; invalid values provoke error messages. </p>
<p> Note that \xhh specifies one byte rather than one character in UTF-8 mode; this makes it possible to construct invalid UTF-8 sequences for testing purposes. On the other hand, \x{hh} is interpreted as a UTF-8 character in UTF-8 mode, generating more than one byte if the value is greater than 127. When testing the 8-bit library not in UTF-8 mode, \x{hh} generates one byte for values less than 256, and causes an error for greater values. </p>
<p> In UTF-16 mode, all 4-digit \x{hhhh} values are accepted. This makes it possible to construct invalid UTF-16 sequences for testing purposes. </p>
<p> In UTF-32 mode, all 4- to 8-digit \x{...} values are accepted. This makes it possible to construct invalid UTF-32 sequences for testing purposes. </p>
<p> The escapes that specify line ending sequences are literal strings, exactly as shown. No more than one newline setting should be present in any data line. </p>
<p> A backslash followed by anything else just escapes the anything else. If the very last character is a backslash, it is ignored. This gives a way of passing an empty line as data, since a real empty line terminates the data input. </p>
<p> The <code>\J</code> escape provides a way of setting the maximum stack size that is used by the just-in-time optimization code. It is ignored if JIT optimization is not being used. Providing a stack that is larger than the default 32K is necessary only for very complicated patterns. </p>
<p> If \M is present, <code>pcretest</code> calls <code>pcre[16|32]_exec()</code> several times, with different values in the <i>match_limit</i> and <i>match_limit_recursion</i> fields of the <code>pcre[16|32]_extra</code> data structure, until it finds the minimum numbers for each parameter that allow <code>pcre[16|32]_exec()</code> to complete without error. Because this is testing a specific feature of the normal interpretive <code>pcre[16|32]_exec()</code> execution, the use of any JIT optimization that might have been set up by the <code>/S+</code> qualifier of <code>-s+</code> option is disabled. </p>
<p> The <i>match_limit</i> number is a measure of the amount of backtracking that takes place, and checking it out can be instructive. For most simple matches, the number is quite small, but for patterns with very large numbers of matching possibilities, it can become large very quickly with increasing length of subject string. The <i>match_limit_recursion</i> number is a measure of how much stack (or, if PCRE is compiled with NO_RECURSE, how much heap) memory is needed to complete the match attempt. </p>
<p> When \O is used, the value specified may be higher or lower than the size set by the <code>-O</code> command line option (or defaulted to 45); \O applies only to the call of <code>pcre[16|32]_exec()</code> for the line in which it appears. </p>
<p> If the <code>/P</code> modifier was present on the pattern, causing the POSIX wrapper API to be used, the only option-setting sequences that have any effect are \B, \N, and \Z, causing REG_NOTBOL, REG_NOTEMPTY, and REG_NOTEOL, respectively, to be passed to <code>regexec()</code>.  </p>
<h2>THE ALTERNATIVE MATCHING FUNCTION</h2>
<p> By default, <code>pcretest</code> uses the standard PCRE matching function, <code>pcre[16|32]_exec()</code> to match each data line. PCRE also supports an alternative matching function, <code>pcre[16|32]_dfa_test()</code>, which operates in a different way, and has some restrictions. The differences between the two functions are described in the <code>pcrematching</code> documentation. </p>
<p> If a data line contains the \D escape sequence, or if the command line contains the <code>-dfa</code> option, the alternative matching function is used. This function finds all possible matches at a given point. If, however, the \F escape sequence is present in the data line, it stops after the first match is found. This is always the shortest possible match.  </p>
<h2>DEFAULT OUTPUT FROM PCRETEST</h2>
<p> This section describes the output when the normal matching function, <code>pcre[16|32]_exec()</code>, is being used. </p>
<p> When a match succeeds, <code>pcretest</code> outputs the list of captured substrings that <code>pcre[16|32]_exec()</code> returns, starting with number 0 for the string that matched the whole pattern. Otherwise, it outputs &quot;No match&quot; when the return is PCRE_ERROR_NOMATCH, and &quot;Partial match:&quot; followed by the partially matching substring when <code>pcre[16|32]_exec()</code> returns PCRE_ERROR_PARTIAL. (Note that this is the entire substring that was inspected during the partial match; it may include characters before the actual match start if a lookbehind assertion, \K, \b, or \B was involved.) For any other return, <code>pcretest</code> outputs the PCRE negative error number and a short descriptive phrase. If the error is a failed UTF string check, the offset of the start of the failing character and the reason code are also output, provided that the size of the output vector is at least two. Here is an example of an interactive <code>pcretest</code> run. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>pcretest <br />
&nbsp;<wbr>&nbsp;<wbr>PCRE version 8.13 2011-04-30 </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/^abc(\d+)/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>abc123 <br />
0: abc123 <br />
1: 123 <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>xyz <br />
&nbsp;<wbr>&nbsp;<wbr>No match </p>
<p> Unset capturing substrings that are not followed by one that is set are not returned by <code>pcre[16|32]_exec()</code>, and are not shown by <code>pcretest</code>. In the following example, there are two capturing substrings, but when the first data line is matched, the second, unset substring is not shown. An &quot;internal&quot; unset substring is shown as &quot;&lt;unset&gt;&quot;, as for the second data line. </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(a)|(b)/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>a <br />
0: a <br />
1: a <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>b <br />
0: b <br />
1:&nbsp;<wbr>&lt;unset&gt; <br />
2: b </p>
<p> If the strings contain any non-printing characters, they are output as \xhh escapes if the value is less than 256 and UTF mode is not set. Otherwise they are output as \x{hh...} escapes. See below for the definition of non-printing characters. If the pattern has the <code>/+</code> modifier, the output for substring 0 is followed by the the rest of the subject string, identified by &quot;0+&quot; like this: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/cat/+ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>cataract <br />
0: cat <br />
0+&nbsp;<wbr>aract </p>
<p> If the pattern has the <code>/g</code> or <code>/G</code> modifier, the results of successive matching attempts are output in sequence, like this: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/\Bi(\w\w)/g <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>Mississippi <br />
0: iss <br />
1: ss <br />
0: iss <br />
1: ss <br />
0: ipp <br />
1: pp </p>
<p> &quot;No match&quot; is output only if the first match attempt fails. Here is an example of a failure message (the offset 4 that is specified by \&gt;4 is past the end of the subject string): </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/xyz/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>xyz\&gt;4 <br />
&nbsp;<wbr>&nbsp;<wbr>Error -24&nbsp;<wbr>(bad offset value) </p>
<p> If any of the sequences <code>\C</code>, <code>\G</code>, or <code>\L</code> are present in a data line that is successfully matched, the substrings extracted by the convenience functions are output with C, G, or L after the string number instead of a colon. This is in addition to the normal full list. The string length (that is, the return from the extraction function) is given in parentheses after each string for <code>\C</code> and <code>\G</code>. </p>
<p> Note that whereas patterns can be continued over several lines (a plain &quot;&gt;&quot; prompt is used for continuations), data lines may not. However newlines can be included in data by means of the \n escape (or \r, \r\n, etc., depending on the newline sequence setting).  </p>
<h2>OUTPUT FROM THE ALTERNATIVE MATCHING FUNCTION</h2>
<p> When the alternative matching function, <code>pcre[16|32]_dfa_exec()</code>, is used (by means of the \D escape sequence or the <code>-dfa</code> command line option), the output consists of a list of all the matches that start at the first point in the subject where there is at least one match. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(tang|tangerine|tan)/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>yellow tangerine\D <br />
0: tangerine <br />
1: tang <br />
2: tan </p>
<p> (Using the normal matching function on this data finds only &quot;tang&quot;.) The longest matching string is always given first (and numbered zero). After a PCRE_ERROR_PARTIAL return, the output is &quot;Partial match:&quot;, followed by the partially matching substring. (Note that this is the entire substring that was inspected during the partial match; it may include characters before the actual match start if a lookbehind assertion, \K, \b, or \B was involved.) </p>
<p> If <code>/g</code> is present on the pattern, the search for further matches resumes at the end of the longest match. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(tang|tangerine|tan)/g <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>yellow tangerine and tangy sultana\D <br />
0: tangerine <br />
1: tang <br />
2: tan <br />
0: tang <br />
1: tan <br />
0: tan </p>
<p> Since the matching function does not support substring capture, the escape sequences that are concerned with captured substrings are not relevant.  </p>
<h2>RESTARTING AFTER A PARTIAL MATCH</h2>
<p> When the alternative matching function has given the PCRE_ERROR_PARTIAL return, indicating that the subject partially matched the pattern, you can restart the match with additional subject data by means of the \R escape sequence. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/^\d?\d(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d\d$/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>23ja\P\D <br />
&nbsp;<wbr>&nbsp;<wbr>Partial match: 23ja <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>n05\R\D <br />
0: n05 </p>
<p> For further information about partial matching, see the <code>pcrepartial</code> documentation.  </p>
<h2>CALLOUTS</h2>
<p> If the pattern contains any callout requests, <code>pcretest</code>&#8216;s callout function is called during matching. This works with both matching functions. By default, the called function displays the callout number, the start and current positions in the text at the callout time, and the next pattern item to be tested. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>---&gt;pqrabcdef <br />
&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\d </p>
<p> This output indicates that callout number 0 occurred for a match attempt starting at the fourth character of the subject string, when the pointer was at the seventh character of the data, and when the next pattern item was \d. Just one circumflex is output if the start and current positions are the same. </p>
<p> Callouts numbered 255 are assumed to be automatic callouts, inserted as a result of the <code>/C</code> pattern modifier. In this case, instead of showing the callout number, the offset in the pattern, preceded by a plus, is output. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/\d?[A-E]\*/C <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>E* <br />
&nbsp;<wbr>&nbsp;<wbr>---&gt;E* <br />
+0&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\d? <br />
+3&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[A-E] <br />
+8&nbsp;<wbr>^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\* <br />
&nbsp;<wbr>&nbsp;<wbr>+10&nbsp;<wbr>^&nbsp;<wbr>^ <br />
0: E* </p>
<p> If a pattern contains (*MARK) items, an additional line is output whenever a change of latest mark is passed to the callout function. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/a(*MARK:X)bc/C <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>abc <br />
&nbsp;<wbr>&nbsp;<wbr>---&gt;abc <br />
+0&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a <br />
+1&nbsp;<wbr>^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(*MARK:X) <br />
&nbsp;<wbr>&nbsp;<wbr>+10&nbsp;<wbr>^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>b <br />
&nbsp;<wbr>&nbsp;<wbr>Latest Mark: X <br />
&nbsp;<wbr>&nbsp;<wbr>+11&nbsp;<wbr>^&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>c <br />
&nbsp;<wbr>&nbsp;<wbr>+12&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>^ <br />
0: abc </p>
<p> The mark changes between matching &quot;a&quot; and &quot;b&quot;, but stays the same for the rest of the match, so nothing more is output. If, as a result of backtracking, the mark reverts to being unset, the text &quot;&lt;unset&gt;&quot; is output. </p>
<p> The callout function in <code>pcretest</code> returns zero (carry on matching) by default, but you can use a \C item in a data line (as described above) to change this and other parameters of the callout. </p>
<p> Inserting callouts can be helpful when using <code>pcretest</code> to check complicated regular expressions. For further information about callouts, see the <code>pcrecallout</code> documentation.  </p>
<h2>NON-PRINTING CHARACTERS</h2>
<p> When <code>pcretest</code> is outputting text in the compiled version of a pattern, bytes other than 32-126 are always treated as non-printing characters are are therefore shown as hex escapes. </p>
<p> When <code>pcretest</code> is outputting text that is a matched part of a subject string, it behaves in the same way, unless a different locale has been set for the pattern (using the <code>/L</code> modifier). In this case, the <code>isprint()</code> function to distinguish printing and non-printing characters.  </p>
<h2>SAVING AND RELOADING COMPILED PATTERNS</h2>
<p> The facilities described in this section are not available when the POSIX interface to PCRE is being used, that is, when the <code>/P</code> pattern modifier is specified. </p>
<p> When the POSIX interface is not in use, you can cause <code>pcretest</code> to write a compiled pattern to a file, by following the modifiers with &gt; and a file name. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/pattern/im&nbsp;<wbr>&gt;/some/file </p>
<p> See the <code>pcreprecompile</code> documentation for a discussion about saving and re-using compiled patterns. Note that if the pattern was successfully studied with JIT optimization, the JIT data cannot be saved. </p>
<p> The data that is written is binary. The first eight bytes are the length of the compiled pattern data followed by the length of the optional study data, each written as four bytes in big-endian order (most significant byte first). If there is no study data (either the pattern was not studied, or studying did not return any data), the second length is zero. The lengths are followed by an exact copy of the compiled pattern. If there is additional study data, this (excluding any JIT data) follows immediately after the compiled pattern. After writing the file, <code>pcretest</code> expects to read a new pattern. </p>
<p> A saved pattern can be reloaded into <code>pcretest</code> by specifying &lt; and a file name instead of a pattern. The name of the file must not contain a &lt; character, as otherwise <code>pcretest</code> will interpret the line as a pattern delimited by &lt; characters. For example: </p>
<p> <br />
re&gt;&nbsp;<wbr>&lt;/some/file <br />
&nbsp;<wbr>&nbsp;<wbr>Compiled pattern loaded from&nbsp;<wbr>/some/file <br />
&nbsp;<wbr>&nbsp;<wbr>No study data </p>
<p> If the pattern was previously studied with the JIT optimization, the JIT information cannot be saved and restored, and so is lost. When the pattern has been loaded, <code>pcretest</code> proceeds to read data lines in the usual way. </p>
<p> You can copy a file written by <code>pcretest</code> to a different host and reload it there, even if the new host has opposite endianness to the one on which the pattern was compiled. For example, you can compile on an i86 machine and run on a SPARC machine. When a pattern is reloaded on a host with different endianness, the confirmation message is changed to: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>Compiled pattern&nbsp;<wbr>(byte-inverted)&nbsp;<wbr>loaded from&nbsp;<wbr>/some/file </p>
<p> The test suite contains some saved pre-compiled patterns with different endianness. These are reloaded using &quot;&lt;!&quot; instead of just &quot;&lt;&quot;. This suppresses the &quot;(byte-inverted)&quot; text so that the output is the same on all hosts. It also forces debugging output once the pattern has been reloaded. </p>
<p> File names for saving and reloading can be absolute or relative, but note that the shell facility of expanding a file name that starts with a tilde (~) is not available. </p>
<p> The ability to save and reload files in <code>pcretest</code> is intended for testing and experimentation. It is not intended for production use because only a single pattern can be written to a file. Furthermore, there is no facility for supplying custom character tables for use with a reloaded pattern. If the original pattern was compiled with custom tables, an attempt to match a subject string using a reloaded pattern is likely to cause <code>pcretest</code> to crash. Finally, if you attempt to load a file that is not in the correct format, the result is undefined.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pcre/">pcre</a></code>(3), <code><a href="/docs/linux/man/3-pcre16/">pcre16</a></code>(3), <code><a href="/docs/linux/man/3-pcre32/">pcre32</a></code>(3), <code><a href="/docs/linux/man/3-pcreapi/">pcreapi</a></code>(3), <code><a href="/docs/linux/man/3-pcrecallout/">pcrecallout</a></code>(3), <code>pcrejit</code>, <code><a href="/docs/linux/man/3-pcrematching/">pcrematching</a></code>(3), <code>pcrepartial</code>(d), <code><a href="/docs/linux/man/3-pcrepattern/">pcrepattern</a></code>(3), <code><a href="/docs/linux/man/3-pcreprecompile/">pcreprecompile</a></code>(3).  </p>
<h2>AUTHOR</h2>
<pre><code>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.
</code></pre>
<h2>REVISION</h2>
<pre><code>Last updated: 10 September 2012
Copyright (c) 1997-2012 University of Cambridge.
</code></pre>
