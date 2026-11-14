---
title: "jbd2_journal_invalidatepage(9)"
name: "jbd2_journal_invalidatepage"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_invalidatepage/"
description: "jbd2_journal_invalidatepage –"
---

<p>jbd2_journal_invalidatepage &#8211;</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_invalidatepage(journal_t *journal, struct page *page, unsigned int offset, unsigned int length);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>journal to use for flush&#8230;</dl>
<p> <i>page</i></p>
<dl>
<dd>page to flush</dl>
<p> <i>offset</i></p>
<dl>
<dd>start of the range to invalidate</dl>
<p> <i>length</i></p>
<dl>
<dd>length of the range to invalidate</dl>
<h2>Description</h2>
<p>Reap page buffers containing data after in the specified range in page. Can return -EBUSY if buffers are part of the committing transaction and the page is straddling i_size. Caller then has to wait for current commit and try again.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
