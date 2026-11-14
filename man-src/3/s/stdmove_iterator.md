---
title: "stdmove_iterator(3)"
name: "stdmove_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmove_iterator/"
---

std::move_iterator - std::move_iterator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class Iter &gt;        (since C++11)

class move_iterator;</code></pre> 
std::move_iterator is an iterator adaptor which behaves exactly like the underlying iterator (which must be at least an LegacyInputIterator), except that dereferencing converts the value returned by the underlying iterator into an rvalue. If this iterator is used as an input iterator, the effect is that the values are moved from, rather than copied from. 

<h2>Member types</h2>

Member type Definition 
iterator_type Iter 
difference_type std::iterator_traits&lt;Iter&gt;::difference_type 
pointer Iter 
value_type std::iterator_traits&lt;Iter&gt;::value_type 
iterator_category std::iterator_traits&lt;Iter&gt;::iterator_category 

 
reference value_type&amp;&amp; <i>(until C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;If std::iterator_traits&lt;Iter&gt;::reference is a reference, this is the rvalue reference version of the same type. Otherwise (such as if the wrapped iterator returns by value), this is std::iterator_traits&lt;Iter&gt;::reference unchanged <i>(since C++17)</i>

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new iterator adaptor 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns another iterator 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the underlying iterator 
base <i>(public member function)</i> 

 
operator* 
operator-&gt; accesses the pointed-to element 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 

 
(deprecated in C++20) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses an element by index 
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
current (private) a copy of the base() iterator, the name is for exposition only

<h2>Non-member functions</h2>

operator== 
operator!= compares the underlying iterators 
operator&lt; <i>(function template)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances the iterator 
operator+ <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the distance between two iterator adaptors 
operator- <i>(function template)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iterator&gt;

#include &lt;numeric&gt;

#include &lt;string&gt;
int main()

{
    std::vector&lt;std::string&gt; v{&quot;this&quot;, &quot;is&quot;, &quot;an&quot;, &quot;example&quot;};
    std::cout &lt;&lt; &quot;Old contents of the vector: &quot;;
    for (auto &amp;s : v)
        std::cout &lt;&lt; '&quot;' &lt;&lt; s &lt;&lt; &quot;\&quot; &quot;;
    typedef std::vector&lt;std::string&gt;::iterator iter_t;
    std::string concat = std::accumulate(
        std::move_iterator&lt;iter_t&gt;(v.begin()),
        std::move_iterator&lt;iter_t&gt;(v.end()),
        std::string()); // Can be simplified with std::make_move_iterator
    std::cout &lt;&lt; &quot;\nConcatenated as string: &quot; &lt;&lt; concat &lt;&lt; '\n'
              &lt;&lt; &quot;New contents of the vector: &quot;;
    for (auto &amp;s : v)
        std::cout &lt;&lt; '&quot;' &lt;&lt; s &lt;&lt; &quot;\&quot; &quot;;
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Old contents of the vector: &quot;this&quot; &quot;is&quot; &quot;an&quot; &quot;example&quot; 
&nbsp;<wbr>&nbsp;Concatenated as string: thisisanexample 
&nbsp;<wbr>&nbsp;New contents of the vector: &quot;&quot; &quot;&quot; &quot;&quot; &quot;&quot;

<h2>See also</h2>

make_move_iterator creates a std::move_iterator of type inferred from the argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
