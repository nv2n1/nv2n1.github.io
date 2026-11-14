---
title: "iscsi_destroy_conn(9)"
name: "iscsi_destroy_conn"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_destroy_conn/"
description: "iscsi_destroy_conn – destroy iscsi class connection"
---

<p>iscsi_destroy_conn &#8211; destroy iscsi class connection</p>
<h2>Synopsis</h2>
<pre><code>int iscsi_destroy_conn(struct iscsi_cls_conn *conn);</code></pre>
<h2>Arguments</h2>
<p><i>conn</i></p>
<dl>
<dd>
<dd>iscsi cls session</dl>
<h2>Description</h2>
<p>This can be called from a LLD or iscsi_transport.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
