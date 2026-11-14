---
title: "stdbinder1ststdbinder2nd(3)"
name: "stdbinder1ststdbinder2nd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinder1ststdbinder2nd/"
description: "std::binder1st,std::binder2nd – std::binder1st,std::binder2nd"
---

<p>std::binder1st,std::binder2nd &#8211; std::binder1st,std::binder2nd</p>
<h2>Synopsis</h2>
<p>template&lt; class Fn &gt;<br />
class binder1st : public std::unary_function&lt;typename Fn::second_argument_type,<br />
typename Fn::result_type&gt; {<br />
protected: </p>
<pre><code>Fn op;

typename Fn::first_argument_type value;

public:
(deprecated in C++ 11)(1)(removed in C++ 17)

    binder1st(const Fn &amp;fn,

              const typename Fn::first_argument_type &amp;value);
typename Fn::result_type

operator()(const typename Fn::second_argument_type &amp;x) const;</code></pre>
<p>typename Fn::result_type<br />
operator()(typename Fn::second_argument_type&amp; x) const;<br />
};<br />
template&lt; class Fn &gt;<br />
class binder2nd : public unary_function&lt;typename Fn::first_argument_type,<br />
typename Fn::result_type&gt; {<br />
protected:<br />
Fn op;<br />
typename Fn::second_argument_type value;<br />
public:<br />
binder2nd(const Fn&amp; fn, <code>(2)</code> (deprecated in C++11)<br />
const typename Fn::second_argument_type&amp; value); (removed in C++17) typename Fn::result_type</p>
<p>operator()(const typename Fn::first_argument_type &amp;x) const;<br />
typename Fn::result_type</p>
<p>operator()(typename Fn::first_argument_type &amp;x) const;<br />
}<br />
;<br />
A function object that binds an argument to a binary function.<br />
The value of the parameter is passed to the object at the construction time and stored within the object. Whenever the function object is invoked though operator(), the stored value is passed as one of the arguments, the other argument is passed as an argument of operator(). The resulting function object is an unary function.<br />
1) Binds the first parameter to the value value given at the construction of the object.<br />
2) Binds the second parameter to the value value given at the construction of the object. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;functional&gt;

#include &lt;cmath&gt;

#include &lt;vector&gt;

const double pi = std::acos(-1);

int main()

{
    // deprecated in C++11, removed in C++17
    std::binder1st&lt;std::multiplies&lt;double&gt;&gt; f1 = std::bind1st(
        std::multiplies&lt;double&gt;(), pi / 180.);
    // C++11 replacement
    auto f2 = [](double a) { return a * pi / 180.; };
    for (double n : {0, 30, 45, 60, 90, 180})
        std::cout &lt;&lt; n &lt;&lt; &quot; deg = &quot; &lt;&lt; f1(n) &lt;&lt; &quot; rad (using binder) &quot;
                  &lt;&lt; f2(n) &lt;&lt; &quot; rad (using lambda)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0 deg = 0 rad (using binder) 0 rad (using lambda)<br />
&nbsp;<wbr>&nbsp;30 deg = 0.523599 rad (using binder) 0.523599 rad (using lambda)<br />
&nbsp;<wbr>&nbsp;45 deg = 0.785398 rad (using binder) 0.785398 rad (using lambda)<br />
&nbsp;<wbr>&nbsp;60 deg = 1.0472 rad (using binder) 1.0472 rad (using lambda)<br />
&nbsp;<wbr>&nbsp;90 deg = 1.5708 rad (using binder) 1.5708 rad (using lambda)<br />
&nbsp;<wbr>&nbsp;180 deg = 3.14159 rad (using binder) 3.14159 rad (using lambda)</p>
<h2>See also</h2>
<p>bind1st binds one argument to a binary function<br />
bind2nd <i>(function template)</i><br />
(deprecated in C++11)(removed in C++17) </p>
