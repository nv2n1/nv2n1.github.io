---
title: "stdlocaleconv(3)"
name: "stdlocaleconv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocaleconv/"
---

std::localeconv - std::localeconv

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;clocale&gt;

std::lconv* localeconv();</code></pre> 
The localeconv function obtains a pointer to a static object of type std::lconv, which represents numeric and monetary formatting rules of the current C locale. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Pointer to the current std::lconv object. 

<h2>Notes</h2>

Modifying the object references through the returned pointer is undefined behavior. 
std::localeconv modifies a static object, calling it from different threads without synchronization is undefined behavior. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;clocale&gt;

#include &lt;iostream&gt;
int main()

{
    std::setlocale(LC_ALL, &quot;ja_JP.UTF-8&quot;);
    std::lconv *lc = std::localeconv();
    std::cout &lt;&lt; &quot;Japanese currency symbol: &quot; &lt;&lt; lc-&gt;currency_symbol
              &lt;&lt; '(' &lt;&lt; lc-&gt;int_curr_symbol &lt;&lt; &quot;)\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Japanese currency symbol: ￥(JPY )

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets and sets the current C locale 
setlocale <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;formatting details, returned by std::localeconv 
lconv <i>(class)</i> 
