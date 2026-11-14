---
title: "x86_64-linux-gnu-strings(1)"
name: "x86_64-linux-gnu-strings"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-linux-gnu-strings/"
description: "strings – print the sequences of printable characters in files"
---

<h2 class="name">NAME</h2>
<p> strings &#8211; print the sequences of printable characters in files </p>
<h2>SYNOPSIS</h2>
<p> strings [<code>-afovV</code>] [<code>&#8211;</code><i>min-len</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-n</code>&nbsp;<i>min-len</i>]&nbsp;[<code>&#8211;bytes=</code><i>min-len</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-t</code>&nbsp;<i>radix</i>]&nbsp;[<code>&#8211;radix=</code><i>radix</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-e</code>&nbsp;<i>encoding</i>]&nbsp;[<code>&#8211;encoding=</code><i>encoding</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-U</code>&nbsp;<i>method</i>]&nbsp;[<code>&#8211;unicode=</code><i>method</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;</code>]&nbsp;[<code>&#8211;all</code>]&nbsp;[<code>&#8211;print-file-name</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-T</code>&nbsp;<i>bfdname</i>]&nbsp;[<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-w</code>]&nbsp;[<code>&#8211;include-all-whitespace</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-s</code>]&nbsp;[<code>&#8211;output-separator</code>&nbsp;<i>sep_string</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;help</code>]&nbsp;[<code>&#8211;version</code>]&nbsp;<i>file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> For each <i>file</i> given, <font SIZE="-1">GNU</font> <code>strings</code> prints the printable character sequences that are at least 4 characters long (or the number given with the options below) and are followed by an unprintable character. </p>
<p> Depending upon how the strings program was configured it will default to either displaying all the printable sequences that it can find in each file, or only those sequences that are in loadable, initialized data sections. If the file type is unrecognizable, or if strings is reading from stdin then it will always display all of the printable sequences that it can find. </p>
<p> For backwards compatibility any file that occurs after a command-line option of just <code>&#8211;</code> will also be scanned in full, regardless of the presence of any <code>-d</code> option. </p>
<p> <code>strings</code> is mainly useful for determining the contents of non-text files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;all</code></p>
<dd>
<dt><code>&#8211;</code></p>
<dd> Scan the whole file, regardless of what sections it contains or whether those sections are loaded or initialized. Normally this is the default behaviour, but strings can be configured so that the <code>-d</code> is the default instead. </p>
<p> The <code>&#8211;</code> option is position dependent and forces strings to perform full scans of any file that is mentioned after the <code>&#8211;</code> on the command line, even if the <code>-d</code> option has been specified.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;data</code></p>
<dd> Only print strings from initialized, loaded data sections in the file. This may reduce the amount of garbage in the output, but it also exposes the strings program to any security flaws that may be present in the <font SIZE="-1">BFD</font> library used to scan and load sections. Strings can be configured so that this option is the default behaviour. In such cases the <code>-a</code> option can be used to avoid using the <font SIZE="-1">BFD</font> library and instead just print all of the strings found in the file.</p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;print-file-name</code></p>
<dd> Print the name of the file before each string.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the program usage on the standard output and exit.</p>
<dt><code>&#8211;</code><i>min-len</i></p>
<dd>
<dt><code>-n</code> <i>min-len</i></p>
<dd>
<dt><code>&#8211;bytes=</code><i>min-len</i></p>
<dd> Print sequences of displayable characters that are at least <i>min-len</i> characters long. If not specified a default minimum length of 4 is used. The distinction between displayable and non-displayable characters depends upon the setting of the <code>-e</code> and <code>-U</code> options. Sequences are always terminated at control characters such as new-line and carriage-return, but not the tab character.</p>
<dt><code>-o</code></p>
<dd> Like <code>-t o</code>. Some other versions of <code>strings</code> have <code>-o</code> act like <code>-t d</code> instead. Since we can not be compatible with both ways, we simply chose one.</p>
<dt><code>-t</code> <i>radix</i></p>
<dd>
<dt><code>&#8211;radix=</code><i>radix</i></p>
<dd> Print the offset within the file before each string. The single character argument specifies the radix of the offset&#8212;<code>o</code> for octal, <code>x</code> for hexadecimal, or <code>d</code> for decimal.</p>
<dt><code>-e</code> <i>encoding</i></p>
<dd>
<dt><code>&#8211;encoding=</code><i>encoding</i></p>
<dd> Select the character encoding of the strings that are to be found. Possible values for <i>encoding</i> are: <code>s</code> = single-7-bit-byte characters (<font SIZE="-1">ASCII, ISO 8859,</font> etc., default), <code>S</code> = single-8-bit-byte characters, <code>b</code> = 16-bit bigendian, <code>l</code> = 16-bit littleendian, <code>B</code> = 32-bit bigendian, <code>L</code> = 32-bit littleendian. Useful for finding wide character strings. (<code>l</code> and <code>b</code> apply to, for example, Unicode <font SIZE="-1">UTF-16/UCS-2</font> encodings).</p>
<dt><code>-U</code> <i>[d|i|l|e|x|h]</i></p>
<dd>
<dt><code>&#8211;unicode=</code><i>[default|invalid|locale|escape|hex|highlight]</i></p>
<dd> Controls the display of <font SIZE="-1">UTF-8</font> encoded multibyte characters in strings. The default (<code>&#8211;unicode=default</code>) is to give them no special treatment, and instead rely upon the setting of the <code>&#8211;encoding</code> option. The other values for this option automatically enable <code>&#8211;encoding=S</code>. </p>
<p> The <code>&#8211;unicode=invalid</code> option treats them as non-graphic characters and hence not part of a valid string. All the remaining options treat them as valid string characters. </p>
<p> The <code>&#8211;unicode=locale</code> option displays them in the current locale, which may or may not support <font SIZE="-1">UTF-8</font> encoding. The <code>&#8211;unicode=hex</code> option displays them as hex byte sequences enclosed between <i>&lt;&gt;</i> characters. The <code>&#8211;unicode=escape</code> option displays them as escape sequences (<i>
