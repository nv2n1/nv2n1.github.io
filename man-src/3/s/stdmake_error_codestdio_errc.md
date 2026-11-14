---
title: "stdmake_error_codestdio_errc(3)"
name: "stdmake_error_codestdio_errc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_error_codestdio_errc/"
---

std::make_error_code(std::io_errc) - std::make_error_code(std::io_errc)

<h2>Synopsis</h2>

Defined in header &lt;ios&gt; 
std::error_code make_error_code( std::io_errc e ) noexcept; <i>(since C++11)</i> 
Constructs an std::error_code object from a value of type std::io_errc as if by return std::error_code(static_cast&lt;int&gt;(e), std::iostream_category()). This function is called by the constructor of std::error_code when given an std::io_errc argument. 

<h2>Parameters</h2>

e - error code number

<h2>Return value</h2>

A value of type std::error_code that holds the error code number from e associated with the error category &quot;iostream&quot;. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;system_error&gt;

int main()

{
    std::error_code ec = std::make_error_code(std::io_errc::stream);
    std::cout &lt;&lt; &quot;Error code from io_errc::stream has category &quot;
              &lt;&lt; ec.category().name() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Error code from io_errc::stream has category iostream

<h2>See also</h2>

error_code holds a platform-dependent error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
io_errc the IO stream error codes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
