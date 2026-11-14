---
title: "axctl(8)"
name: "axctl"
section: "8"
letter: "a"
url: "/docs/linux/man/8-axctl/"
description: "axctl – Configure/Kill running AX.25 connections."
---

<p>axctl &#8211; Configure/Kill running AX.25 connections.</p>
<h2>Synopsis</h2>
<p><code>axctl [-v] port dest src window|t1|t2|t3|n2|idle|paclen|kill [parm]</code></p>
<h2>Description</h2>
<p>The <code>axctl</code> command is designed to be a multi-function command that allows miscellaneous commands to be issued to the Linux AX.25 protocol layer for existing AX.25 connections. The connection is uniquely identified via the combination of port, destination callsign and source callsign, with that information the kernel is able to change the parameters, or abort the connection. </p>
<p> Many of the options are similar to those found in <code>axparms</code> and perform the same function. Only one parameter may be changed on each invokation of <code>axctl.</code></p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></p>
<dd>Displays the version number.</p>
<dt><code>window window</code></p>
<dd>Sets the window size for the AX.25 connection.</p>
<dt><code>t1 t1-timeout</code></p>
<dd>Sets the initial T1 timeout value for the AX.25 connection, the value is given in seconds.</p>
<dt><code>t2 t2-timeout</code></p>
<dd>Sets the T2 timeout value for the AX.25 connection, the value is given in seconds.</p>
<dt><code>t3 t3-timeout</code></p>
<dd>Sets the T3 timeout value for the AX.25 connected, the value is given in seconds.</p>
<dt><code>n2 n2-count</code></p>
<dd>Sets the maximum number of tries for the AX.25 connection.</p>
<dt><code>idle idle-timeout</code></p>
<dd>Sets the value for the idle timer for the AX.25 connection, the value is in minutes.</p>
<dt><code>paclen paclength</code></p>
<dd>Sets the maximum packet length that may be transmitted on the AX.25 connection.</p>
<dt><code>kill</code></p>
<dd>Will abort an existing AX.25 connection.</dl>
<h2>Files</h2>
<p>/etc/ax25/axports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/8-axparms/">axparms</a></code>(8), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5).</p>
<h2>Authors</h2>
<pre>Joerg Reuter DL1BKE &lt;jreuter [at] poboxes.com&gt;</pre>
