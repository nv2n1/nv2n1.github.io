---
title: "sed(1)"
name: "sed"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sed/"
description: "sed – stream editor for filtering and transforming text"
---

<h2 class="name">NAME</h2>
<p> sed &#8211; stream editor for filtering and transforming text </p>
<h2>SYNOPSIS</h2>
<p> <code>sed</code> [<i>OPTION</i>]&#8230; <i>{script-only-if-no-other-script} </i>[<i>input-file</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>Sed</i> is a stream editor. A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline). While in some ways similar to an editor which permits scripted edits (such as <i>ed</i>), <i>sed</i> works by making only one pass over the input(s), and is consequently more efficient. But it is <i>sed</i>&#8216;s ability to filter text in a pipeline which particularly distinguishes it from other types of editors.</p>
<dl>
<dt> <code>-n</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dt>
<dd>
<dd>suppress automatic printing of pattern space</p>
<dt> <code>&#8211;debug</code></p>
<dt>
<dd>
<dd>annotate program execution</p>
<dt> <code>-e</code> script, <code>&#8211;expression</code>=<i>script</i></p>
<dt>
<dd>
<dd>add the script to the commands to be executed</p>
<dt> <code>-f</code> script-file, <code>&#8211;file</code>=<i>script-file</i></p>
<dt>
<dd>
<dd>add the contents of script-file to the commands to be executed</p>
<dt> <code>&#8211;follow-symlinks</code></p>
<dt>
<dd>
<dd>follow symlinks when processing in place</p>
<dt> <code>-i[SUFFIX]</code>, <code>&#8211;in-place</code>[=<i>SUFFIX</i>]</p>
<dt>
<dd>
<dd>edit files in place (makes backup if SUFFIX supplied)</p>
<dt> <code>-l</code> N, <code>&#8211;line-length</code>=<i>N</i></p>
<dt>
<dd>
<dd>specify the desired line-wrap length for the `l&#8217; command</p>
<dt> <code>&#8211;posix</code></p>
<dt>
<dd>
<dd>disable all GNU extensions.</p>
<dt> <code>-E</code>, <code>-r</code>, <code>&#8211;regexp-extended</code></p>
<dt>
<dd>
<dd>use extended regular expressions in the script (for portability use POSIX <code>-E</code>).</p>
<dt> <code>-s</code>, <code>&#8211;separate</code></p>
<dt>
<dd>
<dd>consider files as separate rather than as a single, continuous long stream.</p>
<dt> <code>&#8211;sandbox</code></p>
<dt>
<dd>
<dd>operate in sandbox mode (disable e/r/w commands).</p>
<dt> <code>-u</code>, <code>&#8211;unbuffered</code></p>
<dt>
<dd>
<dd>load minimal amounts of data from the input files and flush the output buffers more often</p>
<dt> <code>-z</code>, <code>&#8211;null-data</code></p>
<dt>
<dd>
<dd>separate lines by NUL characters</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If no <code>-e</code>, <code>&#8211;expression</code>, <code>-f</code>, or <code>&#8211;file</code> option is given, then the first non-option argument is taken as the sed script to interpret. All remaining arguments are names of input files; if no input files are specified, then the standard input is read. </p>
<p> GNU sed home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/sed/">https://www.gnu.org/software/sed/</a>&gt;. General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;. E-mail bug reports to: &lt;bug-sed [at] gnu.org&gt;.</p>
<h2>COMMAND SYNOPSIS</h2>
<p> This is just a brief synopsis of <i>sed</i> commands to serve as a reminder to those who already know <i>sed</i>; other documentation (such as the texinfo document) must be consulted for fuller descriptions.</p>
<h3>Zero-address &#8220;commands&#8221;</h3>
<dl>
<dt>:&nbsp;<i>label</i></p>
<dd> Label for <code>b</code> and <code>t</code> commands.</p>
<dt>#<i>comment</i></p>
<dd> The comment extends until the next newline (or the end of a <code>-e</code> script fragment).</p>
<dt>}</p>
<dd> The closing bracket of a { } block.</dl>
<h3>Zero- or One- address commands</h3>
<dl>
<dt>=</p>
<dd> Print the current line number.</p>
<dt>a \</p>
<dd>
<dt><i>text</i></p>
<dd> Append <i>text</i>, which has each embedded newline preceded by a backslash.</p>
<dt>i \</p>
<dd>
<dt><i>text</i></p>
<dd> Insert <i>text</i>, which has each embedded newline preceded by a backslash.</p>
<dt>q [<i>exit-code</i>]</p>
<dd> Immediately quit the <i>sed</i> script without processing any more input, except that if auto-print is not disabled the current pattern space will be printed. The exit code argument is a GNU extension.</p>
<dt>Q [<i>exit-code</i>]</p>
<dd> Immediately quit the <i>sed</i> script without processing any more input. This is a GNU extension.</p>
<dt>r&nbsp;<i>filename</i></p>
<dd> Append text read from <i>filename</i>.</p>
<dt>R&nbsp;<i>filename</i></p>
<dd> Append a line read from <i>filename</i>. Each invocation of the command reads a line from the file. This is a GNU extension.</dl>
<h3>Commands which accept address ranges</h3>
<dl>
<dt>{</p>
<dd> Begin a block of commands (end with a }).</p>
<dt>b&nbsp;<i>label</i></p>
<dd> Branch to <i>label</i>; if <i>label</i> is omitted, branch to end of script.</p>
<dt>c \</p>
<dd>
<dt><i>text</i></p>
<dd> Replace the selected lines with <i>text</i>, which has each embedded newline preceded by a backslash.</p>
<dt>d</p>
<dd> Delete pattern space. Start next cycle.</p>
<dt>D</p>
<dd> If pattern space contains no newline, start a normal new cycle as if the d command was issued. Otherwise, delete text in the pattern space up to the first newline, and restart cycle with the resultant pattern space, without reading a new line of input.</p>
<dt>h H</p>
<dd> Copy/append pattern space to hold space.</p>
<dt>g G</p>
<dd> Copy/append hold space to pattern space.</p>
<dt>l</p>
<dd> List out the current line in a &#8220;visually unambiguous&#8221; form.</p>
<dt>l&nbsp;<i>width</i></p>
<dd> List out the current line in a &#8220;visually unambiguous&#8221; form, breaking it at <i>width</i> characters. This is a GNU extension.</p>
<dt>n N</p>
<dd> Read/append the next line of input into the pattern space.</p>
<dt>p</p>
<dd> Print the current pattern space.</p>
<dt>P</p>
<dd> Print up to the first embedded newline of the current pattern space.</p>
<dt>s/<i>regexp</i>/<i>replacement</i>/</p>
<dd> Attempt to match <i>regexp</i> against the pattern space. If successful, replace that portion matched with <i>replacement</i>. The <i>replacement</i> may contain the special character <code>&amp;</code> to refer to that portion of the pattern space which matched, and the special escapes \1 through \9 to refer to the corresponding matching sub-expressions in the <i>regexp</i>.</p>
<dt>t&nbsp;<i>label</i></p>
<dd> If a s/// has done a successful substitution since the last input line was read and since the last t or T command, then branch to <i>label</i>; if <i>label</i> is omitted, branch to end of script.</p>
<dt>T&nbsp;<i>label</i></p>
<dd> If no s/// has done a successful substitution since the last input line was read and since the last t or T command, then branch to <i>label</i>; if <i>label</i> is omitted, branch to end of script. This is a GNU extension.</p>
<dt>w&nbsp;<i>filename</i></p>
<dd> Write the current pattern space to <i>filename</i>.</p>
<dt>W&nbsp;<i>filename</i></p>
<dd> Write the first line of the current pattern space to <i>filename</i>. This is a GNU extension.</p>
<dt>x</p>
<dd> Exchange the contents of the hold and pattern spaces.</p>
<dt>y/<i>source</i>/<i>dest</i>/</p>
<dd> Transliterate the characters in the pattern space which appear in <i>source</i> to the corresponding character in <i>dest</i>.</dl>
<h2>Addresses</h2>
<p> <i>Sed</i> commands can be given with no addresses, in which case the command will be executed for all input lines; with one address, in which case the command will only be executed for input lines which match that address; or with two addresses, in which case the command will be executed for all input lines which match the inclusive range of lines starting from the first address and continuing to the second address. Three things to note about address ranges: the syntax is <i>addr1</i>,<i>addr2</i> (i.e., the addresses are separated by a comma); the line which <i>addr1</i> matched will always be accepted, even if <i>addr2</i> selects an earlier line; and if <i>addr2</i> is a <i>regexp</i>, it will not be tested against the line that <i>addr1</i> matched. </p>
<p> After the address (or address-range), and before the command, a <code>!</code> may be inserted, which specifies that the command shall only be executed if the address (or address-range) does <code>not</code> match. </p>
<p> The following address types are supported:</p>
<dl>
<dt><i>number</i></p>
<dd> Match only the specified line <i>number</i> (which increments cumulatively across files, unless the <code>-s</code> option is specified on the command line).</p>
<dt><i>first</i>~<i>step</i></p>
<dd> Match every <i>step</i>&#8216;th line starting with line <i>first</i>. For example, &#8220;sed -n 1~2p&#8221; will print all the odd-numbered lines in the input stream, and the address 2~5 will match every fifth line, starting with the second. <i>first</i> can be zero; in this case, <i>sed</i> operates as if it were equal to <i>step</i>. (This is an extension.)</p>
<dt>$</p>
<dd> Match the last line.</p>
<dt>/<i>regexp</i>/</p>
<dd> Match lines matching the regular expression <i>regexp</i>. Matching is performed on the current pattern space, which can be modified with commands such as &#8220;s///&#8221;.</p>
<dt>
