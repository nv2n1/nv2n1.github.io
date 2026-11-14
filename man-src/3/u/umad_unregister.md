---
title: "umad_unregister(3)"
name: "umad_unregister"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_unregister/"
description: "umad_unregister – unregister umad agent"
---

<p>umad_unregister &#8211; unregister umad agent</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_unregister(int portid, int agentid);</code></pre>
<h2>Description</h2>
<p><code>umad_unregister()</code> unregisters the specified <i>agentid</i> previously registered using <code>umad_register()</code> or <code>umad_register_oui()</code>.</p>
<h2>Return Value</h2>
<p><code>umad_unregister()</code> returns 0 on success and negative value on error as follows:<br />
&nbsp;<wbr>-EINVAL invalid port handle or agentid<br />
&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(kernel error codes)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_register/">umad_register</a></code>(3), <code><a href="/docs/linux/man/3-umad_register_oui/">umad_register_oui</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
