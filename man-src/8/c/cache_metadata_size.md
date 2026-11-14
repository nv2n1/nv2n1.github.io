---
title: "cache_metadata_size(8)"
name: "cache_metadata_size"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cache_metadata_size/"
description: "cache_metadata_size – Estimate the size of the metadata device needed for a given configuration."
---

<p><code>cache_metadata_size </code>&#8211; Estimate the size of the metadata device needed for a given configuration.</p>
<h2>Synopsis</h2>
<pre><code>cache_metadata_size</code> [<i>options</i>]</pre>
<h2>Description</h2>
<dl>
<dt><code>cache_metadata_size</code> estimates the size of the metadata.</p>
<dd>Either <code>&#8211;nr-blocks</code>, or <code>&#8211;block-size</code> and <code>&#8211;device-size</code> must be specified.</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;nr-blocks</code> {natural}</p>
<dd>Specify the number of cache blocks.</p>
<dt><code>&#8211;block-size</code> {sectors}</p>
<dd>Specify the size of each cache block in 512 byte sectors.</p>
<dt><code>&#8211;device-size</code> {sectors}</p>
<dd>Specify total size of the fast device used in the cache. In 512 byte sectors.</p>
<dt><code>&#8211;max-hint-width</code> {nr bytes}</p>
<dd>Specify hint width.</dl>
<pre> Cache policies use a per block 'hint' to record extra info (for instance
 hit counts). At the moment all policies use a 4 byte hint
 width. If you want to use a different hint width specify it with this
 switch.</pre>
<h2>Example</h2>
<p>$ <code>cache_metadata_size</code> <code>&#8211;nr-blocks</code> 10240 </p>
<p> $ <code>cache_metadata_size</code> <code>&#8211;block-size</code> 128 <code>&#8211;device-size</code> 1024000</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cache_dump/">cache_dump</a></code>(8), <code><a href="/docs/linux/man/8-cache_repair/">cache_repair</a></code>(8), <code><a href="/docs/linux/man/8-cache_restore/">cache_restore</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;heinzm [at] redhat.com&gt;</p>
