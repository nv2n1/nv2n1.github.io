---
title: "postw32(1)"
name: "postw32"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postw32/"
description: "postw32 – Free Pascal Windows 32-bit executable post processor."
---

<h2>NAME</h2>
<p> postw32 &#8211; Free Pascal Windows 32-bit executable post processor. </p>
<h2>SYNOPSIS</h2>
<p> <code>postw32 [-vh] [-m subsystem] [-i file] [-V version] [-s size]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>postw32</code> does some post-processing on a Windows 32 bit executable file or library. It can set the windows subsystem, stack size, and file version. </p>
<h2>USAGE</h2>
<p> <code>postw32</code> needs at least 2 options. One is the input filename (option <code>-i</code> ) and the other is one of the possible operations, with their arguments. </p>
<h2>OPTIONS</h2>
<p> takes the following options at this time:</p>
<dl>
<dt><code>-i file</code></p>
<dd> specifies the input file to process. This option is a short notation for the <code>&#8211;input</code> option.</p>
<dt><code>-h </code></p>
<dd> Displays a short help message. This option is a short notation for the <code>&#8211;help</code> option.</p>
<dt><code>-m subsystem</code></p>
<dd> Set the subsystem (the application type) to either or Note that a gui application which writes to the command-line will cause an error. This option is a short notation for the <code>&#8211;subsystem</code> option.</p>
<dt><code>-s size</code></p>
<dd> Set the stack size to <i>size</i> bytes. This option is a short notation for the <code>&#8211;stack </code> option.</p>
<dt><code>-v</code></p>
<dd> Be verbose about the operations that are performed. This option is a short notation for the <code>&#8211;verbose</code> option.</p>
<dt><code>-V M.N</code></p>
<dd> Set the version of the file to <i>M.N</i> , where <i>M</i> and <i>N</i> are 16 bit unsigned values. This option is a short notation for the <code>&#8211;version</code> option. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-fpc/">fpc</a></code>(1) <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) </p>
</dl>
<h2>Index</h2>
