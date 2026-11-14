---
title: "stdreverse_iteratorbase(3)"
name: "stdreverse_iteratorbase"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreverse_iteratorbase/"
---

std::reverse_iterator&lt;Iter&gt;::base - std::reverse_iterator&lt;Iter&gt;::base

<h2>Synopsis</h2>

iterator_type base() const; <i>(until C++17)</i> 
constexpr iterator_type base() const; <i>(since C++17)</i> 
Returns the underlying base iterator. That is std::reverse_iterator(it).base() == it. 
The base iterator refers to the element that is next (from the std::reverse_iterator::iterator_type perspective) to the element the reverse_iterator is currently pointing to. That is &amp;*(rit.base() - 1) == &amp;*rit. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The underlying iterator. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v = {0, 1, 2, 3, 4, 5};
    using RevIt = std::reverse_iterator&lt;std::vector&lt;int&gt;::iterator&gt;;
    {
        const auto it = v.begin() + 3;
        RevIt r_it(it);
        std::cout &lt;&lt; &quot;*it == &quot; &lt;&lt; *it &lt;&lt; &quot;, *r_it.base() == &quot; &lt;&lt; *r_it.base()
                  &lt;&lt; '\n'
                  &lt;&lt; &quot;*r_it == &quot; &lt;&lt; *r_it &lt;&lt; &quot;, *(r_it.base()-1) == &quot; &lt;&lt; *(r_it.base() - 1) &lt;&lt; &quot;\n&quot;;
    }
    {
        RevIt r_end(v.begin());
        RevIt r_begin(v.end());
        for (auto it = r_end.base(); it != r_begin.base(); ++it) {
            std::cout &lt;&lt; *it &lt;&lt; &quot; &quot;;
        }
        std::cout &lt;&lt; &quot;\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;*it == 3, *r_it.base() == 3 
&nbsp;<wbr>&nbsp;*r_it == 2, *(r_it.base()-1) == 2 
&nbsp;<wbr>&nbsp;0 1 2 3 4 5

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the pointed-to element 
operator* <i>(public member function)</i> 
operator-&gt; 
