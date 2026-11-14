---
title: "trace_block_split(9)"
name: "trace_block_split"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_split/"
description: "trace_block_split – split a single bio struct into two bio structs"
---

<p>trace_block_split &#8211; split a single bio struct into two bio structs</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_split(struct request_queue *q, struct bio *bio, unsigned int new_sector);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue containing the bio</dl>
<p> <i>bio</i></p>
<dl>
<dd>block operation being split</dl>
<p> <i>new_sector</i></p>
<dl>
<dd>The starting sector for the new bio</dl>
<h2>Description</h2>
<p>The bio request <i>bio</i> in request queue <i>q</i> needs to be split into two bio requests. The newly created <i>bio</i> request starts at <i>new_sector</i>. This split may be required due to hardware limitation such as operation crossing device boundaries in a RAID system.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
