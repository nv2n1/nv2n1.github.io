---
title: "stdnot_fn(3)"
name: "stdnot_fn"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnot_fn/"
description: "std::not_fn – std::not_fn"
---

<p>std::not_fn &#8211; std::not_fn</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;functional&gt;

template&lt; class F&gt;                (since C++17)

/*unspecified*/ not_fn( F&amp;&amp; f );</code></pre>
<p>Creates a forwarding call wrapper that returns the negation of the callable object it holds. </p>
<h2>Parameters</h2>
<p>f &#8211; the object from which the Callable object held by the wrapper is constructed</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
std::decay_t&lt;F&gt; must meet the requirements of Callable and MoveConstructible.<br />
&#8211;<br />
std::is_constructible_v&lt;std::decay_t&lt;F&gt;, F&gt; is required to be true</p>
<h2>Return value</h2>
<p>A function object of unspecified type T. It has the following members: </p>
<pre><code>std::not_fn return type

</code></pre>
<h2>Member objects</h2>
<p>The return type of std::not_fn holds a member object of type std::decay_t&lt;F&gt;. </p>
<p>Constructors </p>
<p>explicit T(F&amp;&amp; f); <code>(1)</code><br />
T(T&amp;&amp; f) = default; <code>(2)</code><br />
T(const T&amp; f) = default; </p>
<p>1) The constructor initializes the member object (of type std::decay_t&lt;F&gt;) from std::forward&lt;F&gt;(f). Throws any exception thrown by the constructor selected<br />
2) Because std::decay_t&lt;F&gt; is required to be MoveConstructible, the returned call wrapper is always MoveConstructible, and is CopyConstructible if std::decay_t&lt;F&gt; is CopyConstructible.</p>
<h2>Member function operator()</h2>
<p>template&lt;class&#8230; Args&gt; auto operator()(Args&amp;&amp;&#8230; args) &amp;<br />
-&gt; decltype(!std::declval&lt;std::invoke_result_t&lt;std::decay_t&lt;F&gt;&amp;, Args&#8230;&gt;&gt;()); <code>(1)</code><br />
template&lt;class&#8230; Args&gt; auto operator()(Args&amp;&amp;&#8230; args) const&amp;<br />
-&gt; decltype(!std::declval&lt;std::invoke_result_t&lt;std::decay_t&lt;F&gt; const&amp;, Args&#8230;&gt;&gt;());<br />
template&lt;class&#8230; Args&gt; auto operator()(Args&amp;&amp;&#8230; args) &amp;&amp;<br />
-&gt; decltype(!std::declval&lt;std::invoke_result_t&lt;std::decay_t&lt;F&gt;, Args&#8230;&gt;&gt;()); <code>(2)</code><br />
template&lt;class&#8230; Args&gt; auto operator()(Args&amp;&amp;&#8230; args) const&amp;&amp;<br />
-&gt; decltype(!std::declval&lt;std::invoke_result_t&lt;std::decay_t&lt;F&gt; const, Args&#8230;&gt;&gt;()); </p>
<p>1) Equivalent to return !std::invoke(fd, std::forward&lt;Args&gt;(args)&#8230;)<br />
2) Equivalent to return !std::invoke(std::move(fd), std::forward&lt;Args&gt;(args)&#8230;)<br />
where fd is the member object of type std::decay_t&lt;F&gt;</p>
<h2>Exceptions</h2>
<p>Throws no exceptions, unless the construction of fd throws.</p>
<h2>Notes</h2>
<p>not_fn is intended to replace the C++03-era negators std::not1 and std::not2. </p>
<h2>See also</h2>
<p>not1 constructs custom std::unary_negate object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(deprecated in C++17)<br />
(removed in C++20)<br />
not2 constructs custom std::binary_negate object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(deprecated in C++17)<br />
(removed in C++20) </p>
