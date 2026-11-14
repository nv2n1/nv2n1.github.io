---
title: "jbd2_journal_recover(9)"
name: "jbd2_journal_recover"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_recover/"
description: "jbd2_journal_recover – recovers a on-disk journal"
---

<p>jbd2_journal_recover &#8211; recovers a on-disk journal</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_recover(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>the journal to recover</dl>
<h2>Description</h2>
<p>The primary function for recovering the log contents when mounting a journaled device. </p>
<p> Recovery is done in three passes. In the first pass, we look for the end of the log. In the second, we assemble the list of revoke blocks. In the third and final pass, we replay any un-revoked blocks in the log.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
