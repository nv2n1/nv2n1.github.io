---
title: "stdfutureshare(3)"
name: "stdfutureshare"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfutureshare/"
---

std::future&lt;T&gt;::share - std::future&lt;T&gt;::share

<h2>Synopsis</h2>

<pre><code>std::shared_future&lt;T&gt; share() noexcept;</code></pre> 
Transfers the shared state of *this, if any, to a std::shared_future object. Multiple std::shared_future objects may reference the same shared state, which is not possible with std::future. 
After calling share on a std::future, valid() == false. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A std::shared_future object containing the shared state previously held by *this, if any, constructed as if by std::shared_future&lt;T&gt;(std:move(*this)). 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2556 C++11 share() requires valid() to be true requirement removed and made noexcept 

<h2>See also</h2>

shared_future waits for a value (possibly referenced by other futures) that is set asynchronously 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
