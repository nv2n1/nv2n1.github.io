---
title: "runc-delete(8)"
name: "runc-delete"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-delete/"
description: "runc-delete – delete any resources held by the container"
---

<p><code>runc-delete</code> &#8211; delete any resources held by the container </p>
<h2>Synopsis</h2>
<p><code>runc delete</code> [<code>&#8211;force</code>|<code>-f</code>] <i>container-id</i> </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;force</code>|<code>-f</code></p>
<dd>Forcibly delete the running container, using <code>SIGKILL</code> <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) to stop it first. </p>
</dl>
<h2>Examples</h2>
<p>If the container id is <code>ubuntu01</code> and <code>runc list</code> currently shows its status as <code>stopped</code>, the following will delete resources held for <code>ubuntu01</code>, removing it from the <code>runc list</code>:  </p>
<pre># runc delete ubuntu01</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc-kill/">runc-kill</a></code>(8), <code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
