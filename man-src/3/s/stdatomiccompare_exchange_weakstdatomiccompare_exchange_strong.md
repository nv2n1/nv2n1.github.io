---
title: "stdatomiccompare_exchange_weakstdatomiccompare_exchange_strong(3)"
name: "stdatomiccompare_exchange_weakstdatomiccompare_exchange_strong"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomiccompare_exchange_weakstdatomiccompare_exchange_strong/"
description: "std::atomic<T>::compare_exchange_weak,std::atomic<T>::compare_exchange_strong – std::atomic<T>::compare_exchange_weak,std::atomic<T>::compare_exchange_strong"
---

<p>std::atomic&lt;T&gt;::compare_exchange_weak,std::atomic&lt;T&gt;::compare_exchange_strong &#8211; std::atomic&lt;T&gt;::compare_exchange_weak,std::atomic&lt;T&gt;::compare_exchange_strong</p>
<h2>Synopsis</h2>
<pre><code>bool compare_exchange_weak( T&amp; expected, T desired,

std::memory_order success,

std::memory_order failure ) noexcept;

bool compare_exchange_weak( T&amp; expected, T desired,

std::memory_order success,

std::memory_order failure ) volatile noexcept;

bool compare_exchange_weak( T&amp; expected, T desired,

std::memory_order order =

std::memory_order_seq_cst ) noexcept;

bool compare_exchange_weak( T&amp; expected, T desired,

std::memory_order order =

std::memory_order_seq_cst ) volatile noexcept;        (1) (since C++11)

bool compare_exchange_strong( T&amp; expected, T desired,

std::memory_order success,

std::memory_order failure ) noexcept;                                   (2) (since C++11)

bool compare_exchange_strong( T&amp; expected, T desired,

std::memory_order success,

std::memory_order failure ) volatile noexcept;                                            (3) (since C++11)

bool compare_exchange_strong( T&amp; expected, T desired,

std::memory_order order =

std::memory_order_seq_cst ) noexcept;                                                                       (4) (since C++11)

bool compare_exchange_strong( T&amp; expected, T desired,

std::memory_order order =

std::memory_order_seq_cst ) volatile noexcept;</code></pre>
<p>Atomically compares the<br />
object_representation<br />
<i>(until C++20)</i><br />
value_representation<br />
<i>(since C++20)</i> of *this with that of expected, and if those are bitwise-equal, replaces the former with desired (performs read-modify-write operation). Otherwise, loads the actual value stored in *this into expected (performs load operation).<br />
The memory models for the read-modify-write and load operations are success and failure respectively. In the <code>(2)</code> and <code>(4)</code> versions order is used for both read-modify-write and load operations, except that std::memory_order_acquire and std::memory_order_relaxed are used for the load operation if order == std::memory_order_acq_rel, or order == std::memory_order_release respectively. </p>
<h2>Parameters</h2>
<p>expected &#8211; reference to the value expected to be found in the atomic object<br />
desired &#8211; the value to store in the atomic object if it is as expected<br />
success &#8211; the memory synchronization ordering for the read-modify-write operation if the comparison succeeds. All values are permitted.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the memory synchronization ordering for the load operation if the comparison fails. Cannot be std::memory_order_release or std::memory_order_acq_rel<br />
failure &#8211; and cannot specify stronger ordering than success<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++17)</i><br />
order &#8211; the memory synchronization ordering for both operations</p>
<h2>Return value</h2>
<p>true if the underlying atomic value was successfully changed, false otherwise. </p>
<h2>Notes</h2>
<p>The comparison and copying are bitwise (similar to std::memcmp and std::memcpy); no constructor, assignment operator, or comparison operator are used.<br />
The weak forms (1-2) of the functions are allowed to fail spuriously, that is, act as if *this != expected even if they are equal. When a compare-and-exchange is in a loop, the weak version will yield better performance on some platforms.<br />
When a weak compare-and-exchange would require a loop and a strong one would not, the strong one is preferable unless the object representation of T may include<br />
padding bits,<br />
<i>(until C++20)</i> trap bits, or offers multiple object representations for the same value (e.g. floating-point NaN). In those cases, weak compare-and-exchange typically works because it quickly converges on some stable object representation.<br />
For a union with bits that participate in the value representations of some members but not the others, compare-and-exchange might always fail because such padding bits have indeterminate values when they do not participate in the value representation of the active member.<br />
Padding bits that never participate in an object&#8217;s value representation are ignored. <i>(since C++20)</i> </p>
<h2>Example</h2>
<p>Compare-and-exchange operations are often used as basic building blocks of lockfree data structures<br />
 // Run this code #include &lt;atomic&gt;</p>
