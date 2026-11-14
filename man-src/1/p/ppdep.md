---
title: "ppdep(1)"
name: "ppdep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppdep/"
description: "ppdep – The FPC Pascal unit dependency tracking program."
---

<h2>NAME</h2>
<p> ppdep &#8211; The FPC Pascal unit dependency tracking program. </p>
<h2>SYNOPSIS</h2>
<p> <code>ppdep</code> [-DDefine] [-oFile] [-eext] [-V] [-h] [A[call]] file </p>
<h2>Description</h2>
<p> <code>ppdep</code> dumps the dependencies of a unit in a format that can be understood by GNU <code>make</code> writes these dependencies to standard output. It takes care of dependencies both in the interface and implementation section of the unit, and it can handle conditional defines. </p>
<h2>Usage</h2>
<p> You can invoke <code>ppdep</code> with as the only required argument the name of the file (program or unit) whose dependecies you wish to list. You don&#8217;t need to specify an extension, by default <code>.pp</code> is assumed. </p>
<h2>Options</h2>
<p> <code>ppdep</code> has several options, which are case insensitive: </p>
<dl>
<dt><code>-a</code><i>call</i></p>
<dd> This option tells <code>ppdep</code> to generate a compiler call for the makefile. The compiler call will be generated for each file that is found in the current directory. If you do no specify an explicit compiler call, <code>ppc386</code> is used.</p>
<dt><code>-d</code><i>keyword</i></p>
<dd> This option defines <code>keyword</code> that can be used to verify conditional defines. <code>ppdep</code> understands conditional defines, you should use this switch if the <i>uses</i> clause of the programs or units can contain conditional defines.</p>
<dt><code>-e</code><i>ext</i></p>
<dd> This allows you to specify a different extension for the unit files. By default, <code>.ppu</code> is assumed. This extension is written to the makefile.</p>
<dt><code>-f</code><i>[call]</i></p>
<dd> This option tells <code>ppdep</code> to generate a compiler call for the makefile. The compiler call will be generated only for the file that was specified on the <code>ppdep</code> command line. If you want to generate a compiler call for each file found, use the <i>-a</i> option. If you do no specify an explicit compiler call, <code>ppc386</code> is used.</p>
<dt><code>-h</code></p>
<dd> Shows a short help screen.</p>
<dt><code>-o</code><i>file</i></p>
<dd> This option allows you to specify a file to which the dependencies should be written. By default the dependencies are written to standard output. If you specify this option, the dependencies are written to <code>file</code> </p>
<p> instead.</p>
<dt><code>-v</code></p>
<dd> Writes some diagnostic messages. If you use this option, be sure to use <i>-o</i> as well, since the diagnostic messages will also be written to standard output. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) <code><a href="/docs/linux/man/1-make/">make</a></code>(1) </p>
</dl>
<h2>Index</h2>
