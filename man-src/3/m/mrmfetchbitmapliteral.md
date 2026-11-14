---
title: "mrmfetchbitmapliteral(3)"
name: "mrmfetchbitmapliteral"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmfetchbitmapliteral/"
description: "MrmFetchBitmapLiteral — Fetches a bitmap literal from a hierarchy"
---

<p><code>MrmFetchBitmapLiteral</code> &#8212; Fetches a bitmap literal from a hierarchy</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmFetchBitmapLiteral</code>(
<code>MrmHierarchy hierarchy_id</code>,
<code>String index</code>,
<code>Screen *screen</code>,
<code>Display *display</code>,
<code>Pixmap *pixmap_return</code>,
<code>Dimension *width</code>,
<code>Dimension *height</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmFetchBitmapLiteral</code> function fetches a bitmap literal from an MRM hierarchy, and converts the bitmap literal to an X pixmap of depth 1. The function returns this pixmap and its width and height.</p>
<dl COMPACT>
<dt><i>hierarchy_id</i></p>
<dd>Specifies the ID of the UID hierarchy that contains the specified icon literal. The value of <i>hierarchy_id</i> was returned in a previous call to <code>MrmOpenHierarchyPerDisplay</code>.</p>
<dt><i>index</i></p>
<dd>Specifies the UIL name of the bitmap literal to fetch.</p>
<dt><i>screen</i></p>
<dd>Specifies the screen used for the pixmap. The <i>screen</i> argument specifies a pointer to the Xlib structure <code>Screen</code> which contains the information about that screen and is linked to the <code>Display</code> structure. For more information on the <code>Display</code> and <code>Screen</code> structures, see the Xlib function <code>XOpenDisplay</code> and the associated screen information macros.</p>
<dt><i>display</i></p>
<dd>Specifies the display used for the pixmap. The <i>display</i> argument specifies the connection to the X server. For more information on the <code>Display</code> structure, see the Xlib function <code>XOpenDisplay</code>.</p>
<dt><i>pixmap_return</i></p>
<dd>Returns the resulting X pixmap value. The function allocates space for this pixmap. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmDestroyPixmap</code>.</p>
<dt><i>width</i></p>
<dd>Specifies a pointer to the width of the pixmap.</p>
<dt><i>height</i></p>
<dd>Specifies a pointer to the height of the pixmap.</dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmBAD_HIERARCHY</code></p>
<dd>The hierarchy ID was invalid.</p>
<dt><code>MrmNOT_FOUND</code></p>
<dd>The bitmap literal was not found in the hierarchy.</p>
<dt><code>MrmWRONG_TYPE</code></p>
<dd>The caller tried to fetch a literal of a type not supported by this function.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmfetchiconliteral/">MrmFetchIconLiteral</a></code>(3), <code><a href="/docs/linux/man/3-mrmfetchliteral/">MrmFetchLiteral</a></code>(3), and <code><a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a></code>(3).</p>
