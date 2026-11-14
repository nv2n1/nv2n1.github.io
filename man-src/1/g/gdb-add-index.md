---
title: "gdb-add-index(1)"
name: "gdb-add-index"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdb-add-index/"
description: "gdb-add-index – Add index files to speed up GDB"
---

<h2 class="name">NAME</h2>
<p> gdb-add-index &#8211; Add index files to speed up GDB </p>
<h2>SYNOPSIS</h2>
<p> gdb-add-index <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> When <font SIZE="-1">GDB</font> finds a symbol file, it scans the symbols in the file in order to construct an internal symbol table. This lets most <font SIZE="-1">GDB</font> operations work quickly&#8212;at the cost of a delay early on. For large programs, this delay can be quite lengthy, so <font SIZE="-1">GDB</font> provides a way to build an index, which speeds up startup. </p>
<p> To determine whether a file contains such an index, use the command <tt>&quot;readelf -S filename&quot;</tt>: the index is stored in a section named <tt>&quot;.gdb_index&quot;</tt>. The index file can only be produced on systems which use <font SIZE="-1">ELF</font> binaries and <font SIZE="-1">DWARF</font> debug information (i.e., sections named <tt>&quot;.debug_*&quot;</tt>). </p>
<p> <code>gdb-add-index</code> uses <font SIZE="-1">GDB</font> and <code>objdump</code> found in the <font SIZE="-1"><code>PATH</code></font> environment variable. If you want to use different versions of these programs, you can specify them through the <font SIZE="-1"><code>GDB</code></font> and <font SIZE="-1"><code>OBJDUMP</code></font> environment variables. </p>
<p> See more in the <font SIZE="-1">GDB</font> manual in node <tt>&quot;Index Files&quot;</tt> &#8212; shell command <tt>&quot;info -f gdb -n &quot;Index Files&quot;&quot;</tt>.</p>
<h2>OPTIONS</h2>
<h2>SEE ALSO</h2>
<p> The full documentation for <font SIZE="-1">GDB</font> is maintained as a Texinfo manual. If the <tt>&quot;info&quot;</tt> and <tt>&quot;gdb&quot;</tt> programs and <font SIZE="-1">GDB</font>&#8216;s Texinfo documentation are properly installed at your site, the command </p>
<pre>
        info gdb
</pre>
<p> should give you access to the complete manual. </p>
<p> <i>Using </i><font SIZE="-1"><i>GDB: A</i></font><i> Guide to the </i><font SIZE="-1"><i>GNU</i></font><i> Source-Level Debugger</i>, Richard M. Stallman and Roland H. Pesch, July 1991.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1988-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;Free Software&#8221; and &#8220;Free Software Needs Free Documentation&#8221;, with the Front-Cover Texts being &#8220;A <font SIZE="-1">GNU</font> Manual,&#8221; and with the Back-Cover Texts as in (a) below. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: &#8220;You are free to copy and modify this <font SIZE="-1">GNU</font> Manual. Buying copies from <font SIZE="-1">GNU</font> Press supports the <font SIZE="-1">FSF</font> in developing <font SIZE="-1">GNU</font> and promoting software freedom.&#8221; </p>
<h2>Index</h2>
