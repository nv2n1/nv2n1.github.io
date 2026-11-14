---
title: "stdcv_status(3)"
name: "stdcv_status"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcv_status/"
---

std::cv_status - std::cv_status

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;condition_variable&gt;

enum class cv_status {

    no_timeout,                             (since C++11)

    timeout

};</code></pre> 
The scoped enumeration std::cv_status describes whether a timed wait returned because of timeout or not. 
std::cv_status is used by the wait_for and wait_until methods of std::condition_variable and std::condition_variable_any. 

<h2>Member constants</h2>

Constant Explanation 
no_timeout the condition variable was awakened with notify_all, notify_one, or spuriously 
timeout the condition variable was awakened by timeout expiration

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or after the specified timeout duration 
wait_for <i>(public member function of std::condition_variable)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or after the specified timeout duration 
wait_for <i>(public member function of std::condition_variable_any)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or until specified time point has been reached 
wait_until <i>(public member function of std::condition_variable)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or until specified time point has been reached 
wait_until <i>(public member function of std::condition_variable_any)</i> 
