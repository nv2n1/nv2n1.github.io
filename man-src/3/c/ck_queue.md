---
title: "ck_queue(3)"
name: "ck_queue"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_queue/"
description: "CK_LIST_EMPTY CK_LIST_ENTRY CK_LIST_FIRST CK_LIST_FOREACH CK_LIST_FOREACH_SAFE CK_LIST_HEAD CK_LIST_HEAD_INITIALIZER CK_LIST_INIT CK_LIST_INSERT_AFTER CK_LIST_INSERT_BEFORE CK_LIST_INSERT_HEAD CK_L..."
---

<h2>NAME</h2>
<p> <code>CK_LIST_EMPTY</code> <code>CK_LIST_ENTRY</code> <code>CK_LIST_FIRST</code> <code>CK_LIST_FOREACH</code> <code>CK_LIST_FOREACH_SAFE</code> <code>CK_LIST_HEAD</code> <code>CK_LIST_HEAD_INITIALIZER</code> <code>CK_LIST_INIT</code> <code>CK_LIST_INSERT_AFTER</code> <code>CK_LIST_INSERT_BEFORE</code> <code>CK_LIST_INSERT_HEAD</code> <code>CK_LIST_MOVE</code> <code>CK_LIST_NEXT</code> <code>CK_LIST_REMOVE</code> <code>CK_LIST_SWAP</code> <code>CK_SLIST_EMPTY</code> <code>CK_SLIST_ENTRY</code> <code>CK_SLIST_FIRST</code> <code>CK_SLIST_FOREACH</code> <code>CK_SLIST_FOREACH_PREVPTR</code> <code>CK_SLIST_FOREACH_SAFE</code> <code>CK_SLIST_HEAD</code> <code>CK_SLIST_HEAD_INITIALIZER</code> <code>CK_SLIST_INIT</code> <code>CK_SLIST_INSERT_AFTER</code> <code>CK_SLIST_INSERT_HEAD</code> <code>CK_SLIST_MOVE</code> <code>CK_SLIST_NEXT</code> <code>CK_SLIST_REMOVE</code> <code>CK_SLIST_REMOVE_AFTER</code> <code>CK_SLIST_REMOVE_HEAD</code> <code>CK_SLIST_SWAP</code> <code>CK_STAILQ_CONCAT</code> <code>CK_STAILQ_EMPTY</code> <code>CK_STAILQ_ENTRY</code> <code>CK_STAILQ_FIRST</code> <code>CK_STAILQ_FOREACH</code> <code>CK_STAILQ_FOREACH_SAFE</code> <code>CK_STAILQ_HEAD</code> <code>CK_STAILQ_HEAD_INITIALIZER</code> <code>CK_STAILQ_INIT</code> <code>CK_STAILQ_INSERT_AFTER</code> <code>CK_STAILQ_INSERT_HEAD</code> <code>CK_STAILQ_INSERT_TAIL</code> <code>CK_STAILQ_MOVE</code> <code>CK_STAILQ_NEXT</code> <code>CK_STAILQ_REMOVE</code> <code>CK_STAILQ_REMOVE_AFTER</code> <code>CK_STAILQ_REMOVE_HEAD</code> <code>CK_STAILQ_SWAP</code> &#8211; multi-reader single-writer singly-linked lists, singly-linked tail queues and lists</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_queue.h Fn CK_LIST_EMPTY Fn CK_LIST_ENTRY Fn CK_LIST_FIRST Fn CK_LIST_FOREACH Fn CK_LIST_FOREACH_SAFE Fn CK_LIST_HEAD Fn CK_LIST_HEAD_INITIALIZER Fn CK_LIST_INIT Fn CK_LIST_INSERT_AFTER Fn CK_LIST_INSERT_BEFORE Fn CK_LIST_INSERT_HEAD Fn CK_LIST_MOVE Fn CK_LIST_NEXT Fn CK_LIST_REMOVE Fn CK_LIST_SWAP Fn CK_SLIST_EMPTY Fn CK_SLIST_ENTRY Fn CK_SLIST_FIRST Fn CK_SLIST_FOREACH Fn CK_SLIST_FOREACH_PREVPTR Fn CK_SLIST_FOREACH_SAFE Fn CK_SLIST_HEAD Fn CK_SLIST_HEAD_INITIALIZER Fn CK_SLIST_INIT Fn CK_SLIST_INSERT_AFTER Fn CK_SLIST_INSERT_HEAD Fn CK_SLIST_MOVE Fn CK_SLIST_NEXT Fn CK_SLIST_REMOVE Fn CK_SLIST_REMOVE_AFTER Fn CK_SLIST_REMOVE_HEAD Fn CK_SLIST_SWAP Fn CK_STAILQ_CONCAT Fn CK_STAILQ_EMPTY Fn CK_STAILQ_ENTRY Fn CK_STAILQ_FIRST Fn CK_STAILQ_FOREACH Fn CK_STAILQ_FOREACH_SAFE Fn CK_STAILQ_HEAD Fn CK_STAILQ_HEAD_INITIALIZER Fn CK_STAILQ_INIT Fn CK_STAILQ_INSERT_AFTER Fn CK_STAILQ_INSERT_HEAD Fn CK_STAILQ_INSERT_TAIL Fn CK_STAILQ_MOVE Fn CK_STAILQ_NEXT Fn CK_STAILQ_REMOVE Fn CK_STAILQ_REMOVE_AFTER Fn CK_STAILQ_REMOVE_HEAD Fn CK_STAILQ_SWAP</p>
<h2>DESCRIPTION</h2>
<p> See your system&#8217;s manual page for queue for additional information. ck_queue is a queue.h-compatible implementation of many-reader-single-writer queues. It allows for safe concurrent iteration, peeking and read-side access in the presence of a single concurrent writer without any usage of locks. In many cases, adoption of ck_queue will simply require prefixing all queue operations with CK_.</p>
<h2>SEE ALSO</h2>
<p> queue </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
