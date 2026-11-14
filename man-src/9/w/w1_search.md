---
title: "w1_search(9)"
name: "w1_search"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_search/"
description: "w1_search – Performs a ROM Search & registers any devices found."
---

<p>w1_search &#8211; Performs a ROM Search &amp; registers any devices found.</p>
<h2>Synopsis</h2>
<pre><code>void w1_search(struct w1_master *dev, u8 search_type, w1_slave_found_callback cb);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>The master device to search</dl>
<p> <i>search_type</i></p>
<dl>
<dd>W1_SEARCH to search all devices, or W1_ALARM_SEARCH to return only devices in the alarmed state</dl>
<p> <i>cb</i></p>
<dl>
<dd>Function to call when a device is found</dl>
<h2>Description</h2>
<p>The 1-wire search is a simple binary tree search. For each bit of the address, we read two bits and write one bit. The bit written will put to sleep all devies that don&#8217;t match that bit. When the two reads differ, the direction choice is obvious. When both bits are 0, we must choose a path to take. When we can scan all 64 bits without having to choose a path, we are done. </p>
<p> See &#8220;Application note 187 1-wire search algorithm&#8221; at <a rel="nofollow" href="http://www.maxim-ic.com">www.maxim-ic.com</a></p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
