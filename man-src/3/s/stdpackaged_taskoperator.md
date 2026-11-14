---
title: "stdpackaged_taskoperator(3)"
name: "stdpackaged_taskoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpackaged_taskoperator/"
---

std::packaged_task&lt;R(Args...)&gt;::operator= - std::packaged_task&lt;R(Args...)&gt;::operator=

<h2>Synopsis</h2>

<pre><code>packaged_task &amp;operator=(const packaged_task &amp;) = delete;
(1)(since C++ 11)

    packaged_task &amp;
    operator=(packaged_task &amp;&amp;rhs) noexcept;
(2)(since C++ 11)</code></pre> 
1) Copy assignment operator is deleted, std::packaged_task is move-only. 
2) Releases the shared state, if any, destroys the previously-held task, and moves the shared state and the task owned by rhs into *this. rhs is left without a shared state and with a moved-from task. 

<h2>Parameters</h2>

rhs - the std::packaged_task to move from

<h2>Exceptions</h2>

1) <i>(none)</i> 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2067 C++11 the deleted copy assignment operator took reference to non-const made const

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
