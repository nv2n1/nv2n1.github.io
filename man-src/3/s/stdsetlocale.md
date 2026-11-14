---
title: "stdsetlocale(3)"
name: "stdsetlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsetlocale/"
---

std::setlocale - std::setlocale

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;clocale&gt;

    char *setlocale(int category, const char *locale);</code></pre> 
The setlocale function installs the specified system locale or its portion as the new C locale. The modifications remain in effect and influences the execution of all locale-sensitive C library functions until the next call to setlocale. If locale is a null pointer, setlocale queries the current C locale without modifying it. 

<h2>Parameters</h2>

category - locale category identifier, one of the LC_xxx macros. May be 0. 
locale - system-specific locale identifier. Can be &quot;&quot; for the user-preferred locale or &quot;C&quot; for the minimal locale

<h2>Return value</h2>

Pointer to a narrow null-terminated string identifying the C locale after applying the changes, if any, or null pointer on failure. 
A copy of the returned string along with the category used in this call to std::setlocale may be used later in the program to restore the locale back to the state at the end of this call. 

<h2>Notes</h2>

During program startup, the equivalent of std::setlocale(LC_ALL, &quot;C&quot;); is executed before any user code is run. 
Although the return type is char*, modifying the pointed-to characters is undefined behavior. 
Because setlocale modifies global state which affects execution of locale-dependent functions, it is undefined behavior to call it from one thread, while another thread is executing any of the following functions: std::fprintf, std::isprint, std::iswdigit, std::localeconv, std::tolower, std::fscanf, std::ispunct, std::iswgraph, std::mblen, std::toupper, std::isalnum, std::isspace, std::iswlower, std::mbstowcs, std::towlower, std::isalpha, std::isupper, std::iswprint, std::mbtowc, std::towupper, std::isblank, std::iswalnum, std::iswpunct, std::setlocale, std::wcscoll, std::iscntrl, std::iswalpha, std::iswspace, std::strcoll, std::wcstod, std::isdigit, std::iswblank, std::iswupper, std::strerror, std::wcstombs, std::isgraph, std::iswcntrl, std::iswxdigit, std::strtod, std::wcsxfrm, std::islower, std::iswctype, std::isxdigit. 
POSIX also defines a locale named &quot;POSIX&quot;, which is always accessible and is exactly equivalent to the default minimal &quot;C&quot; locale. 
POSIX also specifies that the returned pointer, not just the contents of the pointed-to string, may be invalidated by subsequent calls to setlocale. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;clocale&gt;

#include &lt;ctime&gt;

#include &lt;cwchar&gt;
int main()

{
    // the C locale will be UTF-8 enabled English;
    // decimal dot will be German
    // date and time formatting will be Japanese
    std::setlocale(LC_ALL, &quot;en_US.UTF-8&quot;);
    std::setlocale(LC_NUMERIC, &quot;de_DE.UTF-8&quot;);
    std::setlocale(LC_TIME, &quot;ja_JP.UTF-8&quot;);
    wchar_t str[100];
    std::time_t t = std::time(NULL);
    std::wcsftime(str, 100, L&quot;%A %c&quot;, std::localtime(&amp;t));
    std::wprintf(L&quot;Number: %.2f\nDate: %Ls\n&quot;, 3.14, str);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Number: 3,14 
&nbsp;<wbr>&nbsp;Date: 月曜日 2011年12月19日 18時04分40秒

<h2>See also</h2>

LC_ALL 
LC_COLLATE locale categories for std::setlocale 
LC_CTYPE (macro constant) 
LC_MONETARY 
LC_NUMERIC 
LC_TIME 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set of polymorphic facets that encapsulate cultural differences 
locale <i>(class)</i> 
