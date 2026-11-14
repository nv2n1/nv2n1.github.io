---
title: "jbd2_journal_try_to_free_buffers(9)"
name: "jbd2_journal_try_to_free_buffers"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_try_to_free_buffers/"
description: "jbd2_journal_try_to_free_buffers – try to free page buffers."
---

<p>jbd2_journal_try_to_free_buffers &#8211; try to free page buffers.</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_try_to_free_buffers(journal_t *journal, struct page *page, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>journal for operation</dl>
<p> <i>page</i></p>
<dl>
<dd>to try and free</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>we use the mask to detect how hard should we try to release buffers. If __GFP_DIRECT_RECLAIM and __GFP_FS is set, we wait for commit code to release the buffers.</dl>
<h2>Description</h2>
<p>For all the buffers on this page, if they are fully written out ordered data, move them onto BUF_CLEAN so <code>try_to_free_buffers</code> can reap them. </p>
<p> This function returns non-zero if we wish <code>try_to_free_buffers</code> to be called. We do this if the page is releasable by <code>try_to_free_buffers</code>. We also do it if the page has locked or dirty buffers and the caller wants us to perform sync or async writeout. </p>
<p> This complicates JBD locking somewhat. We aren&#8217;t protected by the BKL here. We wish to remove the buffer from its committing or running transaction&#8217;s -&gt;t_datalist via __jbd2_journal_unfile_buffer. </p>
<p> This may *change* the value of transaction_t-&gt;t_datalist, so anyone who looks at t_datalist needs to lock against this function. </p>
<p> Even worse, someone may be doing a jbd2_journal_dirty_data on this buffer. So we need to lock against that. <code>jbd2_journal_dirty_data</code> will come out of the lock with the buffer dirty, which makes it ineligible for release here. </p>
<p> Who else is affected by this? hmm&#8230; Really the only contender is <code>do_get_write_access</code> &#8211; it could be looking at the buffer while <code>journal_try_to_free_buffer</code> is changing its state. But that cannot happen because we never reallocate freed data as metadata while the data is part of a transaction. Yes? </p>
<p> Return 0 on failure, 1 on success</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
