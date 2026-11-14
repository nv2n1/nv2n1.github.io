---
title: "iscsi_destroy_session(9)"
name: "iscsi_destroy_session"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_destroy_session/"
description: "iscsi_destroy_session – destroy iscsi session"
---

<p>iscsi_destroy_session &#8211; destroy iscsi session</p>
<h2>Synopsis</h2>
<pre><code>int iscsi_destroy_session(struct iscsi_cls_session *session);</code></pre>
<h2>Arguments</h2>
<p><i>session</i></p>
<dl>
<dd>
<dd>iscsi_session</dl>
<h2>Description</h2>
<p>Can be called by a LLD or iscsi_transport. There must not be any running connections.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
