---
title: "runc-list(8)"
name: "runc-list"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-list/"
description: "runc-list – lists containers"
---

<p><code>runc-list</code> &#8211; lists containers </p>
<h2>Synopsis</h2>
<p><code>runc list</code> [<i>option</i> &#8230;] </p>
<h2>Description</h2>
<p>The <code>list</code> commands lists containers. Note that a global <code>&#8211;root</code> option can be specified to change the default root. For the description of <code>&#8211;root</code>, see <code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;format</code>|<code>-f</code> <code>table</code>|<code>json</code></p>
<dd>Specify the format. Default is <code>table</code>. The <code>json</code> format provides more details. </p>
<dt><code>&#8211;quiet</code>|<code>-q</code></p>
<dd>Only display container IDs. </p>
</dl>
<h2>Examples</h2>
<p>To list containers created with the default root:  </p>
<pre># runc list</pre>
</dl>
<p> To list containers in a human-readable JSON (with the help of <code><a href="/docs/linux/man/1-jq/">jq</a></code>(1) utility):  </p>
<pre># runc list -f json | jq</pre>
</dl>
<p> To list containers created with the root of <code>/tmp/myroot</code>:  </p>
<pre># runc --root /tmp/myroot</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
