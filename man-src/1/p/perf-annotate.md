---
title: "perf-annotate(1)"
name: "perf-annotate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-annotate/"
description: "perf-annotate – Read perf.data (created by perf record) and display annotated code"
---

<h2 class="name">NAME</h2>
<p> perf-annotate &#8211; Read perf.data (created by perf record) and display annotated code </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf annotate[-i&lt;file&gt; | --input = file][symbol_name]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command reads the input file and displays an annotated version of the code. If the object file has debug symbols then the source code will be displayed alongside assembly code. </p>
<p> If there is no debug info in the object, then annotated assembly is displayed.</p>
<h2>OPTIONS</h2>
<p> -i, &#8211;input=</p>
<dl>
<dt>
<dd> Input file name. (default: perf.data unless stdin is a fifo)</dl>
<p> -d, &#8211;dsos=&lt;dso[,dso&#8230;]&gt;</p>
<dl>
<dt>
<dd> Only consider symbols in these dsos.</dl>
<p> -s, &#8211;symbol=&lt;symbol&gt;</p>
<dl>
<dt>
<dd> Symbol to annotate.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Don&#8217;t complain, do it.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose. (Show symbol address, etc)</dl>
<p> -D, &#8211;dump-raw-trace</p>
<dl>
<dt>
<dd> Dump raw trace in ASCII.</dl>
<p> -k, &#8211;vmlinux=&lt;file&gt;</p>
<dl>
<dt>
<dd> vmlinux pathname.</dl>
<p> -m, &#8211;modules</p>
<dl>
<dt>
<dd> Load module symbols. WARNING: use only with -k and LIVE kernel.</dl>
<p> -l, &#8211;print-line</p>
<dl>
<dt>
<dd> Print matching source lines (may be slow).</dl>
<p> -P, &#8211;full-paths</p>
<dl>
<dt>
<dd> Don&#8217;t shorten the displayed pathnames.</dl>
<p> &#8211;stdio</p>
<dl>
<dt>
<dd> Use the stdio interface.</dl>
<p> &#8211;tui</p>
<dl>
<dt>
<dd> Use the TUI interface. Use of &#8211;tui requires a tty, if one is not present, as when piping to other commands, the stdio interface is used. This interfaces starts by centering on the line with more samples, TAB/UNTAB cycles through the lines with more samples.</dl>
<p> &#8211;gtk</p>
<dl>
<dt>
<dd> Use the GTK interface.</dl>
<p> -C, &#8211;cpu</p>
<dl>
<dt>
<dd> Only report samples for the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. Default is to report samples on all CPUs.</dl>
<p> &#8211;asm-raw</p>
<dl>
<dt>
<dd> Show raw instruction encoding of assembly instructions.</dl>
<p> &#8211;source</p>
<dl>
<dt>
<dd> Interleave source code with assembly code. Enabled by default, disable with &#8211;no-source.</dl>
<p> &#8211;symfs=&lt;directory&gt;</p>
<dl>
<dt>
<dd> Look for files with symbols relative to this directory.</dl>
<p> -M, &#8211;disassembler-style=</p>
<dl>
<dt>
<dd> Set disassembler style for objdump.</dl>
<p> &#8211;objdump=&lt;path&gt;</p>
<dl>
<dt>
<dd> Path to objdump binary.</dl>
<p> &#8211;skip-missing</p>
<dl>
<dt>
<dd> Skip symbols that cannot be annotated.</dl>
<p> &#8211;group</p>
<dl>
<dt>
<dd> Show event group information together</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1) </p>
<h2>Index</h2>
