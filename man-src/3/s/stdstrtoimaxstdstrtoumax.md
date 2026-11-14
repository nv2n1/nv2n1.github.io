---
title: "stdstrtoimaxstdstrtoumax(3)"
name: "stdstrtoimaxstdstrtoumax"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrtoimaxstdstrtoumax/"
description: "std::strtoimax,std::strtoumax – std::strtoimax,std::strtoumax"
---

<p>std::strtoimax,std::strtoumax &#8211; std::strtoimax,std::strtoumax</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cinttypes&gt;<br />
std::intmax_t strtoimax( const char* nptr, char** endptr, int base ); <i>(since C++11)</i><br />
std::uintmax_t strtoumax( const char* nptr, char** endptr, int base ); <i>(since C++11)</i> </p>
<pre><code>Interprets an integer value in a byte string pointed to by nptr.

Discards any whitespace characters (as identified by calling isspace()) until the first non-whitespace character is found, then takes as many characters as possible to form a valid base-n (where n=base) integer number representation and converts them to an integer value. The valid integer value consists of the following parts:</code></pre>
<p>* (optional) plus or minus sign<br />
* (optional) prefix <code>(0)</code> indicating octal base (applies only when the base is 8 or 0)<br />
* (optional) prefix (0x or 0X) indicating hexadecimal base (applies only when the base is 16 or 0)<br />
* a sequence of digits<br />
The set of valid values for base is {0,2,3,&#8230;,36}. The set of valid digits for base-2 integers is {0,1}, for base-3 integers is {0,1,2}, and so on. For bases larger than 10, valid digits include alphabetic characters, starting from Aa for base-11 integer, to Zz for base-36 integer. The case of the characters is ignored.<br />
Additional numeric formats may be accepted by the currently installed C locale.<br />
If the value of base is 0, the numeric base is auto-detected: if the prefix is 0, the base is octal, if the prefix is 0x or 0X, the base is hexadecimal, otherwise the base is decimal.<br />
If the minus sign was part of the input sequence, the numeric value calculated from the sequence of digits is negated as if by unary_minus in the result type.<br />
The functions sets the pointer pointed to by endptr to point to the character past the last character interpreted. If endptr is NULL, it is ignored.<br />
If the nptr is empty or does not have the expected form, no conversion is performed, and (if enptr is not NULL) the value of nptr is stored in the object pointed to by endptr. </p>
<h2>Parameters</h2>
<p>nptr &#8211; pointer to the null-terminated byte string to be interpreted<br />
endptr &#8211; pointer to a pointer to character.<br />
base &#8211; base of the interpreted integer value</p>
<h2>Return value</h2>
<p>* If successful, an integer value corresponding to the contents of str is returned.<br />
* If the converted value falls out of range of corresponding return type, a range error occurs (setting errno to ERANGE) and INTMAX_MAX, INTMAX_MIN, UINTMAX_MAX or 0 is returned, as appropriate.<br />
* If no conversion can be performed, 0 is returned. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;cinttypes&gt;
int main()

{
    std::string str = &quot;helloworld&quot;;
    std::intmax_t val = std::strtoimax(str.c_str(), nullptr, 36);
    std::cout &lt;&lt; str &lt;&lt; &quot; in base 36 is &quot; &lt;&lt; val &lt;&lt; &quot; in base 10
&quot;;
    char *nptr;
    val = std::strtoimax(str.c_str(), &amp;nptr, 30);
    if (nptr != &amp;str[0] + str.size())
        std::cout &lt;&lt; str &lt;&lt; &quot; in base 30 is invalid.&quot;
                  &lt;&lt; &quot; The first invalid digit is &quot; &lt;&lt; *nptr &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;helloworld in base 36 is 1767707668033969 in base 10<br />
&nbsp;<wbr>&nbsp;helloworld in base 30 is invalid. The first invalid digit is w</p>
<h2>See also</h2>
<p>wcstoimax<br />
wcstoumax converts a wide string to std::intmax_t or std::uintmax_t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string to an integer value<br />
strtol <i>(function)</i><br />
strtoll<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string to an unsigned integer value<br />
strtoul <i>(function)</i><br />
strtoull </p>
