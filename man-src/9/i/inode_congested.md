---
title: "inode_congested(9)"
name: "inode_congested"
section: "9"
letter: "i"
url: "/docs/linux/man/9-inode_congested/"
---

inode_congested - test whether an inode is congested

<h2>Synopsis</h2>

<pre><code>int inode_congested(struct inode *inode, int cong_bits);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode to test for congestion (may be NULL)</dl>
 

 <i>cong_bits</i>
<dl><dd>mask of WB_[a]sync_congested bits to test</dl>

<h2>Description</h2>

Tests whether <i>inode</i> is congested. <i>cong_bits</i> is the mask of congestion bits to test and the return value is the mask of set bits. 

 If cgroup writeback is enabled for <i>inode</i>, the congestion state is determined by whether the cgwb (cgroup bdi_writeback) for the blkcg associated with <i>inode</i> is congested; otherwise, the root wb's congestion state is used. 

 <i>inode</i> is allowed to be NULL as this function is often called on mapping-&gt;host which is NULL for the swapper space.

<h2>Copyright</h2>


