---
title: "stdfilesystempathstringstdfilesystempathwstringstdfilesystempathu8stringstdfilesystempathu16stringstdfilesystempathu32string(3)"
name: "stdfilesystempathstringstdfilesystempathwstringstdfilesystempathu8stringstdfilesystempathu16stringstdfilesystempathu32string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathstringstdfilesystempathwstringstdfilesystempathu8stringstdfilesystempathu16stringstdfilesystempathu32string/"
---

std::filesystem::path::string,std::filesystem::path::wstring,std::filesystem::path::u8string,std::filesystem::path::u16string,std::filesystem::path::u32string - std::filesystem::path::string,std::filesystem::path::wstring,std::filesystem::path::u8string,std::filesystem::path::u16string,std::filesystem::path::u32string

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits = std::char_traits&lt;CharT&gt;,

          class Alloc = std::allocator&lt;CharT&gt;&gt;
(1)(since C++ 17)

    std::basic_string&lt;CharT, Traits, Alloc&gt;

    string(const Alloc &amp;a = Alloc()) const;

std::string string() const;

std::wstring wstring() const;

std::u16string u16string() const;

std::u32string u32string() const;
(2)(since C++ 17)

    std::string u8string() const;
(since C++ 17)(3)(until C++ 20)

    std::u8string u8string() const;
(since C++ 20)</code></pre> 
Returns the internal pathname in native pathname format, converted to specific string type. Conversion, if any, is performed as follows: 
* If path::value_type is char, conversion, if any, is system-dependent. This is the case on typical POSIX systems (such as Linux), where native encoding is UTF-8 and string() performs no conversion. 
* Otherwise, if path::value_type is wchar_t, conversion, if any, is unspecified. This is the case on Windows, where wchar_t is 16 bit and the native encoding is UTF-16. 
* Otherwise, if path::value_type is char16_t, native encoding is UTF-16 and the conversion method is unspecified. 
* Otherwise, if path::value_type is char32_t, native encoding is UTF-32 and the conversion method is unspecified. 
* Otherwise, if path::value_type is char8_t, native encoding is UTF-8 and the conversion method is unspecified. 
1) All memory allocations are performed by a. 
3) The result encoding in the case of u8string() is always UTF-8. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The internal pathname in native pathname format, converted to specified string type. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#ifdef _MSC_VER

#include &lt;io.h&gt;

#include &lt;fcntl.h&gt;

#else

#include &lt;locale&gt;

#include &lt;clocale&gt;

#endif

#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{

#ifdef _MSC_VER
    _setmode(_fileno(stderr), _O_WTEXT);

#else
    std::setlocale(LC_ALL, &quot;&quot;);
    std::locale::global(std::locale(&quot;&quot;));
    std::cout.imbue(std::locale());
    std::wcerr.imbue(std::locale());

#endif
    fs::path p = fs::u8path(u8&quot;要らない.txt&quot;);
    std::ofstream(p) &lt;&lt; &quot;File contents&quot;; // Prior to LWG2676 uses operator string_type()
                                         // on MSVC, where string_type is wstring, only
                                         // works due to non-standard extension.
                                         // Post-LWG2676 uses new fstream constructors
                                         // native string representation can be used with OS APIs
    if (std::FILE *f =

#ifdef _MSC_VER
            _wfopen(p.c_str(), L&quot;r&quot;)

#else
            std::fopen(p.c_str(), &quot;r&quot;)

#endif
    ) {
        int ch;
        while ((ch = fgetc(f)) != EOF)
            putchar(ch);
        std::fclose(f);
    }
    // multibyte and wide representation can be used for output
    std::cout &lt;&lt; &quot;\nFile name in narrow multibyte encoding: &quot; &lt;&lt; p.string() &lt;&lt; '\n';
    std::wcerr &lt;&lt; &quot;File name in wide encoding: &quot; &lt;&lt; p.wstring() &lt;&lt; '\n';
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
