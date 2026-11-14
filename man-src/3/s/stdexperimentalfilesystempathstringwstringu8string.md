---
title: "stdexperimentalfilesystempathstringwstringu8string(3)"
name: "stdexperimentalfilesystempathstringwstringu8string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathstringwstringu8string/"
---

std::experimental::filesystem::path::string,wstring,u8string,... - std::experimental::filesystem::path::string,wstring,u8string,...

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits = std::char_traits&lt;CharT&gt;,

          class Alloc = std::allocator&lt;CharT&gt;&gt;
(1)(filesystem TS)

    std::basic_string&lt;CharT, Traits, Alloc&gt;

    string(const Alloc &amp;a = Alloc()) const;

std::string string() const;

std::wstring wstring() const;

std::string u8string() const;
(2)(filesystem TS)

    std::u16string u16string() const;

std::u32string u32string() const;</code></pre> 
Returns the internal pathname in native pathname format, converted to specific string type. Conversion, if any, is specified in todo. 
1) All memory allocations are performed by a. 
2) The encoding in the case of u8string() is always UTF-8. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The internal pathname in native pathname format, converted to specified string type. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;clocale&gt;

#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    fs::path p = fs::u8path(u8&quot;要らない.txt&quot;);
    // native string representation can be used with OS APIs
    std::ofstream(p) &lt;&lt; &quot;File contents&quot;; // this uses operator string()
    if (std::FILE *f = std::fopen(p.c_str(), &quot;r&quot;)) {
        int ch;
        while ((ch = fgetc(f)) != EOF)
            putchar(ch);
        std::fclose(f);
    }
    // multibyte and wide representation can be used for output
    std::cout.imbue(std::locale());
    std::cout &lt;&lt; &quot;\nFile name in narrow multibyte encoding: &quot;
              &lt;&lt; p.string() &lt;&lt; '\n';
    std::wcerr.imbue(std::locale());
    std::wcerr &lt;&lt; &quot;File name in wide encoding: &quot;
               &lt;&lt; p.wstring() &lt;&lt; '\n';
    fs::remove(p);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;File contents 
&nbsp;<wbr>&nbsp;File name in narrow multibyte encoding: 要らない.txt 
&nbsp;<wbr>&nbsp;File name in wide encoding: 要らない.txt

<h2>See also</h2>

generic_string 
generic_wstring returns the path in generic pathname format converted to a string 
generic_u8string <i>(public member function)</i> 
generic_u16string 
generic_u32string 
