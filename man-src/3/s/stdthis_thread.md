---
title: "stdthis_thread(3)"
name: "stdthis_thread"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthis_thread/"
description: "std::this_thread –"
---

<p>std::this_thread &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions</h3>
<pre><code>void __sleep_for (chrono::seconds, chrono::nanoseconds)



thread::id get_id () noexcept



template&lt;typename _Rep , typename _Period &gt; void sleep_for (const chrono::duration&lt; _Rep, _Period &gt; &amp;__rtime)



template&lt;typename _Clock , typename _Duration &gt; void sleep_until (const chrono::time_point&lt; _Clock, _Duration &gt; &amp;__atime)



void yield () noexcept</code></pre>
<h2>Detailed Description</h2>
<p>ISO C++ 2011 entities sub-namespace for thread. 30.3.2 Namespace this_thread.</p>
<h2>Function Documentation</h2>
<h3><code>thread::id</code> std::this_thread::get_id () [inline], [noexcept]</h3>
<p>get_id </p>
<p> Definition at line 252 of file thread.</p>
<h3>template&lt;typename _Rep , typename _Period &gt; void std::this_thread::sleep_for (const chrono::duration&lt; _Rep, _Period &gt; &amp;__rtime) [inline]</h3>
<p>sleep_for </p>
<p> Definition at line 269 of file thread. </p>
<p> References std::chrono::duration_cast(). </p>
<p> Referenced by sleep_until().</p>
<h3>template&lt;typename _Clock , typename _Duration &gt; void std::this_thread::sleep_until (const chrono::time_point&lt; _Clock, _Duration &gt; &amp;__atime) [inline]</h3>
<p>sleep_until </p>
<p> Definition at line 288 of file thread. </p>
<p> References sleep_for().</p>
<h3>void std::this_thread::yield () [inline], [noexcept]</h3>
<p>yield </p>
<p> Definition at line 256 of file thread.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
