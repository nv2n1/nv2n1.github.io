---
title: "stdexperimentalweak_ptr(3)"
name: "stdexperimentalweak_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalweak_ptr/"
---

std::experimental::weak_ptr - std::experimental::weak_ptr

<h2>Synopsis</h2>

Defined in header &lt;experimental/memory&gt; 
template&lt; class T &gt; class weak_ptr; (library fundamentals TS) 
std::experimental::weak_ptr is a modified version of std::weak_ptr that interoperates with std::experimental::shared_ptr and has support for arrays. 

<h2>Member types</h2>

Member type Definition 
element_type std::remove_extent_t&lt;T&gt;

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new weak_ptr 
constructor <i>(public member function)</i> 

 

 
Members and non-members identical to std::weak_ptr

<h2>Member functions</h2>

The following member functions work with std::experimental::shared_ptr instead of std::shared_ptr and std::experimental::weak_ptr instead of std::weak_ptr. The behavior is otherwise identical. 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a weak_ptr 
destructor <i>(public member function of std::weak_ptr&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the weak_ptr 
operator= <i>(public member function of std::weak_ptr&lt;T&gt;)</i>

<h2>Modifiers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;releases the ownership of the managed object 
reset <i>(public member function of std::weak_ptr&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the managed objects 
swap <i>(public member function of std::weak_ptr&lt;T&gt;)</i>

<h2>Observers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of shared_ptr objects that manage the object 
use_count <i>(public member function of std::weak_ptr&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the referenced object was already deleted 
expired <i>(public member function of std::weak_ptr&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a shared_ptr that manages the referenced object 
lock <i>(public member function of std::weak_ptr&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides owner-based ordering of weak pointers 
owner_before <i>(public member function of std::weak_ptr&lt;T&gt;)</i>

<h2>Non-member functions</h2>

This non-member function is declared in the std::experimental namespace, and work with std::experimental::weak_ptr rather than std::weak_ptr, but otherwise behaves identically to the corresponding C++14 function. 

 

 
std::swap(std::weak_ptr) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
