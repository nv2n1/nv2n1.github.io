---
title: "stdatomic_compare_exchange_weakstdatomic_compare_exchange_strongstdatomic_compare_exchange_weak_explicitstdatomic_compare_exchange_strong_explicit(3)"
name: "stdatomic_compare_exchange_weakstdatomic_compare_exchange_strongstdatomic_compare_exchange_weak_explicitstdatomic_compare_exchange_strong_explicit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_compare_exchange_weakstdatomic_compare_exchange_strongstdatomic_compare_exchange_weak_explicitstdatomic_compare_exchange_strong_explicit/"
description: "std::atomic_compare_exchange_weak,std::atomic_compare_exchange_strong,std::atomic_compare_exchange_weak_explicit,std::atomic_compare_exchange_strong_explicit – std::atomic_compare_exchange_weak,std..."
---

<p>std::atomic_compare_exchange_weak,std::atomic_compare_exchange_strong,std::atomic_compare_exchange_weak_explicit,std::atomic_compare_exchange_strong_explicit &#8211; std::atomic_compare_exchange_weak,std::atomic_compare_exchange_strong,std::atomic_compare_exchange_weak_explicit,std::atomic_compare_exchange_strong_explicit</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;atomic&gt;

template&lt; class T &gt;

bool atomic_compare_exchange_weak( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type* expected,

typename std::atomic&lt;T&gt;::value_type desired ) noexcept;

template&lt; class T &gt;

bool atomic_compare_exchange_weak( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type* expected,

typename std::atomic&lt;T&gt;::value_type desired ) noexcept;

template&lt; class T &gt;

bool atomic_compare_exchange_strong( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type* expected,

typename std::atomic&lt;T&gt;::value_type desired ) noexcept;

template&lt; class T &gt;

bool atomic_compare_exchange_strong( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type* expected,

typename std::atomic&lt;T&gt;::value_type desired ) noexcept;

template&lt; class T &gt;

bool atomic_compare_exchange_weak_explicit( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type* expected,

typename std::atomic&lt;T&gt;::value_type desired,                                 (1) (since C++11)

std::memory_order succ,

std::memory_order fail ) noexcept;

template&lt; class T &gt;

bool atomic_compare_exchange_weak_explicit( volatile std::atomic&lt;T&gt;* obj,                      (2) (since C++11)

typename std::atomic&lt;T&gt;::value_type* expected,

typename std::atomic&lt;T&gt;::value_type desired,

std::memory_order succ,

std::memory_order fail ) noexcept;                                                                               (3) (since C++11)

template&lt; class T &gt;

bool atomic_compare_exchange_strong_explicit( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type* expected,

typename std::atomic&lt;T&gt;::value_type desired,

std::memory_order succ,

std::memory_order fail ) noexcept;                                                                                                 (4) (since C++11)

template&lt; class T &gt;

bool atomic_compare_exchange_strong_explicit( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type* expected,

typename std::atomic&lt;T&gt;::value_type desired,

std::memory_order succ,

std::memory_order fail ) noexcept;</code></pre>
<p>Atomically compares the<br />
object_representation<br />
<i>(until C++20)</i><br />
value_representation<br />
<i>(since C++20)</i> of the object pointed to by obj with that of the object pointed to by expected, and if those are bitwise-equal, replaces the former with desired (performs read-modify-write operation). Otherwise, loads the actual value pointed to by obj into *expected (performs load operation). Copying is performed as if by std::memcpy.<br />
The memory models for the read-modify-write and load operations are succ and fail respectively. The (1-2) versions use std::memory_order_seq_cst by default.<br />
These functions are defined in terms of member functions of std::atomic:<br />
1) obj-&gt;compare_exchange_weak(*expected, desired)<br />
2) obj-&gt;compare_exchange_strong(*expected, desired)<br />
3) obj-&gt;compare_exchange_weak(*expected, desired, succ, fail)<br />
4) obj-&gt;compare_exchange_strong(*expected, desired, succ, fail) </p>
<h2>Parameters</h2>
<p>obj &#8211; pointer to the atomic object to test and modify<br />
expected &#8211; pointer to the value expected to be found in the atomic object<br />
desired &#8211; the value to store in the atomic object if it is as expected<br />
succ &#8211; the memory synchronization ordering for the read-modify-write operation if the comparison succeeds. All values are permitted.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the memory synchronization ordering for the load operation if the comparison fails. Cannot be std::memory_order_release or std::memory_order_acq_rel<br />
fail &#8211; and cannot specify stronger ordering than succ<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++17)</i></p>
<h2>Return value</h2>
<p>The result of the comparison: true if *obj was equal to *expected, false otherwise. </p>
<h2>Notes</h2>
<p>The weak forms (<code>(1)</code> and <code>(3)</code>) of the functions are allowed to fail spuriously, that is, act as if *obj != *expected even if they are equal. When a compare-and-exchange is in a loop, the weak version will yield better performance on some platforms.<br />
When a weak compare-and-exchange would require a loop and a strong one would not, the strong one is preferable unless the object representation of T may include<br />
padding bits,<br />
<i>(until C++20)</i> trap bits, or offers multiple object representations for the same value (e.g. floating-point NaN). In those cases, weak compare-and-exchange typically works because it quickly converges on some stable object representation.<br />
For a union with bits that participate in the value representations of some members but not the others, compare-and-exchange might always fail because such padding bits have indeterminate values when they do not participate in the value representation of the active member.<br />
Padding bits that never participate in an object&#8217;s value representation are ignored. <i>(since C++20)</i> </p>
<h2>Example</h2>
<p>compare and exchange operations are often used as basic building blocks of lockfree data structures<br />
 // Run this code </p>
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
}
</code></pre>
<p>Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
P0558R1 C++11 exact type match required because T is deduced from multiple arguments T is deduced from the atomic argument only </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically compares the value of the atomic object with non-atomic argument and performs atomic exchange if equal or atomic load if not<br />
compare_exchange_weak <i>(public member function of std::atomic&lt;T&gt;)</i><br />
compare_exchange_strong<br />
atomic_exchange<br />
atomic_exchange_explicit atomically replaces the value of the atomic object with non-atomic argument and returns the old value of the atomic<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes atomic operations for std::shared_ptr<br />
std::atomic_compare_exchange_weak(std::shared_ptr)_ <i>(function template)</i><br />
std::atomic_compare_exchange_strong(std::shared_ptr) </p>
