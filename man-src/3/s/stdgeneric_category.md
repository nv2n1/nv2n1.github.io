---
title: "stdgeneric_category(3)"
name: "stdgeneric_category"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgeneric_category/"
---

std::generic_category - std::generic_category

<h2>Synopsis</h2>

Defined in header &lt;system_error&gt; 
const std::error_category&amp; generic_category() noexcept; <i>(since C++11)</i> <pre><code>Obtains a reference to the static error category object for generic errors. The object is required to override the virtual function error_category::name() to return a pointer to the string &quot;generic&quot;. It is used to identify error conditions that correspond to the POSIX errno codes.
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A reference to the static object of unspecified runtime type, derived from std::error_category. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;system_error&gt;

#include &lt;cerrno&gt;

#include &lt;string&gt;

int main()

{
    std::error_condition econd = std::generic_category().default_error_condition(EDOM);
    std::cout &lt;&lt; &quot;Category: &quot; &lt;&lt; econd.category().name() &lt;&lt; '\n'
              &lt;&lt; &quot;Value: &quot; &lt;&lt; econd.value() &lt;&lt; '\n'
              &lt;&lt; &quot;Message: &quot; &lt;&lt; econd.message() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Category: generic 
&nbsp;<wbr>&nbsp;Value: 33 
&nbsp;<wbr>&nbsp;Message: Numerical argument out of domain

<h2>See also</h2>

system_category identifies the operating system error category 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
errc the std::error_condition enumeration listing all standard &lt;cerrno&gt; macro constants 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
