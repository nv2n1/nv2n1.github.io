---
title: "stdlocalename(3)"
name: "stdlocalename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocalename/"
---

std::locale::name - std::locale::name

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    std::string name() const;</code></pre> 
Returns the name of the locale, which is the name by which it is known to the operating system, such as &quot;POSIX&quot; or &quot;en_US.UTF8&quot; or &quot;English_United States.1252&quot;. If the locale is not a copy of a system-supplied locale, the string &quot;*&quot; is returned. 

<h2>Return value</h2>

The name of the locale or &quot;*&quot; if unnamed. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;locale&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;
int main()

{
    std::locale loc(std::locale(), new std::ctype&lt;char&gt;);
    std::cout &lt;&lt; &quot;The default locale is &quot; &lt;&lt; std::locale().name() &lt;&lt; '\n'
              &lt;&lt; &quot;The user's locale is &quot; &lt;&lt; std::locale(&quot;&quot;).name() &lt;&lt; '\n'
              &lt;&lt; &quot;A nameless locale is &quot; &lt;&lt; loc.name() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The default locale is C 
&nbsp;<wbr>&nbsp;The user's locale is en_US.UTF8 
&nbsp;<wbr>&nbsp;A nameless locale is *

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new locale 
constructor <i>(public member function)</i> 
