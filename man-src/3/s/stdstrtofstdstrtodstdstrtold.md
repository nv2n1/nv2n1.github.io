---
title: "stdstrtofstdstrtodstdstrtold(3)"
name: "stdstrtofstdstrtodstdstrtold"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrtofstdstrtodstdstrtold/"
---

std::strtof,std::strtod,std::strtold - std::strtof,std::strtod,std::strtold

<h2>Synopsis</h2>

Defined in header &lt;cstdlib&gt; 
float strtof( const char* str, char** str_end ); <i>(since C++11)</i> 
double strtod( const char* str, char** str_end ); 
long double strtold( const char* str, char** str_end ); <i>(since C++11)</i> 
Interprets a floating point value in a byte string pointed to by str. 
Function discards any whitespace characters (as determined by std::isspace()) until first non-whitespace character is found. Then it takes as many characters as possible to form a valid floating-point representation and converts them to a floating-point value. The valid floating-point value can be one of the following: 
* decimal floating-point expression. It consists of the following parts: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* (optional) plus or minus sign 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* nonempty sequence of decimal digits optionally containing decimal-point character (as determined by the current C locale) (defines significand) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* (optional) e or E followed with optional minus or plus sign and nonempty sequence of decimal digits (defines exponent) 
* binary floating-point expression. It consists of the following parts: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* (optional) plus or minus sign 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* 0x or 0X 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* nonempty sequence of hexadecimal digits optionally containing a decimal-point character (as determined by the current C locale) (defines significand) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* (optional) p or P followed with optional minus or plus sign and nonempty sequence of decimal digits (defines exponent) 
* infinity expression. It consists of the following parts: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* (optional) plus or minus sign 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* INF or INFINITY ignoring case 
* not-a-number expression. It consists of the following parts: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* (optional) plus or minus sign 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* NAN or NAN(char_sequence) ignoring case of the NAN part. char_sequence can only contain digits, Latin letters, and underscores. The result is a quiet NaN floating-point value. 
* any other expression that may be accepted by the currently installed C locale 
The functions sets the pointer pointed to by str_end to point to the character past the last character interpreted. If str_end is NULL, it is ignored. 

<h2>Parameters</h2>

str - pointer to the null-terminated byte string to be interpreted 
str_end - pointer to a pointer to character.

<h2>Return value</h2>

Floating point value corresponding to the contents of str on success. If the converted value falls out of range of corresponding return type, range error occurs and HUGE_VAL, HUGE_VALF or HUGE_VALL is returned. If no conversion can be performed, 0 is returned and *str_end is set to str. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;cerrno&gt;

#include &lt;cstdlib&gt;
int main()

{
    const char *p = &quot;111.11 -2.22 0X1.BC70A3D70A3D7P+6  1.18973e+4932zzz&quot;;
    char *end;
    std::cout &lt;&lt; &quot;Parsing \&quot;&quot; &lt;&lt; p &lt;&lt; &quot;\&quot;:\n&quot;;
    for (double f = std::strtod(p, &amp;end); p != end; f = std::strtod(p, &amp;end)) {
        std::cout &lt;&lt; &quot;'&quot; &lt;&lt; std::string(p, end - p) &lt;&lt; &quot;' -&gt; &quot;;
        p = end;
        if (errno == ERANGE) {
            std::cout &lt;&lt; &quot;range error, got &quot;;
            errno = 0;
        }
        std::cout &lt;&lt; f &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Parsing &quot;111.11 -2.22 0X1.BC70A3D70A3D7P+6 1.18973e+4932zzz&quot;: 
&nbsp;<wbr>&nbsp;'111.11' -&gt; 111.11 
&nbsp;<wbr>&nbsp;' -2.22' -&gt; -2.22 
&nbsp;<wbr>&nbsp;' 0X1.BC70A3D70A3D7P+6' -&gt; 111.11 
&nbsp;<wbr>&nbsp;' 1.18973e+4932' -&gt; range error, got inf

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string to a floating point value 
atof <i>(function)</i> 
wcstof converts a wide string to a floating point value 
wcstod <i>(function)</i> 
wcstold 
from_chars converts a character sequence to an integer or floating-point value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
