---
title: "ndisasm(1)"
name: "ndisasm"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndisasm/"
description: "ndisasm – the Netwide Disassembler, an 80×86 binary file disassembler"
---

<h2 class="name">NAME</h2>
<p> ndisasm &#8211; the Netwide Disassembler, an 80&#215;86 binary file disassembler </p>
<h2>SYNOPSIS</h2>
<p> <code>ndisasm</code> [ <code>-o</code> origin ] [ <code>-s</code> sync-point [&#8230;]] [ <code>-a</code> | <code>-i</code> ] [ <code>-b</code> bits ] [ <code>-u</code> ] [ <code>-e</code> hdrlen ] [ <code>-p</code> vendor ] [ <code>-k</code> offset,length [&#8230;]] infile</p>
<h2>DESCRIPTION</h2>
<p> The <code>ndisasm</code> command generates a disassembly listing of the binary file infile and directs it to stdout.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Causes <code>ndisasm</code> to exit immediately, after giving a summary of its invocation options.</dl>
<p> <code>-r</code>|<code>-v</code></p>
<dl>
<dt>
<dd> Causes <code>ndisasm</code> to exit immediately, after displaying its version number.</dl>
<p> <code>-o</code> <i>origin</i></p>
<dl>
<dt>
<dd> Specifies the notional load address for the file. This option causes <code>ndisasm</code> to get the addresses it lists down the left hand margin, and the target addresses of PC-relative jumps and calls, right.</dl>
<p> <code>-s</code> <i>sync-point</i></p>
<dl>
<dt>
<dd> Manually specifies a synchronisation address, such that <code>ndisasm</code> will not output any machine instruction which encompasses bytes on both sides of the address. Hence the instruction which starts at that address will be correctly disassembled.</dl>
<p> <code>-e</code> <i>hdrlen</i></p>
<dl>
<dt>
<dd> Specifies a number of bytes to discard from the beginning of the file before starting disassembly. This does not count towards the calculation of the disassembly offset: the first <i>disassembled</i> instruction will be shown starting at the given load address.</dl>
<p> <code>-k</code> <i>offset,length</i></p>
<dl>
<dt>
<dd> Specifies that <i>length</i> bytes, starting from disassembly offset <i>offset</i>, should be skipped over without generating any output. The skipped bytes still count towards the calculation of the disassembly offset.</dl>
<p> <code>-a</code>|<code>-i</code></p>
<dl>
<dt>
<dd> Enables automatic (or intelligent) sync mode, in which <code>ndisasm</code> will attempt to guess where synchronisation should be performed, by means of examining the target addresses of the relative jumps and calls it disassembles.</dl>
<p> <code>-b</code> <i>bits</i></p>
<dl>
<dt>
<dd> Specifies 16-, 32- or 64-bit mode. The default is 16-bit mode.</dl>
<p> <code>-u</code></p>
<dl>
<dt>
<dd> Specifies 32-bit mode, more compactly than using &#8216;-b 32&#8217;.</dl>
<p> <code>-p</code> <i>vendor</i></p>
<dl>
<dt>
<dd> Prefers instructions as defined by <i>vendor</i> in case of a conflict. Known <i>vendor</i> names include <code>intel</code>, <code>amd</code>, <code>cyrix</code>, and <code>idt</code>. The default is <code>intel</code>.</dl>
<h2>RESTRICTIONS</h2>
<p> <code>ndisasm</code> only disassembles binary files: it has no understanding of the header information present in object or executable files. If you want to disassemble an object file, you should probably be using <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1). </p>
<p> Auto-sync mode won&#8217;t necessarily cure all your synchronisation problems: a sync marker can only be placed automatically if a jump or call instruction is found to refer to it <i>before</i> <code>ndisasm</code> actually disassembles that part of the code. Also, if spurious jumps or calls result from disassembling non-machine-code data, sync markers may get placed in strange places. Feel free to turn auto-sync off and go back to doing it manually if necessary.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1) </p>
<h2>Index</h2>
