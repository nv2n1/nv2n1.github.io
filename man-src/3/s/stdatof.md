---
title: "stdatof(3)"
name: "stdatof"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatof/"
---

std::atof - std::atof

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    double atof(const char *str);</code></pre> 
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

<h2>Parameters</h2>

str - pointer to the null-terminated byte string to be interpreted

<h2>Return value</h2>

double value corresponding to the contents of str on success. If the converted value falls out of range of the return type, the return value is undefined. If no conversion can be performed, 0.0 is returned. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdlib&gt;

#include &lt;iostream&gt;
int main()

{
    std::cout &lt;&lt; std::atof(&quot;0.0000000123&quot;) &lt;&lt; &quot;\n&quot;
              &lt;&lt; std::atof(&quot;0.012&quot;) &lt;&lt; &quot;\n&quot;
              &lt;&lt; std::atof(&quot;15e16&quot;) &lt;&lt; &quot;\n&quot;
              &lt;&lt; std::atof(&quot;-0x1afp-2&quot;) &lt;&lt; &quot;\n&quot;
              &lt;&lt; std::atof(&quot;inF&quot;) &lt;&lt; &quot;\n&quot;
              &lt;&lt; std::atof(&quot;Nan&quot;) &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1.23e-08 
&nbsp;<wbr>&nbsp;0.012 
&nbsp;<wbr>&nbsp;1.5e+17 
&nbsp;<wbr>&nbsp;-107.75 
&nbsp;<wbr>&nbsp;inf 
&nbsp;<wbr>&nbsp;nan

<h2>See also</h2>

strtof converts a byte string to a floating point value 
strtod <i>(function)</i> 
strtold 
