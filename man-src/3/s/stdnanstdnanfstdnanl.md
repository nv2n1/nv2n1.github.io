---
title: "stdnanstdnanfstdnanl(3)"
name: "stdnanstdnanfstdnanl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnanstdnanfstdnanl/"
description: "std::nan,std::nanf,std::nanl – std::nan,std::nanf,std::nanl"
---

<p>std::nan,std::nanf,std::nanl &#8211; std::nan,std::nanf,std::nanl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float nanf( const char* arg ); <i>(since C++11)</i><br />
double nan( const char* arg ); <i>(since C++11)</i><br />
long double nanl( const char* arg ); <i>(since C++11)</i><br />
Converts the implementation-defined character string arg into the corresponding quiet NaN value, as if by calling std::strtod, std::strtof, or std::strtold, respectively, as follows:<br />
The call std::nan(&quot;n-char-sequence&quot;), where n-char-sequence is a sequence of digits, Latin letters, and underscores, is equivalent to the call std::strtod(&quot;NAN(n-char-sequence)&quot;, (char**)nullptr);.<br />
The call std::nan(&quot;&quot;) is equivalent to the call std::strtod(&quot;NAN()&quot;, (char**)nullptr);.<br />
The call std::nan(&quot;string&quot;), where string is neither an n-char-sequence nor an empty string, is equivalent to the call std::strtod(&quot;NAN&quot;, (char**)nullptr);. </p>
<h2>Parameters</h2>
<p>arg &#8211; narrow character string identifying the contents of a NaN</p>
<h2>Return value</h2>
<p>The quiet NaN value that corresponds to the identifying string arg or zero if the implementation does not support quiet NaNs. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cstdint&gt;

#include &lt;cstring&gt;
int main()

{
    double f1 = std::nan(&quot;1&quot;);
    std::uint64_t f1n;
    std::memcpy(&amp;f1n, &amp;f1, sizeof f1);
    std::cout &lt;&lt; &quot;nan(\&quot;1\&quot;) = &quot; &lt;&lt; f1 &lt;&lt; &quot; (&quot; &lt;&lt; std::hex &lt;&lt; f1n &lt;&lt; &quot;)
&quot;;
    double f2 = std::nan(&quot;2&quot;);
    std::uint64_t f2n;
    std::memcpy(&amp;f2n, &amp;f2, sizeof f2);
    std::cout &lt;&lt; &quot;nan(\&quot;2\&quot;) = &quot; &lt;&lt; f2 &lt;&lt; &quot; (&quot; &lt;&lt; std::hex &lt;&lt; f2n &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;nan(&quot;1&quot;) = nan (7ff0000000000001)<br />
&nbsp;<wbr>&nbsp;nan(&quot;2&quot;) = nan (7ff0000000000002)</p>
<h2>See also</h2>
<p>isnan checks if the given number is NaN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
NAN evaluates to a quiet NaN of type float<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(macro constant)<br />
<i>(C++11)</i><br />
has_quiet_NaN identifies floating-point types that can represent the special value &quot;quiet not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant of std::numeric_limits&lt;T&gt;)</i><br />
<code>[static]</code><br />
has_signaling_NaN identifies floating-point types that can represent the special value &quot;signaling not-a-number&quot; (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant of std::numeric_limits&lt;T&gt;)</i><br />
<code>[static]</code><br />
quiet_NaN returns a quiet NaN value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::numeric_limits&lt;T&gt;)</i><br />
<code>[static]</code><br />
signaling_NaN returns a signaling NaN value of the given floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::numeric_limits&lt;T&gt;)</i><br />
<code>[static]</code> </p>
