---
title: "stdfilesystempathstringstdfilesystempathwstring(3)"
name: "stdfilesystempathstringstdfilesystempathwstring"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathstringstdfilesystempathwstring/"
---

std::filesystem::path::string,std::filesystem::path::wstring, - std::filesystem::path::string,std::filesystem::path::wstring,

<h2>Synopsis</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::filesystem::path::u32string <pre><code>template &lt;class CharT, class Traits =

                           std::char_traits&lt;CharT&gt;,
          (since

           class Alloc = std::allocator&lt;CharT&gt; &gt; (1)C++ 17)

              std::basic_string&lt;CharT, Traits, Alloc&gt;
                  string(const Alloc &amp;a = Alloc()) const;

std::string string() const;

std::wstring wstring() const;

std::u16string u16string() const;

std::u32string u32string() const;
(2)(since(since

              std::string u8string() const;
          C++ 17) C++ 17)(3)(until
                                 C++ 20)

    std::u8string u8string() const;
(since
     C++ 20)</code></pre> 
Returns the internal pathname in native pathname format, converted to specific 
string type. Conversion, if any, is performed as follows: 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If path::value_type is char, conversion, if any, is system-dependent. This is 
&nbsp;<wbr>the case on typical POSIX systems&nbsp;<wbr>(such as Linux), where native encoding is 
&nbsp;<wbr>UTF-8 and string()&nbsp;<wbr>performs no conversion. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, if path::value_type is wchar_t, conversion, if any, is unspecified. 
&nbsp;<wbr>This is the case on Windows, where wchar_t is 16 bit and the native encoding is 
&nbsp;<wbr>UTF-16. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, if path::value_type is char16_t, native encoding is UTF-16 and the 
&nbsp;<wbr>conversion method is unspecified. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, if path::value_type is char32_t, native encoding is UTF-32 and the 
&nbsp;<wbr>conversion method is unspecified. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, if path::value_type is char8_t, native encoding is UTF-8 and the 
&nbsp;<wbr>conversion method is unspecified. 
1)&nbsp;<wbr>All memory allocations are performed by a. 
3)&nbsp;<wbr>The result encoding in the case of u8string()&nbsp;<wbr>is always UTF-8. 

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

&nbsp;<wbr>File contents 
&nbsp;<wbr>File name in narrow multibyte encoding:&nbsp;<wbr>要らない.txt 
&nbsp;<wbr>File name in wide encoding:&nbsp;<wbr>要らない.txt

<h2>See also</h2>

generic_string 
generic_wstring&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>returns the path in generic pathname format converted to a string 
generic_u8string&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i> 
generic_u16string 
generic_u32string 
