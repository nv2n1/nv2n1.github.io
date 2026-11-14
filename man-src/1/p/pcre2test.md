---
title: "pcre2test(1)"
name: "pcre2test"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcre2test/"
description: "pcre2test – a program for testing Perl-compatible regular expressions."
---

<h2>NAME</h2>
<p> pcre2test &#8211; a program for testing Perl-compatible regular expressions.</p>
<h2>SYNOPSIS</h2>
<p> <code>pcre2test [options] [input file [output file]]</code> </p>
<p> <code>pcre2test</code> is a test program for the PCRE2 regular expression libraries, but it can also be used for experimenting with regular expressions. This document describes the features of the test program; for details of the regular expressions themselves, see the <code>pcre2pattern</code> documentation. For details of the PCRE2 library function calls and their options, see the <code>pcre2api</code> documentation. </p>
<p> The input for <code>pcre2test</code> is a sequence of regular expression patterns and subject strings to be matched. There are also command lines for setting defaults and controlling some special actions. The output shows the result of each match attempt. Modifiers on external or internal command lines, the patterns, and the subject lines specify PCRE2 function options, control how the subject is processed, and what output is produced. </p>
<p> As the original fairly simple PCRE library evolved, it acquired many different features, and as a result, the original <code>pcretest</code> program ended up with a lot of options in a messy, arcane syntax, for testing all the features. The move to the new PCRE2 API provided an opportunity to re-implement the test program as <code>pcre2test</code>, with a cleaner modifier syntax. Nevertheless, there are still many obscure modifiers, some of which are specifically designed for use in conjunction with the test script and data files that are distributed as part of PCRE2. All the modifiers are documented here, some without much justification, but many of them are unlikely to be of use except when testing the libraries.</p>
<h2>PCRE2&#8217;s 8-BIT, 16-BIT AND 32-BIT LIBRARIES</h2>
<p> Different versions of the PCRE2 library can be built to support character strings that are encoded in 8-bit, 16-bit, or 32-bit code units. One, two, or all three of these libraries may be simultaneously installed. The <code>pcre2test</code> program can be used to test all the libraries. However, its own input and output are always in 8-bit format. When testing the 16-bit or 32-bit libraries, patterns and subject strings are converted to 16- or 32-bit format before being passed to the library functions. Results are converted back to 8-bit code units for output. </p>
<p> In the rest of this document, the names of library functions and structures are given in generic form, for example, <code>pcre_compile()</code>. The actual names used in the libraries have a suffix _8, _16, or _32, as appropriate.</p>
<h2>INPUT ENCODING</h2>
<p> Input to <code>pcre2test</code> is processed line by line, either by calling the C library&#8217;s <code>fgets()</code> function, or via the <code>libreadline</code> library (see below). The input is processed using using C&#8217;s string functions, so must not contain binary zeroes, even though in Unix-like environments, <code>fgets()</code> treats any bytes other than newline as data characters. In some Windows environments character 26 (hex 1A) causes an immediate end of file, and no further data is read. </p>
<p> For maximum portability, therefore, it is safest to avoid non-printing characters in <code>pcre2test</code> input files. There is a facility for specifying a pattern&#8217;s characters as hexadecimal pairs, thus making it possible to include binary zeroes in a pattern for testing purposes. Subject lines are processed for backslash escapes, which makes it possible to include any data value.</p>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt><code>-8</code></p>
<dd> If the 8-bit library has been built, this option causes it to be used (this is the default). If the 8-bit library has not been built, this option causes an error.</p>
<dt><code>-16</code></p>
<dd> If the 16-bit library has been built, this option causes it to be used. If only the 16-bit library has been built, this is the default. If the 16-bit library has not been built, this option causes an error.</p>
<dt><code>-32</code></p>
<dd> If the 32-bit library has been built, this option causes it to be used. If only the 32-bit library has been built, this is the default. If the 32-bit library has not been built, this option causes an error.</p>
<dt><code>-b</code></p>
<dd> Behave as if each pattern has the <code>/fullbincode</code> modifier; the full internal binary form of the pattern is output after compilation.</p>
<dt><code>-C</code></p>
<dd> Output the version number of the PCRE2 library, and all available information about the optional features that are included, and then exit with zero exit code. All other options are ignored.</p>
<dt><code>-C</code> <i>option</i></p>
<dd> Output information about a specific build-time option, then exit. This functionality is intended for use in scripts such as <code>RunTest</code>. The following options output the value and set the exit code as indicated: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ebcdic-nl&nbsp;<wbr>&nbsp;<wbr>the code for LF&nbsp;<wbr>(=&nbsp;<wbr>NL)&nbsp;<wbr>in an EBCDIC environment:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x15 or 0x25<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 if used in an ASCII environment<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit code is always 0<br />
&nbsp;<wbr>&nbsp;<wbr>linksize&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the configured internal link size&nbsp;<wbr>(2, 3, or 4)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit code is set to the link size<br />
&nbsp;<wbr>&nbsp;<wbr>newline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the default newline setting:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CR, LF, CRLF, ANYCRLF, or ANY<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit code is always 0<br />
&nbsp;<wbr>&nbsp;<wbr>bsr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the default setting for what&nbsp;<wbr>\R matches:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ANYCRLF or ANY<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit code is always 0 </p>
<p> The following options output 1 for true or 0 for false, and set the exit code to the same value: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>backslash-C&nbsp;<wbr>&nbsp;<wbr>\C is supported&nbsp;<wbr>(not locked out)<br />
&nbsp;<wbr>&nbsp;<wbr>ebcdic&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compiled for an EBCDIC environment<br />
&nbsp;<wbr>&nbsp;<wbr>jit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>just-in-time support is available<br />
&nbsp;<wbr>&nbsp;<wbr>pcre2-16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 16-bit library was built<br />
&nbsp;<wbr>&nbsp;<wbr>pcre2-32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 32-bit library was built<br />
&nbsp;<wbr>&nbsp;<wbr>pcre2-8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 8-bit library was built<br />
&nbsp;<wbr>&nbsp;<wbr>unicode&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Unicode support is available </p>
<p> If an unknown option is given, an error message is output; the exit code is 0.</p>
<dt><code>-d</code></p>
<dd> Behave as if each pattern has the <code>debug</code> modifier; the internal form and information about the compiled pattern is output after compilation; <code>-d</code> is equivalent to <code>-b -i</code>.</p>
<dt><code>-dfa</code></p>
<dd> Behave as if each subject line has the <code>dfa</code> modifier; matching is done using the <code>pcre2_dfa_match()</code> function instead of the default <code>pcre2_match()</code>.</p>
<dt><code>-help</code></p>
<dd> Output a brief summary these options and then exit.</p>
<dt><code>-i</code></p>
<dd> Behave as if each pattern has the <code>/info</code> modifier; information about the compiled pattern is given after compilation.</p>
<dt><code>-jit</code></p>
<dd> Behave as if each pattern line has the <code>jit</code> modifier; after successful compilation, each pattern is passed to the just-in-time compiler, if available.</p>
<dt><code>-pattern </code><i>modifier-list</i></p>
<dd> Behave as if each pattern line contains the given modifiers.</p>
<dt><code>-q</code></p>
<dd> Do not output the version number of <code>pcre2test</code> at the start of execution.</p>
<dt><code>-S</code> <i>size</i></p>
<dd> On Unix-like systems, set the size of the run-time stack to <i>size</i> megabytes.</p>
<dt><code>-subject</code> <i>modifier-list</i></p>
<dd> Behave as if each subject line contains the given modifiers.</p>
<dt><code>-t</code></p>
<dd> Run each compile and match many times with a timer, and output the resulting times per compile or match. When JIT is used, separate times are given for the initial compile and the JIT compile. You can control the number of iterations that are used for timing by following <code>-t</code> with a number (as a separate item on the command line). For example, &quot;-t 1000&quot; iterates 1000 times. The default is to iterate 500,000 times.</p>
<dt><code>-tm</code></p>
<dd> This is like <code>-t</code> except that it times only the matching phase, not the compile phase.</p>
<dt><code>-T</code> <code>-TM</code></p>
<dd> These behave like <code>-t</code> and <code>-tm</code>, but in addition, at the end of a run, the total times for all compiles and matches are output.</p>
<dt><code>-version</code></p>
<dd> Output the PCRE2 version number and then exit.</dl>
<h2>DESCRIPTION</h2>
<p> If <code>pcre2test</code> is given two filename arguments, it reads from the first and writes to the second. If the first name is &quot;-&quot;, input is taken from the standard input. If <code>pcre2test</code> is given only one argument, it reads from that file and writes to stdout. Otherwise, it reads from stdin and writes to stdout. </p>
<p> When <code>pcre2test</code> is built, a configuration option can specify that it should be linked with the <code>libreadline</code> or <code>libedit</code> library. When this is done, if the input is from a terminal, it is read using the <code>readline()</code> function. This provides line-editing and history facilities. The output from the <code>-help</code> option states whether or not <code>readline()</code> will be used. </p>
<p> The program handles any number of tests, each of which consists of a set of input lines. Each set starts with a regular expression pattern, followed by any number of subject lines to be matched against that pattern. In between sets of test data, command lines that begin with # may appear. This file format, with some restrictions, can also be processed by the <code>perltest.sh</code> script that is distributed with PCRE2 as a means of checking that the behaviour of PCRE2 and Perl is the same. </p>
<p> When the input is a terminal, <code>pcre2test</code> prompts for each line of input, using &quot;re&gt;&quot; to prompt for regular expression patterns, and &quot;data&gt;&quot; to prompt for subject lines. Command lines starting with # can be entered only in response to the &quot;re&gt;&quot; prompt. </p>
<p> Each subject line is matched separately and independently. If you want to do multi-line matches, you have to use the 
 escape sequence (or  or 
, etc., depending on the newline setting) in a single line of input to encode the newline sequences. There is no limit on the length of subject lines; the input buffer is automatically extended if it is too small. There are replication features that makes it possible to generate long repetitive pattern or subject lines without having to supply them explicitly. </p>
<p> An empty line or the end of the file signals the end of the subject lines for a test, at which point a new pattern or command line is expected if there is still input to be read.</p>
<h2>COMMAND LINES</h2>
<p> In between sets of test data, a line that begins with # is interpreted as a command line. If the first character is followed by white space or an exclamation mark, the line is treated as a comment, and ignored. Otherwise, the following commands are recognized: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#forbid_utf </p>
<p> Subsequent patterns automatically have the PCRE2_NEVER_UTF and PCRE2_NEVER_UCP options set, which locks out the use of the PCRE2_UTF and PCRE2_UCP options and the use of (*UTF) and (*UCP) at the start of patterns. This command also forces an error if a subsequent pattern contains any occurrences of \P, \p, or \X, which are still supported when PCRE2_UTF is not set, but which require Unicode property support to be included in the library. </p>
<p> This is a trigger guard that is used in test files to ensure that UTF or Unicode property tests are not accidentally added to files that are used when Unicode support is not included in the library. Setting PCRE2_NEVER_UTF and PCRE2_NEVER_UCP as a default can also be obtained by the use of <code>#pattern</code>; the difference is that <code>#forbid_utf</code> cannot be unset, and the automatic options are not displayed in pattern information, to avoid cluttering up test output. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#load&nbsp;<wbr>&lt;filename&gt; </p>
<p> This command is used to load a set of precompiled patterns from a file, as described in the section entitled &quot;Saving and restoring compiled patterns&quot; below. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#newline_default&nbsp;<wbr>[&lt;newline-list&gt;] </p>
<p> When PCRE2 is built, a default newline convention can be specified. This determines which characters and/or character pairs are recognized as indicating a newline in a pattern or subject string. The default can be overridden when a pattern is compiled. The standard test files contain tests of various newline conventions, but the majority of the tests expect a single linefeed to be recognized as a newline by default. Without special action the tests would fail when PCRE2 is compiled with either CR or CRLF as the default newline. </p>
<p> The #newline_default command specifies a list of newline types that are acceptable as the default. The types must be one of CR, LF, CRLF, ANYCRLF, or ANY (in upper or lower case), for example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#newline_default LF Any anyCRLF </p>
<p> If the default newline is in the list, this command has no effect. Otherwise, except when testing the POSIX API, a <code>newline</code> modifier that specifies the first newline convention in the list (LF in the above example) is added to any pattern that does not already have a <code>newline</code> modifier. If the newline list is empty, the feature is turned off. This command is present in a number of the standard test input files. </p>
<p> When the POSIX API is being tested there is no way to override the default newline convention, though it is possible to set the newline convention from within the pattern. A warning is given if the <code>posix</code> modifier is used when <code>#newline_default</code> would set a default for the non-POSIX API. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#pattern&nbsp;<wbr>&lt;modifier-list&gt; </p>
<p> This command sets a default modifier list that applies to all subsequent patterns. Modifiers on a pattern can change these settings. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#perltest </p>
<p> The appearance of this line causes all subsequent modifier settings to be checked for compatibility with the <code>perltest.sh</code> script, which is used to confirm that Perl gives the same results as PCRE2. Also, apart from comment lines, none of the other command lines are permitted, because they and many of the modifiers are specific to <code>pcre2test</code>, and should not be used in test files that are also processed by <code>perltest.sh</code>. The <code>#perltest</code> command helps detect tests that are accidentally put in the wrong file. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#pop&nbsp;<wbr>[&lt;modifiers&gt;] </p>
<p> This command is used to manipulate the stack of compiled patterns, as described in the section entitled &quot;Saving and restoring compiled patterns&quot; below. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#save&nbsp;<wbr>&lt;filename&gt; </p>
<p> This command is used to save a set of compiled patterns to a file, as described in the section entitled &quot;Saving and restoring compiled patterns&quot; below. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#subject&nbsp;<wbr>&lt;modifier-list&gt; </p>
<p> This command sets a default modifier list that applies to all subsequent subject lines. Modifiers on a subject line can change these settings.</p>
<h2>MODIFIER SYNTAX</h2>
<p> Modifier lists are used with both pattern and subject lines. Items in a list are separated by commas followed by optional white space. Trailing whitespace in a modifier list is ignored. Some modifiers may be given for both patterns and subject lines, whereas others are valid only for one or the other. Each modifier has a long name, for example &quot;anchored&quot;, and some of them must be followed by an equals sign and a value, for example, &quot;offset=12&quot;. Values cannot contain comma characters, but may contain spaces. Modifiers that do not take values may be preceded by a minus sign to turn off a previous setting. </p>
<p> A few of the more common modifiers can also be specified as single letters, for example &quot;i&quot; for &quot;caseless&quot;. In documentation, following the Perl convention, these are written with a slash (&quot;the /i modifier&quot;) for clarity. Abbreviated modifiers must all be concatenated in the first item of a modifier list. If the first item is not recognized as a long modifier name, it is interpreted as a sequence of these abbreviations. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/abc/ig,newline=cr,jit=3 </p>
<p> This is a pattern line whose modifier list starts with two one-letter modifiers (/i and /g). The lower-case abbreviated modifiers are the same as used in Perl.</p>
<h2>PATTERN SYNTAX</h2>
<p> A pattern line must start with one of the following characters (common symbols, excluding pattern meta-characters): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/&nbsp;<wbr>!&nbsp;<wbr>&quot;&nbsp;<wbr>&#8216;&nbsp;<wbr>`&nbsp;<wbr>&#8211;&nbsp;<wbr>=&nbsp;<wbr>_&nbsp;<wbr>:&nbsp;<wbr>;&nbsp;<wbr>,&nbsp;<wbr>%&nbsp;<wbr>&amp;&nbsp;<wbr>@&nbsp;<wbr>~ </p>
<p> This is interpreted as the pattern&#8217;s delimiter. A regular expression may be continued over several input lines, in which case the newline characters are included within it. It is possible to include the delimiter within the pattern by escaping it with a backslash, for example </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/abc\/def/ </p>
<p> If you do this, the escape and the delimiter form part of the pattern, but since the delimiters are all non-alphanumeric, this does not affect its interpretation. If the terminating delimiter is immediately followed by a backslash, for example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/abc/\ </p>
<p> then a backslash is added to the end of the pattern. This is done to provide a way of testing the error condition that arises if a pattern finishes with a backslash, because </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/abc\/ </p>
<p> is interpreted as the first line of a pattern that starts with &quot;abc/&quot;, causing pcre2test to read the next line as a continuation of the regular expression. </p>
<p> A pattern can be followed by a modifier list (details below).</p>
<h2>SUBJECT LINE SYNTAX</h2>
<p> Before each subject line is passed to <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code>, leading and trailing white space is removed, and the line is scanned for backslash escapes. The following provide a means of encoding non-printing characters in a visible way: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>alarm&nbsp;<wbr>(BEL,&nbsp;<wbr>)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>backspace&nbsp;<wbr>()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>escape&nbsp;<wbr>(')<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>form feed&nbsp;<wbr>()<br />
&nbsp;<wbr>&nbsp;<wbr>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>newline&nbsp;<wbr>(
)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>carriage return&nbsp;<wbr>()<br />
&nbsp;<wbr>&nbsp;<wbr>	&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tab&nbsp;<wbr>(	)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>vertical tab&nbsp;<wbr>()<br />
&nbsp;<wbr>&nbsp;<wbr>
nn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>octal character&nbsp;<wbr>(up to 3 octal digits);&nbsp;<wbr>always<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a byte unless&nbsp;<wbr>&gt;&nbsp;<wbr>255 in UTF-8 or 16-bit or 32-bit mode<br />
&nbsp;<wbr>&nbsp;<wbr>\o{dd&#8230;}&nbsp;<wbr>&nbsp;<wbr>octal character&nbsp;<wbr>(any number of octal digits}<br />
&nbsp;<wbr>&nbsp;<wbr>
