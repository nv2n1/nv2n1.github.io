---
title: "stdexperimentalsplit(3)"
name: "stdexperimentalsplit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsplit/"
---

std::experimental::split - std::experimental::split

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    template &lt;std::size_t... Sizes, class T, class Abi&gt;

    std::tuple&lt;simd&lt;T, simd_abi::deduce_t&lt;T, Sizes&gt;&gt;...&gt;(1)

        split(const simd&lt;T, Abi&gt; &amp;v);

template &lt;std::size_t... Sizes, class T, class Abi&gt;

std::tuple&lt;simd_mask&lt;T, simd_abi::deduce_t&lt;T, Sizes&gt;&gt;...&gt;(2)

    split(const simd_mask&lt;T, Abi&gt; &amp;v);

template &lt;class V, class Abi&gt;

std::array&lt;V, simd_size_v&lt;typename V::value_type, Abi&gt; / V::size()&gt;(3)

    split(const simd&lt;typename V::value_type, Abi&gt; &amp;v);

template &lt;class V, class Abi&gt;

std::array&lt;V, simd_size_v&lt;typename V::value_type, Abi&gt; / V::size()&gt;(4)

    split(const simd_mask&lt;typename V::value_type, Abi&gt; &amp;v);</code></pre> 
Splits the input simd or simd_mask object into multiple simd or simd_mask objects. 
1-2) split the input object into potentially different types (e.g. types with different sizes) of objects. These functions do not participate in overloading resolution unless Sizes... sum up to v.size(). 
3-4) split the input object into a array of objects. These functions do not participate in overloading resolution unless 
* The array element must be of type simd or simd_mask, for the type of v as simd or simd_mask, respectively. 
* simd_size_v&lt;typename V::value_type, Abi&gt; is an integral multiple of V::size(). 

<h2>Parameters</h2>

v - the input simd or simd_mask object

<h2>Return value</h2>

1-2) a tuple that contains the splitted simd or simd_mask objects. 
3-4) an array that contains the splitted simd or simd_mask objects. 

<h2>Example</h2>


