---
title: "mrmfetchcolorliteral(3)"
name: "mrmfetchcolorliteral"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmfetchcolorliteral/"
description: "MrmFetchColorLiteral — Fetches a named color literal from a UID file"
---

<p><code>MrmFetchColorLiteral</code> &#8212; Fetches a named color literal from a UID file</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmFetchColorLiteral</code>(
<code>MrmHierarchy hierarchy_id</code>,
<code>String index</code>,
<code>Display *display</code>,
<code>Colormap colormap_id</code>,
<code>Pixel *pixel</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmFetchColorLiteral</code> function fetches a named color literal from a UID file, and converts the color literal to a pixel color value.</p>
<dl COMPACT>
<dt><i>hierarchy_id</i></p>
<dd>Specifies the ID of the UID hierarchy that contains the specified literal. The value of <i>hierarchy_id</i> was returned in a previous call to <code>MrmOpenHierarchyPerDisplay</code>.</p>
<dt><i>index</i></p>
<dd>Specifies the UIL name of the color literal to fetch. You must define this name in UIL as an exported value.</p>
<dt><i>display</i></p>
<dd>Specifies the display used for the pixmap. The <i>display</i> argument specifies the connection to the X server. For more information on the <code>Display</code> structure, see the Xlib function <code>XOpenDisplay</code>.</p>
<dt><i>colormap_id</i></p>
<dd>Specifies the ID of the color map. If <i>colormap_id</i> is NULL, the default color map is used.</p>
<dt><i>pixel</i></p>
<dd>Returns the ID of the color literal.</dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmBAD_HIERARCHY</code></p>
<dd>The hierarchy ID was invalid.</p>
<dt><code>MrmNOT_FOUND</code></p>
<dd>The color literal was not found in the UIL file.</p>
<dt><code>MrmWRONG_TYPE</code></p>
<dd>The caller tried to fetch a literal of a type not supported by this function.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmfetchbitmapliteral/">MrmFetchBitmapLiteral</a></code>(3), <code><a href="/docs/linux/man/3-mrmopenhierarchyperdisplay/">MrmOpenHierarchyPerDisplay</a></code>(3), <code><a href="/docs/linux/man/3-mrmfetchiconliteral/">MrmFetchIconLiteral</a></code>(3), <code><a href="/docs/linux/man/3-mrmfetchliteral/">MrmFetchLiteral</a></code>(3), and <code><a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a></code>(3).</p>
