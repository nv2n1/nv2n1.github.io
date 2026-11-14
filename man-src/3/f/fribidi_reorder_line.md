---
title: "fribidi_reorder_line(3)"
name: "fribidi_reorder_line"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fribidi_reorder_line/"
---

<h2 class="name">NAME</h2>
 

 fribidi_reorder_line - reorder a line of logical string to visual 

<h2>SYNOPSIS</h2>

 <b> #include &lt;fribidi.h&gt; 

 extern FriBidiLevel fribidi_reorder_line 
 ( 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiFlags flags,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiCharType *bidi_types,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiStrIndex len,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiStrIndex off,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiParType base_dir,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiLevel *embedding_levels,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiChar *visual_str,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiStrIndex *map
 
 ); </b>

<h2>PARAMETERS</h2>

<dl>
<dt><b>FriBidiFlags flags</b>
<dd> Reorder flags.
<dt><b>const FriBidiCharType *bidi_types</b>
<dd> Input list of bidi types as returned by fribidi_get_bidi_types(). 

 Since there are 23 possible values for a <b>const FriBidiCharType</b>, they are not all listed here.
<dt><b>const FriBidiStrIndex len</b>
<dd> Input length of the line.
<dt><b>const FriBidiStrIndex off</b>
<dd> Input offset of the beginning of the line in the paragraph.
<dt><b>const FriBidiParType base_dir</b>
<dd> Resolved paragraph base direction. 

 Possible values for a <b>const FriBidiParType</b> are as follows:
<dl>
<dt>
<dd>
<dl>
<dt><b>FRIBIDI_PAR_LTR</b>
<dd> Left-To-Right paragraph.
<dt><b>FRIBIDI_PAR_RTL</b>
<dd> Right-To-Left paragraph.
<dt><b>FRIBIDI_PAR_ON</b>
<dd> DirectiOn-Neutral paragraph.
<dt><b>FRIBIDI_PAR_WLTR</b>
<dd> Weak Left To Right paragraph.
<dt><b>FRIBIDI_PAR_WRTL</b>
<dd> Weak Right To Left paragraph.</dl>
</dl>

<dt><b>FriBidiLevel *embedding_levels</b>
<dd> Input list of embedding levels, as returned by fribidi_get_par_embedding_levels.
<dt><b>FriBidiChar *visual_str</b>
<dd> Visual string to reorder.
<dt><b>FriBidiStrIndex *map</b>
<dd> A map of string indices which is reordered to reflect where each glyph ends up.</dl>

<h2>DESCRIPTION</h2>

 This function reorders the characters in a line of text from logical to final visual order. This function implements part 4 of rule L1, and rules L2 and L3 of the Unicode Bidirectional Algorithm available at <a rel="nofollow" HREF="http://www.unicode.org/reports/tr9/#Reordering_Resolved_Levels.">http://www.unicode.org/reports/tr9/#Reordering_Resolved_Levels.</a> 

 As a side effect it also sets position maps if not NULL. 

 You should provide the resolved paragraph direction and embedding levels as set by fribidi_get_par_embedding_levels(). Also note that the embedding levels may change a bit. To be exact, the embedding level of any sequence of white space at the end of line is reset to the paragraph embedding level (That is part 4 of rule L1). 

 Note that the bidi types and embedding levels are not reordered. You can reorder these (or any other) arrays using the map later. The user is responsible to initialize map to something sensible, like an identity mapping, or pass NULL if no map is needed. 

 There is an optional part to this function, which is whether non-spacing marks for right-to-left parts of the text should be reordered to come after their base characters in the visual string or not. Most rendering engines expect this behavior, but console-based systems for example do not like it. This is controlled by the FRIBIDI_FLAG_REORDER_NSM flag. The flag is on in FRIBIDI_FLAGS_DEFAULT.

<h2>RETURNS</h2>

 Maximum level found in this line plus one, or zero if any error occurred (memory allocation failure most probably).

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-fribidi_shape_arabic/">fribidi_shape_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_direction/">fribidi_get_par_direction</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels_ex/">fribidi_get_par_embedding_levels_ex</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type/">fribidi_get_bidi_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_types/">fribidi_get_bidi_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type_name/">fribidi_get_bidi_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_debug_status/">fribidi_debug_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_debug/">fribidi_set_debug</a>(3), <a HREF="/docs/linux/man/3-fribidi_charset_to_unicode/">fribidi_charset_to_unicode</a>(3), <a HREF="/docs/linux/man/3-fribidi_unicode_to_charset/">fribidi_unicode_to_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_parse_charset/">fribidi_parse_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_mirroring_status/">fribidi_mirroring_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_mirroring/">fribidi_set_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_nsm_status/">fribidi_reorder_nsm_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_reorder_nsm/">fribidi_set_reorder_nsm</a>(3), <a HREF="/docs/linux/man/3-fribidi_log2vis_get_embedding_levels/">fribidi_log2vis_get_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type/">fribidi_get_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type_internal/">fribidi_get_type_internal</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels/">fribidi_get_par_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_join_arabic/">fribidi_join_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type/">fribidi_get_joining_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_types/">fribidi_get_joining_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type_name/">fribidi_get_joining_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_mirror_char/">fribidi_get_mirror_char</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape_mirroring/">fribidi_shape_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket/">fribidi_get_bracket</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket_types/">fribidi_get_bracket_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape/">fribidi_shape</a>(3), <a HREF="/docs/linux/man/3-fribidi_remove_bidi_marks/">fribidi_remove_bidi_marks</a>(3) 

<h2>Index</h2>


