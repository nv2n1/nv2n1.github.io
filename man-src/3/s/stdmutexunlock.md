---
title: "stdmutexunlock(3)"
name: "stdmutexunlock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmutexunlock/"
---

std::mutex::unlock - std::mutex::unlock

<h2>Synopsis</h2>

<pre><code>void unlock();
(since C++ 11)</code></pre> 
Unlocks the mutex. 
The mutex must be locked by the current thread of execution, otherwise, the behavior is undefined. 
This operation synchronizes-with (as defined in std::memory_order) any subsequent lock operation that obtains ownership of the same mutex. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

unlock() is usually not called directly: std::unique_lock and std::lock_guard are used to manage exclusive locking. 

<h2>Example</h2>

This example shows how lock and unlock can be used to protect shared data. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;thread&gt;

#include &lt;mutex&gt;
int g_num = 0; // protected by g_num_mutex

std::mutex g_num_mutex;
void slow_increment(int id)

{
    for (int i = 0; i &lt; 3; ++i) {
        g_num_mutex.lock();
        ++g_num;
        std::cout &lt;&lt; id &lt;&lt; &quot; =&gt; &quot; &lt;&lt; g_num &lt;&lt; '\n';
        g_num_mutex.unlock();
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}
int main()

{
    std::thread t1(slow_increment, 0);
    std::thread t2(slow_increment, 1);
    t1.join();
    t2.join();
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;0 =&gt; 1 
&nbsp;<wbr>&nbsp;1 =&gt; 2 
&nbsp;<wbr>&nbsp;0 =&gt; 3 
&nbsp;<wbr>&nbsp;1 =&gt; 4 
&nbsp;<wbr>&nbsp;0 =&gt; 5 
&nbsp;<wbr>&nbsp;1 =&gt; 6

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
