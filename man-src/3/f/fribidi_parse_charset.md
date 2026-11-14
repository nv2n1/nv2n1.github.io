---
title: "fribidi_parse_charset(3)"
name: "fribidi_parse_charset"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fribidi_parse_charset/"
---

<h2 class="name">NAME</h2>
 

 fribidi_parse_charset - parse character set name 

<h2>SYNOPSIS</h2>

 <b> #include &lt;fribidi.h&gt; 

 extern FriBidiCharSet fribidi_parse_charset(const char *s); </b>

<h2>PARAMETERS</h2>

<dl>
<dt><b>const char *s</b>
<dd> Input name of the character set.</dl>

<h2>DESCRIPTION</h2>

 Parse character set name.

<h2>RETURNS</h2>

 The character set named s, or FRIBIDI_CHAR_SET_NOT_FOUND if the character set is not available. 

 Possible values for an <b>extern FriBidiCharSet</b> are as follows:
<dl>
<dt>
<dd>
<dl>
<dt><b>FRIBIDI_CHAR_SET_UTF8</b>
<dd> UTF-8 (Unicode).
<dt><b>FRIBIDI_CHAR_SET_CAP_RTL</b>
<dd> CapRTL (Test).
<dt><b>FRIBIDI_CHAR_SET_ISO8859_6</b>
<dd> ISO8859-6 (Arabic).
<dt><b>FRIBIDI_CHAR_SET_ISO8859_8</b>
<dd> ISO8859-8 (Hebrew).
<dt><b>FRIBIDI_CHAR_SET_CP1255</b>
<dd> CP1255 (MS Hebrew/Yiddish).
<dt><b>FRIBIDI_CHAR_SET_CP1256</b>
<dd> CP1256 (MS Arabic).</dl>
</dl>

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-fribidi_shape_arabic/">fribidi_shape_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_direction/">fribidi_get_par_direction</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels_ex/">fribidi_get_par_embedding_levels_ex</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_line/">fribidi_reorder_line</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type/">fribidi_get_bidi_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_types/">fribidi_get_bidi_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type_name/">fribidi_get_bidi_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_debug_status/">fribidi_debug_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_debug/">fribidi_set_debug</a>(3), <a HREF="/docs/linux/man/3-fribidi_charset_to_unicode/">fribidi_charset_to_unicode</a>(3), <a HREF="/docs/linux/man/3-fribidi_unicode_to_charset/">fribidi_unicode_to_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_mirroring_status/">fribidi_mirroring_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_mirroring/">fribidi_set_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_nsm_status/">fribidi_reorder_nsm_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_reorder_nsm/">fribidi_set_reorder_nsm</a>(3), <a HREF="/docs/linux/man/3-fribidi_log2vis_get_embedding_levels/">fribidi_log2vis_get_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type/">fribidi_get_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type_internal/">fribidi_get_type_internal</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels/">fribidi_get_par_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_join_arabic/">fribidi_join_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type/">fribidi_get_joining_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_types/">fribidi_get_joining_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type_name/">fribidi_get_joining_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_mirror_char/">fribidi_get_mirror_char</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape_mirroring/">fribidi_shape_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket/">fribidi_get_bracket</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket_types/">fribidi_get_bracket_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape/">fribidi_shape</a>(3), <a HREF="/docs/linux/man/3-fribidi_remove_bidi_marks/">fribidi_remove_bidi_marks</a>(3) 

<h2>Index</h2>


