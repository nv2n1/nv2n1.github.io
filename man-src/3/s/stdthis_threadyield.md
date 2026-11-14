---
title: "stdthis_threadyield(3)"
name: "stdthis_threadyield"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthis_threadyield/"
---

std::this_thread::yield - std::this_thread::yield

<h2>Synopsis</h2>

Defined in header &lt;thread&gt; 
void yield() noexcept; <i>(since C++11)</i> 
Provides a hint to the implementation to reschedule the execution of threads, allowing other threads to run. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

The exact behavior of this function depends on the implementation, in particular on the mechanics of the OS scheduler in use and the state of the system. For example, a first-in-first-out realtime scheduler (SCHED_FIFO in Linux) would suspend the current thread and put it on the back of the queue of the same-priority threads that are ready to run (and if there are no other threads at the same priority, yield has no effect). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;thread&gt;
// &quot;busy sleep&quot; while suggesting that other threads run

// for a small amount of time

void little_sleep(std::chrono::microseconds us)

{
    auto start = std::chrono::high_resolution_clock::now();
    auto end = start + us;
    do {
        std::this_thread::yield();
    } while (std::chrono::high_resolution_clock::now() &lt; end);
}
int main()

{
    auto start = std::chrono::high_resolution_clock::now();
    little_sleep(std::chrono::microseconds(100));
    auto elapsed = std::chrono::high_resolution_clock::now() - start;
    std::cout &lt;&lt; &quot;waited for &quot;
              &lt;&lt; std::chrono::duration_cast&lt;std::chrono::microseconds&gt;(elapsed).count()
              &lt;&lt; &quot; microseconds\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;waited for 128 microseconds

<h2>See also</h2>


