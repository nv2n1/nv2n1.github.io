---
title: "stdbind_front(3)"
name: "stdbind_front"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbind_front/"
---

std::bind_front - std::bind_front

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template &lt;class F, class... Args&gt;                     (since C++20)

/*unspecified*/ bind_front( F&amp;&amp; f, Args&amp;&amp;... args );</code></pre> 
The function template bind_front generates a forwarding call wrapper for f. Calling this wrapper is equivalent to invoking f with its first sizeof...(Args) parameters bound to args. 
In other words, std::bind_front(f, bound_args...)(call_args...) is equivalent to std::invoke(f, bound_args..., call_args....). 
The program is ill-formed if any of the following is not true: 
* std::is_constructible_v&lt;std::decay_t&lt;F&gt;, F&gt; 
* std::is_move_constructible_v&lt;std::decay_t&lt;F&gt;&gt; 
* (std::is_constructible_v&lt;std::decay_t&lt;Args&gt;, Args&gt; &amp;&amp; ...) 
* (std::is_move_constructible_v&lt;std::decay_t&lt;Args&gt;&gt; &amp;&amp; ...) 

<h2>Parameters</h2>

f - Callable object <i>(function object, pointer to function, reference to function, pointer to member function, or pointer to data member) that will be bound to s</i>ome arguments 
args - list of the arguments to bind to the first sizeof...(Args) parameters of f

<h2>Type requirements</h2>

- 
std::decay_t&lt;F&gt; and each type in std::decay_t&lt;Args&gt;... must meet the requirements of MoveConstructible.

<h2>Return value</h2>

A function object of type T that is unspecified, except that the types of objects returned by two calls to std::bind_front with the same arguments are the same. 
The returned object (call wrapper) has the following properties: <pre><code>std::bind_front return type

</code></pre>

<h2>Member objects</h2>

The returned object behaves as if it holds a member object fd of type std::decay_t&lt;F&gt; constructed from std::forward&lt;F&gt;(f), and an std::tuple object tup constructed with std::make_tuple(std::forward&lt;Args&gt;(args)...) (this unwraps any std::reference_wrappers), except that the returned object's assignment behavior is unspecified and the names are for exposition only. 

 
Constructors 

 
The return type of std::bind_front behaves as if its copy/move constructors perform a memberwise copy/move. It is CopyConstructible if all of its member objects (specified above) are CopyConstructible, and is MoveConstructible otherwise.

<h2>Member function operator()</h2>

Given an object G obtained from an earlier call to bind_front(f, args...), when a glvalue g designating G is invoked in a function call expression g(call_args...), an invocation of the stored object takes place, as if by 

 
&nbsp;<wbr>&nbsp;std::invoke(g.fd, std::get&lt;Ns&gt;(g.tup)..., call_args...) 

 
, where 

 
* Ns is an integer pack 0, 1, ..., (sizeof...(Args) - 1) 
* g is an lvalue in the std::invoke expression if it is an lvalue in the call expression, and is an rvalue otherwise. Thus std::move(g)(call_args...) can move the bound arguments into the call, where g(call_args...) would copy. 

 
The behavior is undefined if g has volatile-qualified type. 
The member operator() is noexcept if the std::invoke expression it calls is noexcept (in other words, it preserves the exception specification of the underlying call operator)

<h2>Exceptions</h2>

Only throws if construction of stored function object or any of the bound arguments throws.

<h2>Notes</h2>

This function is intended to replace std::bind. Unlike std::bind, it does not support arbitrary argument rearrangement and has no special treatment for nested bind-expressions. On the other hand, it pays attention to the value category of the call wrapper object and propagates exception specification of the underlying call operator. 
As described in std::invoke, when invoking a pointer to non-static member function or pointer to non-static data member, the first argument has to be a reference or pointer (including, possibly, smart pointer such as std::shared_ptr and std::unique_ptr) to an object whose member will be accessed. 
The arguments to std::bind_front are copied or moved, and are never passed by reference unless wrapped in std::ref or std::cref. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

bind binds one or more arguments to a function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
mem_fn creates a function object out of a pointer to a member 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
