---
title: "msgpuck-h(3)"
name: "msgpuck-h"
section: "3"
letter: "m"
url: "/docs/linux/man/3-msgpuck-h/"
description: "msgpuck.h – MsgPuck is a simple and efficient MsgPack encoder/decoder library in a single self-contained file."
---

<p>msgpuck.h &#8211; MsgPuck is a simple and efficient MsgPack encoder/decoder library in a single self-contained file.</p>
<h2>Synopsis</h2>
<p>#include &lt;stdlib.h&gt;<br />
 #include &lt;stdint.h&gt;<br />
 #include &lt;stddef.h&gt;<br />
 #include &lt;stdbool.h&gt;<br />
 #include &lt;string.h&gt;<br />
 #include &lt;assert.h&gt;<br />
 #include &lt;stdarg.h&gt;<br />
 #include &lt;stdio.h&gt; </p>
<h3>Enumerations</h3>
<p>enum <code>mp_type</code> { <code>MP_NIL</code> = 0, <code>MP_UINT</code>, <code>MP_INT</code>, <code>MP_STR</code>, <code>MP_BIN</code>, <code>MP_ARRAY</code>, <code>MP_MAP</code>, <code>MP_BOOL</code>, <code>MP_FLOAT</code>, <code>MP_DOUBLE</code>, <code>MP_EXT</code> }<br />
 <i>MsgPack data types. </i></p>
