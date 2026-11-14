---
title: "stdexperimentalfuturefuture(3)"
name: "stdexperimentalfuturefuture"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfuturefuture/"
---

std::experimental::future&lt;T&gt;::future - std::experimental::future&lt;T&gt;::future

<h2>Synopsis</h2>

<pre><code>future() noexcept;
(1)

    future(std::experimental::future&lt;T&gt; &amp;&amp;f) noexcept;
(2)

    future(const std::experimental::future&lt;T&gt; &amp;) = delete;
(3)

    future(std::experimental::future&lt;std::experimental::future&lt;T&gt;&gt; &amp;&amp;other) noexcept;
(4)</code></pre> 
1) Default constructor. Constructs an empty future object that does not refer to a shared state. 
2) Constructs a future object, transferring the shared state held by f, if any. After construction, f.valid() is false. 
3) Copy constructor is deleted. future cannot be copied. 
4) Unwrapping constructor. Constructs a future object from the shared state referred to by other, if any. If other.valid() == false prior to this call, the constructed future object is empty. Otherwise, the resulting future object becomes ready when one of the following happens: 
* other and other.get() are both ready. The value or exception from other.get() is stored in the shared state associated with the resulting future object. 
* other is ready, but other.get() is invalid. An exception of type std::future_error with an error condition of std::future_errc::broken_promise is stored in the shared state associated with the resulting future object. 
After this constructor returns, valid() is equal to the value of other.valid() prior to this call, and other.valid() == false. 

<h2>Parameters</h2>

f - another future object to initialize with 
other - A std::experimental::future object to unwrap

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2697 Concurrency TS behavior of unwrapping constructor is unclear with an invalid future constructs an empty future 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the future object 
constructor <i>(public member function of std::future&lt;T&gt;)</i> 
