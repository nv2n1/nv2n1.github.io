---
title: "d_really_is_positive(9)"
name: "d_really_is_positive"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_really_is_positive/"
description: "d_really_is_positive – Determine if a dentry is really positive (ignoring fallthroughs)"
---

<p>d_really_is_positive &#8211; Determine if a dentry is really positive (ignoring fallthroughs)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool d_really_is_positive(const struct dentry&nbsp;<wbr>*&nbsp;<wbr></code><i>dentry</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>The dentry in question</dl>
<h2>Description</h2>
<p>Returns true if the dentry represents a name that maps to an inode (ie. -&gt;d_inode is not NULL). The dentry might still represent a whiteout if that is represented on medium as a 0,0 chardev. </p>
<p> Note! (1) This should be used *only* by a filesystem to examine its own dentries. It should not be used to look at some other filesystem&#8217;s dentries. (2) It should also be used in combination with <code>d_inode</code> to get the inode.</p>
<h2>Copyright</h2>
