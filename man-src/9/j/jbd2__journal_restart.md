---
title: "jbd2__journal_restart(9)"
name: "jbd2__journal_restart"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2__journal_restart/"
description: "jbd2__journal_restart – restart a handle ."
---

<p>jbd2__journal_restart &#8211; restart a handle .</p>
<h2>Synopsis</h2>
<pre><code>int jbd2__journal_restart(handle_t *handle, int nblocks, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>handle to restart</dl>
<p> <i>nblocks</i></p>
<dl>
<dd>nr credits requested</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>&#8212; undescribed &#8212;</dl>
<h2>Description</h2>
<p>Restart a handle for a multi-transaction filesystem operation. </p>
<p> If the <code>jbd2_journal_extend</code> call above fails to grant new buffer credits to a running handle, a call to jbd2_journal_restart will commit the handle&#8217;s transaction so far and reattach the handle to a new transaction capable of guaranteeing the requested number of credits. We preserve reserved handle if there&#8217;s any attached to the passed in handle.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
