---
title: "fribidi_join_arabic(3)"
name: "fribidi_join_arabic"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fribidi_join_arabic/"
---

<h2 class="name">NAME</h2>
 

 fribidi_join_arabic - do Arabic joining 

<h2>SYNOPSIS</h2>

 <b> #include &lt;fribidi.h&gt; 

 extern void fribidi_join_arabic 
 ( 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiCharType *bidi_types,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiStrIndex len,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const FriBidiLevel *embedding_levels,
 
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>FriBidiArabicProp *ar_props
 
 ); </b>

<h2>PARAMETERS</h2>

<dl>
<dt><b>const FriBidiCharType *bidi_types</b>
<dd> Input list of bidi types as returned by fribidi_get_bidi_types(). 

 Since there are 23 possible values for a <b>const FriBidiCharType</b>, they are not all listed here.
<dt><b>const FriBidiStrIndex len</b>
<dd> Input string length.
<dt><b>const FriBidiLevel *embedding_levels</b>
<dd> Input list of embedding levels, as returned by fribidi_get_par_embedding_levels.
<dt><b>FriBidiArabicProp *ar_props</b>
<dd> Arabic properties to analyze, initialized by joining types, as returned by fribidi_get_joining_types.</dl>

<h2>DESCRIPTION</h2>

 This function does the Arabic joining algorithm. Means, given Arabic joining types of the characters in ar_props (don't worry, FriBidiJoiningType can be casted to FriBidiArabicProp automagically), this function modifies this properties to grasp the effect of neighboring characters. You probably need this information later to do Arabic shaping. 

 This function implements rules R1 to R7 inclusive (all rules) of the Arabic Cursive Joining algorithm of the Unicode standard as available at <a rel="nofollow" HREF="http://www.unicode.org/versions/Unicode4.0.0/ch08.pdf#G7462.">http://www.unicode.org/versions/Unicode4.0.0/ch08.pdf#G7462.</a> It also interacts correctly with the bidirection algorithm as defined in Section 
 3.5 Shaping of the Unicode Bidirectional Algorithm available at <a rel="nofollow" HREF="http://www.unicode.org/reports/tr9/#Shaping.">http://www.unicode.org/reports/tr9/#Shaping.</a> 

 There are a few macros defined in fribidi-joining-types.h for querying the Arabic properties computed by this function.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-fribidi_shape_arabic/">fribidi_shape_arabic</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_direction/">fribidi_get_par_direction</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels_ex/">fribidi_get_par_embedding_levels_ex</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_line/">fribidi_reorder_line</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type/">fribidi_get_bidi_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_types/">fribidi_get_bidi_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bidi_type_name/">fribidi_get_bidi_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_debug_status/">fribidi_debug_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_debug/">fribidi_set_debug</a>(3), <a HREF="/docs/linux/man/3-fribidi_charset_to_unicode/">fribidi_charset_to_unicode</a>(3), <a HREF="/docs/linux/man/3-fribidi_unicode_to_charset/">fribidi_unicode_to_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_parse_charset/">fribidi_parse_charset</a>(3), <a HREF="/docs/linux/man/3-fribidi_mirroring_status/">fribidi_mirroring_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_mirroring/">fribidi_set_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_reorder_nsm_status/">fribidi_reorder_nsm_status</a>(3), <a HREF="/docs/linux/man/3-fribidi_set_reorder_nsm/">fribidi_set_reorder_nsm</a>(3), <a HREF="/docs/linux/man/3-fribidi_log2vis_get_embedding_levels/">fribidi_log2vis_get_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type/">fribidi_get_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_type_internal/">fribidi_get_type_internal</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_par_embedding_levels/">fribidi_get_par_embedding_levels</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type/">fribidi_get_joining_type</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_types/">fribidi_get_joining_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_joining_type_name/">fribidi_get_joining_type_name</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_mirror_char/">fribidi_get_mirror_char</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape_mirroring/">fribidi_shape_mirroring</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket/">fribidi_get_bracket</a>(3), <a HREF="/docs/linux/man/3-fribidi_get_bracket_types/">fribidi_get_bracket_types</a>(3), <a HREF="/docs/linux/man/3-fribidi_shape/">fribidi_shape</a>(3), <a HREF="/docs/linux/man/3-fribidi_remove_bidi_marks/">fribidi_remove_bidi_marks</a>(3) 

<h2>Index</h2>


