---
title: "ares_library_cleanup(3)"
name: "ares_library_cleanup"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_library_cleanup/"
description: "ares_library_cleanup – c-ares library deinitialization"
---

<h2>NAME</h2>
<p> ares_library_cleanup &#8211; c-ares library deinitialization</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_library_cleanup(void)
        cc file.c
    - lcares
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_library_cleanup</code> function uninitializes the c-ares library, freeing all resources previously acquired by <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i> when the library was initialized, provided there was only one single previous call to <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i>. If there was more than one previous call to <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i>, this function uninitializes the c-ares library only if it is the call matching the call to <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i> which initialized the library (usually the very first call to <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i>). Other calls to <i><a href="/docs/linux/man/3-ares_library_cleanup/">ares_library_cleanup</a>(3)</i> have no effect other than decrementing an internal counter. </p>
<p> This function must be called when the program using c-ares will no longer need any c-ares function. Once the program has called <i><a href="/docs/linux/man/3-ares_library_cleanup/">ares_library_cleanup</a>(3)</i> sufficiently often such that the library is uninitialised, it shall not make any further call to any c-ares function. </p>
<p> This function does not cancel any pending c-ares lookups or requests previously done. Program must use <i><a href="/docs/linux/man/3-ares_cancel/">ares_cancel</a>(3)</i> for this purpose. </p>
<p> <code>This function is not thread safe.</code> You have to call it once the program is about to terminate, but this call must be done once the program has terminated every single thread that it could have initiated. This is required to avoid potential race conditions in library deinitialization, and also due to the fact that <i><a href="/docs/linux/man/3-ares_library_cleanup/">ares_library_cleanup</a>(3)</i> might call functions from other libraries that are thread unsafe, and could conflict with any other thread that is already using these other libraries. </p>
<p> Win32/64 application DLLs shall not call <i><a href="/docs/linux/man/3-ares_library_cleanup/">ares_library_cleanup</a>(3)</i> from the DllMain function. Doing so will produce deadlocks and other problems.</p>
<h2>AVAILABILITY</h2>
<p> This function was first introduced in c-ares version 1.7.0 along with the definition of preprocessor symbol <i>CARES_HAVE_ARES_LIBRARY_CLEANUP</i> as an indication of the availability of this function. Reference counting in <i>ares_library_init()</i> and <i>ares_library_cleanup()</i>, which requires calls to the former function to match calls to the latter, is present since c-ares version 1.10.0. Earlier versions would deinitialize the library on the first call to <i>ares_library_cleanup()</i>. </p>
<p> Since the introduction of this function, it is absolutely mandatory to call it for any Win32/64 program using c-ares. </p>
<p> Non-Win32/64 systems can still use c-ares version 1.7.0 without calling <i><a href="/docs/linux/man/3-ares_library_cleanup/">ares_library_cleanup</a>(3)</i> due to the fact that <i>currently</i> it is nearly a do-nothing function on non-Win32/64 platforms.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3),</code> <code><a href="/docs/linux/man/3-ares_cancel/">ares_cancel</a>(3)</code></p>
<h2>AUTHOR</h2>
<p> Yang Tse </p>
<p> Copyright 1998 by the Massachusetts Institute of Technology.<br />
 Copyright (C) 2004-2009 by Daniel Stenberg. </p>
<h2>Index</h2>
