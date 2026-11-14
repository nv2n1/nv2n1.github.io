---
title: "fribidi_get_joining_type(3)"
name: "fribidi_get_joining_type"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fribidi_get_joining_type/"
---

<h2 class="name">NAME</h2>
 

 fribidi_get_joining_type - get character joining type 

<h2>SYNOPSIS</h2>

 <b> #include &lt;fribidi.h&gt; 

 extern FriBidiJoiningType fribidi_get_joining_type(FriBidiChar ch); </b>

<h2>PARAMETERS</h2>

<dl>
<dt><b>FriBidiChar ch</b>
<dd> Input character.</dl>

<h2>DESCRIPTION</h2>

 This function returns the joining type of a character as defined in Table 8-2 Primary Arabic Joining Classes of the Unicode standard available at <a rel="nofollow" HREF="http://www.unicode.org/versions/Unicode4.0.0/ch08.pdf#G7462,">http://www.unicode.org/versions/Unicode4.0.0/ch08.pdf#G7462,</a> using data provided in file ArabicShaping.txt and UnicodeData.txt of the Unicode Character Database available at <a rel="nofollow" HREF="http://www.unicode.org/Public/UNIDATA/ArabicShaping.txt">http://www.unicode.org/Public/UNIDATA/ArabicShaping.txt</a> and <a rel="nofollow" HREF="http://www.unicode.org/Public/UNIDATA/UnicodeData.txt.">http://www.unicode.org/Public/UNIDATA/UnicodeData.txt.</a> 

 There are a few macros defined in fribidi-joining-types.h for querying a joining type.

<h2>RETURNS</h2>

 Possible values for an <b>extern FriBidiJoiningType</b> are as follows:
<dl>
<dt>
<dd>
<dl>
<dt><b>FRIBIDI_JOINING_TYPE_U</b>
<dd> NUn-joining, e.g. Full Stop.
<dt><b>FRIBIDI_JOINING_TYPE_R</b>
<dd> Right-joining, e.g. Arabic Letter Dal.
<dt><b>FRIBIDI_JOINING_TYPE_D</b>
<dd> Dual-joining, e.g. Arabic Letter Ain.
<dt><b>FRIBIDI_JOINING_TYPE_C</b>
<dd> Join-Causing, e.g. Tatweel, ZWJ.
<dt><b>FRIBIDI_JOINING_TYPE_T</b>
<dd> Transparent, e.g. Arabic Fatha.
<dt><b>FRIBIDI_JOINING_TYPE_L</b>
<dd> Left-joining, i.e. Fictional.
<dt><b>FRIBIDI_JOINING_TYPE_G</b>
<dd> IGnored, e.g. LRE, RLE, ZWNBSP.</dl>
</dl>

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-fribidi_shape_arabic/">fribidi_shape_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_direction/">fribidi_get_par_direction</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels_ex/">fribidi_get_par_embedding_levels_ex</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_line/">fribidi_reorder_line</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type/">fribidi_get_bidi_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_types/">fribidi_get_bidi_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type_name/">fribidi_get_bidi_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_debug_status/">fribidi_debug_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_debug/">fribidi_set_debug</a>(3), <a HREF="/docs/linux/man/3-fribidi_charset_to_unicode/">fribidi_charset_to_unicode</a>(3), <a HREF="/docs/linux/man/3-fribidi_unicode_to_charset/">fribidi_unicode_to_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_parse_charset/">fribidi_parse_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_mirroring_status/">fribidi_mirroring_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_mirroring/">fribidi_set_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_nsm_status/">fribidi_reorder_nsm_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_reorder_nsm/">fribidi_set_reorder_nsm</a>(3), <a HREF="/docs/linux/man/3-fribidi_log2vis_get_embedding_levels/">fribidi_log2vis_get_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type/">fribidi_get_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type_internal/">fribidi_get_type_internal</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels/">fribidi_get_par_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_join_arabic/">fribidi_join_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_types/">fribidi_get_joining_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type_name/">fribidi_get_joining_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_mirror_char/">fribidi_get_mirror_char</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape_mirroring/">fribidi_shape_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket/">fribidi_get_bracket</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket_types/">fribidi_get_bracket_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape/">fribidi_shape</a>(3), <a HREF="/docs/linux/man/3-fribidi_remove_bidi_marks/">fribidi_remove_bidi_marks</a>(3) 

<h2>Index</h2>


