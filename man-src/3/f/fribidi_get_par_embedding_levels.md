---

title: "fribidi_get_par_embedding_levels(3)"
name: "fribidi_get_par_embedding_levels"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fribidi_get_par_embedding_levels/"
---

fribidi_get_par_embedding_levels - get bidi embedding levels of a paragraph 

<b> #include &lt;fribidi.h&gt; 

 extern FriBidiLevel fribidi_get_par_embedding_levels 
 ( 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiCharType *bidi_types,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiStrIndex len,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiParType *pbase_dir,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiLevel *embedding_levels
 
 ); </b>

<h2>PARAMETERS</h2>

<dl>
<dt><b>const FriBidiCharType *bidi_types</b>
</dt><dd> Input list of bidi types as returned by fribidi_get_bidi_types(). 
 Since there are 23 possible values for a <b>const FriBidiCharType</b>, they are not all listed here.
</dd><dt><b>const FriBidiStrIndex len</b>
</dt><dd> Input string length of the paragraph.
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

<dt><b>FriBidiLevel *embedding_levels</b>
</dt><dd> Output list of embedding levels.</dd></dl>

Deprecated interface to fribidi_get_par_embedding_levels_ex(). Refer to it for documentation.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-fribidi_shape_arabic/">fribidi_shape_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_direction/">fribidi_get_par_direction</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels_ex/">fribidi_get_par_embedding_levels_ex</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_line/">fribidi_reorder_line</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type/">fribidi_get_bidi_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_types/">fribidi_get_bidi_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type_name/">fribidi_get_bidi_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_debug_status/">fribidi_debug_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_debug/">fribidi_set_debug</a>(3), <a HREF="/docs/linux/man/3-fribidi_charset_to_unicode/">fribidi_charset_to_unicode</a>(3), <a HREF="/docs/linux/man/3-fribidi_unicode_to_charset/">fribidi_unicode_to_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_parse_charset/">fribidi_parse_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_mirroring_status/">fribidi_mirroring_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_mirroring/">fribidi_set_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_nsm_status/">fribidi_reorder_nsm_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_reorder_nsm/">fribidi_set_reorder_nsm</a>(3), <a HREF="/docs/linux/man/3-fribidi_log2vis_get_embedding_levels/">fribidi_log2vis_get_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type/">fribidi_get_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type_internal/">fribidi_get_type_internal</a>(3), <a HREF="/docs/linux/man/3-fribidi_join_arabic/">fribidi_join_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type/">fribidi_get_joining_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_types/">fribidi_get_joining_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type_name/">fribidi_get_joining_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_mirror_char/">fribidi_get_mirror_char</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape_mirroring/">fribidi_shape_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket/">fribidi_get_bracket</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket_types/">fribidi_get_bracket_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape/">fribidi_shape</a>(3), <a HREF="/docs/linux/man/3-fribidi_remove_bidi_marks/">fribidi_remove_bidi_marks</a>(3)
