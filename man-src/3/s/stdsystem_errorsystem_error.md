---
title: "stdsystem_errorsystem_error(3)"
name: "stdsystem_errorsystem_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsystem_errorsystem_error/"
---

std::system_error::system_error - std::system_error::system_error

<h2>Synopsis</h2>

<pre><code>system_error(std::error_code ec);
(1)(since C++ 11)

    system_error(std::error_code ec, const std::string &amp;what_arg);
(2)(since C++ 11)

    system_error(std::error_code ec, const char *what_arg);
(2)(since C++ 11)

    system_error(int ev, const std::error_category &amp;ecat);
(3)(since C++ 11)

    system_error(int ev, const std::error_category &amp;ecat, (4)(since C++ 11)

                                                              const std::string &amp;what_arg);

system_error(int ev, const std::error_category &amp;ecat, (4)(since C++ 11)

                                                          const char *what_arg);</code></pre> 
Constructs new system error object. 
1) Constructs with error code ec 
2) Constructs with error code ec and explanation string what_arg. The string returned by what() is guaranteed to contain what_arg as a substring. 
3) Constructs with underlying error code ev and associated error category ecat. 
4) Constructs with underlying error code ev, associated error category ecat and explanatory string what_arg. The string returned by what() is guaranteed to contain what_arg as a substring. 

<h2>Parameters</h2>

ec - error code 
ev - underlying error code in the enumeration associated with ecat 
ecat - the category of error 
what_arg - explanatory string

<h2>Example</h2>

Demonstrates how to create a system_error exception from an errno value. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;system_error&gt;
int main()

{
    try {
        throw std::system_error(EDOM, std::generic_category(), &quot;hello world&quot;);
    } catch (const std::system_error &amp;ex) {
        std::cout &lt;&lt; ex.code() &lt;&lt; '\n';
        std::cout &lt;&lt; ex.code().message() &lt;&lt; '\n';
        std::cout &lt;&lt; ex.what() &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;generic:33 
&nbsp;<wbr>&nbsp;Numerical argument out of domain 
&nbsp;<wbr>&nbsp;hello world: Numerical argument out of domain
