---
title: "xmcvtxmstringtabletotextproperty(3)"
name: "xmcvtxmstringtabletotextproperty"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcvtxmstringtabletotextproperty/"
description: "XmCvtXmStringTableToTextProperty — A function that converts from XmStringTable to an XTextProperty Structure"
---

<p><code>XmCvtXmStringTableToTextProperty</code> &#8212; A function that converts from XmStringTable to an XTextProperty Structure</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
int XmCvtXmStringTableToTextProperty (<i>display, string_table, count, style, text_prop_return</i>)
 Display *<i>display</i>;
 XmStringTable <i>string_table</i>;
 int <i>count</i>;
 XmICCEncodingStyle <i>style</i>;
 XTextProperty *<i>text_prop_return</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmCvtXmStringTableToTextProperty</code> converts the <code>XmString</code>s in the specified <code>XmStringTable</code> into an <code>XTextProperty</code> structure. </p>
<p> The function sets the encoding member of <i>text_prop_return</i> to an <code>Atom</code> for the specified display naming the encoding determined by the specified style, and it converts the first <i>count</i> compound strings in the specified <code>XmStringTable</code> to this encoding for storage in the <i>text_prop_return</i> value member. Following are the possible encoding styles:</p>
<dl COMPACT>
<dt><code>XmSTYLE_COMPOUND_STRING</code></p>
<dd>The encoding is <code>_MOTIF_COMPOUND_STRING</code>. The function converts each specified <code>XmString</code> to a compound string in Byte Stream format.</p>
<dt><code>XmSTYLE_COMPOUND_TEXT</code></p>
<dd>The encoding is <code>COMPOUND_TEXT</code>. The function converts each specified <code>XmString</code> to compound text.</p>
<dt><code>XmSTYLE_LOCALE</code></p>
<dd>The encoding is the encoding of the current locale. The function converts each specified <code>XmString</code> to the encoding of the current locale.</p>
<dt><code>XmSTYLE_STRING</code></p>
<dd>The encoding is <code>STRING</code> (plain C strings encoded in ISO8859-1), and the function converts each specified <code>XmString</code> to <code>STRING</code>.</p>
<dt><code>XmSTYLE_TEXT</code></p>
<dd>If all specified <code>XmString</code>s are fully convertible to the encoding of the current locale, the encoding is the encoding of the current locale, and the function converts each specified <code>XmString</code> to the encoding of the current locale. Otherwise, the encoding is <code>COMPOUND_TEXT</code>, and the function converts each specified compound string to compound text.</p>
<dt><code>XmSTYLE_STANDARD_ICC_TEXT</code></p>
<dd>If all specified <code>XmString</code>s are fully convertible to <code>STRING</code>, the encoding is <code>STRING</code>, and the function converts each specified <code>XmString</code> to <code>STRING</code>. Otherwise, the encoding is <code>COMPOUND_TEXT</code>, and the function converts each specified <code>XmString</code> to compound text.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>string_table</i></p>
<dd>Specifies a set of <code>XmString</code>s.</p>
<dt><i>count</i></p>
<dd>Specifies the number of <code>XmString</code>s to be converted in <i>string_table</i>.</p>
<dt><i>style</i></p>
<dd>Specifies the manner in which the property is encoded.</p>
<dt><i>text_prop_return</i></p>
<dd>Returns the <code>XTextProperty</code> structure.</dl>
<p> To free the storage for the value member of the <code>XTextProperty</code>, use <code>XtFree</code>.</p>
<h2>Return Values</h2>
<p>If conversion depends on the locale and the current locale is not supported, the function returns <code>XLocaleNotSupported</code>. In both of these cases, the function does not set <i>text_prop_return</i>. </p>
<p> To determine whether the function is guaranteed not to return <code>XLocaleNotSupported</code>, use <code>XSupportsLocale</code>.</p>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmcvtxmstringtobytestream/">XmCvtXmStringToByteStream</a></code>(3), <code><a href="/docs/linux/man/3-xmcvttextpropertytoxmstringtable/">XmCvtTextPropertyToXmStringTable</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringtable/">XmStringTable</a></code>(3).</p>
