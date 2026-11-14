---
title: "stdcondition_variable_anywait(3)"
name: "stdcondition_variable_anywait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variable_anywait/"
description: "std::condition_variable_any::wait – std::condition_variable_any::wait"
---

<p>std::condition_variable_any::wait &#8211; std::condition_variable_any::wait</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Lock&gt;
(1)(since C++ 11)

    void wait(Lock &amp;lock);

template &lt;class Lock, class Predicate&gt;
(2)(since C++ 11)

    void wait(Lock &amp;lock, Predicate pred);</code></pre>
<p>wait causes the current thread to block until the condition variable is notified or a spurious wakeup occurs, optionally looping until some predicate is satisfied.<br />
1) Atomically unlocks lock, blocks the current executing thread, and adds it to the list of threads waiting on *this. The thread will be unblocked when notify_all() or notify_one() is executed. It may also be unblocked spuriously. When unblocked, regardless of the reason, lock is reacquired and wait exits.<br />
If this function exits via exception, lock is also reacquired.<br />
<i>(until C++14)</i><br />
2) Equivalent to while (!pred()) {<br />
    wait(lock);<br />
}<br />
This overload may be used to ignore spurious awakenings while waiting for a specific condition to become true.<br />
Note that lock must be acquired before entering this method, and it is reacquired after wait(lock) exits, which means that lock can be used to guard access to pred().<br />
If these functions fail to meet the postconditions (lock is locked by the calling thread), std::terminate is called. For example, this could happen if relocking the mutex throws an exception, <i>(since C++14)</i> </p>
<h2>Parameters</h2>
<p>lock &#8211; an object of type Lock that meets the BasicLockable requirements, which must be locked by the current thread<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;predicate which returns false if the waiting should be continued.<br />
pred &#8211; The signature of the predicate function should be equivalent to the following:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred();</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Exceptions</h2>
<p>1) </p>
<p>May throw std::system_error, may also propagate exceptions thrown by lock.lock() or lock.unlock(). <i>(until C++14)</i><br />
Does not throw <i>(since C++14)</i> </p>
<p>2) Same as <code>(1)</code> but may also propagate exceptions thrown by pred</p>
<h2>Notes</h2>
<p>The effects of notify_one()/notify_all() and each of the three atomic parts of wait()/wait_for()/wait_until() (unlock+wait, wakeup, and lock) take place in a single total order that can be viewed as modification_order of an atomic variable: the order is specific to this individual condition_variable. This makes it impossible for notify_one() to, for example, be delayed and unblock a thread that started waiting just after the call to notify_one() was made. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

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
    std::cerr &lt;&lt; &quot;Waiting... 
&quot;;
    cv.wait(lk, [] { return i == 1; });
    std::cerr &lt;&lt; &quot;...finished waiting. i == 1
&quot;;
}
void signals()

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
    {
        std::lock_guard&lt;std::mutex&gt; lk(cv_m);
        std::cerr &lt;&lt; &quot;Notifying...
&quot;;
    }
    cv.notify_all();
    std::this_thread::sleep_for(std::chrono::seconds(1));
    {
        std::lock_guard&lt;std::mutex&gt; lk(cv_m);
        i = 1;
        std::cerr &lt;&lt; &quot;Notifying again...
&quot;;
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
<p>&nbsp;<wbr>&nbsp;Waiting&#8230;<br />
&nbsp;<wbr>&nbsp;Waiting&#8230;<br />
&nbsp;<wbr>&nbsp;Waiting&#8230;<br />
&nbsp;<wbr>&nbsp;Notifying&#8230;<br />
&nbsp;<wbr>&nbsp;Notifying again&#8230;<br />
&nbsp;<wbr>&nbsp;&#8230;finished waiting. i == 1<br />
&nbsp;<wbr>&nbsp;&#8230;finished waiting. i == 1<br />
&nbsp;<wbr>&nbsp;&#8230;finished waiting. i == 1</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or after the specified timeout duration<br />
wait_for <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or until specified time point has been reached<br />
wait_until <i>(public member function)</i> </p>
