---
title: "wait_for_stable_page(9)"
name: "wait_for_stable_page"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wait_for_stable_page/"
---

wait_for_stable_page - wait for writeback to finish, if necessary.

<h2>Synopsis</h2>

<pre><code>void wait_for_stable_page(struct page *page);</code></pre>

<h2>Arguments</h2>

<i>page</i>
<dl><dd><dd>The page to wait on.</dl>

<h2>Description</h2>

This function determines if the given page is related to a backing device that requires page contents to be held stable during writeback. If so, then it will wait for any pending writeback to complete.

<h2>Copyright</h2>


