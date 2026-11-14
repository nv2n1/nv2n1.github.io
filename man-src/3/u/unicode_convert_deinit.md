---
title: "unicode_convert_deinit(3)"
name: "unicode_convert_deinit"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_convert_deinit/"
description: "unicode_u_ucs4_native, unicode_u_ucs2_native, unicode_convert_init, unicode_convert, unicode_convert_deinit, unicode_convert_tocbuf_init, unicode_convert_tou_init, unicode_convert_fromu_init, unico..."
---

<p>unicode_u_ucs4_native, unicode_u_ucs2_native, unicode_convert_init, unicode_convert, unicode_convert_deinit, unicode_convert_tocbuf_init, unicode_convert_tou_init, unicode_convert_fromu_init, unicode_convert_uc, unicode_convert_tocbuf_toutf8_init, unicode_convert_tocbuf_fromutf8_init, unicode_convert_toutf8, unicode_convert_fromutf8, unicode_convert_tobuf, unicode_convert_tou_tobuf, unicode_convert_fromu_tobuf &#8211; unicode character set conversion</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

extern const char unicode_u_ucs4_native[];

extern const char unicode_u_ucs2_native[];

unicode_convert_handle_t unicode_convert_init(const char *src_chset, const char *dst_chset, void *cb_arg);

int unicode_convert(unicode_convert_handle_t handle, const char *text, size_t cnt);

int unicode_convert_deinit(unicode_convert_handle_t handle, int *errptr);

unicode_convert_handle_t unicode_convert_tocbuf_init(const char *src_chset, const char *dst_chset, char **cbufptr_ret, size_t *cbufsize_ret, int nullterminate);

unicode_convert_handle_t unicode_convert_tocbuf_toutf8_init(const char *src_chset, char **cbufptr_ret, size_t *cbufsize_ret, int nullterminate);

unicode_convert_handle_t unicode_convert_tocbuf_fromutf8_init(const char *dst_chset, char **cbufptr_ret, size_t *cbufsize_ret, int nullterminate);

unicode_convert_handle_t unicode_convert_tou_init(const char *src_chset, unicode_char **ucptr_ret, size_t *ucsize_ret, int nullterminate);

unicode_convert_handle_t unicode_convert_fromu_init(const char *dst_chset, char **cbufptr_ret, size_t *cbufsize_ret, int nullterminate);

int unicode_convert_uc(unicode_convert_handle_t handle, const unicode_char *text, size_t cnt);

char *unicode_convert_toutf8(const char *text, const char *charset, int *error);

char *unicode_convert_fromutf8(const char *text, const char *charset, int *error);

char *unicode_convert_tobuf(const char *text, const char *charset, const char *dstcharset, int *error);

int unicode_convert_toubuf(const char *text, size_t text_l, const char *charset, unicode_char **uc, size_t *ucsize, int *error);

int unicode_convert_fromu_tobuf(const unicode_char *utext, size_t utext_l, const char *charset, char **c, size_t *csize, int *error);</code></pre>
<h2>Description</h2>
<p><i>unicode_u_ucs4_native</i>[] contains the string &#8220;UCS-4BE&#8221;</p>
<dd>or &#8220;UCS-4LE&#8221;, matching the native unicode_char endianness. <i>unicode_u_ucs2_native</i>[] contains the string &#8220;UCS-2BE&#8221; or &#8220;UCS-2LE&#8221;, matching the native unicode_char endianness. <code>unicode_convert_init</code>(), <code>unicode_convert</code>(), and <code>unicode_convert_deinit</code>() are an adaption of th m[blue]<code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3)m[]<font SIZE="-2">[1]</font> API that uses the same calling convention as the other algorithms in this unicode library, with some value-added features. These functions use <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) to effect the actual character set conversion. <code>unicode_convert_init</code>() returns a non-NULL handle for the requested conversion, or NULL if the requested conversion is not available. <code>unicode_convert_init</code>() takes a pointer to the output function that receives receives converted character text. The output function receives a pointer to the converted character text, and the number of characters in the converted text. The output function gets repeatedly called, until it receives the entire converted text. The character text to convert gets passed, repeatedly, to <code>unicode_convert</code>(). Each call to <code>unicode_convert</code>() results in the output function getting invoked, zero or more times, with each successive part of the converted text. Finally, <code>unicode_convert_deinit</code>() stops the conversion and deallocates the conversion handle. It&#8217;s possible that a call to <code>unicode_convert_deinit</code>() results in some additional calls to the output function, passing the remaining, final parts, of the converted text, before <code>unicode_convert_deinit</code>() deallocates the handle, and returns. The output function should return 0 normally. A non-0 return indicates n error condition. <code>unicode_convert_deinit</code>() returns non-zero if any previous invocation of the output function returned non-zero (this includes any invocations of the output function resulting from this call, or prior <code>unicode_convert</code>() calls), or 0 if all invocations of the output function returned 0. If the <i>errptr</i> is not NULL, *<i>errptr</i> gets set to non-zero if there were any conversion errors &#8212; if there was any text that could not be converted to the destination character text. <code>unicode_convert</code>() also returns non-zero if it calls the output function and it returns non-zero, however the conversion handle remains allocated, so <code>unicode_convert_deinit</code>() must still be called, to clean that up.</p>
<h3>Collecting converted text into a buffer</h3>
<p>Call <code>unicode_convert_tocbuf_init</code>() instead of <code>unicode_convert_init</code>(), then call <code>unicode_convert</code>() and <code>unicode_convert_deinit</code>() normally. The parameters to <code>unicode_convert_init</code>() specify the source and the destination character sets. <code>unicode_convert_tocbuf_toutf8_init</code>() is just an alias that specifies UTF-8 as the destination character set. <code>unicode_convert_tocbuf_fromutf8_init</code>() is just an alias that specifies UTF-8 as the source character st. These functions supply an output function that collects the converted text into a malloc()ed buffer. If <code>unicode_convert_deinit</code>() returns 0, *<i>cbufptr_ret</i> gets initialized to a malloc()ed buffer, and the number of converted characters, the size of the malloc()ed buffer, get placed into *<i>cbufsize_ret</i>.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If the converted string is an empty string, *<i>cbufsize_ret</i> gets set to 0, but *<i>cbufptr_ret</i> still gets initialized (to a dummy malloced buffer).  A non-zero <i>nullterminate</i> places a trailing 
