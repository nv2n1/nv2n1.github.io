---
title: "ttx(1)"
name: "ttx"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttx/"
description: "ttx – tool for manipulating TrueType and OpenType fonts"
---

<h2>NAME</h2>
<p> <code>ttx</code> &#8211; tool for manipulating TrueType and OpenType fonts</p>
<h2>SYNOPSIS</h2>
<p> [<i>option &#8230;</i> ] <i>file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> is a tool for manipulating TrueType and OpenType fonts. It can convert TrueType and OpenType fonts to and from an <code>XML -based format called</code> <code>TTX</code> <code>TTX</code> files have a `.ttx&#8217; extension. </p>
<p> For each <i>file</i> argument it is given, detects whether it is a `.ttf&#8217; , `.otf&#8217; or `.ttx&#8217; file and acts accordingly: if it is a `.ttf&#8217; or `.otf&#8217; file, it generates a `.ttx&#8217; file; if it is a `.ttx&#8217; file, it generates a `.ttf&#8217; or `.otf&#8217; file. </p>
<p> By default, every output file is created in the same directory as the corresponding input file and with the same name except for the extension, which is substituted appropriately. never overwrites existing files; if necessary, it appends a suffix to the output file name before the extension, as in Arial#1.ttf</p>
<h3>General options</h3>
<dl>
<dt><code>-h</code></p>
<dd> Display usage information.</p>
<dt><code>-d </code><i>dir</i></p>
<dd> Write the output files to directory <i>dir</i> instead of writing every output file to the same directory as the corresponding input file.</p>
<dt><code>-o </code><i>file</i></p>
<dd> Write the output to <i>file</i> instead of writing it to the same directory as the corresponding input file.</p>
<dt><code>-v</code></p>
<dd> Be verbose. Write more messages to the standard output describing what is being done.</p>
<dt><code>-a</code></p>
<dd> Allow virtual glyphs ID&#8217;s on compile or decompile.</dl>
<h3>Dump options</h3>
<p> The following options control the process of dumping font files (TrueType or OpenType) to <code>TTX</code> files.</p>
<dl>
<dt><code>-l</code></p>
<dd> List table information. Instead of dumping the font to a <code>TTX</code> file, display minimal information about each table.</p>
<dt><code>-t </code><i>table</i></p>
<dd> Dump table <i>table</i> This option may be given multiple times to dump several tables at once. When not specified, all tables are dumped.</p>
<dt><code>-x </code><i>table</i></p>
<dd> Exclude table <i>table</i> from the list of tables to dump. This option may be given multiple times to exclude several tables from the dump. The &#8211;<code>t</code> and &#8211;<code>x</code> options are mutually exclusive.</p>
<dt><code>-s</code></p>
<dd> Split tables. Dump each table to a separate <code>TTX</code> file and write (under the name that would have been used for the output file if the &#8211;<code>s</code> option had not been given) one small <code>TTX</code> file containing references to the individual table dump files. This file can be used as input to as long as the referenced files can be found in the same directory.</p>
<dt><code>-i</code></p>
<dd> Don&#8217;t disassemble TrueType instructions. When this option is specified, all TrueType programs (glyph programs, the font program and the pre-program) are written to the <code>TTX</code> file as hexadecimal data instead of assembly. This saves some time and results in smaller <code>TTX</code> files.</p>
<dt><code>-y </code><i>n</i></p>
<dd> When decompiling a TrueType Collection (TTC) file, decompile font number <i>n</i> starting from 0.</dl>
<h3>Compilation options</h3>
<p> The following options control the process of compiling <code>TTX</code> files into font files (TrueType or OpenType):</p>
<dl>
<dt><code>-m </code><i>fontfile</i></p>
<dd> Merge the input <code>TTX</code> file <i>file</i> with <i>fontfile</i> No more than one <i>file</i> argument can be specified when this option is used.</p>
<dt><code>-b</code></p>
<dd> Don&#8217;t recalculate glyph bounding boxes. Use the values in the <code>TTX</code> file as is.</dl>
<h2>THE TTX FILE FORMAT</h2>
<p> You can find some information about the <code>TTX</code> file format in documentation.html In particular, you will find in that file the list of tables understood by and the relations between TrueType GlyphIDs and the glyph names used in <code>TTX</code> files.</p>
<h2>EXAMPLES</h2>
<p> In the following examples, all files are read from and written to the current directory. Additionally, the name given for the output file assumes in every case that it did not exist before was invoked. </p>
<p> Dump the TrueType font contained in FreeSans.ttf to FreeSans.ttx </p>
<blockquote><p><tt>ttx FreeSans.ttf</tt></p></blockquote>
<p> Compile MyFont.ttx into a TrueType or OpenType font file: </p>
<blockquote><p><tt>ttx MyFont.ttx</tt></p></blockquote>
<p> List the tables in FreeSans.ttf along with some information: </p>
<blockquote><p><tt>ttx -l FreeSans.ttf</tt></p></blockquote>
<p> Dump the `cmap&#8217; table from FreeSans.ttf to FreeSans.ttx </p>
<blockquote><p><tt>ttx -t cmap FreeSans.ttf</tt></p></blockquote>
<h2>NOTES</h2>
<p> On MS-Windows and MacOS, is available as a graphical application to which files can be dropped.</p>
<h2>SEE ALSO</h2>
<p> documentation.html </p>
<p> <a href="/docs/linux/man/1-fontforge/">fontforge</a>(1), <a href="/docs/linux/man/1-ftinfo/">ftinfo</a>(1), <a href="/docs/linux/man/1-gfontview/">gfontview</a>(1), <a href="/docs/linux/man/1-xmbdfed/">xmbdfed</a>(1), Font::TTF3pm</p>
<h2>AUTHORS</h2>
<p> was written by An -nosplit An Just van Rossum Aq just [at] letterror.com . </p>
<p> This manual page was written by An Florent Rougon Aq f.rougon [at] free.fr for the Debian GNU/Linux system based on the existing FontTools documentation. It may be freely used, modified and distributed without restrictions. </p>
<h2>Index</h2>
