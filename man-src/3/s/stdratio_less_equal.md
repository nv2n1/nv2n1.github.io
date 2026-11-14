---
title: "stdratio_less_equal(3)"
name: "stdratio_less_equal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdratio_less_equal/"
description: "std::ratio_less_equal – std::ratio_less_equal"
---

<p>std::ratio_less_equal &#8211; std::ratio_less_equal</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;ratio&gt;

    template &lt;class R1, class R2&gt;
    (since C++ 11)

        struct ratio_less_equal : std::integral_constant;</code></pre>
<p>If the ratio R1 is less than or equal to the ratio R2, provides the member constant value equal true. Otherwise, value is false.<br />
Helper variable template </p>
<pre><code>template&lt; class R1, class R2 &gt;                                               (since C++17)

inline constexpr bool ratio_less_equal_v = ratio_less_equal&lt;R1, R2&gt;::value;
</code></pre>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if R1::num * R2::den &lt;= R2::num * R1::den, or equivalent expression that avoids overflow , false otherwise<br />
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
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
