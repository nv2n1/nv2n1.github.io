---
title: "stdreverse_iterator(3)"
name: "stdreverse_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreverse_iterator/"
---

std::reverse_iterator - std::reverse_iterator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class Iter &gt;

class reverse_iterator : public std::iterator&lt;

typename std::iterator_traits&lt;Iter&gt;::iterator_category,

typename std::iterator_traits&lt;Iter&gt;::value_type,         (until C++17)

typename std::iterator_traits&lt;Iter&gt;::difference_type,

typename std::iterator_traits&lt;Iter&gt;::pointer,

typename std::iterator_traits&lt;Iter&gt;::reference &gt;

template&lt; class Iter &gt;                                   (since C++17)

class reverse_iterator;</code></pre> 
std::reverse_iterator is an iterator adaptor that reverses the direction of a given iterator. In other words, when provided with a bidirectional iterator, std::reverse_iterator produces a new iterator that moves from the end to the beginning of the sequence defined by the underlying bidirectional iterator. 
For a reverse iterator r constructed from an iterator i, the relationship &amp;*r == &amp;*(i-1) is always true (as long as r is dereferenceable); thus a reverse iterator constructed from a one-past-the-end iterator dereferences to the last element in a sequence. 
This is the iterator returned by member functions rbegin() and rend() of the standard library containers. 
&nbsp;range-rbegin-rend.svg 

<h2>Member types</h2>

Member type Definition 
value_type std::iterator_traits&lt;Iter&gt;::value_type 
difference_type std::iterator_traits&lt;Iter&gt;::difference_type 
pointer std::iterator_traits&lt;Iter&gt;::pointer 
reference std::iterator_traits&lt;Iter&gt;::reference 
iterator_category std::iterator_traits&lt;Iter&gt;::iterator_category 

 

 
These member types are required to be obtained by inheriting from std::iterator&lt; std::iterator_traits&lt;Iter&gt;::iterator_category 
, std::iterator_traits&lt;Iter&gt;::value_type 
, std::iterator_traits&lt;Iter&gt;::difference_type <i>(until C++17)</i> 
, std::iterator_traits&lt;Iter&gt;::pointer 
, std::iterator_traits&lt;Iter&gt;::reference 
&gt;. 

 

 
Member type Definition 
iterator_type Iter

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new iterator adaptor 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns another iterator 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the underlying iterator 
base <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the pointed-to element 
operator* <i>(public member function)</i> 
operator-&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses an element by index 
operator[] <i>(public member function)</i> 

 
operator++ 
operator++(int) 
operator+= advances or decrements the iterator 
operator+ <i>(public member function)</i> 
operator-- 
operator--(int) 
operator-= 
operator-

<h2>Member objects</h2>

Member name Definition 
current (protected) a copy of the base() iterator

<h2>Non-member functions</h2>

make_reverse_iterator creates a std::reverse_iterator of type inferred from the argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++14)</i> 

 
operator== 
operator!= compares the underlying iterators 
operator&lt; <i>(function template)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances the iterator 
operator+ <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the distance between two iterator adaptors 
operator- <i>(function template)</i>

<h2>Notes</h2>

std::reverse_iterator does not work with iterators that return a reference to a member object (so-called &quot;stashing iterators&quot;). An example of stashing iterator is std::filesystem::path::iterator.


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;iterator&gt;
int main()

{
    std::string s = &quot;Hello, world&quot;;
    std::reverse_iterator&lt;std::string::iterator&gt; r = s.rbegin();
    r[7] = 'O'; // replaces 'o' with 'O'
    r += 7;     // iterator now points at 'O'
    std::string rev(r, s.rend());
    std::cout &lt;&lt; rev &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;OlleH

<h2>See also</h2>

iterator base class to ease the definition of required types for simple iterators 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++17) 
