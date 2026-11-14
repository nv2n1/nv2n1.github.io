---
title: "stduses_allocator_construction_args(3)"
name: "stduses_allocator_construction_args"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduses_allocator_construction_args/"
---

std::uses_allocator_construction_args - std::uses_allocator_construction_args

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;memory&gt;

    T is not a specialization of std::pair

    template &lt;class T, class Alloc, class... Args&gt;

    std::tuple&lt;/*see below*/&gt; uses_allocator_construction_args((1)(since C++ 20)

                                                                   const Alloc &amp;alloc,
                                                               Args &amp;&amp;...args);

T is a specialization of std::pair

    template &lt;class T, class Alloc, class Tuple1, class Tuple2&gt;

    std::tuple&lt;/*see below*/&gt; uses_allocator_construction_args((2)(since C++ 20)

                                                                   const Alloc &amp;alloc,
                                                               std::piecewise_construct_t, Tuple1 &amp;&amp;x, Tuple2 &amp;&amp;y);

template &lt;class T, class Alloc&gt;
(3)(since C++ 20)

    std::tuple&lt;/*see below*/&gt; uses_allocator_construction_args(const Alloc &amp;alloc);

template &lt;class T, class Alloc, class U, class V&gt;

std::tuple&lt;/*see below*/&gt; uses_allocator_construction_args((4)(since C++ 20)

                                                               const Alloc &amp;alloc,
                                                           U &amp;&amp;u, V &amp;&amp;v);

template &lt;class T, class Alloc, class U, class V&gt;

std::tuple&lt;/*see below*/&gt; uses_allocator_construction_args((5)(since C++ 20)

                                                               const Alloc &amp;alloc,
                                                           const std::pair&lt;U, V&gt; &amp;pr);

template &lt;class T, class Alloc, class U, class V&gt;

std::tuple&lt;/*see below*/&gt; uses_allocator_construction_args((6)(since C++ 20)

                                                               const Alloc &amp;alloc,
                                                           std::pair&lt;U, V&gt; &amp;&amp;pr);</code></pre> 
Prepares the argument list needed to create an object of the given type T by means of uses-allocator_construction. 
1) This overload only participates in overload resolution if T is not a specialization of std::pair. Returns std::tuple determined as follows: 
* If std::uses_allocator_v&lt;T, Alloc&gt; is false and std::is_constructible_v&lt;T, Args...&gt; is true, returns std::forward_as_tuple(std::forward&lt;Args&gt;(args)...) 
* Otherwise, if std::uses_allocator_v&lt;T, Alloc&gt; is true and std::is_constructible_v&lt;T, std::allocator_arg_t, Alloc, Args...&gt; is true, returns std::tuple&lt;std::allocator_arg_t, const Alloc&amp;, Args&amp;&amp;...&gt;(std::allocator_arg, alloc, std::forward&lt;Args&gt;(args)...) 
* Otherwise, if std::uses_allocator_v&lt;T, Alloc&gt; is true and std::is_constructible_v&lt;T, Args..., Alloc&gt; is true, returns std::forward_as_tuple(std::forward&lt;Args&gt;(args)..., alloc) 
* Otherwise, the program is ill-formed 2) This overload only participates in overload resolution if T is a specialization of std::pair. For T = std::pair&lt;T1, T2&gt;, equivalent to
return std::make_tuple( std::piecewise_construct,
      std::apply( [&amp;alloc](auto&amp;&amp;... args1) {
    return std::uses_allocator_construction_args&lt;T1&gt;(alloc,
                                                     std::forward&lt;decltype(args1)&gt;(args1)...);
          }, std::forward&lt;Tuple1&gt;(x)),
      std::apply( [&amp;alloc](auto&amp;&amp;... args2) {
    return std::uses_allocator_construction_args&lt;T2&gt;(alloc,
                                                     std::forward&lt;decltype(args2)&gt;(args2)...);
          }, std::forward&lt;Tuple2&gt;(y))
      ); 
3) This overload only participates in overload resolution if T is a specialization of std::pair. Equivalent to return std::uses_allocator_construction_args&lt;T&gt;(alloc,
                                                std::piecewise_construct, std::tuple&lt;&gt;{}, std::tuple&lt;&gt;{}

); 
4) This overload only participates in overload resolution if T is a specialization of std::pair. Equivalent to return std::uses_allocator_construction_args&lt;T&gt;(alloc,
                                                std::piecewise_construct,
                                                std::forward_as_tuple(std::forward&lt;U&gt;(u)),
                                                std::forward_as_tuple(std::forward&lt;V&gt;(v))

); 
5) This overload only participates in overload resolution if T is a specialization of std::pair. Equivalent to return std::uses_allocator_construction_args&lt;T&gt;(alloc,
                                                std::piecewise_construct,
                                                std::forward_as_tuple(pr.first),
                                                std::forward_as_tuple(pr.second)

); 
6) This overload only participates in overload resolution if T is a specialization of std::pair. Equivalent to <pre><code>return std::uses_allocator_construction_args&lt;T&gt;(alloc,
                                                std::piecewise_construct,
                                                std::forward_as_tuple(std::move(pr).first),
                                                std::forward_as_tuple(std::move(pr).second));
</code></pre>

<h2>Parameters</h2>

alloc - the allocator to use. 
args - the arguments to pass to T's constructor 
x - tuple of arguments to pass to the constructors of T's .first 
y - tuple of arguments to pass to the constructors of T's .second 
u - single argument to pass to the constructor of T's .first 
v - single argument to pass to the constructor of T's .second 
pr - a pair whose .first will be passed to the constructor of T's .first and .second will be passed to the constructor of T's .second

<h2>Return value</h2>

std::tuple of arguments suitable for passing to the constructor of T 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>Notes</h2>

The overloads (2-6) provide allocator propagation into std::pair, which supports neither leading-allocator nor trailing-allocator calling conventions (unlike, e.g. std::tuple, which uses leading-allocator convention) 

<h2>See also</h2>

uses_allocator checks if the specified type supports uses-allocator construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
make_obj_using_allocator creates an object of the given type by means of uses-allocator construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
uninitialized_construct_using_allocator creates an object of the given type at specified memory location by means of uses-allocator construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
