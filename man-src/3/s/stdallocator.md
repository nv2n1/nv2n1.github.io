---
title: "stdallocator(3)"
name: "stdallocator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator/"
description: "std::allocator – std::allocator"
---

<p>std::allocator &#8211; std::allocator</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
template&lt; class T &gt; <code>(1)</code><br />
struct allocator;<br />
template&lt;&gt; <code>(2)</code> (deprecated in C++17)<br />
struct allocator&lt;void&gt;; (removed in C++20)<br />
The std::allocator class template is the default Allocator used by all standard library containers if no user-specified allocator is provided. The default allocator is stateless, that is, all instances of the given allocator are interchangeable, compare equal and can deallocate memory allocated by any other instance of the same allocator type.<br />
The explicit specialization for void lacks the member typedefs reference, const_reference, size_type and difference_type. This specialization declares no member functions. <i>(until C++20)</i><br />
All custom allocators also must be stateless. <i>(until C++11)</i><br />
Custom allocators may contain state. Each container or another allocator-aware object stores an instance of the supplied allocator and controls allocator replacement through std::allocator_traits. <i>(since C++11)</i><br />
The default allocator satisfies allocator_completeness_requirements. <i>(since C++17)</i> </p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type T<br />
pointer (deprecated in C++17)(removed in C++20) T*<br />
const_pointer (deprecated in C++17)(removed in C++20) const T*<br />
reference (deprecated in C++17)(removed in C++20) T&amp;<br />
const_reference (deprecated in C++17)(removed in C++20) const T&amp;<br />
size_type std::size_t<br />
difference_type std::ptrdiff_t<br />
propagate_on_container_move_assignment<i>(C++14)</i> std::true_type<br />
rebind (deprecated in C++17)(removed in C++20) template&lt; class U &gt; struct rebind { typedef allocator&lt;U&gt; other; };<br />
is_always_equal<i>(C++17)</i> std::true_type</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a new allocator instance<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs an allocator instance<br />
destructor <i>(public member function)</i> </p>
<p>address obtains the address of an object, even if operator&amp; is overloaded<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(deprecated in C++17)<br />
(removed in C++20)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates uninitialized storage<br />
allocate <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates storage<br />
deallocate <i>(public member function)</i> </p>
<p>max_size returns the largest supported allocation size<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(deprecated in C++17)<br />
(removed in C++20) </p>
<p>construct constructs an object in allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(deprecated in C++17)<br />
(removed in C++20) </p>
<p>destroy destructs an object in allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(deprecated in C++17)<br />
(removed in C++20)</p>
<h2>Non-member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two allocator instances<br />
operator== <i>(public member function)</i><br />
operator!=</p>
<h2>Notes</h2>
<p>The member template class rebind provides a way to obtain an allocator for a different type. For example,<br />
std::list&lt;T, A&gt; allocates nodes of some internal type Node&lt;T&gt;, using the allocator A::rebind&lt;Node&lt;T&gt;&gt;::other <i>(until C++11)</i><br />
std::list&lt;T, A&gt; allocates nodes of some internal type Node&lt;T&gt;, using the allocator std::allocator_traits&lt;A&gt;::rebind_alloc&lt;Node&lt;T&gt;&gt;, which is implemented in terms of A::rebind&lt;Node&lt;T&gt;&gt;::other if A is an std::allocator <i>(since C++11)</i> </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;memory&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;
int main()

{
    std::allocator&lt;int&gt; a1;  // default allocator for ints
    int *a = a1.allocate(1); // space for one int
    a1.construct(a, 7);      // construct the int
    std::cout &lt;&lt; a[0] &lt;&lt; '
';
    a1.deallocate(a, 1); // deallocate space for one int
                         // default allocator for strings
    std::allocator&lt;std::string&gt; a2;
    // same, but obtained by rebinding from the type of a1
    decltype(a1)::rebind&lt;std::string&gt;::other a2_1;
    // same, but obtained by rebinding from the type of a1 via allocator_traits
    std::allocator_traits&lt;decltype(a1)&gt;::rebind_alloc&lt;std::string&gt; a2_2;
    std::string *s = a2.allocate(2); // space for 2 strings
    a2.construct(s, &quot;foo&quot;);
    a2.construct(s + 1, &quot;bar&quot;);
    std::cout &lt;&lt; s[0] &lt;&lt; ' ' &lt;&lt; s[1] &lt;&lt; '
';
    a2.destroy(s);
    a2.destroy(s + 1);
    a2.deallocate(s, 2);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;7<br />
&nbsp;<wbr>&nbsp;foo bar</p>
<h2>See also</h2>
<p>allocator_traits provides information about allocator types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
scoped_allocator_adaptor implements multi-level allocator for multi-level containers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
uses_allocator checks if the specified type supports uses-allocator construction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
