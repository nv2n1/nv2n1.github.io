---
title: "stdfilesystemu8path(3)"
name: "stdfilesystemu8path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemu8path/"
description: "std::filesystem::u8path – std::filesystem::u8path"
---

<p>std::filesystem::u8path &#8211; std::filesystem::u8path</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;filesystem&gt;<br />
template&lt; class Source &gt; <code>(1)</code> <i>(since C++17)</i><br />
path u8path( const Source&amp; source ); (deprecated in C++20)<br />
template&lt; class InputIt &gt; <code>(2)</code> <i>(since C++17)</i><br />
path u8path( InputIt first, InputIt last ); (deprecated in C++20)<br />
Constructs a path p from a UTF-8 encoded sequence of chars, supplied either as an std::string, or as std::string_view, or as a null-terminated multibyte string, or as a [first, last) iterator pair.<br />
* If path::value_type is char and native encoding is UTF-8, constructs a path directly as if by path(source) or path(first, last). Note: this is the typical situation of a POSIX system that uses Unicode, such as Linux.<br />
* Otherwise, if path::value_type is wchar_t and native encoding is UTF-16 (this is the situation on Windows), or if path::value_type is char16_t (native encoding guaranteed UTF-16) or char32_t (native encoding guaranteed UTF-32), then first converts the UTF-8 character sequence to a temporary string tmp of type path::string_type and then the new path is constructed as if by path(tmp)<br />
* Otherwise (for non-UTF-8 narrow character encodings and for non-UTF-16 wchar_t), first converts the UTF-8 character sequence to a temporary UTF-32-encoded string tmp of type std::u32string, and then the new path is constructed as if by path(tmp) (this path is taken on a POSIX system with a non-Unicode multibyte or single-byte encoded filesystem) </p>
<h2>Parameters</h2>
<p>source &#8211; a UTF-8 encoded std::string, std::string_view, a pointer to a null-terminated multibyte string, or an input iterator with char value type that points to a null-terminated multibyte string<br />
first, last &#8211; pair of LegacyInputIterators that specify a UTF-8 encoded character sequence</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator.<br />
&#8211;<br />
The value type of InputIt must be char</p>
<h2>Return value</h2>
<p>The path constructed from the input string after conversion from UTF-8 to the filesystem&#8217;s native character encoding. </p>
<h2>Exceptions</h2>
<p>May throw std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>On systems where native path format differs from the generic path format (neither Windows nor POSIX systems are examples of such OSes), if the argument to this function is using generic format, it will be converted to native. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cstdio&gt;

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
    std::cout &lt;&lt; &quot;
File name in narrow multibyte encoding: &quot; &lt;&lt; p.string() &lt;&lt; '
';
    std::wcerr &lt;&lt; &quot;File name in wide encoding: &quot; &lt;&lt; p.wstring() &lt;&lt; '
';
    fs::remove(p);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;File contents<br />
&nbsp;<wbr>&nbsp;File name in narrow multibyte encoding: 要らない.txt<br />
&nbsp;<wbr>&nbsp;File name in wide encoding: 要らない.txt</p>
<h2>See also</h2>
<p>path represents a path<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
<i>(C++17)</i> </p>
