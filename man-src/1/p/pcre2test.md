---

title: "pcre2test(1)"
name: "pcre2test"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcre2test/"
description: "pcre2test – a program for testing Perl-compatible regular expressions."
---

<h2>NAME</h2>
<p> pcre2test - a program for testing Perl-compatible regular expressions.  </p>
<p> <code>pcre2test [options] [input file [output file]]</code> </p>
<p> <code>pcre2test</code> is a test program for the PCRE2 regular expression libraries, but it can also be used for experimenting with regular expressions. This document describes the features of the test program; for details of the regular expressions themselves, see the <code>pcre2pattern</code> documentation. For details of the PCRE2 library function calls and their options, see the <code>pcre2api</code> documentation. </p>
<p> The input for <code>pcre2test</code> is a sequence of regular expression patterns and subject strings to be matched. There are also command lines for setting defaults and controlling some special actions. The output shows the result of each match attempt. Modifiers on external or internal command lines, the patterns, and the subject lines specify PCRE2 function options, control how the subject is processed, and what output is produced. </p>
<p> As the original fairly simple PCRE library evolved, it acquired many different features, and as a result, the original <code>pcretest</code> program ended up with a lot of options in a messy, arcane syntax, for testing all the features. The move to the new PCRE2 API provided an opportunity to re-implement the test program as <code>pcre2test</code>, with a cleaner modifier syntax. Nevertheless, there are still many obscure modifiers, some of which are specifically designed for use in conjunction with the test script and data files that are distributed as part of PCRE2. All the modifiers are documented here, some without much justification, but many of them are unlikely to be of use except when testing the libraries.  </p>
<h2>PCRE2's 8-BIT, 16-BIT AND 32-BIT LIBRARIES</h2>
<p> Different versions of the PCRE2 library can be built to support character strings that are encoded in 8-bit, 16-bit, or 32-bit code units. One, two, or all three of these libraries may be simultaneously installed. The <code>pcre2test</code> program can be used to test all the libraries. However, its own input and output are always in 8-bit format. When testing the 16-bit or 32-bit libraries, patterns and subject strings are converted to 16- or 32-bit format before being passed to the library functions. Results are converted back to 8-bit code units for output. </p>
<p> In the rest of this document, the names of library functions and structures are given in generic form, for example, <code>pcre_compile()</code>. The actual names used in the libraries have a suffix _8, _16, or _32, as appropriate.  </p>
<h2>INPUT ENCODING</h2>
<p> Input to <code>pcre2test</code> is processed line by line, either by calling the C library&#8217;s <code>fgets()</code> function, or via the <code>libreadline</code> library (see below). The input is processed using using C&#8217;s string functions, so must not contain binary zeroes, even though in Unix-like environments, <code>fgets()</code> treats any bytes other than newline as data characters. In some Windows environments character 26 (hex 1A) causes an immediate end of file, and no further data is read. </p>
<p> For maximum portability, therefore, it is safest to avoid non-printing characters in <code>pcre2test</code> input files. There is a facility for specifying a pattern&#8217;s characters as hexadecimal pairs, thus making it possible to include binary zeroes in a pattern for testing purposes. Subject lines are processed for backslash escapes, which makes it possible to include any data value.  </p>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt><code>-8</code></dt>
<dd> <p> If the 8-bit library has been built, this option causes it to be used (this is the default). If the 8-bit library has not been built, this option causes an error. </p>
 </dd>
<dt><code>-16</code></dt>
<dd> <p> If the 16-bit library has been built, this option causes it to be used. If only the 16-bit library has been built, this is the default. If the 16-bit library has not been built, this option causes an error. </p>
 </dd>
<dt><code>-32</code></dt>
<dd> <p> If the 32-bit library has been built, this option causes it to be used. If only the 32-bit library has been built, this is the default. If the 32-bit library has not been built, this option causes an error. </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> Behave as if each pattern has the <code>/fullbincode</code> modifier; the full internal binary form of the pattern is output after compilation. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> Output the version number of the PCRE2 library, and all available information about the optional features that are included, and then exit with zero exit code. All other options are ignored. </p>
 </dd>
<dt><code>-C</code><i>option</i></dt>
<dd> <p> Output information about a specific build-time option, then exit. This functionality is intended for use in scripts such as <code>RunTest</code>. The following options output the value and set the exit code as indicated: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>ebcdic-nl&nbsp;<wbr>&nbsp;<wbr>the code for LF&nbsp;<wbr>(=&nbsp;<wbr>NL)&nbsp;<wbr>in an EBCDIC environment: <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x15 or 0x25 <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 if used in an ASCII environment <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit code is always 0 <br />
&nbsp;<wbr>&nbsp;<wbr>linksize&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the configured internal link size&nbsp;<wbr>(2, 3, or 4) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit code is set to the link size <br />
&nbsp;<wbr>&nbsp;<wbr>newline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the default newline setting: <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CR, LF, CRLF, ANYCRLF, or ANY <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit code is always 0 <br />
&nbsp;<wbr>&nbsp;<wbr>bsr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the default setting for what&nbsp;<wbr>\R matches: <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ANYCRLF or ANY <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit code is always 0 </p>
<p> The following options output 1 for true or 0 for false, and set the exit code to the same value: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>backslash-C&nbsp;<wbr>&nbsp;<wbr>\C is supported&nbsp;<wbr>(not locked out) <br />
&nbsp;<wbr>&nbsp;<wbr>ebcdic&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compiled for an EBCDIC environment <br />
&nbsp;<wbr>&nbsp;<wbr>jit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>just-in-time support is available <br />
&nbsp;<wbr>&nbsp;<wbr>pcre2-16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 16-bit library was built <br />
&nbsp;<wbr>&nbsp;<wbr>pcre2-32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 32-bit library was built <br />
&nbsp;<wbr>&nbsp;<wbr>pcre2-8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the 8-bit library was built <br />
&nbsp;<wbr>&nbsp;<wbr>unicode&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Unicode support is available </p>
<p> If an unknown option is given, an error message is output; the exit code is 0. </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> Behave as if each pattern has the <code>debug</code> modifier; the internal form and information about the compiled pattern is output after compilation; <code>-d</code> is equivalent to <code>-b -i</code>. </p>
 </dd>
<dt><code>-dfa</code></dt>
<dd> <p> Behave as if each subject line has the <code>dfa</code> modifier; matching is done using the <code>pcre2_dfa_match()</code> function instead of the default <code>pcre2_match()</code>. </p>
 </dd>
<dt><code>-help</code></dt>
<dd> <p> Output a brief summary these options and then exit. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> Behave as if each pattern has the <code>/info</code> modifier; information about the compiled pattern is given after compilation. </p>
 </dd>
<dt><code>-jit</code></dt>
<dd> <p> Behave as if each pattern line has the <code>jit</code> modifier; after successful compilation, each pattern is passed to the just-in-time compiler, if available. </p>
 </dd>
<dt><code>-pattern </code><i>modifier-list</i></dt>
<dd> <p> Behave as if each pattern line contains the given modifiers. </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> Do not output the version number of <code>pcre2test</code> at the start of execution. </p>
 </dd>
<dt><code>-S</code><i>size</i></dt>
<dd> <p> On Unix-like systems, set the size of the run-time stack to <i>size</i> megabytes. </p>
 </dd>
<dt><code>-subject</code><i>modifier-list</i></dt>
<dd> <p> Behave as if each subject line contains the given modifiers. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Run each compile and match many times with a timer, and output the resulting times per compile or match. When JIT is used, separate times are given for the initial compile and the JIT compile. You can control the number of iterations that are used for timing by following <code>-t</code> with a number (as a separate item on the command line). For example, &quot;-t 1000&quot; iterates 1000 times. The default is to iterate 500,000 times. </p>
 </dd>
<dt><code>-tm</code></dt>
<dd> <p> This is like <code>-t</code> except that it times only the matching phase, not the compile phase. </p>
 </dd>
<dt><code>-T</code><code>-TM</code></dt>
<dd> <p> These behave like <code>-t</code> and <code>-tm</code>, but in addition, at the end of a run, the total times for all compiles and matches are output. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Output the PCRE2 version number and then exit. </p>
 </dd></dl>
