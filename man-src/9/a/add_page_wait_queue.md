---
title: "add_page_wait_queue(9)"
name: "add_page_wait_queue"
section: "9"
letter: "a"
url: "/docs/linux/man/9-add_page_wait_queue/"
---

add_page_wait_queue - Add an arbitrary waiter to a page's wait queue

<h2>Synopsis</h2>

<pre><code>void add_page_wait_queue(struct page *page, wait_queue_t *waiter);</code></pre>

<h2>Arguments</h2>

<i>page</i>
<dl><dd><dd>Page defining the wait queue of interest</dl>
 

 <i>waiter</i>
<dl><dd>Waiter to add to the queue</dl>

<h2>Description</h2>

Add an arbitrary <i>waiter</i> to the wait queue for the nominated <i>page</i>.

<h2>Copyright</h2>


