---
title: "stdexperimentalshared_futureshared_future(3)"
name: "stdexperimentalshared_futureshared_future"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalshared_futureshared_future/"
description: "std::experimental::shared_future<T>::shared_future – std::experimental::shared_future<T>::shared_future"
---

<p>std::experimental::shared_future&lt;T&gt;::shared_future &#8211; std::experimental::shared_future&lt;T&gt;::shared_future</p>
<h2>Synopsis</h2>
<p>shared_future() noexcept; <code>(1)</code><br />
shared_future(std::experimental::shared_future&lt;T&gt;&amp;&amp; f) noexcept; <code>(2)</code><br />
shared_future(const std::experimental::shared_future&lt;T&gt;&amp; f); <code>(3)</code><br />
shared_future(std::experimental::future&lt;std::experimental::shared_future&lt;T&gt;&gt; &amp;&amp; other) noexcept; <code>(4)</code><br />
shared_future(std::experimental::future&lt;T&gt;&amp;&amp; f) noexcept; <code>(5)</code><br />
1) Default constructor. Constructs an empty shared_future object that does not refer to a shared state.<br />
2) Constructs a shared_future object, transferring the shared state held by f, if any. After construction, f.valid() is false.<br />
3) Constructs a shared future that refers to the same shared state as f, if any.<br />
4) Unwrapping constructor. Constructs a shared_future object from the shared state referred to by other, if any. If other.valid() == false prior to this call, the constructed shared_future object is empty. Otherwise, the resulting shared_future object becomes ready when one of the following happens:<br />
* other and other.get() are both ready. The value or exception from other.get() is stored in the shared state associated with the resulting shared_future object.<br />
* other is ready, but other.get() is invalid. An exception of type std::future_error with an error condition of std::future_errc::broken_promise is stored in the shared state associated with the resulting shared_future object.<br />
After this constructor returns, valid() is equal to the value of other.valid() prior to this call, and other.valid() == false.<br />
5) Constructs a shared_future object, transferring the shared state held by f, if any. After construction, f.valid() is false. </p>
<h2>Parameters</h2>
<p>f &#8211; another future object to initialize with<br />
other &#8211; A std::experimental::future object to unwrap</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_2697 Concurrency TS behavior of unwrapping constructor is unclear with an invalid future constructs an empty future </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the future object<br />
constructor <i>(public member function of std::shared_future&lt;T&gt;)</i> </p>
