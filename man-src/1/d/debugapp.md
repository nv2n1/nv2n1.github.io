---
title: "debugapp(1)"
name: "debugapp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debugapp/"
description: "debugapp – A wrapper for openapp."
---

<h2>NAME</h2>
<p> debugapp &#8211; A wrapper for openapp.</p>
<h2>SYNOPSIS</h2>
<p> <code>debugapp</code> [<code>&#8211;find</code>] [<code>&#8211;gdb=&#8230;</code>] <i>application</i> [<i>arguments&#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>debugapp</code> is a tool that helps you start or find applications by name in debugging mode. It acts as a wrapper around <code>openapp</code> , and calls openapp with the <code>&#8211;debug</code> option; we recommend using openapp directly. </p>
<p> By default gdb is used as the debugger, but this can be changed with the <code>&#8211;gdb=</code> option or through the <code>GDB</code> environment variable. </p>
<p> The <i>arguments</i> are the arguments passed to the application. </p>
<p> See the <code>openapp</code> (1) man-page for a complete description.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-openapp/">openapp</a>(1) </p>
<h2>HISTORY</h2>
<p> Work on <code>debugapp</code> started in October 1997 by Ovidiu Predescu &lt;ovidiu [at] net-community.com&gt;. In October 2006 Nicola Pero &lt;nicola.pero [at] meta-innovation.com&gt; merged it with openapp. </p>
<h2>AUTHORS</h2>
<p> This man page was written by Dennis Leeuw &lt;dleeuw [at] made-it.com&gt;. </p>
<h2>Index</h2>
