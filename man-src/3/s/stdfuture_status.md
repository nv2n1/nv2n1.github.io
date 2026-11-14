---
title: "stdfuture_status(3)"
name: "stdfuture_status"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfuture_status/"
---

std::future_status - std::future_status

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;future&gt;

enum class future_status {

    ready,

    timeout,                    (since C++11)

    deferred

};</code></pre> 
Specifies state of a future as returned by wait_for and wait_until functions of std::future and std::shared_future. 
Constant Explanation 
deferred the shared state contains a deferred function, so the result will be computed only when explicitly requested 
ready the shared state is ready 
timeout the shared state did not become ready before specified timeout duration has passed 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available for the specified timeout duration 
wait_for <i>(public member function of std::future&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available for the specified timeout duration 
wait_for <i>(public member function of std::shared_future&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available until specified time point has been reached 
wait_until <i>(public member function of std::future&lt;T&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;waits for the result, returns if it is not available until specified time point has been reached 
wait_until <i>(public member function of std::shared_future&lt;T&gt;)</i> 
