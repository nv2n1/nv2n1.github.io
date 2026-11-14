---
title: "std-codecvt-3(3)"
name: "std-codecvt-3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-3/"
---

<h2 class="name">NAME</h2>
 

 std::mbrtowc - std::mbrtowc

<h2>Synopsis</h2>

 

 
Defined in header &lt;cwchar&gt; 
std::size_t mbrtowc( wchar_t* pwc, 
const char* s, 
std::size_t n, 
std::mbstate_t* ps ); 

 
Converts a narrow multibyte character to a wide character. 
If s is not a null pointer, inspects at most n bytes of the multibyte character string, beginning with the byte pointed to by s to determine the number of bytes necessary to complete the next multibyte character (including any shift sequences). If the function determines that the next multibyte character in s is complete and valid, converts it to the corresponding wide character and stores it in *pwc (if pwc is not null). 
If s is a null pointer, the values of n and pwc are ignored and call is equivalent to std::mbrtowc(NULL, &quot;&quot;, 1, ps). 
If the wide character produced is the null character, the conversion state stored in *ps is the initial shift state. 

<h2>Parameters</h2>

 

 

 
pwc - pointer to the location where the resulting wide character will be written 
s - pointer to the multibyte character string used as input 
n - limit on the number of bytes in s that can be examined 
ps - pointer to the conversion state used when interpreting the multibyte string 

 

<h2>Return value</h2>

 

 
The first of the following that applies: 

 
* 0 if the character converted from s (and stored in pwc if non-null) was the null character 
* the number of bytes [1...n] of the multibyte character successfully converted from s 
* static_cast&lt;std::size_t&gt;(-2) if the next n bytes constitute an incomplete, but so far valid, multibyte character. Nothing is written to *pwc. 
* static_cast&lt;std::size_t&gt;(-1) if encoding error occurs. Nothing is written to *pwc, the value EILSEQ is stored in errno and the value of *ps is left unspecified. 

 

<h2>Example</h2>

 

 
 // Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;iostream&gt; 
&nbsp;<wbr>&nbsp;#include &lt;clocale&gt; 
&nbsp;<wbr>&nbsp;#include &lt;cstring&gt; 
&nbsp;<wbr>&nbsp;#include &lt;cwchar&gt; 

 
&nbsp;<wbr>&nbsp;void print_mb(const char* ptr) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::mbstate_t state = std::mbstate_t(); // initial state 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char* end = ptr + std::strlen(ptr); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int len; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wchar_t wc; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while((len = std::mbrtowc(&amp;wc, ptr, end-ptr, &amp;state)) &gt; 0) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wcout &lt;&lt; &quot;Next &quot; &lt;&lt; len &lt;&lt; &quot; bytes are the character &quot; &lt;&lt; wc &lt;&lt; '\n'; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptr += len; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;int main() 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::setlocale(LC_ALL, &quot;en_US.utf8&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// UTF-8 narrow multibyte encoding 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char* str = u8&quot;z\u00df\u6c34\U0001d10b&quot;; // or u8&quot;zß水&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// or &quot;\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b&quot;; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print_mb(str); 
&nbsp;<wbr>&nbsp;} 

<h2>Output:</h2>

 

 
&nbsp;<wbr>&nbsp;Next 1 bytes are the character z 
&nbsp;<wbr>&nbsp;Next 2 bytes are the character ß 
&nbsp;<wbr>&nbsp;Next 3 bytes are the character 水 
&nbsp;<wbr>&nbsp;Next 4 bytes are the character  

 

<h2>See also</h2>

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the next multibyte character to wide character 
mbtowc <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to its multibyte representation, given state 
wcrtomb <i>(function)</i> 

 
do_in converts a string from externT to internT, such as when reading from file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
<b>[virtual]</b> 

 

 

 

 

<h2>Index</h2>


