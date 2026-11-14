---
title: "stdshared_futurewait_until(3)"
name: "stdshared_futurewait_until"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_futurewait_until/"
---

std::shared_future&lt;T&gt;::wait_until - std::shared_future&lt;T&gt;::wait_until

<h2>Synopsis</h2>

<pre><code>template &lt;class Clock, class Duration&gt;
(since C++ 11)

    std::future_status wait_until(const std::chrono::time_point&lt;Clock, Duration&gt; &amp;timeout_time) const;</code></pre> 
wait_until waits for a result to become available. It blocks until specified timeout_time has been reached or the result becomes available, whichever comes first. The return value indicates why wait_until returned. 
The behavior is undefined if valid()== false before the call to this function. 

<h2>Parameters</h2>

timeout_time - maximum time point to block until

<h2>Return value</h2>

Constant Explanation 
future_status::deferred The function to calculate the result has not been started yet 
future_status::ready The result is ready 
future_status::timeout The timeout has expired 

<h2>Exceptions</h2>

Any exception thrown by clock, time_point, or duration during the execution (clocks, time points, and durations provided by the standard library never throw)

<h2>Notes</h2>

The implementations are encouraged to detect the case when valid == false before the call and throw a future_error with an error condition of future_errc::no_state. 
The clock tied to timeout_time is used, which is not required to be a monotonic clock.There are no guarantees regarding the behavior of this function if the clock is adjusted discontinuously, but the existing implementations convert timeout_time from Clock to std::chrono::system_clock and delegate to POSIX pthread_cond_timedwait so that the wait honors ajustments to the system clock, but not to the the user-provided Clock. In any case, the function also may wait for longer than until after timeout_time has been reached due to scheduling or resource contention delays. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result to become available 
wait <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available for the specified timeout duration 
wait_for <i>(public member function)</i> 
