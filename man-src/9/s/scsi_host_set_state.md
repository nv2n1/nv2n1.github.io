---
title: "scsi_host_set_state(9)"
name: "scsi_host_set_state"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_host_set_state/"
description: "scsi_host_set_state – Take the given host through the host state model."
---

<p>scsi_host_set_state &#8211; Take the given host through the host state model.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_host_set_state(struct Scsi_Host *shost, enum scsi_host_state state);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>scsi host to change the state of.</dl>
<p> <i>state</i></p>
<dl>
<dd>state to change to.</dl>
<h2>Description</h2>
<p>Returns zero if unsuccessful or an error if the requested transition is illegal.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
