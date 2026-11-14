---
title: "rio_del_mport_pw_handler(9)"
name: "rio_del_mport_pw_handler"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_del_mport_pw_handler/"
description: "rio_del_mport_pw_handler – remove port-write message handler from the list of mport specific pw handlers"
---

<p>rio_del_mport_pw_handler &#8211; remove port-write message handler from the list of mport specific pw handlers</p>
<h2>Synopsis</h2>
<pre><code>int rio_del_mport_pw_handler(struct rio_mport *mport, void *context, int (*pwcback)(struct rio_mport *mport, void *context, union rio_pw_msg *msg, int step));</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>RIO master port to bind the portwrite callback</dl>
<p> <i>context</i></p>
<dl>
<dd>Registered handler specific context to pass on event</dl>
<p> <i>pwcback</i></p>
<dl>
<dd>Registered callback function</dl>
<h2>Description</h2>
<p>Returns 0 if the request has been satisfied.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
