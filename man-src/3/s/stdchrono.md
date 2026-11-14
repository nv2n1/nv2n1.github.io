---
title: "stdchrono(3)"
name: "stdchrono"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchrono/"
description: "std::chrono –"
---

<p>std::chrono &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<pre><code>struct duration



struct duration_values



struct time_point



struct treat_as_floating_point



Typedefs</code></pre>
<p> typedef <code>duration</code>&lt; int, <code>ratio</code>&lt; 3600 &gt; &gt; <code>hours</code> </p>
<p> typedef <code>duration</code>&lt; int64_t, micro &gt; <code>microseconds</code> </p>
<p> typedef <code>duration</code>&lt; int64_t, milli &gt; <code>milliseconds</code> </p>
<p> typedef <code>duration</code>&lt; int, <code>ratio</code>&lt; 60 &gt; &gt; <code>minutes</code> </p>
<p> typedef <code>duration</code>&lt; int64_t, nano &gt; <code>nanoseconds</code> </p>
<p> typedef <code>duration</code>&lt; int64_t &gt; <code>seconds</code></p>
<h3>Functions</h3>
<pre><code>template&lt;typename _ToDur , typename _Rep , typename _Period &gt; constexpr enable_if


&lt; __is_duration&lt; _ToDur &gt;

::value, _ToDur &gt;::type duration_cast (const duration&lt; _Rep, _Period &gt; &amp;__d)&quot;


template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr bool operator!= (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)



template&lt;typename _Clock , typename _Dur1 , typename _Dur2 &gt; constexpr bool operator!= (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const time_point&lt; _Clock, _Dur2 &gt; &amp;__rhs)



template&lt;typename _Rep1 , typename _Period , typename _Rep2 &gt; constexpr duration&lt; typename


__common_rep_type&lt; _Rep1,

typename enable_if

&lt;!__is_duration&lt; _Rep2 &gt;

::value, _Rep2 &gt;::type &gt;::type,

_Period &gt; operator% (const duration&lt; _Rep1, _Period &gt; &amp;__d, const _Rep2 &amp;__s)&quot;


template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr common_type


&lt; duration&lt; _Rep1, _Period1 &gt;

, duration&lt; _Rep2, _Period2 &gt;


&gt;::type operator% (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)&quot;


template&lt;typename _Rep1 , typename _Period , typename _Rep2 &gt; constexpr duration&lt; typename


__common_rep_type&lt; _Rep1,

_Rep2 &gt;::type, _Period &gt; operator* (const duration&lt; _Rep1, _Period &gt; &amp;__d, const _Rep2 &amp;__s)&quot;


template&lt;typename _Rep1 , typename _Rep2 , typename _Period &gt; constexpr duration&lt; typename


__common_rep_type&lt; _Rep2,

_Rep1 &gt;::type, _Period &gt; operator* (const _Rep1 &amp;__s, const duration&lt; _Rep2, _Period &gt; &amp;__d)&quot;


template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr common_type


&lt; duration&lt; _Rep1, _Period1 &gt;

, duration&lt; _Rep2, _Period2 &gt;


&gt;::type operator+ (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)&quot;


template&lt;typename _Clock , typename _Dur1 , typename _Rep2 , typename _Period2 &gt; constexpr time_point&lt; _Clock,


typename common_type&lt; _Dur1,

duration&lt; _Rep2, _Period2 &gt;


&gt;::type &gt; operator+ (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)&quot;


template&lt;typename _Rep1 , typename _Period1 , typename _Clock , typename _Dur2 &gt; constexpr time_point&lt; _Clock,


typename common_type&lt; duration

&lt; _Rep1, _Period1 &gt;, _Dur2 &gt;

::type &gt; operator+ (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const time_point&lt; _Clock, _Dur2 &gt; &amp;__rhs)&quot;


template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr common_type


&lt; duration&lt; _Rep1, _Period1 &gt;

, duration&lt; _Rep2, _Period2 &gt;


&gt;::type operator- (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)&quot;


template&lt;typename _Clock , typename _Dur1 , typename _Rep2 , typename _Period2 &gt; constexpr time_point&lt; _Clock,


typename common_type&lt; _Dur1,

duration&lt; _Rep2, _Period2 &gt;


&gt;::type &gt; operator- (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)&quot;


template&lt;typename _Clock , typename _Dur1 , typename _Dur2 &gt; constexpr common_type&lt; _Dur1,


_Dur2 &gt;::type operator- (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const time_point&lt; _Clock, _Dur2 &gt; &amp;__rhs)&quot;


template&lt;typename _Rep1 , typename _Period , typename _Rep2 &gt; constexpr duration&lt; typename


__common_rep_type&lt; _Rep1,

