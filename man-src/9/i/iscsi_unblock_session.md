---
title: "iscsi_unblock_session(9)"
name: "iscsi_unblock_session"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_unblock_session/"
description: "iscsi_unblock_session – set a session as logged in and start IO."
---

<p>iscsi_unblock_session &#8211; set a session as logged in and start IO.</p>
<h2>Synopsis</h2>
<pre><code>void iscsi_unblock_session(struct iscsi_cls_session *session);</code></pre>
<h2>Arguments</h2>
<p><i>session</i></p>
<dl>
<dd>
<dd>iscsi session</dl>
<h2>Description</h2>
<p>Mark a session as ready to accept IO.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
