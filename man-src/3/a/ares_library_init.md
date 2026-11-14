---
title: "ares_library_init(3)"
name: "ares_library_init"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_library_init/"
description: "ares_library_init – c-ares library initialization"
---

<h2>NAME</h2>
<p> ares_library_init &#8211; c-ares library initialization</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_library_init(int flags)
        cc file.c
    - lcares
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_library_init</code> function performs initializations internally required by the c-ares library that must take place before any other function provided by c-ares can be used in a program. </p>
<p> This function must be called at least once within the life of a program, before the program actually executes any other c-ares library function. Initializations done by this function remain effective until a number of calls to <i><a href="/docs/linux/man/3-ares_library_cleanup/">ares_library_cleanup</a>(3)</i> equal to the number of calls to this function are performed. </p>
<p> Successive calls to this function do nothing further, only the first call done when c-ares is in an uninitialized state is actually effective. </p>
<p> The <i>flags</i> parameter is a bit pattern that tells c-ares exactly which features should be initialized, as described below. Set the desired bits by ORing the values together. In normal operation you should specify <i>ARES_LIB_INIT_ALL</i>. Don&#8217;t use any other value unless you are familiar with it and trying to control some internal c-ares feature. </p>
<p> <code>This function is not thread safe.</code> You have to call it once the program has started, but this call must be done before the program starts any other thread. This is required to avoid potential race conditions in library initialization, and also due to the fact that <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i> might call functions from other libraries that are thread unsafe, and could conflict with any other thread that is already using these other libraries. </p>
<p> Win32/64 application DLLs shall not call <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i> from the DllMain function. Doing so will produce deadlocks and other problems.</p>
<h2>FLAGS</h2>
<dl>
<dt><code>ARES_LIB_INIT_ALL</code></p>
<dd> Initialize everything possible. This sets all known bits.</p>
<dt><code>ARES_LIB_INIT_WIN32</code></p>
<dd> Initialize Win32/64 specific libraries.</p>
<dt><code>ARES_LIB_INIT_NONE</code></p>
<dd> Initialize nothing extra. This sets no bit.</dl>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, ares_library_init() will return 0. Otherwise, a non-zero error number will be returned to indicate the error. Except for <i><a href="/docs/linux/man/3-ares_strerror/">ares_strerror</a>(3)</i>, you shall not call any other c-ares function upon <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i> failure.</p>
<h2>AVAILABILITY</h2>
<p> This function was first introduced in c-ares version 1.7.0 along with the definition of preprocessor symbol <i>CARES_HAVE_ARES_LIBRARY_INIT</i> as an indication of the availability of this function. Its recursive behavior, which requires a matching number of calls to <i>ares_library_cleanup()</i> in order to deinitialize the library, is present since c-ares version 1.10.0. Earlier versions would deinitialize the library on the first call to <i>ares_library_cleanup()</i>. </p>
<p> Since the introduction of this function it is absolutely mandatory to call it for any Win32/64 program using c-ares. </p>
<p> Non-Win32/64 systems can still use c-ares version 1.7.0 without calling <i><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</i> due to the fact that <i>currently</i> it is nearly a do-nothing function on non-Win32/64 platforms at this point.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_library_cleanup/">ares_library_cleanup</a>(3),</code> <code><a href="/docs/linux/man/3-ares_strerror/">ares_strerror</a>(3)</code></p>
<h2>AUTHOR</h2>
<p> Yang Tse </p>
<p> Copyright 1998 by the Massachusetts Institute of Technology.<br />
 Copyright (C) 2004-2009 by Daniel Stenberg. </p>
<h2>Index</h2>
