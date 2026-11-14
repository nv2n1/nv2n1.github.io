---
title: "xmstringgenerate(3)"
name: "xmstringgenerate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringgenerate/"
description: "XmStringGenerate — A convenience function that generates a compound string"
---

<p><code>XmStringGenerate</code> &#8212; A convenience function that generates a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringGenerate</code>(
<code>XtPointer text</code>,
<code>XmStringTag tag</code>,
<code>XmTextType type</code>,
<code>XmStringTag rendition</code>);</pre>
<h2>Description</h2>
<p><code>XmStringGenerate</code> calls the <code>XmStringParseText</code> function with a default parse table of entries consisting of &#8216;&amp;&#8217;, which maps to Separator, and &#8216; &#8216;, which maps to Tab. Matching <code>RENDITION_BEGIN</code> and <code>RENDITION_END</code> components containing <i>rendition</i> are placed around the resulting <code>XmString</code>.</p>
<dl COMPACT>
<dt><i>text</i></p>
<dd>Specifies a NULL-terminated string containing characters of a type determined by <i>type</i>.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag to be used in creating the result. The type of tag created (charset or locale) depends on the text type and the value given. If specified value is NULL, and <i>type</i> indicates that a charset tag should be created, then the tag will have the value of <code>XmFONTLIST_DEFAULT_TAG</code>. If <i>tag</i> is NULL, and <i>type</i> indicates a locale tag, then the tag will have the value of <code>_MOTIF_DEFAULT_LOCALE</code>.</p>
<dt><i>type</i></p>
<dd>Specifies the type of text to be passed in, and the tag type. If a locale tag should be created, then <i>type</i> has a value of either <code>XmMULTIBYTE_TEXT</code> or <code>XmWIDECHAR_TEXT</code>. If a charset should be created, <i>type</i> has a value of <code>XmCHARSET_TEXT</code>.</p>
<dt><i>rendition</i></p>
<dd>Specifies the rendition tag to be used in an <code>XmSTRING_COMPONENT_RENDITION_BEGIN</code> component which will begin the returned string and in an <code>XmSTRING_COMPONENT_RENDITION_END</code> component which will end it. If <i>rendition</i> is NULL, no rendition tag is placed.</dl>
<h2>Return</h2>
<p>Returns a new compound string. The function will allocate space to hold the returned compound string. When the application no longer needs the returned compound string, the application should call <code>XmStringFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
