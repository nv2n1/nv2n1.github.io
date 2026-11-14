---
title: "std-codecvt-6(3)"
name: "std-codecvt-6"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-6/"
description: "std::wcsrtombs – std::wcsrtombs"
---

<h2 id="name">NAME</h2>
<p>std::wcsrtombs &#8211; std::wcsrtombs</p>
<h2 id="synopsis">SYNOPSIS</h2>
<p>Defined in header <code>&lt;cwchar&gt;</code></p>
<pre><code>std::size_t wcsrtombs(char* dst,
                       const wchar_t** src,
                       std::size_t len,
                       std::mbstate_t* ps);</code></pre>
<p>Converts a sequence of wide characters from the array whose first element is pointed to by *src to its narrow multibyte representation that begins in the conversion state described by *ps. If dst is not null, converted characters are stored in the successive elements of the char array pointed to by dst. No more than len bytes are written to the destination array.</p>
<p>Each character is converted as if by a call to <code>std::wcrtomb</code>. The conversion stops if:</p>
<ul>
<li>The null character was converted and stored. src is set to NULL and *ps represents the initial shift state.</li>
<li>A wchar_t was found that does not correspond to a valid character in the current C locale. src is set to point at the first unconverted wide character.</li>
<li>The next multibyte character to be stored would exceed len. src is set to point at the first unconverted wide character. This condition is not checked if dst==NULL.</li>
</ul>
<h2 id="parameters">Parameters</h2>
<dl>
<dt>dst</dt>
<dd>pointer to narrow character array where the multibyte characters will be stored</dd>
<dt>src</dt>
<dd>pointer to pointer to the first element of a null-terminated wide string</dd>
<dt>len</dt>
<dd>number of bytes available in the array pointed to by dst</dd>
<dt>ps</dt>
<dd>pointer to the conversion state object</dd>
</dl>
<h2 id="return-value">Return value</h2>
<p>On success, returns the number of bytes (including any shift sequences, but excluding the terminating '\0') written to the character array whose first element is pointed to by dst. If dst==NULL, returns the number of bytes that would have been written (again, excluding the terminating null character '\0').</p>
<p>On conversion error (if invalid wide character was encountered), returns <code>static_cast&lt;std::size_t&gt;(-1)</code>, stores EILSEQ in errno, and leaves *ps in unspecified state.</p>
<h2 id="example">Example</h2>
<pre><code>// Run this code
#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;clocale&gt;
#include &lt;string&gt;
#include &lt;cwchar&gt;

void print_wide(const wchar_t* wstr)
{
    std::mbstate_t state = std::mbstate_t();
    std::size_t len = 1 + std::wcsrtombs(nullptr, &amp;wstr, 0, &amp;state);
    std::vector&lt;char&gt; mbstr(len);
    std::wcsrtombs(&amp;mbstr[0], &amp;wstr, mbstr.size(), &amp;state);
    std::cout &lt;&lt; "multibyte string: " &lt;&lt; &amp;mbstr[0] &lt;&lt; '\n';
    std::cout &lt;&lt; "Length, including '\\0': " &lt;&lt; mbstr.size() &lt;&lt; '\n';
}

int main()
{
    std::setlocale(LC_ALL, "en_US.utf8");
    // UTF-8 narrow multibyte encoding
    const wchar_t* wstr = L"zß水\U0001d10b"; // or L"zß水"
    print_wide(wstr);
}</code></pre>
<h2 id="output">Output</h2>
<pre><code>multibyte string: zß水
Length, including '\0': 11</code></pre>
<h2 id="see-also">See also</h2>
<dl>
<dt>wcrtomb (function)</dt>
<dd>converts a wide character to its multibyte representation, given state</dd>
<dt>mbsrtowcs (function)</dt>
<dd>converts a narrow multibyte character string to wide string, given state</dd>
<dt>do_out (virtual protected member function of <code>std::codecvt&lt;InternT,ExternT,State&gt;</code>)</dt>
<dd>converts a string from internT to externT, such as when writing to file</dd>
</dl>
<h2 id="index">Index</h2>
