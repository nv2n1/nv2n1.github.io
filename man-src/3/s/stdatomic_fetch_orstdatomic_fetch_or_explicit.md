---
title: "stdatomic_fetch_orstdatomic_fetch_or_explicit(3)"
name: "stdatomic_fetch_orstdatomic_fetch_or_explicit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_fetch_orstdatomic_fetch_or_explicit/"
---

std::atomic_fetch_or,std::atomic_fetch_or_explicit - std::atomic_fetch_or,std::atomic_fetch_or_explicit

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;atomic&gt;

template&lt; class T &gt;

T atomic_fetch_or( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type arg ) noexcept;

template&lt; class T &gt;

T atomic_fetch_or( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type arg ) noexcept;

template&lt; class T &gt;                                       (1) (since C++11)

T atomic_fetch_or_explicit( std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type arg,

std::memory_order order) noexcept;                                          (2) (since C++11)

template&lt; class T &gt;

T atomic_fetch_or_explicit( volatile std::atomic&lt;T&gt;* obj,

typename std::atomic&lt;T&gt;::value_type arg,

std::memory_order order) noexcept;</code></pre> 
Atomically replaces the value pointed by obj with the result of bitwise OR between the old value of obj and arg. Returns the value obj held previously. 
The operation is performed as if the following is executed: 
1) obj-&gt;fetch_or(arg) 
2) obj-&gt;fetch_or(arg, order) 
If std::atomic&lt;T&gt; has no fetch_xor member (this member is only provided for integral_types), the program is ill-formed. 

<h2>Parameters</h2>

obj - pointer to the atomic object to modify 
arg - the value to bitwise OR to the value stored in the atomic object 
order - the memory synchronization ordering for this operation: all values are permitted.

<h2>Return value</h2>

The value immediately preceding the effects of this function in the modification_order of *obj. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;T atomic_fetch_or( std::atomic&lt;T&gt;* obj, typename std::atomic&lt;T&gt;::value_type arg ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return obj-&gt;fetch_or(arg); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;atomic&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;

#include &lt;functional&gt;
// Binary semaphore for demonstrative purposes only

// This is a simple yet meaningful example: atomic operations

// are unnecessary without threads.

class Semaphore
{
    std::atomic_char m_signaled;

  public:
    Semaphore(bool initial = false)
    {
        m_signaled = initial;
    }
    // Block until semaphore is signaled
    void take()
    {
        while (!std::atomic_fetch_and(&amp;m_signaled, false)) {
            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }
    void put()
    {
        std::atomic_fetch_or(&amp;m_signaled, true);
    }
};
class ThreadedCounter
{
    static const int N = 100;
    static const int REPORT_INTERVAL = 10;
    int m_count;
    bool m_done;
    Semaphore m_count_sem;
    Semaphore m_print_sem;
    void count_up()
    {
        for (m_count = 1; m_count &lt;= N; m_count++) {
            if (m_count % REPORT_INTERVAL == 0) {
                if (m_count == N)
                    m_done = true;
                m_print_sem.put();  // signal printing to occur
                m_count_sem.take(); // wait until printing is complete proceeding
            }
        }
        std::cout &lt;&lt; &quot;count_up() done\n&quot;;
        m_done = true;
        m_print_sem.put();
    }
    void print_count()
    {
        do {
            m_print_sem.take();
            std::cout &lt;&lt; m_count &lt;&lt; '\n';
            m_count_sem.put();
        } while (!m_done);
        std::cout &lt;&lt; &quot;print_count() done\n&quot;;
    }

  public:
    ThreadedCounter()
        : m_done(false)
    {
    }
    void run()
    {
        auto print_thread = std::thread(&amp;ThreadedCounter::print_count, this);
        auto count_thread = std::thread(&amp;ThreadedCounter::count_up, this);
        print_thread.join();
        count_thread.join();
    }
};
int main()

{
    ThreadedCounter m_counter;
    m_counter.run();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;10 
&nbsp;<wbr>&nbsp;20 
&nbsp;<wbr>&nbsp;30 
&nbsp;<wbr>&nbsp;40 
&nbsp;<wbr>&nbsp;50 
&nbsp;<wbr>&nbsp;60 
&nbsp;<wbr>&nbsp;70 
&nbsp;<wbr>&nbsp;80 
&nbsp;<wbr>&nbsp;90 
&nbsp;<wbr>&nbsp;100 
&nbsp;<wbr>&nbsp;print_count() done 
&nbsp;<wbr>&nbsp;count_up() done 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 exact type match required because T is deduced from multiple arguments T is deduced from the atomic argument only

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs bitwise OR between the argument and the value of the atomic object and obtains the value held previously 
fetch_or <i>(public member function of std::atomic&lt;T&gt;)</i> 
atomic_fetch_and 
atomic_fetch_and_explicit replaces the atomic object with the result of bitwise AND with a non-atomic argument and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
atomic_fetch_xor 
atomic_fetch_xor_explicit replaces the atomic object with the result of bitwise XOR with a non-atomic argument and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
