---
title: "xmstringunparse(3)"
name: "xmstringunparse"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringunparse/"
description: "XmStringUnparse — A compound string function that unparses text"
---

<p><code>XmStringUnparse</code> &#8212; A compound string function that unparses text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XtPointer XmStringUnparse</code>(
<code>XmString string</code>,
<code>XmStringTag tag</code>,
<code>XmTextType tag_type</code>,
<code>XmTextType output_type</code>,
<code>XmParseTable parse_table</code>,
<code>Cardinal parse_count</code>,
<code>XmParseModel parse_model</code>);</pre>
<h2>Description</h2>
<p><code>XmStringUnparse</code> looks in the input <i>string</i> for text segments that are tagged with locale or charset tags that match <i>tag</i>. The <i>tag_type</i> parameter specifies whether the tag is a locale or charset type. If <i>tag</i> has a value of NULL, all the segments are matched. When a text segment is found with a matching tag, it is added to the end of a resulting string. The characters in the resulting string are of type <i>output_type</i>. </p>
<p> <code>XmStringUnparse</code> also checks <i>string</i> for components that match components in <i>parse_table</i>, and also to see if the component matches the condition specified by <i>parse_model</i>. If the string component matches in both checks, then the associated character is added to the end of the resulting string.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies the <code>XmString</code> to be converted.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag to be used in matching with text segments. Only text segments that match <i>tag</i> will be included in the resulting string. If <i>tag</i> has a value of NULL, all segments are considered as matches, and <i>tag_type</i> is ignored.</p>
<dt><i>tag_type</i></p>
<dd>Specifies the type of tag to be searched for, including <code>XmMULTIBYTE_TEXT</code>, <code>XmWIDECHAR_TEXT</code>, and <code>XmCHARSET_TEXT</code>.</p>
<dt><i>output_type</i></p>
<dd>Specifies the type of text to be returned in the string, including <code>XmMULTIBYTE_TEXT</code>, <code>XmWIDECHAR_TEXT</code>, and <code>XmCHARSET_TEXT</code>.</p>
<dt><i>parse_table</i></p>
<dd>Specifies the parse table to be used in scanning for compound string components to be converted to other characters.</p>
<dt><i>parse_count</i></p>
<dd>Specifies how many entries are in <i>parse_table</i>.</p>
<dt><i>parse_model</i></p>
<dd>Specifies which non-text components to be considered in matching in <i>parse_table</i>. These include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmOUTPUT_ALL</code></p>
<dd>Puts out all matching components.</p>
<dt><code>XmOUTPUT_BETWEEN</code></p>
<dd>Puts out only those matching components that are between two matching text components.</p>
<dt><code>XmOUTPUT_BEGINNING</code></p>
<dd>Puts out only those matching components that are at the beginning of a matching text component.</p>
<dt><code>XmOUTPUT_END</code></p>
<dd>Puts out only those matching components that are at the end of a matching text component.</p>
<dt><code>XmOUTPUT_BOTH</code></p>
<dd>Puts out only those matching components that are at the beginning or end of a matching text component.</dl>
</dl>
</dl>
<h2>Return</h2>
<p>Returns a newly allocated string containing characters of a type determined by <i>output_type</i>. The application is responsible for managing this allocated space. The application can recover this allocated space by calling <code>XtFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetable/">XmParseTable</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3).</p>
