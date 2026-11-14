---
title: "delp(1)"
name: "delp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-delp/"
description: "delp – The Free Pascal file deletion tool."
---

<h2>NAME</h2>
<p> delp &#8211; The Free Pascal file deletion tool. </p>
<h2>SYNOPSIS</h2>
<p> <code>delp [options] directory</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>delp</code> deletes files in the specified directory that are left over from a Free Pascal compilation process. It knows what files can be produced by the compile steps and deletes any such files it finds. At the end it gives a summary of the number of files that were deleted, together with the amount of bytes freed by this process. </p>
<h2>USAGE</h2>
<p> <code>delp </code> takes the following options at this time:</p>
<dl>
<dt><code>-e</code></p>
<dd> Delete all executable files as well. This option has no effect on Linux.</p>
<dt><code>-h </code></p>
<dd> Displays a short help message.</p>
<dt><code>-q</code></p>
<dd> Be more quiet. Normally, delp gives a count of the number of files deleted. If this option is given, no messages are displayed. </p>
</dl>
<h2>FILE TYPES:</h2>
<p> The following file types are recognized by the program and are deleted:</p>
<dl>
<dt><i>*.exe</i></p>
<dd> Executable files under dos and windows. Only deleted if the <i>-e</i> option is given.</p>
<dt><i>*.so *.dll</i></p>
<dd> Shared libraries under linux and Windows.</p>
<dt><i>*.tpu *.tpp *.tpw *.tr</i></p>
<dd> Turbo Pascal compiled units.</p>
<dt><i>*.log *.bak</i></p>
<dd> Backup files and log files.</p>
<dt><i>*.ppu *.o *.a *.s</i></p>
<dd> Compiled units, object files, archives and assembler files created by the Free Pascal compiler on Linux or Dos</p>
<dt><i>*.ppw *.ow *.aw *.sw</i></p>
<dd> Compiled units, object files, archives and assembler files created by the Free Pascal compiler on Windows.</p>
<dt><i>*.pp1 *.o1 *.a1 *.s1</i></p>
<dd> Compiled units, object files, archives and assembler files created by the Free Pascal compiler on the go321v1 platform.</p>
<dt><i>*.ppo *.oo *.ao *.so</i></p>
<dd> Compiled units, object files, archives and assembler files created by the Free Pascal compiler on the OS/2 platform.</p>
<dt><i>ppas.bat ppas.sh link.res fpcmaked</i></p>
<dd> Batch files, link script and makefile utility files.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-fpcmake/">fpcmake</a></code>(1) <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-make/">make</a></code>(1) </p>
</dl>
<h2>Index</h2>
