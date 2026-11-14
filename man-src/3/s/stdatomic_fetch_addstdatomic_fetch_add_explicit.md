---
title: "stdatomic_fetch_addstdatomic_fetch_add_explicit(3)"
name: "stdatomic_fetch_addstdatomic_fetch_add_explicit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_fetch_addstdatomic_fetch_add_explicit/"
---

std::atomic_fetch_add,std::atomic_fetch_add_explicit - std::atomic_fetch_add,std::atomic_fetch_add_explicit

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;atomic&gt;

template&lt; class T &gt;

T atomic_fetch_add( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::difference_type arg ) noexcept;

template&lt; class T &gt;

T atomic_fetch_add( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::difference_type arg ) noexcept;

template&lt; class T &gt;                                        (1)

T atomic_fetch_add_explicit( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::difference_type arg,

std::memory_order order ) noexcept;                            (2)

template&lt; class T &gt;

T atomic_fetch_add_explicit( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::difference_type arg,

std::memory_order order ) noexcept;</code></pre> 
Performs atomic addition. Atomically adds arg to the value pointed to by obj and returns the value obj held previously. The operation is performed as if the following was executed: 
1) obj-&gt;fetch_add(arg) 
2) obj-&gt;fetch_add(arg, order) 

<h2>Parameters</h2>

obj - pointer to the atomic object to modify 
arg - the value to add to the value stored in the atomic object 
order - the memory synchronization ordering for this operation: all values are permitted.

<h2>Return value</h2>

The value immediately preceding the effects of this function in the modification_order of *obj. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;T atomic_fetch_add( std::atomic&lt;T&gt;* obj, typename std::atomic&lt;T&gt;::difference_type arg ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return obj-&gt;fetch_add(arg); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Single-writer/multiple-reader lock can be made with fetch_add. Note that this simplistic implementation is not lockout-free 
 // Run this code <pre><code>#include &lt;string&gt;

#include &lt;thread&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;atomic&gt;

#include &lt;chrono&gt;
// meaning of cnt:

// 5: there are no active readers or writers.

// 1...4: there are 4...1 readers active, The writer is blocked

// 0: temporary value between fetch_sub and fetch_add in reader lock

// -1: there is a writer active. The readers are blocked.

const int N = 5; // four concurrent readers are allowed

std::atomic&lt;int&gt; cnt(N);
std::vector&lt;int&gt; data;
void reader(int id)

{
    for (;;) {
        // lock
        while (std::atomic_fetch_sub(&amp;cnt, 1) &lt;= 0)
            std::atomic_fetch_add(&amp;cnt, 1);
        // read
        if (!data.empty())
            std::cout &lt;&lt; (&quot;reader &quot; + std::to_string(id) + &quot; sees &quot; + std::to_string(*data.rbegin()) + '\n');
        if (data.size() == 25)
            break;
        // unlock
        std::atomic_fetch_add(&amp;cnt, 1);
        // pause
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
}
void writer()

{
    for (int n = 0; n &lt; 25; ++n) {
        // lock
        while (std::atomic_fetch_sub(&amp;cnt, N + 1) != N)
            std::atomic_fetch_add(&amp;cnt, N + 1);
        // write
        data.push_back(n);
        std::cout &lt;&lt; &quot;writer pushed back &quot; &lt;&lt; n &lt;&lt; '\n';
        // unlock
        std::atomic_fetch_add(&amp;cnt, N + 1);
        // pause
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
}
int main()

{
    std::vector&lt;std::thread&gt; v;
    for (int n = 0; n &lt; N; ++n) {
        v.emplace_back(reader, n);
    }
    v.emplace_back(writer);
    for (auto &amp;t : v) {
        t.join();
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;writer pushed back 0 
&nbsp;<wbr>&nbsp;reader 2 sees 0 
&nbsp;<wbr>&nbsp;reader 3 sees 0 
&nbsp;<wbr>&nbsp;reader 1 sees 0 
&nbsp;<wbr>&nbsp;&lt;...&gt; 
&nbsp;<wbr>&nbsp;reader 2 sees 24 
&nbsp;<wbr>&nbsp;reader 4 sees 24 
&nbsp;<wbr>&nbsp;reader 1 sees 24 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 exact type match required because T is deduced from multiple arguments T is deduced from the atomic argument only

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically adds the argument to the value stored in the atomic object and obtains the value held previously 
fetch_add <i>(public member function of std::atomic&lt;T&gt;)</i> 
atomic_fetch_sub 
atomic_fetch_sub_explicit subtracts a non-atomic value from an atomic object and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
