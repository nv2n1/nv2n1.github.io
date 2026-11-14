---
title: "iscsi_session_event(9)"
name: "iscsi_session_event"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_session_event/"
description: "iscsi_session_event – send session destr. completion event"
---

<p>iscsi_session_event &#8211; send session destr. completion event</p>
<h2>Synopsis</h2>
<pre><code>int iscsi_session_event(struct iscsi_cls_session *session, enum iscsi_uevent_e event);</code></pre>
<h2>Arguments</h2>
<p><i>session</i></p>
<dl>
<dd>
<dd>iscsi class session</dl>
<p> <i>event</i></p>
<dl>
<dd>type of event</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
