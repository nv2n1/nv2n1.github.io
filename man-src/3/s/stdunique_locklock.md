---
title: "stdunique_locklock(3)"
name: "stdunique_locklock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_locklock/"
---

std::unique_lock&lt;Mutex&gt;::lock - std::unique_lock&lt;Mutex&gt;::lock

<h2>Synopsis</h2>

<pre><code>void lock();
(since C++ 11)</code></pre> 
Locks the associated mutex. Effectively calls mutex()-&gt;lock(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

* Any exceptions thrown by mutex()-&gt;lock() 

 

 
* If there is no associated mutex, std::system_error with an error code of std::errc::operation_not_permitted 

 

 
* If the mutex is already locked by this unique_lock (in other words, owns_lock is true), std::system_error with an error code of std::errc::resource_deadlock_would_occur

<h2>Example</h2>

The following example uses lock to re-acquire a mutex that was unlocked. 
 // Run this code <pre><code>#include &lt;mutex&gt;

#include &lt;thread&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;chrono&gt;
int main()

{
    int counter = 0;
    std::mutex counter_mutex;
    std::vector&lt;std::thread&gt; threads;
    auto worker_task = [&amp;](int id) {
        std::unique_lock&lt;std::mutex&gt; lock(counter_mutex);
        ++counter;
        std::cout &lt;&lt; id &lt;&lt; &quot;, initial counter: &quot; &lt;&lt; counter &lt;&lt; '\n';
        lock.unlock();
        // don't hold the lock while we simulate an expensive operation
        std::this_thread::sleep_for(std::chrono::seconds(1));
        lock.lock();
        ++counter;
        std::cout &lt;&lt; id &lt;&lt; &quot;, final counter: &quot; &lt;&lt; counter &lt;&lt; '\n';
    };
    for (int i = 0; i &lt; 10; ++i)
        threads.emplace_back(worker_task, i);
    for (auto &amp;thread : threads)
        thread.join();
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;0, initial counter: 1 
&nbsp;<wbr>&nbsp;1, initial counter: 2 
&nbsp;<wbr>&nbsp;2, initial counter: 3 
&nbsp;<wbr>&nbsp;3, initial counter: 4 
&nbsp;<wbr>&nbsp;4, initial counter: 5 
&nbsp;<wbr>&nbsp;5, initial counter: 6 
&nbsp;<wbr>&nbsp;6, initial counter: 7 
&nbsp;<wbr>&nbsp;7, initial counter: 8 
&nbsp;<wbr>&nbsp;8, initial counter: 9 
&nbsp;<wbr>&nbsp;9, initial counter: 10 
&nbsp;<wbr>&nbsp;6, final counter: 11 
&nbsp;<wbr>&nbsp;3, final counter: 12 
&nbsp;<wbr>&nbsp;4, final counter: 13 
&nbsp;<wbr>&nbsp;2, final counter: 14 
&nbsp;<wbr>&nbsp;5, final counter: 15 
&nbsp;<wbr>&nbsp;0, final counter: 16 
&nbsp;<wbr>&nbsp;1, final counter: 17 
&nbsp;<wbr>&nbsp;7, final counter: 18 
&nbsp;<wbr>&nbsp;9, final counter: 19 
&nbsp;<wbr>&nbsp;8, final counter: 20

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the associated mutex 
unlock <i>(public member function)</i> 
