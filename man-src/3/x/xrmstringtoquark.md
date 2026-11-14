---
title: "xrmstringtoquark(3)"
name: "xrmstringtoquark"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrmstringtoquark/"
description: "XrmUniqueQuark, XrmStringToQuark, XrmPermStringToQuark, XrmQuarkToString, XrmStringToQuarkList, XrmStringToBindingQuarkList – manipulate resource quarks"
---

<p>XrmUniqueQuark, XrmStringToQuark, XrmPermStringToQuark, XrmQuarkToString, XrmStringToQuarkList, XrmStringToBindingQuarkList &#8211; manipulate resource quarks </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> #include &lt;X11/Xresource.h&gt;</p>
<dd>XrmQuark XrmUniqueQuark(void);</dl>
<p> #define XrmStringToName(string) XrmStringToQuark(string)<br />
 #define XrmStringToClass(string) XrmStringToQuark(string)<br />
 #define XrmStringToRepresentation(string) XrmStringToQuark(string)</p>
<dl COMPACT>
<dd>int XrmQuark XrmStringToQuark(char *<i>string</i>);</p>
<dd>XrmQuark XrmPermStringToQuark(char *<i>string</i>);</dl>
<p> #define XrmStringToName(string) XrmStringToQuark(string)<br />
 #define XrmStringToClass(string) XrmStringToQuark(string)<br />
 #define XrmStringToRepresentation(string) XrmStringToQuark(string)</p>
<dl COMPACT>
<dd>XrmQuark XrmStringToQuark(char *<i>string</i>);</p>
<dd>XrmQuark XrmPermStringToQuark(char *<i>string</i>);</dl>
<p> #define XrmNameToString(name) XrmQuarkToString(name)<br />
 #define XrmClassToString(class) XrmQuarkToString(class)<br />
 #define XrmRepresentationToString(type) XrmQuarkToString(type)</p>
<dl COMPACT>
<dd>char *XrmQuarkToString(XrmQuark <i>quark</i>);</dl>
<p> #define XrmStringToNameList(str, name) XrmStringToQuarkList((str), (name))<br />
 #define XrmStringToClassList(str,class) XrmStringToQuarkList((str), (class)) </p>
<dl COMPACT>
<dd>void XrmStringToQuarkList(char *<i>string</i>, XrmQuarkList <i>quarks_return</i>);</p>
<dd>XrmStringToBindingQuarkList(char *<i>string</i>, XrmBindingList <i>bindings_return</i>, XrmQuarkList <i>quarks_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>bindings_return</i></p>
<dd>Returns the binding list.</p>
<dt><i>quark</i></p>
<dd>Specifies the quark for which the equivalent string is desired.</p>
<dt><i>quarks_return</i></p>
<dd>Returns the list of quarks.</p>
<dt><i>string</i></p>
<dd>Specifies the string for which a quark or quark list is to be allocated.</dl>
<h2>Description</h2>
<p>The <code>XrmUniqueQuark</code> function allocates a quark that is guaranteed not to represent any string that is known to the resource manager. </p>
<p> These functions can be used to convert from string to quark representation. If the string is not in the Host Portable Character Encoding, the conversion is implementation-dependent. The string argument to <code>XrmStringToQuark</code> need not be permanently allocated storage. <code>XrmPermStringToQuark</code> is just like <code>XrmStringToQuark</code>, except that Xlib is permitted to assume the string argument is permanently allocated, and, hence, that it can be used as the value to be returned by <code>XrmQuarkToString</code>. </p>
<p> For any given quark, if <code>XrmStringToQuark</code> returns a non-NULL value, all future calls will return the same value (identical address). </p>
<p> These functions can be used to convert from quark representation to string. The string pointed to by the return value must not be modified or freed. The returned string is byte-for-byte equal to the original string passed to one of the string-to-quark routines. If no string exists for that quark, <code>XrmQuarkToString</code> returns NULL. For any given quark, if <code>XrmQuarkToString</code> returns a non-NULL value, all future calls will return the same value (identical address). </p>
<p> These functions can be used to convert from string to quark representation. If the string is not in the Host Portable Character Encoding, the conversion is implementation-dependent. The string argument to <code>XrmStringToQuark</code> need not be permanently allocated storage. <code>XrmPermStringToQuark</code> is just like <code>XrmStringToQuark</code>, except that Xlib is permitted to assume the string argument is permanently allocated, and, hence, that it can be used as the value to be returned by <code>XrmQuarkToString</code>. </p>
<p> For any given quark, if <code>XrmStringToQuark</code> returns a non-NULL value, all future calls will return the same value (identical address). </p>
<p> The <code>XrmStringToQuarkList</code> function converts the null-terminated string (generally a fully qualified name) to a list of quarks. The caller must allocate sufficient space for the quarks list before calling <code>XrmStringToQuarkList</code>. Note that the string must be in the valid ResourceName format (see section 15.1). If the string is not in the Host Portable Character Encoding, the conversion is implementation-dependent. </p>
<p> A binding list is a list of type <code>XrmBindingList</code> and indicates if components of name or class lists are bound tightly or loosely (that is, if wildcarding of intermediate components is specified). </p>
<p> typedef enum {XrmBindTightly, XrmBindLoosely} XrmBinding, *XrmBindingList; </p>
<p> <code>XrmBindTightly</code> indicates that a period separates the components, and <code>XrmBindLoosely</code> indicates that an asterisk separates the components. </p>
<p> The <code>XrmStringToBindingQuarkList</code> function converts the specified string to a binding list and a quark list. The caller must allocate sufficient space for the quarks list and the binding list before calling <code>XrmStringToBindingQuarkList</code>. If the string is not in the Host Portable Character Encoding the conversion is implementation-dependent. Component names in the list are separated by a period or an asterisk character. If the string does not start with period or asterisk, a period is assumed. For example, &#8220;*a.b*c&#8221; becomes: </p>
<table>
<tr VALIGN=top>
<td>quarks</td>
<td>a</td>
<td>b</td>
<td>c
</td>
</tr>
<tr VALIGN=top>
<td>bindings</td>
<td>loose</td>
<td>tight</td>
<td>loose
</td>
</tr>
</table>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xrmgetresource/">XrmGetResource</a>(3), <a href="/docs/linux/man/3-xrminitialize/">XrmInitialize</a>(3), <a href="/docs/linux/man/3-xrmmergedatabases/">XrmMergeDatabases</a>(3), <a href="/docs/linux/man/3-xrmputresource/">XrmPutResource</a>(3) </p>
<p> <i>Xlib &#8211; C Language X Interface</i></p>
