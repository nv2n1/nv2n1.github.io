---
title: "stdcondition_variable_anywait_for(3)"
name: "stdcondition_variable_anywait_for"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variable_anywait_for/"
description: "std::condition_variable_any::wait_for – std::condition_variable_any::wait_for"
---

<p>std::condition_variable_any::wait_for &#8211; std::condition_variable_any::wait_for</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Lock, class Rep, class Period&gt;

std::cv_status wait_for(Lock &amp;lock, (1)(since C++ 11)

                                        const std::chrono::duration&lt;Rep, Period&gt; &amp;rel_time);

template &lt;class Lock, class Rep, class Period, class Predicate&gt;

bool wait_for(Lock &amp;lock, (2)(since C++ 11)

                              const std::chrono::duration&lt;Rep, Period&gt; &amp;rel_time,

              Predicate pred);
1) Atomically releases lock, blocks the current executing thread, and adds it to the list of threads waiting on *this. The thread will be unblocked when notify_all() or notify_one() is executed, or when the relative timeout rel_time expires. It may also be unblocked spuriously. When unblocked, regardless of the reason, lock is reacquired and wait_for() exits.

If this function exits via exception, lock is also reacquired.

(until C++14)

2) Equivalent to return wait_until(lock, std::chrono::steady_clock::now() + rel_time, std::move(pred));. This overload may be used to ignore spurious awakenings.

A steady clock is used to measure the duration. This function may block for longer than timeout_duration due to scheduling or resource contention delays.
</code></pre>
<p>If these functions fail to meet the postcondition (lock is locked by the calling thread), std::terminate is called. For example, this could happen if relocking the mutex throws an exception, <i>(since C++14)</i> </p>
<h2>Parameters</h2>
<p>lock &#8211; an object of type Lock that meets the BasicLockable requirements, which must be locked by the current thread<br />
rel_time &#8211; an object of type std::chrono::duration representing the maximum time to spend waiting. Note that rel_time must be small enough not to overflow when added to std::chrono::steady_clock::now().<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;predicate which returns false if the waiting should be continued.<br />
pred &#8211; The signature of the predicate function should be equivalent to the following:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred();</p>
<h2>Return value</h2>
<p>1) std::cv_status::timeout if the relative timeout specified by rel_time expired, std::cv_status::no_timeout otherwise.<br />
2) false if the predicate pred still evaluates to false after the rel_time timeout expired, otherwise true. </p>
<h2>Exceptions</h2>
<p>1) </p>
<p>May throw std::system_error, may also propagate exceptions thrown by lock.lock() or lock.unlock(). <i>(until C++14)</i><br />
Any exception thrown by clock, time_point, or duration during the execution (clocks, time points, and durations provided by the standard library never throw) <i>(since C++14)</i> </p>
<p>2) Same as <code>(1)</code> but may also propagate exceptions thrown by pred</p>
<h2>Notes</h2>
<p>Even if notified under lock, overload <code>(1)</code> makes no guarantees about the state of the associated predicate when returning due to timeout.<br />
The effects of notify_one()/notify_all() and each of the three atomic parts of wait()/wait_for()/wait_until() (unlock+wait, wakeup, and lock) take place in a single total order that can be viewed as modification_order of an atomic variable: the order is specific to this individual condition_variable. This makes it impossible for notify_one() to, for example, be delayed and unblock a thread that started waiting just after the call to notify_one() was made. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;atomic&gt;

#include &lt;condition_variable&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;

using namespace std::chrono_literals;
std::condition_variable_any cv;

std::mutex cv_m;

int i;
void waits(int idx)

{
    std::unique_lock&lt;std::mutex&gt; lk(cv_m);
    if (cv.wait_for(lk, idx * 100ms, [] { return i == 1; }))
        std::cerr &lt;&lt; &quot;Thread &quot; &lt;&lt; idx &lt;&lt; &quot; finished waiting. i == &quot; &lt;&lt; i &lt;&lt; '
';
    else
        std::cerr &lt;&lt; &quot;Thread &quot; &lt;&lt; idx &lt;&lt; &quot; timed out. i == &quot; &lt;&lt; i &lt;&lt; '
';
}
void signals()

{
    std::this_thread::sleep_for(120ms);
    std::cerr &lt;&lt; &quot;Notifying...
&quot;;
    cv.notify_all();
    std::this_thread::sleep_for(100ms);
    {
        std::lock_guard&lt;std::mutex&gt; lk(cv_m);
        i = 1;
    }
    std::cerr &lt;&lt; &quot;Notifying again...
&quot;;
    cv.notify_all();
}
int main()

{
    std::thread t1(waits, 1), t2(waits, 2), t3(waits, 3), t4(signals);
    t1.join();
    t2.join();
    t3.join();
    t4.join();
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Thread 1 timed out. i == 0<br />
&nbsp;<wbr>&nbsp;Notifying&#8230;<br />
&nbsp;<wbr>&nbsp;Thread 2 timed out. i == 0<br />
&nbsp;<wbr>&nbsp;Notifying again&#8230;<br />
&nbsp;<wbr>&nbsp;Thread 3 finished waiting. i == 1</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up<br />
wait <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or until specified time point has been reached<br />
wait_until <i>(public member function)</i> </p>
