---
title: "stdfposstate(3)"
name: "stdfposstate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfposstate/"
description: "std::fpos<State>::state – std::fpos<State>::state"
---

<p>std::fpos&lt;State&gt;::state &#8211; std::fpos&lt;State&gt;::state</p>
<h2>Synopsis</h2>
<p>State state() const; <code>(1)</code><br />
void state( State st ); <code>(2)</code><br />
Manages the file position state.<br />
1) Returns the value of the file position state<br />
2) Replaces the file position state with the value of st.<br />
For the specializations of std::fpos that are used in the standard library, State is always std::mbstate_t </p>
<h2>Parameters</h2>
<p>st &#8211; new value for the state</p>
<h2>Return value</h2>
<p>1) the current value of the fpos state<br />
2) <i>(none)</i> </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;sstream&gt;

#include &lt;cwchar&gt;
int main()

{
    std::istringstream s(&quot;test&quot;);
    std::mbstate_t st = s.tellg().state();
    if (std::mbsinit(&amp;st))
        std::cout &lt;&lt; &quot;The stream is in the initial shift state
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;The stream is in the initial shift state</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;conversion state information necessary to iterate multibyte character strings<br />
mbstate_t <i>(class)</i> </p>
