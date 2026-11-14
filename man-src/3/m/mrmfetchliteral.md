---
title: "mrmfetchliteral(3)"
name: "mrmfetchliteral"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmfetchliteral/"
description: "MrmFetchLiteral — Fetches a literal from a UID file"
---

<p><code>MrmFetchLiteral</code> &#8212; Fetches a literal from a UID file</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmFetchLiteral</code>(
<code>MrmHierarchy hierarchy_id</code>,
<code>String index</code>,
<code>Display *display</code>,
<code>XtPointer *value</code>,
<code>MrmCode *type</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmFetchLiteral</code> function reads and returns the value and type of a literal (named value) that is stored as a public resource in a single UID file. This function returns a pointer to the value of the literal. For example, an integer is always returned as a pointer to an integer, and a string is always returned as a pointer to a string. </p>
<p> Applications should not use <code>MrmFetchLiteral</code> for fetching icon or color literals. If this is attempted, <code>MrmFetchLiteral</code> returns an error.</p>
<dl COMPACT>
<dt><i>hierarchy_id</i></p>
<dd>Specifies the ID of the UID hierarchy that contains the specified literal. The value of <i>hierarchy_id</i> was returned in a previous call to <code>MrmOpenHierarchyPerDisplay</code>.</p>
<dt><i>index</i></p>
<dd>Specifies the UIL name of the literal (pixmap) to fetch. You must define this name in UIL as an exported value.</p>
<dt><i>display</i></p>
<dd>Specifies the display used for the pixmap. The <i>display</i> argument specifies the connection to the X server. For more information on the <code>Display</code> structure, see the Xlib function <code>XOpenDisplay</code>.</p>
<dt><i>value</i></p>
<dd>Returns the ID of the named literal&#8217;s value. The function allocates space for the returned value. The application is responsible for managing the allocated space by calling the appropriate deallocation function. For example, if the returned ID symbolizes a pixmap, then the application can recover the allocated space by calling <code>XmDestroyPixmap</code>.</p>
<dt><i>type</i></p>
<dd>Returns the named literal&#8217;s data type. Types are defined in the include file <code>Mrm/MrmPublic.h</code>.</dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmBAD_HIERARCHY</code></p>
<dd>The hierarchy ID was invalid.</p>
<dt><code>MrmNOT_FOUND</code></p>
<dd>The literal was not found in the UIL file.</p>
<dt><code>MrmWRONG_TYPE</code></p>
<dd>The caller tried to fetch a literal of a type not supported by this function.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmfetchbitmapliteral/">MrmFetchBitmapLiteral</a></code>(3), <code><a href="/docs/linux/man/3-mrmopenhierarchyperdisplay/">MrmOpenHierarchyPerDisplay</a></code>(3), <code><a href="/docs/linux/man/3-mrmfetchiconliteral/">MrmFetchIconLiteral</a></code>(3), <code><a href="/docs/linux/man/3-mrmfetchcolorliteral/">MrmFetchColorLiteral</a></code>(3), and <code><a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a></code>(3).</p>
