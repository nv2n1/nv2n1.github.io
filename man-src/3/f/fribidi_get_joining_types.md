---
title: "fribidi_get_joining_types(3)"
name: "fribidi_get_joining_types"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fribidi_get_joining_types/"
---

<h2 class="name">NAME</h2>
 

 fribidi_get_joining_types - get joining types for an string of characters 

<h2>SYNOPSIS</h2>

 <b> #include &lt;fribidi.h&gt; 

 extern void fribidi_get_joining_types 
 ( 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiChar *str,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiStrIndex len,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiJoiningType *jtypes
 
 ); </b>

<h2>PARAMETERS</h2>

<dl>
<dt><b>const FriBidiChar *str</b>
</dt><dd> Input string.
</dd><dt><b>const FriBidiStrIndex len</b>
</dt><dd> Input string length.
</dd><dt><b>FriBidiJoiningType *jtypes</b>
</dt><dd> Output joining types. 
 Possible values for a <b>FriBidiJoiningType</b> are as follows:
</dd><dl>
<dl>
<dt><b>FRIBIDI_JOINING_TYPE_U</b>
</dt><dd> NUn-joining, e.g. Full Stop.
</dd><dt><b>FRIBIDI_JOINING_TYPE_R</b>
</dt><dd> Right-joining, e.g. Arabic Letter Dal.
</dd><dt><b>FRIBIDI_JOINING_TYPE_D</b>
</dt><dd> Dual-joining, e.g. Arabic Letter Ain.
</dd><dt><b>FRIBIDI_JOINING_TYPE_C</b>
</dt><dd> Join-Causing, e.g. Tatweel, ZWJ.
</dd><dt><b>FRIBIDI_JOINING_TYPE_T</b>
</dt><dd> Transparent, e.g. Arabic Fatha.
</dd><dt><b>FRIBIDI_JOINING_TYPE_L</b>
</dt><dd> Left-joining, i.e. Fictional.
</dd><dt><b>FRIBIDI_JOINING_TYPE_G</b>
</dt><dd> IGnored, e.g. LRE, RLE, ZWNBSP.</dd></dl>
</dl>
</dl>

<h2>DESCRIPTION</h2>

 This function finds the joining types of an string of characters. See fribidi_get_joining_type for more information about the joining types returned by this function.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-fribidi_shape_arabic/">fribidi_shape_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_direction/">fribidi_get_par_direction</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels_ex/">fribidi_get_par_embedding_levels_ex</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_line/">fribidi_reorder_line</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type/">fribidi_get_bidi_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_types/">fribidi_get_bidi_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type_name/">fribidi_get_bidi_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_debug_status/">fribidi_debug_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_debug/">fribidi_set_debug</a>(3), <a HREF="/docs/linux/man/3-fribidi_charset_to_unicode/">fribidi_charset_to_unicode</a>(3), <a HREF="/docs/linux/man/3-fribidi_unicode_to_charset/">fribidi_unicode_to_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_parse_charset/">fribidi_parse_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_mirroring_status/">fribidi_mirroring_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_mirroring/">fribidi_set_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_nsm_status/">fribidi_reorder_nsm_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_reorder_nsm/">fribidi_set_reorder_nsm</a>(3), <a HREF="/docs/linux/man/3-fribidi_log2vis_get_embedding_levels/">fribidi_log2vis_get_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type/">fribidi_get_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type_internal/">fribidi_get_type_internal</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels/">fribidi_get_par_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_join_arabic/">fribidi_join_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type/">fribidi_get_joining_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type_name/">fribidi_get_joining_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_mirror_char/">fribidi_get_mirror_char</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape_mirroring/">fribidi_shape_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket/">fribidi_get_bracket</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket_types/">fribidi_get_bracket_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape/">fribidi_shape</a>(3), <a HREF="/docs/linux/man/3-fribidi_remove_bidi_marks/">fribidi_remove_bidi_marks</a>(3) 

<h2>Index</h2>


