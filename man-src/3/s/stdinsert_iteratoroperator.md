---
title: "stdinsert_iteratoroperator(3)"
name: "stdinsert_iteratoroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinsert_iteratoroperator/"
---

std::insert_iterator&lt;Container&gt;::operator= - std::insert_iterator&lt;Container&gt;::operator=

<h2>Synopsis</h2>

<pre><code>insert_iterator&lt;Container&gt; &amp;(until C++ 11)

operator=(typename Container::const_reference value);

insert_iterator&lt;Container&gt; &amp;(since C++ 11)

operator=(const typename Container::value_type &amp;value);
(until C++ 20)

    constexpr insert_iterator&lt;Container&gt; &amp;(1)(since C++ 20)

    operator=(const typename Container::value_type &amp;value);

insert_iterator&lt;Container&gt; &amp;(since C++ 11)

operator=(typename Container::value_type &amp;&amp;value);
(2)(until C++ 20)

    constexpr insert_iterator&lt;Container&gt; &amp;(since C++ 20)

    operator=(typename Container::value_type &amp;&amp;value);
Inserts the given value value to the container.

1) Results in iter = container-&gt;insert(iter, value);
++iter;

2) Results in iter = container-&gt;insert(iter, std::move(value));
++iter;
</code></pre>

<h2>Parameters</h2>

value - the value to insert

<h2>Return value</h2>

*this 

<h2>Notes</h2>

This function exploits the signature compatibility between hinted insert for associative containers (such as std::set::insert) and positional insert for sequential containers (such as std::vector::insert). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;deque&gt;
int main()

{
    std::deque&lt;int&gt; q;
    std::insert_iterator&lt;std::deque&lt;int&gt;&gt; it(q, q.begin());
    for (int i = 0; i &lt; 10; ++i)
        it = i; // inserts i
    for (auto &amp;elem : q)
        std::cout &lt;&lt; elem &lt;&lt; ' ';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0 1 2 3 4 5 6 7 8 9
