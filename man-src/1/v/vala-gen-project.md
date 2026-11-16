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
<dt>-?, &#8211;help Show help options</dt>
<dd>
</dd><dt>-p, &#8211;projectdir=DIRECTORY Project directory</dt>
<dd>
</dd><dt>-t, &#8211;type=TYPE Project TYPE: gtk+, console</dt>
<dd>
</dd><dt>-l, &#8211;license=TYPE License TYPE: gpl2, gpl3, lgpl2, lgpl3</dt>
<dd>
</dd><dt>&#8211;version Display version number</dt>
<dd>
</dd><dt>-a, &#8211;author=NAME Author name</dt>
<dd>
</dd><dt>-e, &#8211;email=EMAIL Author email address</dt>
<dd></dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Create a gtk+ project with a gpl2 license and the name valatest</dt>
<dd>
<p> <code>vala-gen-project </code> -t gtk+ -l gpl2 valatest</dd></dl>
<h2>EXIT STATUS</h2>
<p> vala-gen-project returns a zero exist status if it succeed. Non zero is returned in case of failure.</p>
<h2>AUTHOR</h2>
<p> Andrea Del Signore (sejerpz (at) tin.it)</p>
<h2>SEE ALSO</h2>
<p> valac(1) </p>
<h2>Index</h2>
</p>