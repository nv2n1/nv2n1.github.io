---
title: "mrmclosehierarchy(3)"
name: "mrmclosehierarchy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmclosehierarchy/"
description: "MrmCloseHierarchy — Closes a UID hierarchy"
---

<p><code>MrmCloseHierarchy</code> &#8212; Closes a UID hierarchy</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmCloseHierarchy</code>(
<code>MrmHierarchy hierarchy_id</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmCloseHierarchy</code> function closes a UID hierarchy previously opened by <code>MrmOpenHierarchyPerDisplay</code>. All files associated with the hierarchy are closed by the Motif Resource Manager (MRM) and all associated memory is returned.</p>
<dl COMPACT>
<dt><i>hierarchy_id</i></p>
<dd>Specifies the ID of a previously opened UID hierarchy. The <i>hierarchy_id</i> was returned in a previous call to <code>MrmOpenHierarchyPerDisplay</code>.</dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmBAD_HIERARCHY</code></p>
<dd>The hierarchy ID was invalid.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmopenhierarchyperdisplay/">MrmOpenHierarchyPerDisplay</a></code>(3).</p>
