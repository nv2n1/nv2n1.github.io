---
title: "cross-readelf(1)"
name: "cross-readelf"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cross-readelf/"
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
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;dyn-syms</code>]<br />
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
&nbsp;<wbr>&nbsp;<wbr>[<code>-z</code>|<code>&#8211;decompress</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-c</code>|<code>&#8211;archive-index</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-w[lLiaprmfFsoRt]</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;debug-dump</code>[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=loc,=Ranges,=pubtypes,=trace_info,=trace_abbrev,=trace_aranges,=gdb_index]]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;dwarf-depth=</code><i>n</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;dwarf-start=</code><i>n</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-I</code>|<code>&#8211;histogram</code>]<br />
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
<dt><code>-a</code></dt>
<dd>
</dd><dt><code>&#8211;all</code></dt>
<dd> Equivalent to specifying <code>&#8211;file-header</code>, <code>&#8211;program-headers</code>, <code>&#8211;sections</code>, <code>&#8211;symbols</code>, <code>&#8211;relocs</code>, <code>&#8211;dynamic</code>, <code>&#8211;notes</code> and <code>&#8211;version-info</code>.</dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;file-header</code></dt>
<dd> Displays the information contained in the <font SIZE="-1">ELF</font> header at the start of the file.</dd>
<dt><code>-l</code></dt>
<dd>
</dd><dt><code>&#8211;program-headers</code></dt>
<dd>
</dd><dt><code>&#8211;segments</code></dt>
<dd> Displays the information contained in the file&#8217;s segment headers, if it has any.</dd>
<dt><code>-S</code></dt>
<dd>
</dd><dt><code>&#8211;sections</code></dt>
<dd>
</dd><dt><code>&#8211;section-headers</code></dt>
<dd> Displays the information contained in the file&#8217;s section headers, if it has any.</dd>
<dt><code>-g</code></dt>
<dd>
</dd><dt><code>&#8211;section-groups</code></dt>
<dd> Displays the information contained in the file&#8217;s section groups, if it has any.</dd>
<dt><code>-t</code></dt>
<dd>
</dd><dt><code>&#8211;section-details</code></dt>
<dd> Displays the detailed section information. Implies <code>-S</code>.</dd>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>&#8211;symbols</code></dt>
<dd>
</dd><dt><code>&#8211;syms</code></dt>
<dd> Displays the entries in symbol table section of the file, if it has one.</dd>
<dt><code>&#8211;dyn-syms</code></dt>
<dd> Displays the entries in dynamic symbol table section of the file, if it has one.</dd>
<dt><code>-e</code></dt>
<dd>
</dd><dt><code>&#8211;headers</code></dt>
<dd> Display all the headers in the file. Equivalent to <code>-h -l -S</code>.</dd>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>&#8211;notes</code></dt>
<dd> Displays the contents of the <font SIZE="-1">NOTE</font> segments and/or sections, if any.</dd>
<dt><code>-r</code></dt>
<dd>
</dd><dt><code>&#8211;relocs</code></dt>
<dd> Displays the contents of the file&#8217;s relocation section, if it has one.</dd>
<dt><code>-u</code></dt>
<dd>
</dd><dt><code>&#8211;unwind</code></dt>
<dd> Displays the contents of the file&#8217;s unwind section, if it has one. Only the unwind sections for <font SIZE="-1">IA64 ELF</font> files, as well as <font SIZE="-1">ARM</font> unwind tables (<tt>&quot;.ARM.exidx&quot;</tt> / <tt>&quot;.ARM.extab&quot;</tt>) are currently supported.</dd>
<dt><code>-d</code></dt>
<dd>
</dd><dt><code>&#8211;dynamic</code></dt>
<dd> Displays the contents of the file&#8217;s dynamic section, if it has one.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version-info</code></dt>
<dd> Displays the contents of the version sections in the file, it they exist.</dd>
<dt><code>-A</code></dt>
<dd>
</dd><dt><code>&#8211;arch-specific</code></dt>
<dd> Displays architecture-specific information in the file, if there is any.</dd>
<dt><code>-D</code></dt>
<dd>
</dd><dt><code>&#8211;use-dynamic</code></dt>
<dd> When displaying symbols, this option makes <code>readelf</code> use the symbol hash tables in the file&#8217;s dynamic section, rather than the symbol table sections.</dd>
<dt><code>-x &lt;number or name&gt;</code></dt>
<dd>
</dd><dt><code>&#8211;hex-dump=&lt;number or name&gt;</code></dt>
<dd> Displays the contents of the indicated section as a hexadecimal bytes. A number identifies a particular section by index in the section table; any other string identifies all sections with that name in the object file.</dd>
<dt><code>-R &lt;number or name&gt;</code></dt>
<dd>
</dd><dt><code>&#8211;relocated-dump=&lt;number or name&gt;</code></dt>
<dd> Displays the contents of the indicated section as a hexadecimal bytes. A number identifies a particular section by index in the section table; any other string identifies all sections with that name in the object file. The contents of the section will be relocated before they are displayed.</dd>
<dt><code>-p &lt;number or name&gt;</code></dt>
<dd>
</dd><dt><code>&#8211;string-dump=&lt;number or name&gt;</code></dt>
<dd> Displays the contents of the indicated section as printable strings. A number identifies a particular section by index in the section table; any other string identifies all sections with that name in the object file.</dd>
<dt><code>-z</code></dt>
<dd>
</dd><dt><code>&#8211;decompress</code></dt>
<dd> Requests that the section(s) being dumped by <code>x</code>, <code>R</code> or <code>p</code> options are decompressed before being displayed. If the section(s) are not compressed then they are displayed as is.</dd>
<dt><code>-c</code></dt>
<dd>
</dd><dt><code>&#8211;archive-index</code></dt>
<dd> Displays the file symbol index information contained in the header part of binary archives. Performs the same function as the <code>t</code> command to <code>ar</code>, but without using the <font SIZE="-1">BFD</font> library.</dd>
<dt><code>-w[lLiaprmfFsoRt]</code></dt>
<dd>
</dd><dt><code>&#8211;debug-dump[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=loc,=Ranges,=pubtypes,=trace_info,=trace_abbrev,=trace_aranges,=gdb_index]</code></dt>
<dd> Displays the contents of the debug sections in the file, if any are present. If one of the optional letters or words follows the switch then only data found in those specific sections will be dumped. </dd>
<p> Note that there is no single letter option to display the content of trace sections or .gdb_index. </p>
<p> Note: the <code>=decodedline</code> option will display the interpreted contents of a .debug_line section whereas the <code>=rawline</code> option dumps the contents in a raw format. </p>
<p> Note: the <code>=frames-interp</code> option will display the interpreted contents of a .debug_frame section whereas the <code>=frames</code> option dumps the contents in a raw format. </p>
<p> Note: the output from the <code>=info</code> option can also be affected by the options <code>&#8211;dwarf-depth</code> and <code>&#8211;dwarf-start</code>.</p>
<dt><code>&#8211;dwarf-depth=</code><i>n</i></dt>
<dd> Limit the dump of the <tt>&quot;.debug_info&quot;</tt> section to <i>n</i> children. This is only useful with <code>&#8211;debug-dump=info</code>. The default is to print all DIEs; the special value 0 for <i>n</i> will also have this effect. </dd>
<p> With a non-zero value for <i>n</i>, DIEs at or deeper than <i>n</i> levels will not be printed. The range for <i>n</i> is zero-based.</p>
<dt><code>&#8211;dwarf-start=</code><i>n</i></dt>
<dd> Print only DIEs beginning with the <font SIZE="-1">DIE</font> numbered <i>n</i>. This is only useful with <code>&#8211;debug-dump=info</code>. </dd>
<p> If specified, this option will suppress printing of any header information and all DIEs before the <font SIZE="-1">DIE</font> numbered <i>n</i>. Only siblings and children of the specified <font SIZE="-1">DIE</font> will be printed. </p>
<p> This can be used in conjunction with <code>&#8211;dwarf-depth</code>.</p>
<dt><code>-I</code></dt>
<dd>
</dd><dt><code>&#8211;histogram</code></dt>
<dd> Display a histogram of bucket list lengths when displaying the contents of the symbol tables.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display the version number of readelf.</dd>
<dt><code>-W</code></dt>
<dd>
</dd><dt><code>&#8211;wide</code></dt>
<dd> Don&#8217;t break output lines to fit into 80 columns. By default <code>readelf</code> breaks section header and segment listing lines for 64-bit <font SIZE="-1">ELF</font> files, so that they fit into 80 columns. This option causes <code>readelf</code> to print each section header resp. each segment one a single line, which is far more readable on terminals wider than 80 columns.</dd>
<dt><code>-H</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd> Display the command line options understood by <code>readelf</code>.</dd>
<dt><code>@</code><i>file</i></dt>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </dd>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-objdump/">objdump</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2015 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
