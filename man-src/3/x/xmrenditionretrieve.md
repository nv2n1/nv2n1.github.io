---
title: "xmrenditionretrieve(3)"
name: "xmrenditionretrieve"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrenditionretrieve/"
description: "XmRenditionRetrieve — A convenience function that retrieves rendition resources"
---

<p><code>XmRenditionRetrieve</code> &#8212; A convenience function that retrieves rendition resources</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmRenditionRetrieve</code>(
<code>XmRendition rendition</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmRenditionRetrieve</code> extracts values for the given resources (<i>arglist</i>) from the specified rendition. Note that the function returns the actual values of the resources, not copies. Therefore it is necessary to copy before modifying any resource whose value is an address. This will include such resources as <code>XmNfontName</code>, <code>XmNfont</code>, and <code>XmNtabList</code>.</p>
<dl COMPACT>
<dt><i>rendition</i></p>
<dd>Specifies the rendition.</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list.</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>).</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendition/">XmRendition</a></code>(3) and <code><a href="/docs/linux/man/3-xmtablistcopy/">XmTabListCopy</a></code>(3).</p>
