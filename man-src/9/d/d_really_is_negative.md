---
title: "d_really_is_negative(9)"
name: "d_really_is_negative"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_really_is_negative/"
description: "d_really_is_negative – Determine if a dentry is really negative (ignoring fallthroughs)"
---

<p>d_really_is_negative &#8211; Determine if a dentry is really negative (ignoring fallthroughs)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool d_really_is_negative(const struct dentry&nbsp;<wbr>*&nbsp;<wbr></code><i>dentry</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>The dentry in question</dl>
<h2>Description</h2>
<p>Returns true if the dentry represents either an absent name or a name that doesn&#8217;t map to an inode (ie. -&gt;d_inode is NULL). The dentry could represent a true miss, a whiteout that isn&#8217;t represented by a 0,0 chardev or a fallthrough marker in an opaque directory. </p>
<p> Note! (1) This should be used *only* by a filesystem to examine its own dentries. It should not be used to look at some other filesystem&#8217;s dentries. (2) It should also be used in combination with <code>d_inode</code> to get the inode. (3) The dentry may have something attached to -&gt;d_lower and the type field of the flags may be set to something other than miss or whiteout.</p>
<h2>Copyright</h2>
