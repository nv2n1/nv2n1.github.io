---
title: "gdbinit(5)"
name: "gdbinit"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gdbinit/"
description: "gdbinit – GDB initialization scripts"
---

<p>gdbinit &#8211; GDB initialization scripts</p>
<h2>Synopsis</h2>
<p>/etc/gdb/gdbinit </p>
<p> /etc/gdb/gdbinit.d/* </p>
<p> ~/.config/gdb/gdbinit </p>
<p> ~/.gdbinit </p>
<p> ./.gdbinit</p>
<h2>Description</h2>
<p>These files contain <font SIZE="-1">GDB</font> commands to automatically execute during <font SIZE="-1">GDB</font> startup. The lines of contents are canned sequences of commands, described in the <font SIZE="-1">GDB</font> manual in node <tt>&quot;Sequences&quot;</tt> &#8212; shell command <tt>&quot;info -f gdb -n Sequences&quot;</tt>. </p>
<p> Please read more in the <font SIZE="-1">GDB</font> manual in node <tt>&quot;Startup&quot;</tt> &#8212; shell command <tt>&quot;info -f gdb -n Startup&quot;</tt>.</p>
<dl>
<dt><code>/etc/gdb/gdbinit</code></p>
<dd>System-wide initialization file. It is executed unless user specified <font SIZE="-1">GDB</font> option <tt>&quot;-nx&quot;</tt> or <tt>&quot;-n&quot;</tt>. See more in the <font SIZE="-1">GDB</font> manual in node <tt>&quot;System-wide configuration&quot;</tt> &#8212; shell command <tt>&quot;info -f gdb -n 'System-wide configuration'&quot;</tt>.</p>
<dt><code>/etc/gdb/gdbinit.d</code></p>
<dd>System-wide initialization directory. All files in this directory are executed on startup unless user specified <font SIZE="-1">GDB</font> option <tt>&quot;-nx&quot;</tt> or <tt>&quot;-n&quot;</tt>, as long as they have a recognized file extension. See more in the <font SIZE="-1">GDB</font> manual in node <tt>&quot;System-wide configuration&quot;</tt> &#8212; shell command <tt>&quot;info -f gdb -n 'System-wide configuration'&quot;</tt>.</p>
<dt>~/.config/gdb/gdbinit<code> or </code>~/.gdbinit</p>
<dd>User initialization file. It is executed unless user specified <font SIZE="-1">GDB</font> options <tt>&quot;-nx&quot;</tt>, <tt>&quot;-n&quot;</tt> or <tt>&quot;-nh&quot;</tt>.</p>
<dt>.gdbinit</p>
<dd>Initialization file for current directory. It may need to be enabled with <font SIZE="-1">GDB</font> security command <tt>&quot;set auto-load local-gdbinit&quot;</tt>. See more in the <font SIZE="-1">GDB</font> manual in node <tt>&quot;Init File in the Current Directory&quot;</tt> &#8212; shell command <tt>&quot;info -f gdb -n 'Init File in the Current Directory'&quot;</tt>.</dl>
<h2>Options</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <tt>&quot;info -f gdb -n Startup&quot;</tt> </p>
<p> The full documentation for <font SIZE="-1">GDB</font> is maintained as a Texinfo manual. If the <tt>&quot;info&quot;</tt> and <tt>&quot;gdb&quot;</tt> programs and <font SIZE="-1">GDB</font>&#8216;s Texinfo documentation are properly installed at your site, the command </p>
<pre> info gdb</pre>
<p>should give you access to the complete manual. </p>
<p> <i>Using </i><font SIZE="-1"><i>GDB: A</i></font><i> Guide to the </i><font SIZE="-1"><i>GNU</i></font><i> Source-Level Debugger</i>, Richard M. Stallman and Roland H. Pesch, July 1991.</p>
<h2>Copyright</h2>
<p>Copyright (c) 1988-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;Free Software&#8221; and &#8220;Free Software Needs Free Documentation&#8221;, with the Front-Cover Texts being &#8220;A <font SIZE="-1">GNU</font> Manual,&#8221; and with the Back-Cover Texts as in (a) below. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: &#8220;You are free to copy and modify this <font SIZE="-1">GNU</font> Manual. Buying copies from <font SIZE="-1">GNU</font> Press supports the <font SIZE="-1">FSF</font> in developing <font SIZE="-1">GNU</font> and promoting software freedom.&#8221;</p>
