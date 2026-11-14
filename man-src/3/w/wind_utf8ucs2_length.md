---
title: "wind_utf8ucs2_length(3)"
name: "wind_utf8ucs2_length"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wind_utf8ucs2_length/"
description: "Heimdal wind library –"
---

<p>Heimdal wind library &#8211;</p>
<h3>Functions</h3>
<pre><code>int wind_punycode_label_toascii (const uint32_t *in, size_t in_len, char *out, size_t *out_len)



int wind_stringprep (const uint32_t *in, size_t in_len, uint32_t *out, size_t *out_len, wind_profile_flags flags)



int wind_profile (const char *name, wind_profile_flags *flags)



int wind_utf8ucs4 (const char *in, uint32_t *out, size_t *out_len)



int wind_utf8ucs4_length (const char *in, size_t *out_len)



int wind_ucs4utf8 (const uint32_t *in, size_t in_len, char *out, size_t *out_len)



int wind_ucs4utf8_length (const uint32_t *in, size_t in_len, size_t *out_len)



int wind_ucs2read (const void *ptr, size_t len, unsigned int *flags, uint16_t *out, size_t *out_len)



int wind_ucs2write (const uint16_t *in, size_t in_len, unsigned int *flags, void *ptr, size_t *out_len)



int wind_utf8ucs2 (const char *in, uint16_t *out, size_t *out_len)



int wind_utf8ucs2_length (const char *in, size_t *out_len)



int wind_ucs2utf8 (const uint16_t *in, size_t in_len, char *out, size_t *out_len)



int wind_ucs2utf8_length (const uint16_t *in, size_t in_len, size_t *out_len)</code></pre>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int wind_profile (const char *name, wind_profile_flags *flags)</h3>
<p>Try to find the profile given a name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> name of the profile.<br />
 <i>flags</i> the resulting profile.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_punycode_label_toascii (const uint32_t *in, size_tin_len, char *out, size_t *out_len)</h3>
<p>Convert an UCS4 string to a puny-coded DNS label string suitable when combined with delimiters and other labels for DNS lookup. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UCS4 string to convert<br />
 <i>in_len</i> the length of in.<br />
 <i>out</i> the resulting puny-coded string. The string is not NUL terminatied.<br />
 <i>out_len</i> before processing out_len should be the length of the out variable, after processing it will be the length of the out string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_stringprep (const uint32_t *in, size_tin_len, uint32_t *out, size_t *out_len, wind_profile_flagsflags)</h3>
<p>Process a input UCS4 string according a string-prep profile. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> input UCS4 string to process<br />
 <i>in_len</i> length of the input string<br />
 <i>out</i> output UCS4 string<br />
 <i>out_len</i> length of the output string.<br />
 <i>flags</i> stringprep profile.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_ucs2read (const void *ptr, size_tlen, unsigned int *flags, uint16_t *out, size_t *out_len)</h3>
<p>Read in an UCS2 from a buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ptr</i> The input buffer to read from.<br />
 <i>len</i> the length of the input buffer.<br />
 <i>flags</i> Flags to control the behavior of the function.<br />
 <i>out</i> the output UCS2, the array must be at least out/2 long.<br />
 <i>out_len</i> the output length</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise.</dl>
<p> if len is zero, flags are unchanged </p>
<p> if len is odd, WIND_ERR_LENGTH_NOT_MOD2 is returned </p>
<p> If the flags WIND_RW_BOM is set, check for BOM. If not BOM is found, check is LE/BE flag is already and use that otherwise fail with WIND_ERR_NO_BOM. When done, clear WIND_RW_BOM and the LE/BE flag and set the resulting LE/BE flag.</p>
<h3>int wind_ucs2utf8 (const uint16_t *in, size_tin_len, char *out, size_t *out_len)</h3>
<p>Convert an UCS2 string to a UTF-8 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UCS2 string to convert.<br />
 <i>in_len</i> the length of the in UCS2 string.<br />
 <i>out</i> the resulting UTF-8 strint, must be at least <code>wind_ucs2utf8_length()</code> long. If out is NULL, the function will calculate the needed space for the out variable (just like <code>wind_ucs2utf8_length()</code>).<br />
 <i>out_len</i> before processing out_len should be the length of the out variable, after processing it will be the length of the out string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_ucs2utf8_length (const uint16_t *in, size_tin_len, size_t *out_len)</h3>
