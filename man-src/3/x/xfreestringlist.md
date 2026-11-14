---
title: "xfreestringlist(3)"
name: "xfreestringlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfreestringlist/"
description: "XStringListToTextProperty, XTextPropertyToStringList, XFreeStringList, XTextProperty – convert string lists and text property structure"
---

<p>XStringListToTextProperty, XTextPropertyToStringList, XFreeStringList, XTextProperty &#8211; convert string lists and text property structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XStringListToTextProperty(char **<i>list</i>, int <i>count</i>, XTextProperty *<i>text_prop_return</i>);</p>
<dd>Status XTextPropertyToStringList(XTextProperty *<i>text_prop</i>, char ***<i>list_return</i>, int *<i>count_return</i>);</p>
<dd>void XFreeStringList(char **<i>list</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>count</i></p>
<dd>Specifies the number of strings.</p>
<dt><i>count_return</i></p>
<dd>Returns the number of strings.</p>
<dt><i>list</i></p>
<dd>Specifies the list of strings to be freed.</p>
<dt><i>list</i></p>
<dd>Specifies a list of null-terminated character strings.</p>
<dt><i>list_return</i></p>
<dd>Returns a list of null-terminated character strings.</p>
<dt><i>text_prop</i></p>
<dd>Specifies the <code>XTextProperty</code> structure to be used.</p>
<dt><i>text_prop_return</i></p>
<dd>Returns the <code>XTextProperty</code> structure.</dl>
<h2>Description</h2>
<p>The <code>XStringListToTextProperty</code> function sets the specified <code>XTextProperty</code> to be of type STRING (format 8) with a value representing the concatenation of the specified list of null-separated character strings. An extra null byte (which is not included in the nitems member) is stored at the end of the value field of text_prop_return. The strings are assumed (without verification) to be in the STRING encoding. If insufficient memory is available for the new value string, <code>XStringListToTextProperty</code> does not set any fields in the <code>XTextProperty</code> structure and returns a zero status. Otherwise, it returns a nonzero status. To free the storage for the value field, use <code>XFree</code>. </p>
<p> The <code>XTextPropertyToStringList</code> function returns a list of strings representing the null-separated elements of the specified <code>XTextProperty</code> structure. The data in text_prop must be of type STRING and format 8. Multiple elements of the property (for example, the strings in a disjoint text selection) are separated by NULL (encoding 0). The contents of the property are not null-terminated. If insufficient memory is available for the list and its elements, <code>XTextPropertyToStringList</code> sets no return values and returns a zero status. Otherwise, it returns a nonzero status. To free the storage for the list and its contents, use <code>XFreeStringList</code>. </p>
<p> The <code>XFreeStringList</code> function releases memory allocated by <code>XmbTextPropertyToTextList</code>, <code>Xutf8TextPropertyToTextList</code> and <code>XTextPropertyToStringList</code> and the missing charset list allocated by <code>XCreateFontSet</code>.</p>
<h2>Structures</h2>
<p>The <code>XTextProperty</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;*value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;property data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Atom encoding;&nbsp;<wbr>&nbsp;/*&nbsp;type of property&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int format;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;8, 16, or 32&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long nitems;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;number of items in value&nbsp;*/ } XTextProperty;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
