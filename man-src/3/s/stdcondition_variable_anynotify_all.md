---
title: "stdcondition_variable_anynotify_all(3)"
name: "stdcondition_variable_anynotify_all"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variable_anynotify_all/"
---

std::condition_variable_any::notify_all - std::condition_variable_any::notify_all

<h2>Synopsis</h2>

<pre><code>void notify_all() noexcept;
(since C++ 11)</code></pre> 
Unblocks all threads currently waiting for *this. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

The effects of notify_one()/notify_all() and each of the three atomic parts of wait()/wait_for()/wait_until() (unlock+wait, wakeup, and lock) take place in a single total order that can be viewed as modification_order of an atomic variable: the order is specific to this individual condition_variable. This makes it impossible for notify_one() to, for example, be delayed and unblock a thread that started waiting just after the call to notify_one() was made. 
The notifying thread does not need to hold the lock on the same mutex as the one held by the waiting thread(s); in fact doing so is a pessimization, since the notified thread would immediately block again, waiting for the notifying thread to release the lock. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;condition_variable&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;
std::condition_variable_any cv;

std::mutex cv_m; // This mutex is used for three purposes:
                 // 1) to synchronize accesses to i
                 // 2) to synchronize accesses to std::cerr
                 // 3) for the condition variable cv

int i = 0;
void waits()

{
    std::unique_lock&lt;std::mutex&gt; lk(cv_m);
    std::cerr &lt;&lt; &quot;Waiting... \n&quot;;
    cv.wait(lk, [] { return i == 1; });
    std::cerr &lt;&lt; &quot;...finished waiting. i == 1\n&quot;;
}
void signals()

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
    {
        std::lock_guard&lt;std::mutex&gt; lk(cv_m);
        std::cerr &lt;&lt; &quot;Notifying...\n&quot;;
    }
    cv.notify_all();
    std::this_thread::sleep_for(std::chrono::seconds(1));
    {
        std::lock_guard&lt;std::mutex&gt; lk(cv_m);
        i = 1;
        std::cerr &lt;&lt; &quot;Notifying again...\n&quot;;
    }
    cv.notify_all();
}
int main()

{
    std::thread t1(waits), t2(waits), t3(waits), t4(signals);
    t1.join();
    t2.join();
    t3.join();
    t4.join();
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Waiting... 
&nbsp;<wbr>&nbsp;Waiting... 
&nbsp;<wbr>&nbsp;Waiting... 
&nbsp;<wbr>&nbsp;Notifying... 
&nbsp;<wbr>&nbsp;Notifying again... 
&nbsp;<wbr>&nbsp;...finished waiting. i == 1 
&nbsp;<wbr>&nbsp;...finished waiting. i == 1 
&nbsp;<wbr>&nbsp;...finished waiting. i == 1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;notifies one waiting thread 
notify_one <i>(public member function)</i> 
