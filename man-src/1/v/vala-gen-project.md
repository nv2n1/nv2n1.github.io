---
title: "vala-gen-project(1)"
name: "vala-gen-project"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vala-gen-project/"
description: "vala-gen-project – generate the and automake skeleton for your vala project"
---

<h2>NAME</h2>
<p> vala-gen-project &#8211; generate the and automake skeleton for your vala project</p>
<h2>SYNOPSIS</h2>
<p> <code>vala-gen-project</code> [OPTION&#8230;] [NAME]</p>
<h2>DESCRIPTION</h2>
<p> Vala project generator is a little gui or command line utility that creates an automake project skeletoni vala program. </p>
<p> It can be used without specifing a project name, so that a gtk+ gui will be presented or directly from the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-?, &#8211;help Show help options</p>
<dd>
<dt>-p, &#8211;projectdir=DIRECTORY Project directory</p>
<dd>
<dt>-t, &#8211;type=TYPE Project TYPE: gtk+, console</p>
<dd>
<dt>-l, &#8211;license=TYPE License TYPE: gpl2, gpl3, lgpl2, lgpl3</p>
<dd>
<dt>&#8211;version Display version number</p>
<dd>
<dt>-a, &#8211;author=NAME Author name</p>
<dd>
<dt>-e, &#8211;email=EMAIL Author email address</p>
<dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Create a gtk+ project with a gpl2 license and the name valatest</p>
<dd>
<p> <code>vala-gen-project </code> -t gtk+ -l gpl2 valatest</dl>
<h2>EXIT STATUS</h2>
<p> vala-gen-project returns a zero exist status if it succeed. Non zero is returned in case of failure.</p>
<h2>AUTHOR</h2>
<p> Andrea Del Signore (sejerpz (at) tin.it)</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-valac/">valac</a>(1) </p>
<h2>Index</h2>
