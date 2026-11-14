---
title: "xgetomvalues(3)"
name: "xgetomvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetomvalues/"
description: "XOpenOM, XCloseOM, XSetOMValues, XGetOMValues, XDisplayOfOM, XLocaleOfOM – open output methods"
---

<p>XOpenOM, XCloseOM, XSetOMValues, XGetOMValues, XDisplayOfOM, XLocaleOfOM &#8211; open output methods </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XOM XOpenOM(Display *<i>display</i>, XrmDatabase <i>db</i>, char *<i>res_name</i>, char *<i>res_class</i>);</p>
<dd>Status XCloseOM(XOM <i>om</i>);</p>
<dd>char *XSetOMValues(XOM <i>om</i>);</p>
<dd>char *XGetOMValues(XOM <i>om</i>);</p>
<dd>Display *XDisplayOfOM(XOM <i>om</i>);</p>
<dd>char *XLocaleOfOM(XOM <i>om</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>db</i></p>
<dd>Specifies a pointer to the resource database.</p>
<dt><i>res_name</i></p>
<dd>Specifies the full resource name of the application.</p>
<dt><i>res_class</i></p>
<dd>Specifies the full class name of the application.</p>
<dt><i>om</i></p>
<dd>Specifies the output method.</p>
<dt>&#8230;</p>
<dd>Specifies the variable length argument list to set or get XOM values.</dl>
<h2>Description</h2>
<p>The <code>XOpenOM</code> function opens an output method matching the current locale and modifiers specification. The current locale and modifiers are bound to the output method when <code>XOpenOM</code> is called. The locale associated with an output method cannot be changed. </p>
<p> The specific output method to which this call will be routed is identified on the basis of the current locale and modifiers. <code>XOpenOM</code> will identify a default output method corresponding to the current locale. That default can be modified using <code>XSetLocaleModifiers</code> to set the output method modifier. </p>
<p> The db argument is the resource database to be used by the output method for looking up resources that are private to the output method. It is not intended that this database be used to look up values that can be set as OC values in an output context. If db is NULL, no database is passed to the output method. </p>
<p> The res_name and res_class arguments specify the resource name and class of the application. They are intended to be used as prefixes by the output method when looking up resources that are common to all output contexts that may be created for this output method. The characters used for resource names and classes must be in the X Portable Character Set. The resources looked up are not fully specified if res_name or res_class is NULL. </p>
<p> The res_name and res_class arguments are not assumed to exist beyond the call to <code>XOpenOM</code>. The specified resource database is assumed to exist for the lifetime of the output method. </p>
<p> <code>XOpenOM</code> returns NULL if no output method could be opened. </p>
<p> The <code>XCloseOM</code> function closes the specified output method. </p>
<p> The <code>XSetOMValues</code> function presents a variable argument list programming interface for setting properties or features of the specified output method. This function returns NULL if it succeeds; otherwise, it returns the name of the first argument that could not be set. Xlib does not attempt to set arguments from the supplied list that follow the failed argument; all arguments in the list preceding the failed argument have been set correctly. </p>
<p> No standard arguments are currently defined by Xlib. </p>
<p> The <code>XGetOMValues</code> function presents a variable argument list programming interface for querying properties or features of the specified output method. This function returns NULL if it succeeds; otherwise, it returns the name of the first argument that could not be obtained. </p>
<p> The <code>XDisplayOfOM</code> function returns the display associated with the specified output method. </p>
<p> The <code>XLocaleOfOM</code> returns the locale associated with the specified output method.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreateoc/">XCreateOC</a>(3), <a href="/docs/linux/man/3-xcreatefontset/">XCreateFontSet</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
