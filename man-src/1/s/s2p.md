---
title: "s2p(1)"
name: "s2p"
section: "1"
letter: "s"
url: "/docs/linux/man/1-s2p/"
description: "psed – a stream editor"
---

<h2 class="name">NAME</h2>
<p> psed &#8211; a stream editor </p>
<h2>SYNOPSIS</h2>
<pre><code>
psed[-an] script[file...] psed[-an][-e script][-f script - file][file...] s2p[-an][-e script][-f script - file]
</code></pre>
<h2>DESCRIPTION</h2>
<p> A stream editor reads the input stream consisting of the specified files (or standard input, if none are given), processes is line by line by applying a script consisting of edit commands, and writes resulting lines to standard output. The filename &#8216;<tt>&quot;-&quot;</tt>&#8216; may be used to read standard input. </p>
<p> The edit script is composed from arguments of <code>-e</code> options and script-files, in the given order. A single script argument may be specified as the first parameter. </p>
<p> If this program is invoked with the name <i>s2p</i>, it will act as a sed-to-Perl translator. See &#8220;<font SIZE="-1">SED</font> <font SIZE="-1">SCRIPT</font> <font SIZE="-1">TRANSLATION</font>&#8221;. </p>
<p> <code>sed</code> returns an exit code of 0 on success or &gt;0 if an error occurred.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> A file specified as argument to the <code>w</code> edit command is by default opened before input processing starts. Using <code>-a</code>, opening of such files is delayed until the first line is actually written to the file.</p>
<dt><code>-e</code> <i>script</i></p>
<dd> The editing commands defined by <i>script</i> are appended to the script. Multiple commands must be separated by newlines.</p>
<dt><code>-f</code> <i>script-file</i></p>
<dd> Editing commands from the specified <i>script-file</i> are read and appended to the script.</p>
<dt><code>-n</code></p>
<dd> By default, a line is written to standard output after the editing script has been applied to it. The <code>-n</code> option suppresses automatic printing.</dl>
<h2>COMMANDS</h2>
<p> <code>sed</code> command syntax is defined as </p>
<p>[<i>address</i>[<code>,</code><i>address</i>]][<code>!</code>]<i>function</i>[<i>argument</i>] </p>
<p> with whitespace being permitted before or after addresses, and between the function character and the argument. The <i>address</i>es and the address inverter (<tt>&quot;!&quot;</tt>) are used to restrict the application of a command to the selected line(s) of input. </p>
<p> Each command must be on a line of its own, except where noted in the synopses below. </p>
<p> The edit cycle performed on each input line consist of reading the line (without its trailing newline character) into the <i>pattern space</i>, applying the applicable commands of the edit script, writing the final contents of the pattern space and a newline to the standard output. A <i>hold space</i> is provided for saving the contents of the pattern space for later use.</p>
<h3>Addresses</h3>
<p> A sed address is either a line number or a pattern, which may be combined arbitrarily to construct ranges. Lines are numbered across all input files. </p>
<p> Any address may be followed by an exclamation mark (&#8216;<tt>&quot;!&quot;</tt>&#8216;), selecting all lines not matching that address.</p>
<dl>
<dt><i>number</i></p>
<dd> The line with the given number is selected.</p>
<dt><code>$</code></p>
<dd> A dollar sign (<tt>&quot;$&quot;</tt>) is the line number of the last line of the input stream.</p>
<dt><code>/</code><i>regular expression</i><code>/</code></p>
<dd> A pattern address is a basic regular expression (see &#8220;<font SIZE="-1">BASIC</font> <font SIZE="-1">REGULAR</font> <font SIZE="-1">EXPRESSIONS</font>&#8221;), between the delimiting character <tt>&quot;/&quot;</tt>. Any other character except <tt>&quot;\&quot;</tt> or newline may be used to delimit a pattern address when the initial delimiter is prefixed with a backslash (&#8216;<tt>&quot;\&quot;</tt>&#8216;).</dl>
<p> If no address is given, the command selects every line. </p>
<p> If one address is given, it selects the line (or lines) matching the address. </p>
<p> Two addresses select a range that begins whenever the first address matches, and ends (including that line) when the second address matches. If the first (second) address is a matching pattern, the second address is not applied to the very same line to determine the end of the range. Likewise, if the second address is a matching pattern, the first address is not applied to the very same line to determine the begin of another range. If both addresses are line numbers, and the second line number is less than the first line number, then only the first line is selected.</p>
<h3>Functions</h3>
<p> The maximum permitted number of addresses is indicated with each function synopsis below. </p>
<p> The argument <i>text</i> consists of one or more lines following the command. Embedded newlines in <i>text</i> must be preceded with a backslash. Other backslashes in <i>text</i> are deleted and the following character is taken literally.</p>
<dl>
<dt>[1addr]<code>a\</code> <i>text</i></p>
<dd> Write <i>text</i> (which must start on the line following the command) to standard output immediately before reading the next line of input, either by executing the <code>N</code> function or by beginning a new cycle.</p>
<dt>[2addr]<code>b</code> [<i>label</i>]</p>
<dd> Branch to the <code>:</code> function with the specified <i>label</i>. If no label is given, branch to the end of the script.</p>
<dt>[2addr]<code>c\</code> <i>text</i></p>
<dd> The line, or range of lines, selected by the address is deleted. The <i>text</i> (which must start on the line following the command) is written to standard output. With an address range, this occurs at the end of the range.</p>
<dt>[2addr]<code>d</code></p>
<dd> Deletes the pattern space and starts the next cycle.</p>
<dt>[2addr]<code>D</code></p>
<dd> Deletes the pattern space through the first embedded newline or to the end. If the pattern space becomes empty, a new cycle is started, otherwise execution of the script is restarted.</p>
<dt>[2addr]<code>g</code></p>
<dd> Replace the contents of the pattern space with the hold space.</p>
<dt>[2addr]<code>G</code></p>
<dd> Append a newline and the contents of the hold space to the pattern space.</p>
<dt>[2addr]<code>h</code></p>
<dd> Replace the contents of the hold space with the pattern space.</p>
<dt>[2addr]<code>H</code></p>
<dd> Append a newline and the contents of the pattern space to the hold space.</p>
<dt>[1addr]<code>i\</code> <i>text</i></p>
<dd> Write the <i>text</i> (which must start on the line following the command) to standard output.</p>
<dt>[2addr]<code>l</code></p>
<dd> Print the contents of the pattern space: non-printable characters are shown in C-style escaped form; long lines are split and have a trailing ^&#8217;<tt>&quot;\&quot;</tt>&#8216; at the point of the split; the true end of a line is marked with a &#8216;<tt>&quot;$&quot;</tt>&#8216;. Escapes are: &#8216;&#8217;, &#8216;	&#8217;, &#8216;
&#8217;, &#8216;&#8217;, &#8216;&#8217;, &#8216;&#8217; for <font SIZE="-1">BEL</font>, <font SIZE="-1">HT</font>, <font SIZE="-1">LF</font>, <font SIZE="-1">FF</font>, <font SIZE="-1">CR</font>, <font SIZE="-1">ESC</font>, respectively, and &#8216;\&#8217; followed by a three-digit octal number for all other non-printable characters.</p>
<dt>[2addr]<code>n</code></p>
<dd> If automatic printing is enabled, write the pattern space to the standard output. Replace the pattern space with the next line of input. If there is no more input, processing is terminated.</p>
<dt>[2addr]<code>N</code></p>
<dd> Append a newline and the next line of input to the pattern space. If there is no more input, processing is terminated.</p>
<dt>[2addr]<code>p</code></p>
<dd> Print the pattern space to the standard output. (Use the <code>-n</code> option to suppress automatic printing at the end of a cycle if you want to avoid double printing of lines.)</p>
<dt>[2addr]<code>P</code></p>
<dd> Prints the pattern space through the first embedded newline or to the end.</p>
<dt>[1addr]<code>q</code></p>
<dd> Branch to the end of the script and quit without starting a new cycle.</p>
<dt>[1addr]<code>r</code> <i>file</i></p>
<dd> Copy the contents of the <i>file</i> to standard output immediately before the next attempt to read a line of input. Any error encountered while reading <i>file</i> is silently ignored.</p>
<dt>[2addr]<code>s/</code><i>regular expression</i><code>/</code><i>replacement</i><code>/</code><i>flags</i></p>
<dd> Substitute the <i>replacement</i> string for the first substring in the pattern space that matches the <i>regular expression</i>. Any character other than backslash or newline can be used instead of a slash to delimit the regular expression and the replacement. To use the delimiter as a literal character within the regular expression and the replacement, precede the character by a backslash (&#8216;<tt>&quot;\&quot;</tt>&#8216;). </p>
<p> Literal newlines may be embedded in the replacement string by preceding a newline with a backslash. </p>
<p> Within the replacement, an ampersand (&#8216;<tt>&quot;&amp;&quot;</tt>&#8216;) is replaced by the string matching the regular expression. The strings &#8216;<tt>&quot;\1&quot;</tt>&#8216; through &#8216;<tt>&quot;\9&quot;</tt>&#8216; are replaced by the corresponding subpattern (see &#8220;<font SIZE="-1">BASIC</font> <font SIZE="-1">REGULAR</font> <font SIZE="-1">EXPRESSIONS</font>&#8221;). To get a literal &#8216;<tt>&quot;&amp;&quot;</tt>&#8216; or &#8216;<tt>&quot;\&quot;</tt>&#8216; in the replacement text, precede it by a backslash. </p>
<p> The following <i>flags</i> modify the behaviour of the <code>s</code> command:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>g</code></p>
<dd> The replacement is performed for all matching, non-overlapping substrings of the pattern space.</p>
<dt><code>1</code>..<code>9</code></p>
<dd> Replace only the n-th matching substring of the pattern space.</p>
<dt><code>p</code></p>
<dd> If the substitution was made, print the new value of the pattern space.</p>
<dt><code>w</code> <i>file</i></p>
<dd> If the substitution was made, write the new value of the pattern space to the specified file.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>[2addr]<code>t</code> [<i>label</i>]</p>
<dd> Branch to the <code>:</code> function with the specified <i>label</i> if any <code>s</code> substitutions have been made since the most recent reading of an input line or execution of a <code>t</code> function. If no label is given, branch to the end of the script.</p>
<dt>[2addr]<code>w</code> <i>file</i></p>
<dd> The contents of the pattern space are written to the <i>file</i>.</p>
<dt>[2addr]<code>x</code></p>
<dd> Swap the contents of the pattern space and the hold space.</p>
<dt>[2addr]<code>y</code><code>/</code><i>string1</i><code>/</code><i>string2</i><code>/</code></p>
<dd> In the pattern space, replace all characters occurring in <i>string1</i> by the character at the corresponding position in <i>string2</i>. It is possible to use any character (other than a backslash or newline) instead of a slash to delimit the strings. Within <i>string1</i> and <i>string2</i>, a backslash followed by any character other than a newline is that literal character, and a backslash followed by an &#8216;n&#8217; is replaced by a newline character.</p>
<dt>[1addr]<code>=</code></p>
<dd> Prints the current line number on the standard output.</p>
<dt>[0addr]<code>:</code> [<i>label</i>]</p>
<dd> The command specifies the position of the <i>label</i>. It has no other effect.</p>
<dt>[2addr]<code>{</code> [<i>command</i>]</p>
<dd>
<dt>[0addr]<code>}</code></p>
<dd> These two commands begin and end a command list. The first command may be given on the same line as the opening <code>{</code> command. The commands within the list are jointly selected by the address(es) given on the <code>{</code> command (but may still have individual addresses).</p>
<dt>[0addr]<code>#</code> [<i>comment</i>]</p>
<dd> The entire line is ignored (treated as a comment). If, however, the first two characters in the script are &#8216;<tt>&quot;#n&quot;</tt>&#8216;, automatic printing of output is suppressed, as if the <code>-n</code> option were given on the command line.</dl>
<h2>BASIC REGULAR EXPRESSIONS</h2>
<p> A <i>Basic Regular Expression</i> (<font SIZE="-1">BRE</font>), as defined in <font SIZE="-1">POSIX</font> 1003.2, consists of <i>atoms</i>, for matching parts of a string, and <i>bounds</i>, specifying repetitions of a preceding atom.</p>
<h3>Atoms</h3>
<p> The possible atoms of a <font SIZE="-1">BRE</font> are: <code>.</code>, matching any single character; <code>^</code> and <code>$</code>, matching the null string at the beginning or end of a string, respectively; a <i>bracket expressions</i>, enclosed in <code>[</code> and <code>]</code> (see below); and any single character with no other significance (matching that character). A <code>\</code> before one of: <code>.</code>, <code>^</code>, <code>$</code>, <code>[</code>, <code>*</code>, <code>\</code>, matching the character after the backslash. A sequence of atoms enclosed in <code>\(</code> and <code>\)</code> becomes an atom and establishes the target for a <i>backreference</i>, consisting of the substring that actually matches the enclosed atoms. Finally, <code>\</code> followed by one of the digits <code>0</code> through <code>9</code> is a backreference. </p>
<p> A <code>^</code> that is not first, or a <code>$</code> that is not last does not have a special significance and need not be preceded by a backslash to become literal. The same is true for a <code>]</code>, that does not terminate a bracket expression. </p>
<p> An unescaped backslash cannot be last in a <font SIZE="-1">BRE</font>.</p>
<h3>Bounds</h3>
<p> The <font SIZE="-1">BRE</font> bounds are: <code>*</code>, specifying 0 or more matches of the preceding atom; <code>\{</code><i>count</i><code>\}</code>, specifying that many repetitions; <code>\{</code><i>minimum</i><code>,\}</code>, giving a lower limit; and <code>\{</code><i>minimum</i><code>,</code><i>maximum</i><code>\}</code> finally defines a lower and upper bound. </p>
<p> A bound appearing as the first item in a <font SIZE="-1">BRE</font> is taken literally.</p>
<h3>Bracket Expressions</h3>
<p> A <i>bracket expression</i> is a list of characters, character ranges and character classes enclosed in <code>[</code> and <code>]</code> and matches any single character from the represented set of characters. </p>
<p> A character range is written as two characters separated by <code>&#8211;</code> and represents all characters (according to the character collating sequence) that are not less than the first and not greater than the second. (Ranges are very collating-sequence-dependent, and portable programs should avoid relying on them.) </p>
<p> A character class is one of the class names </p>
<pre>
   alnum     digit     punct
   alpha     graph     space
   blank     lower     upper
   cntrl     print     xdigit
</pre>
<p> enclosed in <code>[:</code> and <code>:]</code> and represents the set of characters as defined in <i><a href="/docs/linux/man/3-ctype/">ctype</a></i>(3). </p>
<p> If the first character after <code>[</code> is <code>^</code>, the sense of matching is inverted. </p>
<p> To include a literal &#8216;<tt>&quot;^&quot;</tt>&#8216;, place it anywhere else but first. To include a literal &#8216;<tt>&quot;]&quot;</tt>&#8216; place it first or immediately after an initial <code>^</code>. To include a literal &#8216;<tt>&quot;-&quot;</tt>&#8216; make it the first (or second after <code>^</code>) or last character, or the second endpoint of a range. </p>
<p> The special bracket expression constructs <tt>&quot;[[:&lt;:]]&quot;</tt> and <tt>&quot;[[:&gt;:]]&quot;</tt> match the null string at the beginning and end of a word respectively. (Note that neither is identical to Perl&#8217;s &#8216;&#8217; atom.)</p>
<h3>Additional Atoms</h3>
<p> Since some sed implementations provide additional regular expression atoms (not defined in <font SIZE="-1">POSIX</font> 1003.2), <code>psed</code> is capable of translating the following backslash escapes:</p>
<dl>
<dt><code>\&lt;</code> This is the same as &quot;[[:&gt;:]]&quot;.</p>
<dd>
<dt><code>\&gt;</code> This is the same as &quot;[[:&lt;:]]&quot;.</p>
<dd>
<dt><code>\w</code> This is an abbreviation for &quot;[[:alnum:]_]&quot;.</p>
<dd>
<dt><code>\W</code> This is an abbreviation for &quot;[^[:alnum:]_]&quot;.</p>
<dd>
<dt><code>\y</code> Match the empty string at a word boundary.</p>
<dd>
<dt><code>\B</code> Match the empty string between any two either word or non-word characters.</p>
<dd></dl>
<p> To enable this feature, the environment variable <font SIZE="-1">PSEDEXTBRE</font> must be set to a string containing the requested characters, e.g.: <tt>&quot;PSEDEXTBRE='&lt;&gt;wW'&quot;</tt>.</p>
<h2>ENVIRONMENT</h2>
<p> The environment variable <tt>&quot;PSEDEXTBRE&quot;</tt> may be set to extend BREs. See &#8220;Additional Atoms&#8221;.</p>
<h2>DIAGNOSTICS</h2>
<dl>
<dt>ambiguous translation for character &#8216;%s&#8217; in &#8216;y&#8217; command</p>
<dd> The indicated character appears twice, with different translations.</p>
<dt>&#8216;[&#8216; cannot be last in pattern</p>
<dd> A &#8216;[&#8216; in a <font SIZE="-1">BRE</font> indicates the beginning of a <i>bracket expression</i>.</p>
<dt>&#8216;\&#8217; cannot be last in pattern</p>
<dd> A &#8216;\&#8217; in a <font SIZE="-1">BRE</font> is used to make the subsequent character literal.</p>
<dt>&#8216;\&#8217; cannot be last in substitution</p>
<dd> A &#8216;\&#8217; in a substitution string is used to make the subsequent character literal.</p>
<dt>conflicting flags &#8216;%s&#8217;</p>
<dd> In an <code>s</code> command, either the &#8216;g&#8217; flag and an n-th occurrence flag, or multiple n-th occurrence flags are specified. Note that only the digits ^&#8217;1&#8242; through &#8216;9&#8217; are permitted.</p>
<dt>duplicate label %s (first defined at %s)</p>
<dd>
<dt>excess address(es)</p>
<dd> The command has more than the permitted number of addresses.</p>
<dt>extra characters after command (%s)</p>
<dd>
<dt>illegal option &#8216;%s&#8217;</p>
<dd>
<dt>improper delimiter in s command</p>
<dd> The <font SIZE="-1">BRE</font> and substitution may not be delimited with &#8216;\&#8217; or newline.</p>
<dt>invalid address after &#8216;,&#8217;</p>
<dd>
<dt>invalid backreference (%s)</p>
<dd> The specified backreference number exceeds the number of backreferences in the <font SIZE="-1">BRE</font>.</p>
<dt>invalid repeat clause &#8216;\{%s\}&#8217;</p>
<dd> The repeat clause does not contain a valid integer value, or pair of values.</p>
<dt>malformed regex, 1st address</p>
<dd>
<dt>malformed regex, 2nd address</p>
<dd>
<dt>malformed regular expression</p>
<dd>
<dt>malformed substitution expression</p>
<dd>
<dt>malformed &#8216;y&#8217; command argument</p>
<dd> The first or second string of a <code>y</code> command is syntactically incorrect.</p>
<dt>maximum less than minimum in &#8216;\{%s\}&#8217;</p>
<dd>
<dt>no script command given</p>
<dd> There must be at least one <code>-e</code> or one <code>-f</code> option specifying a script or script file.</p>
<dt>&#8216;\&#8217; not valid as delimiter in &#8216;y&#8217; command</p>
<dd>
<dt>option -e requires an argument</p>
<dd>
<dt>option -f requires an argument</p>
<dd>
<dt>&#8216;s&#8217; command requires argument</p>
<dd>
<dt>start of unterminated &#8216;{&#8216;</p>
<dd>
<dt>string lengths in &#8216;y&#8217; command differ</p>
<dd> The translation table strings in a <code>y</code> command must have equal lengths.</p>
<dt>undefined label &#8216;%s&#8217;</p>
<dd>
<dt>unexpected &#8216;}&#8217;</p>
<dd> A <code>}</code> command without a preceding <code>{</code> command was encountered.</p>
<dt>unexpected end of script</p>
<dd> The end of the script was reached although a text line after a <code>a</code>, <code>c</code> or <code>i</code> command indicated another line.</p>
<dt>unknown command &#8216;%s&#8217;</p>
<dd>
<dt>unterminated &#8216;[&#8216;</p>
<dd> A <font SIZE="-1">BRE</font> contains an unterminated bracket expression.</p>
<dt>unterminated &#8216;\(&#8216;</p>
<dd> A <font SIZE="-1">BRE</font> contains an unterminated backreference.</p>
<dt>&#8216;\{&#8216; without closing &#8216;\}&#8217;</p>
<dd> A <font SIZE="-1">BRE</font> contains an unterminated bounds specification.</p>
<dt>&#8216;\)&#8217; without preceding &#8216;\(&#8216;</p>
<dd>
<dt>&#8216;y&#8217; command requires argument</p>
<dd></dl>
<h2>EXAMPLE</h2>
<p> The basic material for the preceding section was generated by running the sed script </p>
<pre><code>
#no autoprint
   s/^.*Warn( *"\([^"]*\)".*$/\1/
   t process
   b
   :process
   s/$!/%s/g
   s/$[_[:alnum:]]\{1,\}/%s/g
   s/\\/\/g
   s/^/=item /
   p
</code></pre>
<p> on the program&#8217;s own text, and piping the output into <tt>&quot;sort -u&quot;</tt>.</p>
<h2>SED SCRIPT TRANSLATION</h2>
<p> If this program is invoked with the name <i>s2p</i> it will act as a sed-to-Perl translator. After option processing (all other arguments are ignored), a Perl program is printed on standard output, which will process the input stream (as read from all arguments) in the way defined by the sed script and the option setting used for the translation.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i><a href="/docs/linux/man/7-re_format/">re_format</a></i>(7)</p>
<h2>BUGS</h2>
<p> The <code>l</code> command will show escape characters (<font SIZE="-1">ESC</font>) as &#8216;<tt>&quot;&quot;</tt>&#8216;, but a vertical tab (<font SIZE="-1">VT</font>) in octal. </p>
<p> Trailing spaces are truncated from labels in <code>:</code>, <code>t</code> and <code>b</code> commands. </p>
<p> The meaning of an empty regular expression (&#8216;<tt>&quot;//&quot;</tt>&#8216;), as defined by <code>sed</code>, is &#8220;the last pattern used, at run time&#8221;. This deviates from the Perl interpretation, which will re-use the &#8220;last last successfully executed regular expression&#8221;. Since keeping track of pattern usage would create terribly cluttered code, and differences would only appear in obscure context (where other <code>sed</code> implementations appear to deviate, too), the Perl semantics was adopted. Note that common usage of this feature, such as in <tt>&quot;/abc/s//xyz/&quot;</tt>, will work as expected. </p>
<p> Collating elements (of bracket expressions in BREs) are not implemented.</p>
<h2>STANDARDS</h2>
<p> This <code>sed</code> implementation conforms to the <font SIZE="-1">IEEE</font> Std1003.2-1992 (&#8220;<font SIZE="-1">POSIX</font>.2&#8221;) definition of <code>sed</code>, and is compatible with the <i>OpenBSD</i> implementation, except where otherwise noted (see &#8220;<font SIZE="-1">BUGS</font>&#8221;).</p>
<h2>AUTHOR</h2>
<p> This Perl implementation of <i>sed</i> was written by Wolfgang Laun, <i>Wolfgang.Laun [at] alcatel.at</i>.</p>
<h2>COPYRIGHT and LICENSE</h2>
<p> This program is free and open software. You may use, modify, distribute, and sell this program (and any modified variants) in any way you wish, provided you do not restrict others from doing the same. </p>
<h2>Index</h2>
