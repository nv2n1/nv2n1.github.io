---
title: "xdestroyoc(3)"
name: "xdestroyoc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdestroyoc/"
description: "XCreateOC, XDestroyOC, XSetOCValues, XGetOCValues, XOMOfOC – create output contexts"
---

<p>XCreateOC, XDestroyOC, XSetOCValues, XGetOCValues, XOMOfOC &#8211; create output contexts </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XOC XCreateOC(XOM <i>om</i>);</dd>
<dd>void XDestroyOC(XOC <i>oc</i>);</dd>
<dd>char * XSetOCValues(XOC <i>oc</i>, &#8230;);</dd>
<dd>char * XGetOCValues(XOC <i>oc</i>, &#8230;);</dd>
<dd>XOM XOMOfOC(XOC <i>oc</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>oc</i></dt>
<dd>Specifies the output context.</dd>
<dt><i>om</i></dt>
<dd>Specifies the output method.</dd>
<dt>&#8230;</dt>
<dd>Specifies the variable length argument list to set or get XOC values.</dd></dl>
<h2>Description</h2>
<p>The <code>XCreateOC</code> function creates an output context within the specified output method. </p>
<p> The base font names argument is mandatory at creation time, and the output context will not be created unless it is provided. All other output context values can be set later. </p>
<p> <code>XCreateOC</code> returns NULL if no output context could be created. NULL can be returned for any of the following reasons:</p>
<dl COMPACT>
<dt>&bull;</dt>
<dd>A required argument was not set.</dd>
<dt>&bull;</dt>
<dd>A read-only argument was set.</dd>
<dt>&bull;</dt>
<dd>An argument name is not recognized.</dd>
<dt>&bull;</dt>
<dd>The output method encountered an output method implementation-dependent error.</dd></dl>
<p> The <code>XDestroyOC</code> function destroys the specified output context. </p>
<p> The <code>XSetOCValues</code> function returns NULL if no error occurred; otherwise, it returns the name of the first argument that could not be set. An argument might not be set for any of the following reasons:</p>
<dl COMPACT>
<dt>&bull;</dt>
<dd>The argument is read-only.</dd>
<dt>&bull;</dt>
<dd>The argument name is not recognized.</dd>
<dt>&bull;</dt>
<dd>An implementation-dependent error occurs.</dd></dl>
<p> Each value to be set must be an appropriate datum, matching the data type imposed by the semantics of the argument. </p>
<p> The <code>XGetOCValues</code> function returns NULL if no error occurred; otherwise, it returns the name of the first argument that could not be obtained. An argument might not be obtained for any of the following reasons:</p>
<dl COMPACT>
<dt>&bull;</dt>
<dd>The argument name is not recognized.</dd>
<dt>&bull;</dt>
<dd>An implementation-dependent error occurs.</dd></dl>
<p> Each argument value following a name must point to a location where the value is to be stored. </p>
<p> The <code>XOMOfOC</code> function returns the output method associated with the specified output context.</p>
<h2>See Also</h2>
<p>XCreateOM(3), <a href="/docs/linux/man/3-xcreatefontset/">XCreateFontSet</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
