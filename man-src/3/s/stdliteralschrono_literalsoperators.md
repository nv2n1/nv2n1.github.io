---
title: "stdliteralschrono_literalsoperators(3)"
name: "stdliteralschrono_literalsoperators"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdliteralschrono_literalsoperators/"
description: "std::literals::chrono_literals::operator\"\"s – std::literals::chrono_literals::operator\"\"s"
---

<p>std::literals::chrono_literals::operator&quot;&quot;s &#8211; std::literals::chrono_literals::operator&quot;&quot;s</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;chrono&gt;<br />
constexpr chrono::seconds operator &quot;&quot; s(unsigned long long secs); <code>(1)</code> <i>(since C++14)</i><br />
constexpr chrono::duration&lt;/*unspecified*/&gt; operator &quot;&quot; s(long double secs); <code>(2)</code> <i>(since C++14)</i><br />
Forms a std::chrono::duration literal representing seconds.<br />
1) integer literal, returns exactly std::chrono::seconds(secs)<br />
2) floating-point literal, returns a floating-point duration equivalent to std::chrono::seconds </p>
<h2>Parameters</h2>
<p>secs &#8211; the number of seconds</p>
<h2>Return value</h2>
<p>The std::chrono::duration literal. </p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;constexpr std::chrono::seconds operator &quot;&quot;s(unsigned long long s)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::chrono::seconds(s);<br />
&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;constexpr std::chrono::duration&lt;long double&gt; operator &quot;&quot;s(long double s)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::chrono::duration&lt;long double&gt;(s);<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Notes</h2>
<p>These operators are declared in the namespace std::literals::chrono_literals, where both literals and chrono_literals are inline namespaces. Access to these operators can be gained with using namespace std::literals, using namespace std::chrono_literals, and using namespace std::literals::chrono_literals.<br />
In addition, within the namespace std::chrono, the directive using namespace literals::chrono_literals; is provided by the standard library, so that if a programmer uses using namespace std::chrono; to gain access to the classes in the chrono library, the corresponding literal operators become visible as well.<br />
std::string also defines operator&quot;&quot;s, to represent literal objects of type std::string, but it is a string literal: 10s is ten seconds, but &quot;10&quot;s is a two-character string. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;
int main()

{
    using namespace std::chrono_literals;
    auto halfmin = 30s;
    std::cout &lt;&lt; &quot;half a minute is &quot; &lt;&lt; halfmin.count() &lt;&lt; &quot; seconds
&quot;
              &lt;&lt; &quot;a minute and a second is &quot; &lt;&lt; (1min + 1s).count() &lt;&lt; &quot; seconds
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;half a minute is 30 seconds<br />
&nbsp;<wbr>&nbsp;a minute and a second is 61 seconds</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new duration<br />
constructor <i>(public member function of std::chrono::duration&lt;Rep,Period&gt;)</i> </p>
