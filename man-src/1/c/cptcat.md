---
title: "cptcat(1)"
name: "cptcat"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cptcat/"
description: "cptcat – concatenate GMT colour palette tables."
---

<h2 class="name">NAME</h2>
<p> cptcat &#8211; concatenate GMT colour palette tables. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cptcat</code> [-h] [-o&nbsp;<wbr><i>file</i>] [-v] [-V] <i>file</i>&#8230;</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cptcat</code> utility concatenates two or more GMT colour palette table (cpt) files. The mandatory <i>file</i> arguments specify the input files which may be specified in any order. However, when sorted, the maximum (z-value) of the lower file should equal the minimum of the upper file; files can be modified with the <code><a href="/docs/linux/man/1-makecpt/">makecpt</a></code>(1) utility to be in this form. </p>
<p> The background colour will be taken from that of the lower (or lowest) file, and the forground from that of the upper. </p>
<p> The program will write to stdout if the <code>-o</code> option is not specified.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>EXAMPLES</h2>
<p> Create a cpt-file topobath.cpt from topo.cpt and bath.cpt </p>
<dl>
<dt>
<dd>
<pre>
  cptcat -v -o topobath.cpt topo.cpt bath.cpt
</pre>
</dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1), <code><a href="/docs/linux/man/1-makecpt/">makecpt</a></code>(1). </p>
<h2>Index</h2>
