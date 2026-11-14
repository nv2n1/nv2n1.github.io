---
title: "stdexperimentalparallelis_execution_policy(3)"
name: "stdexperimentalparallelis_execution_policy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalparallelis_execution_policy/"
description: "std::experimental::parallel::is_execution_policy – std::experimental::parallel::is_execution_policy"
---

<p>std::experimental::parallel::is_execution_policy &#8211; std::experimental::parallel::is_execution_policy</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / execution_policy&gt;

    template &lt;class T&gt;
    (parallelism TS)

        struct is_execution_policy;</code></pre>
<p>Checks whether T is a standard or implementation-defined execution policy type.<br />
Provides the member constant value which is equal to true, if T is execution_policy, sequential_execution_policy, parallel_execution_policy, parallel_vector_execution_policy, or an implementation-defined execution policy type. Otherwise, value is equal to false.<br />
The behavior of a program that adds specializations for is_execution_policy is undefined. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper template </p>
<p>Defined in header &lt;experimental/execution_policy&gt;<br />
template&lt; class T &gt; (parallelism TS)<br />
constexpr bool is_execution_policy_v = is_execution_policy&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is a standard or implementation-defined execution policy type , false otherwise<br />
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
