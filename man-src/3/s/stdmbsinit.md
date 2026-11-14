---
title: "stdmbsinit(3)"
name: "stdmbsinit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmbsinit/"
---

std::mbsinit - std::mbsinit

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    int mbsinit(const std::mbstate_t *ps);</code></pre> 
If ps is not a null pointer, the mbsinit function determines whether the pointed-to std::mbstate_t object describes the initial conversion state. 

<h2>Notes</h2>

Although a zero-initialized std::mbstate_t always represents the initial conversion state, there may be other values of std::mbstate_t that also represent the initial conversion state. 

<h2>Parameters</h2>

ps - pointer to the std::mbstate_t object to examine

<h2>Return value</h2>

0 if ps is not a null pointer and does not represent the initial conversion state, nonzero value otherwise. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;clocale&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;cwchar&gt;
int main()

{
    // allow mbrlen() to work with UTF-8 multibyte encoding
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    // UTF-8 narrow multibyte encoding
    std::string str = u8&quot;水&quot;; // or u8&quot;\u6c34&quot; or &quot;\xe6\xb0\xb4&quot;
    std::mbstate_t mb = std::mbstate_t();
    (void)std::mbrlen(&amp;str[0], 1, &amp;mb);
    if (!std::mbsinit(&amp;mb)) {
        std::cout &lt;&lt; &quot;After processing the first 1 byte of &quot; &lt;&lt; str
                  &lt;&lt; &quot; the conversion state is not initial\n&quot;;
    }
    (void)std::mbrlen(&amp;str[1], str.size() - 1, &amp;mb);
    if (std::mbsinit(&amp;mb)) {
        std::cout &lt;&lt; &quot;After processing the remaining 2 bytes of &quot; &lt;&lt; str
                  &lt;&lt; &quot;, the conversion state is initial conversion state\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;After processing the first 1 byte of 水 the conversion state is not initial 
&nbsp;<wbr>&nbsp;After processing the remaining 2 bytes of 水, the conversion state is initial conversion state

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;conversion state information necessary to iterate multibyte character strings 
mbstate_t <i>(class)</i> 
