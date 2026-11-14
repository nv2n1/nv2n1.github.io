---
title: "meatclient(8)"
name: "meatclient"
section: "8"
letter: "m"
url: "/docs/linux/man/8-meatclient/"
description: "stonith – extensible interface for remotely powering down a node in the cluster"
---

<p>stonith &#8211; extensible interface for remotely powering down a node in the cluster</p>
<h2>Synopsis</h2>
<p><code>meatclinet</code> [ -c nodename ]</p>
<h2>Description</h2>
<p>meatclient is a program that confirms that a manual reset has been done when stonith needed an operator to power-cycle a node on it&#8217;s behalf.</p>
<h2>Options</h2>
<dl>
<dt><code>-c nodename:</code></p>
<dd>manual power reset has been done on the node.</dl>
<h2>See Also</h2>
<p>heartbeat (8) stonith (8)</p>
<h2>Authors</h2>
<pre>meatclient - Gregor Binder &lt;gbinder [at] sysfive.com&gt;
man page - Michael Moerz &lt;mikem [at] debian.org&gt;, Horms &lt;horms [at] vergenet.net&gt;</pre>
