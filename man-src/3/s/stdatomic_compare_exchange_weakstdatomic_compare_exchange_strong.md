---
title: "stdatomic_compare_exchange_weakstdatomic_compare_exchange_strong(3)"
name: "stdatomic_compare_exchange_weakstdatomic_compare_exchange_strong"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_compare_exchange_weakstdatomic_compare_exchange_strong/"
description: "std::atomic_compare_exchange_weak,std::atomic_compare_exchange_strong, – std::atomic_compare_exchange_weak,std::atomic_compare_exchange_strong,"
---

<p>std::atomic_compare_exchange_weak,std::atomic_compare_exchange_strong, &#8211; std::atomic_compare_exchange_weak,std::atomic_compare_exchange_strong,</p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Defined in header&nbsp;<wbr>&lt;atomic&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>template&lt;&nbsp;<wbr>class T&nbsp;<wbr>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bool atomic_compare_exchange_weak(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::atomic&lt;T&gt;*&nbsp;<wbr>obj,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired&nbsp;<wbr>)&nbsp;<wbr>noexcept;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>template&lt;&nbsp;<wbr>class T&nbsp;<wbr>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bool atomic_compare_exchange_weak(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>volatile std::atomic&lt;T&gt;*&nbsp;<wbr>obj,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired&nbsp;<wbr>)&nbsp;<wbr>noexcept;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>template&lt;&nbsp;<wbr>class T&nbsp;<wbr>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bool atomic_compare_exchange_strong(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::atomic&lt;T&gt;*&nbsp;<wbr>obj,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired&nbsp;<wbr>)&nbsp;<wbr>noexcept;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>template&lt;&nbsp;<wbr>class T&nbsp;<wbr>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bool atomic_compare_exchange_strong(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>volatile std::atomic&lt;T&gt;*&nbsp;<wbr>obj,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired&nbsp;<wbr>)&nbsp;<wbr>noexcept;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>template&lt;&nbsp;<wbr>class T&nbsp;<wbr>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bool<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomic_compare_exchange_weak_explicit(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::atomic&lt;T&gt;*&nbsp;<wbr>obj,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(1)</code>&nbsp;<wbr>(since<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C++11)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::memory_order succ,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::memory_order fail&nbsp;<wbr>)&nbsp;<wbr>noexcept;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>template&lt;&nbsp;<wbr>class T&nbsp;<wbr>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bool&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr>(since<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomic_compare_exchange_weak_explicit(&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C++11)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>volatile std::atomic&lt;T&gt;*&nbsp;<wbr>obj,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::memory_order succ,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::memory_order fail&nbsp;<wbr>)&nbsp;<wbr>noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(3)</code>&nbsp;<wbr>(since<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>template&lt;&nbsp;<wbr>class T&nbsp;<wbr>&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C++11)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bool<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomic_compare_exchange_strong_explicit(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::atomic&lt;T&gt;*&nbsp;<wbr>obj,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::memory_order succ,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::memory_order fail&nbsp;<wbr>)&nbsp;<wbr>noexcept;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(4)</code>&nbsp;<wbr>(since<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>template&lt;&nbsp;<wbr>class T&nbsp;<wbr>&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C++11)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bool<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomic_compare_exchange_strong_explicit(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>volatile std::atomic&lt;T&gt;*&nbsp;<wbr>obj,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::atomic&lt;T&gt;::value_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::memory_order succ, </p>
<pre><code>std::memory_order fail ) noexcept;</code></pre>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Atomically compares the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>object representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(until C++20)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>value representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(since C++20)</i>&nbsp;<wbr>of the object pointed to by obj with that of the object pointed to by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected, and if those are bitwise-equal, replaces the former with desired&nbsp;<wbr>(performs<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>read-modify-write operation). Otherwise, loads the actual value pointed to by obj<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>into&nbsp;<wbr>*expected&nbsp;<wbr>(performs load operation). Copying is performed as if by std::memcpy.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The memory models for the read-modify-write and load operations are succ and fail<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>respectively. The&nbsp;<wbr>(1-2)&nbsp;<wbr>versions use std::memory_order_seq_cst by default.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>These functions are defined in terms of member functions of std::atomic:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1)&nbsp;<wbr>obj-&gt;compare_exchange_weak(*expected, desired)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2)&nbsp;<wbr>obj-&gt;compare_exchange_strong(*expected, desired)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3)&nbsp;<wbr>obj-&gt;compare_exchange_weak(*expected, desired, succ, fail)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4)&nbsp;<wbr>obj-&gt;compare_exchange_strong(*expected, desired, succ, fail) </p>
<h2>Parameters</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>obj&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; pointer to the atomic object to test and modify<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expected &#8211; pointer to the value expected to be found in the atomic object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>desired&nbsp;<wbr>&nbsp;<wbr>&#8211; the value to store in the atomic object if it is as expected<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>succ&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the memory synchronization ordering for the read-modify-write operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if the comparison succeeds. All values are permitted.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the memory synchronization ordering for the load operation if the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>comparison fails. Cannot be std::memory_order_release or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fail&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; std::memory_order_acq_rel<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and cannot specify stronger ordering than succ<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(until C++17)</i></p>
<h2>Return value</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The result of the comparison: true if&nbsp;<wbr>*obj was equal to&nbsp;<wbr>*expected, false otherwise. </p>
<h2>Notes</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The weak forms&nbsp;<wbr>(<code>(1)</code>&nbsp;<wbr>and&nbsp;<wbr><code>(3)</code>)&nbsp;<wbr>of the functions are allowed to fail spuriously, that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is, act as if&nbsp;<wbr>*obj&nbsp;<wbr>!=&nbsp;<wbr>*expected even if they are equal. When a compare-and-exchange<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is in a loop, the weak version will yield better performance on some platforms.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>When a weak compare-and-exchange would require a loop and a strong one would not,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the strong one is preferable unless the object representation of T may include<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>padding bits,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(until C++20)</i>&nbsp;<wbr>trap bits, or offers multiple object representations for the same<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>value&nbsp;<wbr>(e.g. floating-point NaN). In those cases, weak compare-and-exchange typically<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>works because it quickly converges on some stable object representation.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>For a union with bits that participate in the value representations of some members<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>but not the others, compare-and-exchange might always fail because such padding bits<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>have indeterminate values when they do not participate in the value representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the active member.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Padding bits that never participate in an object&#8217;s value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(since C++20)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>representation are ignored. </p>
<h2>Example</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compare and exchange operations are often used as basic building blocks of lockfree<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data structures<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> // Run this code </p>
<pre><code>#include &lt;atomic&gt;
template &lt;class T&gt;

