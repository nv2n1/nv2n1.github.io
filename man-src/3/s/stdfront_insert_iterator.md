---
title: "stdfront_insert_iterator(3)"
name: "stdfront_insert_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfront_insert_iterator/"
---

std::front_insert_iterator - std::front_insert_iterator

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class Container&gt;

    class front_insert_iterator : public std::iterator&lt;std::output_iterator_tag, (until C++ 17)

                                                                                     void,
                                                       void, void, void&gt;

                                  template &lt;class Container&gt;
                                  (since C++ 17)

                                      class front_insert_iterator;</code></pre> 
std::front_insert_iterator is an LegacyOutputIterator that prepends elements to a container for which it was constructed. The container's push_front() member function is called whenever the iterator (whether dereferenced or not) is assigned to. Incrementing the std::front_insert_iterator is a no-op. 

<h2>Member types</h2>

Member type Definition 
container_type Container

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new front_insert_iterator 
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

// Run this code <pre><code>#include &lt;vector&gt;

#include &lt;deque&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;algorithm&gt;

int main()

{
    std::vector&lt;int&gt; v{1, 2, 3, 4, 5};
    std::deque&lt;int&gt; d;
    std::copy(v.begin(), v.end(),
              std::front_insert_iterator&lt;std::deque&lt;int&gt;&gt;(d)); // or std::front_inserter(d)
    for (int n : d)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;5 4 3 2 1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::front_insert_iterator of type inferred from the argument 
front_inserter <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for insertion at the end of a container 
back_insert_iterator <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for insertion into a container 
insert_iterator <i>(class template)</i> 
