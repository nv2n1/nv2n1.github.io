---
title: "plserver(1)"
name: "plserver"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plserver/"
description: "plserver – PLplot graphics server"
---

<h2>NAME</h2>
<p> plserver &#8211; PLplot graphics server</p>
<h2>SYNOPSIS</h2>
<p> <code>plserver </code> <i>[args]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>plserver</code>, command. </p>
<p> <code>plserver</code> is just a front-end to the pltkMain() function. Structured along the preferred lines for extended wish&#8217;es. It typically runs as a child process from the PLplot TK driver to render output. Can use either TK send or Tcl-DP RPC for communication, depending on how it is invoked. </p>
<p> Note that plserver can be used the same way as wish or dpwish, as it contains the functionality of each of these (except the -notk Tcl-DP command-line option is not supported).</p>
<h2>SEE ALSO</h2>
<p> See /usr/share/doc/plplot/plplot.ps.gz for more details.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Rafael Laboissiere &lt;rafael [at] debian.org&gt;. </p>
<h2>Index</h2>
