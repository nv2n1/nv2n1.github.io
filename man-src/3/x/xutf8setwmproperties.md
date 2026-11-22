---
title: "xutf8setwmproperties(3)"
name: "xutf8setwmproperties"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xutf8setwmproperties/"
description: "XSetWMProperties, XmbSetWMProperties, Xutf8SetWMProperties – set standard window properties"
---

<p>XSetWMProperties, XmbSetWMProperties, Xutf8SetWMProperties &#8211; set standard window properties </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XSetWMProperties(Display *<i>display</i>, Window <i>w</i>, XTextProperty *<i>window_name</i>, XTextProperty *<i>icon_name</i>, char **<i>argv</i>, int <i>argc</i>, XSizeHints *<i>normal_hints</i>, XWMHints *<i>wm_hints</i>, XClassHint *<i>class_hints</i>);</dd>
<dd>void XmbSetWMProperties(Display *<i>display</i>, Window <i>w</i>, char *<i>window_name</i>, char *<i>icon_name</i>, char *<i>argv</i>[], int <i>argc</i>, XSizeHints *<i>normal_hints</i>, XWMHints *<i>wm_hints</i>, XClassHint *<i>class_hints</i>);</dd>
<dd>void Xutf8SetWMProperties(Display *<i>display</i>, Window <i>w</i>, char *<i>window_name</i>, char *<i>icon_name</i>, char *<i>argv</i>[], int <i>argc</i>, XSizeHints *<i>normal_hints</i>, XWMHints *<i>wm_hints</i>, XClassHint *<i>class_hints</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>argc</i></dt>
<dd>Specifies the number of arguments.</dd>
<dt><i>argv</i></dt>
<dd>Specifies the application&#8217;s argument list.</dd>
<dt><i>class_hints</i></dt>
<dd>Specifies the <code>XClassHint</code> structure to be used.</dd>
<dt><i>display</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>icon_name</i></dt>
<dd>Specifies the icon name, which should be a null-terminated string.</dd>
<dt><i>normal_hints</i></dt>
<dd>Specifies the size hints for the window in its normal state.</dd>
<dt><i>w</i></dt>
<dd>Specifies the window.</dd>
<dt><i>window_name</i></dt>
<dd>Specifies the window name, which should be a null-terminated string.</dd>
<dt><i>wm_hints</i></dt>
<dd>Specifies the <code>XWMHints</code> structure to be used.</dd></dl>
<h2>Description</h2>
<p>The <code>XSetWMProperties</code> convenience function provides a single programming interface for setting those essential window properties that are used for communicating with other clients (particularly window and session managers). </p>
<p> If the window_name argument is non-NULL, <code>XSetWMProperties</code> calls <code>XSetWMName</code>, which in turn, sets the WM_NAME property (see section 14.1.4). If the icon_name argument is non-NULL, <code>XSetWMProperties</code> calls <code>XSetWMIconName</code>, which sets the WM_ICON_NAME property (see section 14.1.5). If the argv argument is non-NULL, <code>XSetWMProperties</code> calls <code>XSetCommand</code>, which sets the WM_COMMAND property (see section 14.2.1). Note that an argc of zero is allowed to indicate a zero-length command. Note also that the hostname of this machine is stored using <code>XSetWMClientMachine</code> (see section 14.2.2). </p>
<p> If the normal_hints argument is non-NULL, <code>XSetWMProperties</code> calls <code>XSetWMNormalHints</code>, which sets the WM_NORMAL_HINTS property (see section 14.1.7). If the wm_hints argument is non-NULL, <code>XSetWMProperties</code> calls <code>XSetWMHints</code>, which sets the WM_HINTS property (see section 14.1.6). </p>
<p> If the class_hints argument is non-NULL, <code>XSetWMProperties</code> calls <code>XSetClassHint</code>, which sets the WM_CLASS property (see section 14.1.8). If the res_name member in the <code>XClassHint</code> structure is set to the NULL pointer and the RESOURCE_NAME environment variable is set, then the value of the environment variable is substituted for res_name. If the res_name member is NULL, the environment variable is not set, and argv and argv[0] are set, then the value of argv[0], stripped of any directory prefixes, is substituted for res_name. </p>
<p> The <code>XmbSetWMProperties</code> and <code>Xutf8SetWMProperties</code> convenience functions provide a simple programming interface for setting those essential window properties that are used for communicating with other clients (particularly window and session managers). </p>
<p> If the window_name argument is non-NULL, they set the WM_NAME property. If the icon_name argument is non-NULL, they set the WM_ICON_NAME property. The window_name and icon_name arguments are null-terminated strings, for <code>XmbSetWMProperties</code> in the encoding of the current locale, for <code>Xutf8SetWMProperties</code> in UTF-8 encoding. If the arguments can be fully converted to the STRING encoding, the properties are created with type &#8220;STRING&#8221;; otherwise, the arguments are converted to Compound Text, and the properties are created with type &#8220;COMPOUND_TEXT&#8221;. </p>
<p> If the normal_hints argument is non-NULL, <code>XmbSetWMProperties</code> and <code>Xutf8SetWMProperties</code> call <code>XSetWMNormalHints</code>, which sets the WM_NORMAL_HINTS property (see section 14.1.7). If the wm_hints argument is non-NULL, <code>XmbSetWMProperties</code> and <code>Xutf8SetWMProperties</code> call <code>XSetWMHints</code>, which sets the WM_HINTS property (see section 14.1.6). </p>
<p> If the argv argument is non-NULL, <code>XmbSetWMProperties</code> and <code>Xutf8SetWMProperties</code> set the WM_COMMAND property from argv and argc. An argc of zero indicates a zero-length command. </p>
<p> The hostname of the machine is stored using <code>XSetWMClientMachine</code> (see section 14.2.2). </p>
<p> If the class_hints argument is non-NULL, <code>XmbSetWMProperties</code> and <code>Xutf8SetWMProperties</code> set the WM_CLASS property. If the res_name member in the <code>XClassHint</code> structure is set to the NULL pointer and the RESOURCE_NAME environment variable is set, the value of the environment variable is substituted for res_name. If the res_name member is NULL, the environment variable is not set, and argv and argv[0] are set, then the value of argv[0], stripped of any directory prefixes, is substituted for res_name. </p>
<p> It is assumed that the supplied class_hints.res_name and argv, the RESOURCE_NAME environment variable, and the hostname of the machine are in the encoding of the current locale. The corresponding WM_CLASS, WM_COMMAND, and WM_CLIENT_MACHINE properties are typed according to the local host locale announcer. No encoding conversion is performed for these strings prior to storage in the properties. </p>
<p> For clients that need to process the property text in a locale, <code>XmbSetWMProperties</code> and <code>Xutf8SetWMProperties</code> set the WM_LOCALE_NAME property to be the name of the current locale. The name is assumed to be in the Host Portable Character Encoding and is converted to STRING for storage in the property. </p>
<p> <code>XSetWMProperties</code>, <code>XmbSetWMProperties</code> and <code>Xutf8SetWMProperties</code> can generate <code>BadAlloc</code> and <code>BadWindow</code> errors. </p>
<p> The function <code>Xutf8SetWMProperties</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>Properties</h2>
<dl COMPACT>
<dt>WM_CLASS</dt>
<dd>Set by application programs to allow window and session managers to obtain the application&#8217;s resources from the resource database.</dd>
<dt>WM_CLIENT_MACHINE</dt>
<dd>The string name of the machine on which the client application is running.</dd>
<dt>WM_COMMAND</dt>
<dd>The command and arguments, null-separated, used to invoke the application.</dd>
<dt>WM_HINTS</dt>
<dd>Additional hints set by the client for use by the window manager. The C type of this property is <code>XWMHints</code>.</dd>
<dt>WM_ICON_NAME</dt>
<dd>The name to be used in an icon.</dd>
<dt>WM_NAME</dt>
<dd>The name of the application.</dd>
<dt>WM_NORMAL_HINTS</dt>
<dd>Size hints for a window in its normal state. The C type of this property is <code>XSizeHints</code>.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></dt>
<dd>The server failed to allocate the requested resource or server memory.</dd>
<dt><code>BadWindow</code></dt>
<dd>A value for a Window argument does not name a defined Window.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallocclasshint/">XAllocClassHint</a>(3), <a href="/docs/linux/man/3-xallociconsize/">XAllocIconSize</a>(3), <a href="/docs/linux/man/3-xallocsizehints/">XAllocSizeHints</a>(3), <a href="/docs/linux/man/3-xallocwmhints/">XAllocWMHints</a>(3), <a href="/docs/linux/man/3-xparsegeometry/">XParseGeometry</a>(3), <a href="/docs/linux/man/3-xsetcommand/">XSetCommand</a>(3), <a href="/docs/linux/man/3-xsettransientforhint/">XSetTransientForHint</a>(3), <a href="/docs/linux/man/3-xsettextproperty/">XSetTextProperty</a>(3), <a href="/docs/linux/man/3-xsetwmclientmachine/">XSetWMClientMachine</a>(3), <a href="/docs/linux/man/3-xsetwmcolormapwindows/">XSetWMColormapWindows</a>(3), <a href="/docs/linux/man/3-xsetwmiconname/">XSetWMIconName</a>(3), <a href="/docs/linux/man/3-xsetwmname/">XSetWMName</a>(3), <a href="/docs/linux/man/3-xsetwmprotocols/">XSetWMProtocols</a>(3), <a href="/docs/linux/man/3-xstringlisttotextproperty/">XStringListToTextProperty</a>(3), XTextListToTextProperty(3)<br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