<p>Calculate the length of from converting a UCS2 string to an UTF-8 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UCS2 string to convert.<br />
 <i>in_len</i> an UCS2 string length to convert.<br />
 <i>out_len</i> the length of the resulting UTF-8 string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_ucs2write (const uint16_t *in, size_tin_len, unsigned int *flags, void *ptr, size_t *out_len)</h3>
<p>Write an UCS2 string to a buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> The input UCS2 string.<br />
 <i>in_len</i> the length of the input buffer.<br />
 <i>flags</i> Flags to control the behavior of the function.<br />
 <i>ptr</i> The input buffer to write to, the array must be at least (in + 1) * 2 bytes long.<br />
 <i>out_len</i> the output length</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise.</dl>
<p> If in buffer is not of length be mod 2, WIND_ERR_LENGTH_NOT_MOD2 is returned </p>
<p> On zero input length, flags are preserved </p>
<p> If flags have WIND_RW_BOM set, the byte order mark is written first to the output data </p>
<p> If the output wont fit into out_len, WIND_ERR_OVERRUN is returned</p>
<h3>int wind_ucs4utf8 (const uint32_t *in, size_tin_len, char *out, size_t *out_len)</h3>
<p>Convert an UCS4 string to a UTF-8 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UCS4 string to convert.<br />
 <i>in_len</i> the length input array.<br />
 <i>out</i> the resulting UTF-8 strint, must be at least <code>wind_ucs4utf8_length()</code> + 1 long (the extra char for the NUL). If out is NULL, the function will calculate the needed space for the out variable (just like <code>wind_ucs4utf8_length()</code>).<br />
 <i>out_len</i> before processing out_len should be the length of the out variable, after processing it will be the length of the out string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_ucs4utf8_length (const uint32_t *in, size_tin_len, size_t *out_len)</h3>
<p>Calculate the length of from converting a UCS4 string to an UTF-8 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UCS4 string to convert.<br />
 <i>in_len</i> the length of UCS4 string to convert.<br />
 <i>out_len</i> the length of the resulting UTF-8 string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_utf8ucs2 (const char *in, uint16_t *out, size_t *out_len)</h3>
<p>Convert an UTF-8 string to an UCS2 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UTF-8 string to convert.<br />
 <i>out</i> the resulting UCS2 strint, must be at least <code>wind_utf8ucs2_length()</code> long. If out is NULL, the function will calculate the needed space for the out variable (just like <code>wind_utf8ucs2_length()</code>).<br />
 <i>out_len</i> before processing out_len should be the length of the out variable, after processing it will be the length of the out string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_utf8ucs2_length (const char *in, size_t *out_len)</h3>
<p>Calculate the length of from converting a UTF-8 string to a UCS2 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UTF-8 string to convert.<br />
 <i>out_len</i> the length of the resulting UCS4 string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_utf8ucs4 (const char *in, uint32_t *out, size_t *out_len)</h3>
<p>Convert an UTF-8 string to an UCS4 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UTF-8 string to convert.<br />
 <i>out</i> the resulting UCS4 strint, must be at least <code>wind_utf8ucs4_length()</code> long. If out is NULL, the function will calculate the needed space for the out variable (just like <code>wind_utf8ucs4_length()</code>).<br />
 <i>out_len</i> before processing out_len should be the length of the out variable, after processing it will be the length of the out string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h3>int wind_utf8ucs4_length (const char *in, size_t *out_len)</h3>
<p>Calculate the length of from converting a UTF-8 string to a UCS4 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in</i> an UTF-8 string to convert.<br />
 <i>out_len</i> the length of the resulting UCS4 string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>returns 0 on success, an wind error code otherwise</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdalwindlibrary from the source code.</p>
