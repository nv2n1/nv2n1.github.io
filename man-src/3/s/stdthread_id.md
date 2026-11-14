---
title: "stdthread_id(3)"
name: "stdthread_id"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthread_id/"
description: "std::thread::id –"
---

<p>std::thread::id &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p><code>id</code> (native_handle_type __id)</p>
<h3>Friends</h3>
<p>class <code>hash&lt; thread::id &gt;</code> </p>
<p> bool <code>operator&lt;</code> (<code>thread::id</code> __x, <code>thread::id</code> __y) noexcept </p>
<p> template&lt;class _CharT , class _Traits &gt; <code>basic_ostream</code>&lt; _CharT, _Traits &gt; &amp; <code>operator&lt;&lt;</code> (<code>basic_ostream</code>&lt; _CharT, _Traits &gt; &amp;__out, <code>thread::id</code> __id) </p>
<p> bool <code>operator==</code> (<code>thread::id</code> __x, <code>thread::id</code> __y) noexcept </p>
<p> class <code>thread</code></p>
<h2>Detailed Description</h2>
<p>thread::id </p>
<p> Definition at line 68 of file thread.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
