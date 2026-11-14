---
title: "stdvector(3)"
name: "stdvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvector/"
description: "std::vector<bool> – std::vector<bool>"
---

<p>std::vector&lt;bool&gt; &#8211; std::vector&lt;bool&gt;</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;vector&gt;

template&lt;class Allocator&gt;

class vector&lt;bool, Allocator&gt;;</code></pre>
<p>std::vector&lt;bool&gt; is a possibly space-efficient specialization of std::vector for the type bool.<br />
The manner in which std::vector&lt;bool&gt; is made space efficient (as well as whether it is optimized at all) is implementation defined. One potential optimization involves coalescing vector elements such that each element occupies a single bit instead of sizeof(bool) bytes.<br />
std::vector&lt;bool&gt; behaves similarly to std::vector, but in order to be space efficient, it:<br />
* Does not necessarily store its elements as a contiguous array (so &amp;v[0] + n != &amp;v[n])<br />
* Exposes class std::vector&lt;bool&gt;::reference as a method of accessing individual bits. In particular, objects of this class are returned by operator[] by value.<br />
* Does not use std::allocator_traits::construct to construct bit values.<br />
* Does not guarantee that different elements in the same container can be modified concurrently by different threads. </p>
<h2>Member types</h2>
<p>Member type Definition<br />
value_type bool<br />
allocator_type Allocator<br />
size_type implementation-defined<br />
difference_type implementation-defined<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;proxy class representing a reference to a single bool<br />
reference <i>(class)</i><br />
const_reference bool<br />
pointer implementation-defined<br />
const_pointer implementation-defined<br />
iterator implementation-defined<br />
const_iterator implementation-defined<br />
reverse_iterator std::reverse_iterator&lt;iterator&gt;<br />
const_reverse_iterator std::reverse_iterator&lt;const_iterator&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the vector<br />
constructor <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the vector<br />
destructor <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns values to the container<br />
operator= <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns values to the container<br />
assign <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the associated allocator<br />
get_allocator <i>(public member function of std::vector&lt;T,Allocator&gt;)</i></p>
<h2>Element access</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;access specified element with bounds checking<br />
at <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;access specified element<br />
operator[] <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;access the first element<br />
front <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;access the last element<br />
back <i>(public member function of std::vector&lt;T,Allocator&gt;)</i></p>
<h2>Iterators</h2>
<p>begin returns an iterator to the beginning<br />
cbegin <i>(public member function of std::vector&lt;T,Allocator&gt;)</i> </p>
<p>end_ returns an iterator to the end<br />
cend <i>(public member function of std::vector&lt;T,Allocator&gt;)</i> </p>
<p>rbegin returns a reverse iterator to the beginning<br />
crbegin <i>(public member function of std::vector&lt;T,Allocator&gt;)</i> </p>
<p>rend returns a reverse iterator to the end<br />
crend <i>(public member function of std::vector&lt;T,Allocator&gt;)</i></p>
<h2>Capacity</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the container is empty<br />
empty <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of elements<br />
size <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the maximum possible number of elements<br />
max_size <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reserves storage<br />
reserve <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of elements that can be held in currently allocated storage<br />
capacity <i>(public member function of std::vector&lt;T,Allocator&gt;)</i></p>
<h2>Modifiers</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears the contents<br />
clear <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inserts elements<br />
insert <i>(public member function of std::vector&lt;T,Allocator&gt;)</i> </p>
<p>emplace constructs element in-place<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
<i>(C++14)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;erases elements<br />
erase <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;adds an element to the end<br />
push_back <i>(public member function of std::vector&lt;T,Allocator&gt;)</i> </p>
<p>emplace_back constructs elements in-place at the end<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
<i>(C++14)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes the last element<br />
pop_back <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the number of elements stored<br />
resize <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents<br />
swap <i>(public member function of std::vector&lt;T,Allocator&gt;)</i></p>
<h2>vector&lt;bool&gt; specific modifiers</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flips all the bits<br />
flip <i>(public member function)</i> </p>
<p>swap swaps two std::vector&lt;bool&gt;::references<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
<h2>Non-member functions</h2>
<p>operator==<br />
operator!= lexicographically compares the values in the vector<br />
operator&lt; <i>(function template)</i><br />
operator&lt;=<br />
operator&gt;<br />
operator&gt;=<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes the std::swap algorithm<br />
std::swap(std::vector) <i>(function template)</i></p>
<h2>Helper classes</h2>
<p>std::hash&lt;std::vector&lt;bool&gt;&gt; hash support for std::vector&lt;bool&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i><br />
<i>(C++11)</i></p>
<h2>Notes</h2>
<p>If the size of the bitset is known at compile time, std::bitset may be used, which offers a richer set of member functions. In addition, boost::dynamic_bitset exists as an alternative to std::vector&lt;bool&gt;.<br />
Since its representation may by optimized, std::vector&lt;bool&gt; does not necessarily meet all Container or SequenceContainer requirements. For example, because std::vector&lt;bool&gt;::iterator is implementation-defined, it may not satisfy the LegacyForwardIterator requirement. Use of algorithms such as std::search that require LegacyForwardIterators may result in either_compile-time_or_run-time_errors.<br />
The Boost.Container_version_of_vector does not specialize for bool. </p>
