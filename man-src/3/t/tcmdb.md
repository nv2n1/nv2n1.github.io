---
title: "tcmdb(3)"
name: "tcmdb"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcmdb/"
description: "tcutil – the utility API"
---

<p>tcutil &#8211; the utility API</p>
<h2>Description</h2>
<p>The utility API is a set of routines to handle records on memory easily. Especially, extensible string, array list, hash map, and ordered tree are useful. To use the utility API, include `<code>tcutil.h</code>&#8216; and related standard header files. Usually, write the following description near the front of a source file. </p>
<pre><code>#include &lt;tcutil.h&gt;

#include &lt;stdlib.h&gt;

#include &lt;time.h&gt;

#include &lt;stdbool.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<p> Objects whose type is pointer to `<code>TCXSTR</code>&#8216; are used for extensible string. An extensible string object is created with the function `<code>tcxstrnew</code>&#8216; and is deleted with the function `<code>tcxstrdel</code>&#8216;. Objects whose type is pointer to `<code>TCLIST</code>&#8216; are used for array list. A list object is created with the function `<code>tclistnew</code>&#8216; and is deleted with the function `<code>tclistdel</code>&#8216;. Objects whose type is pointer to `<code>TCMAP</code>&#8216; are used for hash map. A map object is created with the function `<code>tcmapnew</code>&#8216; and is deleted with the function `<code>tcmapdel</code>&#8216;. Objects whose type is pointer to `<code>TCTREE</code>&#8216; are used for ordered tree. A tree object is created with the function `<code>tctreenew</code>&#8216; and is deleted with the function `<code>tctreedel</code>&#8216;. To avoid memory leak, it is important to delete every object when it is no longer in use. </p>
<h2>Api Of Basic Utilities</h2>
<p>The constant `tcversion&#8217; is the string containing the version information. </p>
<dl>
<dd><code>extern const char *tcversion;</code></dl>
<p> The variable `tcfatalfunc&#8217; is the pointer to the call back function for handling a fatal error. </p>
<dl>
<dd><code>extern void (*tcfatalfunc)(const char *);</code></p>
<dl>
<dd>The argument specifies the error message.</dl>
<dl>
<dd>The initial value of this variable is `NULL&#8217;. If the value is `NULL&#8217;, the default function is called when a fatal error occurs. A fatal error occurs when memory allocation is failed.</dl>
</dl>
<p> The function `tcmalloc&#8217; is used in order to allocate a region on memory. </p>
<dl>
<dd><code>void *tcmalloc(size_t </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the pointer to the allocated region.</dl>
<dl>
<dd>This function handles failure of memory allocation implicitly. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tccalloc&#8217; is used in order to allocate a nullified region on memory. </p>
<dl>
<dd><code>void *tccalloc(size_t </code><i>nmemb</i><code>, size_t </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>nmemb</i>&#8216; specifies the number of elements.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of each element.</dl>
<dl>
<dd>The return value is the pointer to the allocated nullified region.</dl>
<dl>
<dd>This function handles failure of memory allocation implicitly. Because the region of the return value is allocated with the `calloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcrealloc&#8217; is used in order to re-allocate a region on memory. </p>
<dl>
<dd><code>void *tcrealloc(void *</code><i>ptr</i><code>, size_t </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the pointer to the re-allocated region.</dl>
<dl>
<dd>This function handles failure of memory allocation implicitly. Because the region of the return value is allocated with the `realloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmemdup&#8217; is used in order to duplicate a region on memory. </p>
<dl>
<dd><code>void *tcmemdup(const void *</code><i>ptr</i><code>, size_t </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the pointer to the allocated region of the duplicate.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcstrdup&#8217; is used in order to duplicate a string on memory. </p>
<dl>
<dd><code>char *tcstrdup(const void *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string.</dl>
<dl>
<dd>The return value is the allocated string equivalent to the specified string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcfree&#8217; is used in order to free a region on memory. </p>
<dl>
<dd><code>void tcfree(void *</code><i>ptr</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region. If it is `NULL&#8217;, this function has no effect.</dl>
<dl>
<dd>Although this function is just a wrapper of `free&#8217; call, this is useful in applications using another package of the `malloc&#8217; series.</dl>
</dl>
<h2>Api Of Extensible String</h2>
<p>The function `tcxstrnew&#8217; is used in order to create an extensible string object. </p>
<dl>
<dd><code>TCXSTR *tcxstrnew(void);</code></p>
<dl>
<dd>The return value is the new extensible string object.</dl>
</dl>
<p> The function `tcxstrnew2&#8242; is used in order to create an extensible string object from a character string. </p>
<dl>
<dd><code>TCXSTR *tcxstrnew2(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of the initial content.</dl>
<dl>
<dd>The return value is the new extensible string object containing the specified string.</dl>
</dl>
<p> The function `tcxstrnew3&#8242; is used in order to create an extensible string object with the initial allocation size. </p>
<dl>
<dd><code>TCXSTR *tcxstrnew3(int </code><i>asiz</i><code>);</code></p>
<dl>
<dd>`<i>asiz</i>&#8216; specifies the initial allocation size.</dl>
<dl>
<dd>The return value is the new extensible string object.</dl>
</dl>
<p> The function `tcxstrdup&#8217; is used in order to copy an extensible string object. </p>
<dl>
<dd><code>TCXSTR *tcxstrdup(const TCXSTR *</code><i>xstr</i><code>);</code></p>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object.</dl>
<dl>
<dd>The return value is the new extensible string object equivalent to the specified object.</dl>
</dl>
<p> The function `tcxstrdel&#8217; is used in order to delete an extensible string object. </p>
<dl>
<dd><code>void tcxstrdel(TCXSTR *</code><i>xstr</i><code>);</code></p>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object.</dl>
<dl>
<dd>Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tcxstrcat&#8217; is used in order to concatenate a region to the end of an extensible string object. </p>
<dl>
<dd><code>void tcxstrcat(TCXSTR *</code><i>xstr</i><code>, const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region to be appended.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
</dl>
<p> The function `tcxstrcat2&#8242; is used in order to concatenate a character string to the end of an extensible string object. </p>
<dl>
<dd><code>void tcxstrcat2(TCXSTR *</code><i>xstr</i><code>, const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object.</dl>
<dl>
<dd>`<i>str</i>&#8216; specifies the string to be appended.</dl>
</dl>
<p> The function `tcxstrptr&#8217; is used in order to get the pointer of the region of an extensible string object. </p>
<dl>
<dd><code>const void *tcxstrptr(const TCXSTR *</code><i>xstr</i><code>);</code></p>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object.</dl>
<dl>
<dd>The return value is the pointer of the region of the object.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string.</dl>
</dl>
<p> The function `tcxstrsize&#8217; is used in order to get the size of the region of an extensible string object. </p>
<dl>
<dd><code>int tcxstrsize(const TCXSTR *</code><i>xstr</i><code>);</code></p>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object.</dl>
<dl>
<dd>The return value is the size of the region of the object.</dl>
</dl>
<p> The function `tcxstrclear&#8217; is used in order to clear an extensible string object. </p>
<dl>
<dd><code>void tcxstrclear(TCXSTR *</code><i>xstr</i><code>);</code></p>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object.</dl>
<dl>
<dd>The internal buffer of the object is cleared and the size is set zero.</dl>
</dl>
<p> The function `tcxstrprintf&#8217; is used in order to perform formatted output into an extensible string object. </p>
<dl>
<dd><code>void tcxstrprintf(TCXSTR *</code><i>xstr</i><code>, const char *</code><i>format</i><code>, &#8230;);</code></p>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object.</dl>
<dl>
<dd>`<i>format</i>&#8216; specifies the printf-like format string. The conversion character `%&#8217; can be used with such flag characters as `s&#8217;, `d&#8217;, `o&#8217;, `u&#8217;, `x&#8217;, `X&#8217;, `c&#8217;, `e&#8217;, `E&#8217;, `f&#8217;, `g&#8217;, `G&#8217;, `@&#8217;, `?&#8217;, `b&#8217;, and `%&#8217;. `@&#8217; works as with `s&#8217; but escapes meta characters of XML. `?&#8217; works as with `s&#8217; but escapes meta characters of URL. `b&#8217; converts an integer to the string as binary numbers. The other conversion character work as with each original.</dl>
<dl>
<dd>The other arguments are used according to the format string.</dl>
</dl>
<p> The function `tcsprintf&#8217; is used in order to allocate a formatted string on memory. </p>
<dl>
<dd><code>char *tcsprintf(const char *</code><i>format</i><code>, &#8230;);</code></p>
<dl>
<dd>`<i>format</i>&#8216; specifies the printf-like format string. The conversion character `%&#8217; can be used with such flag characters as `s&#8217;, `d&#8217;, `o&#8217;, `u&#8217;, `x&#8217;, `X&#8217;, `c&#8217;, `e&#8217;, `E&#8217;, `f&#8217;, `g&#8217;, `G&#8217;, `@&#8217;, `?&#8217;, `b&#8217;, and `%&#8217;. `@&#8217; works as with `s&#8217; but escapes meta characters of XML. `?&#8217; works as with `s&#8217; but escapes meta characters of URL. `b&#8217; converts an integer to the string as binary numbers. The other conversion character work as with each original.</dl>
<dl>
<dd>The other arguments are used according to the format string.</dl>
<dl>
<dd>The return value is the pointer to the region of the result string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<h2>Api Of Array List</h2>
<p>The function `tclistnew&#8217; is used in order to create a list object. </p>
<dl>
<dd><code>TCLIST *tclistnew(void);</code></p>
<dl>
<dd>The return value is the new list object.</dl>
</dl>
<p> The function `tclistnew2&#8242; is used in order to create a list object with expecting the number of elements. </p>
<dl>
<dd><code>TCLIST *tclistnew2(int </code><i>anum</i><code>);</code></p>
<dl>
<dd>`<i>anum</i>&#8216; specifies the number of elements expected to be stored in the list.</dl>
<dl>
<dd>The return value is the new list object.</dl>
</dl>
<p> The function `tclistnew3&#8242; is used in order to create a list object with initial string elements. </p>
<dl>
<dd><code>TCLIST *tclistnew3(const char *</code><i>str</i><code>, &#8230;);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of the first element.</dl>
<dl>
<dd>The other arguments are other elements. They should be trailed by a `NULL&#8217; argument.</dl>
<dl>
<dd>The return value is the new list object.</dl>
</dl>
<p> The function `tclistdup&#8217; is used in order to copy a list object. </p>
<dl>
<dd><code>TCLIST *tclistdup(const TCLIST *</code><i>list</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>The return value is the new list object equivalent to the specified object.</dl>
</dl>
<p> The function `tclistdel&#8217; is used in order to delete a list object. </p>
<dl>
<dd><code>void tclistdel(TCLIST *</code><i>list</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tclistnum&#8217; is used in order to get the number of elements of a list object. </p>
<dl>
<dd><code>int tclistnum(const TCLIST *</code><i>list</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>The return value is the number of elements of the list.</dl>
</dl>
<p> The function `tclistval&#8217; is used in order to get the pointer to the region of an element of a list object. </p>
<dl>
<dd><code>const void *tclistval(const TCLIST *</code><i>list</i><code>, int </code><i>index</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>index</i>&#8216; specifies the index of the element.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the value.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. If `index&#8217; is equal to or more than the number of elements, the return value is `NULL&#8217;.</dl>
</dl>
<p> The function `tclistval2&#8242; is used in order to get the string of an element of a list object. </p>
<dl>
<dd><code>const char *tclistval2(const TCLIST *</code><i>list</i><code>, int </code><i>index</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>index</i>&#8216; specifies the index of the element.</dl>
<dl>
<dd>The return value is the string of the value.</dl>
<dl>
<dd>If `index&#8217; is equal to or more than the number of elements, the return value is `NULL&#8217;.</dl>
</dl>
<p> The function `tclistpush&#8217; is used in order to add an element at the end of a list object. </p>
<dl>
<dd><code>void tclistpush(TCLIST *</code><i>list</i><code>, const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of the new element.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
</dl>
<p> The function `tclistpush2&#8242; is used in order to add a string element at the end of a list object. </p>
<dl>
<dd><code>void tclistpush2(TCLIST *</code><i>list</i><code>, const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of the new element.</dl>
</dl>
<p> The function `tclistpop&#8217; is used in order to remove an element of the end of a list object. </p>
<dl>
<dd><code>void *tclistpop(TCLIST *</code><i>list</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the removed element.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. If the list is empty, the return value is `NULL&#8217;.</dl>
</dl>
<p> The function `tclistpop2&#8242; is used in order to remove a string element of the end of a list object. </p>
<dl>
<dd><code>char *tclistpop2(TCLIST *</code><i>list</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>The return value is the string of the removed element.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. If the list is empty, the return value is `NULL&#8217;.</dl>
</dl>
<p> The function `tclistunshift&#8217; is used in order to add an element at the top of a list object. </p>
<dl>
<dd><code>void tclistunshift(TCLIST *</code><i>list</i><code>, const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of the new element.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
</dl>
<p> The function `tclistunshift2&#8242; is used in order to add a string element at the top of a list object. </p>
<dl>
<dd><code>void tclistunshift2(TCLIST *</code><i>list</i><code>, const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of the new element.</dl>
</dl>
<p> The function `tclistshift&#8217; is used in order to remove an element of the top of a list object. </p>
<dl>
<dd><code>void *tclistshift(TCLIST *</code><i>list</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the removed element.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. If the list is empty, the return value is `NULL&#8217;.</dl>
</dl>
<p> The function `tclistshift2&#8242; is used in order to remove a string element of the top of a list object. </p>
<dl>
<dd><code>char *tclistshift2(TCLIST *</code><i>list</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>The return value is the string of the removed element.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. If the list is empty, the return value is `NULL&#8217;.</dl>
</dl>
<p> The function `tclistinsert&#8217; is used in order to add an element at the specified location of a list object. </p>
<dl>
<dd><code>void tclistinsert(TCLIST *</code><i>list</i><code>, int </code><i>index</i><code>, const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>index</i>&#8216; specifies the index of the new element.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of the new element.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>If `index&#8217; is equal to or more than the number of elements, this function has no effect.</dl>
</dl>
<p> The function `tclistinsert2&#8242; is used in order to add a string element at the specified location of a list object. </p>
<dl>
<dd><code>void tclistinsert2(TCLIST *</code><i>list</i><code>, int </code><i>index</i><code>, const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>index</i>&#8216; specifies the index of the new element.</dl>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of the new element.</dl>
<dl>
<dd>If `index&#8217; is equal to or more than the number of elements, this function has no effect.</dl>
</dl>
<p> The function `tclistremove&#8217; is used in order to remove an element at the specified location of a list object. </p>
<dl>
<dd><code>void *tclistremove(TCLIST *</code><i>list</i><code>, int </code><i>index</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>index</i>&#8216; specifies the index of the element to be removed.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the removed element.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. If `index&#8217; is equal to or more than the number of elements, no element is removed and the return value is `NULL&#8217;.</dl>
</dl>
<p> The function `tclistremove2&#8242; is used in order to remove a string element at the specified location of a list object. </p>
<dl>
<dd><code>char *tclistremove2(TCLIST *</code><i>list</i><code>, int </code><i>index</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>index</i>&#8216; specifies the index of the element to be removed.</dl>
<dl>
<dd>The return value is the string of the removed element.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. If `index&#8217; is equal to or more than the number of elements, no element is removed and the return value is `NULL&#8217;.</dl>
</dl>
<p> The function `tclistover&#8217; is used in order to overwrite an element at the specified location of a list object. </p>
<dl>
<dd><code>void tclistover(TCLIST *</code><i>list</i><code>, int </code><i>index</i><code>, const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>index</i>&#8216; specifies the index of the element to be overwritten.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of the new content.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the new content.</dl>
<dl>
<dd>If `index&#8217; is equal to or more than the number of elements, this function has no effect.</dl>
</dl>
<p> The function `tclistover2&#8242; is used in order to overwrite a string element at the specified location of a list object. </p>
<dl>
<dd><code>void tclistover2(TCLIST *</code><i>list</i><code>, int </code><i>index</i><code>, const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>index</i>&#8216; specifies the index of the element to be overwritten.</dl>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of the new content.</dl>
<dl>
<dd>If `index&#8217; is equal to or more than the number of elements, this function has no effect.</dl>
</dl>
<p> The function `tclistsort&#8217; is used in order to sort elements of a list object in lexical order. </p>
<dl>
<dd><code>void tclistsort(TCLIST *</code><i>list</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
</dl>
<p> The function `tclistlsearch&#8217; is used in order to search a list object for an element using liner search. </p>
<dl>
<dd><code>int tclistlsearch(const TCLIST *</code><i>list</i><code>, const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the index of a corresponding element or -1 if there is no corresponding element.</dl>
<dl>
<dd>If two or more elements correspond, the former returns.</dl>
</dl>
<p> The function `tclistbsearch&#8217; is used in order to search a list object for an element using binary search. </p>
<dl>
<dd><code>int tclistbsearch(const TCLIST *</code><i>list</i><code>, const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object. It should be sorted in lexical order.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the index of a corresponding element or -1 if there is no corresponding element.</dl>
<dl>
<dd>If two or more elements correspond, which returns is not defined.</dl>
</dl>
<p> The function `tclistclear&#8217; is used in order to clear a list object. </p>
<dl>
<dd><code>void tclistclear(TCLIST *</code><i>list</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>All elements are removed.</dl>
</dl>
<p> The function `tclistdump&#8217; is used in order to serialize a list object into a byte array. </p>
<dl>
<dd><code>void *tclistdump(const TCLIST *</code><i>list</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the result serial region.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tclistload&#8217; is used in order to create a list object from a serialized byte array. </p>
<dl>
<dd><code>TCLIST *tclistload(const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of serialized byte array.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is a new list object.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<h2>Api Of Hash Map</h2>
<p>The function `tcmapnew&#8217; is used in order to create a map object. </p>
<dl>
<dd><code>TCMAP *tcmapnew(void);</code></p>
<dl>
<dd>The return value is the new map object.</dl>
</dl>
<p> The function `tcmapnew2&#8242; is used in order to create a map object with specifying the number of the buckets. </p>
<dl>
<dd><code>TCMAP *tcmapnew2(uint32_t </code><i>bnum</i><code>);</code></p>
<dl>
<dd>`<i>bnum</i>&#8216; specifies the number of the buckets.</dl>
<dl>
<dd>The return value is the new map object.</dl>
</dl>
<p> The function `tcmapnew3&#8242; is used in order to create a map object with initial string elements. </p>
<dl>
<dd><code>TCMAP *tcmapnew3(const char *</code><i>str</i><code>, &#8230;);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of the first element.</dl>
<dl>
<dd>The other arguments are other elements. They should be trailed by a `NULL&#8217; argument.</dl>
<dl>
<dd>The return value is the new map object.</dl>
<dl>
<dd>The key and the value of each record are situated one after the other.</dl>
</dl>
<p> The function `tcmapdup&#8217; is used in order to copy a map object. </p>
<dl>
<dd><code>TCMAP *tcmapdup(const TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>The return value is the new map object equivalent to the specified object.</dl>
</dl>
<p> The function `tcmapdel&#8217; is used in order to delete a map object. </p>
<dl>
<dd><code>void tcmapdel(TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tcmapput&#8217; is used in order to store a record into a map object. </p>
<dl>
<dd><code>void tcmapput(TCMAP *</code><i>map</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If a record with the same key exists in the map, it is overwritten.</dl>
</dl>
<p> The function `tcmapput2&#8242; is used in order to store a string record into a map object. </p>
<dl>
<dd><code>void tcmapput2(TCMAP *</code><i>map</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If a record with the same key exists in the map, it is overwritten.</dl>
</dl>
<p> The function `tcmapputkeep&#8217; is used in order to store a new record into a map object. </p>
<dl>
<dd><code>bool tcmapputkeep(TCMAP *</code><i>map</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the map, this function has no effect.</dl>
</dl>
<p> The function `tcmapputkeep2&#8242; is used in order to store a new string record into a map object. </p>
<dl>
<dd><code>bool tcmapputkeep2(TCMAP *</code><i>map</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the map, this function has no effect.</dl>
</dl>
<p> The function `tcmapputcat&#8217; is used in order to concatenate a value at the end of the value of the existing record in a map object. </p>
<dl>
<dd><code>void tcmapputcat(TCMAP *</code><i>map</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcmapputcat2&#8242; is used in order to concatenate a string value at the end of the value of the existing record in a map object. </p>
<dl>
<dd><code>void tcmapputcat2(TCMAP *</code><i>map</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcmapout&#8217; is used in order to remove a record of a map object. </p>
<dl>
<dd><code>bool tcmapout(TCMAP *</code><i>map</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tcmapout2&#8242; is used in order to remove a string record of a map object. </p>
<dl>
<dd><code>bool tcmapout2(TCMAP *</code><i>map</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tcmapget&#8217; is used in order to retrieve a record in a map object. </p>
<dl>
<dd><code>const void *tcmapget(const TCMAP *</code><i>map</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned when no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string.</dl>
</dl>
<p> The function `tcmapget2&#8242; is used in order to retrieve a string record in a map object. </p>
<dl>
<dd><code>const char *tcmapget2(const TCMAP *</code><i>map</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the string of the value of the corresponding record. `NULL&#8217; is returned when no record corresponds.</dl>
</dl>
<p> The function `tcmapmove&#8217; is used in order to move a record to the edge of a map object. </p>
<dl>
<dd><code>bool tcmapmove(TCMAP *</code><i>map</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, bool </code><i>head</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of a key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>head</i>&#8216; specifies the destination which is the head if it is true or the tail if else.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tcmapmove2&#8242; is used in order to move a string record to the edge of a map object. </p>
<dl>
<dd><code>bool tcmapmove2(TCMAP *</code><i>map</i><code>, const char *</code><i>kstr</i><code>, bool </code><i>head</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of a key.</dl>
<dl>
<dd>`<i>head</i>&#8216; specifies the destination which is the head if it is true or the tail if else.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tcmapiterinit&#8217; is used in order to initialize the iterator of a map object. </p>
<dl>
<dd><code>void tcmapiterinit(TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>The iterator is used in order to access the key of every record stored in the map object.</dl>
</dl>
<p> The function `tcmapiternext&#8217; is used in order to get the next key of the iterator of a map object. </p>
<dl>
<dd><code>const void *tcmapiternext(TCMAP *</code><i>map</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record can be fetched from the iterator.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. The order of iteration is assured to be the same as the stored order.</dl>
</dl>
<p> The function `tcmapiternext2&#8242; is used in order to get the next key string of the iterator of a map object. </p>
<dl>
<dd><code>const char *tcmapiternext2(TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record can be fetched from the iterator.</dl>
<dl>
<dd>The order of iteration is assured to be the same as the stored order.</dl>
</dl>
<p> The function `tcmaprnum&#8217; is used in order to get the number of records stored in a map object. </p>
<dl>
<dd><code>uint64_t tcmaprnum(const TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>The return value is the number of the records stored in the map object.</dl>
</dl>
<p> The function `tcmapmsiz&#8217; is used in order to get the total size of memory used in a map object. </p>
<dl>
<dd><code>uint64_t tcmapmsiz(const TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>The return value is the total size of memory used in a map object.</dl>
</dl>
<p> The function `tcmapkeys&#8217; is used in order to create a list object containing all keys in a map object. </p>
<dl>
<dd><code>TCLIST *tcmapkeys(const TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>The return value is the new list object containing all keys in the map object.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcmapvals&#8217; is used in order to create a list object containing all values in a map object. </p>
<dl>
<dd><code>TCLIST *tcmapvals(const TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>The return value is the new list object containing all values in the map object.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcmapaddint&#8217; is used in order to add an integer to a record in a map object. </p>
<dl>
<dd><code>int tcmapaddint(TCMAP *</code><i>map</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>The return value is the summation value.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as an integer and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcmapadddouble&#8217; is used in order to add a real number to a record in a map object. </p>
<dl>
<dd><code>double tcmapadddouble(TCMAP *</code><i>map</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>The return value is the summation value.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as a real number and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcmapclear&#8217; is used in order to clear a map object. </p>
<dl>
<dd><code>void tcmapclear(TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>All records are removed.</dl>
</dl>
<p> The function `tcmapcutfront&#8217; is used in order to remove front records of a map object. </p>
<dl>
<dd><code>void tcmapcutfront(TCMAP *</code><i>map</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the number of records to be removed.</dl>
</dl>
<p> The function `tcmapdump&#8217; is used in order to serialize a map object into a byte array. </p>
<dl>
<dd><code>void *tcmapdump(const TCMAP *</code><i>map</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the result serial region.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmapload&#8217; is used in order to create a map object from a serialized byte array. </p>
<dl>
<dd><code>TCMAP *tcmapload(const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of serialized byte array.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is a new map object.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tcmapnew&#8217;, it should be deleted with the function `tcmapdel&#8217; when it is no longer in use.</dl>
</dl>
<h2>Api Of Ordered Tree</h2>
<p>The function `tctreenew&#8217; is used in order to create a tree object. </p>
<dl>
<dd><code>TCTREE *tctreenew(void);</code></p>
<dl>
<dd>The return value is the new tree object.</dl>
</dl>
<p> The function `tctreenew2&#8242; is used in order to create a tree object with specifying the custom comparison function. </p>
<dl>
<dd><code>TCTREE *tctreenew2(TCCMP </code><i>cmp</i><code>, void *</code><i>cmpop</i><code>);</code></p>
<dl>
<dd>`<i>cmp</i>&#8216; specifies the pointer to the custom comparison function. It receives five parameters. The first parameter is the pointer to the region of one key. The second parameter is the size of the region of one key. The third parameter is the pointer to the region of the other key. The fourth parameter is the size of the region of the other key. The fifth parameter is the pointer to the optional opaque object. It returns positive if the former is big, negative if the latter is big, 0 if both are equivalent.</dl>
<dl>
<dd>`<i>cmpop</i>&#8216; specifies an arbitrary pointer to be given as a parameter of the comparison function. If it is not needed, `NULL&#8217; can be specified.</dl>
<dl>
<dd>The return value is the new tree object.</dl>
<dl>
<dd>The default comparison function compares keys of two records by lexical order. The functions `tccmplexical&#8217; (dafault), `tccmpdecimal&#8217;, `tccmpint32&#8242;, and `tccmpint64&#8242; are built-in.</dl>
</dl>
<p> The function `tctreedup&#8217; is used in order to copy a tree object. </p>
<dl>
<dd><code>TCTREE *tctreedup(const TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>The return value is the new tree object equivalent to the specified object.</dl>
</dl>
<p> The function `tctreedel&#8217; is used in order to delete a tree object. </p>
<dl>
<dd><code>void tctreedel(TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`tree&#8217; specifies the tree object.</dl>
<dl>
<dd>Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tctreeput&#8217; is used in order to store a record into a tree object. </p>
<dl>
<dd><code>void tctreeput(TCTREE *</code><i>tree</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If a record with the same key exists in the tree, it is overwritten.</dl>
</dl>
<p> The function `tctreeput2&#8242; is used in order to store a string record into a tree object. </p>
<dl>
<dd><code>void tctreeput2(TCTREE *</code><i>tree</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If a record with the same key exists in the tree, it is overwritten.</dl>
</dl>
<p> The function `tctreeputkeep&#8217; is used in order to store a new record into a tree object. </p>
<dl>
<dd><code>bool tctreeputkeep(TCTREE *</code><i>tree</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the tree, this function has no effect.</dl>
</dl>
<p> The function `tctreeputkeep2&#8242; is used in order to store a new string record into a tree object. </p>
<dl>
<dd><code>bool tctreeputkeep2(TCTREE *</code><i>tree</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the tree, this function has no effect.</dl>
</dl>
<p> The function `tctreeputcat&#8217; is used in order to concatenate a value at the end of the value of the existing record in a tree object. </p>
<dl>
<dd><code>void tctreeputcat(TCTREE *</code><i>tree</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tctreeputcat2&#8242; is used in order to concatenate a string value at the end of the value of the existing record in a tree object. </p>
<dl>
<dd><code>void tctreeputcat2(TCTREE *</code><i>tree</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tctreeout&#8217; is used in order to remove a record of a tree object. </p>
<dl>
<dd><code>bool tctreeout(TCTREE *</code><i>tree</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tctreeout2&#8242; is used in order to remove a string record of a tree object. </p>
<dl>
<dd><code>bool tctreeout2(TCTREE *</code><i>tree</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tctreeget&#8217; is used in order to retrieve a record in a tree object. </p>
<dl>
<dd><code>const void *tctreeget(TCTREE *</code><i>tree</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned when no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string.</dl>
</dl>
<p> The function `tctreeget2&#8242; is used in order to retrieve a string record in a tree object. </p>
<dl>
<dd><code>const char *tctreeget2(TCTREE *</code><i>tree</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the string of the value of the corresponding record. `NULL&#8217; is returned when no record corresponds.</dl>
</dl>
<p> The function `tctreeiterinit&#8217; is used in order to initialize the iterator of a tree object. </p>
<dl>
<dd><code>void tctreeiterinit(TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>The iterator is used in order to access the key of every record stored in the tree object.</dl>
</dl>
<p> The function `tctreeiternext&#8217; is used in order to get the next key of the iterator of a tree object. </p>
<dl>
<dd><code>const void *tctreeiternext(TCTREE *</code><i>tree</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record can be fetched from the iterator.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. The order of iteration is assured to be ascending of the keys.</dl>
</dl>
<p> The function `tctreeiternext2&#8242; is used in order to get the next key string of the iterator of a tree object. </p>
<dl>
<dd><code>const char *tctreeiternext2(TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record can be fetched from the iterator.</dl>
<dl>
<dd>The order of iteration is assured to be ascending of the keys.</dl>
</dl>
<p> The function `tctreernum&#8217; is used in order to get the number of records stored in a tree object. </p>
<dl>
<dd><code>uint64_t tctreernum(const TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>The return value is the number of the records stored in the tree object.</dl>
</dl>
<p> The function `tctreemsiz&#8217; is used in order to get the total size of memory used in a tree object. </p>
<dl>
<dd><code>uint64_t tctreemsiz(const TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>The return value is the total size of memory used in a tree object.</dl>
</dl>
<p> The function `tctreekeys&#8217; is used in order to create a list object containing all keys in a tree object. </p>
<dl>
<dd><code>TCLIST *tctreekeys(const TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>The return value is the new list object containing all keys in the tree object.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tctreevals&#8217; is used in order to create a list object containing all values in a tree object. </p>
<dl>
<dd><code>TCLIST *tctreevals(const TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>The return value is the new list object containing all values in the tree object.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tctreeaddint&#8217; is used in order to add an integer to a record in a tree object. </p>
<dl>
<dd><code>int tctreeaddint(TCTREE *</code><i>tree</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>The return value is the summation value.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as an integer and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tctreeadddouble&#8217; is used in order to add a real number to a record in a tree object. </p>
<dl>
<dd><code>double tctreeadddouble(TCTREE *</code><i>tree</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>The return value is the summation value.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as a real number and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tctreeclear&#8217; is used in order to clear a tree object. </p>
<dl>
<dd><code>void tctreeclear(TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>All records are removed.</dl>
</dl>
<p> The function `tctreecutfringe&#8217; is used in order to remove fringe records of a tree object. </p>
<dl>
<dd><code>void tctreecutfringe(TCTREE *</code><i>tree</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the number of records to be removed.</dl>
</dl>
<p> The function `tctreedump&#8217; is used in order to serialize a tree object into a byte array. </p>
<dl>
<dd><code>void *tctreedump(const TCTREE *</code><i>tree</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the result serial region.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tctreeload&#8217; is used in order to create a tree object from a serialized byte array. </p>
<dl>
<dd><code>TCTREE *tctreeload(const void *</code><i>ptr</i><code>, int </code><i>size</i><code>, TCCMP </code><i>cmp</i><code>, void *</code><i>cmpop</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of serialized byte array.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>cmp</i>&#8216; specifies the pointer to the custom comparison function.</dl>
<dl>
<dd>`<i>cmpop</i>&#8216; specifies an arbitrary pointer to be given as a parameter of the comparison function.</dl>
<dl>
<dd>If it is not needed, `NULL&#8217; can be specified.</dl>
<dl>
<dd>The return value is a new tree object.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tctreenew&#8217;, it should be deleted with the function `tctreedel&#8217; when it is no longer in use.</dl>
</dl>
<h2>Api Of On-Memory Hash Database</h2>
<p>The function `tcmdbnew&#8217; is used in order to create an on-memory hash database object. </p>
<dl>
<dd><code>TCMDB *tcmdbnew(void);</code></p>
<dl>
<dd>The return value is the new on-memory hash database object.</dl>
<dl>
<dd>The object can be shared by plural threads because of the internal mutex.</dl>
</dl>
<p> The function `tcmdbnew2&#8242; is used in order to create an on-memory hash database object with specifying the number of the buckets. </p>
<dl>
<dd><code>TCMDB *tcmdbnew2(uint32_t </code><i>bnum</i><code>);</code></p>
<dl>
<dd>`<i>bnum</i>&#8216; specifies the number of the buckets.</dl>
<dl>
<dd>The return value is the new on-memory hash database object.</dl>
<dl>
<dd>The object can be shared by plural threads because of the internal mutex.</dl>
</dl>
<p> The function `tcmdbdel&#8217; is used in order to delete an on-memory hash database object. </p>
<dl>
<dd><code>void tcmdbdel(TCMDB *</code><i>mdb</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
</dl>
<p> The function `tcmdbput&#8217; is used in order to store a record into an on-memory hash database object. </p>
<dl>
<dd><code>void tcmdbput(TCMDB *</code><i>mdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcmdbput2&#8242; is used in order to store a string record into an on-memory hash database object. </p>
<dl>
<dd><code>void tcmdbput2(TCMDB *</code><i>mdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcmdbputkeep&#8217; is used in order to store a new record into an on-memory hash database object. </p>
<dl>
<dd><code>bool tcmdbputkeep(TCMDB *</code><i>mdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcmdbputkeep2&#8242; is used in order to store a new string record into an on-memory hash database object. </p>
<dl>
<dd><code>bool tcmdbputkeep2(TCMDB *</code><i>mdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcmdbputcat&#8217; is used in order to concatenate a value at the end of the existing record in an on-memory hash database. </p>
<dl>
<dd><code>void tcmdbputcat(TCMDB *</code><i>mdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcmdbputcat2&#8242; is used in order to concatenate a string at the end of the existing record in an on-memory hash database. </p>
<dl>
<dd><code>void tcmdbputcat2(TCMDB *</code><i>mdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcmdbout&#8217; is used in order to remove a record of an on-memory hash database object. </p>
<dl>
<dd><code>bool tcmdbout(TCMDB *</code><i>mdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tcmdbout2&#8242; is used in order to remove a string record of an on-memory hash database object. </p>
<dl>
<dd><code>bool tcmdbout2(TCMDB *</code><i>mdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tcmdbget&#8217; is used in order to retrieve a record in an on-memory hash database object. </p>
<dl>
<dd><code>void *tcmdbget(TCMDB *</code><i>mdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned when no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmdbget2&#8242; is used in order to retrieve a string record in an on-memory hash database object. </p>
<dl>
<dd><code>char *tcmdbget2(TCMDB *</code><i>mdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the string of the value of the corresponding record. `NULL&#8217; is returned when no record corresponds.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmdbvsiz&#8217; is used in order to get the size of the value of a record in an on-memory hash database object. </p>
<dl>
<dd><code>int tcmdbvsiz(TCMDB *</code><i>mdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcmdbvsiz2&#8242; is used in order to get the size of the value of a string record in an on-memory hash database object. </p>
<dl>
<dd><code>int tcmdbvsiz2(TCMDB *</code><i>mdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcmdbiterinit&#8217; is used in order to initialize the iterator of an on-memory hash database object. </p>
<dl>
<dd><code>void tcmdbiterinit(TCMDB *</code><i>mdb</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>The iterator is used in order to access the key of every record stored in the on-memory hash database.</dl>
</dl>
<p> The function `tcmdbiternext&#8217; is used in order to get the next key of the iterator of an on-memory hash database object. </p>
<dl>
<dd><code>void *tcmdbiternext(TCMDB *</code><i>mdb</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return</dl>
<dl>
<dd>value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record can be fetched from the iterator.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. The order of iteration is assured to be the same as the stored order.</dl>
</dl>
<p> The function `tcmdbiternext2&#8242; is used in order to get the next key string of the iterator of an on-memory hash database object. </p>
<dl>
<dd><code>char *tcmdbiternext2(TCMDB *</code><i>mdb</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record can be fetched from the iterator.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. The order of iteration is assured to be the same as the stored order.</dl>
</dl>
<p> The function `tcmdbfwmkeys&#8217; is used in order to get forward matching keys in an on-memory hash database object. </p>
<dl>
<dd><code>TCLIST *tcmdbfwmkeys(TCMDB *</code><i>mdb</i><code>, const void *</code><i>pbuf</i><code>, int </code><i>psiz</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>pbuf</i>&#8216; specifies the pointer to the region of the prefix.</dl>
<dl>
<dd>`<i>psiz</i>&#8216; specifies the size of the region of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tcmdbfwmkeys2&#8242; is used in order to get forward matching string keys in an on-memory hash database object. </p>
<dl>
<dd><code>TCLIST *tcmdbfwmkeys2(TCMDB *</code><i>mdb</i><code>, const char *</code><i>pstr</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>pstr</i>&#8216; specifies the string of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tcmdbrnum&#8217; is used in order to get the number of records stored in an on-memory hash database object. </p>
<dl>
<dd><code>uint64_t tcmdbrnum(TCMDB *</code><i>mdb</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>The return value is the number of the records stored in the database.</dl>
</dl>
<p> The function `tcmdbmsiz&#8217; is used in order to get the total size of memory used in an on-memory hash database object. </p>
<dl>
<dd><code>uint64_t tcmdbmsiz(TCMDB *</code><i>mdb</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>The return value is the total size of memory used in the database.</dl>
</dl>
<p> The function `tcmdbaddint&#8217; is used in order to add an integer to a record in an on-memory hash database object. </p>
<dl>
<dd><code>int tcmdbaddint(TCMDB *</code><i>mdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>The return value is the summation value.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as an integer and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcmdbadddouble&#8217; is used in order to add a real number to a record in an on-memory hash database object. </p>
<dl>
<dd><code>double tcmdbadddouble(TCMDB *</code><i>mdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>The return value is the summation value.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as a real number and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcmdbvanish&#8217; is used in order to clear an on-memory hash database object. </p>
<dl>
<dd><code>void tcmdbvanish(TCMDB *</code><i>mdb</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>All records are removed.</dl>
</dl>
<p> The function `tcmdbcutfront&#8217; is used in order to remove front records of an on-memory hash database object. </p>
<dl>
<dd><code>void tcmdbcutfront(TCMDB *</code><i>mdb</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>mdb</i>&#8216; specifies the on-memory hash database object.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the number of records to be removed.</dl>
</dl>
<h2>Api Of On-Memory Tree Database</h2>
<p>The function `tcndbnew&#8217; is used in order to create an on-memory tree database object. </p>
<dl>
<dd><code>TCNDB *tcndbnew(void);</code></p>
<dl>
<dd>The return value is the new on-memory tree database object.</dl>
<dl>
<dd>The object can be shared by plural threads because of the internal mutex.</dl>
</dl>
<p> The function `tcndbnew2&#8242; is used in order to create an on-memory tree database object with specifying the custom comparison function. </p>
<dl>
<dd><code>TCNDB *tcndbnew2(TCCMP </code><i>cmp</i><code>, void *</code><i>cmpop</i><code>);</code></p>
<dl>
<dd>`<i>cmp</i>&#8216; specifies the pointer to the custom comparison function.</dl>
<dl>
<dd>`<i>cmpop</i>&#8216; specifies an arbitrary pointer to be given as a parameter of the comparison function. If it is not needed, `NULL&#8217; can be specified.</dl>
<dl>
<dd>The return value is the new on-memory tree database object.</dl>
<dl>
<dd>The default comparison function compares keys of two records by lexical order. The functions `tccmplexical&#8217; (dafault), `tccmpdecimal&#8217;, `tccmpint32&#8242;, and `tccmpint64&#8242; are built-in. The object can be shared by plural threads because of the internal mutex.</dl>
</dl>
<p> The function `tcndbdel&#8217; is used in order to delete an on-memory tree database object. </p>
<dl>
<dd><code>void tcndbdel(TCNDB *</code><i>ndb</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
</dl>
<p> The function `tcndbput&#8217; is used in order to store a record into an on-memory tree database object. </p>
<dl>
<dd><code>void tcndbput(TCNDB *</code><i>ndb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcndbput2&#8242; is used in order to store a string record into an on-memory tree database object. </p>
<dl>
<dd><code>void tcndbput2(TCNDB *</code><i>ndb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcndbputkeep&#8217; is used in order to store a new record into an on-memory tree database object. </p>
<dl>
<dd><code>bool tcndbputkeep(TCNDB *</code><i>ndb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcndbputkeep2&#8242; is used in order to store a new string record into an on-memory tree database object. </p>
<dl>
<dd><code>bool tcndbputkeep2(TCNDB *</code><i>ndb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcndbputcat&#8217; is used in order to concatenate a value at the end of the existing record in an on-memory tree database. </p>
<dl>
<dd><code>void tcndbputcat(TCNDB *</code><i>ndb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcndbputcat2&#8242; is used in order to concatenate a string at the end of the existing record in an on-memory tree database. </p>
<dl>
<dd><code>void tcndbputcat2(TCNDB *</code><i>ndb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcndbout&#8217; is used in order to remove a record of an on-memory tree database object. </p>
<dl>
<dd><code>bool tcndbout(TCNDB *</code><i>ndb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tcndbout2&#8242; is used in order to remove a string record of an on-memory tree database object. </p>
<dl>
<dd><code>bool tcndbout2(TCNDB *</code><i>ndb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is true. False is returned when no record corresponds to the specified key.</dl>
</dl>
<p> The function `tcndbget&#8217; is used in order to retrieve a record in an on-memory tree database object. </p>
<dl>
<dd><code>void *tcndbget(TCNDB *</code><i>ndb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned when no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcndbget2&#8242; is used in order to retrieve a string record in an on-memory tree database object. </p>
<dl>
<dd><code>char *tcndbget2(TCNDB *</code><i>ndb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the string of the value of the corresponding record. `NULL&#8217; is returned when no record corresponds.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcndbvsiz&#8217; is used in order to get the size of the value of a record in an on-memory tree database object. </p>
<dl>
<dd><code>int tcndbvsiz(TCNDB *</code><i>ndb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcndbvsiz2&#8242; is used in order to get the size of the value of a string record in an on-memory tree database object. </p>
<dl>
<dd><code>int tcndbvsiz2(TCNDB *</code><i>ndb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcndbiterinit&#8217; is used in order to initialize the iterator of an on-memory tree database object. </p>
<dl>
<dd><code>void tcndbiterinit(TCNDB *</code><i>ndb</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>The iterator is used in order to access the key of every record stored in the on-memory database.</dl>
</dl>
<p> The function `tcndbiternext&#8217; is used in order to get the next key of the iterator of an on-memory tree database object. </p>
<dl>
<dd><code>void *tcndbiternext(TCNDB *</code><i>ndb</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record can be fetched from the iterator.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. The order of iteration is assured to be the same as the stored order.</dl>
</dl>
<p> The function `tcndbiternext2&#8242; is used in order to get the next key string of the iterator of an on-memory tree database object. </p>
<dl>
<dd><code>char *tcndbiternext2(TCNDB *</code><i>ndb</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record can be fetched from the iterator.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. The order of iteration is assured to be the same as the stored order.</dl>
</dl>
<p> The function `tcndbfwmkeys&#8217; is used in order to get forward matching keys in an on-memory tree database object. </p>
<dl>
<dd><code>TCLIST *tcndbfwmkeys(TCNDB *</code><i>ndb</i><code>, const void *</code><i>pbuf</i><code>, int </code><i>psiz</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>pbuf</i>&#8216; specifies the pointer to the region of the prefix.</dl>
<dl>
<dd>`<i>psiz</i>&#8216; specifies the size of the region of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcndbfwmkeys2&#8242; is used in order to get forward matching string keys in an on-memory tree database object. </p>
<dl>
<dd><code>TCLIST *tcndbfwmkeys2(TCNDB *</code><i>ndb</i><code>, const char *</code><i>pstr</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>pstr</i>&#8216; specifies the string of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcndbrnum&#8217; is used in order to get the number of records stored in an on-memory tree database object. </p>
<dl>
<dd><code>uint64_t tcndbrnum(TCNDB *</code><i>ndb</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>The return value is the number of the records stored in the database.</dl>
</dl>
<p> The function `tcndbmsiz&#8217; is used in order to get the total size of memory used in an on-memory tree database object. </p>
<dl>
<dd><code>uint64_t tcndbmsiz(TCNDB *</code><i>ndb</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>The return value is the total size of memory used in the database.</dl>
</dl>
<p> The function `tcndbaddint&#8217; is used in order to add an integer to a record in an on-memory tree database object. </p>
<dl>
<dd><code>int tcndbaddint(TCNDB *</code><i>ndb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>The return value is the summation value.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as an integer and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcndbadddouble&#8217; is used in order to add a real number to a record in an on-memory tree database object. </p>
<dl>
<dd><code>double tcndbadddouble(TCNDB *</code><i>ndb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>The return value is the summation value.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as a real number and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcndbvanish&#8217; is used in order to clear an on-memory tree database object. </p>
<dl>
<dd><code>void tcndbvanish(TCNDB *</code><i>ndb</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>All records are removed.</dl>
</dl>
<p> The function `tcndbcutfringe&#8217; is used in order to remove fringe records of an on-memory tree database object. </p>
<dl>
<dd><code>void tcndbcutfringe(TCNDB *</code><i>ndb</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>ndb</i>&#8216; specifies the on-memory tree database object.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the number of records to be removed.</dl>
</dl>
<h2>Api Of Memory Pool</h2>
<p>The function `tcmpoolnew&#8217; is used in order to create a memory pool object. </p>
<dl>
<dd><code>TCMPOOL *tcmpoolnew(void);</code></p>
<dl>
<dd>The return value is the new memory pool object.</dl>
</dl>
<p> The function `tcmpooldel&#8217; is used in order to delete a memory pool object. </p>
<dl>
<dd><code>void tcmpooldel(TCMPOOL *</code><i>mpool</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tcmpoolpush&#8217; is used in order to relegate an arbitrary object to a memory pool object. </p>
<dl>
<dd><code>void *tcmpoolpush(TCMPOOL *</code><i>mpool</i><code>, void *</code><i>ptr</i><code>, void (*</code><i>del</i><code>)(void *));</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the object to be relegated. If it is `NULL&#8217;, this function has no effect.</dl>
<dl>
<dd>`<i>del</i>&#8216; specifies the pointer to the function to delete the object.</dl>
<dl>
<dd>The return value is the pointer to the given object.</dl>
<dl>
<dd>This function assures that the specified object is deleted when the memory pool object is deleted.</dl>
</dl>
<p> The function `tcmpoolpushptr&#8217; is used in order to relegate an allocated region to a memory pool object. </p>
<dl>
<dd><code>void *tcmpoolpushptr(TCMPOOL *</code><i>mpool</i><code>, void *</code><i>ptr</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region to be relegated. If it is `NULL&#8217;, this function has no effect.</dl>
<dl>
<dd>The return value is the pointer to the given object.</dl>
<dl>
<dd>This function assures that the specified region is released when the memory pool object is deleted.</dl>
</dl>
<p> The function `tcmpoolpushxstr&#8217; is used in order to relegate an extensible string object to a memory pool object. </p>
<dl>
<dd><code>TCXSTR *tcmpoolpushxstr(TCMPOOL *</code><i>mpool</i><code>, TCXSTR *</code><i>xstr</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>`<i>xstr</i>&#8216; specifies the extensible string object. If it is `NULL&#8217;, this function has no effect.</dl>
<dl>
<dd>The return value is the pointer to the given object.</dl>
<dl>
<dd>This function assures that the specified object is deleted when the memory pool object is deleted.</dl>
</dl>
<p> The function `tcmpoolpushlist&#8217; is used in order to relegate a list object to a memory pool object. </p>
<dl>
<dd><code>TCLIST *tcmpoolpushlist(TCMPOOL *</code><i>mpool</i><code>, TCLIST *</code><i>list</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>`<i>list</i>&#8216; specifies the list object. If it is `NULL&#8217;, this function has no effect.</dl>
<dl>
<dd>The return value is the pointer to the given object.</dl>
<dl>
<dd>This function assures that the specified object is deleted when the memory pool object is deleted.</dl>
</dl>
<p> The function `tcmpoolpushmap&#8217; is used in order to relegate a map object to a memory pool object. </p>
<dl>
<dd><code>TCMAP *tcmpoolpushmap(TCMPOOL *</code><i>mpool</i><code>, TCMAP *</code><i>map</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>`<i>map</i>&#8216; specifies the map object. If it is `NULL&#8217;, this function has no effect.</dl>
<dl>
<dd>The return value is the pointer to the given object.</dl>
<dl>
<dd>This function assures that the specified object is deleted when the memory pool object is deleted.</dl>
</dl>
<p> The function `tcmpoolpushtree&#8217; is used in order to relegate a tree object to a memory pool object. </p>
<dl>
<dd><code>TCTREE *tcmpoolpushtree(TCMPOOL *</code><i>mpool</i><code>, TCTREE *</code><i>tree</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>`<i>tree</i>&#8216; specifies the tree object. If it is `NULL&#8217;, this function has no effect.</dl>
<dl>
<dd>The return value is the pointer to the given object.</dl>
<dl>
<dd>This function assures that the specified object is deleted when the memory pool object is deleted.</dl>
</dl>
<p> The function `tcmpoolmalloc&#8217; is used in order to allocate a region relegated to a memory pool object. </p>
<dl>
<dd><code>void *tcmpoolmalloc(TCMPOOL *</code><i>mpool</i><code>, size_t </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>The return value is the pointer to the allocated region under the memory pool.</dl>
</dl>
<p> The function `tcmpoolxstrnew&#8217; is used in order to create an extensible string object relegated to a memory pool object. </p>
<dl>
<dd><code>TCXSTR *tcmpoolxstrnew(TCMPOOL *</code><i>mpool</i><code>);</code></p>
<dl>
<dd>The return value is the new extensible string object under the memory pool.</dl>
</dl>
<p> The function `tcmpoollistnew&#8217; is used in order to create a list object relegated to a memory pool object. </p>
<dl>
<dd><code>TCLIST *tcmpoollistnew(TCMPOOL *</code><i>mpool</i><code>);</code></p>
<dl>
<dd>The return value is the new list object under the memory pool.</dl>
</dl>
<p> The function `tcmpoolmapnew&#8217; is used in order to create a map object relegated to a memory pool object. </p>
<dl>
<dd><code>TCMAP *tcmpoolmapnew(TCMPOOL *</code><i>mpool</i><code>);</code></p>
<dl>
<dd>The return value is the new map object under the memory pool.</dl>
</dl>
<p> The function `tcmpooltreenew&#8217; is used in order to create a tree object relegated to a memory pool object. </p>
<dl>
<dd><code>TCTREE *tcmpooltreenew(TCMPOOL *</code><i>mpool</i><code>);</code></p>
<dl>
<dd>The return value is the new tree object under the memory pool.</dl>
</dl>
<p> The function `tcmpoolpop&#8217; is used in order to remove the most recently installed cleanup handler of a memory pool object. </p>
<dl>
<dd><code>void tcmpoolpop(TCMPOOL *</code><i>mpool</i><code>, bool </code><i>exe</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>`<i>exe</i>&#8216; specifies whether to execute the destructor of the removed handler.</dl>
</dl>
<p> The function `tcmpoolclear&#8217; is used in order to remove all cleanup handler of a memory pool object. </p>
<dl>
<dd><code>void tcmpoolclear(TCMPOOL *</code><i>mpool</i><code>, bool </code><i>exe</i><code>);</code></p>
<dl>
<dd>`<i>mpool</i>&#8216; specifies the memory pool object.</dl>
<dl>
<dd>`<i>exe</i>&#8216; specifies whether to execute the destructors of the removed handlers.</dl>
</dl>
<p> The function `tcmpoolglobal&#8217; is used in order to get the global memory pool object. </p>
<dl>
<dd><code>TCMPOOL *tcmpoolglobal(void);</code></p>
<dl>
<dd>The return value is the global memory pool object.</dl>
<dl>
<dd>The global memory pool object is a singleton and assured to be deleted when the process is terminating normally.</dl>
</dl>
<h2>Api Of Miscellaneous Utilities</h2>
<p>The function `tclmax&#8217; is used in order to get the larger value of two integers. </p>
<dl>
<dd><code>long tclmax(long </code><i>a</i><code>, long </code><i>b</i><code>);</code></p>
<dl>
<dd>`<i>a</i>&#8216; specifies an integer.</dl>
<dl>
<dd>`<i>b</i>&#8216; specifies the other integer.</dl>
<dl>
<dd>The return value is the larger value of the two.</dl>
</dl>
<p> The function `tclmin&#8217; is used in order to get the lesser value of two integers. </p>
<dl>
<dd><code>long tclmin(long </code><i>a</i><code>, long </code><i>b</i><code>);</code></p>
<dl>
<dd>`<i>a</i>&#8216; specifies an integer.</dl>
<dl>
<dd>`<i>b</i>&#8216; specifies the other integer.</dl>
<dl>
<dd>The return value is the lesser value of the two.</dl>
</dl>
<p> The function `tclrand&#8217; is used in order to get a random number as long integer based on uniform distribution. </p>
<dl>
<dd><code>unsigned long tclrand(void);</code></p>
<dl>
<dd>The return value is the random number between 0 and `ULONG_MAX&#8217;.</dl>
<dl>
<dd>This function uses the random number source device and generates a real random number if possible.</dl>
</dl>
<p> The function `tcdrand&#8217; is used in order to get a random number as double decimal based on uniform distribution. </p>
<dl>
<dd><code>double tcdrand(void);</code></p>
<dl>
<dd>The return value is the random number equal to or greater than 0, and less than 1.0.</dl>
<dl>
<dd>This function uses the random number source device and generates a real random number if possible.</dl>
</dl>
<p> The function `tcdrandnd&#8217; is used in order to get a random number as double decimal based on normal distribution. </p>
<dl>
<dd><code>double tcdrandnd(double </code><i>avg</i><code>, double </code><i>sd</i><code>);</code></p>
<dl>
<dd>`<i>avg</i>&#8216; specifies the average.</dl>
<dl>
<dd>`<i>sd</i>&#8216; specifies the standard deviation.</dl>
<dl>
<dd>The return value is the random number.</dl>
<dl>
<dd>This function uses the random number source device and generates a real random number if possible.</dl>
</dl>
<p> The function `tcstricmp&#8217; is used in order to compare two strings with case insensitive evaluation. </p>
<dl>
<dd><code>int tcstricmp(const char *</code><i>astr</i><code>, const char *</code><i>bstr</i><code>);</code></p>
<dl>
<dd>`<i>astr</i>&#8216; specifies a string.</dl>
<dl>
<dd>`<i>bstr</i>&#8216; specifies of the other string.</dl>
<dl>
<dd>The return value is positive if the former is big, negative if the latter is big, 0 if both are equivalent.</dl>
</dl>
<p> The function `tcstrfwm&#8217; is used in order to check whether a string begins with a key. </p>
<dl>
<dd><code>bool tcstrfwm(const char *</code><i>str</i><code>, const char *</code><i>key</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the target string.</dl>
<dl>
<dd>`<i>key</i>&#8216; specifies the forward matching key string.</dl>
<dl>
<dd>The return value is true if the target string begins with the key, else, it is false.</dl>
</dl>
<p> The function `tcstrifwm&#8217; is used in order to check whether a string begins with a key with case insensitive evaluation. </p>
<dl>
<dd><code>bool tcstrifwm(const char *</code><i>str</i><code>, const char *</code><i>key</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the target string.</dl>
<dl>
<dd>`<i>key</i>&#8216; specifies the forward matching key string.</dl>
<dl>
<dd>The return value is true if the target string begins with the key, else, it is false.</dl>
</dl>
<p> The function `tcstrbwm&#8217; is used in order to check whether a string ends with a key. </p>
<dl>
<dd><code>bool tcstrbwm(const char *</code><i>str</i><code>, const char *</code><i>key</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the target string.</dl>
<dl>
<dd>`<i>key</i>&#8216; specifies the backward matching key string.</dl>
<dl>
<dd>The return value is true if the target string ends with the key, else, it is false.</dl>
</dl>
<p> The function `tcstribwm&#8217; is used in order to check whether a string ends with a key with case insensitive evaluation. </p>
<dl>
<dd><code>bool tcstribwm(const char *</code><i>str</i><code>, const char *</code><i>key</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the target string.</dl>
<dl>
<dd>`<i>key</i>&#8216; specifies the backward matching key string.</dl>
<dl>
<dd>The return value is true if the target string ends with the key, else, it is false.</dl>
</dl>
<p> The function `tcstrdist&#8217; is used in order to calculate the edit distance of two strings. </p>
<dl>
<dd><code>int tcstrdist(const char *</code><i>astr</i><code>, const char *</code><i>bstr</i><code>);</code></p>
<dl>
<dd>`<i>astr</i>&#8216; specifies a string.</dl>
<dl>
<dd>`<i>bstr</i>&#8216; specifies of the other string.</dl>
<dl>
<dd>The return value is the edit distance which is known as the Levenshtein distance. The cost is calculated by byte.</dl>
</dl>
<p> The function `tcstrdistutf&#8217; is used in order to calculate the edit distance of two UTF-8 strings. </p>
<dl>
<dd><code>int tcstrdistutf(const char *</code><i>astr</i><code>, const char *</code><i>bstr</i><code>);</code></p>
<dl>
<dd>`<i>astr</i>&#8216; specifies a string.</dl>
<dl>
<dd>`<i>bstr</i>&#8216; specifies of the other string.</dl>
<dl>
<dd>The return value is the edit distance which is known as the Levenshtein distance. The cost is calculated by Unicode character.</dl>
</dl>
<p> The function `tcstrtoupper&#8217; is used in order to convert the letters of a string into upper case. </p>
<dl>
<dd><code>char *tcstrtoupper(char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string to be converted.</dl>
<dl>
<dd>The return value is the string itself.</dl>
</dl>
<p> The function `tcstrtolower&#8217; is used in order to convert the letters of a string into lower case. </p>
<dl>
<dd><code>char *tcstrtolower(char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string to be converted.</dl>
<dl>
<dd>The return value is the string itself.</dl>
</dl>
<p> The function `tcstrtrim&#8217; is used in order to cut space characters at head or tail of a string. </p>
<dl>
<dd><code>char *tcstrtrim(char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string to be converted.</dl>
<dl>
<dd>The return value is the string itself.</dl>
</dl>
<p> The function `tcstrsqzspc&#8217; is used in order to squeeze space characters in a string and trim it. </p>
<dl>
<dd><code>char *tcstrsqzspc(char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string to be converted.</dl>
<dl>
<dd>The return value is the string itself.</dl>
</dl>
<p> The function `tcstrsubchr&#8217; is used in order to substitute characters in a string. </p>
<dl>
<dd><code>char *tcstrsubchr(char *</code><i>str</i><code>, const char *</code><i>rstr</i><code>, const char *</code><i>sstr</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string to be converted.</dl>
<dl>
<dd>`<i>rstr</i>&#8216; specifies the string containing characters to be replaced.</dl>
<dl>
<dd>`<i>sstr</i>&#8216; specifies the string containing characters to be substituted.</dl>
<dl>
<dd>If the substitute string is shorter then the replacement string, corresponding characters are removed.</dl>
</dl>
<p> The function `tcstrcntutf&#8217; is used in order to count the number of characters in a string of UTF-8. </p>
<dl>
<dd><code>int tcstrcntutf(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of UTF-8.</dl>
<dl>
<dd>The return value is the number of characters in the string.</dl>
</dl>
<p> The function `tcstrcututf&#8217; is used in order to cut a string of UTF-8 at the specified number of characters. </p>
<dl>
<dd><code>char *tcstrcututf(char *</code><i>str</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string of UTF-8.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the number of characters to be kept.</dl>
<dl>
<dd>The return value is the string itself.</dl>
</dl>
<p> The function `tcstrutftoucs&#8217; is used in order to convert a UTF-8 string into a UCS-2 array. </p>
<dl>
<dd><code>void tcstrutftoucs(const char *</code><i>str</i><code>, uint16_t *</code><i>ary</i><code>, int *</code><i>np</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the UTF-8 string.</dl>
<dl>
<dd>`<i>ary</i>&#8216; specifies the pointer to the region into which the result UCS-2 codes are written. The size of the buffer should be sufficient.</dl>
<dl>
<dd>`<i>np</i>&#8216; specifies the pointer to a variable into which the number of elements of the result array is assigned.</dl>
</dl>
<p> The function `tcstrucstoutf&#8217; is used in order to convert a UCS-2 array into a UTF-8 string. </p>
<dl>
<dd><code>int tcstrucstoutf(const uint16_t *</code><i>ary</i><code>, int </code><i>num</i><code>, char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>ary</i>&#8216; specifies the array of UCS-2 codes.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the number of the array.</dl>
<dl>
<dd>`<i>str</i>&#8216; specifies the pointer to the region into which the result UTF-8 string is written. The size of the buffer should be sufficient.</dl>
<dl>
<dd>The return value is the length of the result string.</dl>
</dl>
<p> The function `tcstrsplit&#8217; is used in order to create a list object by splitting a string. </p>
<dl>
<dd><code>TCLIST *tcstrsplit(const char *</code><i>str</i><code>, const char *</code><i>delims</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the source string.</dl>
<dl>
<dd>`<i>delims</i>&#8216; specifies a string containing delimiting characters.</dl>
<dl>
<dd>The return value is a list object of the split elements.</dl>
<dl>
<dd>If two delimiters are successive, it is assumed that an empty element is between the two. Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcstrjoin&#8217; is used in order to create a string by joining all elements of a list object. </p>
<dl>
<dd><code>char *tcstrjoin(const TCLIST *</code><i>list</i><code>, char </code><i>delim</i><code>);</code></p>
<dl>
<dd>`<i>list</i>&#8216; specifies a list object.</dl>
<dl>
<dd>`<i>delim</i>&#8216; specifies a delimiting character.</dl>
<dl>
<dd>The return value is the result string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcatoi&#8217; is used in order to convert a string to an integer. </p>
<dl>
<dd><code>int64_t tcatoi(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string.</dl>
<dl>
<dd>The return value is the integer. If the string does not contain numeric expression, 0 is returned.</dl>
<dl>
<dd>This function is equivalent to `atoll&#8217; except that it does not depend on the locale.</dl>
</dl>
<p> The function `tcatoix&#8217; is used in order to convert a string with a metric prefix to an integer. </p>
<dl>
<dd><code>int64_t tcatoix(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string, which can be trailed by a binary metric prefix. &quot;K&quot;, &quot;M&quot;, &quot;G&quot;, &quot;T&quot;, &quot;P&quot;, and &quot;E&quot; are supported. They are case-insensitive.</dl>
<dl>
<dd>The return value is the integer. If the string does not contain numeric expression, 0 is returned. If the integer overflows the domain, `INT64_MAX&#8217; or `INT64_MIN&#8217; is returned according to the sign.</dl>
</dl>
<p> The function `tcatof&#8217; is used in order to convert a string to a real number. </p>
<dl>
<dd><code>double tcatof(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string.</dl>
<dl>
<dd>The return value is the real number. If the string does not contain numeric expression, 0.0 is returned.</dl>
<dl>
<dd>This function is equivalent to `atof&#8217; except that it does not depend on the locale.</dl>
</dl>
<p> The function `tcregexmatch&#8217; is used in order to check whether a string matches a regular expression. </p>
<dl>
<dd><code>bool tcregexmatch(const char *</code><i>str</i><code>, const char *</code><i>regex</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the target string.</dl>
<dl>
<dd>`<i>regex</i>&#8216; specifies the regular expression string. If it begins with `*&#8217;, the trailing substring is used as a case-insensitive regular expression.</dl>
<dl>
<dd>The return value is true if matching is success, else, it is false.</dl>
</dl>
<p> The function `tcregexreplace&#8217; is used in order to replace each substring matching a regular expression string. </p>
<dl>
<dd><code>char *tcregexreplace(const char *</code><i>str</i><code>, const char *</code><i>regex</i><code>, const char *</code><i>alt</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the target string.</dl>
<dl>
<dd>`<i>regex</i>&#8216; specifies the regular expression string for substrings. If it begins with `*&#8217;, the trailing substring is used as a case-insensitive regular expression.</dl>
<dl>
<dd>`<i>alt</i>&#8216; specifies the alternative string with which each substrings is replaced. Each `&amp;&#8217; in the string is replaced with the matched substring. Each `&#8217; in the string escapes the following character. Special escapes &quot;1&quot; through &quot;9&quot; referring to the corresponding matching sub-expressions in the regular expression string are supported.</dl>
<dl>
<dd>The return value is a new converted string. Even if the regular expression is invalid, a copy of the original string is returned.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmd5hash&#8217; is used in order to get the MD5 hash value of a serial object. </p>
<dl>
<dd><code>void tcmd5hash(const void *</code><i>ptr</i><code>, int </code><i>size</i><code>, char *</code><i>buf</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>buf</i>&#8216; specifies the pointer to the region into which the result string is written. The size of the buffer should be equal to or more than 48 bytes.</dl>
</dl>
<p> The function `tcarccipher&#8217; is used in order to cipher or decipher a serial object with the Arcfour stream cipher. </p>
<dl>
<dd><code>void tcarccipher(const void *</code><i>ptr</i><code>, int </code><i>size</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, void *</code><i>obuf</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the cipher key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the cipher key.</dl>
<dl>
<dd>`<i>obuf</i>&#8216; specifies the pointer to the region into which the result data is written. The size of the buffer should be equal to or more than the input region.</dl>
</dl>
<p> The function `tctime&#8217; is used in order to get the time of day in seconds. </p>
<dl>
<dd><code>double tctime(void);</code></p>
<dl>
<dd>The return value is the time of day in seconds. The accuracy is in microseconds.</dl>
</dl>
<p> The function `tccalendar&#8217; is used in order to get the Gregorian calendar of a time. </p>
<dl>
<dd><code>void tccalendar(int64_t </code><i>t</i><code>, int </code><i>jl</i><code>, int *</code><i>yearp</i><code>, int *</code><i>monp</i><code>, int *</code><i>dayp</i><code>, int *</code><i>hourp</i><code>, int *</code><i>minp</i><code>, int *</code><i>secp</i><code>);</code></p>
<dl>
<dd>`<i>t</i>&#8216; specifies the source time in seconds from the epoch. If it is `INT64_MAX&#8217;, the current time is specified.</dl>
<dl>
<dd>`<i>jl</i>&#8216; specifies the jet lag of a location in seconds. If it is `INT_MAX&#8217;, the local jet lag is specified.</dl>
<dl>
<dd>`<i>yearp</i>&#8216; specifies the pointer to a variable to which the year is assigned. If it is `NULL&#8217;, it is not used.</dl>
<dl>
<dd>`<i>monp</i>&#8216; specifies the pointer to a variable to which the month is assigned. If it is `NULL&#8217;, it is not used. 1 means January and 12 means December.</dl>
<dl>
<dd>`<i>dayp</i>&#8216; specifies the pointer to a variable to which the day of the month is assigned. If it is `NULL&#8217;, it is not used.</dl>
<dl>
<dd>`<i>hourp</i>&#8216; specifies the pointer to a variable to which the hours is assigned. If it is `NULL&#8217;, it is not used.</dl>
<dl>
<dd>`<i>minp</i>&#8216; specifies the pointer to a variable to which the minutes is assigned. If it is `NULL&#8217;, it is not used.</dl>
<dl>
<dd>`<i>secp</i>&#8216; specifies the pointer to a variable to which the seconds is assigned. If it is `NULL&#8217;, it is not used.</dl>
</dl>
<p> The function `tcdatestrwww&#8217; is used in order to format a date as a string in W3CDTF. </p>
<dl>
<dd><code>void tcdatestrwww(int64_t </code><i>t</i><code>, int </code><i>jl</i><code>, char *</code><i>buf</i><code>);</code></p>
<dl>
<dd>`<i>t</i>&#8216; specifies the source time in seconds from the epoch. If it is `INT64_MAX&#8217;, the current time is specified.</dl>
<dl>
<dd>`<i>jl</i>&#8216; specifies the jet lag of a location in seconds. If it is `INT_MAX&#8217;, the local jet lag is specified.</dl>
<dl>
<dd>`<i>buf</i>&#8216; specifies the pointer to the region into which the result string is written. The size of the buffer should be equal to or more than 48 bytes.</dl>
<dl>
<dd>W3CDTF represents a date as &quot;YYYY-MM-DDThh:mm:ddTZD&quot;.</dl>
</dl>
<p> The function `tcdatestrhttp&#8217; is used in order to format a date as a string in RFC 1123 format. </p>
<dl>
<dd><code>void tcdatestrhttp(int64_t </code><i>t</i><code>, int </code><i>jl</i><code>, char *</code><i>buf</i><code>);</code></p>
<dl>
<dd>`<i>t</i>&#8216; specifies the source time in seconds from the epoch. If it is `INT64_MAX&#8217;, the current time is specified.</dl>
<dl>
<dd>`<i>jl</i>&#8216; specifies the jet lag of a location in seconds. If it is `INT_MAX&#8217;, the local jet lag is specified.</dl>
<dl>
<dd>`<i>buf</i>&#8216; specifies the pointer to the region into which the result string is written. The size of the buffer should be equal to or more than 48 bytes.</dl>
<dl>
<dd>RFC 1123 format represents a date as &quot;Wdy, DD-Mon-YYYY hh:mm:dd TZD&quot;.</dl>
</dl>
<p> The function `tcstrmktime&#8217; is used in order to get the time value of a date string. </p>
<dl>
<dd><code>int64_t tcstrmktime(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the date string in decimal, hexadecimal, W3CDTF, or RFC 822 (1123). Decimal can be trailed by &quot;s&quot; for in seconds, &quot;m&quot; for in minutes, &quot;h&quot; for in hours, and &quot;d&quot; for in days.</dl>
<dl>
<dd>The return value is the time value of the date or `INT64_MIN&#8217; if the format is invalid.</dl>
</dl>
<p> The function `tcjetlag&#8217; is used in order to get the jet lag of the local time. </p>
<dl>
<dd><code>int tcjetlag(void);</code></p>
<dl>
<dd>The return value is the jet lag of the local time in seconds.</dl>
</dl>
<p> The function `tcdayofweek&#8217; is used in order to get the day of week of a date. </p>
<dl>
<dd><code>int tcdayofweek(int </code><i>year</i><code>, int </code><i>mon</i><code>, int </code><i>day</i><code>);</code></p>
<dl>
<dd>`<i>year</i>&#8216; specifies the year of a date.</dl>
<dl>
<dd>`<i>mon</i>&#8216; specifies the month of the date.</dl>
<dl>
<dd>`<i>day</i>&#8216; specifies the day of the date.</dl>
<dl>
<dd>The return value is the day of week of the date. 0 means Sunday and 6 means Saturday.</dl>
</dl>
<h2>Api Of Filesystem Utilities</h2>
<p>The function `tcrealpath&#8217; is used in order to get the canonicalized absolute path of a file. </p>
<dl>
<dd><code>char *tcrealpath(const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the file.</dl>
<dl>
<dd>The return value is the canonicalized absolute path of a file, or `NULL&#8217; if the path is invalid.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcstatfile&#8217; is used in order to get the status information of a file. </p>
<dl>
<dd><code>bool tcstatfile(const char *</code><i>path</i><code>, bool *</code><i>isdirp</i><code>, int64_t *</code><i>sizep</i><code>, int64_t *</code><i>mtimep</i><code>);</code></p>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the file.</dl>
<dl>
<dd>`<i>isdirp</i>&#8216; specifies the pointer to a variable into which whether the file is a directory is assigned. If it is `NULL&#8217;, it is ignored.</dl>
<dl>
<dd>`<i>sizep</i>&#8216; specifies the pointer to a variable into which the size of the file is assigned. If it is `NULL&#8217;, it is ignored.</dl>
<dl>
<dd>`<i>ntimep</i>&#8216; specifies the pointer to a variable into which the size of the file is assigned. If it is `NULL&#8217;, it is ignored.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcreadfile&#8217; is used in order to read whole data of a file. </p>
<dl>
<dd><code>void *tcreadfile(const char *</code><i>path</i><code>, int </code><i>limit</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the file. If it is `NULL&#8217;, the standard input is specified.</dl>
<dl>
<dd>`<i>limit</i>&#8216; specifies the limiting size of reading data. If it is not more than 0, the limitation is not specified.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned. If it is `NULL&#8217;, it is not used.</dl>
<dl>
<dd>The return value is the pointer to the allocated region of the read data, or `NULL&#8217; if the file could not be opened.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when when is no longer in use.</dl>
</dl>
<p> The function `tcreadfilelines&#8217; is used in order to read every line of a file. </p>
<dl>
<dd><code>TCLIST *tcreadfilelines(const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the file. If it is `NULL&#8217;, the standard input is specified.</dl>
<dl>
<dd>The return value is a list object of every lines if successful, else it is `NULL&#8217;.</dl>
<dl>
<dd>Line separators are cut out. Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcwritefile&#8217; is used in order to write data into a file. </p>
<dl>
<dd><code>bool tcwritefile(const char *</code><i>path</i><code>, const void *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the file. If it is `NULL&#8217;, the standard output is specified.</dl>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the data region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tccopyfile&#8217; is used in order to copy a file. </p>
<dl>
<dd><code>bool tccopyfile(const char *</code><i>src</i><code>, const char *</code><i>dest</i><code>);</code></p>
<dl>
<dd>`<i>src</i>&#8216; specifies the path of the source file.</dl>
<dl>
<dd>`<i>dest</i>&#8216; specifies the path of the destination file.</dl>
<dl>
<dd>The return value is true if successful, else, it is false.</dl>
<dl>
<dd>If the destination file exists, it is overwritten.</dl>
</dl>
<p> The function `tcreaddir&#8217; is used in order to read names of files in a directory. </p>
<dl>
<dd><code>TCLIST *tcreaddir(const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the directory.</dl>
<dl>
<dd>The return value is a list object of names if successful, else it is `NULL&#8217;.</dl>
<dl>
<dd>Links to the directory itself and to the parent directory are ignored.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcglobpat&#8217; is used in order to expand a pattern into a list of matched paths. </p>
<dl>
<dd><code>TCLIST *tcglobpat(const char *</code><i>pattern</i><code>);</code></p>
<dl>
<dd>`<i>pattern</i>&#8216; specifies the matching pattern.</dl>
<dl>
<dd>The return value is a list object of matched paths. If no path is matched, an empty list is returned.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcremovelink&#8217; is used in order to remove a file or a directory and its sub ones recursively. </p>
<dl>
<dd><code>bool tcremovelink(const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the link.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned when the link does not exist or the permission is denied.</dl>
</dl>
<p> The function `tcwrite&#8217; is used in order to write data into a file. </p>
<dl>
<dd><code>bool tcwrite(int </code><i>fd</i><code>, const void *</code><i>buf</i><code>, size_t </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>fd</i>&#8216; specifies the file descriptor.</dl>
<dl>
<dd>`<i>buf</i>&#8216; specifies the buffer to be written.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the buffer.</dl>
<dl>
<dd>The return value is true if successful, else, it is false.</dl>
</dl>
<p> The function `tcread&#8217; is used in order to read data from a file. </p>
<dl>
<dd><code>bool tcread(int </code><i>fd</i><code>, void *</code><i>buf</i><code>, size_t </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>fd</i>&#8216; specifies the file descriptor.</dl>
<dl>
<dd>`<i>buf</i>&#8216; specifies the buffer to store into.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the buffer.</dl>
<dl>
<dd>The return value is true if successful, else, it is false.</dl>
</dl>
<p> The function `tclock&#8217; is used in order to lock a file. </p>
<dl>
<dd><code>bool tclock(int </code><i>fd</i><code>, bool </code><i>ex</i><code>, bool </code><i>nb</i><code>);</code></p>
<dl>
<dd>`<i>fd</i>&#8216; specifies the file descriptor.</dl>
<dl>
<dd>`<i>ex</i>&#8216; specifies whether an exclusive lock or a shared lock is performed.</dl>
<dl>
<dd>`<i>nb</i>&#8216; specifies whether to request with non-blocking.</dl>
<dl>
<dd>The return value is true if successful, else, it is false.</dl>
</dl>
<p> The function `tcunlock&#8217; is used in order to unlock a file. </p>
<dl>
<dd><code>bool tcunlock(int </code><i>fd</i><code>);</code></p>
<dl>
<dd>`<i>fd</i>&#8216; specifies the file descriptor.</dl>
<dl>
<dd>The return value is true if successful, else, it is false.</dl>
</dl>
<p> The function `tcsystem&#8217; is used in order to execute a shell command. </p>
<dl>
<dd><code>int tcsystem(const char **</code><i>args</i><code>, int </code><i>anum</i><code>);</code></p>
<dl>
<dd>`<i>args</i>&#8216; specifies an array of the command name and its arguments.</dl>
<dl>
<dd>`<i>anum</i>&#8216; specifies the number of elements of the array.</dl>
<dl>
<dd>The return value is the exit code of the command or `INT_MAX&#8217; on failure.</dl>
<dl>
<dd>The command name and the arguments are quoted and meta characters are escaped.</dl>
</dl>
<h2>Api Of Encoding Utilities</h2>
<p>The function `tcurlencode&#8217; is used in order to encode a serial object with URL encoding. </p>
<dl>
<dd><code>char *tcurlencode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the result string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call if when is no longer in use.</dl>
</dl>
<p> The function `tcurldecode&#8217; is used in order to decode a string encoded with URL encoding. </p>
<dl>
<dd><code>char *tcurldecode(const char *</code><i>str</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the encoded string.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the result.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcurlbreak&#8217; is used in order to break up a URL into elements. </p>
<dl>
<dd><code>TCMAP *tcurlbreak(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the URL string.</dl>
<dl>
<dd>The return value is the map object whose keys are the name of elements. The key &quot;self&quot; indicates the URL itself. The key &quot;scheme&quot; indicates the scheme. The key &quot;host&quot; indicates the host of the server. The key &quot;port&quot; indicates the port number of the server. The key &quot;authority&quot; indicates the authority information. The key &quot;path&quot; indicates the path of the resource. The key &quot;file&quot; indicates the file name without the directory section. The key &quot;query&quot; indicates the query string. The key &quot;fragment&quot; indicates the fragment string.</dl>
<dl>
<dd>Supported schema are HTTP, HTTPS, FTP, and FILE. Absolute URL and relative URL are supported. Because the object of the return value is created with the function `tcmapnew&#8217;, it should be deleted with the function `tcmapdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcurlresolve&#8217; is used in order to resolve a relative URL with an absolute URL. </p>
<dl>
<dd><code>char *tcurlresolve(const char *</code><i>base</i><code>, const char *</code><i>target</i><code>);</code></p>
<dl>
<dd>`<i>base</i>&#8216; specifies the absolute URL of the base location.</dl>
<dl>
<dd>`<i>target</i>&#8216; specifies the URL to be resolved.</dl>
<dl>
<dd>The return value is the resolved URL. If the target URL is relative, a new URL of relative location from the base location is returned. Else, a copy of the target URL is returned.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbaseencode&#8217; is used in order to encode a serial object with Base64 encoding. </p>
<dl>
<dd><code>char *tcbaseencode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the result string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call if when is no longer in use.</dl>
</dl>
<p> The function `tcbasedecode&#8217; is used in order to decode a string encoded with Base64 encoding. </p>
<dl>
<dd><code>char *tcbasedecode(const char *</code><i>str</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the encoded string.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the result.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcquoteencode&#8217; is used in order to encode a serial object with Quoted-printable encoding. </p>
<dl>
<dd><code>char *tcquoteencode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the result string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call if when is no longer in use.</dl>
</dl>
<p> The function `tcquotedecode&#8217; is used in order to decode a string encoded with Quoted-printable encoding. </p>
<dl>
<dd><code>char *tcquotedecode(const char *</code><i>str</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the encoded string.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the result.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmimeencode&#8217; is used in order to encode a string with MIME encoding. </p>
<dl>
<dd><code>char *tcmimeencode(const char *</code><i>str</i><code>, const char *</code><i>encname</i><code>, bool </code><i>base</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string.</dl>
<dl>
<dd>`<i>encname</i>&#8216; specifies the string of the name of the character encoding.</dl>
<dl>
<dd>`<i>base</i>&#8216; specifies whether to use Base64 encoding. If it is false, Quoted-printable is used.</dl>
<dl>
<dd>The return value is the result string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmimedecode&#8217; is used in order to decode a string encoded with MIME encoding. </p>
<dl>
<dd><code>char *tcmimedecode(const char *</code><i>str</i><code>, char *</code><i>enp</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the encoded string.</dl>
<dl>
<dd>`<i>enp</i>&#8216; specifies the pointer to the region into which the name of encoding is written. If it is `NULL&#8217;, it is not used. The size of the buffer should be equal to or more than 32 bytes.</dl>
<dl>
<dd>The return value is the result string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmimebreak&#8217; is used in order to split a string of MIME into headers and the body. </p>
<dl>
<dd><code>char *tcmimebreak(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, TCMAP *</code><i>headers</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of MIME data.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>headers</i>&#8216; specifies a map object to store headers. If it is `NULL&#8217;, it is not used. Each key of the map is an uncapitalized header name.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the body data.</dl>
<dl>
<dd>If the content type is defined, the header map has the key &quot;TYPE&quot; specifying the type. If the character encoding is defined, the key &quot;CHARSET&quot; indicates the encoding name. If the boundary string of multipart is defined, the key &quot;BOUNDARY&quot; indicates the string. If the content disposition is defined, the key &quot;DISPOSITION&quot; indicates the direction. If the file name is defined, the key &quot;FILENAME&quot; indicates the name. If the attribute name is defined, the key &quot;NAME&quot; indicates the name. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcmimeparts&#8217; is used in order to split multipart data of MIME into its parts. </p>
<dl>
<dd><code>TCLIST *tcmimeparts(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, const char *</code><i>boundary</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region of multipart data of MIME.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>boundary</i>&#8216; specifies the boundary string.</dl>
<dl>
<dd>The return value is a list object. Each element of the list is the data of a part.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tchexencode&#8217; is used in order to encode a serial object with hexadecimal encoding. </p>
<dl>
<dd><code>char *tchexencode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the result string.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call if when is no longer in use.</dl>
</dl>
<p> The function `tchexdecode&#8217; is used in order to decode a string encoded with hexadecimal encoding. </p>
<dl>
<dd><code>char *tchexdecode(const char *</code><i>str</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the encoded string.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return</dl>
<dl>
<dd>value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the result.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcpackencode&#8217; is used in order to compress a serial object with Packbits encoding. </p>
<dl>
<dd><code>char *tcpackencode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcpackdecode&#8217; is used in order to decompress a serial object compressed with Packbits encoding. </p>
<dl>
<dd><code>char *tcpackdecode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbsencode&#8217; is used in order to compress a serial object with TCBS encoding. </p>
<dl>
<dd><code>char *tcbsencode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbsdecode&#8217; is used in order to decompress a serial object compressed with TCBS encoding. </p>
<dl>
<dd><code>char *tcbsdecode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcdeflate&#8217; is used in order to compress a serial object with Deflate encoding. </p>
<dl>
<dd><code>char *tcdeflate(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcinflate&#8217; is used in order to decompress a serial object compressed with Deflate encoding. </p>
<dl>
<dd><code>char *tcinflate(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcgzipencode&#8217; is used in order to compress a serial object with GZIP encoding. </p>
<dl>
<dd><code>char *tcgzipencode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcgzipdecode&#8217; is used in order to decompress a serial object compressed with GZIP encoding. </p>
<dl>
<dd><code>char *tcgzipdecode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcgetcrc&#8217; is used in order to get the CRC32 checksum of a serial object. </p>
<dl>
<dd><code>unsigned int tcgetcrc(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>The return value is the CRC32 checksum of the object.</dl>
</dl>
<p> The function `tcbzipencode&#8217; is used in order to compress a serial object with BZIP2 encoding. </p>
<dl>
<dd><code>char *tcbzipencode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbzipdecode&#8217; is used in order to decompress a serial object compressed with BZIP2 encoding. </p>
<dl>
<dd><code>char *tcbzipdecode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the result object, else, it is `NULL&#8217;.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcberencode&#8217; is used in order to encode an array of nonnegative integers with BER encoding. </p>
<dl>
<dd><code>char *tcberencode(const unsigned int *</code><i>ary</i><code>, int </code><i>anum</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>ary</i>&#8216; specifies the pointer to the array of nonnegative integers.</dl>
<dl>
<dd>`<i>anum</i>&#8216; specifies the size of the array.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to a variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the region of the result.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call if when is no longer in use.</dl>
</dl>
<p> The function `tcberdecode&#8217; is used in order to decode a serial object encoded with BER encoding. </p>
<dl>
<dd><code>unsigned int *tcberdecode(const char *</code><i>ptr</i><code>, int </code><i>size</i><code>, int *</code><i>np</i><code>);</code></p>
<dl>
<dd>`<i>ptr</i>&#8216; specifies the pointer to the region.</dl>
<dl>
<dd>`<i>size</i>&#8216; specifies the size of the region.</dl>
<dl>
<dd>`<i>np</i>&#8216; specifies the pointer to a variable into which the number of elements of the return value is assigned.</dl>
<dl>
<dd>The return value is the pointer to the array of the result.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call if when is no longer in use.</dl>
</dl>
<p> The function `tcxmlescape&#8217; is used in order to escape meta characters in a string with the entity references of XML. </p>
<dl>
<dd><code>char *tcxmlescape(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string.</dl>
<dl>
<dd>The return value is the pointer to the escaped string.</dl>
<dl>
<dd>This function escapes only `&amp;&#8217;, `&lt;&#8216;, `&gt;&#8217;, and `&quot;&#8217;. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcxmlunescape&#8217; is used in order to unescape entity references in a string of XML. </p>
<dl>
<dd><code>char *tcxmlunescape(const char *</code><i>str</i><code>);</code></p>
<dl>
<dd>`<i>str</i>&#8216; specifies the string.</dl>
<dl>
<dd>The return value is the unescaped string.</dl>
<dl>
<dd>This function restores only `&amp;amp;&#8217;, `&amp;lt;&#8217;, `&amp;gt;&#8217;, and `&amp;quot;&#8217;. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tcutest/">tcutest</a></code>(1), <code><a href="/docs/linux/man/1-tcucodec/">tcucodec</a></code>(1), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
