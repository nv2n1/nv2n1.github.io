---
title: "stdoptionalemplace(3)"
name: "stdoptionalemplace"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptionalemplace/"
description: "std::optional<T>::emplace – std::optional<T>::emplace"
---

<p>std::optional&lt;T&gt;::emplace &#8211; std::optional&lt;T&gt;::emplace</p>
<h2>Synopsis</h2>
<pre><code>template&lt; class... Args &gt;                                      (since C++17)

T&amp; emplace( Args&amp;&amp;... args );

template&lt; class U, class... Args &gt;                             (since C++17)

T&amp; emplace( std::initializer_list&lt;U&gt; ilist, Args&amp;&amp;... args );</code></pre>
<p>Constructs the contained value in-place. If *this already contains a value before the call, the contained value is destroyed by calling its destructor.<br />
1) Initializes the contained value by direct-initializing (but not direct-list-initializing) with std::forward&lt;Args&gt;(args)&#8230; as parameters.<br />
2) Initializes the contained value by calling its constructor with ilist, std::forward&lt;Args&gt;(args)&#8230; as parameters. This overload only participates in overload resolution if std::is_constructible&lt;T, std::initializer_list&lt;U&gt;&amp;, Args&amp;&amp;&#8230;&gt;::value is true. </p>
<h2>Parameters</h2>
<p>args&#8230; &#8211; the arguments to pass to the constructor<br />
ilist &#8211; the initializer list to pass to the constructor</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
T must be constructible from Args&#8230; for overload <code>(1)</code><br />
&#8211;<br />
T must be constructible from std::initializer_list and Args&#8230; for overload <code>(2)</code></p>
<h2>Return value</h2>
<p>A reference to the new contained value. </p>
<h2>Exceptions</h2>
<p>Any exception thrown by the selected constructor of T. If an exception is thrown, *this does not contain a value after this call (the previously contained value, if any, had been destroyed).</p>
<h2>See also</h2>
<pre><code>assigns contents

operator= (public member function)




</code></pre>
