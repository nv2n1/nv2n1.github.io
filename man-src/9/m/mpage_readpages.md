---
title: "mpage_readpages(9)"
name: "mpage_readpages"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mpage_readpages/"
description: "mpage_readpages – populate an address space with some pages & start reads against them"
---

<p>mpage_readpages &#8211; populate an address space with some pages &amp; start reads against them</p>
<h2>Synopsis</h2>
<pre><code>int mpage_readpages(struct address_space *mapping, struct list_head *pages, unsigned nr_pages, get_block_t get_block);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>the address_space</dl>
<p> <i>pages</i></p>
<dl>
<dd>The address of a list_head which contains the target pages. These pages have their -&gt;index populated and are otherwise uninitialised. The page at <i>pages</i>-&gt;prev has the lowest file offset, and reads should be issued in <i>pages</i>-&gt;prev to <i>pages</i>-&gt;next order.</dl>
<p> <i>nr_pages</i></p>
<dl>
<dd>The number of pages at *<i>pages</i></dl>
<p> <i>get_block</i></p>
<dl>
<dd>The filesystem&#8217;s block mapper function.</dl>
<h2>Description</h2>
<p>This function walks the pages and the blocks within each page, building and emitting large BIOs. </p>
<p> If anything unusual happens, such as: </p>
<p> &#8211; encountering a page which has buffers &#8211; encountering a page which has a non-hole after a hole &#8211; encountering a page with non-contiguous blocks </p>
<p> then this code just gives up and calls the buffer_head-based read function. It does handle a page which has holes at the end &#8211; that is a common case: the end-of-file on blocksize &lt; PAGE_SIZE setups. </p>
<p> BH_Boundary explanation: </p>
<p> There is a problem. The mpage read code assembles several pages, gets all their disk mappings, and then submits them all. That&#8217;s fine, but obtaining the disk mappings may require I/O. Reads of indirect blocks, for example. </p>
<p> So an mpage read of the first 16 blocks of an ext2 file will cause I/O to be submitted in the following order: 12 0 1 2 3 4 5 6 7 8 9 10 11 13 14 15 16 </p>
<p> because the indirect block has to be read to get the mappings of blocks 13,14,15,16. Obviously, this impacts performance. </p>
<p> So what we do it to allow the filesystem&#8217;s <code>get_block</code> function to set BH_Boundary when it maps block 11. BH_Boundary says: mapping of the block after this one will require I/O against a block which is probably close to this one. So you should push what I/O you have currently accumulated. </p>
<p> This all causes the disk requests to be issued in the correct order.</p>
<h2>Copyright</h2>
