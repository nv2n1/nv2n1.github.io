---
title: "hbwallocator(3)"
name: "hbwallocator"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hbwallocator/"
description: "hbw::allocator<T> – The C++ allocator compatible with the C++ standard library allocator concepts Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (includ..."
---

<h2>NAME</h2>
<p> hbw::allocator&lt;T&gt; &#8211; The C++ allocator compatible with the C++ standard library allocator concepts<br />
 Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or remove.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;hbw_allocator.h&gt;
Link with - lmemkind
            hbw::allocator()

                template &lt;class U&gt;
                hbw::allocator&lt;T&gt;::allocator(const hbw::allocator&lt;U&gt; &amp;)

                    hbw::allocator&lt;T&gt;::~allocator()

                        hbw::allocator&lt;T&gt;::pointer hbw::allocator&lt;T&gt;::address(hbw::allocator&lt;T&gt;::reference x)

                            hbw::allocator&lt;T&gt;::const_pointer hbw::allocator&lt;T&gt;::address(hbw::allocator&lt;T&gt;::const_reference x)

                                hbw::allocator&lt;T&gt;::pointer hbw::allocator&lt;T&gt;::allocate(hbw::allocator&lt;T&gt;::size_type n, const void * = 0)

                                    void hbw::allocator&lt;T&gt;::deallocate(hbw::allocator&lt;T&gt;::pointer p, hbw::allocator&lt;T&gt;::size_type n)

                                        hbw::allocator&lt;T&gt;::size_type hbw::allocator&lt;T&gt;::max_size()

                                            void hbw::allocator&lt;T&gt;::construct(hbw::allocator&lt;T&gt;::pointer p, const hbw::allocator&lt;T&gt;::value_type &amp;val)

                                                void hbw::allocator&lt;T&gt;::destroy(hbw::allocator&lt;T&gt;::pointer p)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The hbw::allocator&lt;T&gt; is intended to be used with STL containers to allocate high bandwidth memory. Memory management is based on hbwmalloc (memkind library), enabling users to gain performance in multithreaded applications. Refer <a href="/docs/linux/man/3-hbwmalloc/">hbwmalloc</a>(3) and <a href="/docs/linux/man/3-memkind/">memkind</a>(3) man page for more details. </p>
<p> All public member types and functions corresponds to standard library allocator concepts and definitions. The current implementation supports C++03 standard. </p>
<p> Template arguments:<br />
 T is an object type aliased by value_type.<br />
 U is an object type. </p>
<p> Note:<br />
 hbw::allocator&lt;T&gt;::pointer hbw::allocator&lt;T&gt;::allocate(hbw::allocator&lt;T&gt;::size_type n, const void * = 0) allocates high bandwidth memory using <i>hbw_malloc().</i> Throw <i>std::bad_alloc</i> when:<br />
 <i>n</i> = 0,<br />
 <i>n</i> &gt; max_size()<i>,</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>or there is not enough memory to satisfy the request.</p>
<p> void hbw::allocator&lt;T&gt;::deallocate(hbw::allocator&lt;T&gt;::pointer p, hbw::allocator&lt;T&gt;::size_type n) deallocates memory associated with pointer returned by <i>allocate()</i> using <i>hbw_free().</i> </p>
<p> To find out more about <i>hbw_malloc()</i> and <i>hbw_free()</i> read <a href="/docs/linux/man/3-hbwmalloc/">hbwmalloc</a>(3) man page. </p>
<h2>ERRORS</h2>
<dl>
<dt>The same as described in ERRORS section of <a href="/docs/linux/man/3-hbwmalloc/">hbwmalloc</a>(3) man page.</p>
<dd></dl>
<h2>NOTES</h2>
<p> The <i>hbw::allocator&lt;T&gt;</i> behavior depends on hbwmalloc heap management policy. To get and set the policy please use <i>hbw_get_policy()</i> and <i>hbw_set_policy()</i> respectively.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2015 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hbwmalloc/">hbwmalloc</a>(3),</code> <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8), <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3) </p>
<h2>Index</h2>
