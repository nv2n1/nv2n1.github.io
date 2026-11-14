---
title: "stdmake_error_conditionstdio_errc(3)"
name: "stdmake_error_conditionstdio_errc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_error_conditionstdio_errc/"
---

std::make_error_condition(std::io_errc) - std::make_error_condition(std::io_errc)

<h2>Synopsis</h2>

Defined in header &lt;ios&gt; 
std::error_condition make_error_condition( std::io_errc e ) noexcept; <i>(since C++11)</i> <pre><code>Constructs an std::error_condition object from a value of type std::io_errc as if by return std::error_condition(static_cast&lt;int&gt;(e), std::iostream_category()).
</code></pre>

<h2>Parameters</h2>

e - error code number

<h2>Return value</h2>

A value of type std::error_condition that holds the error code number from e associated with the error category &quot;iostream&quot;. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;system_error&gt;

#include &lt;string&gt;
int main()

{
    std::error_condition ec = std::make_error_condition(std::io_errc::stream);
    std::cout &lt;&lt; &quot;error condition for io_errc::stream has value &quot; &lt;&lt; ec.value()
              &lt;&lt; &quot;\nand message \&quot;&quot; &lt;&lt; ec.message() &lt;&lt; &quot;\&quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;error condition for io_errc::stream has value 1 
&nbsp;<wbr>&nbsp;and message &quot;unspecified iostream_category error&quot;

<h2>See also</h2>

error_condition holds a portable error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
io_errc the IO stream error codes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