<p> If <code>pcre2test</code> is given two filename arguments, it reads from the first and writes to the second. If the first name is &quot;-&quot;, input is taken from the standard input. If <code>pcre2test</code> is given only one argument, it reads from that file and writes to stdout. Otherwise, it reads from stdin and writes to stdout. </p>
<p> When <code>pcre2test</code> is built, a configuration option can specify that it should be linked with the <code>libreadline</code> or <code>libedit</code> library. When this is done, if the input is from a terminal, it is read using the <code>readline()</code> function. This provides line-editing and history facilities. The output from the <code>-help</code> option states whether or not <code>readline()</code> will be used. </p>
<p> The program handles any number of tests, each of which consists of a set of input lines. Each set starts with a regular expression pattern, followed by any number of subject lines to be matched against that pattern. In between sets of test data, command lines that begin with # may appear. This file format, with some restrictions, can also be processed by the <code>perltest.sh</code> script that is distributed with PCRE2 as a means of checking that the behaviour of PCRE2 and Perl is the same. </p>
<p> When the input is a terminal, <code>pcre2test</code> prompts for each line of input, using &quot;re&gt;&quot; to prompt for regular expression patterns, and &quot;data&gt;&quot; to prompt for subject lines. Command lines starting with # can be entered only in response to the &quot;re&gt;&quot; prompt. </p>
<p> Each subject line is matched separately and independently. If you want to do multi-line matches, you have to use the \n escape sequence (or \r or \r\n, etc., depending on the newline setting) in a single line of input to encode the newline sequences. There is no limit on the length of subject lines; the input buffer is automatically extended if it is too small. There are replication features that makes it possible to generate long repetitive pattern or subject lines without having to supply them explicitly. </p>
<p> An empty line or the end of the file signals the end of the subject lines for a test, at which point a new pattern or command line is expected if there is still input to be read.  </p>
<h2>COMMAND LINES</h2>
<p> In between sets of test data, a line that begins with # is interpreted as a command line. If the first character is followed by white space or an exclamation mark, the line is treated as a comment, and ignored. Otherwise, the following commands are recognized: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#forbid_utf </p>
<p> Subsequent patterns automatically have the PCRE2_NEVER_UTF and PCRE2_NEVER_UCP options set, which locks out the use of the PCRE2_UTF and PCRE2_UCP options and the use of (*UTF) and (*UCP) at the start of patterns. This command also forces an error if a subsequent pattern contains any occurrences of \P, \p, or \X, which are still supported when PCRE2_UTF is not set, but which require Unicode property support to be included in the library. </p>
<p> This is a trigger guard that is used in test files to ensure that UTF or Unicode property tests are not accidentally added to files that are used when Unicode support is not included in the library. Setting PCRE2_NEVER_UTF and PCRE2_NEVER_UCP as a default can also be obtained by the use of <code>#pattern</code>; the difference is that <code>#forbid_utf</code> cannot be unset, and the automatic options are not displayed in pattern information, to avoid cluttering up test output. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#load&nbsp;<wbr>&lt;filename&gt; </p>
<p> This command is used to load a set of precompiled patterns from a file, as described in the section entitled &quot;Saving and restoring compiled patterns&quot; below. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#newline_default&nbsp;<wbr>[&lt;newline-list&gt;] </p>
<p> When PCRE2 is built, a default newline convention can be specified. This determines which characters and/or character pairs are recognized as indicating a newline in a pattern or subject string. The default can be overridden when a pattern is compiled. The standard test files contain tests of various newline conventions, but the majority of the tests expect a single linefeed to be recognized as a newline by default. Without special action the tests would fail when PCRE2 is compiled with either CR or CRLF as the default newline. </p>
<p> The #newline_default command specifies a list of newline types that are acceptable as the default. The types must be one of CR, LF, CRLF, ANYCRLF, or ANY (in upper or lower case), for example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#newline_default LF Any anyCRLF </p>
<p> If the default newline is in the list, this command has no effect. Otherwise, except when testing the POSIX API, a <code>newline</code> modifier that specifies the first newline convention in the list (LF in the above example) is added to any pattern that does not already have a <code>newline</code> modifier. If the newline list is empty, the feature is turned off. This command is present in a number of the standard test input files. </p>
<p> When the POSIX API is being tested there is no way to override the default newline convention, though it is possible to set the newline convention from within the pattern. A warning is given if the <code>posix</code> modifier is used when <code>#newline_default</code> would set a default for the non-POSIX API. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#pattern&nbsp;<wbr>&lt;modifier-list&gt; </p>
<p> This command sets a default modifier list that applies to all subsequent patterns. Modifiers on a pattern can change these settings. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#perltest </p>
<p> The appearance of this line causes all subsequent modifier settings to be checked for compatibility with the <code>perltest.sh</code> script, which is used to confirm that Perl gives the same results as PCRE2. Also, apart from comment lines, none of the other command lines are permitted, because they and many of the modifiers are specific to <code>pcre2test</code>, and should not be used in test files that are also processed by <code>perltest.sh</code>. The <code>#perltest</code> command helps detect tests that are accidentally put in the wrong file. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#pop&nbsp;<wbr>[&lt;modifiers&gt;] </p>
<p> This command is used to manipulate the stack of compiled patterns, as described in the section entitled &quot;Saving and restoring compiled patterns&quot; below. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#save&nbsp;<wbr>&lt;filename&gt; </p>
<p> This command is used to save a set of compiled patterns to a file, as described in the section entitled &quot;Saving and restoring compiled patterns&quot; below. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#subject&nbsp;<wbr>&lt;modifier-list&gt; </p>
<p> This command sets a default modifier list that applies to all subsequent subject lines. Modifiers on a subject line can change these settings.  </p>
<h2>MODIFIER SYNTAX</h2>
<p> Modifier lists are used with both pattern and subject lines. Items in a list are separated by commas followed by optional white space. Trailing whitespace in a modifier list is ignored. Some modifiers may be given for both patterns and subject lines, whereas others are valid only for one or the other. Each modifier has a long name, for example &quot;anchored&quot;, and some of them must be followed by an equals sign and a value, for example, &quot;offset=12&quot;. Values cannot contain comma characters, but may contain spaces. Modifiers that do not take values may be preceded by a minus sign to turn off a previous setting. </p>
<p> A few of the more common modifiers can also be specified as single letters, for example &quot;i&quot; for &quot;caseless&quot;. In documentation, following the Perl convention, these are written with a slash (&quot;the /i modifier&quot;) for clarity. Abbreviated modifiers must all be concatenated in the first item of a modifier list. If the first item is not recognized as a long modifier name, it is interpreted as a sequence of these abbreviations. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc/ig,newline=cr,jit=3 </p>
<p> This is a pattern line whose modifier list starts with two one-letter modifiers (/i and /g). The lower-case abbreviated modifiers are the same as used in Perl.  </p>
<h2>PATTERN SYNTAX</h2>
<p> A pattern line must start with one of the following characters (common symbols, excluding pattern meta-characters): </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/&nbsp;<wbr>!&nbsp;<wbr>&quot;&nbsp;<wbr>&#8216;&nbsp;<wbr>`&nbsp;<wbr>-&nbsp;<wbr>=&nbsp;<wbr>_&nbsp;<wbr>:&nbsp;<wbr>;&nbsp;<wbr>,&nbsp;<wbr>%&nbsp;<wbr>&amp;&nbsp;<wbr>@&nbsp;<wbr>~ </p>
<p> This is interpreted as the pattern&#8217;s delimiter. A regular expression may be continued over several input lines, in which case the newline characters are included within it. It is possible to include the delimiter within the pattern by escaping it with a backslash, for example </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc\/def/ </p>
<p> If you do this, the escape and the delimiter form part of the pattern, but since the delimiters are all non-alphanumeric, this does not affect its interpretation. If the terminating delimiter is immediately followed by a backslash, for example, </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc/\ </p>
<p> then a backslash is added to the end of the pattern. This is done to provide a way of testing the error condition that arises if a pattern finishes with a backslash, because </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc\/ </p>
<p> is interpreted as the first line of a pattern that starts with &quot;abc/&quot;, causing pcre2test to read the next line as a continuation of the regular expression. </p>
<p> A pattern can be followed by a modifier list (details below).  </p>
<h2>SUBJECT LINE SYNTAX</h2>
<p> Before each subject line is passed to <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code>, leading and trailing white space is removed, and the line is scanned for backslash escapes. The following provide a means of encoding non-printing characters in a visible way: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>\a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>alarm&nbsp;<wbr>(BEL,&nbsp;<wbr>\x07) <br />
&nbsp;<wbr>&nbsp;<wbr>\b&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>backspace&nbsp;<wbr>(\x08) <br />
&nbsp;<wbr>&nbsp;<wbr>\e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>escape&nbsp;<wbr>(\x27) <br />
&nbsp;<wbr>&nbsp;<wbr>\f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>form feed&nbsp;<wbr>(\x0c) <br />
&nbsp;<wbr>&nbsp;<wbr>\n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>newline&nbsp;<wbr>(\x0a) <br />
&nbsp;<wbr>&nbsp;<wbr>\r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>carriage return&nbsp;<wbr>(\x0d) <br />
&nbsp;<wbr>&nbsp;<wbr>\t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tab&nbsp;<wbr>(\x09) <br />
&nbsp;<wbr>&nbsp;<wbr>\v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>vertical tab&nbsp;<wbr>(\x0b) <br />
&nbsp;<wbr>&nbsp;<wbr>\nnn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>octal character&nbsp;<wbr>(up to 3 octal digits);&nbsp;<wbr>always <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a byte unless&nbsp;<wbr>&gt;&nbsp;<wbr>255 in UTF-8 or 16-bit or 32-bit mode <br />
&nbsp;<wbr>&nbsp;<wbr>\o{dd...}&nbsp;<wbr>&nbsp;<wbr>octal character&nbsp;<wbr>(any number of octal digits} <br />
&nbsp;<wbr>&nbsp;<wbr>\xhh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hexadecimal byte&nbsp;<wbr>(up to 2 hex digits) <br />
&nbsp;<wbr>&nbsp;<wbr>\x{hh...}&nbsp;<wbr>&nbsp;<wbr>hexadecimal character&nbsp;<wbr>(any number of hex digits) </p>
<p> The use of \x{hh...} is not dependent on the use of the <code>utf</code> modifier on the pattern. It is recognized always. There may be any number of hexadecimal digits inside the braces; invalid values provoke error messages. </p>
<p> Note that \xhh specifies one byte rather than one character in UTF-8 mode; this makes it possible to construct invalid UTF-8 sequences for testing purposes. On the other hand, \x{hh} is interpreted as a UTF-8 character in UTF-8 mode, generating more than one byte if the value is greater than 127. When testing the 8-bit library not in UTF-8 mode, \x{hh} generates one byte for values less than 256, and causes an error for greater values. </p>
<p> In UTF-16 mode, all 4-digit \x{hhhh} values are accepted. This makes it possible to construct invalid UTF-16 sequences for testing purposes. </p>
<p> In UTF-32 mode, all 4- to 8-digit \x{...} values are accepted. This makes it possible to construct invalid UTF-32 sequences for testing purposes. </p>
<p> There is a special backslash sequence that specifies replication of one or more characters: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>\[&lt;characters&gt;]{&lt;count&gt;} </p>
<p> This makes it possible to test long strings without having to provide them as part of the file. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>\[abc]{4} </p>
<p> is converted to &quot;abcabcabcabc&quot;. This feature does not support nesting. To include a closing square bracket in the characters, code it as \x5D. </p>
<p> A backslash followed by an equals sign marks the end of the subject string and the start of a modifier list. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>abc\=notbol,notempty </p>
<p> If the subject string is empty and \= is followed by whitespace, the line is treated as a comment line, and is not used for matching. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>\=&nbsp;<wbr>This is a comment. <br />
&nbsp;<wbr>&nbsp;<wbr>abc\=&nbsp;<wbr>This is an invalid modifier list. </p>
<p> A backslash followed by any other non-alphanumeric character just escapes that character. A backslash followed by anything else causes an error. However, if the very last character in the line is a backslash (and there is no modifier list), it is ignored. This gives a way of passing an empty line as data, since a real empty line terminates the data input.  </p>
<h2>PATTERN MODIFIERS</h2>
<p> There are several types of modifier that can appear in pattern lines. Except where noted below, they may also be used in <code>#pattern</code> commands. A pattern&#8217;s modifier list can add to or override default modifiers that were set by a previous <code>#pattern</code> command.  </p>
<h3>Setting compilation options</h3>
<p> The following modifiers set options for <code>pcre2_compile()</code>. The most common ones have single-letter abbreviations. See <code>pcre2api</code> for a description of their effects. </p>
<p> <br />
allow_empty_class&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_ALLOW_EMPTY_CLASS <br />
alt_bsux&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_ALT_BSUX <br />
alt_circumflex&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_ALT_CIRCUMFLEX <br />
alt_verbnames&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_ALT_VERBNAMES <br />
anchored&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_ANCHORED <br />
auto_callout&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_AUTO_CALLOUT <br />
&nbsp;<wbr>&nbsp;<wbr>/i&nbsp;<wbr>&nbsp;<wbr>caseless&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_CASELESS <br />
dollar_endonly&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_DOLLAR_ENDONLY <br />
&nbsp;<wbr>&nbsp;<wbr>/s&nbsp;<wbr>&nbsp;<wbr>dotall&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_DOTALL <br />
dupnames&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_DUPNAMES <br />
&nbsp;<wbr>&nbsp;<wbr>/x&nbsp;<wbr>&nbsp;<wbr>extended&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_EXTENDED <br />
firstline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_FIRSTLINE <br />
match_unset_backref&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_MATCH_UNSET_BACKREF <br />
&nbsp;<wbr>&nbsp;<wbr>/m&nbsp;<wbr>&nbsp;<wbr>multiline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_MULTILINE <br />
never_backslash_c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NEVER_BACKSLASH_C <br />
never_ucp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NEVER_UCP <br />
never_utf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NEVER_UTF <br />
no_auto_capture&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NO_AUTO_CAPTURE <br />
no_auto_possess&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NO_AUTO_POSSESS <br />
no_dotstar_anchor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NO_DOTSTAR_ANCHOR <br />
no_start_optimize&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NO_START_OPTIMIZE <br />
no_utf_check&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NO_UTF_CHECK <br />
ucp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_UCP <br />
ungreedy&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_UNGREEDY <br />
use_offset_limit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_USE_OFFSET_LIMIT <br />
utf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_UTF </p>
<p> As well as turning on the PCRE2_UTF option, the <code>utf</code> modifier causes all non-printing characters in output strings to be printed using the \x{hh...} notation. Otherwise, those less than 0x100 are output in hex without the curly brackets.  </p>
<h3>Setting compilation controls</h3>
<p> The following modifiers affect the compilation process or request information about the pattern: </p>
<p> <br />
bsr=[anycrlf|unicode]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify&nbsp;<wbr>\R handling <br />
&nbsp;<wbr>&nbsp;<wbr>/B&nbsp;<wbr>&nbsp;<wbr>bincode&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show binary code without lengths <br />
callout_info&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show callout information <br />
debug&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>same as info,fullbincode <br />
fullbincode&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show binary code with lengths <br />
&nbsp;<wbr>&nbsp;<wbr>/I&nbsp;<wbr>&nbsp;<wbr>info&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show info about compiled pattern <br />
hex&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pattern is coded in hexadecimal <br />
jit[=&lt;number&gt;]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use JIT <br />
jitfast&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use JIT fast path <br />
jitverify&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>verify JIT use <br />
locale=&lt;name&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use this locale <br />
max_pattern_length=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set the maximum pattern length <br />
memory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show memory used <br />
newline=&lt;type&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set newline type <br />
null_context&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compile with a NULL context <br />
parens_nest_limit=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set maximum parentheses depth <br />
posix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the POSIX API <br />
push&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>push compiled pattern onto the stack <br />
stackguard=&lt;number&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>test the stackguard feature <br />
tables=[0|1|2]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>select internal tables </p>
<p> The effects of these modifiers are described in the following sections.  </p>
<h3>Newline and \R handling</h3>
<p> The <code>bsr</code> modifier specifies what \R in a pattern should match. If it is set to &quot;anycrlf&quot;, \R matches CR, LF, or CRLF only. If it is set to &quot;unicode&quot;, \R matches any Unicode newline sequence. The default is specified when PCRE2 is built, with the default default being Unicode. </p>
<p> The <code>newline</code> modifier specifies which characters are to be interpreted as newlines, both in the pattern and in subject lines. The type must be one of CR, LF, CRLF, ANYCRLF, or ANY (in upper or lower case).  </p>
<h3>Information about a pattern</h3>
<p> The <code>debug</code> modifier is a shorthand for <code>info,fullbincode</code>, requesting all available information. </p>
<p> The <code>bincode</code> modifier causes a representation of the compiled code to be output after compilation. This information does not contain length and offset values, which ensures that the same output is generated for different internal link sizes and different code unit widths. By using <code>bincode</code>, the same regression tests can be used in different environments. </p>
<p> The <code>fullbincode</code> modifier, by contrast, <i>does</i> include length and offset values. This is used in a few special tests that run only for specific code unit widths and link sizes, and is also useful for one-off tests. </p>
<p> The <code>info</code> modifier requests information about the compiled pattern (whether it is anchored, has a fixed first character, and so on). The information is obtained from the <code>pcre2_pattern_info()</code> function. Here are some typical examples: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(?i)(^a|^b)/m,info <br />
&nbsp;<wbr>&nbsp;<wbr>Capturing subpattern count&nbsp;<wbr>=&nbsp;<wbr>1 <br />
&nbsp;<wbr>&nbsp;<wbr>Compile options: multiline <br />
&nbsp;<wbr>&nbsp;<wbr>Overall options: caseless multiline <br />
&nbsp;<wbr>&nbsp;<wbr>First code unit at start or follows newline <br />
&nbsp;<wbr>&nbsp;<wbr>Subject length lower bound&nbsp;<wbr>=&nbsp;<wbr>1 </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(?i)abc/info <br />
&nbsp;<wbr>&nbsp;<wbr>Capturing subpattern count&nbsp;<wbr>=&nbsp;<wbr>0 <br />
&nbsp;<wbr>&nbsp;<wbr>Compile options:&nbsp;<wbr>&lt;none&gt; <br />
&nbsp;<wbr>&nbsp;<wbr>Overall options: caseless <br />
&nbsp;<wbr>&nbsp;<wbr>First code unit&nbsp;<wbr>=&nbsp;<wbr>&#8216;a&#8217;&nbsp;<wbr>(caseless) <br />
&nbsp;<wbr>&nbsp;<wbr>Last code unit&nbsp;<wbr>=&nbsp;<wbr>&#8216;c&#8217;&nbsp;<wbr>(caseless) <br />
&nbsp;<wbr>&nbsp;<wbr>Subject length lower bound&nbsp;<wbr>=&nbsp;<wbr>3 </p>
<p> &quot;Compile options&quot; are those specified by modifiers; &quot;overall options&quot; have added options that are taken or deduced from the pattern. If both sets of options are the same, just a single &quot;options&quot; line is output; if there are no options, the line is omitted. &quot;First code unit&quot; is where any match must start; if there is more than one they are listed as &quot;starting code units&quot;. &quot;Last code unit&quot; is the last literal code unit that must be present in any match. This is not necessarily the last character. These lines are omitted if no starting or ending code units are recorded. </p>
<p> The <code>callout_info</code> modifier requests information about all the callouts in the pattern. A list of them is output at the end of any other information that is requested. For each callout, either its number or string is given, followed by the item that follows it in the pattern.  </p>
<h3>Passing a NULL context</h3>
<p> Normally, <code>pcre2test</code> passes a context block to <code>pcre2_compile()</code>. If the <code>null_context</code> modifier is set, however, NULL is passed. This is for testing that <code>pcre2_compile()</code> behaves correctly in this case (it uses default values).  </p>
<h3>Specifying a pattern in hex</h3>
<p> The <code>hex</code> modifier specifies that the characters of the pattern are to be interpreted as pairs of hexadecimal digits. White space is permitted between pairs. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/ab 32 59/hex </p>
<p> This feature is provided as a way of creating patterns that contain binary zero and other non-printing characters. By default, <code>pcre2test</code> passes patterns as zero-terminated strings to <code>pcre2_compile()</code>, giving the length as PCRE2_ZERO_TERMINATED. However, for patterns specified in hexadecimal, the actual length of the pattern is passed.  </p>
<h3>Generating long repetitive patterns</h3>
<p> Some tests use long patterns that are very repetitive. Instead of creating a very long input line for such a pattern, you can use a special repetition feature, similar to the one described for subject lines above. If the <code>expand</code> modifier is present on a pattern, parts of the pattern that have the form </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>\[&lt;characters&gt;]{&lt;count&gt;} </p>
<p> are expanded before the pattern is passed to <code>pcre2_compile()</code>. For example, \[AB]{6000} is expanded to &quot;ABAB...&quot; 6000 times. This construction cannot be nested. An initial &quot;\[&quot; sequence is recognized only if &quot;]{&quot; followed by decimal digits and &quot;}&quot; is found later in the pattern. If not, the characters remain in the pattern unaltered. </p>
<p> If part of an expanded pattern looks like an expansion, but is really part of the actual pattern, unwanted expansion can be avoided by giving two values in the quantifier. For example, \[AB]{6000,6000} is not recognized as an expansion item. </p>
<p> If the <code>info</code> modifier is set on an expanded pattern, the result of the expansion is included in the information that is output.  </p>
<h3>JIT compilation</h3>
<p> Just-in-time (JIT) compiling is a heavyweight optimization that can greatly speed up pattern matching. See the <code>pcre2jit</code> documentation for details. JIT compiling happens, optionally, after a pattern has been successfully compiled into an internal form. The JIT compiler converts this to optimized machine code. It needs to know whether the match-time options PCRE2_PARTIAL_HARD and PCRE2_PARTIAL_SOFT are going to be used, because different code is generated for the different cases. See the <code>partial</code> modifier in &quot;Subject Modifiers&quot; below for details of how these options are specified for each match attempt. </p>
<p> JIT compilation is requested by the <code>/jit</code> pattern modifier, which may optionally be followed by an equals sign and a number in the range 0 to 7. The three bits that make up the number specify which of the three JIT operating modes are to be compiled: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>compile JIT code for non-partial matching <br />
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>compile JIT code for soft partial matching <br />
&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>compile JIT code for hard partial matching </p>
<p> The possible values for the <code>/jit</code> modifier are therefore: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>disable JIT <br />
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>normal matching only <br />
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>soft partial matching only <br />
&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>normal and soft partial matching <br />
&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>hard partial matching only <br />
&nbsp;<wbr>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>soft and hard partial matching only <br />
&nbsp;<wbr>&nbsp;<wbr>7&nbsp;<wbr>&nbsp;<wbr>all three modes </p>
<p> If no number is given, 7 is assumed. The phrase &quot;partial matching&quot; means a call to <code>pcre2_match()</code> with either the PCRE2_PARTIAL_SOFT or the PCRE2_PARTIAL_HARD option set. Note that such a call may return a complete match; the options enable the possibility of a partial match, but do not require it. Note also that if you request JIT compilation only for partial matching (for example, /jit=2) but do not set the <code>partial</code> modifier on a subject line, that match will not use JIT code because none was compiled for non-partial matching. </p>
<p> If JIT compilation is successful, the compiled JIT code will automatically be used when an appropriate type of match is run, except when incompatible run-time options are specified. For more details, see the <code>pcre2jit</code> documentation. See also the <code>jitstack</code> modifier below for a way of setting the size of the JIT stack. </p>
<p> If the <code>jitfast</code> modifier is specified, matching is done using the JIT &quot;fast path&quot; interface, <code>pcre2_jit_match()</code>, which skips some of the sanity checks that are done by <code>pcre2_match()</code>, and of course does not work when JIT is not supported. If <code>jitfast</code> is specified without <code>jit</code>, jit=7 is assumed. </p>
<p> If the <code>jitverify</code> modifier is specified, information about the compiled pattern shows whether JIT compilation was or was not successful. If <code>jitverify</code> is specified without <code>jit</code>, jit=7 is assumed. If JIT compilation is successful when <code>jitverify</code> is set, the text &quot;(JIT)&quot; is added to the first output line after a match or non match when JIT-compiled code was actually used in the match.  </p>
<h3>Setting a locale</h3>
<p> The <code>/locale</code> modifier must specify the name of a locale, for example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/pattern/locale=fr_FR </p>
<p> The given locale is set, <code>pcre2_maketables()</code> is called to build a set of character tables for the locale, and this is then passed to <code>pcre2_compile()</code> when compiling the regular expression. The same tables are used when matching the following subject lines. The <code>/locale</code> modifier applies only to the pattern on which it appears, but can be given in a <code>#pattern</code> command if a default is needed. Setting a locale and alternate character tables are mutually exclusive.  </p>
<h3>Showing pattern memory</h3>
<p> The <code>/memory</code> modifier causes the size in bytes of the memory used to hold the compiled pattern to be output. This does not include the size of the <code>pcre2_code</code> block; it is just the actual compiled data. If the pattern is subsequently passed to the JIT compiler, the size of the JIT compiled code is also output. Here is an example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/a(b)c/jit,memory <br />
&nbsp;<wbr>&nbsp;<wbr>Memory allocation&nbsp;<wbr>(code space): 21 <br />
&nbsp;<wbr>&nbsp;<wbr>Memory allocation&nbsp;<wbr>(JIT code): 1910 </p>
<h3>Limiting nested parentheses</h3>
<p> The <code>parens_nest_limit</code> modifier sets a limit on the depth of nested parentheses in a pattern. Breaching the limit causes a compilation error. The default for the library is set when PCRE2 is built, but <code>pcre2test</code> sets its own default of 220, which is required for running the standard test suite.  </p>
<h3>Limiting the pattern length</h3>
<p> The <code>max_pattern_length</code> modifier sets a limit, in code units, to the length of pattern that <code>pcre2_compile()</code> will accept. Breaching the limit causes a compilation error. The default is the largest number a PCRE2_SIZE variable can hold (essentially unlimited).  </p>
<h3>Using the POSIX wrapper API</h3>
<p> The <code>/posix</code> modifier causes <code>pcre2test</code> to call PCRE2 via the POSIX wrapper API rather than its native API. This supports only the 8-bit library. Note that it does not imply POSIX matching semantics; for more detail see the <code>pcre2posix</code> documentation. When the POSIX API is being used, the following pattern modifiers set options for the <code>regcomp()</code> function: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>caseless&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_ICASE <br />
&nbsp;<wbr>&nbsp;<wbr>multiline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_NEWLINE <br />
&nbsp;<wbr>&nbsp;<wbr>no_auto_capture&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_NOSUB <br />
&nbsp;<wbr>&nbsp;<wbr>dotall&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_DOTALL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>) <br />
&nbsp;<wbr>&nbsp;<wbr>ungreedy&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_UNGREEDY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>These options are not part of <br />
&nbsp;<wbr>&nbsp;<wbr>ucp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_UCP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the POSIX standard <br />
&nbsp;<wbr>&nbsp;<wbr>utf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>REG_UTF8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>) </p>
<p> The <code>regerror_buffsize</code> modifier specifies a size for the error buffer that is passed to <code>regerror()</code> in the event of a compilation error. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc/posix,regerror_buffsize=20 </p>
<p> This provides a means of testing the behaviour of <code>regerror()</code> when the buffer is too small for the error message. If this modifier has not been set, a large buffer is used. </p>
<p> The <code>aftertext</code> and <code>allaftertext</code> subject modifiers work as described below. All other modifiers cause an error.  </p>
<h3>Testing the stack guard feature</h3>
<p> The <code>/stackguard</code> modifier is used to test the use of <code>pcre2_set_compile_recursion_guard()</code>, a function that is provided to enable stack availability to be checked during compilation (see the <code>pcre2api</code> documentation for details). If the number specified by the modifier is greater than zero, <code>pcre2_set_compile_recursion_guard()</code> is called to set up callback from <code>pcre2_compile()</code> to a local function. The argument it receives is the current nesting parenthesis depth; if this is greater than the value given by the modifier, non-zero is returned, causing the compilation to be aborted.  </p>
<h3>Using alternative character tables</h3>
<p> The value specified for the <code>/tables</code> modifier must be one of the digits 0, 1, or 2. It causes a specific set of built-in character tables to be passed to <code>pcre2_compile()</code>. This is used in the PCRE2 tests to check behaviour with different character tables. The digit specifies the tables as follows: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not pass any special character tables <br />
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the default ASCII tables, as distributed in <br />
&nbsp;<wbr>&nbsp;<wbr>pcre2_chartables.c.dist <br />
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a set of tables defining ISO 8859 characters </p>
<p> In table 2, some characters whose codes are greater than 128 are identified as letters, digits, spaces, etc. Setting alternate character tables and a locale are mutually exclusive.  </p>
<h3>Setting certain match controls</h3>
<p> The following modifiers are really subject modifiers, and are described below. However, they may be included in a pattern&#8217;s modifier list, in which case they are applied to every subject line that is processed with that pattern. They may not appear in <code>#pattern</code> commands. These modifiers do not affect the compilation process. </p>
<p> <br />
aftertext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show text after match <br />
allaftertext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show text after captures <br />
allcaptures&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show all captures <br />
allusedtext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show all consulted text <br />
&nbsp;<wbr>&nbsp;<wbr>/g&nbsp;<wbr>&nbsp;<wbr>global&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>global matching <br />
mark&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show mark values <br />
replace=&lt;string&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify a replacement string <br />
startchar&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show starting character when relevant <br />
substitute_extended&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use PCRE2_SUBSTITUTE_EXTENDED <br />
substitute_overflow_length use PCRE2_SUBSTITUTE_OVERFLOW_LENGTH <br />
substitute_unknown_unset&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use PCRE2_SUBSTITUTE_UNKNOWN_UNSET <br />
substitute_unset_empty&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use PCRE2_SUBSTITUTE_UNSET_EMPTY </p>
<p> These modifiers may not appear in a <code>#pattern</code> command. If you want them as defaults, set them in a <code>#subject</code> command.  </p>
<h3>Saving a compiled pattern</h3>
<p> When a pattern with the <code>push</code> modifier is successfully compiled, it is pushed onto a stack of compiled patterns, and <code>pcre2test</code> expects the next line to contain a new pattern (or a command) instead of a subject line. This facility is used when saving compiled patterns to a file, as described in the section entitled &quot;Saving and restoring compiled patterns&quot; below. The <code>push</code> modifier is incompatible with compilation modifiers such as <code>global</code> that act at match time. Any that are specified are ignored, with a warning message, except for <code>replace</code>, which causes an error. Note that, <code>jitverify</code>, which is allowed, does not carry through to any subsequent matching that uses this pattern.  </p>
<h2>SUBJECT MODIFIERS</h2>
<p> The modifiers that can appear in subject lines and the <code>#subject</code> command are of two types.  </p>
<h3>Setting match options</h3>
<p> The following modifiers set options for <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code>. See <code>pcreapi</code> for a description of their effects. </p>
<p> <br />
anchored&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_ANCHORED <br />
dfa_restart&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_DFA_RESTART <br />
dfa_shortest&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_DFA_SHORTEST <br />
no_utf_check&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NO_UTF_CHECK <br />
notbol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NOTBOL <br />
notempty&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NOTEMPTY <br />
notempty_atstart&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NOTEMPTY_ATSTART <br />
noteol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_NOTEOL <br />
partial_hard&nbsp;<wbr>(or ph)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_PARTIAL_HARD <br />
partial_soft&nbsp;<wbr>(or ps)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set PCRE2_PARTIAL_SOFT </p>
<p> The partial matching modifiers are provided with abbreviations because they appear frequently in tests. </p>
<p> If the <code>/posix</code> modifier was present on the pattern, causing the POSIX wrapper API to be used, the only option-setting modifiers that have any effect are <code>notbol</code>, <code>notempty</code>, and <code>noteol</code>, causing REG_NOTBOL, REG_NOTEMPTY, and REG_NOTEOL, respectively, to be passed to <code>regexec()</code>. Any other modifiers cause an error.  </p>
<h3>Setting match controls</h3>
<p> The following modifiers affect the matching process or request additional information. Some of them may also be specified on a pattern line (see above), in which case they apply to every subject line that is matched against that pattern. </p>
<p> <br />
aftertext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show text after match <br />
allaftertext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show text after captures <br />
allcaptures&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show all captures <br />
allusedtext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show all consulted text&nbsp;<wbr>(non-JIT only) <br />
altglobal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>alternative global matching <br />
callout_capture&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show captures at callout time <br />
callout_data=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set a value to pass via callouts <br />
callout_fail=&lt;n&gt;[:&lt;m&gt;]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>control callout failure <br />
callout_none&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not supply a callout function <br />
copy=&lt;number or name&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>copy captured substring <br />
dfa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use&nbsp;<wbr><code>pcre2_dfa_match()</code> <br />
find_limits&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>find match and recursion limits <br />
get=&lt;number or name&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>extract captured substring <br />
getall&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>extract all captured substrings <br />
&nbsp;<wbr>&nbsp;<wbr>/g&nbsp;<wbr>&nbsp;<wbr>global&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>global matching <br />
jitstack=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set size of JIT stack <br />
mark&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show mark values <br />
match_limit=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set a match limit <br />
memory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show memory usage <br />
null_context&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>match with a NULL context <br />
offset=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set starting offset <br />
offset_limit=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set offset limit <br />
ovector=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set size of output vector <br />
recursion_limit=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set a recursion limit <br />
replace=&lt;string&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify a replacement string <br />
startchar&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show startchar when relevant <br />
startoffset=&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>same as offset=&lt;n&gt; <br />
substitute_extedded&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use PCRE2_SUBSTITUTE_EXTENDED <br />
substitute_overflow_length use PCRE2_SUBSTITUTE_OVERFLOW_LENGTH <br />
substitute_unknown_unset&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use PCRE2_SUBSTITUTE_UNKNOWN_UNSET <br />
substitute_unset_empty&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use PCRE2_SUBSTITUTE_UNSET_EMPTY <br />
zero_terminate&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the subject as zero-terminated </p>
<p> The effects of these modifiers are described in the following sections.  </p>
<h3>Showing more text</h3>
<p> The <code>aftertext</code> modifier requests that as well as outputting the part of the subject string that matched the entire pattern, <code>pcre2test</code> should in addition output the remainder of the subject string. This is useful for tests where the subject contains multiple copies of the same substring. The <code>allaftertext</code> modifier requests the same action for captured substrings as well as the main matched substring. In each case the remainder is output on the following line with a plus character following the capture number. </p>
<p> The <code>allusedtext</code> modifier requests that all the text that was consulted during a successful pattern match by the interpreter should be shown. This feature is not supported for JIT matching, and if requested with JIT it is ignored (with a warning message). Setting this modifier affects the output if there is a lookbehind at the start of a match, or a lookahead at the end, or if \K is used in the pattern. Characters that precede or follow the start and end of the actual match are indicated in the output by &#8216;&lt;&#8216; or &#8216;&gt;&#8216; characters underneath them. Here is an example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(?&lt;=pqr)abc(?=xyz)/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>123pqrabcxyz456\=allusedtext <br />
0: pqrabcxyz <br />
&lt;&lt;&lt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&gt;&gt;&gt; </p>
<p> This shows that the matched string is &quot;abc&quot;, with the preceding and following strings &quot;pqr&quot; and &quot;xyz&quot; having been consulted during the match (when processing the assertions). </p>
<p> The <code>startchar</code> modifier requests that the starting character for the match be indicated, if it is different to the start of the matched string. The only time when this occurs is when \K has been processed as part of the match. In this situation, the output for the matched string is displayed from the starting character instead of from the match point, with circumflex characters under the earlier characters. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/abc\Kxyz/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>abcxyz\=startchar <br />
0: abcxyz <br />
^^^ </p>
<p> Unlike <code>allusedtext</code>, the <code>startchar</code> modifier can be used with JIT. However, these two modifiers are mutually exclusive.  </p>
<h3>Showing the value of all capture groups</h3>
<p> The <code>allcaptures</code> modifier requests that the values of all potential captured parentheses be output after a match. By default, only those up to the highest one actually used in the match are output (corresponding to the return code from <code>pcre2_match()</code>). Groups that did not take part in the match are output as &quot;&lt;unset&gt;&quot;.  </p>
<h3>Testing callouts</h3>
<p> A callout function is supplied when <code>pcre2test</code> calls the library matching functions, unless <code>callout_none</code> is specified. If <code>callout_capture</code> is set, the current captured groups are output when a callout occurs. </p>
<p> The <code>callout_fail</code> modifier can be given one or two numbers. If there is only one number, 1 is returned instead of 0 when a callout of that number is reached. If two numbers are given, 1 is returned when callout &lt;n&gt; is reached for the &lt;m&gt;th time. Note that callouts with string arguments are always given the number zero. See &quot;Callouts&quot; below for a description of the output when a callout it taken. </p>
<p> The <code>callout_data</code> modifier can be given an unsigned or a negative number. This is set as the &quot;user data&quot; that is passed to the matching function, and passed back when the callout function is invoked. Any value other than zero is used as a return from <code>pcre2test</code>&#8216;s callout function.  </p>
<h3>Finding all matches in a string</h3>
<p> Searching for all possible matches within a subject can be requested by the <code>global</code> or <code>/altglobal</code> modifier. After finding a match, the matching function is called again to search the remainder of the subject. The difference between <code>global</code> and <code>altglobal</code> is that the former uses the <i>start_offset</i> argument to <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code> to start searching at a new point within the entire string (which is what Perl does), whereas the latter passes over a shortened subject. This makes a difference to the matching process if the pattern begins with a lookbehind assertion (including \b or \B). </p>
<p> If an empty string is matched, the next match is done with the PCRE2_NOTEMPTY_ATSTART and PCRE2_ANCHORED flags set, in order to search for another, non-empty, match at the same point in the subject. If this match fails, the start offset is advanced, and the normal match is retried. This imitates the way Perl handles such cases when using the <code>/g</code> modifier or the <code>split()</code> function. Normally, the start offset is advanced by one character, but if the newline convention recognizes CRLF as a newline, and the current character is CR followed by LF, an advance of two characters occurs.  </p>
<h3>Testing substring extraction functions</h3>
<p> The <code>copy</code> and <code>get</code> modifiers can be used to test the <code>pcre2_substring_copy_xxx()</code> and <code>pcre2_substring_get_xxx()</code> functions. They can be given more than once, and each can specify a group name or number, for example: </p>
<p> <br />
abcd\=copy=1,copy=3,get=G1 </p>
<p> If the <code>#subject</code> command is used to set default copy and/or get lists, these can be unset by specifying a negative number to cancel all numbered groups and an empty name to cancel all named groups. </p>
<p> The <code>getall</code> modifier tests <code>pcre2_substring_list_get()</code>, which extracts all captured substrings. </p>
<p> If the subject line is successfully matched, the substrings extracted by the convenience functions are output with C, G, or L after the string number instead of a colon. This is in addition to the normal full list. The string length (that is, the return from the extraction function) is given in parentheses after each substring, followed by the name when the extraction was by name.  </p>
<h3>Testing the substitution function</h3>
<p> If the <code>replace</code> modifier is set, the <code>pcre2_substitute()</code> function is called instead of one of the matching functions. Note that replacement strings cannot contain commas, because a comma signifies the end of a modifier. This is not thought to be an issue in a test program. </p>
<p> Unlike subject strings, <code>pcre2test</code> does not process replacement strings for escape sequences. In UTF mode, a replacement string is checked to see if it is a valid UTF-8 string. If so, it is correctly converted to a UTF string of the appropriate code unit width. If it is not a valid UTF-8 string, the individual code units are copied directly. This provides a means of passing an invalid UTF-8 string for testing purposes. </p>
<p> The following modifiers set options (in additional to the normal match options) for <code>pcre2_substitute()</code>: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>global&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE2_SUBSTITUTE_GLOBAL <br />
&nbsp;<wbr>&nbsp;<wbr>substitute_extended&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE2_SUBSTITUTE_EXTENDED <br />
&nbsp;<wbr>&nbsp;<wbr>substitute_overflow_length&nbsp;<wbr>&nbsp;<wbr>PCRE2_SUBSTITUTE_OVERFLOW_LENGTH <br />
&nbsp;<wbr>&nbsp;<wbr>substitute_unknown_unset&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE2_SUBSTITUTE_UNKNOWN_UNSET <br />
&nbsp;<wbr>&nbsp;<wbr>substitute_unset_empty&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PCRE2_SUBSTITUTE_UNSET_EMPTY </p>
<p> After a successful substitution, the modified string is output, preceded by the number of replacements. This may be zero if there were no matches. Here is a simple example of a substitution test: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc/replace=xxx <br />
=abc=abc= <br />
1:&nbsp;<wbr>=xxx=abc= <br />
=abc=abc=\=global <br />
2:&nbsp;<wbr>=xxx=xxx= </p>
<p> Subject and replacement strings should be kept relatively short (fewer than 256 characters) for substitution tests, as fixed-size buffers are used. To make it easy to test for buffer overflow, if the replacement string starts with a number in square brackets, that number is passed to <code>pcre2_substitute()</code> as the size of the output buffer, with the replacement string starting at the next character. Here is an example that tests the edge case: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc/ <br />
123abc123\=replace=[10]XYZ <br />
1: 123XYZ123 <br />
123abc123\=replace=[9]XYZ <br />
&nbsp;<wbr>&nbsp;<wbr>Failed: error -47: no more memory </p>
<p> The default action of <code>pcre2_substitute()</code> is to return PCRE2_ERROR_NOMEMORY when the output buffer is too small. However, if the PCRE2_SUBSTITUTE_OVERFLOW_LENGTH option is set (by using the <code>substitute_overflow_length</code> modifier), <code>pcre2_substitute()</code> continues to go through the motions of matching and substituting, in order to compute the size of buffer that is required. When this happens, <code>pcre2test</code> shows the required buffer length (which includes space for the trailing zero) as part of the error message. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc/substitute_overflow_length <br />
123abc123\=replace=[9]XYZ <br />
&nbsp;<wbr>&nbsp;<wbr>Failed: error -47: no more memory: 10 code units are needed </p>
<p> A replacement string is ignored with POSIX and DFA matching. Specifying partial matching provokes an error return (&quot;bad option value&quot;) from <code>pcre2_substitute()</code>.  </p>
<h3>Setting the JIT stack size</h3>
<p> The <code>jitstack</code> modifier provides a way of setting the maximum stack size that is used by the just-in-time optimization code. It is ignored if JIT optimization is not being used. The value is a number of kilobytes. Providing a stack that is larger than the default 32K is necessary only for very complicated patterns.  </p>
<h3>Setting match and recursion limits</h3>
<p> The <code>match_limit</code> and <code>recursion_limit</code> modifiers set the appropriate limits in the match context. These values are ignored when the <code>find_limits</code> modifier is specified.  </p>
<h3>Finding minimum limits</h3>
<p> If the <code>find_limits</code> modifier is present, <code>pcre2test</code> calls <code>pcre2_match()</code> several times, setting different values in the match context via <code>pcre2_set_match_limit()</code> and <code>pcre2_set_recursion_limit()</code> until it finds the minimum values for each parameter that allow <code>pcre2_match()</code> to complete without error. </p>
<p> If JIT is being used, only the match limit is relevant. If DFA matching is being used, neither limit is relevant, and this modifier is ignored (with a warning message). </p>
<p> The <i>match_limit</i> number is a measure of the amount of backtracking that takes place, and learning the minimum value can be instructive. For most simple matches, the number is quite small, but for patterns with very large numbers of matching possibilities, it can become large very quickly with increasing length of subject string. The <i>match_limit_recursion</i> number is a measure of how much stack (or, if PCRE2 is compiled with NO_RECURSE, how much heap) memory is needed to complete the match attempt.  </p>
<h3>Showing MARK names</h3>
<p> The <code>mark</code> modifier causes the names from backtracking control verbs that are returned from calls to <code>pcre2_match()</code> to be displayed. If a mark is returned for a match, non-match, or partial match, <code>pcre2test</code> shows it. For a match, it is on a line by itself, tagged with &quot;MK:&quot;. Otherwise, it is added to the non-match message.  </p>
<h3>Showing memory usage</h3>
<p> The <code>memory</code> modifier causes <code>pcre2test</code> to log all memory allocation and freeing calls that occur during a match operation.  </p>
<h3>Setting a starting offset</h3>
<p> The <code>offset</code> modifier sets an offset in the subject string at which matching starts. Its value is a number of code units, not characters.  </p>
<h3>Setting an offset limit</h3>
<p> The <code>offset_limit</code> modifier sets a limit for unanchored matches. If a match cannot be found starting at or before this offset in the subject, a &quot;no match&quot; return is given. The data value is a number of code units, not characters. When this modifier is used, the <code>use_offset_limit</code> modifier must have been set for the pattern; if not, an error is generated.  </p>
<h3>Setting the size of the output vector</h3>
<p> The <code>ovector</code> modifier applies only to the subject line in which it appears, though of course it can also be used to set a default in a <code>#subject</code> command. It specifies the number of pairs of offsets that are available for storing matching information. The default is 15. </p>
<p> A value of zero is useful when testing the POSIX API because it causes <code>regexec()</code> to be called with a NULL capture vector. When not testing the POSIX API, a value of zero is used to cause <code>pcre2_match_data_create_from_pattern()</code> to be called, in order to create a match block of exactly the right size for the pattern. (It is not possible to create a match block with a zero-length ovector; there is always at least one pair of offsets.)  </p>
<h3>Passing the subject as zero-terminated</h3>
<p> By default, the subject string is passed to a native API matching function with its correct length. In order to test the facility for passing a zero-terminated string, the <code>zero_terminate</code> modifier is provided. It causes the length to be passed as PCRE2_ZERO_TERMINATED. (When matching via the POSIX interface, this modifier has no effect, as there is no facility for passing a length.) </p>
<p> When testing <code>pcre2_substitute()</code>, this modifier also has the effect of passing the replacement string as zero-terminated.  </p>
<h3>Passing a NULL context</h3>
<p> Normally, <code>pcre2test</code> passes a context block to <code>pcre2_match()</code>, <code>pcre2_dfa_match()</code> or <code>pcre2_jit_match()</code>. If the <code>null_context</code> modifier is set, however, NULL is passed. This is for testing that the matching functions behave correctly in this case (they use default values). This modifier cannot be used with the <code>find_limits</code> modifier or when testing the substitution function.  </p>
<h2>THE ALTERNATIVE MATCHING FUNCTION</h2>
<p> By default, <code>pcre2test</code> uses the standard PCRE2 matching function, <code>pcre2_match()</code> to match each subject line. PCRE2 also supports an alternative matching function, <code>pcre2_dfa_match()</code>, which operates in a different way, and has some restrictions. The differences between the two functions are described in the <code>pcre2matching</code> documentation. </p>
<p> If the <code>dfa</code> modifier is set, the alternative matching function is used. This function finds all possible matches at a given point in the subject. If, however, the <code>dfa_shortest</code> modifier is set, processing stops after the first match is found. This is always the shortest possible match.  </p>
<h2>DEFAULT OUTPUT FROM pcre2test</h2>
<p> This section describes the output when the normal matching function, <code>pcre2_match()</code>, is being used. </p>
<p> When a match succeeds, <code>pcre2test</code> outputs the list of captured substrings, starting with number 0 for the string that matched the whole pattern. Otherwise, it outputs &quot;No match&quot; when the return is PCRE2_ERROR_NOMATCH, or &quot;Partial match:&quot; followed by the partially matching substring when the return is PCRE2_ERROR_PARTIAL. (Note that this is the entire substring that was inspected during the partial match; it may include characters before the actual match start if a lookbehind assertion, \K, \b, or \B was involved.) </p>
<p> For any other return, <code>pcre2test</code> outputs the PCRE2 negative error number and a short descriptive phrase. If the error is a failed UTF string check, the code unit offset of the start of the failing character is also output. Here is an example of an interactive <code>pcre2test</code> run. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>pcre2test <br />
&nbsp;<wbr>&nbsp;<wbr>PCRE2 version 9.00 2014-05-10 </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/^abc(\d+)/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>abc123 <br />
0: abc123 <br />
1: 123 <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>xyz <br />
&nbsp;<wbr>&nbsp;<wbr>No match </p>
<p> Unset capturing substrings that are not followed by one that is set are not shown by <code>pcre2test</code> unless the <code>allcaptures</code> modifier is specified. In the following example, there are two capturing substrings, but when the first data line is matched, the second, unset substring is not shown. An &quot;internal&quot; unset substring is shown as &quot;&lt;unset&gt;&quot;, as for the second data line. </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(a)|(b)/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>a <br />
0: a <br />
1: a <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>b <br />
0: b <br />
1:&nbsp;<wbr>&lt;unset&gt; <br />
2: b </p>
<p> If the strings contain any non-printing characters, they are output as \xhh escapes if the value is less than 256 and UTF mode is not set. Otherwise they are output as \x{hh...} escapes. See below for the definition of non-printing characters. If the <code>/aftertext</code> modifier is set, the output for substring 0 is followed by the the rest of the subject string, identified by &quot;0+&quot; like this: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/cat/aftertext <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>cataract <br />
0: cat <br />
0+&nbsp;<wbr>aract </p>
<p> If global matching is requested, the results of successive matching attempts are output in sequence, like this: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/\Bi(\w\w)/g <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>Mississippi <br />
0: iss <br />
1: ss <br />
0: iss <br />
1: ss <br />
0: ipp <br />
1: pp </p>
<p> &quot;No match&quot; is output only if the first match attempt fails. Here is an example of a failure message (the offset 4 that is specified by the <code>offset</code> modifier is past the end of the subject string): </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/xyz/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>xyz\=offset=4 <br />
&nbsp;<wbr>&nbsp;<wbr>Error -24&nbsp;<wbr>(bad offset value) </p>
<p> Note that whereas patterns can be continued over several lines (a plain &quot;&gt;&quot; prompt is used for continuations), subject lines may not. However newlines can be included in a subject by means of the \n escape (or \r, \r\n, etc., depending on the newline sequence setting).  </p>
<h2>OUTPUT FROM THE ALTERNATIVE MATCHING FUNCTION</h2>
<p> When the alternative matching function, <code>pcre2_dfa_match()</code>, is used, the output consists of a list of all the matches that start at the first point in the subject where there is at least one match. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(tang|tangerine|tan)/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>yellow tangerine\=dfa <br />
0: tangerine <br />
1: tang <br />
2: tan </p>
<p> Using the normal matching function on this data finds only &quot;tang&quot;. The longest matching string is always given first (and numbered zero). After a PCRE2_ERROR_PARTIAL return, the output is &quot;Partial match:&quot;, followed by the partially matching substring. Note that this is the entire substring that was inspected during the partial match; it may include characters before the actual match start if a lookbehind assertion, \b, or \B was involved. (\K is not supported for DFA matching.) </p>
<p> If global matching is requested, the search for further matches resumes at the end of the longest match. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/(tang|tangerine|tan)/g <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>yellow tangerine and tangy sultana\=dfa <br />
0: tangerine <br />
1: tang <br />
2: tan <br />
0: tang <br />
1: tan <br />
0: tan </p>
<p> The alternative matching function does not support substring capture, so the modifiers that are concerned with captured substrings are not relevant.  </p>
<h2>RESTARTING AFTER A PARTIAL MATCH</h2>
<p> When the alternative matching function has given the PCRE2_ERROR_PARTIAL return, indicating that the subject partially matched the pattern, you can restart the match with additional subject data by means of the <code>dfa_restart</code> modifier. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/^\d?\d(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d\d$/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>23ja\=P,dfa <br />
&nbsp;<wbr>&nbsp;<wbr>Partial match: 23ja <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>n05\=dfa,dfa_restart <br />
0: n05 </p>
<p> For further information about partial matching, see the <code>pcre2partial</code> documentation.  </p>
<h2>CALLOUTS</h2>
<p> If the pattern contains any callout requests, <code>pcre2test</code>&#8216;s callout function is called during matching unless <code>callout_none</code> is specified. This works with both matching functions. </p>
<p> The callout function in <code>pcre2test</code> returns zero (carry on matching) by default, but you can use a <code>callout_fail</code> modifier in a subject line (as described above) to change this and other parameters of the callout. </p>
<p> Inserting callouts can be helpful when using <code>pcre2test</code> to check complicated regular expressions. For further information about callouts, see the <code>pcre2callout</code> documentation. </p>
<p> The output for callouts with numerical arguments and those with string arguments is slightly different.  </p>
<h3>Callouts with numerical arguments</h3>
<p> By default, the callout function displays the callout number, the start and current positions in the subject text at the callout time, and the next pattern item to be tested. For example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>---&gt;pqrabcdef <br />
&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\d </p>
<p> This output indicates that callout number 0 occurred for a match attempt starting at the fourth character of the subject string, when the pointer was at the seventh character, and when the next pattern item was \d. Just one circumflex is output if the start and current positions are the same, or if the current position precedes the start position, which can happen if the callout is in a lookbehind assertion. </p>
<p> Callouts numbered 255 are assumed to be automatic callouts, inserted as a result of the <code>/auto_callout</code> pattern modifier. In this case, instead of showing the callout number, the offset in the pattern, preceded by a plus, is output. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/\d?[A-E]\*/auto_callout <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>E* <br />
&nbsp;<wbr>&nbsp;<wbr>---&gt;E* <br />
+0&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\d? <br />
+3&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[A-E] <br />
+8&nbsp;<wbr>^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\* <br />
&nbsp;<wbr>&nbsp;<wbr>+10&nbsp;<wbr>^&nbsp;<wbr>^ <br />
0: E* </p>
<p> If a pattern contains (*MARK) items, an additional line is output whenever a change of latest mark is passed to the callout function. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/a(*MARK:X)bc/auto_callout <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>abc <br />
&nbsp;<wbr>&nbsp;<wbr>---&gt;abc <br />
+0&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a <br />
+1&nbsp;<wbr>^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(*MARK:X) <br />
&nbsp;<wbr>&nbsp;<wbr>+10&nbsp;<wbr>^^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>b <br />
&nbsp;<wbr>&nbsp;<wbr>Latest Mark: X <br />
&nbsp;<wbr>&nbsp;<wbr>+11&nbsp;<wbr>^&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>c <br />
&nbsp;<wbr>&nbsp;<wbr>+12&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>^ <br />
0: abc </p>
<p> The mark changes between matching &quot;a&quot; and &quot;b&quot;, but stays the same for the rest of the match, so nothing more is output. If, as a result of backtracking, the mark reverts to being unset, the text &quot;&lt;unset&gt;&quot; is output.  </p>
<h3>Callouts with string arguments</h3>
<p> The output for a callout with a string argument is similar, except that instead of outputting a callout number before the position indicators, the callout string and its offset in the pattern string are output before the reflection of the subject string, and the subject string is reflected for each callout. For example: </p>
<p> <br />
&nbsp;<wbr>re&gt;&nbsp;<wbr>/^ab(?C&#8217;first&#8217;)cd(?C&quot;second&quot;)ef/ <br />
&nbsp;<wbr>&nbsp;<wbr>data&gt;&nbsp;<wbr>abcdefg <br />
&nbsp;<wbr>&nbsp;<wbr>Callout&nbsp;<wbr>(7):&nbsp;<wbr>&#8216;first&#8217; <br />
&nbsp;<wbr>&nbsp;<wbr>---&gt;abcdefg <br />
^&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>c <br />
&nbsp;<wbr>&nbsp;<wbr>Callout&nbsp;<wbr>(20):&nbsp;<wbr>&quot;second&quot; <br />
&nbsp;<wbr>&nbsp;<wbr>---&gt;abcdefg <br />
^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e <br />
0: abcdef </p>
<h2>NON-PRINTING CHARACTERS</h2>
<p> When <code>pcre2test</code> is outputting text in the compiled version of a pattern, bytes other than 32-126 are always treated as non-printing characters and are therefore shown as hex escapes. </p>
<p> When <code>pcre2test</code> is outputting text that is a matched part of a subject string, it behaves in the same way, unless a different locale has been set for the pattern (using the <code>/locale</code> modifier). In this case, the <code>isprint()</code> function is used to distinguish printing and non-printing characters.  </p>
<h2>SAVING AND RESTORING COMPILED PATTERNS</h2>
<p> It is possible to save compiled patterns on disc or elsewhere, and reload them later, subject to a number of restrictions. JIT data cannot be saved. The host on which the patterns are reloaded must be running the same version of PCRE2, with the same code unit width, and must also have the same endianness, pointer width and PCRE2_SIZE type. Before compiled patterns can be saved they must be serialized, that is, converted to a stream of bytes. A single byte stream may contain any number of compiled patterns, but they must all use the same character tables. A single copy of the tables is included in the byte stream (its size is 1088 bytes). </p>
<p> The functions whose names begin with <code>pcre2_serialize_</code> are used for serializing and de-serializing. They are described in the <code>pcre2serialize</code> documentation. In this section we describe the features of <code>pcre2test</code> that can be used to test these functions. </p>
<p> When a pattern with <code>push</code> modifier is successfully compiled, it is pushed onto a stack of compiled patterns, and <code>pcre2test</code> expects the next line to contain a new pattern (or command) instead of a subject line. By this means, a number of patterns can be compiled and retained. The <code>push</code> modifier is incompatible with <code>posix</code>, and control modifiers that act at match time are ignored (with a message). The <code>jitverify</code> modifier applies only at compile time. The command </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#save&nbsp;<wbr>&lt;filename&gt; </p>
<p> causes all the stacked patterns to be serialized and the result written to the named file. Afterwards, all the stacked patterns are freed. The command </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#load&nbsp;<wbr>&lt;filename&gt; </p>
<p> reads the data in the file, and then arranges for it to be de-serialized, with the resulting compiled patterns added to the pattern stack. The pattern on the top of the stack can be retrieved by the #pop command, which must be followed by lines of subjects that are to be matched with the pattern, terminated as usual by an empty line or end of file. This command may be followed by a modifier list containing only control modifiers that act after a pattern has been compiled. In particular, <code>hex</code>, <code>posix</code>, and <code>push</code> are not allowed, nor are any option-setting modifiers. The JIT modifiers are, however permitted. Here is an example that saves and reloads two patterns. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>/abc/push <br />
&nbsp;<wbr>&nbsp;<wbr>/xyz/push <br />
&nbsp;<wbr>&nbsp;<wbr>#save tempfile <br />
&nbsp;<wbr>&nbsp;<wbr>#load tempfile <br />
&nbsp;<wbr>&nbsp;<wbr>#pop info <br />
&nbsp;<wbr>&nbsp;<wbr>xyz </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>#pop jit,bincode <br />
&nbsp;<wbr>&nbsp;<wbr>abc </p>
<p> If <code>jitverify</code> is used with #pop, it does not automatically imply <code>jit</code>, which is different behaviour from when it is used on a pattern.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pcre2/">pcre2</a></code>(3), <code><a href="/docs/linux/man/3-pcre2api/">pcre2api</a></code>(3), <code><a href="/docs/linux/man/3-pcre2callout/">pcre2callout</a></code>(3), <code>pcre2jit</code>, <code><a href="/docs/linux/man/3-pcre2matching/">pcre2matching</a></code>(3), <code>pcre2partial</code>(d), <code><a href="/docs/linux/man/3-pcre2pattern/">pcre2pattern</a></code>(3), <code><a href="/docs/linux/man/3-pcre2serialize/">pcre2serialize</a></code>(3).  </p>
<h2>AUTHOR</h2>
<pre><code>Philip Hazel
University Computing Service
Cambridge, England.
</code></pre>
<h2>REVISION</h2>
<pre><code>Last updated: 12 December 2015
Copyright (c) 1997-2015 University of Cambridge.
</code></pre>
