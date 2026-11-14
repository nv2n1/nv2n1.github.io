---
title: "stdrecursive_timed_mutexlock(3)"
name: "stdrecursive_timed_mutexlock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrecursive_timed_mutexlock/"
---

std::recursive_timed_mutex::lock - std::recursive_timed_mutex::lock

<h2>Synopsis</h2>

<pre><code>void lock();
(since C++ 11)</code></pre> 
Locks the mutex. If another thread has already locked the mutex, a call to lock will block execution until the lock is acquired. 
A thread may call lock on a recursive mutex repeatedly. Ownership will only be released after the thread makes a matching number of calls to unlock. 
The maximum number of levels of ownership is unspecified. An exception of type std::system_error will be thrown if this number is exceeded. 
Prior unlock() operations on the same mutex synchronize-with (as defined in std::memory_order) this operation. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Throws std::system_error when errors occur, including errors from the underlying operating system that would prevent lock from meeting its specifications. The mutex is not locked in the case of any exception being thrown.

<h2>Notes</h2>

lock() is usually not called directly: std::unique_lock and std::lock_guard are used to manage exclusive locking. 

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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex has been 
try_lock_for unavailable for the specified timeout duration 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex has been 
try_lock_until unavailable until specified time point has been reached 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex 
unlock <i>(public member function)</i> 
