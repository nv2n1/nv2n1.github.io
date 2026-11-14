---
title: "stdratio(3)"
name: "stdratio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdratio/"
description: "std::ratio – std::ratio"
---

<p>std::ratio &#8211; std::ratio</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;ratio&gt;

template&lt;

std::intmax_t Num,         (since C++11)

std::intmax_t Denom = 1

&gt; class ratio;</code></pre>
<p>The class template std::ratio provides compile-time_rational_arithmetic support. Each instantiation of this template exactly represents any finite rational number as long as its numerator Num and denominator Denom are representable as compile-time constants of type std::intmax_t. In addition, Denom may not be zero and may not be equal to the most negative value.<br />
The static data members nom and den representing the numerator and denominator are calculated by dividing Num and Denom by their greatest common divisor. However, two std::ratio with different Num or Denom are distinct types even if they represent the same rational number (after reduction). A ratio type can be reduced to the lowest terms via its type member: std::ratio&lt;3, 6&gt;::type is std::ratio&lt;1, 2&gt;.<br />
Several convenience typedefs that correspond to the SI ratios are provided by the standard library:<br />
Defined in header &lt;ratio&gt;<br />
Type Definition<br />
yocto std::ratio&lt;1, 1000000000000000000000000&gt;, if std::intmax_t can represent the denominator<br />
zepto std::ratio&lt;1, 1000000000000000000000&gt;, if std::intmax_t can represent the denominator<br />
atto std::ratio&lt;1, 1000000000000000000&gt;<br />
femto std::ratio&lt;1, 1000000000000000&gt;<br />
pico std::ratio&lt;1, 1000000000000&gt;<br />
nano std::ratio&lt;1, 1000000000&gt;<br />
micro std::ratio&lt;1, 1000000&gt;<br />
milli std::ratio&lt;1, 1000&gt;<br />
centi std::ratio&lt;1, 100&gt;<br />
deci std::ratio&lt;1, 10&gt;<br />
deca std::ratio&lt;10, 1&gt;<br />
hecto std::ratio&lt;100, 1&gt;<br />
kilo std::ratio&lt;1000, 1&gt;<br />
mega std::ratio&lt;1000000, 1&gt;<br />
giga std::ratio&lt;1000000000, 1&gt;<br />
tera std::ratio&lt;1000000000000, 1&gt;<br />
peta std::ratio&lt;1000000000000000, 1&gt;<br />
exa std::ratio&lt;1000000000000000000, 1&gt;<br />
zetta std::ratio&lt;1000000000000000000000, 1&gt;, if std::intmax_t can represent the numerator<br />
yotta std::ratio&lt;1000000000000000000000000, 1&gt;, if std::intmax_t can represent the numerator </p>
<h2>Member types</h2>
<p>Member type Definition<br />
type std::ratio&lt;num, den&gt;</p>
<h2>Member objects</h2>
<p>constexpr intmax_t num constexpr value of type std::intmax_t equal to sign(Num) * sign(Denom) * abs(Num) / gcd(Num, Denom)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>constexpr intmax_t den constexpr value of type std::intmax_t equal to abs(Denom) / gcd(Num, Denom)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
