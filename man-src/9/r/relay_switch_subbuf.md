---
title: "relay_switch_subbuf(9)"
name: "relay_switch_subbuf"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_switch_subbuf/"
---

relay_switch_subbuf - switch to a new sub-buffer

<h2>Synopsis</h2>

<pre><code>size_t relay_switch_subbuf(struct rchan_buf *buf, size_t length);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>channel buffer</dl>
 

 <i>length</i>
<dl><dd>size of current event</dl>

<h2>Description</h2>

Returns either the length passed in or 0 if full. 

 Performs sub-buffer-switch tasks such as invoking callbacks, updating padding counts, waking up readers, etc.

<h2>Copyright</h2>


