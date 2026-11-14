---
title: "mglview(1)"
name: "mglview"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mglview/"
description: "mglview – Execute MathGL scripts and show in an window"
---

<h2>NAME</h2>
<p> mglview &#8211; Execute MathGL scripts and show in an window</p>
<h2>SYNOPSIS</h2>
<p> <code>mglview</code> [parameters] scriptfile</p>
<h2>DESCRIPTION</h2>
<p> <code>mglview</code> reads MGL scripts from <i>scriptfile</i> to produce plots of specified functions or data. The program will create a GUI window showing the script result. You can use <code>&#8211;</code> as file name for reading script from standard input. Another option is using *.mgld files for quick viewing 3d pictures.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1 string</code></p>
<dd> Set <i>string</i> as argument $1 for script.</p>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>-9 string</code></p>
<dd> Set <i>string</i> as argument $9 for script.</p>
<dt><code>-L locname</code></p>
<dd> Set the locale to <i>locname.</i></p>
<dt><code>-h</code></p>
<dd> Print help message.</dl>
<h2>AUTHOR</h2>
<p> mglview was written by Alexey Balakin, <a rel="nofollow" href="http://mathgl.sourceforge.net/">http://mathgl.sourceforge.net/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mglconv/">mglconv</a></code>(1), <code><a href="/docs/linux/man/1-udav/">udav</a></code>(1), <code><a href="/docs/linux/man/5-mgl/">mgl</a></code>(5) </p>
<h2>Index</h2>
