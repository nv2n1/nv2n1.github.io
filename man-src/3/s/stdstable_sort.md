---
title: "stdstable_sort(3)"
name: "stdstable_sort"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstable_sort/"
---

std::stable_sort - std::stable_sort

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class RandomIt&gt;
    (1)

        void stable_sort(RandomIt first, RandomIt last);

template &lt;class ExecutionPolicy, class RandomIt&gt;
(2)(since C++ 17)

    void stable_sort(ExecutionPolicy &amp;&amp;policy, RandomIt first, RandomIt last);

template &lt;class RandomIt, class Compare&gt;
(3)

    void stable_sort(RandomIt first, RandomIt last, Compare comp);

template &lt;class ExecutionPolicy, class RandomIt, class Compare&gt;
(4)(since C++ 17)

    void stable_sort(ExecutionPolicy &amp;&amp;policy, RandomIt first, RandomIt last, Compare comp);</code></pre> 
Sorts the elements in the range [first, last) in ascending order. The order of equivalent elements is guaranteed to be preserved. 
1) Elements are compared using operator&lt;. 
3) Elements are compared using the given comparison function comp. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to sort 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type RandomIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
RandomIt must meet the requirements of ValueSwappable and LegacyRandomAccessIterator. 
- 
The type of dereferenced RandomIt must meet the requirements of MoveAssignable and MoveConstructible.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

O(N·log(N)2), where N = std::distance(first, last) applications of cmp. If additional memory is available, then the complexity is O(N·log(N)).

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

This function attempts to allocate a temporary buffer equal in size to the sequence to be sorted. If the allocation fails, the less efficient algorithm is chosen. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;vector&gt;
struct Employee

{
    int age;
    std::string name; // Does not participate in comparisons
};
bool operator&lt;(const Employee &amp;lhs, const Employee &amp;rhs)

{
    return lhs.age &lt; rhs.age;
}
int main()

{
    std::vector&lt;Employee&gt; v =
        {
            {108, &quot;Zaphod&quot;},
            {32, &quot;Arthur&quot;},
            {108, &quot;Ford&quot;},
        };
    std::stable_sort(v.begin(), v.end());
    for (const Employee &amp;e : v)
        std::cout &lt;&lt; e.age &lt;&lt; &quot;, &quot; &lt;&lt; e.name &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;32, Arthur 
&nbsp;<wbr>&nbsp;108, Zaphod 
&nbsp;<wbr>&nbsp;108, Ford

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts the first N elements of a range 
partial_sort <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range into ascending order 
sort <i>(function template)</i> 
