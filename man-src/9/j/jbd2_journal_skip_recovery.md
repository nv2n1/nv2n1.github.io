---
title: "jbd2_journal_skip_recovery(9)"
name: "jbd2_journal_skip_recovery"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_skip_recovery/"
description: "jbd2_journal_skip_recovery – Start journal and wipe exiting records"
---

<p>jbd2_journal_skip_recovery &#8211; Start journal and wipe exiting records</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_skip_recovery(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>journal to startup</dl>
<h2>Description</h2>
<p>Locate any valid recovery information from the journal and set up the journal structures in memory to ignore it (presumably because the caller has evidence that it is out of date). This function doesn&#8217;t appear to be exported.. </p>
<p> We perform one pass over the journal to allow us to tell the user how much recovery information is being erased, and to let us initialise the journal transaction sequence numbers to the next unused ID.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