struct node

{
    T data;
    node *next;
    node(const T &amp;data)
        : data(data), next(nullptr)
    {
    }
};
template &lt;class T&gt;

class stack

{
    std::atomic&lt;node&lt;T&gt; *&gt; head;

  public:
    void push(const T &amp;data)
    {
        node&lt;T&gt; *new_node = new node&lt;T&gt;(data);
        // put the current value of head into new_node-&gt;next
        new_node-&gt;next = head.load(std::memory_order_relaxed);
        // now make new_node the new head, but if the head
        // is no longer what's stored in new_node-&gt;next
        // (some other thread must have inserted a node just now)
        // then put that new head into new_node-&gt;next and try again
        while (!std::atomic_compare_exchange_weak_explicit(
            &amp;head,
            &amp;new_node-&gt;next,
            new_node,
            std::memory_order_release,
            std::memory_order_relaxed))
            ; // the body of the loop is empty

        // note: the above loop is not thread-safe in at least

        // GCC prior to 4.8.3 (bug 60272), clang prior to 2014-05-05 (bug 18899)

        // MSVC prior to 2014-03-17 (bug 819819). See member function version for workaround
    }
};
int main()

{
    stack&lt;int&gt; s;
    s.push(1);
    s.push(2);
    s.push(3);
}</code></pre>
<p>&nbsp;<wbr>&nbsp;<wbr>Defect reports<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The following behavior-changing defect reports were applied retroactively to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>previously published C++&nbsp;<wbr>standards.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Applied to&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Behavior as published&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Correct behavior<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>P0558R1 C++11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exact type match required because T is&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>T is deduced from the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>deduced from multiple arguments&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomic argument only </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomically compares the value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the atomic object with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compare_exchange_weak&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>non-atomic argument and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compare_exchange_strong&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>performs atomic exchange if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>equal or atomic load if not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member</i>&nbsp;<wbr>function of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::atomic&lt;T&gt;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomic_exchange&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomically replaces the value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>atomic_exchange_explicit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the atomic object with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>non-atomic argument and returns<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the old value of the atomic<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::atomic_compare_exchange_weak(std::shared_ptr)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specializes atomic operations<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::atomic_compare_exchange_strong(std::shared_ptr)&nbsp;<wbr>for std::shared_ptr<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i> </p>
