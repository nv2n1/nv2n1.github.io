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
<dt><i>hierarchy_id</i></dt>
<dd>Specifies the ID of the UID hierarchy that contains the specified icon literal. The value of <i>hierarchy_id</i> was returned in a previous call to <code>MrmOpenHierarchyPerDisplay</code>.</dd>
<dt><i>index</i></dt>
<dd>Specifies the UIL name of the bitmap literal to fetch.</dd>
<dt><i>screen</i></dt>
<dd>Specifies the screen used for the pixmap. The <i>screen</i> argument specifies a pointer to the Xlib structure <code>Screen</code> which contains the information about that screen and is linked to the <code>Display</code> structure. For more information on the <code>Display</code> and <code>Screen</code> structures, see the Xlib function <code>XOpenDisplay</code> and the associated screen information macros.</dd>
<dt><i>display</i></dt>
<dd>Specifies the display used for the pixmap. The <i>display</i> argument specifies the connection to the X server. For more information on the <code>Display</code> structure, see the Xlib function <code>XOpenDisplay</code>.</dd>
<dt><i>pixmap_return</i></dt>
<dd>Returns the resulting X pixmap value. The function allocates space for this pixmap. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmDestroyPixmap</code>.</dd>
<dt><i>width</i></dt>
<dd>Specifies a pointer to the width of the pixmap.</dd>
<dt><i>height</i></dt>
<dd>Specifies a pointer to the height of the pixmap.</dd></dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></dt>
<dd>The function executed successfully.</dd>
<dt><code>MrmBAD_HIERARCHY</code></dt>
<dd>The hierarchy ID was invalid.</dd>
<dt><code>MrmNOT_FOUND</code></dt>
<dd>The bitmap literal was not found in the hierarchy.</dd>
<dt><code>MrmWRONG_TYPE</code></dt>
<dd>The caller tried to fetch a literal of a type not supported by this function.</dd>
<dt><code>MrmFAILURE</code></dt>
<dd>The function failed.</dd></dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmfetchiconliteral/">MrmFetchIconLiteral</a></code>(3), <code><a href="/docs/linux/man/3-mrmfetchliteral/">MrmFetchLiteral</a></code>(3), and <code><a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a></code>(3).</p>
