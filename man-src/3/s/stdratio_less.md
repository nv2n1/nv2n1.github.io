---
title: "stdratio_less(3)"
name: "stdratio_less"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdratio_less/"
description: "std::ratio_less – std::ratio_less"
---

<p>std::ratio_less &#8211; std::ratio_less</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;ratio&gt;

    template &lt;class R1, class R2&gt;
    (since C++ 11)

        struct ratio_less : std::integral_constant;</code></pre>
<p>If the ratio R1 is less than the ratio R2, provides the member constant value equal true. Otherwise, value is false.<br />
Helper variable template template&lt; class R1, class R2 &gt;                                   (since C++17)</p>
<p>inline constexpr bool ratio_less_v = ratio_less&lt;R1, R2&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if R1::num * R2::den &lt; R2::num * R1::den, or equivalent expression that avoids overflow , false otherwise<br />
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
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;ratio&gt;
int main()

{
    if (std::ratio_less&lt;std::ratio&lt;23, 37&gt;, std::ratio&lt;57, 90&gt;&gt;::value) {
        std::cout &lt;&lt; &quot;23/37 &lt; 57/90
&quot;;
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;23/37 &lt; 57/90</p>
<h2>See also</h2>
