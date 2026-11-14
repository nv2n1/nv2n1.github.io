---
title: "xmrenditioncreate(3)"
name: "xmrenditioncreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrenditioncreate/"
description: "XmRenditionCreate — A convenience function that creates a rendition"
---

<p><code>XmRenditionCreate</code> &#8212; A convenience function that creates a rendition</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmRendition XmRenditionCreate</code>(
<code>Widget widget</code>,
<code>XmStringTag tag</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmRenditionCreate</code> creates a rendition whose resources are set to the values specified in <i>arglist</i>. Default values are assigned to resources that are not specified.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget used for deriving any necessary information for creating the rendition. In particular, the X display of <i>widget</i> will be used for loading fonts.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag for the rendition. (This will become the <code>XmNtag</code> resource for the rendition.)</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list.</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>).</dl>
<h2>Return</h2>
<p>Returns the created rendition. The function allocates space to hold the returned rendition. The application is responsible for managing this allocated space. The application can recover this allocated space by calling <code>XmRenditionFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendition/">XmRendition</a></code>(3) and <code><a href="/docs/linux/man/3-xmrenditionfree/">XmRenditionFree</a></code>(3).</p>
