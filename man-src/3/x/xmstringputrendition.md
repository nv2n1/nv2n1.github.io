---
title: "xmstringputrendition(3)"
name: "xmstringputrendition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringputrendition/"
description: "XmStringPutRendition — A convenience function that places renditions around strings"
---

<p><code>XmStringPutRendition</code> &#8212; A convenience function that places renditions around strings</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringPutRendition</code>(
<code>XmString string</code>,
<code>XmStringTag rendition</code>);</pre>
<h2>Description</h2>
<p><code>XmStringPutRendition</code> places matching <code>Xm_STRING_COMPONENT_RENDITION_BEGIN</code> and <code>XmSTRING_COMPONENT_RENDITION_END</code> components containing <i>rendition</i> around <i>string</i>. The original string is preserved.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies the compound string to which begin and end rendition components should be added.</p>
<dt><i>rendition</i></p>
<dd>Specifies the rendition tag to be used in an <code>XmSTRING_COMPONENT_RENDITION_BEGIN</code> component which will begin the returned string and in an <code>XmSTRING_COMPONENT_RENDITION_END</code> component which will end it.</dl>
<h2>Return</h2>
<p>Returns a new compound string. The function allocates space to hold this returned compound string. When the application no longer needs the returned compound string, the application should call <code>XmStringFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
