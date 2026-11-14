---
title: "i686-pc-mingw32-readelf(1)"
name: "i686-pc-mingw32-readelf"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i686-pc-mingw32-readelf/"
description: "readelf – Displays information about ELF files."
---

<h2 class="name">NAME</h2>
<p> readelf &#8211; Displays information about ELF files. </p>
<h2>SYNOPSIS</h2>
<p> readelf [<code>-a</code>|<code>&#8211;all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-h</code>|<code>&#8211;file-header</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-l</code>|<code>&#8211;program-headers</code>|<code>&#8211;segments</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-S</code>|<code>&#8211;section-headers</code>|<code>&#8211;sections</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-g</code>|<code>&#8211;section-groups</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-t</code>|<code>&#8211;section-details</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-e</code>|<code>&#8211;headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-s</code>|<code>&#8211;syms</code>|<code>&#8211;symbols</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-n</code>|<code>&#8211;notes</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-r</code>|<code>&#8211;relocs</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-u</code>|<code>&#8211;unwind</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-d</code>|<code>&#8211;dynamic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version-info</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-A</code>|<code>&#8211;arch-specific</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-D</code>|<code>&#8211;use-dynamic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-x</code>&nbsp;<wbr>&lt;number or name&gt;|<code>&#8211;hex-dump=</code>&lt;number or name&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr>&lt;number or name&gt;|<code>&#8211;string-dump=</code>&lt;number or name&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-R</code>&nbsp;<wbr>&lt;number or name&gt;|<code>&#8211;relocated-dump=</code>&lt;number or name&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-c</code>|<code>&#8211;archive-index</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-w[lLiaprmfFsoR]</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;debug-dump</code>[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=loc,=Ranges]]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-I</code>|<code>-histogram</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-v</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-W</code>|<code>&#8211;wide</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-H</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr><i>elffile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>readelf</code> displays information about one or more <font SIZE="-1">ELF</font> format object files. The options control what particular information to display. </p>
<p> <i>elffile</i>&#8230; are the object files to be examined. 32-bit and 64-bit <font SIZE="-1">ELF</font> files are supported, as are archives containing <font SIZE="-1">ELF</font> files. </p>
<p> This program performs a similar function to <code>objdump</code> but it goes into more detail and it exists independently of the <font SIZE="-1">BFD</font> library, so if there is a bug in <font SIZE="-1">BFD</font> then readelf will not be affected.</p>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent. At least one option besides <code>-v</code> or <code>-H</code> must be given.</p>
<dl>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;all</code></p>
<dd> Equivalent to specifying <code>&#8211;file-header</code>, <code>&#8211;program-headers</code>, <code>&#8211;sections</code>, <code>&#8211;symbols</code>, <code>&#8211;relocs</code>, <code>&#8211;dynamic</code>, <code>&#8211;notes</code> and <code>&#8211;version-info</code>.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;file-header</code></p>
<dd> Displays the information contained in the <font SIZE="-1">ELF</font> header at the start of the file.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;program-headers</code></p>
<dd>
<dt><code>&#8211;segments</code></p>
<dd> Displays the information contained in the file&#8217;s segment headers, if it has any.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;sections</code></p>
<dd>
<dt><code>&#8211;section-headers</code></p>
<dd> Displays the information contained in the file&#8217;s section headers, if it has any.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;section-groups</code></p>
<dd> Displays the information contained in the file&#8217;s section groups, if it has any.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;section-details</code></p>
<dd> Displays the detailed section information. Implies <code>-S</code>.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;symbols</code></p>
<dd>
<dt><code>&#8211;syms</code></p>
<dd> Displays the entries in symbol table section of the file, if it has one.</p>
<dt><code>-e</code></p>
<dd>
<dt><code>&#8211;headers</code></p>
<dd> Display all the headers in the file. Equivalent to <code>-h -l -S</code>.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;notes</code></p>
<dd> Displays the contents of the <font SIZE="-1">NOTE</font> segments and/or sections, if any.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;relocs</code></p>
<dd> Displays the contents of the file&#8217;s relocation section, if it has one.</p>
<dt><code>-u</code></p>
<dd>
<dt><code>&#8211;unwind</code></p>
<dd> Displays the contents of the file&#8217;s unwind section, if it has one. Only the unwind sections for <font SIZE="-1">IA64</font> <font SIZE="-1">ELF</font> files are currently supported.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;dynamic</code></p>
<dd> Displays the contents of the file&#8217;s dynamic section, if it has one.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version-info</code></p>
<dd> Displays the contents of the version sections in the file, it they exist.</p>
<dt><code>-A</code></p>
<dd>
<dt><code>&#8211;arch-specific</code></p>
<dd> Displays architecture-specific information in the file, if there is any.</p>
<dt><code>-D</code></p>
<dd>
<dt><code>&#8211;use-dynamic</code></p>
<dd> When displaying symbols, this option makes <code>readelf</code> use the symbol table in the file&#8217;s dynamic section, rather than the one in the symbols section.</p>
<dt><code>-x &lt;number or name&gt;</code></p>
<dd>
<dt><code>&#8211;hex-dump=&lt;number or name&gt;</code></p>
<dd> Displays the contents of the indicated section as a hexadecimal bytes. A number identifies a particular section by index in the section table; any other string identifies all sections with that name in the object file.</p>
<dt><code>-R &lt;number or name&gt;</code></p>
<dd>
<dt><code>&#8211;relocated-dump=&lt;number or name&gt;</code></p>
<dd> Displays the contents of the indicated section as a hexadecimal bytes. A number identifies a particular section by index in the section table; any other string identifies all sections with that name in the object file. The contents of the section will be relocated before they are displayed.</p>
<dt><code>-p &lt;number or name&gt;</code></p>
<dd>
<dt><code>&#8211;string-dump=&lt;number or name&gt;</code></p>
<dd> Displays the contents of the indicated section as printable strings. A number identifies a particular section by index in the section table; any other string identifies all sections with that name in the object file.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;archive-index</code></p>
<dd> Displays the file symbol index infomation contained in the header part of binary archives. Performs the same function as the <code>t</code> command to <code>ar</code>, but without using the <font SIZE="-1">BFD</font> library.</p>
<dt><code>-w[lLiaprmfFsoR]</code></p>
<dd>
<dt><code>&#8211;debug-dump[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=loc,=Ranges]</code></p>
<dd> Displays the contents of the debug sections in the file, if any are present. If one of the optional letters or words follows the switch then only data found in those specific sections will be dumped. </p>
<p> Note: the <code>=decodedline</code> option will display the interpreted contents of a .debug_line section whereas the <code>=rawline</code> option dumps the contents in a raw format.</p>
<dt><code>-I</code></p>
<dd>
<dt><code>&#8211;histogram</code></p>
<dd> Display a histogram of bucket list lengths when displaying the contents of the symbol tables.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the version number of readelf.</p>
<dt><code>-W</code></p>
<dd>
<dt><code>&#8211;wide</code></p>
<dd> Don&#8217;t break output lines to fit into 80 columns. By default <code>readelf</code> breaks section header and segment listing lines for 64-bit <font SIZE="-1">ELF</font> files, so that they fit into 80 columns. This option causes <code>readelf</code> to print each section header resp. each segment one a single line, which is far more readable on terminals wider than 80 columns.</p>
<dt><code>-H</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Display the command line options understood by <code>readelf</code>.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-objdump/">objdump</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
