---
title: "jbd2_journal_set_triggers(9)"
name: "jbd2_journal_set_triggers"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_set_triggers/"
description: "jbd2_journal_set_triggers – Add triggers for commit writeout"
---

<p>jbd2_journal_set_triggers &#8211; Add triggers for commit writeout</p>
<h2>Synopsis</h2>
<pre><code>void jbd2_journal_set_triggers(struct buffer_head *bh, struct jbd2_buffer_trigger_type *type);</code></pre>
<h2>Arguments</h2>
<p><i>bh</i></p>
<dl>
<dd>
<dd>buffer to trigger on</dl>
<p> <i>type</i></p>
<dl>
<dd>struct jbd2_buffer_trigger_type containing the trigger(s).</dl>
<h2>Description</h2>
<p>Set any triggers on this journal_head. This is always safe, because triggers for a committing buffer will be saved off, and triggers for a running transaction will match the buffer in that transaction. </p>
<p> Call with NULL to clear the triggers.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
