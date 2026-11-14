---
title: "xmcvttextpropertytoxmstringtable(3)"
name: "xmcvttextpropertytoxmstringtable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcvttextpropertytoxmstringtable/"
description: "XmCvtTextPropertyToXmStringTable — A function that converts from a TextProperty Structure to a StringTable"
---

<p><code>XmCvtTextPropertyToXmStringTable</code> &#8212; A function that converts from a TextProperty Structure to a StringTable</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
int XmCvtTextPropertyToXmStringTable (<i>display, text_prop, string_table_return, count_return</i>)
 Display *<i>display</i>;
 XTextProperty *<i>text_prop</i>;
 XmStringTable *<i>string_table_return</i>;
 int *<i>count_return</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmCvtTextPropertyToXmStringTable</code> converts the specified <code>XTextProperty</code> structure into an <code>XmStringTable</code>, as follows:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>If the encoding member of <i>text_prop</i> is the Atom <code>STRING</code>, each returned <code>XmString</code> has a tag of &quot;ISO8859-1&quot; and a text type of <code>XmCHARSET_TEXT</code>.</p>
<dt> &bull;</p>
<dd>If the encoding member of <i>text_prop</i> is the encoding of the current locale, and if that encoding is not <code>STRING</code>, each returned <code>XmString</code> has a tag of <code>_MOTIF_DEFAULT_LOCALE</code> and a text type of <code>XmMULTIBYTE_TEXT</code>.</p>
<dt> &bull;</p>
<dd>If the encoding member of <i>text_prop</i> is other than <code>STRING</code> or the encoding of the current locale, the contents of the returned compound strings are implementation dependent.</dl>
<p> If conversion depends on the locale and the current locale is not supported, the function returns <code>XLocaleNotSupported</code>. If conversion to the encoding of the current locale is required and if the locale is supported but no converter is available for the encoding specified in <i>text_prop</i>, the function returns <code>XConverterNotFound</code>. For supported locales, existence of a converter from <code>COMPOUND_TEXT</code>, <code>STRING</code>, <code>UTF8_STRING</code>, or the encoding of the current locale is guaranteed if <code>XSupportsLocale</code> returns True for the current locale (but the actual text may contain unconvertible characters). Conversion of other encodings to the encoding of the current locale is implementation dependent. In all of these error cases, the function does not set any return values. </p>
<p> If an element of the value member of <i>text_prop</i> is not convertible to <code>XmString</code>, the corresponding entry in the returned <code>XmStringTable</code> will be NULL, and <code>XmCvtTextPropertyToXmStringTable</code> returns Success. </p>
<p> To free the storage for the <code>XmStringTable</code> and its <i>count_return</i> compound strings returned by this function, first free each <code>XmString</code> in the table using <code>XmStringFree</code>, and then free the <code>XmStringTable</code> itself using <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>text_prop</i></p>
<dd>Specifies a pointer to the <code>XTextProperty</code>. The format member of <i>text_prop</i> must be 8.</p>
<dt><i>string_table_return</i></p>
<dd>Specifies the <code>XmStringTable</code> array into which the converted compound strings are placed.</p>
<dt><i>count_return</i></p>
<dd>Specifies the number of <code>XmString</code>s returned by this function.</dl>
<h2>Return Values</h2>
<p>Upon success, this function returns the set of <code>XmString</code>s in <i>string_table_return</i>, and it returns the number of <code>XmString</code>s in <i>count_return</i>, and returns Success. Otherwise, it returns the following:</p>
<dl COMPACT>
<dt><code>XLocaleNotSupported</code></p>
<dd>Returned if conversion depends on the locale and the current locale is not supported.</p>
<dt><code>XConverterNotFound</code></p>
<dd>Returned if conversion to the encoding of the current locale is required and if the locale is supported but no converter is available for the encoding specified in <i>text_prop</i>.</dl>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmcvtxmstringtabletotextproperty/">XmCvtXmStringTableToTextProperty</a></code>(3), <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3), and <code><a href="/docs/linux/man/3-xmtextgetstring/">XmTextGetString</a></code>(3).</p>
