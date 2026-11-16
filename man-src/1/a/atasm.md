---
title: "atasm(1)"
name: "atasm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atasm/"
description: "atasm – assembler targeted for the 6502 CPU with Atari-specific features"
---

<h2>NAME</h2>
<p> atasm &#8211; assembler targeted for the 6502 CPU with Atari-specific features</p>
<h2>SYNOPSIS</h2>
<p> <code>atasm [</code><i>options</i><code>] </code><i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> <code>atasm</code> assembles 6502 code to an Atari DOS executable, an Atari XFD disk image, or a raw binary file. </p>
<p> The syntax used is compatible with the Atari 8-bit assembler MAC/65, with a few extensions (notably 6502 illegal opcode support)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code><i>filename</i></dt>
<dd> saves the object file to <i>filename</i> instead of <i>sourcefile</i> [.65o] </dd>
<dt><code>-D</code><i>symbol=value</i></dt>
<dd> Defines <i>symbol</i> to <i>value</i> before assembly begins. This is equivalent to inserting a line like <code>symbol=value</code> before the first line of the source file. </dd>
<dt><code>-I</code><i>directory</i></dt>
<dd> specifies a search directory for .INCLUDE directives </dd>
<dt><code>-v</code></dt>
<dd> prints assembly trace. </dd>
<dt><code>-s</code></dt>
<dd> prints symbol table when assembly is completed. </dd>
<dt><code>-u</code></dt>
<dd> enables undocumented opcodes. This is equivalent to using the <code>.OPT</code>ILL in the source file. Notice that this command-line paramter is overriden by any directives in the source files. </dd>
<dt><code>-m</code><i>filename</i></dt>
<dd> defines the template emulator state file. </dd>
<dt><code>-x</code><i>filename</i></dt>
<dd> saves object file to .XFD image <i>filename</i> </dd>
<dt><code>-r</code></dt>
<dd> saves object code as a raw binary image </dd>
<dt><code>-f</code><i>value</i></dt>
<dd> set the raw binary fill byte to <i>value</i> <code>te that if you specify this value in hex, it will probably need to be escaped.</code> </dd>
</dl>
<h2>NOTES</h2>
<p> This man page is nowhere near complete. For full documentation, see <code>%/usr/share/doc/atasm-1.07d%/atasm.txt</code> </p>
<h2>Index</h2>
