---
title: "std__exception_ptr_exception_ptr(3)"
name: "std__exception_ptr_exception_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__exception_ptr_exception_ptr/"
description: "std::__exception_ptr::exception_ptr –"
---

<p>std::__exception_ptr::exception_ptr &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>exception_ptr (const exception_ptr &amp;) noexcept



exception_ptr (nullptr_t) noexcept



exception_ptr (exception_ptr &amp;&amp;__o) noexcept



class std::type_info * __cxa_exception_type () const noexcept __attribute__((__pure__))



operator bool () const



exception_ptr &amp; operator= (const exception_ptr &amp;) noexcept



exception_ptr &amp; operator= (exception_ptr &amp;&amp;__o) noexcept



void swap (exception_ptr &amp;) noexcept



Friends</code></pre>
<p> bool <code>operator==</code> (const <code>exception_ptr</code> &amp;, const <code>exception_ptr</code> &amp;) noexcept __attribute__((__pure__)) </p>
<p> <code>exception_ptr</code> <code>std::current_exception</code> () noexcept </p>
<p> void <code>std::rethrow_exception</code> (<code>exception_ptr</code>)</p>
<h2>Detailed Description</h2>
<p>An opaque pointer to an arbitrary exception. </p>
<p> Definition at line 75 of file exception_ptr.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
