---
title: "splice_direct_to_actor(9)"
name: "splice_direct_to_actor"
section: "9"
letter: "s"
url: "/docs/linux/man/9-splice_direct_to_actor/"
description: "splice_direct_to_actor – splices data directly between two non-pipes"
---

<p>splice_direct_to_actor &#8211; splices data directly between two non-pipes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t splice_direct_to_actor(struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>in</i><code>, struct splice_desc&nbsp;<wbr>*&nbsp;<wbr></code><i>sd</i><code>, splice_direct_actor&nbsp;<wbr>*&nbsp;<wbr></code><i>actor</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>in</i></p>
<dl>
<dd>
<dd>file to splice from</dl>
<p> <i>sd</i></p>
<dl>
<dd>actor information on where to splice to</dl>
<p> <i>actor</i></p>
<dl>
<dd>handles the data splicing</dl>
<h2>Description</h2>
<p>This is a special case helper to splice directly between two points, without requiring an explicit pipe. Internally an allocated pipe is cached in the process, and reused during the lifetime of that process.</p>
<h2>Copyright</h2>
