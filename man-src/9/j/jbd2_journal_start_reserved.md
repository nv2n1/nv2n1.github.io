---
title: "jbd2_journal_start_reserved(9)"
name: "jbd2_journal_start_reserved"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_start_reserved/"
description: "jbd2_journal_start_reserved – start reserved handle"
---

<p>jbd2_journal_start_reserved &#8211; start reserved handle</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_start_reserved(handle_t *handle, unsigned int type, unsigned int line_no);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>handle to start</dl>
<p> <i>type</i></p>
<dl>
<dd>&#8212; undescribed &#8212;</dl>
<p> <i>line_no</i></p>
<dl>
<dd>&#8212; undescribed &#8212;</dl>
<h2>Description</h2>
<p>Start handle that has been previously reserved with <code>jbd2_journal_reserve</code>. This attaches <i>handle</i> to the running transaction (or creates one if there&#8217;s not transaction running). Unlike <code>jbd2_journal_start</code> this function cannot block on journal commit, checkpointing, or similar stuff. It can block on memory allocation or frozen journal though. </p>
<p> Return 0 on success, non-zero on error &#8211; handle is freed in that case.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
