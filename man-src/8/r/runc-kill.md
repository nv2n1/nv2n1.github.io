---
title: "runc-kill(8)"
name: "runc-kill"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-kill/"
description: "runc-kill – send a specified signal to container"
---

<p><code>runc-kill</code> &#8211; send a specified signal to container </p>
<h2>Synopsis</h2>
<p><code>runc kill</code> [<code>&#8211;all</code>|<code>-a</code>] <i>container-id</i> [<i>signal</i>] </p>
<h2>Description</h2>
<p>By default, <code>runc kill</code> sends <code>SIGTERM</code> to the container&#8217;s initial process only. A different signal can be specified either by its name (with or without the <code>SIG</code> prefix), or its numeric value. Use <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1) with <code>-l</code> option to list available signals. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;all</code>|<code>-a</code></p>
<dd>Send the signal to all processes inside the container. </p>
</dl>
<h2>Examples</h2>
<p>The following will send a <code>KILL</code> signal to the init process of the <code>ubuntu01</code> container:  </p>
<pre># runc kill ubuntu01 KILL</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-runc/">runc</a></code>(1). </p>
