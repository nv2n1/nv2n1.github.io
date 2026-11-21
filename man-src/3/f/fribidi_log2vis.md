---

title: "fribidi_log2vis(3)"
name: "fribidi_log2vis"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fribidi_log2vis/"
---

fribidi_log2vis - get visual string 

<b> #include &lt;fribidi.h&gt; 

 extern FriBidiLevel fribidi_log2vis 
 ( 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiChar *str,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiStrIndex len,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiParType *pbase_dir,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiChar *visual_str,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiStrIndex *positions_L_to_V,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiStrIndex *positions_V_to_L,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiLevel *embedding_levels
 
 ); </b>

<h2>PARAMETERS</h2>

<dl>
<dt><b>const FriBidiChar *str</b>
</dt><dd> Input logical string.
</dd><dt><b>const FriBidiStrIndex len</b>
</dt><dd> Input string length.
</dd><dt><b>FriBidiParType *pbase_dir</b>
</dt><dd> Requested and resolved paragraph base direction. 
 Possible values for a <b>FriBidiParType</b> are as follows:
</dd><dl>
<dl>
<dt><b>FRIBIDI_PAR_LTR</b>
</dt><dd> Left-To-Right paragraph.
</dd><dt><b>FRIBIDI_PAR_RTL</b>
</dt><dd> Right-To-Left paragraph.
</dd><dt><b>FRIBIDI_PAR_ON</b>
</dt><dd> DirectiOn-Neutral paragraph.
</dd><dt><b>FRIBIDI_PAR_WLTR</b>
</dt><dd> Weak Left To Right paragraph.
</dd><dt><b>FRIBIDI_PAR_WRTL</b>
</dt><dd> Weak Right To Left paragraph.</dd></dl>
</dl>

<dt><b>FriBidiChar *visual_str</b>
</dt><dd> Output visual string.
</dd><dt><b>FriBidiStrIndex *positions_L_to_V</b>
</dt><dd> Output mapping from logical to visual string positions.
</dd><dt><b>FriBidiStrIndex *positions_V_to_L</b>
</dt><dd> Output mapping from visual string back to the logical string positions.
</dd><dt><b>FriBidiLevel *embedding_levels</b>
</dt><dd> Output list of embedding levels.</dd></dl>

This function converts the logical input string to the visual output strings as specified by the Unicode Bidirectional Algorithm. As a side effect it also generates mapping lists between the two strings, and the list of embedding levels as defined by the algorithm. 

 If NULL is passed as any of the the lists, the list is ignored and not filled. 

 This function is obsolete because it only handles one-line paragraphs. Please consider using other functions instead. Deprecated.

<h2>RETURNS</h2>

 Maximum level found plus one, or zero if any error occurred (memory allocation failure most probably).

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-fribidi_shape_arabic/">fribidi_shape_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_direction/">fribidi_get_par_direction</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels_ex/">fribidi_get_par_embedding_levels_ex</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_line/">fribidi_reorder_line</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type/">fribidi_get_bidi_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_types/">fribidi_get_bidi_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type_name/">fribidi_get_bidi_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_debug_status/">fribidi_debug_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_debug/">fribidi_set_debug</a>(3), <a HREF="/docs/linux/man/3-fribidi_charset_to_unicode/">fribidi_charset_to_unicode</a>(3), <a HREF="/docs/linux/man/3-fribidi_unicode_to_charset/">fribidi_unicode_to_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_parse_charset/">fribidi_parse_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_mirroring_status/">fribidi_mirroring_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_mirroring/">fribidi_set_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_nsm_status/">fribidi_reorder_nsm_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_reorder_nsm/">fribidi_set_reorder_nsm</a>(3), <a HREF="/docs/linux/man/3-fribidi_log2vis_get_embedding_levels/">fribidi_log2vis_get_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type/">fribidi_get_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type_internal/">fribidi_get_type_internal</a>(3), <a HREF="/docs/linux/man/3-fribidi_join_arabic/">fribidi_join_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type/">fribidi_get_joining_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_types/">fribidi_get_joining_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type_name/">fribidi_get_joining_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_mirror_char/">fribidi_get_mirror_char</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape_mirroring/">fribidi_shape_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket/">fribidi_get_bracket</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket_types/">fribidi_get_bracket_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape/">fribidi_shape</a>(3), <a HREF="/docs/linux/man/3-fribidi_remove_bidi_marks/">fribidi_remove_bidi_marks</a>(3)
