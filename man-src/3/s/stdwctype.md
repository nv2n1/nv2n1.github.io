---
title: "stdwctype(3)"
name: "stdwctype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwctype/"
---

std::wctype - std::wctype

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwctype&gt;

    std::wctype_t wctype(const char *str);</code></pre> 
Constructs a value of type std::wctype_t that describes a LC_CTYPE category of wide character classification. It may be one of the standard classification categories, or a locale-specific category, such as &quot;jkanji&quot;. 

<h2>Parameters</h2>

str - C string holding the name of the desired category 

 
The following values of str are supported in all C locales: 

 
value of str effect 
&quot;alnum&quot; identifies the category used by std::iswalnum 
&quot;alpha&quot; identifies the category used by std::iswalpha 
&quot;blank&quot; identifies the category used by std::iswblank <i>(C++11)</i> 
&quot;cntrl&quot; identifies the category used by std::iswcntrl 
&quot;digit&quot; identifies the category used by std::iswdigit 
&quot;graph&quot; identifies the category used by std::iswgraph 
&quot;lower&quot; identifies the category used by std::iswlower 
&quot;print&quot; identifies the category used by std::iswprint 
&quot;space&quot; identifies the category used by std::iswspace 
&quot;upper&quot; identifies the category used by std::iswupper 
&quot;xdigit&quot; identifies the category used by std::iswxdigit

<h2>Return value</h2>

std::wctype_t object suitable for use with std::iswctype to classify wide characters according to the named category of the current C locale or zero if str does not name a category supported by the current C locale. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;classifies a wide character according to the specified LC_CTYPE category 
iswctype <i>(function)</i> 
