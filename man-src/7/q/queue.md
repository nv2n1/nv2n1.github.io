---
title: "queue(7)"
name: "queue"
section: "7"
letter: "q"
url: "/docs/linux/man/7-queue/"
description: "queue – implementations of linked lists and queues"
---

<p>queue &#8211; implementations of linked lists and queues</p>
<h2>Description</h2>
<p>The <i>&lt;sys/queue.h&gt;</i> header file provides a set of macros that define and operate on the following data structures:</p>
<dl>
<dt>*</p>
<dd>singly linked lists (SLIST)</p>
<dt>*</p>
<dd>doubly linked lists (LIST)</p>
<dt>*</p>
<dd>singly linked tail queues (STAILQ)</p>
<dt>*</p>
<dd>doubly linked tail queues (TAILQ)</p>
<dt>*</p>
<dd>doubly linked circular queues (CIRCLEQ)</dl>
<p> All structures support the following functionality:</p>
<dl>
<dt>*</p>
<dd>Insertion of a new entry at the head of the list.</p>
<dt>*</p>
<dd>Insertion of a new entry after any element in the list.</p>
<dt>*</p>
<dd><a href="/docs/linux/man/1-o/">O</a>(1) removal of an entry from the head of the list.</p>
<dt>*</p>
<dd>Forward traversal through the list.</dl>
<p> Code size and execution time depend on the complexity of the data structure being used, so programmers should take care to choose the appropriate one.</p>
<h3>Singly linked lists (SLIST)</h3>
<p>Singly linked lists are the simplest and support only the above functionality. Singly linked lists are ideal for applications with large datasets and few or no removals, or for implementing a LIFO queue. Singly linked lists add the following functionality:</p>
<dl>
<dt>*</p>
<dd><a href="/docs/linux/man/n-o/">O</a>(n) removal of any entry in the list.</dl>
<h3>Singly linked tail queues (STAILQ)</h3>
<p>Singly linked tail queues add the following functionality:</p>
<dl>
<dt>*</p>
<dd>Entries can be added at the end of a list.</p>
<dt>*</p>
<dd><a href="/docs/linux/man/n-o/">O</a>(n) removal of any entry in the list.</p>
<dt>*</p>
<dd>They may be concatenated.</dl>
<p> However:</p>
<dl>
<dt>*</p>
<dd>All list insertions must specify the head of the list.</p>
<dt>*</p>
<dd>Each head entry requires two pointers rather than one.</dl>
<p> Singly linked tail queues are ideal for applications with large datasets and few or no removals, or for implementing a FIFO queue.</p>
<h3>Doubly linked data structures</h3>
<p>All doubly linked types of data structures (lists and tail queues) additionally allow:</p>
<dl>
<dt>*</p>
<dd>Insertion of a new entry before any element in the list.</p>
<dt>*</p>
<dd><a href="/docs/linux/man/1-o/">O</a>(1) removal of any entry in the list.</dl>
<p> However:</p>
<dl>
<dt>*</p>
<dd>Each element requires two pointers rather than one.</dl>
<h3>Doubly linked lists (LIST)</h3>
<p>Linked lists are the simplest of the doubly linked data structures. They add the following functionality over the above:</p>
<dl>
<dt>*</p>
<dd>They may be traversed backwards.</dl>
<p> However:</p>
<dl>
<dt>*</p>
<dd>To traverse backwards, an entry to begin the traversal and the list in which it is contained must be specified.</dl>
<h3>Doubly linked tail queues (TAILQ)</h3>
<p>Tail queues add the following functionality:</p>
<dl>
<dt>*</p>
<dd>Entries can be added at the end of a list.</p>
<dt>*</p>
<dd>They may be traversed backwards, from tail to head.</p>
<dt>*</p>
<dd>They may be concatenated.</dl>
<p> However:</p>
<dl>
<dt>*</p>
<dd>All list insertions and removals must specify the head of the list.</p>
<dt>*</p>
<dd>Each head entry requires two pointers rather than one.</dl>
<h3>Doubly linked circular queues (CIRCLEQ)</h3>
<p>Circular queues add the following functionality over the above:</p>
<dl>
<dt>*</p>
<dd>The first and last entries are connected.</dl>
<p> However:</p>
<dl>
<dt>*</p>
<dd>The termination condition for traversal is more complex.</dl>
<h2>Conforming To</h2>
<p>Not in POSIX.1, POSIX.1-2001 or POSIX.1-2008. Present on the BSDs. <i>&lt;sys/queue.h&gt;</i> macros first appeared in 4.4BSD.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-circleq/">circleq</a></code>(3), <code><a href="/docs/linux/man/3-insque/">insque</a></code>(3), <code><a href="/docs/linux/man/3-list/">list</a></code>(3), <code><a href="/docs/linux/man/3-slist/">slist</a></code>(3), <code><a href="/docs/linux/man/3-stailq/">stailq</a></code>(3), <code><a href="/docs/linux/man/3-tailq/">tailq</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
