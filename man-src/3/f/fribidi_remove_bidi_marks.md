---
title: "fribidi_remove_bidi_marks(3)"
name: "fribidi_remove_bidi_marks"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fribidi_remove_bidi_marks/"
---

<h2 class="name">NAME</h2>
 

 fribidi_remove_bidi_marks - remove bidi marks out of an string 

<h2>SYNOPSIS</h2>

 <b> #include &lt;fribidi.h&gt; 

 extern FriBidiStrIndex fribidi_remove_bidi_marks 
 ( 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiChar *str,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiStrIndex len,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiStrIndex *positions_to_this,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiStrIndex *position_from_this_list,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiLevel *embedding_levels
 
 ); </b>

<h2>PARAMETERS</h2>

<dl>
<dt><b>FriBidiChar *str</b>
<dd> Input string to clean.
<dt><b>const FriBidiStrIndex len</b>
<dd> Input string length.
<dt><b>FriBidiStrIndex *positions_to_this</b>
<dd> List mapping positions to the order used in str.
<dt><b>FriBidiStrIndex *position_from_this_list</b>
<dd> List mapping positions from the order used in str.
<dt><b>FriBidiLevel *embedding_levels</b>
<dd> List of embedding levels.</dl>

<h2>DESCRIPTION</h2>

 This function removes the bidi and boundary-neutral marks out of an string and the accompanying lists. It implements rule X9 of the Unicode Bidirectional Algorithm available at <a rel="nofollow" HREF="http://www.unicode.org/reports/tr9/#X9,">http://www.unicode.org/reports/tr9/#X9,</a> with the exception that it removes U+200E LEFT-TO-RIGHT MARK and U+200F RIGHT-TO-LEFT MARK too. 

 If any of the input lists are NULL, the list is skipped. If str is the visual string, then positions_to_this is positions_L_to_V and position_from_this_list is positions_V_to_L; if str is the logical string, the other way. Moreover, the position maps should be filled with valid entries. 

 A position map pointing to a removed character is filled with -1. By the way, you should not use embedding_levels if str is visual string. 

 For best results this function should be run on a whole paragraph, not lines; but feel free to do otherwise if you know what you are doing.

<h2>RETURNS</h2>

 New length of the string, or -1 if an error occurred (memory allocation failure most probably).

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-fribidi_shape_arabic/">fribidi_shape_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_direction/">fribidi_get_par_direction</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels_ex/">fribidi_get_par_embedding_levels_ex</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_line/">fribidi_reorder_line</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type/">fribidi_get_bidi_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_types/">fribidi_get_bidi_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type_name/">fribidi_get_bidi_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_debug_status/">fribidi_debug_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_debug/">fribidi_set_debug</a>(3), <a HREF="/docs/linux/man/3-fribidi_charset_to_unicode/">fribidi_charset_to_unicode</a>(3), <a HREF="/docs/linux/man/3-fribidi_unicode_to_charset/">fribidi_unicode_to_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_parse_charset/">fribidi_parse_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_mirroring_status/">fribidi_mirroring_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_mirroring/">fribidi_set_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_nsm_status/">fribidi_reorder_nsm_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_reorder_nsm/">fribidi_set_reorder_nsm</a>(3), <a HREF="/docs/linux/man/3-fribidi_log2vis_get_embedding_levels/">fribidi_log2vis_get_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type/">fribidi_get_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type_internal/">fribidi_get_type_internal</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels/">fribidi_get_par_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_join_arabic/">fribidi_join_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type/">fribidi_get_joining_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_types/">fribidi_get_joining_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type_name/">fribidi_get_joining_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_mirror_char/">fribidi_get_mirror_char</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape_mirroring/">fribidi_shape_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket/">fribidi_get_bracket</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket_types/">fribidi_get_bracket_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape/">fribidi_shape</a>(3) 

<h2>Index</h2>


