---
title: "jbd2_journal_init_inode(9)"
name: "jbd2_journal_init_inode"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_init_inode/"
description: "jbd2_journal_init_inode – creates a journal which maps to a inode."
---

<p>jbd2_journal_init_inode &#8211; creates a journal which maps to a inode.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>journal_t * jbd2_journal_init_inode(struct inode&nbsp;<wbr>*&nbsp;<wbr></code><i>inode</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>An inode to create the journal in</dl>
<h2>Description</h2>
<p>jbd2_journal_init_inode creates a journal which maps an on-disk inode as the journal. The inode must exist already, must support <code>bmap</code> and must have all data blocks preallocated.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
