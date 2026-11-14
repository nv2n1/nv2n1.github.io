---
title: "stdshared_futurewait_for(3)"
name: "stdshared_futurewait_for"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_futurewait_for/"
---

std::shared_future&lt;T&gt;::wait_for - std::shared_future&lt;T&gt;::wait_for

<h2>Synopsis</h2>

<pre><code>template &lt;class Rep, class Period&gt;
(since C++ 11)

    std::future_status wait_for(const std::chrono::duration&lt;Rep, Period&gt; &amp;timeout_duration) const;</code></pre> 
Waits for the result to become available. Blocks until specified timeout_duration has elapsed or the result becomes available, whichever comes first. Returns value identifies the state of the result. 
This function may block for longer than timeout_duration due to scheduling or resource contention delays. 
The standard recommends that a steady clock is used to measure the duration. If an implementation uses a system clock instead, the wait time may also be sensitive to clock adjustments. 
The behavior is undefined if valid()== false before the call to this function. 

<h2>Parameters</h2>

timeout_duration - maximum duration to block for

<h2>Return value</h2>

Constant Explanation 
future_status::deferred The function to calculate the result has not been started yet 
future_status::ready The result is ready 
future_status::timeout The timeout has expired 

<h2>Exceptions</h2>

Any exception thrown by clock, time_point, or duration during the execution (clocks, time points, and durations provided by the standard library never throw)

<h2>Notes</h2>

The implementations are encouraged to detect the case when valid == false before the call and throw a future_error with an error condition of future_errc::no_state. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;future&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;
int main()

{
    std::shared_future&lt;int&gt; future = std::async(std::launch::async, []() {
        std::this_thread::sleep_for(std::chrono::seconds(3));
        return 8;
    });
    std::cout &lt;&lt; &quot;waiting...\n&quot;;
    std::future_status status;
    do {
        status = future.wait_for(std::chrono::seconds(1));
        if (status == std::future_status::deferred) {
            std::cout &lt;&lt; &quot;deferred\n&quot;;
        } else if (status == std::future_status::timeout) {
            std::cout &lt;&lt; &quot;timeout\n&quot;;
        } else if (status == std::future_status::ready) {
            std::cout &lt;&lt; &quot;ready!\n&quot;;
        }
    } while (status != std::future_status::ready);
    std::cout &lt;&lt; &quot;result is &quot; &lt;&lt; future.get() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;waiting... 
&nbsp;<wbr>&nbsp;timeout 
&nbsp;<wbr>&nbsp;timeout 
&nbsp;<wbr>&nbsp;ready! 
&nbsp;<wbr>&nbsp;result is 8

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result to become available 
wait <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available until specified time point has been reached 
wait_until <i>(public member function)</i> 
