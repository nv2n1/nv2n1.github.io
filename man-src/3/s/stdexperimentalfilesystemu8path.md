---
title: "stdexperimentalfilesystemu8path(3)"
name: "stdexperimentalfilesystemu8path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemu8path/"
---

std::experimental::filesystem::u8path - std::experimental::filesystem::u8path

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    template &lt;class Source&gt;
    (1)(filesystem TS)

        path u8path(const Source &amp;source);

template &lt;class InputIt&gt;
(2)(filesystem TS)

    path u8path(InputIt first, InputIt last);</code></pre> 
Constructs a path p from a UTF-8 encoded sequence of chars, supplied either as an std::string, or as a null-terminated multibyte string, or as a [first, last) iterator pair. 
* If path::value_type is char and native encoding is UTF-8, constructs a path directly as if by path(source) or path(first, last). Note: this is the typical situation of a POSIX system that uses Unicode, such as Linux. 
* Otherwise, if path::value_type is wchar_t and native encoding is UTF-16 (this is the situation on Windows), or if path::value_type is char16_t (native encoding guaranteed UTF-16) or char32_t (native encoding guaranteed UTF-32), then first converts the UTF-8 character sequence to a temporary string tmp of type path::string_type and then the new path is constructed as if by path(tmp) 
* Otherwise (for non-UTF-8 narrow character encodings and for non-UTF-16 wchar_t), first converts the UTF-8 character sequence to a temporary UTF-32-encoded string tmp of type std::u32string, and then the new path is constructed as if by path(tmp) (this path is taken on a POSIX system with a non-Unicode multibyte or single-byte encoded filesystem) 

<h2>Parameters</h2>

source - an UTF-8 encoded std::string, pointer to a null-terminated multibyte string, or an input iterator with char value type that points to a null-terminated multibyte string 
first, last - pair of LegacyInputIterators that specify a UTF-8 encoded character sequence

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
The value type of InputIt must be char

<h2>Return value</h2>

The path constructed from the input string after conversion from UTF-8 to the filesystem's native character encoding. 

<h2>Exceptions</h2>

May throw filesystem_error on underlying OS API errors or std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

On systems where native path format differs from the generic path format (neither Windows nor POSIX systems are examples of such OSes), if the argument to this function is using generic format, it will be converted to native. 

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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represents a path 
path <i>(class)</i> 
