---
title: "xwctextpropertytotextlist(3)"
name: "xwctextpropertytotextlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xwctextpropertytotextlist/"
description: "XmbTextListToTextProperty, XwcTextListToTextProperty, Xutf8TextListToTextProperty, XmbTextPropertyToTextList, XwcTextPropertyToTextList, Xutf8TextPropertyToTextList, XwcFreeStringList, XDefaultStri..."
---

<p>XmbTextListToTextProperty, XwcTextListToTextProperty, Xutf8TextListToTextProperty, XmbTextPropertyToTextList, XwcTextPropertyToTextList, Xutf8TextPropertyToTextList, XwcFreeStringList, XDefaultString &#8211; convert text lists and text property structures </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XmbTextListToTextProperty(Display *<i>display</i>, char **<i>list</i>, int <i>count</i>, XICCEncodingStyle <i>style</i>, XTextProperty *<i>text_prop_return</i>);</p>
<dd>int XwcTextListToTextProperty(Display *<i>display</i>, wchar_t **<i>list</i>, int <i>count</i>, XICCEncodingStyle <i>style</i>, XTextProperty *<i>text_prop_return</i>);</p>
<dd>int Xutf8TextListToTextProperty(Display *<i>display</i>, char **<i>list</i>, int <i>count</i>, XICCEncodingStyle <i>style</i>, XTextProperty *<i>text_prop_return</i>);</p>
<dd>int XmbTextPropertyToTextList(Display *<i>display</i>, XTextProperty *<i>text_prop</i>, char ***<i>list_return</i>, int *<i>count_return</i>);</p>
<dd>int XwcTextPropertyToTextList(Display *<i>display</i>, XTextProperty *<i>text_prop</i>, wchar_t ***<i>list_return</i>, int *<i>count_return</i>);</p>
<dd>int Xutf8TextPropertyToTextList(Display *<i>display</i>, XTextProperty *<i>text_prop</i>, char ***<i>list_return</i>, int *<i>count_return</i>);</p>
<dd>void XwcFreeStringList(wchar_t **<i>list</i>);</p>
<dd>char *XDefaultString(void)</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>list</i></p>
<dd>Specifies a list of null-terminated character strings.</p>
<dt><i>count</i></p>
<dd>Specifies the number of strings specified.</p>
<dt><i>style</i></p>
<dd>Specifies the manner in which the property is encoded.</p>
<dt><i>text_prop_return</i></p>
<dd>Returns the <code>XTextProperty</code> structure.</p>
<dt><i>text_prop</i></p>
<dd>Specifies the <code>XTextProperty</code> structure to be used.</p>
<dt><i>list_return</i></p>
<dd>Returns a list of null-terminated character strings.</p>
<dt><i>count_return</i></p>
<dd>Returns the number of strings.</p>
<dt><i>list</i></p>
<dd>Specifies the list of strings to be freed.</dl>
<h2>Description</h2>
<p>The <code>XmbTextListToTextProperty</code>, <code>XwcTextListToTextProperty</code> and <code>Xutf8TextListToTextProperty</code> functions set the specified <code>XTextProperty</code> value to a set of null-separated elements representing the concatenation of the specified list of null-terminated text strings. The input text strings must be given in the current locale encoding (for <code>XmbTextListToTextProperty</code> and <code>XwcTextListToTextProperty</code>), or in UTF-8 encoding (for <code>Xutf8TextListToTextProperty</code>). </p>
<p> The functions set the encoding field of text_prop_return to an <code>Atom</code> for the specified display naming the encoding determined by the specified style and convert the specified text list to this encoding for storage in the text_prop_return value field. If the style <code>XStringStyle</code> or <code>XCompoundTextStyle</code> is specified, this encoding is &#8220;STRING&#8221; or &#8220;COMPOUND_TEXT&#8221;, respectively. If the style <code>XUTF8StringStyle</code> is specified, this encoding is &#8220;UTF8_STRING&#8221;. (This is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.) If the style <code>XTextStyle</code> is specified, this encoding is the encoding of the current locale. If the style <code>XStdICCTextStyle</code> is specified, this encoding is &#8220;STRING&#8221; if the text is fully convertible to STRING, else &#8220;COMPOUND_TEXT&#8221;. A final terminating null byte is stored at the end of the value field of text_prop_return but is not included in the nitems member. </p>
<p> If insufficient memory is available for the new value string, the functions return <code>XNoMemory</code>. If the current locale is not supported, the functions return <code>XLocaleNotSupported</code>. In both of these error cases, the functions do not set text_prop_return. </p>
<p> To determine if the functions are guaranteed not to return <code>XLocaleNotSupported</code>, use <code>XSupportsLocale</code>. </p>
<p> If the supplied text is not fully convertible to the specified encoding, the functions return the number of unconvertible characters. Each unconvertible character is converted to an implementation-defined and encoding-specific default string. Otherwise, the functions return <code>Success</code>. Note that full convertibility to all styles except <code>XStringStyle</code> is guaranteed. </p>
<p> To free the storage for the value field, use <code>XFree</code>. </p>
<p> The <code>XmbTextPropertyToTextList</code>, <code>XwcTextPropertyToTextList</code> and <code>Xutf8TextPropertyToTextList</code> functions return a list of text strings representing the null-separated elements of the specified <code>XTextProperty</code> structure. The returned strings are encoded using the current locale encoding (for <code>XmbTextPropertyToTextList</code> and <code>XwcTextPropertyToTextList</code>) or in UTF-8 (for <code>Xutf8TextPropertyToTextList</code>). The data in text_prop must be format 8. </p>
<p> Multiple elements of the property (for example, the strings in a disjoint text selection) are separated by a null byte. The contents of the property are not required to be null-terminated; any terminating null should not be included in text_prop.nitems. </p>
<p> If insufficient memory is available for the list and its elements, <code>XmbTextPropertyToTextList</code>, <code>XwcTextPropertyToTextList</code> and <code>Xutf8TextPropertyToTextList</code> return <code>XNoMemory</code>. If the current locale is not supported, the functions return <code>XLocaleNotSupported</code>. Otherwise, if the encoding field of text_prop is not convertible to the encoding of the current locale, the functions return <code>XConverterNotFound</code>. For supported locales, existence of a converter from COMPOUND_TEXT, STRING, UTF8_STRING or the encoding of the current locale is guaranteed if <code>XSupportsLocale</code> returns <code>True</code> for the current locale (but the actual text may contain unconvertible characters). Conversion of other encodings is implementation-dependent. In all of these error cases, the functions do not set any return values. </p>
<p> Otherwise, <code>XmbTextPropertyToTextList</code>, <code>XwcTextPropertyToTextList</code> and <code>Xutf8TextPropertyToTextList</code> return the list of null-terminated text strings to list_return and the number of text strings to count_return. </p>
<p> If the value field of text_prop is not fully convertible to the encoding of the current locale, the functions return the number of unconvertible characters. Each unconvertible character is converted to a string in the current locale that is specific to the current locale. To obtain the value of this string, use <code>XDefaultString</code>. Otherwise, <code>XmbTextPropertyToTextList</code>, <code>XwcTextPropertyToTextList</code> and <code>Xutf8TextPropertyToTextList</code> return <code>Success</code>. </p>
<p> To free the storage for the list and its contents returned by <code>XmbTextPropertyToTextList</code> or <code>Xutf8TextPropertyToTextList</code>, use <code>XFreeStringList</code>. To free the storage for the list and its contents returned by <code>XwcTextPropertyToTextList</code>, use <code>XwcFreeStringList</code>. </p>
<p> The <code>XwcFreeStringList</code> function frees memory allocated by <code>XwcTextPropertyToTextList</code>. </p>
<p> The <code>XDefaultString</code> function returns the default string used by Xlib for text conversion (for example, in <code>XmbTextPropertyToTextList</code>). The default string is the string in the current locale that is output when an unconvertible character is found during text conversion. If the string returned by <code>XDefaultString</code> is the empty string (&quot;&quot;), no character is output in the converted text. <code>XDefaultString</code> does not return NULL. </p>
<p> The string returned by <code>XDefaultString</code> is independent of the default string for text drawing; see <code>XCreateFontSet</code> to obtain the default string for an <code>XFontSet</code>. </p>
<p> The behavior when an invalid codepoint is supplied to any Xlib function is undefined. </p>
<p> The returned string is null-terminated. It is owned by Xlib and should not be modified or freed by the client. It may be freed after the current locale is changed. Until freed, it will not be modified by Xlib. </p>
<p> The functions <code>Xutf8TextListToTextProperty</code> and <code>Xutf8TextPropertyToTextList</code> are extensions introduced by The XFree86 Project, Inc., in their 4.0.2 release. Their presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>Structures</h2>
<p>The <code>XTextProperty</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;*value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;property data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Atom encoding;&nbsp;<wbr>&nbsp;/*&nbsp;type of property&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int format;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;8, 16, or 32&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long nitems;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;number of items in value&nbsp;*/ } XTextProperty; </p>
<p> The <code>XICCEncodingStyle</code> structure contains: </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>XNoMemory</code> </td>
<td> -1
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>XLocaleNotSupported</code> </td>
<td> -2
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>XConverterNotFound</code> </td>
<td> -3
</td>
</tr>
</table>
<p> typedef enum {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XStringStyle,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;STRING&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XCompoundTextStyle,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;COMPOUND_TEXT&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XTextStyle,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;text in owner&#8217;s encoding&nbsp;(current locale)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XStdICCTextStyle,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;STRING, else COMPOUND_TEXT&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XUTF8StringStyle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;UTF8_STRING&nbsp;*/ } XICCEncodingStyle;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
