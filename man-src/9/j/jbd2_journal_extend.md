---
title: "jbd2_journal_extend(9)"
name: "jbd2_journal_extend"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_extend/"
description: "jbd2_journal_extend – extend buffer credits."
---

<p>jbd2_journal_extend &#8211; extend buffer credits.</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_extend(handle_t *handle, int nblocks);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>handle to &#8216;extend&#8217;</dl>
<p> <i>nblocks</i></p>
<dl>
<dd>nr blocks to try to extend by.</dl>
<h2>Description</h2>
<p>Some transactions, such as large extends and truncates, can be done atomically all at once or in several stages. The operation requests a credit for a number of buffer modifications in advance, but can extend its credit if it needs more. </p>
<p> jbd2_journal_extend tries to give the running handle more buffer credits. It does not guarantee that allocation &#8211; this is a best-effort only. The calling process MUST be able to deal cleanly with a failure to extend here. </p>
<p> Return 0 on success, non-zero on failure. </p>
<p> return code &lt; 0 implies an error return code &gt; 0 implies normal transaction-full status.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
