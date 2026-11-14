---
title: "stdmblen(3)"
name: "stdmblen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmblen/"
---

std::mblen - std::mblen

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    int mblen(const char *s, std::size_t n);</code></pre> 
Determines the size, in bytes, of the multibyte character whose first byte is pointed to by s. 
If s is a null pointer, resets the global conversion state and determines whether shift sequences are used. 
This function is equivalent to the call std::mbtowc((wchar_t*)0, s, n), except that conversion state of std::mbtowc is unaffected. 

<h2>Notes</h2>

Each call to mblen updates the internal global conversion state (a static object of type std::mbstate_t, only known to this function). If the multibyte encoding uses shift states, care must be taken to avoid backtracking or multiple scans. In any case, multiple threads should not call mblen without synchronization: std::mbrlen may be used instead. 

<h2>Parameters</h2>

s - pointer to the multibyte character 
n - limit on the number of bytes in s that can be examined

<h2>Return value</h2>

If s is not a null pointer, returns the number of bytes that are contained in the multibyte character or -1 if the first bytes pointed to by s do not form a valid multibyte character or 0 if s is pointing at the null charcter '\0'. 
If s is a null pointer, resets its internal conversion state to represent the initial shift state and returns 0 if the current multibyte encoding is not state-dependent (does not use shift sequences) or a non-zero value if the current multibyte encoding is state-dependent (uses shift sequences). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;clocale&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;cstdlib&gt;

#include &lt;stdexcept&gt;
// the number of characters in a multibyte string is the sum of mblen()'s

// note: the simpler approach is std::mbstowcs(NULL, s.c_str(), s.size())

std::size_t strlen_mb(const std::string &amp;s)

{
    std::size_t result = 0;
    const char *ptr = s.data();
    const char *end = ptr + s.size();
    std::mblen(NULL, 0); // reset the conversion state
    while (ptr &lt; end) {
        int next = std::mblen(ptr, end - ptr);
        if (next == -1) {
            throw std::runtime_error(&quot;strlen_mb(): conversion error&quot;);
        }
        ptr += next;
        ++result;
    }
    return result;
}
int main()

{
    // allow mblen() to work with UTF-8 multibyte encoding
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    // UTF-8 narrow multibyte encoding
    std::string str = u8&quot;z\u00df\u6c34\U0001f34c&quot;; // or u8&quot;zß水&#x1f34c;&quot;
    std::cout &lt;&lt; str &lt;&lt; &quot; is &quot; &lt;&lt; str.size() &lt;&lt; &quot; bytes, but only &quot;
              &lt;&lt; strlen_mb(str) &lt;&lt; &quot; characters\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;zß水 is 10 bytes, but only 4 characters

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the next multibyte character to wide character 
mbtowc <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of bytes in the next multibyte character, given state 
mbrlen <i>(function)</i> 
