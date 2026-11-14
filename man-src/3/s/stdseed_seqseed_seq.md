---
title: "stdseed_seqseed_seq(3)"
name: "stdseed_seqseed_seq"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdseed_seqseed_seq/"
---

std::seed_seq::seed_seq - std::seed_seq::seed_seq

<h2>Synopsis</h2>

<pre><code>seed_seq();
(1)(since C++ 11)

    seed_seq(const seed_seq &amp;) = delete;
(2)(since C++ 11)

    template &lt;class InputIt&gt;
    (3)(since C++ 11)

        seed_seq(InputIt begin, InputIt end);

template &lt;class T&gt;
(4)(since C++ 11)

    seed_seq(std::initializer_list&lt;T&gt; il);</code></pre> 
1) The default constructor creates a std::seed_seq object with an initial seed sequence of length zero. 
2) The copy constructor is deleted: std::seed_seq is not copyable. 
3) Constructs a std::seed_seq with the initial seed sequence obtained by iterating over the range [begin, end) and copying the values obtained by dereferencing the iterator, modulo 232 
(that is, the lower 32 bits are copied) 
4) Equivalent to seed_seq(il.begin(), il.end()). This constructor enables list-initialization. 

<h2>Parameters</h2>

begin, end - the initial seed sequence represented as a pair of input iterators whose std::iterator_traits&lt;&gt;::value_type is an integer type 
il - std::initializer_list of objects of integer type, providing the initial seed sequence

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator.

<h2>Exceptions</h2>

1) Does not throw

<h2>Example</h2>

// Run this code <pre><code>#include &lt;random&gt;

#include &lt;sstream&gt;

#include &lt;iterator&gt;

int main()

{
    std::seed_seq s1;              // default-constructible
    std::seed_seq s2{1, 2, 3};     // can use list-initialization
    std::seed_seq s3 = {-1, 0, 1}; // another form of list-initialization
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::seed_seq s4(a, a + 10); // can use iterators
    std::istringstream buf(&quot;1 2 3 4 5&quot;);
    std::istream_iterator&lt;int&gt; beg(buf), end;
    std::seed_seq s5(beg, end); // even stream input iterators
}
</code></pre>
