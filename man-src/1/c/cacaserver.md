---
title: "cacaserver(1)"
name: "cacaserver"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cacaserver/"
description: "cacaserver – telnet server for libcaca"
---

<h2>NAME</h2>
<p> cacaserver &#8211; telnet server for libcaca</p>
<h2>SYNOPSIS</h2>
<p> <code>cacaserver</code></p>
<h2>DESCRIPTION</h2>
<p> <code>cacaserver</code> reads libcaca animation files in its standard input and serves them as ANSI art on network port 51914. These animations can be created by any libcaca program by setting the <code>CACA_DRIVER</code> environment variable to <code>raw</code> and piping the program&#8217;s standard output to <code>cacaserver.</code> </p>
<p> Clients can then connect to port 51914 using <code>telnet</code> or <code>netcat</code> to see the output.</p>
<h2>EXAMPLE</h2>
<p> CACA_DRIVER=raw cacademo | cacaserver </p>
<p> telnet localhost 51914</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cacaplay/">cacaplay</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sam Hocevar &lt;sam [at] hocevar.net&gt;. </p>
<h2>Index</h2>
