---
title: "xtconvertandstore(3)"
name: "xtconvertandstore"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtconvertandstore/"
description: "XtConvertAndStore, XtCallConverter – invoke resource converters"
---

<p>XtConvertAndStore, XtCallConverter &#8211; invoke resource converters </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Boolean XtConvertAndStore(Widget <i>widget</i>, const char *<i>from_type</i>, XrmValuePtr <i>from</i>, const char *<i>to_type</i>, XrmValuePtr <i>to_in_out</i>);</p>
<dd>Boolean XtCallConverter(Display* <i>dpy</i>, XtTypeConverter <i>converter</i>, XrmValuePtr <i>args</i>, Cardinal <i>num_args</i>, XrmValuePtr <i>from</i>, XrmValuePtr <i>to_in_out</i>, XtCacheRef* <i>cache_ref_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>args</i></p>
<dd>Specifies the argument list that contains the additional arguments needed to perform the conversion, or NULL.</p>
<dt><i>converter</i></p>
<dd>Specifies the conversion procedure that is to be called.</p>
<dt><i>from</i></p>
<dd>Specifies the value to be converted.</p>
<dt><i>from_type</i></p>
<dd>Specifies the source type.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of additional arguments (often zero).</p>
<dt><i>to_type</i></p>
<dd>Specifies the destination type.</p>
<dt><i>to_in_out</i></p>
<dd>Returns the converted value.</p>
<dt><i>widget</i></p>
<dd>Specifies the widget to use for additional arguments, if any are needed, and the destroy callback list.</p>
<dt><i>dpy</i></p>
<dd>Specifies the display with which the conversion is to be associated.</dl>
<h2>Description</h2>
<p>The <code>XtConvertAndStore</code> function looks up the type converter registered to convert from_type to to_type, computes any additional arguments needed, and then calls <code>XtCallConverter</code>. (or <code>XtDirectConvert</code> if an old-style converter was registered with <code>XtAddConverter</code> or <code>XtAppAddConverter</code>. ) with the from and to_in_out arguments. </p>
<p> The <code>XtCallConverter</code> function looks up the specified type converter in the application context associated with the display and, if the converter was not registered or was registered with cache type <code>XtCacheAll</code> or <code>XtCacheByDisplay</code> looks in the conversion cache to see if this conversion procedure has been called with the specified conversion arguments. If so, it checks the success status of the prior call, and if the conversion failed, <code>XtCallConverter</code> returns <code>False</code> immediately; otherwise it checks the size specified in the <i>to</i> argument and, if it is greater than or equal to the size stored in the cache, copies the information stored in the cache into the location specified by <i>to-&gt;addr</i>, stores the cache size into <i>to-&gt;size</i>, and returns <code>True</code>. If the size specified in the <i>to</i> argument is smaller than the size stored in the cache, <code>XtCallConverter</code> copies the cache size into the <i>to-&gt;size</i> and returns <code>False</code>. If the converter was registered with cache type <code>XtCacheNone</code> or no value was found in the conversion cache, <code>XtCallConverter</code> calls the converter and, if it was not registered with cache type <code>XtCacheNone</code>, enters the result into the cache. <code>XtCallConverter</code> then returns what the converter returned. </p>
<p> The <i>cache_ref_return</i> field specifies storage allocated by the caller in which an opaque value will be stored. If the type converter has been registered with the <code>XtCacheRefCount</code> modifier and if the value returned in in <i>cache_ref_return</i> is non-NULL, then the call should store the <i>cache_ref_return</i> value in order to decrement the reference count when the converted value is no longer required. The <i>cache_ref_return</i> argument should be NULL if the caller is unwilling or unable to store the value.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappreleasecacherefs/">XtAppReleaseCacheRefs</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
