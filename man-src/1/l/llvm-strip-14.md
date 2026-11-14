---
title: "llvm-strip-14(1)"
name: "llvm-strip-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-strip-14/"
description: "llvm-strip – object stripping tool"
---

<h2 class="name">NAME</h2>
<p> llvm-strip &#8211; object stripping tool </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-strip</code> [<i>options</i>] <i>inputs…</i></p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-strip</code> is a tool to strip sections and symbols from object files. If no other stripping or remove options are specified, <i>&#8211;strip-all</i> will be enabled. </p>
<p> By default, the input files are modified in-place. If “-” is specified for the input file, the input is read from the program’s standard input stream. </p>
<p> If the input is an archive, any requested operations will be applied to each archive member individually. </p>
<p> The tool is still in active development, but in most scenarios it works as a drop-in replacement for GNU’s <code>strip</code>.</p>
<h2>GENERIC AND CROSS-PLATFORM OPTIONS</h2>
<p> The following options are either agnostic of the file format, or apply to multiple file formats.</p>
<dl>
<dt><code>&#8211;disable-deterministic-archives, -U</code></p>
<dd> Use real values for UIDs, GIDs and timestamps when updating archive member headers.</p>
<dt><code>&#8211;discard-all, -x</code></p>
<dd> Remove most local symbols from the output. Different file formats may limit this to a subset of the local symbols. For example, file and section symbols in ELF objects will not be discarded. Additionally, remove all debug sections.</p>
<dt><code>&#8211;enable-deterministic-archives, -D</code></p>
<dd> Enable deterministic mode when stripping archives, i.e. use 0 for archive member header UIDs, GIDs and timestamp fields. On by default.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>&#8211;no-strip-all</code></p>
<dd> Disable <i>&#8211;strip-all</i>.</p>
<dt><code>-o &lt;file&gt;</code></p>
<dd> Write output to &lt;file&gt;. Multiple input files cannot be used in combination with -o.</p>
<dt><code>&#8211;regex</code></p>
<dd> If specified, symbol and section names specified by other switches are treated as extended POSIX regular expression patterns.</p>
<dt><code>&#8211;remove-section &lt;section&gt;, -R</code></p>
<dd> Remove the specified section from the output. Can be specified multiple times to remove multiple sections simultaneously.</p>
<dt><code>&#8211;strip-all-gnu</code></p>
<dd> Remove all symbols, debug sections and relocations from the output. This option is equivalent to GNU <code>strip</code>’s <code>&#8211;strip-all</code> switch.</p>
<dt><code>&#8211;strip-all, -s</code></p>
<dd> For ELF objects, remove from the output all symbols and non-alloc sections not within segments, except for .gnu.warning, .ARM.attribute sections and the section name table. </p>
<p> For COFF objects, remove all symbols, debug sections, and relocations from the output.</p>
<dt><code>&#8211;strip-debug, -d, -g, -S</code></p>
<dd> Remove all debug sections from the output.</p>
<dt><code>&#8211;strip-symbol &lt;symbol&gt;, -N</code></p>
<dd> Remove all symbols named <code>&lt;symbol&gt;</code> from the output. Can be specified multiple times to remove multiple symbols.</p>
<dt><code>&#8211;strip-unneeded</code></p>
<dd> Remove from the output all local or undefined symbols that are not required by relocations. Also remove all debug sections.</p>
<dt><code>&#8211;version, -V</code></p>
<dd> Display the version of the <code>llvm-strip</code> executable.</p>
<dt><code>&#8211;wildcard, -w</code></p>
<dd> Allow wildcard syntax for symbol-related flags. On by default for section-related flags. Incompatible with –regex. </p>
<p> Wildcard syntax allows the following special symbols: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Character </td>
<td> Meaning </td>
<td> Equivalent
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>*</code> </td>
<td> Any number of characters </td>
<td> <code>.*</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>?</code> </td>
<td> Any single character </td>
<td> <code>.</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>\</code> </td>
<td> Escape the next character </td>
<td> <code>\</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>[a-z]</code> </td>
<td> Character class </td>
<td> <code>[a-z]</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>[!a-z]</code>, <code>[^a-z]</code> </td>
<td> Negated character class </td>
<td> <code>[^a-z]</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Additionally, starting a wildcard with ‘!’ will prevent a match, even if another flag matches. For example <code>-w -N &#8216;*&#8217; -N &#8216;!x&#8217;</code> will strip all symbols except for <code>x</code>. </p>
<p> The order of wildcards does not matter. For example, <code>-w -N &#8216;*&#8217; -N &#8216;!x&#8217;</code> is the same as <code>-w -N &#8216;!x&#8217; -N &#8216;*&#8217;</code>.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options and commands from response file <i>&lt;FILE&gt;</i>.</dl>
<h2>COFF-SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for COFF objects. If used with other objects, <code>llvm-strip</code> will either emit an error or silently ignore them.</p>
<dl>
<dt><code>&#8211;only-keep-debug</code></p>
<dd> Remove the contents of non-debug sections from the output, but keep the section headers.</dl>
<h2>ELF-SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for ELF objects. If used with other objects, <code>llvm-strip</code> will either emit an error or silently ignore them.</p>
<dl>
<dt><code>&#8211;allow-broken-links</code></p>
<dd> Allow <code>llvm-strip</code> to remove sections even if it would leave invalid section references. Any invalid sh_link fields will be set to zero.</p>
<dt><code>&#8211;discard-locals, -X</code></p>
<dd> Remove local symbols starting with “.L” from the output.</p>
<dt><code>&#8211;keep-file-symbols</code></p>
<dd> Keep symbols of type <i>STT_FILE</i>, even if they would otherwise be stripped.</p>
<dt><code>&#8211;keep-section &lt;section&gt;</code></p>
<dd> When removing sections from the output, do not remove sections named <code>&lt;section&gt;</code>. Can be specified multiple times to keep multiple sections.</p>
<dt><code>&#8211;keep-symbol &lt;symbol&gt;, -K</code></p>
<dd> When removing symbols from the output, do not remove symbols named <code>&lt;symbol&gt;</code>. Can be specified multiple times to keep multiple symbols.</p>
<dt><code>&#8211;preserve-dates, -p</code></p>
<dd> Preserve access and modification timestamps in the output.</p>
<dt><code>&#8211;strip-sections</code></p>
<dd> Remove from the output all section headers and all section data not within segments. Note that many tools will not be able to use an object without section headers.</p>
<dt><code>-T</code></p>
<dd> Remove Swift symbols.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-strip</code> exits with a non-zero exit code if there is an error. Otherwise, it exits with code 0.</p>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/labels/tools:llvm-objcopy%2Fstrip">https://github.com/llvm/llvm-project/labels/tools:llvm-objcopy%2Fstrip</a></i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-objcopy/">llvm-objcopy</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
