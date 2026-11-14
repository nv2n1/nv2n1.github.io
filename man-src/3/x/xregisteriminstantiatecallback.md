---
title: "xregisteriminstantiatecallback(3)"
name: "xregisteriminstantiatecallback"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xregisteriminstantiatecallback/"
description: "XOpenIM, XCloseIM, XSetIMValues, XGetIMValues, XDisplayOfIM, XLocaleOfIM, XRegisterIMInstantiateCallback, XUnregisterIMInstantiateCallback – open, close, and obtain input method information"
---

<p>XOpenIM, XCloseIM, XSetIMValues, XGetIMValues, XDisplayOfIM, XLocaleOfIM, XRegisterIMInstantiateCallback, XUnregisterIMInstantiateCallback &#8211; open, close, and obtain input method information </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XIM XOpenIM(Display *<i>display</i>, XrmDatabase <i>db</i>, char *<i>res_name</i>, char *<i>res_class</i>);</p>
<dd>Status XCloseIM(XIM <i>im</i>);</p>
<dd>char *XSetIMValues(XIM <i>im</i>, &#8230;);</p>
<dd>char *XGetIMValues(XIM <i>im</i>, &#8230;);</p>
<dd>Display *XDisplayOfIM(XIM <i>im</i>);</p>
<dd>char *XLocaleOfIM(XIM <i>im</i>);</p>
<dd>Bool XRegisterIMInstantiateCallback(Display *<i>display</i>, XrmDatabase <i>db</i>, char *<i>res_name</i>, char *<i>res_class</i>, XIDProc <i>callback</i>, XPointer <i>client_data</i>);</p>
<dd>Bool XUnregisterIMInstantiateCallback(Display *<i>display</i>, XrmDatabase <i>db</i>, char *<i>res_name</i>, char *<i>res_class</i>, XIDProc <i>callback</i>, XPointer <i>client_data</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>callback</i></p>
<dd>Specifies a pointer to the input method instantiate callback.</p>
<dt><i>client_data</i></p>
<dd>Specifies the additional client data.</p>
<dt><i>db</i></p>
<dd>Specifies a pointer to the resource database.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>im</i></p>
<dd>Specifies the input method.</p>
<dt><i>res_class</i></p>
<dd>Specifies the full class name of the application.</p>
<dt><i>res_name</i></p>
<dd>Specifies the full resource name of the application.</p>
<dt>&#8230;</p>
<dd>Specifies the variable length argument list to set or get XIM values.</dl>
<h2>Description</h2>
<p>The <code>XOpenIM</code> function opens an input method, matching the current locale and modifiers specification. Current locale and modifiers are bound to the input method at opening time. The locale associated with an input method cannot be changed dynamically. This implies that the strings returned by <code>XmbLookupString</code> or <code>XwcLookupString</code>, for any input context affiliated with a given input method will be encoded in the locale current at the time the input method is opened. </p>
<p> The specific input method to which this call will be routed is identified on the basis of the current locale. <code>XOpenIM</code> will identify a default input method corresponding to the current locale. That default can be modified using <code>XSetLocaleModifiers</code> for the input method modifier. </p>
<p> The db argument is the resource database to be used by the input method for looking up resources that are private to the input method. It is not intended that this database be used to look up values that can be set as IC values in an input context. If db is NULL, no database is passed to the input method. </p>
<p> The res_name and res_class arguments specify the resource name and class of the application. They are intended to be used as prefixes by the input method when looking up resources that are common to all input contexts that may be created for this input method. The characters used for resource names and classes must be in the X Portable Character Set. The resources looked up are not fully specified if res_name or res_class is NULL. </p>
<p> The res_name and res_class arguments are not assumed to exist beyond the call to <code>XOpenIM</code>. The specified resource database is assumed to exist for the lifetime of the input method. </p>
<p> <code>XOpenIM</code> returns NULL if no input method could be opened. </p>
<p> The <code>XCloseIM</code> function closes the specified input method. </p>
<p> The <code>XSetIMValues</code> function presents a variable argument list programming interface for setting attributes of the specified input method. It returns NULL if it succeeds; otherwise, it returns the name of the first argument that could not be set. Xlib does not attempt to set arguments from the supplied list that follow the failed argument; all arguments in the list preceding the failed argument have been set correctly. </p>
<p> The <code>XGetIMValues</code> function presents a variable argument list programming interface for querying properties or features of the specified input method. This function returns NULL if it succeeds; otherwise, it returns the name of the first argument that could not be obtained. </p>
<p> Each XIM value argument (following a name) must point to a location where the XIM value is to be stored. That is, if the XIM value is of type T, the argument must be of type T*. If T itself is a pointer type, then <code>XGetIMValues</code> allocates memory to store the actual data, and the client is responsible for freeing this data by calling <code>XFree</code> with the returned pointer. </p>
<p> The <code>XDisplayOfIM</code> function returns the display associated with the specified input method. </p>
<p> The <code>XLocaleOfIM</code> function returns the locale associated with the specified input method. </p>
<p> The <code>XRegisterIMInstantiateCallback</code> function registers a callback to be invoked whenever a new input method becomes available for the specified display that matches the current locale and modifiers. </p>
<p> The function returns <code>True</code> if it succeeds; otherwise, it returns <code>False</code>. </p>
<p> The <code>XUnregisterIMInstantiateCallback</code> function removes an input method instantiation callback previously registered. The function returns <code>True</code> if it succeeds; otherwise, it returns <code>False</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreateic/">XCreateIC</a>(3), <a href="/docs/linux/man/3-xseticfocus/">XSetICFocus</a>(3), <a href="/docs/linux/man/3-xseticvalues/">XSetICValues</a>(3), <a href="/docs/linux/man/3-xmbresetic/">XmbResetIC</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
