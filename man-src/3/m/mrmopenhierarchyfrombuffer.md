---
title: "mrmopenhierarchyfrombuffer(3)"
name: "mrmopenhierarchyfrombuffer"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmopenhierarchyfrombuffer/"
description: "MrmOpenHierarchyFromBuffer — Allocates a hierarchy ID and opens a buffer containing a memory image of a UID file"
---

<p><code>MrmOpenHierarchyFromBuffer</code> &#8212; Allocates a hierarchy ID and opens a buffer containing a memory image of a UID file</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmOpenHierarchyFromBuffer</code>(
<code>unsigned char uid_buffer</code>,
<code>MrmHierarchy *hierarchy_id</code>);</pre>
<h2>Description</h2>
<p><code>MrmOpenHierarchyFromBuffer</code> allows you to specify a buffer containing information from UID files that MRM searches in subsequent fetch operations. This function also allocates a hierarchy ID and initializes the optimized search lists in the hierarchy.</p>
<dl COMPACT>
<dt><i>buffer</i></dt>
<dd>Specifies a stream of bytes containing information from UID files</dd>
<dt><i>hierarchy_id</i></dt>
<dd>Returns the search hierarchy ID. The search hierarchy ID identifies the buffer that MRM searches when performing subsequent fetch calls.</dd></dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></dt>
<dd>The function executed successfully.</dd>
<dt><code>MrmFAILURE</code></dt>
<dd>The function failed.</dd></dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmclosehierarchy/">MrmCloseHierarchy</a></code>(3) and <code><a href="/docs/linux/man/3-mrmopenhierarchyperdisplay/">MrmOpenHierarchyPerDisplay</a></code>(3).</p>
