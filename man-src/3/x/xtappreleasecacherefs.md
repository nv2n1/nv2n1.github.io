---
title: "xtappreleasecacherefs(3)"
name: "xtappreleasecacherefs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappreleasecacherefs/"
description: "XtAppReleaseCacheRefs – decrement reference counts for resources"
---

<p>XtAppReleaseCacheRefs &#8211; decrement reference counts for resources </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppReleaseCacheRefs(XtAppContext <i>app_context</i>, XtCacheRef* <i>refs</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>refs</i></p>
<dd>Specifies the list of cache references to be released.</dl>
<h2>Description</h2>
<p><code>XtAppReleaseCacheRefs</code> decrements the reference count for the conversion entries identified by the <i>refs</i> argument. This argument is a pointer to a NULL-terminated list of <code>XtCacheRef</code> values. If any reference count reaches zero, the destructor, if any, will be called and the resource removed from the conversion cache.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
