---
title: "stdmbrtoc8(3)"
name: "stdmbrtoc8"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmbrtoc8/"
---

std::mbrtoc8 - std::mbrtoc8

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cuchar&gt;

    std::size_t mbrtoc8(char8_t *pc8,

                        const char *s, (since C++ 20)

                                           std::size_t n,

                        std::mbstate_t *ps);</code></pre> 
Converts a narrow multibyte character to UTF-8 encoding. 
If s is not a null pointer, inspects at most n bytes of the multibyte character string, beginning with the byte pointed to by s to determine the number of bytes necessary to complete the next multibyte character (including any shift sequences). If the function determines that the next multibyte character in s is complete and valid, converts it to UTF-8 and stores the first UTf-8 code unit in *pc8 (if pc8 is not null). 
If UTF-8 encoding of the multibyte character in *s consists of more than one UTF-8 code unit, then after the first call to this function, *ps is updated in such a way that the next call to mbrtoc8 will write out the additional UTF-8 code units, without considering *s. 
If s is a null pointer, the values of n and pc8 are ignored and the call is equivalent to std::mbrtoc8(NULL, &quot;&quot;, 1, ps). 
If UTF-8 code unit produced is u8'\0', the conversion state *ps represents the initial shift state. 
The multibyte encoding used by this function is specified by the currently active C locale. 

<h2>Parameters</h2>

pc8 - pointer to the location where the resulting UTF-8 code units will be written 
s - pointer to the multibyte character string used as input 
n - limit on the number of bytes in s that can be examined 
ps - pointer to the conversion state object used when interpreting the multibyte string

<h2>Return value</h2>

The first of the following that applies: 
* 0 if the character converted from s (and stored in *pc8 if non-null) was the null character 
* the number of bytes [1...n] of the multibyte character successfully converted from s 
* -3 if the next UTF-8 code unit from a character whose encoding consists of multiple code units has now been written to *pc8. No bytes are processed from the input in this case. 
* -2 if the next n bytes constitute an incomplete, but so far valid, multibyte character. Nothing is written to *pc8. 
* -1 if encoding error occurs. Nothing is written to *pc8, the value EILSEQ is stored in errno and the value of *ps is unspecified. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

c8rtomb converts UTF-8 string to narrow multibyte encoding 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(C++20) 
