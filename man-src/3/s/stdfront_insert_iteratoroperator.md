---
title: "stdfront_insert_iteratoroperator(3)"
name: "stdfront_insert_iteratoroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfront_insert_iteratoroperator/"
---

std::front_insert_iterator&lt;Container&gt;::operator= - std::front_insert_iterator&lt;Container&gt;::operator=

<h2>Synopsis</h2>

<pre><code>front_insert_iterator&lt;Container&gt; &amp;(until C++ 11)

operator=(typename Container::const_reference value);

front_insert_iterator&lt;Container&gt; &amp;(since C++ 11)

operator=(const typename Container::value_type &amp;value);
(until C++ 20)

    constexpr front_insert_iterator&lt;Container&gt; &amp;(1)(since C++ 20)

    operator=(const typename Container::value_type &amp;value);

front_insert_iterator&lt;Container&gt; &amp;(since C++ 11)

operator=(typename Container::value_type &amp;&amp;value);
(2)(until C++ 20)

    constexpr front_insert_iterator&lt;Container&gt; &amp;(since C++ 20)

    operator=(typename Container::value_type &amp;&amp;value);</code></pre> 
Inserts the given value value to the container. 
1) Results in container-&gt;push_front(value) 
2) Results in container-&gt;push_front(std::move(value)) 

<h2>Parameters</h2>

value - the value to insert

<h2>Return value</h2>

*this 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;deque&gt;
int main()

{
    std::deque&lt;int&gt; q;
    std::front_insert_iterator&lt;std::deque&lt;int&gt;&gt; it(q);
    for (int i = 0; i &lt; 10; ++i)
        it = i; // calls q.push_front(i)
    for (auto &amp;elem : q)
        std::cout &lt;&lt; elem &lt;&lt; ' ';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;9 8 7 6 5 4 3 2 1 0