<h3>Functions</h3>
<p>MP_PROTO enum <code>mp_type</code> <code>mp_typeof</code> (const char c)<br />
 <i>Determine MsgPack type by a first byte c</i> of encoded data.<br />
 MP_PROTO uint32_t <code>mp_sizeof_array</code> (uint32_t size)<br />
 <i>Calculate exact buffer size needed to store an array header of size</i> elements. Maximum return value is 5. For performance reasons you can preallocate buffer for maximum size without calling the function.<br />
 MP_PROTO char * <code>mp_encode_array</code> (char *data, uint32_t size)<br />
 <i>Encode an array header of size</i> elements.<br />
 MP_PROTO ptrdiff_t <code>mp_check_array</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode an array header.<br />
 MP_PROTO uint32_t <code>mp_decode_array</code> (const char **data)<br />
 <i>Decode an array header from MsgPack data</i>.<br />
 MP_PROTO uint32_t <code>mp_sizeof_map</code> (uint32_t size)<br />
 <i>Calculate exact buffer size needed to store a map header of size</i> elements. Maximum return value is 5. For performance reasons you can preallocate buffer for maximum size without calling the function.<br />
 MP_PROTO char * <code>mp_encode_map</code> (char *data, uint32_t size)<br />
 <i>Encode a map header of size</i> elements.<br />
 MP_PROTO ptrdiff_t <code>mp_check_map</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode a map header.<br />
 MP_PROTO uint32_t <code>mp_decode_map</code> (const char **data)<br />
 <i>Decode a map header from MsgPack data</i>.<br />
 MP_PROTO uint32_t <code>mp_sizeof_uint</code> (uint64_t num)<br />
 <i>Calculate exact buffer size needed to store an integer num</i>. Maximum return value is 9. For performance reasons you can preallocate buffer for maximum size without calling the function. Example usage:<br />
 MP_PROTO uint32_t <code>mp_sizeof_int</code> (int64_t num)<br />
 <i>Calculate exact buffer size needed to store an integer num</i>. Maximum return value is 9. For performance reasons you can preallocate buffer for maximum size without calling the function.<br />
 MP_PROTO char * <code>mp_encode_uint</code> (char *data, uint64_t num)<br />
 <i>Encode an unsigned integer num</i>. It is your responsibility to ensure that <i>data</i> has enough space.<br />
 MP_PROTO char * <code>mp_encode_int</code> (char *data, int64_t num)<br />
 <i>Encode a signed integer num</i>. It is your responsibility to ensure that <i>data</i> has enough space.<br />
 MP_PROTO ptrdiff_t <code>mp_check_uint</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode an uint.<br />
 MP_PROTO ptrdiff_t <code>mp_check_int</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode an int.<br />
 MP_PROTO uint64_t <code>mp_decode_uint</code> (const char **data)<br />
 <i>Decode an unsigned integer from MsgPack data</i>.<br />
 MP_PROTO int64_t <code>mp_decode_int</code> (const char **data)<br />
 <i>Decode a signed integer from MsgPack data</i>.<br />
 MP_PROTO int <code>mp_compare_uint</code> (const char *data_a, const char *data_b)<br />
 <i>Compare two packed unsigned integers. </i><br />
 MP_PROTO uint32_t <code>mp_sizeof_float</code> (float num)<br />
 <i>Calculate exact buffer size needed to store a float num</i>. The return value is always 5. The function was added to provide integrity of the library.<br />
 MP_PROTO uint32_t <code>mp_sizeof_double</code> (double num)<br />
 <i>Calculate exact buffer size needed to store a double num</i>. The return value is either 5 or 9. The function was added to provide integrity of the library. For performance reasons you can preallocate buffer for maximum size without calling the function.<br />
 MP_PROTO char * <code>mp_encode_float</code> (char *data, float num)<br />
 <i>Encode a float num</i>. It is your responsibility to ensure that <i>data</i> has enough space.<br />
 MP_PROTO char * <code>mp_encode_double</code> (char *data, double num)<br />
 <i>Encode a double num</i>. It is your responsibility to ensure that <i>data</i> has enough space.<br />
 MP_PROTO ptrdiff_t <code>mp_check_float</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode a float.<br />
 MP_PROTO ptrdiff_t <code>mp_check_double</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode a double.<br />
 MP_PROTO float <code>mp_decode_float</code> (const char **data)<br />
 <i>Decode a float from MsgPack data</i>.<br />
 MP_PROTO double <code>mp_decode_double</code> (const char **data)<br />
 <i>Decode a double from MsgPack data</i>.<br />
 MP_PROTO uint32_t <code>mp_sizeof_strl</code> (uint32_t len)<br />
 <i>Calculate exact buffer size needed to store a string header of length num</i>. Maximum return value is 5. For performance reasons you can preallocate buffer for maximum size without calling the function.<br />
 MP_PROTO uint32_t <code>mp_sizeof_str</code> (uint32_t len)<br />
 <i>Equivalent to mp_sizeof_strl(len</i>) + <i>len</i>.<br />
 MP_PROTO uint32_t <code>mp_sizeof_binl</code> (uint32_t len)<br />
 <i>Calculate exact buffer size needed to store a binstring header of length num</i>. Maximum return value is 5. For performance reasons you can preallocate buffer for maximum size without calling the function.<br />
 MP_PROTO uint32_t <code>mp_sizeof_bin</code> (uint32_t len)<br />
 <i>Equivalent to mp_sizeof_binl(len</i>) + <i>len</i>.<br />
 MP_PROTO char * <code>mp_encode_strl</code> (char *data, uint32_t len)<br />
 <i>Encode a string header of length len</i>.<br />
 MP_PROTO char * <code>mp_encode_str</code> (char *data, const char *str, uint32_t len)<br />
 <i>Encode a string of length len</i>. The function is equivalent to <code>mp_encode_strl()</code> + memcpy.<br />
 MP_PROTO char * <code>mp_encode_binl</code> (char *data, uint32_t len)<br />
 <i>Encode a binstring header of length len</i>. See <code>mp_encode_strl()</code> for more details.<br />
 MP_PROTO char * <code>mp_encode_bin</code> (char *data, const char *str, uint32_t len)<br />
 <i>Encode a binstring of length len</i>. The function is equivalent to <code>mp_encode_binl()</code> + memcpy.<br />
 MP_PROTO size_t <code>mp_format</code> (char *data, size_t data_size, const char *format,&#8230;)<br />
 <i>Encode a sequence of values according to format string. Example: mp_format(buf, sz, &#8216;[%d {%d%s%d%s}]&#8217;, 42, 0, &#8216;false&#8217;, 1, &#8216;true&#8217;); to get a msgpack array of two items: number 42 and map (0-&gt;&#8217;false, 2-&gt;&#8217;true)Does</i>not<i>write</i>items<i>that</i>don&#8217;t<i>fit</i>to<i>data_size</i>argument.<i></i><br />
 MP_PROTO size_t <code>mp_vformat</code> (char *data, size_t data_size, const char *format, va_list args)<br />
 <i>mp_format variation, taking variable argument list Example: va_list args; va_start(args, fmt); mp_vformat(data, data_size, fmt, args); va_end(args); </i><br />
 MP_PROTO int <code>mp_fprint</code> (FILE *file, const char *data)<br />
 <i>print MsgPack data file</i> using JSON-like format. MP_EXT is printed as &#8216;undefined&#8217;<br />
 MP_PROTO int <code>mp_snprint</code> (char *buf, int size, const char *data)<br />
 <i>format MsgPack data to buf</i> using JSON-like format.<br />
 MP_PROTO ptrdiff_t <code>mp_check_strl</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode a string header.<br />
 MP_PROTO ptrdiff_t <code>mp_check_binl</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode a binstring header.<br />
 MP_PROTO uint32_t <code>mp_decode_strl</code> (const char **data)<br />
 <i>Decode a length of a string from MsgPack data</i>.<br />
 MP_PROTO const char * <code>mp_decode_str</code> (const char **data, uint32_t *len)<br />
 <i>Decode a string from MsgPack data</i>.<br />
 MP_PROTO uint32_t <code>mp_decode_binl</code> (const char **data)<br />
 <i>Decode a length of a binstring from MsgPack data</i>.<br />
 MP_PROTO const char * <code>mp_decode_bin</code> (const char **data, uint32_t *len)<br />
 <i>Decode a binstring from MsgPack data</i>.<br />
 MP_PROTO uint32_t <code>mp_decode_strbinl</code> (const char **data)<br />
 <i>Decode a length of a string or binstring from MsgPack data</i>.<br />
 MP_PROTO const char * <code>mp_decode_strbin</code> (const char **data, uint32_t *len)<br />
 <i>Decode a string or binstring from MsgPack data</i>.<br />
 MP_PROTO uint32_t <code>mp_sizeof_nil</code> (void)<br />
 <i>Calculate exact buffer size needed to store the nil value. The return value is always 1. The function was added to provide integrity of the library. </i><br />
 MP_PROTO char * <code>mp_encode_nil</code> (char *data)<br />
 <i>Encode the nil value. It is your responsibility to ensure that data</i> has enough space.<br />
 MP_PROTO ptrdiff_t <code>mp_check_nil</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode nil.<br />
 MP_PROTO void <code>mp_decode_nil</code> (const char **data)<br />
 <i>Decode the nil value from MsgPack data</i>.<br />
 MP_PROTO uint32_t <code>mp_sizeof_bool</code> (bool val)<br />
 <i>Calculate exact buffer size needed to store a boolean value. The return value is always 1. The function was added to provide integrity of the library. </i><br />
 MP_PROTO char * <code>mp_encode_bool</code> (char *data, bool val)<br />
 <i>Encode a bool value val</i>. It is your responsibility to ensure that <i>data</i> has enough space.<br />
 MP_PROTO ptrdiff_t <code>mp_check_bool</code> (const char *cur, const char *end)<br />
 <i>Check that cur</i> buffer has enough bytes to decode a bool value.<br />
 MP_PROTO bool <code>mp_decode_bool</code> (const char **data)<br />
 <i>Decode a bool value from MsgPack data</i>.<br />
 MP_PROTO void <code>mp_next</code> (const char **data)<br />
 <i>Skip one element in a packed data</i>.<br />
 MP_PROTO int <code>mp_check</code> (const char **data, const char *end)<br />
 <i>Equivalent to </i><code>mp_next()</code> but also validates MsgPack in <i>data</i>.</p>
<h2>Detailed Description</h2>
<p>MsgPuck is a simple and efficient MsgPack encoder/decoder library in a single self-contained file. </p>
<p> MsgPuck Usage example: </p>
<pre>* // Encode
* char buf[1024];
* char *w = buf;
* w = mp_encode_array(w, 4)
* w = mp_encode_uint(w, 10);
* w = mp_encode_str(w, &quot;hello world&quot;, strlen(&quot;hello world&quot;));
* w = mp_encode_bool(w, true);
* w = mp_encode_double(w, 3.1415);
*
* // Validate
* const char *b = buf;
* int r = mp_check(&amp;b, w);
* assert(!r)
* assert(b == w);
*
* // Decode
* uint32_t size;
* uint64_t ival;
* const char *sval;
* uint32_t sval_len;
* bool bval;
* double dval;
*
* const char *r = buf;
*
* size = mp_decode_array(&amp;r);
* // size is 4
*
* ival = mp_decode_uint(&amp;r);
* // ival is 10;
*
* sval = mp_decode_str(&amp;r, &amp;sval_len);
* // sval is &quot;hello world&quot;, sval_len is strlen(&quot;hello world&quot;)
*
* bval = mp_decode_bool(&amp;r);
* // bval is true
*
* dval = mp_decode_double(&amp;r);
* // dval is 3.1415
*
* assert(r == w);
* </pre>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>Supported compilers. The implementation requires a C99+ or C++03+ compatible compiler. </p>
<p> Inline functions. The implementation is compatible with both C99 and GNU inline functions. Please define MP_SOURCE 1 before #include &lt;<code>msgpuck.h</code>&gt; in a single compilation unit. This module will be used to store non-inlined versions of functions and global tables.</dl>
<h2>Function Documentation</h2>
<h3>MP_PROTO int mp_check (const char **data, const char *end)</h3>
<p>Equivalent to <code>mp_next()</code> but also validates MsgPack in <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer<br />
 <i>end</i> &#8211; the end of a buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> when MsgPack in <i>data</i> is valid.<br />
 <i>!=</i> 0 when MsgPack in <i>data</i> is not valid.</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_TYPE() where TYPE is mp_typeof(**data) </p>
<p> *data is not defined if MsgPack is not valid</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_next()</code></dl>
<h3>MP_PROTO ptrdiff_t mp_check_array (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode an array header. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_ARRAY</dl>
<h3>MP_PROTO ptrdiff_t mp_check_binl (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode a binstring header. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_BIN</dl>
<h3>MP_PROTO ptrdiff_t mp_check_bool (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode a bool value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_BOOL</dl>
<h3>MP_PROTO ptrdiff_t mp_check_double (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode a double. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_DOUBLE</dl>
<h3>MP_PROTO ptrdiff_t mp_check_float (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode a float. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_FLOAT</dl>
<h3>MP_PROTO ptrdiff_t mp_check_int (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode an int. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_INT</dl>
<h3>MP_PROTO ptrdiff_t mp_check_map (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode a map header. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_MAP</dl>
<h3>MP_PROTO ptrdiff_t mp_check_nil (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode nil. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_NIL</dl>
<h3>MP_PROTO ptrdiff_t mp_check_strl (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode a string header. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_STR</dl>
<h3>MP_PROTO ptrdiff_t mp_check_uint (const char *cur, const char *end)</h3>
<p>Check that <i>cur</i> buffer has enough bytes to decode an uint. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cur</i> buffer<br />
 <i>end</i> end of the buffer</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>0</i> &#8211; buffer has enough bytes<br />
 <i>&gt;</i> 0 &#8211; the number of remaining bytes to read</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>cur &lt; end </p>
<p> mp_typeof(*cur) == MP_UINT</dl>
<h3>MP_PROTO int mp_compare_uint (const char *data_a, const char *data_b)</h3>
<p>Compare two packed unsigned integers. The function is faster than two <code>mp_decode_uint()</code> calls. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data_a</i> unsigned int a<br />
 <i>data_b</i> unsigned int b</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>&lt;</i> 0 when <i>a</i> &lt; <i>b</i><br />
 <i>0</i> when <i>a</i> == <i>b</i><br />
 <i>&gt;</i> 0 when <i>a</i> &gt; <i>b</i></dl>
<h3>MP_PROTO uint32_t mp_decode_array (const char **data)</h3>
<p>Decode an array header from MsgPack <i>data</i>. All array members must be decoded after the header. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the number of elements in an array</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_array(retval)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>An usage example </code></dl>
<h3>MP_PROTO const char* mp_decode_bin (const char **data, uint32_t *len)</h3>
<p>Decode a binstring from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer<br />
 <i>len</i> &#8211; the pointer to save a binstring length</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to a decoded binstring</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_str(*len)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_binl</code></dl>
<h3>MP_PROTO uint32_t mp_decode_binl (const char **data)</h3>
<p>Decode a length of a binstring from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a length of a binstring</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_binl(retval)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_binl</code></dl>
<h3>MP_PROTO bool mp_decode_bool (const char **data)</h3>
<p>Decode a bool value from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a decoded bool value</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_bool(retval)</dl>
<h3>MP_PROTO double mp_decode_double (const char **data)</h3>
<p>Decode a double from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a double</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_double(retval)</dl>
<h3>MP_PROTO float mp_decode_float (const char **data)</h3>
<p>Decode a float from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a float</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_float(retval)</dl>
<h3>MP_PROTO int64_t mp_decode_int (const char **data)</h3>
<p>Decode a signed integer from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>an unsigned number</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_int(retval)</dl>
<h3>MP_PROTO uint32_t mp_decode_map (const char **data)</h3>
<p>Decode a map header from MsgPack <i>data</i>. All map key-value pairs must be decoded after the header. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the number of key/value pairs in a map</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_array(retval)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>An usage example </code></dl>
<h3>MP_PROTO void mp_decode_nil (const char **data)</h3>
<p>Decode the nil value from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + <code>mp_sizeof_nil()</code></dl>
<h3>MP_PROTO const char* mp_decode_str (const char **data, uint32_t *len)</h3>
<p>Decode a string from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer<br />
 <i>len</i> &#8211; the pointer to save a string length</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to a decoded string</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_str(*len)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_binl</code></dl>
<h3>MP_PROTO const char* mp_decode_strbin (const char **data, uint32_t *len)</h3>
<p>Decode a string or binstring from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer<br />
 <i>len</i> &#8211; the pointer to save a binstring length</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to a decoded binstring</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_strbinl(*len)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_binl</code></dl>
<h3>MP_PROTO uint32_t mp_decode_strbinl (const char **data)</h3>
<p>Decode a length of a string or binstring from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a length of a string</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_strbinl(retval)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_binl</code></dl>
<h3>MP_PROTO uint32_t mp_decode_strl (const char **data)</h3>
<p>Decode a length of a string from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a length of astring</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_strl(retval)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_strl</code></dl>
<h3>MP_PROTO uint64_t mp_decode_uint (const char **data)</h3>
<p>Decode an unsigned integer from MsgPack <i>data</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; the pointer to a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>an unsigned number</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>*data = *data + mp_sizeof_uint(retval)</dl>
<h3>MP_PROTO char* mp_encode_array (char *data, uint32_tsize)</h3>
<p>Encode an array header of <i>size</i> elements. All array members must be encoded after the header. </p>
<p> Example usage: </p>
<pre>* // Encode
* char buf[1024];
* char *w = buf;
* w = mp_encode_array(w, 2)
* w = mp_encode_uint(w, 10);
* w = mp_encode_uint(w, 15);
*
* // Decode
* const char *r = buf;
* uint32_t size = mp_decode_array(&amp;r);
* for (uint32_t i = 0; i &lt; size; i++) {
* uint64_t val = mp_decode_uint(&amp;r);
* }
* assert (r == w);
* </pre>
<p>&nbsp;<wbr>It is your responsibility to ensure that&nbsp;<wbr><i>data</i>&nbsp;<wbr>has enough space.&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer<br />
 <i>size</i> &#8211; a number of elements</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + <code>mp_sizeof_array(size) </code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_sizeof_array</code></dl>
<h3>MP_PROTO char* mp_encode_bin (char *data, const char *str, uint32_tlen)</h3>
<p>Encode a binstring of length <i>len</i>. The function is equivalent to <code>mp_encode_binl()</code> + memcpy. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer<br />
 <i>str</i> &#8211; a pointer to binstring data<br />
 <i>len</i> &#8211; a binstring length</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + mp_sizeof_bin(<i>len</i>) == data + mp_sizeof_binl(<i>len</i>) + <i>len</i></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_strl</code></dl>
<h3>MP_PROTO char* mp_encode_binl (char *data, uint32_tlen)</h3>
<p>Encode a binstring header of length <i>len</i>. See <code>mp_encode_strl()</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a bufer<br />
 <i>len</i> &#8211; a string length</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>data + mp_sizeof_binl(<i>len</i>)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_strl</code></dl>
<h3>MP_PROTO char* mp_encode_bool (char *data, boolval)</h3>
<p>Encode a bool value <i>val</i>. It is your responsibility to ensure that <i>data</i> has enough space. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer<br />
 <i>val</i> &#8211; a bool</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + mp_sizeof_bool(val)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>An usage example </code> </p>
<p> <code>mp_sizeof_bool()</code></dl>
<h3>MP_PROTO char* mp_encode_double (char *data, doublenum)</h3>
<p>Encode a double <i>num</i>. It is your responsibility to ensure that <i>data</i> has enough space. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer<br />
 <i>num</i> &#8211; a float</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + mp_sizeof_double(<i>num</i>)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>An usage example </code> </p>
<p> <code>mp_sizeof_double()</code></dl>
<h3>MP_PROTO char* mp_encode_float (char *data, floatnum)</h3>
<p>Encode a float <i>num</i>. It is your responsibility to ensure that <i>data</i> has enough space. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer<br />
 <i>num</i> &#8211; a float</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + mp_sizeof_float(<i>num</i>)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_sizeof_float()</code> </p>
<p> <code>An usage example </code></dl>
<h3>MP_PROTO char* mp_encode_int (char *data, int64_tnum)</h3>
<p>Encode a signed integer <i>num</i>. It is your responsibility to ensure that <i>data</i> has enough space. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer<br />
 <i>num</i> &#8211; a number</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + mp_sizeof_int(<i>num</i>)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>An usage example </code> </p>
<p> <code>mp_sizeof_int()</code></dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd><i>num</i> &lt; 0</dl>
<h3>MP_PROTO char* mp_encode_map (char *data, uint32_tsize)</h3>
<p>Encode a map header of <i>size</i> elements. All map key-value pairs must be encoded after the header. </p>
<p> Example usage: </p>
<pre>* char buf[1024];
*
* // Encode
* char *w = buf;
* w = mp_encode_map(b, 2);
* w = mp_encode_str(b, &quot;key1&quot;, 4);
* w = mp_encode_str(b, &quot;value1&quot;, 6);
* w = mp_encode_str(b, &quot;key2&quot;, 4);
* w = mp_encode_str(b, &quot;value2&quot;, 6);
*
* // Decode
* const char *r = buf;
* uint32_t size = mp_decode_map(&amp;r);
* for (uint32_t i = 0; i &lt; size; i++) {
* // Use switch(mp_typeof(**r)) to support more types
* uint32_t key_len, val_len;
* const char *key = mp_decode_str(&amp;r, key_len);
* const char *val = mp_decode_str(&amp;r, val_len);
* }
* assert (r == w);
* </pre>
<p>&nbsp;<wbr>It is your responsibility to ensure that&nbsp;<wbr><i>data</i>&nbsp;<wbr>has enough space.&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer<br />
 <i>size</i> &#8211; a number of key/value pairs</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + <code>mp_sizeof_map(size)</code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_sizeof_map</code></dl>
<h3>MP_PROTO char* mp_encode_nil (char *data)</h3>
<p>Encode the nil value. It is your responsibility to ensure that <i>data</i> has enough space. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + <code>mp_sizeof_nil()</code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>An usage example </code> </p>
<p> <code>mp_sizeof_nil()</code></dl>
<h3>MP_PROTO char* mp_encode_str (char *data, const char *str, uint32_tlen)</h3>
<p>Encode a string of length <i>len</i>. The function is equivalent to <code>mp_encode_strl()</code> + memcpy. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> &#8211; a buffer<br />
 <i>str</i> &#8211; a pointer to string data<br />
 <i>len</i> &#8211; a string length</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><i>data</i> + mp_sizeof_str(len) == data + mp_sizeof_strl(len) + len</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mp_encode_strl</code></dl>
<h3>MP_PROTO char* mp_encode_strl (char *data, uint32_tlen)</h3>
<p>Encode a string header of length <i>len</i>. The function encodes MsgPack header (<i>only</i> header) for a string of length <i>len</i>. You should append actual string data to the buffer manually after encoding the header (exactly <i>len</i> bytes without trailing &#8216;
