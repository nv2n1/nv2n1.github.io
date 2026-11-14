---
title: "stdcondition_variable_anywait_until(3)"
name: "stdcondition_variable_anywait_until"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variable_anywait_until/"
description: "std::condition_variable_any::wait_until – std::condition_variable_any::wait_until"
---

<p>std::condition_variable_any::wait_until &#8211; std::condition_variable_any::wait_until</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Lock, class Clock, class Duration&gt;

std::cv_status(1)(since C++ 11)

    wait_until(Lock &amp;lock,

               const std::chrono::time_point&lt;Clock, Duration&gt; &amp;timeout_time);

template &lt;class Lock, class Clock, class Duration, class Pred&gt;

bool wait_until(Lock &amp;lock, (2)(since C++ 11)

                                const std::chrono::time_point&lt;Clock, Duration&gt; &amp;timeout_time,

                Pred pred);</code></pre>
<p>wait_until causes the current thread to block until the condition variable is notified, a specific time is reached, or a spurious wakeup occurs, optionally looping until some predicate is satisfied.<br />
1) Atomically releases lock, blocks the current executing thread, and adds it to the list of threads waiting on *this. The thread will be unblocked when notify_all() or notify_one() is executed, or when the absolute time point timeout_time is reached. It may also be unblocked spuriously. When unblocked, regardless of the reason, lock is reacquired and wait_until exits.<br />
If this function exits via exception, lock is also reacquired.<br />
<i>(until C++14)</i><br />
2) Equivalent to while (!pred()) {<br />
    if (wait_until(lock, timeout_time) == std::cv_status::timeout) {<br />
        return pred();<br />
    }<br />
}</p>
<p>return true;<br />
This overload may be used to ignore spurious wakeups.<br />
If these functions fail to meet the postcondition (lock is locked by the calling thread), std::terminate is called. For example, this could happen if relocking the mutex throws an exception, <i>(since C++14)</i> </p>
<h2>Parameters</h2>
<p>lock &#8211; an object of type Lock that meets the requirements of BasicLockable, which must be locked by the current thread<br />
timeout_time &#8211; an object of type std::chrono::time_point representing the time when to stop waiting<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;predicate which returns false if the waiting should be continued.<br />
pred &#8211; The signature of the predicate function should be equivalent to the following:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred();</p>
<h2>Return value</h2>
<p>1) std::cv_status::timeout if the absolute timeout specified by timeout_time was reached, std::cv_status::no_timeout overwise.<br />
2) false if the predicate pred still evaluates to false after the timeout_time timeout expired, otherwise true. If the timeout had already expired, evaluates and returns the result of pred. </p>
<h2>Exceptions</h2>
<p>1) </p>
<p>May throw std::system_error, may also propagate exceptions thrown by lock.lock() or lock.unlock(). <i>(until C++14)</i><br />
Any exception thrown by clock, time point, or duration during the execution (clocks, time points, and durations provided by the standard library never throw) <i>(since C++14)</i> </p>
<p>2) Same as <code>(1)</code> but may also propagate exceptions thrown by pred</p>
<h2>Notes</h2>
<p>The clock tied to timeout_time is used, which is not required to be a monotonic clock.There are no guarantees regarding the behavior of this function if the clock is adjusted discontinuously, but the existing implementations convert timeout_time from Clock to std::chrono::system_clock and delegate to POSIX pthread_cond_timedwait so that the wait honors ajustments to the system clock, but not to the the user-provided Clock. In any case, the function also may wait for longer than until after timeout_time has been reached due to scheduling or resource contention delays.<br />
Even if the clock in use is std::chrono::steady_clock or another monotonic clock, a system clock adjustment may induce a spurious wakeup.<br />
The effects of notify_one()/notify_all() and each of the three atomic parts of wait()/wait_for()/wait_until() (unlock+wait, wakeup, and lock) take place in a single total order that can be viewed as modification_order of an atomic variable: the order is specific to this individual condition_variable. This makes it impossible for notify_one() to, for example, be delayed and unblock a thread that started waiting just after the call to notify_one() was made. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;atomic&gt;

#include &lt;condition_variable&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;

using namespace std::chrono_literals;
std::condition_variable cv;

std::mutex cv_m;

std::atomic&lt;int&gt; i{0};
void waits(int idx)

{
    std::unique_lock&lt;std::mutex&gt; lk(cv_m);
    auto now = std::chrono::system_clock::now();
    if (cv.wait_until(lk, now + idx * 100ms, []() { return i == 1; }))
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
    i = 1;
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
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Thread 1 timed out. i == 0<br />
&nbsp;<wbr>&nbsp;Notifying&#8230;<br />
&nbsp;<wbr>&nbsp;Thread 2 timed out. i == 0<br />
&nbsp;<wbr>&nbsp;Notifying again&#8230;<br />
&nbsp;<wbr>&nbsp;Thread 3 finished waiting. i == 1</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up<br />
wait <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or after the specified timeout duration<br />
wait_for <i>(public member function)</i> </p>
