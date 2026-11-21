---

title: "llvm-size-10(1)"
name: "llvm-size-10"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-size-10/"
description: "llvm-size – manual page for llvm-size 10"
---

<p> OVERVIEW: llvm object size dumper </p>
<p> USAGE: llvm-size [options] &lt;input files&gt; </p>
<p> OPTIONS: </p>
<p> Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</dt>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</dt>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dt></dl>
<dd>llvm-size Options:</dd>
<dl>
<dt>
</dt><dd> Specify output format</dd>
<dt> <code>-A</code> &#8211; System V format</dt>
<dt> <code>-B</code> &#8211; Berkeley format</dt>
<dt> <code>-m</code> &#8211; Darwin <code>-m</code> format</dt>
<dt> <code>&#8211;arch=</code>&lt;string&gt; &#8211; architecture(s) from a Mach-O file to dump</dt>
<dt><code>&#8211;common</code> &#8211; Print common symbols in the ELF file.</dt>
<dd>
</dd><dd>When using Berkeley format, this is added to bss.</dd>
<dt> <code>&#8211;format=</code>&lt;value&gt; &#8211; Specify output format</dt>
<dt>=sysv</dt>
<dd> &#8211; System V format</dd>
<dt>=berkeley</dt>
<dd> &#8211; Berkeley format</dd>
<dt>=darwin</dt>
<dd> &#8211; Darwin <code>-m</code> format</dd>
<dt> <code>-l</code> &#8211; When format is darwin, use long format to include addresses and offsets.</dt>
<dt> <code>&#8211;radix=</code>&lt;value&gt; &#8211; Print size in radix</dt>
<dt>=8</dt>
<dd> &#8211; Print size in octal</dd>
<dt>=10</dt>
<dd> &#8211; Print size in decimal</dd>
<dt>=16</dt>
<dd> &#8211; Print size in hexadecimal</dd>
<dt> <code>&#8211;totals</code> &#8211; Print totals of all objects &#8211; Berkeley format only</dt>
<dd>Print size in radix:</dd>
<dt> <code>-o</code> &#8211; Print size in octal</dt>
<dt> <code>-d</code> &#8211; Print size in decimal</dt>
<dt> <code>-x</code> &#8211; Print size in hexadecimal</dt></dl>
<dd>Pass @FILE as argument to read options from FILE. </dd>
