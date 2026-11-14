---
title: "readelf(1)"
name: "readelf"
section: "1"
letter: "r"
url: "/docs/linux/man/1-readelf/"
description: "readelf – display information about ELF files"
---

<h2 class="name">NAME</h2>
<p> readelf &#8211; display information about ELF files </p>
<h2>SYNOPSIS</h2>
<p> readelf [<code>-a</code>|<code>&#8211;all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-h</code>|<code>&#8211;file-header</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-l</code>|<code>&#8211;program-headers</code>|<code>&#8211;segments</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-S</code>|<code>&#8211;section-headers</code>|<code>&#8211;sections</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-g</code>|<code>&#8211;section-groups</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-t</code>|<code>&#8211;section-details</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-e</code>|<code>&#8211;headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-s</code>|<code>&#8211;syms</code>|<code>&#8211;symbols</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;dyn-syms</code>|<code>&#8211;lto-syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;sym-base=[0|8|10|16]</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;demangle</code><i>=style</i>|<code>&#8211;no-demangle</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;quiet</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;recurse-limit</code>|<code>&#8211;no-recurse-limit</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-U</code>&nbsp;<i>method</i>|<code>&#8211;unicode=</code><i>method</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-n</code>|<code>&#8211;notes</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-r</code>|<code>&#8211;relocs</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-u</code>|<code>&#8211;unwind</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-d</code>|<code>&#8211;dynamic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-V</code>|<code>&#8211;version-info</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-A</code>|<code>&#8211;arch-specific</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-D</code>|<code>&#8211;use-dynamic</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-L</code>|<code>&#8211;lint</code>|<code>&#8211;enable-checks</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-x</code>&nbsp;&lt;number or name&gt;|<code>&#8211;hex-dump=</code>&lt;number or name&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-p</code>&nbsp;&lt;number or name&gt;|<code>&#8211;string-dump=</code>&lt;number or name&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-R</code>&nbsp;&lt;number or name&gt;|<code>&#8211;relocated-dump=</code>&lt;number or name&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-z</code>|<code>&#8211;decompress</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-c</code>|<code>&#8211;archive-index</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-w[lLiaprmfFsoORtUuTgAck]</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;debug-dump</code>[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=str-offsets,=loc,=Ranges,=pubtypes,=trace_info,=trace_abbrev,=trace_aranges,=gdb_index,=addr,=cu_index,=links]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-wK</code>|<code>&#8211;debug-dump=follow-links</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-wN</code>|<code>&#8211;debug-dump=no-follow-links</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-P</code>|<code>&#8211;process-links</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;dwarf-depth=</code><i>n</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;dwarf-start=</code><i>n</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;ctf=</code><i>section</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;ctf-parent=</code><i>section</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;ctf-symbols=</code><i>section</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;ctf-strings=</code><i>section</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-I</code>|<code>&#8211;histogram</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-v</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-W</code>|<code>&#8211;wide</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-T</code>|<code>&#8211;silent-truncation</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-H</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>elffile</i>&#8230;</p>
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
<dd> Equivalent to specifying <code>&#8211;file-header</code>, <code>&#8211;program-headers</code>, <code>&#8211;sections</code>, <code>&#8211;symbols</code>, <code>&#8211;relocs</code>, <code>&#8211;dynamic</code>, <code>&#8211;notes</code>, <code>&#8211;version-info</code>, <code>&#8211;arch-specific</code>, <code>&#8211;unwind</code>, <code>&#8211;section-groups</code> and <code>&#8211;histogram</code>. </p>
<p> Note &#8211; this option does not enable <code>&#8211;use-dynamic</code> itself, so if that option is not present on the command line then dynamic symbols and dynamic relocs will not be displayed.</p>
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
<dt><code>&#8211;quiet</code></p>
<dd> Suppress &#8220;no symbols&#8221; diagnostic.</p>
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
<dd> Displays the entries in symbol table section of the file, if it has one. If a symbol has version information associated with it then this is displayed as well. The version string is displayed as a suffix to the symbol name, preceded by an @ character. For example <code>foo [at] VER_1</code>. If the version is the default version to be used when resolving unversioned references to the symbol then it is displayed as a suffix preceded by two @ characters. For example <code>foo@@VER_2</code>.</p>
<dt><code>&#8211;dyn-syms</code></p>
<dd> Displays the entries in dynamic symbol table section of the file, if it has one. The output format is the same as the format used by the <code>&#8211;syms</code> option.</p>
<dt><code>&#8211;lto-syms</code></p>
<dd> Displays the contents of any <font SIZE="-1">LTO</font> symbol tables in the file.</p>
<dt><code>&#8211;sym-base=[0|8|10|16]</code></p>
<dd> Forces the size field of the symbol table to use the given base. Any unrecognized options will be treated as <code>0</code>. <code>&#8211;sym-base=0</code> represents the default and legacy behaviour. This will output sizes as decimal for numbers less than 100000. For sizes 100000 and greater hexadecimal notation will be used with a 0x prefix. <code>&#8211;sym-base=8</code> will give the symbol sizes in octal. <code>&#8211;sym-base=10</code> will always give the symbol sizes in decimal. <code>&#8211;sym-base=16</code> will always give the symbol sizes in hexadecimal with a 0x prefix.</p>
<dt><code>-C</code></p>
<dd>
<dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></p>
<dd> Decode (<i>demangle</i>) low-level symbol names into user-level names. This makes C<font SIZE="-2">++</font> function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler.</p>
<dt><code>&#8211;no-demangle</code></p>
<dd> Do not demangle low-level symbol names. This is the default.</p>
<dt><code>&#8211;recurse-limit</code></p>
<dd>
<dt><code>&#8211;no-recurse-limit</code></p>
<dd>
<dt><code>&#8211;recursion-limit</code></p>
<dd>
<dt><code>&#8211;no-recursion-limit</code></p>
<dd> Enables or disables a limit on the amount of recursion performed whilst demangling strings. Since the name mangling formats allow for an infinite level of recursion it is possible to create strings whose decoding will exhaust the amount of stack space available on the host machine, triggering a memory fault. The limit tries to prevent this from happening by restricting recursion to 2048 levels of nesting. </p>
<p> The default is for this limit to be enabled, but disabling it may be necessary in order to demangle truly complicated names. Note however that if the recursion limit is disabled then stack exhaustion is possible and any bug reports about such an event will be rejected.</p>
<dt><code>-U</code> <i>[d|i|l|e|x|h]</i></p>
<dd>
<dt><code>&#8211;unicode=[default|invalid|locale|escape|hex|highlight]</code></p>
<dd> Controls the display of non-ASCII characters in identifier names. The default (<code>&#8211;unicode=locale</code> or <code>&#8211;unicode=default</code>) is to treat them as multibyte characters and display them in the current locale. All other versions of this option treat the bytes as <font SIZE="-1">UTF-8</font> encoded values and attempt to interpret them. If they cannot be interpreted or if the <code>&#8211;unicode=invalid</code> option is used then they are displayed as a sequence of hex bytes, encloses in curly parethesis characters. </p>
<p> Using the <code>&#8211;unicode=escape</code> option will display the characters as as unicode escape sequences (<i>
