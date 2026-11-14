---
title: "ppufiles(1)"
name: "ppufiles"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppufiles/"
description: "ppufiles – The FPC Pascal unit object file lister."
---

<h2>NAME</h2>
<p> ppufiles &#8211; The FPC Pascal unit object file lister. </p>
<h2>SYNOPSIS</h2>
<p> <code>ppufiles</code> [options] [file [file [file]]] </p>
<h2>Description</h2>
<p> <code>ppufiles</code> lists all the binary files that are needed to link a unit file. This includes any object files or libraries that must be linked in through some directive in the unit. </p>
<h2>Usage</h2>
<p> You can invoke <code>ppufiles</code> with as arguments the name of the units whose object files you wish to list. An extension must be given. This can be useful for creating a listing of all created object files and deleting them in a Makefile. </p>
<h2>Options</h2>
<p> <code>ppufiles</code> has several options, which are case insensitive: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-a</code></p>
<dd> This option tells <code>ppufiles</code> to list all files.</p>
<dt><code>-h </code></p>
<dd> Help screen.</p>
<dt><code>-l</code></p>
<dd> This option tells <code>ppufiles</code> to list only shared libraries.</p>
<dt><code>-o </code></p>
<dd> This option tells <code>ppufiles</code> to list only object files.</p>
<dt><code>-s </code></p>
<dd> This option tells <code>ppufiles</code> to list only static libraries.</dl>
</dl>
<h2>ERRORS</h2>
<p> In case the unit is in an older or unrecognised format, ppufiles will complain about that.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) <code><a href="/docs/linux/man/1-make/">make</a></code>(1) </p>
</dl>
<h2>Index</h2>
