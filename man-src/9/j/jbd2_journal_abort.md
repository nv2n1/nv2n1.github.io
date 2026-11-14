---
title: "jbd2_journal_abort(9)"
name: "jbd2_journal_abort"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_abort/"
description: "jbd2_journal_abort – Shutdown the journal immediately."
---

<p>jbd2_journal_abort &#8211; Shutdown the journal immediately.</p>
<h2>Synopsis</h2>
<pre><code>void jbd2_journal_abort(journal_t *journal, int errno);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>the journal to shutdown.</dl>
<p> <i>errno</i></p>
<dl>
<dd>an error number to record in the journal indicating the reason for the shutdown.</dl>
<h2>Description</h2>
<p>Perform a complete, immediate shutdown of the ENTIRE journal (not of a single transaction). This operation cannot be undone without closing and reopening the journal. </p>
<p> The jbd2_journal_abort function is intended to support higher level error recovery mechanisms such as the ext2/ext3 remount-readonly error mode. </p>
<p> Journal abort has very specific semantics. Any existing dirty, unjournaled buffers in the main filesystem will still be written to disk by bdflush, but the journaling mechanism will be suspended immediately and no further transaction commits will be honoured. </p>
<p> Any dirty, journaled buffers will be written back to disk without hitting the journal. Atomicity cannot be guaranteed on an aborted filesystem, but we _do_ attempt to leave as much data as possible behind for fsck to use for cleanup. </p>
<p> Any attempt to get a new transaction handle on a journal which is in ABORT state will just result in an -EROFS error return. A jbd2_journal_stop on an existing handle will return -EIO if we have entered abort state during the update. </p>
<p> Recursive transactions are not disturbed by journal abort until the final jbd2_journal_stop, which will receive the -EIO error. </p>
<p> Finally, the jbd2_journal_abort call allows the caller to supply an errno which will be recorded (if possible) in the journal superblock. This allows a client to record failure conditions in the middle of a transaction without having to complete the transaction to record the failure to disk. ext3_error, for example, now uses this functionality. </p>
<p> Errors which originate from within the journaling layer will NOT supply an errno; a null errno implies that absolutely no further writes are done to the journal (unless there are any already in progress).</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
