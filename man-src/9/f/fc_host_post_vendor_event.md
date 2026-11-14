---
title: "fc_host_post_vendor_event(9)"
name: "fc_host_post_vendor_event"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_host_post_vendor_event/"
description: "fc_host_post_vendor_event – called to post a vendor unique event on an fc_host"
---

<p>fc_host_post_vendor_event &#8211; called to post a vendor unique event on an fc_host</p>
<h2>Synopsis</h2>
<pre><code>void fc_host_post_vendor_event(struct Scsi_Host *shost, u32 event_number, u32 data_len, char *data_buf, u64 vendor_id);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>host the event occurred on</dl>
<p> <i>event_number</i></p>
<dl>
<dd>fc event number obtained from <code>get_fc_event_number</code></dl>
<p> <i>data_len</i></p>
<dl>
<dd>amount, in bytes, of vendor unique data</dl>
<p> <i>data_buf</i></p>
<dl>
<dd>pointer to vendor unique data</dl>
<p> <i>vendor_id</i></p>
<dl>
<dd>Vendor id</dl>
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
