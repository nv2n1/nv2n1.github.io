---
title: "scsi_target_reap_ref_release(9)"
name: "scsi_target_reap_ref_release"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_target_reap_ref_release/"
description: "scsi_target_reap_ref_release – remove target from visibility"
---

<p>scsi_target_reap_ref_release &#8211; remove target from visibility</p>
<h2>Synopsis</h2>
<pre><code>void scsi_target_reap_ref_release(struct kref *kref);</code></pre>
<h2>Arguments</h2>
<p><i>kref</i></p>
<dl>
<dd>
<dd>the reap_ref in the target being released</dl>
<h2>Description</h2>
<p>Called on last put of reap_ref, which is the indication that no device under this target is visible anymore, so render the target invisible in sysfs. Note: we have to be in user context here because the target reaps should be done in places where the scsi device visibility is being removed.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
