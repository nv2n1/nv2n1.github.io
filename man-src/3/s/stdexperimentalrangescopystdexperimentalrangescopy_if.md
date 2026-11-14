---
title: "stdexperimentalrangescopystdexperimentalrangescopy_if(3)"
name: "stdexperimentalrangescopystdexperimentalrangescopy_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangescopystdexperimentalrangescopy_if/"
---

std::experimental::ranges::copy,std::experimental::ranges::copy_if - std::experimental::ranges::copy,std::experimental::ranges::copy_if

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / algorithm&gt;

    template &lt;InputIterator I, Sentinel&lt;I&gt; S, WeaklyIncrementable O&gt;

requires IndirectlyCopyable&lt;I, O&gt;(1)
(ranges TS)

    ranges::tagged_pair&lt;tag::in(I), tag::out(O)&gt;

    copy(I first, S last, O result);

template &lt;InputRange R, WeaklyIncrementable O&gt;

requires IndirectlyCopyable&lt;ranges::iterator_t&lt;R&gt;, O&gt;(2)
(ranges TS)

    ranges::tagged_pair&lt;tag::in(ranges::safe_iterator_t&lt;R&gt;), tag::out(O)&gt;

    copy(R &amp;&amp;r, O result);

template &lt;InputIterator I, Sentinel&lt;I&gt; S, WeaklyIncrementable O,

          class Proj = ranges::identity,

          IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred&gt;
(3)(ranges TS)

    requires IndirectlyCopyable&lt;I, O&gt;

    ranges::tagged_pair&lt;tag::in(I), tag::out(O)&gt;

    copy_if(I first, S last, O result, Pred pred, Proj proj = Proj{});

template &lt;InputRange R, WeaklyIncrementable O,

          class Proj = ranges::identity,

          IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred&gt;
(4)(ranges TS)

    requires IndirectlyCopyable&lt;iterator_t&lt;R&gt;, O&gt;

    ranges::tagged_pair&lt;tag::in(ranges::safe_iterator_t&lt;R&gt;), tag::out(O)&gt;

    copy_if(R &amp;&amp;r, O result, Pred pred, Proj proj = Proj{});
Copies elements in the source range ([first,last) or r) into the destination range beginning at result, starting from the first element in the source range and proceeding to the last one.

1) Copies all elements in the range [first, last). For each non-negative integer n &lt; (last - first), performs *(result + n) = *(first + n). The behavior is undefined if result is within the range [first, last). In this case, ranges::copy_backward may be used instead.

2) Same as (1), but uses r as the source range, as if by ranges::copy(ranges::begin(r), ranges::end(r), result); except that result may not be copied.

3) Only copies the elements for which the predicate pred returns true when applied to the element's value as projected by the projection proj. The order of the elements that are copied is preserved. The behavior is undefined if the source and the destination ranges overlap.

4) Same as (3), but uses r as the source range, as if by ranges::copy_if(ranges::begin(r), ranges::end(r), result, pred, proj); except that result, pred and proj may not be copied.

Notwithstanding the declarations depicted above, the actual number and order of template parameters for algorithm declarations is unspecified. Thus, if explicit template arguments are used when calling an algorithm, the program is probably non-portable.
</code></pre>

<h2>Parameters</h2>

first, last - the range of elements to copy 
r - the range of elements to copy 
result - the beginning of the destination range 
pred - predicate to apply to the projected elements 
proj - projection to apply to the elements

<h2>Return value</h2>

A tagged_pair object containing the following two members: 
* The first member, with the tag tag::in, is the past-the-end iterator of the source range (that is, an iterator of type I that compares equal to the sentinel last). 
* The second member, with the tag tag::out, is the past-the-end iterator of the result range. 

<h2>Complexity</h2>

1) Exactly ranges::distance(first, last) assignments. 
2) Exactly ranges::distance(r) assignments. 
3) Exactly ranges::distance(first, last) applications of the corresponding projection and predicate. 
4) Exactly ranges::distance(r) applications of the corresponding projection and predicate.

<h2>Possible implementations</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template &lt;InputIterator I, Sentinel&lt;I&gt; S, WeaklyIncrementable O&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectlyCopyable&lt;I, O&gt;() 
&nbsp;<wbr>&nbsp;ranges::tagged_pair&lt;tag::in(I), tag::out(O)&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy(I first, S last, O result) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first, (void)++result) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*result = *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return {first, result}; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template &lt;InputRange R, WeaklyIncrementable O&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectlyCopyable&lt;ranges::iterator_t&lt;R&gt;, O&gt;() 
&nbsp;<wbr>&nbsp;ranges::tagged_pair&lt;tag::in(ranges::safe_iterator_t&lt;R&gt;), tag::out(O)&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy(R&amp;&amp; r, O result) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::copy(ranges::begin(r), ranges::end(r), result); 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template &lt;InputIterator I, Sentinel&lt;I&gt; S, WeaklyIncrementable O, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;I, Proj&gt;&gt; Pred&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectlyCopyable&lt;I, O&gt;() 
&nbsp;<wbr>&nbsp;ranges::tagged_pair&lt;tag::in(I), tag::out(O)&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy_if(I first, S last, O result, Pred pred, Proj proj = Proj{}) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (ranges::invoke(pred, ranges::invoke(proj, *first))){ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*result = *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++result; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return {first, result}; 
&nbsp;<wbr>&nbsp;} 

 
Fourth version 

 
&nbsp;<wbr>&nbsp;template &lt;InputRange R, WeaklyIncrementable O, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class Proj = ranges::identity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IndirectUnaryPredicate&lt;projected&lt;ranges::iterator_t&lt;R&gt;, Proj&gt;&gt; Pred&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires IndirectlyCopyable&lt;ranges::iterator_t&lt;R&gt;, O&gt;() 
&nbsp;<wbr>&nbsp;ranges::tagged_pair&lt;tag::in(ranges::safe_iterator_t&lt;R&gt;), tag::out(O)&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy_if(R&amp;&amp; r, O result, Pred pred, Proj proj = Proj{}) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ranges::copy_if(ranges::begin(r), ranges::end(r), result, pred, proj); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following code uses copy to both copy the contents of one vector to another and to display the resulting vector: 
 // Run this code <pre><code>#include &lt;experimental/ranges/algorithm&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;experimental/ranges/iterator&gt;

#include &lt;numeric&gt;
int main()

{
    // see http://en.cppreference.com/w/cpp/language/namespace_alias
    namespace ranges = std::experimental::ranges;
    std::vector&lt;int&gt; from_vector(10);
    std::iota(from_vector.begin(), from_vector.end(), 0);
    std::vector&lt;int&gt; to_vector;
    ranges::copy_if(from_vector.begin(), from_vector.end(),
                    ranges::back_inserter(to_vector),
                    [](const auto i) {
                        return i % 3;
                    });

    // or, alternatively,

    //  std::vector&lt;int&gt; to_vector(from_vector.size());

    //  std::copy(from_vector, to_vector.begin());
    std::cout &lt;&lt; &quot;to_vector contains: &quot;;
    ranges::copy(to_vector, ranges::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;to_vector contains: 1 2 4 5 7 8

<h2>See also</h2>

copy 
copy_if copies a range of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of elements in backwards order 
copy_backward <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a copy of a range that is reversed 
reverse_copy <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a number of elements to a new location 
copy_n <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns a range of elements a certain value 
fill <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of elements omitting those that satisfy specific criteria 
remove_copy <i>(function template)</i> 
remove_copy_if 
