---
title: "stdstofstdstodstdstold(3)"
name: "stdstofstdstodstdstold"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstofstdstodstdstold/"
---

std::stof,std::stod,std::stold - std::stof,std::stod,std::stold

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;string&gt;

    float stof(const std::string &amp;str, std::size_t *pos = 0);
(1)(since C++ 11)

    float stof(const std::wstring &amp;str, std::size_t *pos = 0);

double stod(const std::string &amp;str, std::size_t *pos = 0);
(2)(since C++ 11)

    double stod(const std::wstring &amp;str, std::size_t *pos = 0);

long double stold(const std::string &amp;str, std::size_t *pos = 0);
(3)(since C++ 11)

    long double stold(const std::wstring &amp;str, std::size_t *pos = 0);</code></pre> 
Interprets a floating point value in a string str. 
1) calls std::strtod(str.c_str(), &amp;ptr) or std::wcstod(str.c_str(), &amp;ptr) <i>(until C++17)</i> 
1) calls std::strtof(str.c_str(), &amp;ptr) or std::wcstof(str.c_str(), &amp;ptr) <i>(since C++17)</i> 
2) calls std::strtod(str.c_str(), &amp;ptr) or std::wcstod(str.c_str(), &amp;ptr) 
3) calls std::strtold(str.c_str(), &amp;ptr) or std::wcstold(str.c_str(), &amp;ptr) 
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
If pos is not a null pointer, then a pointer ptr, internal to the conversion functions, will receive the address of the first unconverted character in str.c_str(), and the index of that character will be calculated and stored in *pos, giving the number of characters that were processed by the conversion. 

<h2>Parameters</h2>

str - the string to convert 
pos - address of an integer to store the number of characters processed

<h2>Return value</h2>

The string converted to the specified floating point type. 

<h2>Exceptions</h2>

std::invalid_argument if no conversion could be performed 
std::out_of_range if the converted value would fall out of the range of the result type or if the underlying function ( 
strtof, 
<i>(since C++17)</i>strtod or strtold) sets errno to ERANGE.

<h2>See also</h2>

stoi 
stol 
stoll converts a string to a signed integer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
stoul 
stoull converts a string to an unsigned integer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
from_chars converts a character sequence to an integer or floating-point value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
