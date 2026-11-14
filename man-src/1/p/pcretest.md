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
<h2>SYNOPSIS</h2>
<p> <code>pcretest [options] [input file [output file]]</code> </p>
<p> <code>pcretest</code> was written as a test program for the PCRE regular expression library itself, but it can also be used for experimenting with regular expressions. This document describes the features of the test program; for details of the regular expressions themselves, see the <code>pcrepattern</code> documentation. For details of the PCRE library function calls and their options, see the <code>pcreapi</code> , <code>pcre16</code> and <code>pcre32</code> documentation. </p>
<p> The input for <code>pcretest</code> is a sequence of regular expression patterns and strings to be matched, as described below. The output shows the result of each match. Options on the command line and the patterns control PCRE options and exactly what is output. </p>
<p> As PCRE has evolved, it has acquired many different features, and as a result, <code>pcretest</code> now has rather a lot of obscure options for testing every possible feature. Some of these options are specifically designed for use in conjunction with the test script and data files that are distributed as part of PCRE, and are unlikely to be of use otherwise. They are all documented here, but without much justification.</p>
<h2>PCRE&#8217;s 8-BIT, 16-BIT AND 32-BIT LIBRARIES</h2>
<p> From release 8.30, two separate PCRE libraries can be built. The original one supports 8-bit character strings, whereas the newer 16-bit library supports character strings encoded in 16-bit units. From release 8.32, a third library can be built, supporting character strings encoded in 32-bit units. The <code>pcretest</code> program can be used to test all three libraries. However, it is itself still an 8-bit program, reading 8-bit input and writing 8-bit output. When testing the 16-bit or 32-bit library, the patterns and data strings are converted to 16- or 32-bit format before being passed to the PCRE library functions. Results are converted to 8-bit for output. </p>
<p> References to functions and structures of the form <code>pcre[16|32]_xx</code> below mean &quot;<code>pcre_xx</code> when using the 8-bit library or <code>pcre16_xx</code> when using the 16-bit library&quot;.</p>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt><code>-8</code></p>
<dd> If both the 8-bit library has been built, this option causes the 8-bit library to be used (which is the default); if the 8-bit library has not been built, this option causes an error.</p>
<dt><code>-16</code></p>
<dd> If both the 8-bit or the 32-bit, and the 16-bit libraries have been built, this option causes the 16-bit library to be used. If only the 16-bit library has been built, this is the default (so has no effect). If only the 8-bit or the 32-bit library has been built, this option causes an error.</p>
<dt><code>-32</code></p>
<dd> If both the 8-bit or the 16-bit, and the 32-bit libraries have been built, this option causes the 32-bit library to be used. If only the 32-bit library has been built, this is the default (so has no effect). If only the 8-bit or the 16-bit library has been built, this option causes an error.</p>
<dt><code>-b</code></p>
<dd> Behave as if each pattern has the <code>/B</code> (show byte code) modifier; the internal form is output after compilation.</p>
<dt><code>-C</code></p>
<dd> Output the version number of the PCRE library, and all available information about the optional features that are included, and then exit. All other options are ignored.</p>
<dt><code>-C</code> <i>option</i></p>
<dd> Output information about a specific build-time option, then exit. This functionality is intended for use in scripts such as <code>RunTest</code>. The following options output the value indicated: </p>
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
<dt><code>-d</code></p>
<dd> Behave as if each pattern has the <code>/D</code> (debug) modifier; the internal form and information about the compiled pattern is output after compilation; <code>-d</code> is equivalent to <code>-b -i</code>.</p>
<dt><code>-dfa</code></p>
<dd> Behave as if each data line contains the \D escape sequence; this causes the alternative matching function, <code>pcre[16|32]_dfa_exec()</code>, to be used instead of the standard <code>pcre[16|32]_exec()</code> function (more detail is given below).</p>
<dt><code>-help</code></p>
<dd> Output a brief summary these options and then exit.</p>
<dt><code>-i</code></p>
<dd> Behave as if each pattern has the <code>/I</code> modifier; information about the compiled pattern is given after compilation.</p>
<dt><code>-M</code></p>
<dd> Behave as if each data line contains the \M escape sequence; this causes PCRE to discover the minimum MATCH_LIMIT and MATCH_LIMIT_RECURSION settings by calling <code>pcre[16|32]_exec()</code> repeatedly with different limits.</p>
<dt><code>-m</code></p>
<dd> Output the size of each compiled pattern after it has been compiled. This is equivalent to adding <code>/M</code> to each regular expression. The size is given in bytes for both libraries.</p>
<dt><code>-o</code> <i>osize</i></p>
<dd> Set the number of elements in the output vector that is used when calling <code>pcre[16|32]_exec()</code> or <code>pcre[16|32]_dfa_exec()</code> to be <i>osize</i>. The default value is 45, which is enough for 14 capturing subexpressions for <code>pcre[16|32]_exec()</code> or 22 different matches for <code>pcre[16|32]_dfa_exec()</code>. The vector size can be changed for individual matching calls by including \O in the data line (see below).</p>
<dt><code>-p</code></p>
<dd> Behave as if each pattern has the <code>/P</code> modifier; the POSIX wrapper API is used to call PCRE. None of the other options has any effect when <code>-p</code> is set. This option can be used only with the 8-bit library.</p>
<dt><code>-q</code></p>
<dd> Do not output the version number of <code>pcretest</code> at the start of execution.</p>
<dt><code>-S</code> <i>size</i></p>
<dd> On Unix-like systems, set the size of the run-time stack to <i>size</i> megabytes.</p>
<dt><code>-s</code> or <code>-s+</code></p>
<dd> Behave as if each pattern has the <code>/S</code> modifier; in other words, force each pattern to be studied. If <code>-s+</code> is used, all the JIT compile options are passed to <code>pcre[16|32]_study()</code>, causing just-in-time optimization to be set up if it is available, for both full and partial matching. Specific JIT compile options can be selected by following <code>-s+</code> with a digit in the range 1 to 7, which selects the JIT compile modes as follows: </p>
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
<dt><code>-t</code></p>
<dd> Run each compile, study, and match many times with a timer, and output resulting time per compile or match (in milliseconds). Do not set <code>-m</code> with <code>-t</code>, because you will then get the size output a zillion times, and the timing will be distorted. You can control the number of iterations that are used for timing by following <code>-t</code> with a number (as a separate item on the command line). For example, &quot;-t 1000&quot; would iterate 1000 times. The default is to iterate 500000 times.</p>
<dt><code>-tm</code></p>
<dd> This is like <code>-t</code> except that it times only the matching phase, not the compile or study phases.</dl>
<h2>DESCRIPTION</h2>
<p> If <code>pcretest</code> is given two filename arguments, it reads from the first and writes to the second. If it is given only one filename argument, it reads from that file and writes to stdout. Otherwise, it reads from stdin and writes to stdout, and prompts for each line of input, using &quot;re&gt;&quot; to prompt for regular expressions, and &quot;data&gt;&quot; to prompt for data lines. </p>
<p> When <code>pcretest</code> is built, a configuration option can specify that it should be linked with the <code>libreadline</code> library. When this is done, if the input is from a terminal, it is read using the <code>readline()</code> function. This provides line-editing and history facilities. The output from the <code>-help</code> option states whether or not <code>readline()</code> will be used. </p>
<p> The program handles any number of sets of input on a single input file. Each set starts with a regular expression, and continues with any number of data lines to be matched against the pattern. </p>
<p> Each data line is matched separately and independently. If you want to do multi-line matches, you have to use the 
 escape sequence (or  or 
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
<p> As well as turning on the PCRE_UTF8/16/32 option, the <code>/8</code> modifier causes all non-printing characters in output strings to be printed using the 
