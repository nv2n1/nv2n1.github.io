---
title: "fc_host_post_event(9)"
name: "fc_host_post_event"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_host_post_event/"
description: "fc_host_post_event – called to post an even on an fc_host."
---

<p>fc_host_post_event &#8211; called to post an even on an fc_host.</p>
<h2>Synopsis</h2>
<pre><code>void fc_host_post_event(struct Scsi_Host *shost, u32 event_number, enum fc_host_event_code event_code, u32 event_data);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>host the event occurred on</dl>
<p> <i>event_number</i></p>
<dl>
<dd>fc event number obtained from <code>get_fc_event_number</code></dl>
<p> <i>event_code</i></p>
<dl>
<dd>fc_host event being posted</dl>
<p> <i>event_data</i></p>
<dl>
<dd>32bits of data for the event being posted</dl>
<h2>Notes</h2>
<p>This routine assumes no locks are held on entry.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
