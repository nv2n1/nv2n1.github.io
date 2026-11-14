---
title: "stdatomic_fetch_substdatomic_fetch_sub_explicit(3)"
name: "stdatomic_fetch_substdatomic_fetch_sub_explicit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_fetch_substdatomic_fetch_sub_explicit/"
---

std::atomic_fetch_sub,std::atomic_fetch_sub_explicit - std::atomic_fetch_sub,std::atomic_fetch_sub_explicit

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;atomic&gt;

template&lt; class T &gt;

T atomic_fetch_sub( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::difference_type arg ) noexcept;

template&lt; class T &gt;

T atomic_fetch_sub( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::difference_type arg ) noexcept;

template&lt; class T &gt;                                        (1)

T atomic_fetch_sub_explicit( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::difference_type arg,

std::memory_order order ) noexcept;                            (2)

template&lt; class T &gt;

T atomic_fetch_sub_explicit( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::difference_type arg,

std::memory_order order ) noexcept;</code></pre> 
Performs atomic subtraction. Atomically subtracts arg from the value pointed to by obj and returns the value obj held previously. The operation is performed as if the following was executed: 
1) obj-&gt;fetch_sub(arg) 
2) obj-&gt;fetch_sub(arg, order) 

<h2>Parameters</h2>

obj - pointer to the atomic object to modify 
arg - the value to subtract from the value stored in the atomic object 
order - the memory sycnhronization ordering for this operation: all values are permitted.

<h2>Return value</h2>

The value immediately preceding the effects of this function in the modification_order of *obj. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;T atomic_fetch_sub( std::atomic&lt;T&gt;* obj, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::atomic&lt;T&gt;::difference_type arg ) noexcept 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return obj-&gt;fetch_sub(arg); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Multiple threads may use fetch_sub to concurrently process an indexed container 
 // Run this code <pre><code>#include &lt;string&gt;

#include &lt;thread&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;atomic&gt;

#include &lt;numeric&gt;
const int N = 50;

std::atomic&lt;int&gt; cnt;

std::vector&lt;int&gt; data(N);
void reader(int id)

{
    for (;;) {
        int idx = atomic_fetch_sub_explicit(&amp;cnt, 1, std::memory_order_relaxed);
        if (idx &gt;= 0) {
            std::cout &lt;&lt; &quot;reader &quot; &lt;&lt; std::to_string(id) &lt;&lt; &quot; processed item &quot;
                      &lt;&lt; std::to_string(data[idx]) &lt;&lt; '\n';
        } else {
            std::cout &lt;&lt; &quot;reader &quot; &lt;&lt; std::to_string(id) &lt;&lt; &quot; done\n&quot;;
            break;
        }
    }
}
int main()

{
    std::iota(data.begin(), data.end(), 1);
    cnt = data.size() - 1;
    std::vector&lt;std::thread&gt; v;
    for (int n = 0; n &lt; 5; ++n) {
        v.emplace_back(reader, n);
    }
    for (auto &amp;t : v) {
        t.join();
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;reader 2 processed item 50 
&nbsp;<wbr>&nbsp;reader 1 processed item 44 
&nbsp;<wbr>&nbsp;reader 4 processed item 46 
&nbsp;<wbr>&nbsp;&lt;....&gt; 
&nbsp;<wbr>&nbsp;reader 0 done 
&nbsp;<wbr>&nbsp;reader 4 done 
&nbsp;<wbr>&nbsp;reader 3 done 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 exact type match required because T is deduced from multiple arguments T is deduced from the atomic argument only

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically subtracts the argument from the value stored in the atomic object and obtains the value held previously 
fetch_sub <i>(public member function of std::atomic&lt;T&gt;)</i> 
atomic_fetch_add 
atomic_fetch_add_explicit adds a non-atomic value to an atomic object and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
