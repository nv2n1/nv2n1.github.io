---
title: "jbd2_journal_init_dev(9)"
name: "jbd2_journal_init_dev"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_init_dev/"
description: "jbd2_journal_init_dev – creates and initialises a journal structure"
---

<p>jbd2_journal_init_dev &#8211; creates and initialises a journal structure</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>journal_t * jbd2_journal_init_dev(struct block_device&nbsp;<wbr>*&nbsp;<wbr></code><i>bdev</i><code>, struct block_device&nbsp;<wbr>*&nbsp;<wbr></code><i>fs_dev</i><code>, unsigned long long&nbsp;<wbr></code><i>start</i><code>, int&nbsp;<wbr></code><i>len</i><code>, int&nbsp;<wbr></code><i>blocksize</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>Block device on which to create the journal</dl>
<p> <i>fs_dev</i></p>
<dl>
<dd>Device which hold journalled filesystem for this journal.</dl>
<p> <i>start</i></p>
<dl>
<dd>Block nr Start of journal.</dl>
<p> <i>len</i></p>
<dl>
<dd>Length of the journal in blocks.</dl>
<p> <i>blocksize</i></p>
<dl>
<dd>blocksize of journalling device</dl>
<h2>Return</h2>
<p>a newly created journal_t * </p>
<p> jbd2_journal_init_dev creates a journal which maps a fixed contiguous range of blocks on an arbitrary block device.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