typename enable_if

&lt;!__is_duration&lt; _Rep2 &gt;

::value, _Rep2 &gt;::type &gt;::type,

_Period &gt; operator/ (const duration&lt; _Rep1, _Period &gt; &amp;__d, const _Rep2 &amp;__s)&quot;


template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr common_type&lt; _Rep1,


_Rep2 &gt;::type operator/ (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)&quot;


template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr bool operator&lt; (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)



template&lt;typename _Clock , typename _Dur1 , typename _Dur2 &gt; constexpr bool operator&lt; (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const time_point&lt; _Clock, _Dur2 &gt; &amp;__rhs)



template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr bool operator&lt;= (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)



template&lt;typename _Clock , typename _Dur1 , typename _Dur2 &gt; constexpr bool operator&lt;= (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const time_point&lt; _Clock, _Dur2 &gt; &amp;__rhs)



template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr bool operator== (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)



template&lt;typename _Clock , typename _Dur1 , typename _Dur2 &gt; constexpr bool operator== (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const time_point&lt; _Clock, _Dur2 &gt; &amp;__rhs)



template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr bool operator&gt; (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)



template&lt;typename _Clock , typename _Dur1 , typename _Dur2 &gt; constexpr bool operator&gt; (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const time_point&lt; _Clock, _Dur2 &gt; &amp;__rhs)



template&lt;typename _Rep1 , typename _Period1 , typename _Rep2 , typename _Period2 &gt; constexpr bool operator&gt;= (const duration&lt; _Rep1, _Period1 &gt; &amp;__lhs, const duration&lt; _Rep2, _Period2 &gt; &amp;__rhs)



template&lt;typename _Clock , typename _Dur1 , typename _Dur2 &gt; constexpr bool operator&gt;= (const time_point&lt; _Clock, _Dur1 &gt; &amp;__lhs, const time_point&lt; _Clock, _Dur2 &gt; &amp;__rhs)



template&lt;typename _ToDur , typename _Clock , typename _Dur &gt; constexpr enable_if


&lt; __is_duration&lt; _ToDur &gt;

::value, time_point&lt; _Clock,

_ToDur &gt; &gt;::type time_point_cast (const time_point&lt; _Clock, _Dur &gt; &amp;__t)&quot;</code></pre>
<h2>Detailed Description</h2>
<p>ISO C++ 2011 entities sub-namespace for time and date.</p>
<h2>Typedef Documentation</h2>
<h3>typedef <code>duration</code>&lt;int, <code>ratio</code>&lt;3600&gt; &gt; <code>std::chrono::hours</code></h3>
<p>hours </p>
<p> Definition at line 541 of file chrono.</p>
<h3>typedef <code>duration</code>&lt;int64_t, micro&gt; <code>std::chrono::microseconds</code></h3>
<p>microseconds </p>
<p> Definition at line 529 of file chrono.</p>
<h3>typedef <code>duration</code>&lt;int64_t, milli&gt; <code>std::chrono::milliseconds</code></h3>
<p>milliseconds </p>
<p> Definition at line 532 of file chrono.</p>
<h3>typedef <code>duration</code>&lt;int, <code>ratio</code>&lt; 60&gt; &gt; <code>std::chrono::minutes</code></h3>
<p>minutes </p>
<p> Definition at line 538 of file chrono.</p>
<h3>typedef <code>duration</code>&lt;int64_t, nano&gt; <code>std::chrono::nanoseconds</code></h3>
<p>nanoseconds </p>
<p> Definition at line 526 of file chrono.</p>
<h3>typedef <code>duration</code>&lt;int64_t&gt; <code>std::chrono::seconds</code></h3>
<p>seconds </p>
<p> Definition at line 535 of file chrono.</p>
<h2>Function Documentation</h2>
<h3>template&lt;typename _ToDur , typename _Rep , typename _Period &gt; constexpr <code>enable_if</code>&lt;__is_duration&lt;_ToDur&gt;::value, _ToDur&gt;::type std::chrono::duration_cast (const duration&lt; _Rep, _Period &gt; &amp;__d)</h3>
<p>duration_cast </p>
<p> Definition at line 193 of file chrono. </p>
<p> Referenced by std::this_thread::sleep_for().</p>
<h3>template&lt;typename _ToDur , typename _Clock , typename _Dur &gt; constexpr <code>enable_if</code>&lt;__is_duration&lt;_ToDur&gt;::value, <code>time_point</code>&lt;_Clock, _ToDur&gt; &gt;::type std::chrono::time_point_cast (const time_point&lt; _Clock, _Dur &gt; &amp;__t)</h3>
<p>time_point_cast </p>
<p> Definition at line 602 of file chrono.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
