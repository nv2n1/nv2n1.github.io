---
title: "ppumove(1)"
name: "ppumove"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppumove/"
description: "ppdep – The FPC Pascal unit mover."
---

<h2>NAME</h2>
<p> ppdep &#8211; The FPC Pascal unit mover. </p>
<h2>SYNOPSIS</h2>
<p> <code>ppumove</code> [-sqbhw] [-o File] [-d path] [-e extension] files&#8230; </p>
<h2>Description</h2>
<p> <code>ppumove</code> collects one or several Free Pascal unit files and archives them in a static or shared library. </p>
<h2>Usage</h2>
<p> You can invoke <code>ppumove</code> with as the only required argument the name of the unit from which you want to make an archive. Specifying multiple files is also possible, they will be put in the same archive. </p>
<h2>Options</h2>
<p> <code>ppumove</code> has several options, which are case sensitive: </p>
<dl>
<dt><code>-b</code></p>
<dd> This option tells <code>ppumove</code> to write a shell script (a batch file on DOS) that performs the needed calls to <code>ar</code> and <code>ld</code>. The script will be called <code>pmove</code>, with an extension of <code>.sh</code> on Linux, and <code>.bat</code> on DOS. You can then call this script manually afterwards. </p>
<dt><code>-d</code><i> path</i></p>
<dd> This option tells <code>ppumove</code> where to generate the new unit files. By default, this is the same directory as where the files are found. If you specify as the output extension the same extension as the units you want to move, not specifying the destination directory may cause problems. </p>
<dt><code>-e</code><i> ext</i></p>
<dd> This option sets the extension of the new unit files to <code>ext</code>. By default <code>.ppl</code> is used. However, you can specify <code>.ppu</code> as the extension. If you do, be sure to use also the <i>-d</i> switch, or you will overwrite the old units. Note however, that the compiler will only look for extensions <code>.ppu</code> and <code>.ppl</code> when looking for units. </p>
<dt><code>-h</code></p>
<dd> Shows a short help screen. </p>
<dt><code>-o</code><i> file</i></p>
<dd> This option allows you to specify the name of the library to be generated. You <code>must</code> use this option if you specify more than one unit on the command-line. If you specified only one unit on the command-line, the generated library will have the unit name, with <code>lib</code> prepended (on Linux). You do not need to specify the <code>lib</code> part, this will be prepended automatically if needed. </p>
<dt><code>-q</code></p>
<dd> Tells <code>ppumove</code> to operate quietly. </p>
<dt><code>-s</code></p>
<dd> Tells <code>ppumove</code> to generate a static library. By default, a shared library is generated (except on DOS). </p>
<dt><code>-w</code></p>
<dd> Tells <code>ppumove</code> it should use the windows linker and archiver. Do not use this option on Linux. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-ppudep/">ppudep</a></code>(1) <code><a href="/docs/linux/man/1-ppudump/">ppudump</a></code>(1)</dl>
<h2>Index</h2>
