---
title: "xmstringparsetext(3)"
name: "xmstringparsetext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringparsetext/"
description: "XmStringParseText — A function that converts a character string to a compound string"
---

<p><code>XmStringParseText</code> &#8212; A function that converts a character string to a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringParseText</code>(
<code>XtPointer text</code>,
<code>XtPointer *text_end</code>,
<code>XmStringTag tag</code>,
<code>XmTextType type</code>,
<code>XmParseTable parse_table</code>,
<code>Cardinal parse_count</code>,
<code>XtPointer call_data</code>);</pre>
<h2>Description</h2>
<p><code>XmStringParseText</code> converts characters specified in <i>text</i> to corresponding components in the returned compound string. The resulting compound string consists of at least one locale or charset tag component and a series of <code>XmString</code> text components and other components. The conversion proceeds according to the parse information contained in <i>parse_table</i>. See the <i>Motif Programmer&#8217;s Guide</i> for more information about parsing and parse tables.</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>If <i>type</i> is <code>XmCHARSET_TEXT</code>, the associated <i>tag</i> is interpreted as a charset name. If <i>tag</i> has a value of NULL, a charset component whose value is the result of mapping <code>XmFONTLIST_DEFAULT_TAG</code> is created.</p>
<dt> &bull;</p>
<dd>If <i>type</i> is <code>XmMULTIBYTE_TEXT</code> or <code>XmWIDECHAR_TEXT</code>, the associated <i>tag</i> is interpreted as a language environment name. If <i>tag</i> has a value of NULL, a locale component with a value of <code>_MOTIF_DEFAULT_LOCALE</code> is created. If <i>type</i> is <code>XmMULTIBYTE_TEXT</code> or <code>XmWIDECHAR_TEXT</code>, <i>tag</i> must be NULL or <code>_MOTIF_DEFAULT_LOCALE</code>.</dl>
<p> <code>XmStringParseText</code> also scans the string for characters that have matches in <i>parse_table</i>. Whenever a match is found, the text up to that point is concatenated with the mapped component.</p>
<dl COMPACT>
<dt><i>text</i></p>
<dd>Specifies the NULL-terminated string containing characters of a type determined by <i>type</i>. This is updated to point to after the last character scanned.</p>
<dt><i>text_end</i></p>
<dd>Specifies a pointer into <i>text</i>. If a NULL is supplied to the <i>text_end</i> parameter, then <code>XmStringParseText</code> parses <i>text</i> until NULL is encountered, or until it reaches a point in <i>text</i> where it is directed to stop (for example, by a <code>parse_proc</code>). Otherwise, the value supplied to the <i>text_end</i> parameter is the pointer into <i>text</i> where parsing is to stop, and the returned character is the one where parsing did stop.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag to be used in creating the result. The type of string tag created (charset or locale) depends on the text type and the passed in <i>tag</i> value. If the <i>tag</i> value is NULL and if <i>type</i> indicates that a charset string tag should be created, the string tag has the value that is the result of mapping <code>XmFONTLIST_DEFAULT_TAG</code>. If <i>type</i> indicates a locale string tag, the string tag has the value <code>_MOTIF_DEFAULT_LOCALE</code>.</p>
<dt><i>type</i></p>
<dd>Specifies the type of text and the tag type. If a locale tag should be created, <i>type</i> has a value of either <code>XmMULTIBYTE_TEXT</code> or <code>XmWIDECHAR_TEXT</code>. If <i>type</i> has value of <code>XmCHARSET_TEXT</code>, a charset tag will be created.</p>
<dt><i>parse_table</i></p>
<dd>Specifies the parse table to be used in scanning for characters to be converted to other compound string components.</p>
<dt><i>parse_count</i></p>
<dd>Specifies the number of entries in <i>parse_table</i>.</p>
<dt><i>call_data</i></p>
<dd>Specifies data to be passed to the parse procedures.</dl>
<h2>Return</h2>
<p>Returns a new compound string. The function allocates space to hold the returned compound string. When the application no longer needs the returned compound string, the application should call <code>XmStringFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetable/">XmParseTable</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3).</p>
