---
title: "blk_run_queue(9)"
name: "blk_run_queue"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_run_queue/"
---

blk_run_queue - run a single device queue

<h2>Synopsis</h2>

<pre><code>void blk_run_queue(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>The queue to run</dl>

<h2>Description</h2>

Invoke request handling on this queue, if it has pending work to do. May be used to restart queueing when a request has completed.

<h2>Copyright</h2>


