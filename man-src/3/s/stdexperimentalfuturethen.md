---
title: "stdexperimentalfuturethen(3)"
name: "stdexperimentalfuturethen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfuturethen/"
---

std::experimental::future&lt;T&gt;::then - std::experimental::future&lt;T&gt;::then

<h2>Synopsis</h2>

<pre><code>template &lt; class F &gt;

future&lt;/* see below */&gt; then(F&amp;&amp; func) ;</code></pre> 
Attach the continuation func to *this. The behavior is undefined if *this has no associated shared state (i.e., valid() == false). 
Creates a shared state associated with the future object to be returned, and a copy fd of func constructed as if by DECAY_COPY(std::forward&lt;F&gt;(func)) evaluated in the thread calling then, where DECAY_COPY is defined as <pre><code>template &lt;class T&gt;

std::decay_t&lt;T&gt; DECAY_COPY(T &amp;&amp;v)
{
    return std::forward&lt;T&gt;(v);
}
</code></pre> 
When the shared state currently associated with *this is ready, the continuation INVOKE(std::move(fd), std::move(*this)) is called on an unspecified thread of execution, where INVOKE is the operation defined in Callable. If that expression is invalid, the behavior is undefined. 
Any value returned from the continuation is stored as the result in the shared state of the returned future object. Any exception propagated from the execution of the continuation is stored as the exceptional result in the shared state of the returned future object. 
Let U be the return type of the continuation (i.e. std::result_of_t&lt;std::decay_t&lt;F&gt;(std::experimental::future&lt;T&gt;)&gt;). If U is std::experimental::future&lt;T2&gt; for some type T2, then the return type of then is std::experimental::future&lt;T2&gt;, otherwise it is std::experimental::future&lt;U&gt;. This is known as implicit unwrapping. 
If implicit unwrapping takes place and the continuation returns an invalid future, then the shared state is made ready with an exception of type std::future_error with an error condition of std::future_errc::broken_promise. 
After this function returns, valid() is false. 

<h2>Parameters</h2>

func - A continuation to be attached.

<h2>Return value</h2>

A std::experimental::future object associated with the shared state created by this object. valid() == true for the returned object. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
