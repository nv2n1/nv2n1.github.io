---
title: "stdmbrlen(3)"
name: "stdmbrlen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmbrlen/"
description: "std::mbrlen – std::mbrlen"
---

<p>std::mbrlen &#8211; std::mbrlen</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cwchar&gt;

    std::size_t mbrlen(const char *s, std::size_t n, std::mbstate_t *ps);</code></pre>
<p>Determines the size, in bytes, of the remainder of the multibyte character whose first byte is pointed to by s, given the current conversion state ps.<br />
This function is equivalent to the call std::mbrtowc(nullptr, s, n, ps?ps:&amp;internal) for some hidden object internal of type std::mbstate_t, except that the expression ps is evaluated only once. </p>
<h2>Parameters</h2>
<p>s &#8211; pointer to an element of a multibyte character string<br />
n &#8211; limit on the number of bytes in s that can be examined<br />
ps &#8211; pointer to the variable holding the conversion state</p>
<h2>Return value</h2>
<p>0 if the next n or fewer bytes complete the null character.<br />
The number of bytes (between 1 and n) that complete a valid multibyte character<br />
(size_t)-1 if encoding error occurs<br />
(size_t)-2 if the next n bytes are part of a possibly valid multibyte character, which is still incomplete after examining all n bytes </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;clocale&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;cwchar&gt;
int main()

{
    // allow mbrlen() to work with UTF-8 multibyte encoding
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    // UTF-8 narrow multibyte encoding
    std::string str = u8&quot;水&quot;; // or u8&quot;水&quot; or &quot;水&quot;
    std::mbstate_t mb = std::mbstate_t();
    int len1 = std::mbrlen(&amp;str[0], 1, &amp;mb);
    if (len1 == -2) {
        std::cout &lt;&lt; &quot;The first 1 byte of &quot; &lt;&lt; str
                  &lt;&lt; &quot; is an incomplete multibyte char (mbrlen returns -2)
&quot;;
    }
    int len2 = std::mbrlen(&amp;str[1], str.size() - 1, &amp;mb);
    std::cout &lt;&lt; &quot;The remaining &quot; &lt;&lt; str.size() - 1 &lt;&lt; &quot; bytes of &quot; &lt;&lt; str
              &lt;&lt; &quot; hold &quot; &lt;&lt; len2 &lt;&lt; &quot; bytes of the multibyte character
&quot;;
    std::cout &lt;&lt; &quot;Attempting to call mbrlen() in the middle of &quot; &lt;&lt; str
              &lt;&lt; &quot; while in initial shift state returns &quot;
              &lt;&lt; (int)mbrlen(&amp;str[1], str.size(), &amp;mb) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;The first 1 byte of 水 is an incomplete multibyte char (mbrlen returns -2)<br />
&nbsp;<wbr>&nbsp;The remaining 2 bytes of 水 hold 2 bytes of the multibyte character<br />
&nbsp;<wbr>&nbsp;Attempting to call mbrlen() in the middle of 水 while in initial shift state returns -1</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the next multibyte character to wide character, given state<br />
mbrtowc <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of bytes in the next multibyte character<br />
mblen <i>(function)</i><br />
do_length calculates the length of the externT string that would be consumed by conversion into given internT buffer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
