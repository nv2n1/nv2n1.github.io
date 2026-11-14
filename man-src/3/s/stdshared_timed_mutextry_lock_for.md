---
title: "stdshared_timed_mutextry_lock_for(3)"
name: "stdshared_timed_mutextry_lock_for"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_timed_mutextry_lock_for/"
---

std::shared_timed_mutex::try_lock_for - std::shared_timed_mutex::try_lock_for

<h2>Synopsis</h2>

<pre><code>template &lt;class Rep, class Period&gt;
(since C++ 14)

    bool try_lock_for(const std::chrono::duration&lt;Rep, Period&gt; &amp;timeout_duration);</code></pre> 
Tries to lock the mutex. Blocks until specified timeout_duration has elapsed or the lock is acquired, whichever comes first. On successful lock acquisition returns true, otherwise returns false. 
If timeout_duration is less or equal timeout_duration.zero(), the function behaves like try_lock(). 
This function may block for longer than timeout_duration due to scheduling or resource contention delays. 
The standard recommends that a steady_clock is used to measure the duration. If an implementation uses a system_clock instead, the wait time may also be sensitive to clock adjustments. 
As with try_lock(), this function is allowed to fail spuriously and return false even if the mutex was not locked by any other thread at some point during timeout_duration. 
Prior unlock() operation on the same mutex synchronizes-with (as defined in std::memory_order) this operation if it returns true. 
If try_lock_for is called by a thread that already owns the mutex in any mode (shared or exclusive), the behavior is undefined. 

<h2>Parameters</h2>

timeout_duration - minimum duration to block for

<h2>Return value</h2>

true if the lock was acquired successfully, otherwise false. 

<h2>Exceptions</h2>

Any exception thrown by clock, time_point, or duration during the execution (clocks, time points, and durations provided by the standard library never throw)

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;mutex&gt;

#include &lt;thread&gt;

#include &lt;vector&gt;

#include &lt;sstream&gt;
std::mutex cout_mutex; // control access to std::cout

std::timed_mutex mutex;
void job(int id)

{
    using Ms = std::chrono::milliseconds;
    std::ostringstream stream;
    for (int i = 0; i &lt; 3; ++i) {
        if (mutex.try_lock_for(Ms(100))) {
            stream &lt;&lt; &quot;success &quot;;
            std::this_thread::sleep_for(Ms(100));
            mutex.unlock();
        } else {
            stream &lt;&lt; &quot;failed &quot;;
        }
        std::this_thread::sleep_for(Ms(100));
    }
    std::lock_guard&lt;std::mutex&gt; lock(cout_mutex);
    std::cout &lt;&lt; &quot;[&quot; &lt;&lt; id &lt;&lt; &quot;] &quot; &lt;&lt; stream.str() &lt;&lt; &quot;\n&quot;;
}
int main()

{
    std::vector&lt;std::thread&gt; threads;
    for (int i = 0; i &lt; 4; ++i) {
        threads.emplace_back(job, i);
    }
    for (auto &amp;i : threads) {
        i.join();
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;[0] failed failed failed 
&nbsp;<wbr>&nbsp;[3] failed failed success 
&nbsp;<wbr>&nbsp;[2] failed success failed 
&nbsp;<wbr>&nbsp;[1] success failed success

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex has been 
try_lock_until unavailable until specified time point has been reached 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex 
unlock <i>(public member function)</i> 
