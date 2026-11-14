---
title: "unlock_page(9)"
name: "unlock_page"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unlock_page/"
description: "unlock_page – unlock a locked page"
---

<p>unlock_page &#8211; unlock a locked page</p>
<h2>Synopsis</h2>
<pre><code>void unlock_page(struct page *page);</code></pre>
<h2>Arguments</h2>
<p><i>page</i></p>
<dl>
<dd>
<dd>the page</dl>
<h2>Description</h2>
<p>Unlocks the page and wakes up sleepers in <code>___wait_on_page_locked</code>. Also wakes sleepers in <code>wait_on_page_writeback</code> because the wakeup mechanism between PageLocked pages and PageWriteback pages is shared. But that&#8217;s OK &#8211; sleepers in <code>wait_on_page_writeback</code> just go back to sleep. </p>
<p> The mb is necessary to enforce ordering between the clear_bit and the read of the waitqueue (to avoid SMP races with a parallel <code>wait_on_page_locked</code>).</p>
<h2>Copyright</h2>
