---
title: "stdexperimentaloptionalemplace(3)"
name: "stdexperimentaloptionalemplace"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaloptionalemplace/"
---

std::experimental::optional&lt;T&gt;::emplace - std::experimental::optional&lt;T&gt;::emplace

<h2>Synopsis</h2>

<pre><code>template &lt;class... Args&gt;
(library fundamentals TS)

    void emplace(Args &amp;&amp;...args);

template &lt;class U, class... Args&gt;
(library fundamentals TS)

    void emplace(std::initializer_list&lt;U&gt; ilist, Args &amp;&amp;...args);</code></pre> 
Constructs the contained value in-place. If *this already contains a value before the call, the contained value is destroyed by calling its destructor. 
1) Initializes the contained value by direct-initializing (but not direct-list-initializing) with std::forward&lt;Args&gt;(args)... as parameters. 
2) Initializes the contained value by calling its constructor with ilist, std::forward&lt;Args&gt;(args)... as parameters. This overload only participates in overload resolution if std::is_constructible&lt;T, std::initializer_list&lt;U&gt;&amp;, Args&amp;&amp;...&gt;::value is true. 

<h2>Parameters</h2>

args... - the arguments to pass to the constructor 
ilist - the initializer list to pass to the constructor

<h2>Type requirements</h2>

- 
T must be constructible from Args... 
- 
T must be constructible from std::initializer_list and Args...

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Any exception thrown by the selected constructor of T. If an exception is thrown, *this does not contain a value after this call (the previously contained value, if any, had been destroyed).

<h2>See also</h2>

<pre><code>assigns contents

operator= (public member function)




</code></pre>
