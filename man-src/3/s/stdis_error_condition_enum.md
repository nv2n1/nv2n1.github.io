---
title: "stdis_error_condition_enum(3)"
name: "stdis_error_condition_enum"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_error_condition_enum/"
description: "std::is_error_condition_enum<std::errc> – std::is_error_condition_enum<std::errc>"
---

<p>std::is_error_condition_enum&lt;std::errc&gt; &#8211; std::is_error_condition_enum&lt;std::errc&gt;</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;system_error&gt;

    template &lt;&gt;
    (since C++ 11)

        struct is_error_condition_enum&lt;std::errc&gt; : std::true_type;</code></pre>
<p>Specifies that std::errc is an error condition enum. This enables implicit conversion to std::error_condition.<br />
Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the object to bool, returns value<br />
operator bool <i>(public member function)</i> </p>
<p>operator() returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i></p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type bool<br />
type std::integral_constant&lt;bool, value&gt;</p>
<h2>See also</h2>
<p>is_error_condition_enum identifies an enumeration as an std::error_condition<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