<p>template &lt;typename T&gt;</p>
<p>struct node</p>
<p>{<br />
    T data;<br />
    node *next;<br />
    node(const T &amp;data)<br />
        : data(data), next(nullptr)<br />
    {<br />
    }<br />
};<br />
template &lt;typename T&gt;</p>
<p>class stack</p>
<p>{<br />
    std::atomic&lt;node&lt;T&gt; *&gt; head;</p>
<p>  public:<br />
    void push(const T &amp;data)<br />
    {<br />
        node&lt;T&gt; *new_node = new node&lt;T&gt;(data);<br />
        // put the current value of head into new_node-&gt;next<br />
        new_node-&gt;next = head.load(std::memory_order_relaxed);<br />
        // now make new_node the new head, but if the head<br />
        // is no longer what&#8217;s stored in new_node-&gt;next<br />
        // (some other thread must have inserted a node just now)<br />
        // then put that new head into new_node-&gt;next and try again<br />
        while (!head.compare_exchange_weak(new_node-&gt;next, new_node,<br />
                                           std::memory_order_release,<br />
                                           std::memory_order_relaxed))<br />
            ; // the body of the loop is empty<br />
              // Note: the above use is not thread-safe in at least</p>
<p>        // GCC prior to 4.8.3 (bug 60272), clang prior to 2014-05-05 (bug 18899)</p>
<p>        // MSVC prior to 2014-03-17 (bug 819819). The following is a workaround:</p>
<p>        //      node&lt;T&gt;* old_head = head.load(std::memory_order_relaxed);</p>
<p>        //      do {</p>
<p>        //          new_node-&gt;next = old_head;</p>
<p>        //       } while(!head.compare_exchange_weak(old_head, new_node,</p>
<p>        //                                           std::memory_order_release,</p>
<p>        //                                           std::memory_order_relaxed));<br />
    }<br />
};</p>
<p>int main()</p>
<p>{<br />
    stack&lt;int&gt; s;<br />
    s.push(1);<br />
    s.push(2);<br />
    s.push(3);<br />
}</p>
<p>Demonstrates how compare_exchange_strong either changes the value of the atomic variable or the variable used for comparison.<br />
&nbsp;This section is incomplete<br />
&nbsp;Reason: more practical use of the strong CAS would be nice, such as where Concurrency in Action uses it<br />
 // Run this code </p>
<pre><code>#include &lt;atomic&gt;

#include &lt;iostream&gt;
std::atomic&lt;int&gt; ai;
int tst_val = 4;

int new_val = 5;

bool exchanged = false;
void valsout()

{
    std::cout &lt;&lt; &quot;ai= &quot; &lt;&lt; ai

              &lt;&lt; &quot;  tst_val= &quot; &lt;&lt; tst_val

              &lt;&lt; &quot;  new_val= &quot; &lt;&lt; new_val

              &lt;&lt; &quot;  exchanged= &quot; &lt;&lt; std::boolalpha &lt;&lt; exchanged

              &lt;&lt; &quot;
&quot;;
}
int main()

{
    ai = 3;
    valsout();
    // tst_val != ai   ==&gt;  tst_val is modified
    exchanged = ai.compare_exchange_strong(tst_val, new_val);
    valsout();
    // tst_val == ai   ==&gt;  ai is modified
    exchanged = ai.compare_exchange_strong(tst_val, new_val);
    valsout();
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;ai= 3 tst_val= 4 new_val= 5 exchanged= false<br />
&nbsp;<wbr>&nbsp;ai= 3 tst_val= 3 new_val= 5 exchanged= false<br />
&nbsp;<wbr>&nbsp;ai= 5 tst_val= 3 new_val= 5 exchanged= true</p>
<h2>See also</h2>
<p>atomic_compare_exchange_weak<br />
atomic_compare_exchange_weak_explicit<br />
atomic_compare_exchange_strong<br />
atomic_compare_exchange_strong_explicit atomically compares the value of the atomic object with non-atomic argument and performs atomic exchange if equal or atomic load if not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
