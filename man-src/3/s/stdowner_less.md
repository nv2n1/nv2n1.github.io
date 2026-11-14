---
title: "stdowner_less(3)"
name: "stdowner_less"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdowner_less/"
---

std::owner_less - std::owner_less

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;memory&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct owner_less; /* undefined */
(until C++ 17)

    template &lt;class T = void&gt;
    (since C++ 17)

        struct owner_less; /* undefined */

template &lt;class T&gt;
(1)(2)(since C++ 11)

    struct owner_less&lt;std::shared_ptr&lt;T&gt;&gt;;

template &lt;class T&gt;
(3)(since C++ 11)

    struct owner_less&lt;std::weak_ptr&lt;T&gt;&gt;;

template &lt;&gt;
(4)(since C++ 17)

    struct owner_less&lt;void&gt;;</code></pre> 
This function object provides owner-based (as opposed to value-based) mixed-type ordering of both std::weak_ptr and std::shared_ptr. The order is such that two smart pointers compare equivalent only if they are both empty or if they share ownership, even if the values of the raw pointers obtained by get() are different (e.g. because they point at different subobjects within the same object) 
This class template is the preferred comparison predicate when building associative containers with std::shared_ptr or std::weak_ptr as keys, that is, 
std::map&lt;std::shared_ptr&lt;T&gt;, U, std::owner_less&lt;std::shared_ptr&lt;T&gt;&gt;&gt; 
or 
std::map&lt;std::weak_ptr&lt;T&gt;, U, std::owner_less&lt;std::weak_ptr&lt;T&gt;&gt;&gt;. 
The default operator&lt; is not defined for weak pointers, and may wrongly consider two shared pointers for the same object non-equivalent (see shared_ptr::owner_before) 

<h2>Specializations</h2>

The standard library provides a specialization of std::owner_less when T is not specified. In this case, the parameter types are deduced from the arguments (each of which must still be either a std::shared_ptr or a std::weak_ptr). 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object providing mixed-type owner-based ordering of shared and weak pointers, regardless of the type of the pointee <i>(since C++17)</i> 
owner_less&lt;void&gt; <i>(class template specialization)</i>

<h2>Member types</h2>

Member type Definition 
result_type(deprecated in c++17) 2-3) bool <i>(until C++20)</i> 
first_argument_type(deprecated in c++17) 2) std::shared_ptr&lt;T&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3) std::weak_ptr&lt;T&gt; 
second_argument_type(deprecated in c++17) 2) std::shared_ptr&lt;T&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3) std::weak_ptr&lt;T&gt;

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares its arguments using owner-based semantics 
operator() <i>(function)</i> 

 

 
&nbsp;std::owner_less::operator() 

 

 
bool operator()( const std::shared_ptr&lt;T&gt;&amp; lhs, <i>(since C++11)</i> 
const std::shared_ptr&lt;T&gt;&amp; rhs ) const; (member only of owner_less&lt;shared_ptr&lt;T&gt;&gt; template specialization) 
bool operator()( const std::shared_ptr&lt;T&gt;&amp; lhs, <i>(since C++11)</i> 
const std::weak_ptr&lt;T&gt;&amp; rhs ) const; 
bool operator()( const std::weak_ptr&lt;T&gt;&amp; lhs, <i>(since C++11)</i> 
const std::shared_ptr&lt;T&gt;&amp; rhs ) const; 
bool operator()( const std::weak_ptr&lt;T&gt;&amp; lhs, <i>(since C++11)</i> 
const std::weak_ptr&lt;T&gt;&amp; rhs ) const; (member only of owner_less&lt;weak_ptr&lt;T&gt;&gt; template specialization) 

 
Compares lhs and rhs using owner-based semantics. Effectively calls lhs.owner_before(rhs). 
The ordering is strict weak ordering relation. 
lhs and rhs are equivalent only if they are both empty or share ownership.

<h2>Parameters</h2>

lhs, rhs - shared-ownership pointers to compare

<h2>Return value</h2>

true if lhs is less than rhs as determined by the owner-based ordering. 

<h2>Exceptions</h2>

<i>(none)</i> <i>(until C++17)</i> 
noexcept specification: <i>(since C++17)</i> 
noexcept

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides owner-based ordering of shared pointers 
owner_before <i>(public member function of std::shared_ptr&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides owner-based ordering of weak pointers 
owner_before <i>(public member function of std::weak_ptr&lt;T&gt;)</i> 
