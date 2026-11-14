---
title: "stdbind1ststdbind2nd(3)"
name: "stdbind1ststdbind2nd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbind1ststdbind2nd/"
description: "std::bind1st,std::bind2nd – std::bind1st,std::bind2nd"
---

<p>std::bind1st,std::bind2nd &#8211; std::bind1st,std::bind2nd</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;functional&gt;<br />
template&lt; class F, class T &gt; <code>(1)</code> (deprecated in C++11)<br />
std::binder1st&lt;F&gt; bind1st( const F&amp; f, const T&amp; x ); (removed in C++17)<br />
template&lt; class F, class T &gt; <code>(2)</code> (deprecated in C++11)<br />
std::binder2nd&lt;F&gt; bind2nd( const F&amp; f, const T&amp; x ); (removed in C++17)<br />
Binds a given argument x to a first or second parameter of the given binary function object f. That is, stores x within the resulting wrapper, which, if called, passes x as the first or the second parameter of f.<br />
1) Binds the first argument of f to x. Effectively calls std::binder1st&lt;F&gt;(f, typename F::first_argument_type(x)).<br />
2) Binds the second argument of f to x. Effectively calls std::binder2nd&lt;F&gt;(f, typename F::second_argument_type(x)). </p>
<h2>Parameters</h2>
<p>f &#8211; pointer to a function to bind an argument to<br />
x &#8211; argument to bind to f</p>
<h2>Return value</h2>
<p>A function object wrapping f and x. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;functional&gt;

#include &lt;cmath&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;double&gt; a = {0, 30, 45, 60, 90, 180};
    std::vector&lt;double&gt; r(a.size());
    double pi = std::acos(-1);
    std::transform(a.begin(), a.end(), r.begin(),
                   std::bind1st(std::multiplies&lt;double&gt;(), pi / 180.));

    // equivalent lambda: [pi](double a){ return a*pi/180.; });
    for (size_t n = 0; n &lt; a.size(); ++n)
        std::cout &lt;&lt; a[n] &lt;&lt; &quot; deg = &quot; &lt;&lt; r[n] &lt;&lt; &quot; rad
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0 deg = 0 rad<br />
&nbsp;<wbr>&nbsp;30 deg = 0.523599 rad<br />
&nbsp;<wbr>&nbsp;45 deg = 0.785398 rad<br />
&nbsp;<wbr>&nbsp;60 deg = 1.0472 rad<br />
&nbsp;<wbr>&nbsp;90 deg = 1.5708 rad<br />
&nbsp;<wbr>&nbsp;180 deg = 3.14159 rad</p>
<h2>See also</h2>
<p>binder1st function object holding a binary function and one of its arguments<br />
binder2nd <i>(class template)</i><br />
(deprecated in C++11)(removed in C++17) </p>
