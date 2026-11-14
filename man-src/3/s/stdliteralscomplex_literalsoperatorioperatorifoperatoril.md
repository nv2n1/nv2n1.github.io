---
title: "stdliteralscomplex_literalsoperatorioperatorifoperatoril(3)"
name: "stdliteralscomplex_literalsoperatorioperatorifoperatoril"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdliteralscomplex_literalsoperatorioperatorifoperatoril/"
---

std::literals::complex_literals::operator&quot;&quot;i,operator&quot;&quot;if,operator&quot;&quot;il - std::literals::complex_literals::operator&quot;&quot;i,operator&quot;&quot;if,operator&quot;&quot;il

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    constexpr complex&lt;double&gt; operator&quot;&quot;i(long double arg);
(1)(since C++ 14)

    constexpr complex&lt;double&gt;
    operator&quot;&quot;i(unsigned long long arg);

constexpr complex&lt;float&gt; operator&quot;&quot;if(long double arg);
(2)(since C++ 14)

    constexpr complex&lt;float&gt;
    operator&quot;&quot;if(unsigned long long arg);

constexpr complex&lt;long double&gt; operator&quot;&quot;il(long double arg);
(3)(since C++ 14)

    constexpr complex&lt;long double&gt;
    operator&quot;&quot;il(unsigned long long arg);</code></pre> 
Forms a std::complex literal representing an imaginary number. 
1) forms a literal std::complex&lt;double&gt; with the real part zero and imaginary part arg 
2) forms a literal std::complex&lt;float&gt; with the real part zero and imaginary part arg 
3) forms a literal std::complex&lt;long double&gt; with the real part zero and imaginary part arg 

<h2>Parameters</h2>

arg - the value of the imaginary number

<h2>Return value</h2>

The std::complex literal with the real part zero and imaginary part arg 

<h2>Notes</h2>

These operators are declared in the namespace std::literals::complex_literals, where both literals and complex_literals are inline namespaces. Access to these operators can be gained with using namespace std::literals, using namespace std::complex_literals, and using namespace std::literals::complex_literals. 
Even though if is a keyword in C++, it is a ud-suffix of the literal_operator of the form operator &quot;&quot;if and in the literal expressions such as 1if or 1.0if because it is not separated by whitespace and is not a standalone token. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;constexpr std::complex&lt;double&gt; operator&quot;&quot;i(unsigned long long d) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::complex&lt;double&gt;{0.0, static_cast&lt;double&gt;(d)}; 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;constexpr std::complex&lt;double&gt; operator&quot;&quot;i(long double d) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::complex&lt;double&gt;{0.0, static_cast&lt;double&gt;(d)}; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;constexpr std::complex&lt;float&gt; operator&quot;&quot;if(unsigned long long d) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::complex&lt;float&gt;{0.0f, static_cast&lt;float&gt;(d)}; 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;constexpr std::complex&lt;float&gt; operator&quot;&quot;if(long double d) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::complex&lt;float&gt;{0.0f, static_cast&lt;float&gt;(d)}; 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;constexpr std::complex&lt;long double&gt; operator&quot;&quot;il(unsigned long long d) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::complex&lt;long double&gt;{0.0L, static_cast&lt;long double&gt;(d)}; 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;constexpr std::complex&lt;long double&gt; operator&quot;&quot;il(long double d) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::complex&lt;long double&gt;{0.0L, d}; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code #include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    using namespace std::complex_literals;
    std::complex&lt;double&gt; c = 1.0 + 1i;
    std::cout &lt;&lt; &quot;abs&quot; &lt;&lt; c &lt;&lt; &quot; = &quot; &lt;&lt; abs(c) &lt;&lt; '\n';
}


<h2>Output:</h2>

&nbsp;<wbr>&nbsp;abs(1,1) = 1.41421

<h2>See also</h2>

<pre><code>constructs a complex number

constructor   (public member function)
assigns the contents

operator=     (public member function)




</code></pre>
