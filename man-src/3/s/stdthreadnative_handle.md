---
title: "stdthreadnative_handle(3)"
name: "stdthreadnative_handle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreadnative_handle/"
---

std::thread::native_handle - std::thread::native_handle

<h2>Synopsis</h2>

native_handle_type native_handle(); <i>(since C++11)</i> 
Returns the implementation defined underlying thread handle. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

implementation defined handle type representing the thread. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

Uses native_handle to enable realtime scheduling of C++ threads on a POSIX system 
 // Run this code <pre><code>#include &lt;thread&gt;

#include &lt;mutex&gt;

#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;cstring&gt;

#include &lt;pthread.h&gt;
std::mutex iomutex;

void f(int num)

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
    sched_param sch;
    int policy;
    pthread_getschedparam(pthread_self(), &amp;policy, &amp;sch);
    std::lock_guard&lt;std::mutex&gt; lk(iomutex);
    std::cout &lt;&lt; &quot;Thread &quot; &lt;&lt; num &lt;&lt; &quot; is executing at priority &quot;
              &lt;&lt; sch.sched_priority &lt;&lt; '\n';
}
int main()

{
    std::thread t1(f, 1), t2(f, 2);
    sched_param sch;
    int policy;
    pthread_getschedparam(t1.native_handle(), &amp;policy, &amp;sch);
    sch.sched_priority = 20;
    if (pthread_setschedparam(t1.native_handle(), SCHED_FIFO, &amp;sch)) {
        std::cout &lt;&lt; &quot;Failed to setschedparam: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '\n';
    }
    t1.join();
    t2.join();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Thread 2 is executing at priority 0 
&nbsp;<wbr>&nbsp;Thread 1 is executing at priority 20
