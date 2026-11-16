---
title: "iscsi_create_conn(9)"
name: "iscsi_create_conn"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_create_conn/"
description: "iscsi_create_conn – create iscsi class connection"
---

<p>iscsi_create_conn &#8211; create iscsi class connection</p>
<h2>Synopsis</h2>
<pre><code>struct iscsi_cls_conn *iscsi_create_conn(struct iscsi_cls_session *session, int dd_size, uint32_t cid);</code></pre>
<h2>Arguments</h2>
<p><i>session</i></p>
<dl>
<dd>
</dd><dd>iscsi cls session</dd></dl>
<p> <i>dd_size</i></p>
<dl>
<dd>private driver data size</dd></dl>
<p> <i>cid</i></p>
<dl>
<dd>connection id</dd></dl>
<h2>Description</h2>
<p>This can be called from a LLD or iscsi_transport. The connection is child of the session so cid must be unique for all connections on the session. </p>
<p> Since we do not support MCS, cid will normally be zero. In some cases for software iscsi we could be trying to preallocate a connection struct in which case there could be two connection structs and cid would be non-zero.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
