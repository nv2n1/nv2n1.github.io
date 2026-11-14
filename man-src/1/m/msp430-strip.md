---
title: "msp430-strip(1)"
name: "msp430-strip"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msp430-strip/"
description: "strip – Discard symbols from object files."
---

<h2>NAME</h2>
<p> strip &#8211; Discard symbols from object files.</p>
<h2>SYNOPSIS</h2>
<p> strip [<code>-F</code> <i>bfdname</i> |<code>&#8211;target=</code><i>bfdname</i>]<br />
[<code>-I</code>&nbsp;<wbr><i>bfdname</i>&nbsp;<wbr>|<code>&#8211;input-target=</code><i>bfdname</i>]<br />
[<code>-O</code>&nbsp;<wbr><i>bfdname</i>&nbsp;<wbr>|<code>&#8211;output-target=</code><i>bfdname</i>]<br />
[<code>-s</code>|<code>&#8211;strip-all</code>]<br />
[<code>-S</code>|<code>-g</code>|<code>-d</code>|<code>&#8211;strip-debug</code>]<br />
[<code>-K</code>&nbsp;<wbr><i>symbolname</i>&nbsp;<wbr>|<code>&#8211;keep-symbol=</code><i>symbolname</i>]<br />
[<code>-N</code>&nbsp;<wbr><i>symbolname</i>&nbsp;<wbr>|<code>&#8211;strip-symbol=</code><i>symbolname</i>]<br />
[<code>-w</code>|<code>&#8211;wildcard</code>]<br />
[<code>-x</code>|<code>&#8211;discard-all</code>]&nbsp;<wbr>[<code>-X</code>&nbsp;<wbr>|<code>&#8211;discard-locals</code>]<br />
[<code>-R</code>&nbsp;<wbr><i>sectionname</i>&nbsp;<wbr>|<code>&#8211;remove-section=</code><i>sectionname</i>]<br />
[<code>-o</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>-p</code>|<code>&#8211;preserve-dates</code>]<br />
[<code>&#8211;keep-file-symbols</code>]<br />
[<code>&#8211;only-keep-debug</code>]<br />
[<code>-v</code>&nbsp;<wbr>|<code>&#8211;verbose</code>]&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
[<code>&#8211;help</code>]&nbsp;<wbr>[<code>&#8211;info</code>]<br />
<i>objfile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">GNU</font> <code>strip</code> discards all symbols from object files <i>objfile</i>. The list of object files may include archives. At least one object file must be given. </p>
<p> <code>strip</code> modifies the files named in its argument, rather than writing modified copies under different names.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;target=</code><i>bfdname</i></p>
<dd> Treat the original <i>objfile</i> as a file with the object code format <i>bfdname</i>, and rewrite it in the same format.</p>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of the options to <code>strip</code> and exit.</p>
<dt><code>&#8211;info</code></p>
<dd> Display a list showing all architectures and object formats available.</p>
<dt><code>-I</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;input-target=</code><i>bfdname</i></p>
<dd> Treat the original <i>objfile</i> as a file with the object code format <i>bfdname</i>.</p>
<dt><code>-O</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;output-target=</code><i>bfdname</i></p>
<dd> Replace <i>objfile</i> with a file in the output format <i>bfdname</i>.</p>
<dt><code>-R</code> <i>sectionname</i></p>
<dd>
<dt><code>&#8211;remove-section=</code><i>sectionname</i></p>
<dd> Remove any section named <i>sectionname</i> from the output file. This option may be given more than once. Note that using this option inappropriately may make the output file unusable.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;strip-all</code></p>
<dd> Remove all symbols.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>-S</code></p>
<dd>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;strip-debug</code></p>
<dd> Remove debugging symbols only.</p>
<dt><code>&#8211;strip-unneeded</code></p>
<dd> Remove all symbols that are not needed for relocation processing.</p>
<dt><code>-K</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;keep-symbol=</code><i>symbolname</i></p>
<dd> When stripping symbols, keep symbol <i>symbolname</i> even if it would normally be stripped. This option may be given more than once.</p>
<dt><code>-N</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;strip-symbol=</code><i>symbolname</i></p>
<dd> Remove symbol <i>symbolname</i> from the source file. This option may be given more than once, and may be combined with strip options other than <code>-K</code>.</p>
<dt><code>-o</code> <i>file</i></p>
<dd> Put the stripped output in <i>file</i>, rather than replacing the existing file. When this argument is used, only one <i>objfile</i> argument may be specified.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;preserve-dates</code></p>
<dd> Preserve the access and modification dates of the file.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;wildcard</code></p>
<dd> Permit regular expressions in <i>symbolname</i>s used in other command line options. The question mark (?), asterisk (*), backslash (\) and square brackets ([]) operators can be used anywhere in the symbol name. If the first character of the symbol name is the exclamation point (!) then the sense of the switch is reversed for that symbol. For example: </p>
<pre>
          -w -K !foo -K fo*
</pre>
<p> would cause strip to only keep symbols that start with the letters &#8220;fo&#8221;, but to discard the symbol &#8220;foo&#8221;.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;discard-all</code></p>
<dd> Remove non-global symbols.</p>
<dt><code>-X</code></p>
<dd>
<dt><code>&#8211;discard-locals</code></p>
<dd> Remove compiler-generated local symbols. (These usually start with <code>L</code> or <code>.</code>.)</p>
<dt><code>&#8211;keep-file-symbols</code></p>
<dd> When stripping a file, perhaps with <code>&#8211;strip-debug</code> or <code>&#8211;strip-unneeded</code>, retain any symbols specifying source file names, which would otherwise get stripped.</p>
<dt><code>&#8211;only-keep-debug</code></p>
<dd> Strip a file, removing contents of any sections that would not be stripped by <code>&#8211;strip-debug</code> and leaving the debugging sections intact. In <font SIZE="-1">ELF</font> files, this preserves all note sections in the output. </p>
<p> The intention is that this option will be used in conjunction with <code>&#8211;add-gnu-debuglink</code> to create a two part executable. One a stripped binary which will occupy less space in <font SIZE="-1">RAM</font> and in a distribution and the second a debugging information file which is only needed if debugging abilities are required. The suggested procedure to create these files is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.&lt;Link the executable as normal. Assuming that is is called&gt;</p>
<dd> <tt>&quot;foo&quot;</tt> then&#8230;</p>
<dt>1.&lt;Run objcopy &#8211;only-keep-debug foo foo.dbg to&gt;</p>
<dd> create a file containing the debugging info.</p>
<dt>1.&lt;Run objcopy &#8211;strip-debug foo to create a&gt;</p>
<dd> stripped executable.</p>
<dt>1.&lt;Run objcopy &#8211;add-gnu-debuglink=foo.dbg foo&gt;</p>
<dd> to add a link to the debugging info into the stripped executable.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note&#8212;the choice of <tt>&quot;.dbg&quot;</tt> as an extension for the debug info file is arbitrary. Also the <tt>&quot;--only-keep-debug&quot;</tt> step is optional. You could instead do this:</p>
<dl>
<dt>1.&lt;Link the executable as normal.&gt;</p>
<dd>
<dt>1.&lt;Copy foo to <tt>foo.full&gt;</p>
<dd>
<dt>1.&lt;Run strip --strip-debug foo&gt;</p>
<dd>
<dt>1.&lt;Run objcopy --add-gnu-debuglink=foo.full foo&gt;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> i.e., the file pointed to by the </tt><code>&#8211;add-gnu-debuglink</code> can be the full executable. It does not have to be a file created by the <code>&#8211;only-keep-debug</code> switch. </p>
<p> Note&#8212;this switch is only intended for use on fully linked files. It does not make sense to use it on object files where the debugging information may be incomplete. Besides the gnu_debuglink feature currently only supports the presence of one filename containing debugging information, not multiple filenames on a one-per-object-file basis.</dl>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Show the version number for <code>strip</code>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Verbose output: list all object files modified. In the case of archives, <code>strip -v</code> lists all members of the archive.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
