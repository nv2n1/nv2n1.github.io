---
title: "stdback_insert_iterator(3)"
name: "stdback_insert_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdback_insert_iterator/"
---

std::back_insert_iterator - std::back_insert_iterator

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class Container&gt;

    class back_insert_iterator : public std::iterator&lt;std::output_iterator_tag, (until C++ 17)

                                                                                    void,
                                                      void, void, void&gt;

                                 template &lt;class Container&gt;
                                 (since C++ 17)

                                     class back_insert_iterator;</code></pre> 
std::back_insert_iterator is an LegacyOutputIterator that appends to a container for which it was constructed. The container's push_back() member function is called whenever the iterator (whether dereferenced or not) is assigned to. Incrementing the std::back_insert_iterator is a no-op. 

<h2>Member types</h2>

Member type Definition 
container_type Container

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new back_insert_iterator 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inserts an object into the associated container 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no-op 
operator* <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no-op 
operator++ <i>(public member function)</i> 
operator++(int)

<h2>Member objects</h2>

Member name Definition 
container (protected) a pointer of type Container*

<h2>Member types</h2>

Member type Definition 
value_type void 
difference_type void 
pointer void 
reference void 
iterator_category std::output_iterator_tag 

 

 
These member types are required to be obtained by inheriting from std::iterator&lt;std::output_iterator_tag, void, void, void, void&gt;. <i>(until C++17)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;algorithm&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v;
    std::generate_n(std::back_insert_iterator&lt;std::vector&lt;int&gt;&gt;(v), // can be simplified
                    10, [n = 0]() mutable { return ++n; });         // with std::back_inserter
    for (int n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 3 4 5 6 7 8 9 10

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::back_insert_iterator of type inferred from the argument 
back_inserter <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for insertion at the front of a container 
front_insert_iterator <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for insertion into a container 
insert_iterator <i>(class template)</i> 
