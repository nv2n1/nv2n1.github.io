---
title: "stdexperimentalfunctionfunction(3)"
name: "stdexperimentalfunctionfunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfunctionfunction/"
---

std::experimental::function&lt;R(Args...)&gt;::function - std::experimental::function&lt;R(Args...)&gt;::function

<h2>Synopsis</h2>

<pre><code>function() noexcept;
(1)(library fundamentals TS)

    function(std::nullptr_t) noexcept;
(2)(library fundamentals TS)

    function(const function &amp;other);
(3)(library fundamentals TS)

    function(function &amp;&amp;other);
(4)(library fundamentals TS)

    template &lt;class F&gt;
    (5)(library fundamentals TS)

        function(F f);

template &lt;class Alloc&gt;
(6)(library fundamentals TS)

    function(std::allocator_arg_t, const Alloc &amp;alloc) noexcept;

template &lt;class Alloc&gt;

function(std::allocator_arg_t, const Alloc &amp;alloc, (7)(library fundamentals TS)

                                                       std::nullptr_t) noexcept;

template &lt;class Alloc&gt;

function(std::allocator_arg_t, const Alloc &amp;alloc, (8)(library fundamentals TS)

                                                       const function &amp;other);

template &lt;class Alloc&gt;

function(std::allocator_arg_t, const Alloc &amp;alloc, (9)(library fundamentals TS)

                                                       function &amp;&amp;other);

template &lt;class F, class Alloc&gt;
(10)(library fundamentals TS)

    function(std::allocator_arg_t, const Alloc &amp;alloc, F f);
Constructs a std::experimental::function from a variety of sources.

1-2) Creates an empty function.

3-4) Copies (3) or moves (4) the target of other to the target of *this. If other is empty, *this will be empty after the call too.

5) Initializes the target with a copy of f. If f is a null pointer to function or null pointer to member, *this will be empty after the call. This constructor does not participate in overload resolution unless f is Callable for argument types Args... and return type R.

6-10) Same as (1-5) except that alloc is used to allocate memory for any internal data structures that the function might use. These constructors treat alloc as a type-erased allocator (see below).

When the target is a function pointer or a std::reference_wrapper, small object optimization is guaranteed, that is, these targets are always directly stored inside the std::experimental::function object, no dynamic allocation takes place. Other large objects may be constructed in dynamic allocated storage and accessed by the std::experimental::function object through a pointer.

If a constructor moves or copies a function object, including an instance of std::experimental::function, then that move or copy is performed by using-allocator_construction with allocator this-&gt;get_memory_resource().</code></pre> 
Type-erased allocator 
The constructors of function taking an allocator argument alloc treats that argument as a type-erased allocator. The memory resource pointer used by function to allocate memory is determined using the allocator argument (if specified) as follows: 
Type of alloc value of the memory resource pointer 
Non-existent (no allocator specified at time of construction) The value of std::experimental::pmr::get_default_resource() at time of construction. 
std::nullptr_t The value of std::experimental::pmr::get_default_resource() at time of construction 
A pointer type convertible to static_cast&lt;std::experimental::pmr::memory_resource*&gt;(alloc) 
std::experimental::pmr::memory_resource* 
A specialization of alloc.resource() 
std::experimental::pmr::polymorphic_allocator 
Any other type meeting the Allocator requirements A pointer to a value of type std::experimental::pmr::resource_adaptor&lt;A&gt;(alloc), where A is the type of alloc. The pointer remains valid only for the lifetime of the function object. 
None of the above The program is ill-formed. 

<h2>Parameters</h2>

other - the function object used to initialize *this 
f - a callable used to initialize *this 
alloc - an allocator used for internal memory allocation

<h2>Type requirements</h2>

- 
F must meet the requirements of Callable and CopyConstructible.

<h2>Exceptions</h2>

3,8) does not throw if other's target is a function pointer or a std::reference_wrapper, otherwise may throw std::bad_alloc or any exception thrown by the copy constructor of the stored callable object. 
4) <i>(none)</i> 
5,10) does not throw if f is a function pointer or a std::reference_wrapper, otherwise may throw std::bad_alloc or any exception thrown by the copy constructor of the stored callable object. 
9) <i>(none)</i>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
