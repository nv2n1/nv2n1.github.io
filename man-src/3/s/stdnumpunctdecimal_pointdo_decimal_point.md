---
title: "stdnumpunctdecimal_pointdo_decimal_point(3)"
name: "stdnumpunctdecimal_pointdo_decimal_point"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumpunctdecimal_pointdo_decimal_point/"
---

std::numpunct&lt;CharT&gt;::decimal_point,do_decimal_point - std::numpunct&lt;CharT&gt;::decimal_point,do_decimal_point

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 char_type decimal_point() const;

protected:
(2)

    virtual char_type do_decimal_point() const;</code></pre> 
1) Public member function, calls the member function do_decimal_point of the most derived class. 
2) Returns the character to be used as the decimal separator between integer and fractional parts. 

<h2>Return value</h2>

The value of type char_type to use as the decimal separator. The standard specializations of std::numpunct return '.' and L'.'. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
struct slash : std::numpunct&lt;char&gt; {
    char do_decimal_point() const
    {
        return '/';
    } // separate with slash
};
int main()

{
    std::cout.precision(10);
    std::cout &lt;&lt; &quot;default locale: &quot; &lt;&lt; 1234.5678 &lt;&lt; '\n';
    std::cout.imbue(std::locale(std::cout.getloc(), new slash));
    std::cout &lt;&lt; &quot;locale with modified numpunct: &quot; &lt;&lt; 1234.5678 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;default locale: 1234.5678 
&nbsp;<wbr>&nbsp;locale with modified numpunct: 1234/5678
