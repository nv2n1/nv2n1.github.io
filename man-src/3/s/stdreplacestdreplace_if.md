---
title: "stdreplacestdreplace_if(3)"
name: "stdreplacestdreplace_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreplacestdreplace_if/"
---

std::replace,std::replace_if - std::replace,std::replace_if

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class ForwardIt, class T&gt;

    void replace(ForwardIt first, ForwardIt last, (until C++ 20)

                                                      const T &amp;old_value,
                 const T &amp;new_value);

template &lt;class ForwardIt, class T&gt;

constexpr void replace(ForwardIt first, ForwardIt last, (since C++ 20)

                                                            const T &amp;old_value,
                       const T &amp;new_value);

template &lt;class ExecutionPolicy, class ForwardIt, class T&gt;

void replace(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, (2)(since C++ 17)

                                                                            const T &amp;old_value,
             const T &amp;new_value);
(1)

    template &lt;class ForwardIt, class UnaryPredicate, class T&gt;

    void replace_if(ForwardIt first, ForwardIt last, (until C++ 20)

                                                         UnaryPredicate p,
                    const T &amp;new_value);

template &lt;class ForwardIt, class UnaryPredicate, class T&gt;

constexpr void replace_if(ForwardIt first, ForwardIt last, (3)(since C++ 20)

                                                               UnaryPredicate p,
                          const T &amp;new_value);

template &lt;class ExecutionPolicy, class ForwardIt, class UnaryPredicate, class T&gt;

void replace_if(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, (4)(since C++ 17)

                                                                               UnaryPredicate p,
                const T &amp;new_value);</code></pre> 
Replaces all elements satisfying specific criteria with new_value in the range [first, last). 
1) Replaces all elements that are equal to old_value. 
3) Replaces all elements for which predicate p returns true. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to process 
old_value - the value of elements to replace 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true if the element value should be replaced. 
p - The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of ForwardIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>. 
new_value - the value to use as replacement

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
UnaryPredicate must meet the requirements of Predicate.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Exactly last - first applications of the predicate.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

Because the algorithm takes old_value and new_value by reference, it can have unexpected behavior if either is a reference to an element of the range [first, last). 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class T&gt; 
&nbsp;<wbr>&nbsp;void replace(ForwardIt first, ForwardIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const T&amp; old_value, const T&amp; new_value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (*first == old_value) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*first = new_value; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class UnaryPredicate, class T&gt; 
&nbsp;<wbr>&nbsp;void replace_if(ForwardIt first, ForwardIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UnaryPredicate p, const T&amp; new_value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if(p(*first)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*first = new_value; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following code at first replaces all occurrences of 8 with 88 in a vector of integers. Then it replaces all values less than 5 with 55. 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;array&gt;

#include &lt;iostream&gt;

#include &lt;functional&gt;
int main()

{
    std::array&lt;int, 10&gt; s{5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    std::replace(s.begin(), s.end(), 8, 88);
    for (int a : s) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
    std::replace_if(s.begin(), s.end(),
                    std::bind(std::less&lt;int&gt;(), std::placeholders::_1, 5), 55);
    for (int a : s) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;5 7 4 2 88 6 1 9 0 3 
&nbsp;<wbr>&nbsp;5 7 55 55 88 6 55 9 55 55

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range, replacing elements satisfying specific criteria with another value 
replace_copy <i>(function template)</i> 
replace_copy_if 
