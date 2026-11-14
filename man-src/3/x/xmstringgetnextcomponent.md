---
title: "xmstringgetnextcomponent(3)"
name: "xmstringgetnextcomponent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringgetnextcomponent/"
description: "XmStringGetNextComponent — A compound string function that returns the type and value of the next component in a compound string"
---

<p><code>XmStringGetNextComponent</code> &#8212; A compound string function that returns the type and value of the next component in a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmStringComponentType XmStringGetNextComponent</code>(
<code>XmStringContext context</code>,
<code>char **text</code>,
<code>XmStringTag *tag</code>,
<code>XmStringDirection *direction</code>,
<code>XmStringComponentType *unknown_tag</code>,
<code>unsigned short *unknown_length</code>,
<code>unsigned char **unknown_value</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. It is replaced by <code>XmStringGetNextTriple</code>. <code>XmStringGetNextComponent</code> returns the type and value of the next component in the compound string identified by <i>context</i>. Components are returned one at a time. On return, only some output parameters will be valid; which ones can be determined by examining the returned component type. The following table describes the valid returns for each component type. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Valid Fields</code></td>
<td><code>Component Type</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><i>tag</i></td>
<td> <code>XmSTRING_COMPONENT_LOCALE, XmSTRING_COMPONENT_TAG</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><i>text</i></td>
<td> <code>XmSTRING_COMPONENT_LOCALE_TEXT, XmSTRING_COMPONENT_TEXT, XmSTRING_COMPONENT_WIDECHAR_TEXT</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><i>direction</i></td>
<td><code>XmSTRING_COMPONENT_DIRECTION</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>unknown_tag, unknown_length, unknown_value</i> </td>
<td> <code>XmSTRING_COMPONENT_LAYOUT_POP, XmSTRING_COMPONENT_LAYOUT_PUSH, XmSTRING_COMPONENT_TAB, XmSTRING_COMPONENT_RENDITION_BEGIN, XmSTRING_COMPONENT_RENDITION_END</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><i>no valid field</i></td>
<td> <code>XmSTRING_COMPONENT_SEPARATOR, XmSTRING_COMPONENT_END, XmSTRING_COMPONENT_UNKNOWN</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<p> Note that several components produce a return value of <code>XmSTRING_COMPONENT_UNKNOWN</code>. The data returned by these components is returned in the <i>unknown_tag</i>, <i>unknown_length</i>, and <i>unknown_value</i> fields. This apparent inconsistency is designed to accomodate older applications that may not be equipped to handle the newer component types of Motif version 2.0 and beyond. Consequently, the use of this procedure is not recommended. Instead, use the <code>XmStringGetNextTriple</code> procedure, which provides all the functionality of <code>XmStringGetNextComponent</code>, and is fully compatible with the newer component types. </p>
<p> If the function return value is <code>XmSTRING_COMPONENT_LOCALE_TEXT</code> or <code>XmSTRING_COMPONENT_TEXT</code>, the the function allocates space to hold the returned <i>text</i>. If the function return value is <code>XmSTRING_COMPONENT_FONTLIST_ELEMENT_TAG</code>, or <code>XmSTRING_COMPONENT_TAG</code>, then the function allocates space to hold the returned <i>tag</i>. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the string context structure that was allocated by the <code>XmStringInitContext</code> function.</p>
<dt><i>text</i></p>
<dd>Specifies a pointer to a NULL terminated string.</p>
<dt><i>tag</i></p>
<dd>Specifies a pointer to the tag component associated with the text. The value <code>XmFONTLIST_DEFAULT_TAG</code> identifies a locale text segment.</p>
<dt><i>direction</i></p>
<dd>Specifies a pointer to the direction of the text.</p>
<dt><i>unknown_tag</i></p>
<dd>Specifies a pointer to the tag of an unknown component.</p>
<dt><i>unknown_length</i></p>
<dd>Specifies a pointer to the length of an unknown component.</p>
<dt><i>unknown_value</i></p>
<dd>Specifies a pointer to the value of an unknown component.</dl>
<h2>Return</h2>
<p>Returns the type of component found. Refer to the <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3) reference page for a list of component types.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringinitcontext/">XmStringInitContext</a></code>(3).</p>
