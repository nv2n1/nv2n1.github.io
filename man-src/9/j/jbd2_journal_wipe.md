---
title: "jbd2_journal_wipe(9)"
name: "jbd2_journal_wipe"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_wipe/"
description: "jbd2_journal_wipe – Wipe journal contents"
---

<p>jbd2_journal_wipe &#8211; Wipe journal contents</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_wipe(journal_t *journal, int write);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>Journal to act on.</dl>
<p> <i>write</i></p>
<dl>
<dd>flag (see below)</dl>
<h2>Description</h2>
<p>Wipe out all of the contents of a journal, safely. This will produce a warning if the journal contains any valid recovery information. Must be called between journal_init_*() and <code>jbd2_journal_load</code>. </p>
<p> If &#8216;write&#8217; is non-zero, then we wipe out the journal on disk; otherwise we merely suppress recovery.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
