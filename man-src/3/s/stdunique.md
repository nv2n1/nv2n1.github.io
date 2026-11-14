---
title: "stdunique(3)"
name: "stdunique"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique/"
---

std::unique - std::unique

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt &gt;                                                                               (until C++20)

ForwardIt unique( ForwardIt first, ForwardIt last );

template&lt; class ForwardIt &gt;                                                                               (since C++20)

constexpr ForwardIt unique( ForwardIt first, ForwardIt last );

template&lt; class ExecutionPolicy, class ForwardIt &gt;                                                    (2) (since C++17)

ForwardIt unique( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last );                    (1)

template&lt; class ForwardIt, class BinaryPredicate &gt;                                                                      (until C++20)

ForwardIt unique( ForwardIt first, ForwardIt last, BinaryPredicate p );

template&lt; class ForwardIt, class BinaryPredicate &gt;                                                    (3)               (since C++20)

constexpr ForwardIt unique( ForwardIt first, ForwardIt last, BinaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt, class BinaryPredicate &gt;                                 (4)           (since C++17)

ForwardIt unique( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last, BinaryPredicate p );</code></pre> 
Eliminates all but the first element from every consecutive group of equivalent elements from the range [first, last) and returns a past-the-end iterator for the new logical end of the range. 
Removing is done by shifting the elements in the range in such a way that elements to be erased are overwritten. Relative order of the elements that remain is preserved and the physical size of the container is unchanged. Iterators pointing to an element between the new logical end and the physical end of the range are still dereferenceable, but the elements themselves have unspecified values. A call to unique is typically followed by a call to a container's erase method, which erases the unspecified values and reduces the physical size of the container to match its new logical size. 
1) Elements are compared using operator==. The behavior is undefined if it is not an equivalence_relation. 
3) Elements are compared using the given binary predicate p. The behavior is undefined if it is not an equivalence relation. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true. 

<h2>Parameters</h2>

first, last - the range of elements to process 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the elements should be treated as equal. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type1 &amp;a, const Type2 &amp;b); 
p - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type ForwardIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
The type of dereferenced ForwardIt must meet the requirements of MoveAssignable.

<h2>Return value</h2>

Forward iterator to the new end of the range 

<h2>Complexity</h2>

For nonempty ranges, exactly std::distance(first,last) -1 applications of the corresponding predicate.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt&gt; 
&nbsp;<wbr>&nbsp;ForwardIt unique(ForwardIt first, ForwardIt last) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt result = first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (++first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!(*result == *first) &amp;&amp; ++result != first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*result = std::move(*first); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ++result; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class BinaryPredicate&gt; 
&nbsp;<wbr>&nbsp;ForwardIt unique(ForwardIt first, ForwardIt last, BinaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt result = first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (++first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!p(*result, *first) &amp;&amp; ++result != first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*result = std::move(*first); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ++result; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;string&gt;

#include &lt;cctype&gt;
int main()

{
    // remove duplicate elements
    std::vector&lt;int&gt; v{1, 2, 3, 1, 2, 3, 3, 4, 5, 4, 5, 6, 7};
    std::sort(v.begin(), v.end()); // 1 1 2 2 3 3 3 4 4 5 5 6 7
    auto last = std::unique(v.begin(), v.end());
    // v now holds {1 2 3 4 5 6 7 x x x x x x}, where 'x' is indeterminate
    v.erase(last, v.end());
    for (int i : v)
        std::cout &lt;&lt; i &lt;&lt; &quot; &quot;;
    std::cout &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 3 4 5 6 7

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first two adjacent items that are equal (or satisfy a given predicate) 
adjacent_find <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a copy of some range of elements that contains no consecutive duplicates 
unique_copy <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes consecutive duplicate elements 
unique <i>(public member function of std::list&lt;T,Allocator&gt;)</i> 
