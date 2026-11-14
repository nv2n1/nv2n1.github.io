---
title: "std-codecvt-7(3)"
name: "std-codecvt-7"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-7/"
description: "std::wcstombs – std::wcstombs"
---

<h2 class="name">NAME</h2>
<p> std::wcstombs &#8211; std::wcstombs</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cstdlib&gt;<br />
std::size_t wcstombs( char* dst, const wchar_t* src, std::size_t len); </p>
<p>Converts a sequence of wide characters from the array whose first element is pointed to by src to its narrow multibyte representation that begins in the initial shift state. Converted characters are stored in the successive elements of the char array pointed to by dst. No more than len bytes are written to the destination array.<br />
Each character is converted as if by a call to std::wctomb, except that the wctomb&#8217;s conversion state is unaffected. The conversion stops if: </p>
<p>* The null character was converted and stored.<br />
* A wchar_t was found that does not correspond to a valid character in the current C locale.<br />
* The next multibyte character to be stored would exceed len. </p>
<h2>Notes</h2>
<p>In most implementations, this function updates a global static object of type std::mbstate_t as it processes through the string, and cannot be called simultaneously by two threads, std::wcsrtombs should be used in such cases.<br />
POSIX specifies a common extension: if dst is a null pointer, this function returns the number of bytes that would be written to dst, if converted. Similar behavior is standard for std::wcsrtombs. </p>
<h2>Parameters</h2>
<p>dst &#8211; pointer to narrow character array where the multibyte character will be stored<br />
src &#8211; pointer to the first element of a null-terminated wide string to convert<br />
len &#8211; number of byte available in the array pointed to by dst </p>
<h2>Return value</h2>
<p>On success, returns the number of bytes (including any shift sequences, but excluding the terminating &#8216;
