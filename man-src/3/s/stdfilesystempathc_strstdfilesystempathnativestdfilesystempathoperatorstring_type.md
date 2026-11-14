---
title: "stdfilesystempathc_strstdfilesystempathnativestdfilesystempathoperatorstring_type(3)"
name: "stdfilesystempathc_strstdfilesystempathnativestdfilesystempathoperatorstring_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathc_strstdfilesystempathnativestdfilesystempathoperatorstring_type/"
description: "std::filesystem::path::c_str,std::filesystem::path::native,std::filesystem::path::operatorstring_type() – std::filesystem::path::c_str,std::filesystem::path::native,std::filesystem::path::operators..."
---

<p>std::filesystem::path::c_str,std::filesystem::path::native,std::filesystem::path::operatorstring_type() &#8211; std::filesystem::path::c_str,std::filesystem::path::native,std::filesystem::path::operatorstring_type()</p>
<h2>Synopsis</h2>
<pre><code>const value_type *c_str() const noexcept;
(1)(since C++ 17)

    const string_type &amp;native() const noexcept;
(2)(since C++ 17)

operator string_type() const;
(3)(since C++ 17)</code></pre>
<p>Accesses the native path name as a character string.<br />
1) Equivalent to native().c_str().<br />
2) Returns the native-format representation of the pathname by reference.<br />
3) Returns the native-format representation of the pathname by value. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The native string representation of the pathname, using native syntax, native character type, and native character encoding. This string is suitable for use with OS APIs. </p>
<h2>Notes</h2>
<p>The conversion function <code>(3)</code> is provided so that APIs that accept std::basic_string file names can use pathnames with no changes to code. </p>
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
<p>string<br />
wstring returns the path in native pathname format converted to a string<br />
u8string <i>(public member function)</i><br />
u16string<br />
u32string<br />
generic_string<br />
generic_wstring returns the path in generic pathname format converted to a string<br />
generic_u8string <i>(public member function)</i><br />
generic_u16string<br />
generic_u32string </p>
