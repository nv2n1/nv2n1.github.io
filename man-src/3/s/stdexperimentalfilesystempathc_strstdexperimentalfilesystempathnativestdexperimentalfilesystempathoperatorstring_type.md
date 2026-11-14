---
title: "stdexperimentalfilesystempathc_strstdexperimentalfilesystempathnativestdexperimentalfilesystempathoperatorstring_type(3)"
name: "stdexperimentalfilesystempathc_strstdexperimentalfilesystempathnativestdexperimentalfilesystempathoperatorstring_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathc_strstdexperimentalfilesystempathnativestdexperimentalfilesystempathoperatorstring_type/"
description: "std::experimental::filesystem::path::c_str,std::experimental::filesystem::path::native,std::experimental::filesystem::path::operatorstring_type() – std::experimental::filesystem::path::c_str,std::e..."
---

<p>std::experimental::filesystem::path::c_str,std::experimental::filesystem::path::native,std::experimental::filesystem::path::operatorstring_type() &#8211; std::experimental::filesystem::path::c_str,std::experimental::filesystem::path::native,std::experimental::filesystem::path::operatorstring_type()</p>
<h2>Synopsis</h2>
<pre><code>const value_type *c_str() const;
(1)(filesystem TS)

    const string_type &amp;native() const;
(2)(filesystem TS)

operator string_type() const;
(3)(filesystem TS)</code></pre>
<p>Accesses the native path name as a character string.<br />
1) Equivalent to native().c_str().<br />
2) Returns the native string representation of the pathname by reference.<br />
3) Returns the native string representation of the pathname by value. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The native string representation of the pathname, using native syntax, native character type, and native character encoding. This string is suitable for use with OS APIs. </p>
<h2>Exceptions</h2>
<p>1,2)<br />
noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>The conversion function <code>(3)</code> is provided so that standard file-opening APIs that accept std::basic_string file names, such as the std::ifstream constructor, can use pathnames with no changes to code: fs::path p = &quot;/tmp/text.txt&quot;;</p>
<p>std::ifstream f(p);</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cstdio&gt;

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
    std::cout &lt;&lt; &quot;
File name in narrow multibyte encoding: &quot;
              &lt;&lt; p.string() &lt;&lt; '
';
    std::wcerr.imbue(std::locale());
    std::wcerr &lt;&lt; &quot;File name in wide encoding: &quot;
               &lt;&lt; p.wstring() &lt;&lt; '
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
