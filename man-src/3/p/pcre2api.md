---
title: "pcre2api(3)"
name: "pcre2api"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2api/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API) </p>
<pre><code>#include &lt;
pcre2.h&gt;</code></pre>
<p> PCRE2 is a new API for PCRE, starting at release 10.0. This document contains a description of all its native functions. See the <code>pcre2</code> document for an overview of all the PCRE2 documentation.</p>
<h2>Pcre2 Native Api Basic Functions</h2>
<pre><code>pcre2_code *pcre2_compile(PCRE2_SPTR </code><i>pattern</i>, PCRE2_SIZE <i>length</i>,
<code> uint32_t </code><i>options</i>, int *<i>errorcode</i>, PCRE2_SIZE *<i>erroroffset,</i>
<code> pcre2_compile_context *</code><i>ccontext</i>);
<code>void pcre2_code_free(pcre2_code *</code><i>code</i>);
<code>pcre2_match_data *pcre2_match_data_create(uint32_t </code><i>ovecsize</i>,
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>pcre2_match_data *pcre2_match_data_create_from_pattern(</code>
<code> const pcre2_code *</code><i>code</i>, pcre2_general_context *<i>gcontext</i>);
<code>int pcre2_match(const pcre2_code *</code><i>code</i>, PCRE2_SPTR <i>subject</i>,
<code> PCRE2_SIZE </code><i>length</i>, PCRE2_SIZE <i>startoffset</i>,
<code> uint32_t </code><i>options</i>, pcre2_match_data *<i>match_data</i>,
<code> pcre2_match_context *</code><i>mcontext</i>);
<code>int pcre2_dfa_match(const pcre2_code *</code><i>code</i>, PCRE2_SPTR <i>subject</i>,
<code> PCRE2_SIZE </code><i>length</i>, PCRE2_SIZE <i>startoffset</i>,
<code> uint32_t </code><i>options</i>, pcre2_match_data *<i>match_data</i>,
<code> pcre2_match_context *</code><i>mcontext</i>,
<code> int *</code><i>workspace</i>, PCRE2_SIZE <i>wscount</i>);
<code>void pcre2_match_data_free(pcre2_match_data *</code><i>match_data</i>);</pre>
<h2>Pcre2 Native Api Auxiliary Match Functions</h2>
<pre><code>PCRE2_SPTR pcre2_get_mark(pcre2_match_data *</code><i>match_data</i>);
<code>uint32_t pcre2_get_ovector_count(pcre2_match_data *</code><i>match_data</i>);
<code>PCRE2_SIZE *pcre2_get_ovector_pointer(pcre2_match_data *</code><i>match_data</i>);
<code>PCRE2_SIZE pcre2_get_startchar(pcre2_match_data *</code><i>match_data</i>);</pre>
<h2>Pcre2 Native Api General Context Functions</h2>
<pre><code>pcre2_general_context *pcre2_general_context_create(</code>
<code> void *(*</code><i>private_malloc</i>)(PCRE2_SIZE, void *),
<code> void (*</code><i>private_free</i>)(void *, void *), void *<i>memory_data</i>);
<code>pcre2_general_context *pcre2_general_context_copy(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>void pcre2_general_context_free(pcre2_general_context *</code><i>gcontext</i>);</pre>
<h2>Pcre2 Native Api Compile Context Functions</h2>
<pre><code>pcre2_compile_context *pcre2_compile_context_create(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>pcre2_compile_context *pcre2_compile_context_copy(</code>
<code> pcre2_compile_context *</code><i>ccontext</i>);
<code>void pcre2_compile_context_free(pcre2_compile_context *</code><i>ccontext</i>);
<code>int pcre2_set_bsr(pcre2_compile_context *</code><i>ccontext</i>,
<code> uint32_t </code><i>value</i>);
<code>int pcre2_set_character_tables(pcre2_compile_context *</code><i>ccontext</i>,
<code> const uint8_t *</code><i>tables</i>);
<code>int pcre2_set_compile_extra_options(pcre2_compile_context *</code><i>ccontext</i>,
<code> uint32_t </code><i>extra_options</i>);
<code>int pcre2_set_max_pattern_length(pcre2_compile_context *</code><i>ccontext</i>,
<code> PCRE2_SIZE </code><i>value</i>);
<code>int pcre2_set_newline(pcre2_compile_context *</code><i>ccontext</i>,
<code> uint32_t </code><i>value</i>);
<code>int pcre2_set_parens_nest_limit(pcre2_compile_context *</code><i>ccontext</i>,
<code> uint32_t </code><i>value</i>);
<code>int pcre2_set_compile_recursion_guard(pcre2_compile_context *</code><i>ccontext</i>,
<code> int (*</code><i>guard_function</i>)(uint32_t, void *), void *<i>user_data</i>);</pre>
<h2>Pcre2 Native Api Match Context Functions</h2>
<pre><code>pcre2_match_context *pcre2_match_context_create(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>pcre2_match_context *pcre2_match_context_copy(</code>
<code> pcre2_match_context *</code><i>mcontext</i>);
<code>void pcre2_match_context_free(pcre2_match_context *</code><i>mcontext</i>);
<code>int pcre2_set_callout(pcre2_match_context *</code><i>mcontext</i>,
<code> int (*</code><i>callout_function</i>)(pcre2_callout_block *, void *),
<code> void *</code><i>callout_data</i>);
<code>int pcre2_set_substitute_callout(pcre2_match_context *</code><i>mcontext</i>,
<code> int (*</code><i>callout_function</i>)(pcre2_substitute_callout_block *, void *),
<code> void *</code><i>callout_data</i>);
<code>int pcre2_set_offset_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> PCRE2_SIZE </code><i>value</i>);
<code>int pcre2_set_heap_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> uint32_t </code><i>value</i>);
<code>int pcre2_set_match_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> uint32_t </code><i>value</i>);
<code>int pcre2_set_depth_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> uint32_t </code><i>value</i>);</pre>
<h2>Pcre2 Native Api String Extraction Functions</h2>
<pre><code>int pcre2_substring_copy_byname(pcre2_match_data *</code><i>match_data</i>,
<code> PCRE2_SPTR </code><i>name</i>, PCRE2_UCHAR *<i>buffer</i>, PCRE2_SIZE *<i>bufflen</i>);
<code>int pcre2_substring_copy_bynumber(pcre2_match_data *</code><i>match_data</i>,
<code> uint32_t </code><i>number</i>, PCRE2_UCHAR *<i>buffer</i>,
<code> PCRE2_SIZE *</code><i>bufflen</i>);
<code>void pcre2_substring_free(PCRE2_UCHAR *</code><i>buffer</i>);
<code>int pcre2_substring_get_byname(pcre2_match_data *</code><i>match_data</i>,
<code> PCRE2_SPTR </code><i>name</i>, PCRE2_UCHAR **<i>bufferptr</i>, PCRE2_SIZE *<i>bufflen</i>);
<code>int pcre2_substring_get_bynumber(pcre2_match_data *</code><i>match_data</i>,
<code> uint32_t </code><i>number</i>, PCRE2_UCHAR **<i>bufferptr</i>,
<code> PCRE2_SIZE *</code><i>bufflen</i>);
<code>int pcre2_substring_length_byname(pcre2_match_data *</code><i>match_data</i>,
<code> PCRE2_SPTR </code><i>name</i>, PCRE2_SIZE *<i>length</i>);
<code>int pcre2_substring_length_bynumber(pcre2_match_data *</code><i>match_data</i>,
<code> uint32_t </code><i>number</i>, PCRE2_SIZE *<i>length</i>);
<code>int pcre2_substring_nametable_scan(const pcre2_code *</code><i>code</i>,
<code> PCRE2_SPTR </code><i>name</i>, PCRE2_SPTR *<i>first</i>, PCRE2_SPTR *<i>last</i>);
<code>int pcre2_substring_number_from_name(const pcre2_code *</code><i>code</i>,
<code> PCRE2_SPTR </code><i>name</i>);
<code>void pcre2_substring_list_free(PCRE2_SPTR *</code><i>list</i>);
<code>int pcre2_substring_list_get(pcre2_match_data *</code><i>match_data</i>,
<code> PCRE2_UCHAR ***</code><i>listptr</i>, PCRE2_SIZE **<i>lengthsptr</i>);</pre>
<h2>Pcre2 Native Api String Substitution Function</h2>
<pre><code>int pcre2_substitute(const pcre2_code *</code><i>code</i>, PCRE2_SPTR <i>subject</i>,
<code> PCRE2_SIZE </code><i>length</i>, PCRE2_SIZE <i>startoffset</i>,
<code> uint32_t </code><i>options</i>, pcre2_match_data *<i>match_data</i>,
<code> pcre2_match_context *</code><i>mcontext</i>, PCRE2_SPTR <i>replacementzfP,</i>
<code> PCRE2_SIZE </code><i>rlength</i>, PCRE2_UCHAR *<i>outputbuffer</i>,
<code> PCRE2_SIZE *</code><i>outlengthptr</i>);</pre>
<h2>Pcre2 Native Api Jit Functions</h2>
<pre><code>int pcre2_jit_compile(pcre2_code *</code><i>code</i>, uint32_t <i>options</i>);
<code>int pcre2_jit_match(const pcre2_code *</code><i>code</i>, PCRE2_SPTR <i>subject</i>,
<code> PCRE2_SIZE </code><i>length</i>, PCRE2_SIZE <i>startoffset</i>,
<code> uint32_t </code><i>options</i>, pcre2_match_data *<i>match_data</i>,
<code> pcre2_match_context *</code><i>mcontext</i>);
<code>void pcre2_jit_free_unused_memory(pcre2_general_context *</code><i>gcontext</i>);
<code>pcre2_jit_stack *pcre2_jit_stack_create(PCRE2_SIZE </code><i>startsize</i>,
<code> PCRE2_SIZE </code><i>maxsize</i>, pcre2_general_context *<i>gcontext</i>);
<code>void pcre2_jit_stack_assign(pcre2_match_context *</code><i>mcontext</i>,
<code> pcre2_jit_callback </code><i>callback_function</i>, void *<i>callback_data</i>);
<code>void pcre2_jit_stack_free(pcre2_jit_stack *</code><i>jit_stack</i>);</pre>
<h2>Pcre2 Native Api Serialization Functions</h2>
<pre><code>int32_t pcre2_serialize_decode(pcre2_code **</code><i>codes</i>,
<code> int32_t </code><i>number_of_codes</i>, const uint8_t *<i>bytes</i>,
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>int32_t pcre2_serialize_encode(const pcre2_code **</code><i>codes</i>,
<code> int32_t </code><i>number_of_codes</i>, uint8_t **<i>serialized_bytes</i>,
<code> PCRE2_SIZE *</code><i>serialized_size</i>, pcre2_general_context *<i>gcontext</i>);
<code>void pcre2_serialize_free(uint8_t *</code><i>bytes</i>);
<code>int32_t pcre2_serialize_get_number_of_codes(const uint8_t *</code><i>bytes</i>);</pre>
<h2>Pcre2 Native Api Auxiliary Functions</h2>
<pre><code>pcre2_code *pcre2_code_copy(const pcre2_code *</code><i>code</i>);
<code>pcre2_code *pcre2_code_copy_with_tables(const pcre2_code *</code><i>code</i>);
<code>int pcre2_get_error_message(int </code><i>errorcode</i>, PCRE2_UCHAR *<i>buffer</i>,
<code> PCRE2_SIZE </code><i>bufflen</i>);
<code>const uint8_t *pcre2_maketables(pcre2_general_context *</code><i>gcontext</i>);
<code>void pcre2_maketables_free(pcre2_general_context *</code><i>gcontext</i>,
<code> const uint8_t *</code><i>tables</i>);
<code>int pcre2_pattern_info(const pcre2_code *</code><i>code</i>, uint32_t <i>what</i>,
<code> void *</code><i>where</i>);
<code>int pcre2_callout_enumerate(const pcre2_code *</code><i>code</i>,
<code> int (*</code><i>callback</i>)(pcre2_callout_enumerate_block *, void *),
<code> void *</code><i>user_data</i>);
<code>int pcre2_config(uint32_t </code><i>what</i>, void *<i>where</i>);</pre>
<h2>Pcre2 Native Api Obsolete Functions</h2>
<pre><code>int pcre2_set_recursion_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> uint32_t </code><i>value</i>);
<code>int pcre2_set_recursion_memory_management(</code>
<code> pcre2_match_context *</code><i>mcontext</i>,
<code> void *(*</code><i>private_malloc</i>)(PCRE2_SIZE, void *),
<code> void (*</code><i>private_free</i>)(void *, void *), void *<i>memory_data</i>);</pre>
<p>These functions became obsolete at release 10.30 and are retained only for backward compatibility. They should not be used in new code. The first is replaced by <code>pcre2_set_depth_limit()</code>; the second is no longer needed and has no effect (it always returns zero).</p>
<h2>Pcre2 Experimental Pattern Conversion Functions</h2>
<pre><code>pcre2_convert_context *pcre2_convert_context_create(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>pcre2_convert_context *pcre2_convert_context_copy(</code>
<code> pcre2_convert_context *</code><i>cvcontext</i>);
<code>void pcre2_convert_context_free(pcre2_convert_context *</code><i>cvcontext</i>);
<code>int pcre2_set_glob_escape(pcre2_convert_context *</code><i>cvcontext</i>,
<code> uint32_t </code><i>escape_char</i>);
<code>int pcre2_set_glob_separator(pcre2_convert_context *</code><i>cvcontext</i>,
<code> uint32_t </code><i>separator_char</i>);
<code>int pcre2_pattern_convert(PCRE2_SPTR </code><i>pattern</i>, PCRE2_SIZE <i>length</i>,
<code> uint32_t </code><i>options</i>, PCRE2_UCHAR **<i>buffer</i>,
<code> PCRE2_SIZE *</code><i>blength</i>, pcre2_convert_context *<i>cvcontext</i>);
<code>void pcre2_converted_pattern_free(PCRE2_UCHAR *</code><i>converted_pattern</i>);</pre>
<p>These functions provide a way of converting non-PCRE2 patterns into patterns that can be processed by <code>pcre2_compile()</code>. This facility is experimental and may be changed in future releases. At present, &quot;globs&quot; and POSIX basic and extended patterns can be converted. Details are given in the <code>pcre2convert</code> documentation.</p>
<h2>Pcre2 8-Bit, 16-Bit, And 32-Bit Libraries</h2>
<p>There are three PCRE2 libraries, supporting 8-bit, 16-bit, and 32-bit code units, respectively. However, there is just one header file, <code>pcre2.h</code>. This contains the function prototypes and other definitions for all three libraries. One, two, or all three can be installed simultaneously. On Unix-like systems the libraries are called <code>libpcre2-8</code>, <code>libpcre2-16</code>, and <code>libpcre2-32</code>, and they can also co-exist with the original PCRE libraries. </p>
<p> Character strings are passed to and from a PCRE2 library as a sequence of unsigned integers in code units of the appropriate width. Every PCRE2 function comes in three different forms, one for each library, for example: </p>
<p>&nbsp;<wbr>&nbsp;<code>pcre2_compile_8()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_compile_16()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_compile_32()</code> </p>
<p> There are also three different sets of data types: </p>
<p>&nbsp;<wbr>&nbsp;<code>PCRE2_UCHAR8, PCRE2_UCHAR16, PCRE2_UCHAR32</code><br />
&nbsp;<wbr>&nbsp;<code>PCRE2_SPTR8,&nbsp;<wbr>&nbsp;PCRE2_SPTR16,&nbsp;<wbr>&nbsp;PCRE2_SPTR32</code> </p>
<p> The UCHAR types define unsigned code units of the appropriate widths. For example, PCRE2_UCHAR16 is usually defined as `uint16_t&#8217;. The SPTR types are constant pointers to the equivalent UCHAR types, that is, they are pointers to vectors of unsigned code units. </p>
<p> Many applications use only one code unit width. For their convenience, macros are defined whose names are the generic forms such as <code>pcre2_compile()</code> and PCRE2_SPTR. These macros use the value of the macro PCRE2_CODE_UNIT_WIDTH to generate the appropriate width-specific function and macro names. PCRE2_CODE_UNIT_WIDTH is not defined by default. An application must define it to be 8, 16, or 32 before including <code>pcre2.h</code> in order to make use of the generic names. </p>
<p> Applications that use more than one code unit width can be linked with more than one PCRE2 library, but must define PCRE2_CODE_UNIT_WIDTH to be 0 before including <code>pcre2.h</code>, and then use the real function names. Any code that is to be included in an environment where the value of PCRE2_CODE_UNIT_WIDTH is unknown should also use the real function names. (Unfortunately, it is not possible in C code to save and restore the value of a macro.) </p>
<p> If PCRE2_CODE_UNIT_WIDTH is not defined before including <code>pcre2.h</code>, a compiler error occurs. </p>
<p> When using multiple libraries in an application, you must take care when processing any particular pattern to use only functions from a single library. For example, if you want to run a match using a pattern that was compiled with <code>pcre2_compile_16()</code>, you must do so with <code>pcre2_match_16()</code>, not <code>pcre2_match_8()</code> or <code>pcre2_match_32()</code>. </p>
<p> In the function summaries above, and in the rest of this document and other PCRE2 documents, functions and data types are described using their generic names, without the _8, _16, or _32 suffix.</p>
<h2>Pcre2 Api Overview</h2>
<p>PCRE2 has its own native API, which is described in this document. There are also some wrapper functions for the 8-bit library that correspond to the POSIX regular expression API, but they do not give access to all the functionality of PCRE2. They are described in the <code>pcre2posix</code> documentation. Both these APIs define a set of C function calls. </p>
<p> The native API C data types, function prototypes, option values, and error codes are defined in the header file <code>pcre2.h</code>, which also contains definitions of PCRE2_MAJOR and PCRE2_MINOR, the major and minor release numbers for the library. Applications can use these to include support for different releases of PCRE2. </p>
<p> In a Windows environment, if you want to statically link an application program against a non-dll PCRE2 library, you must define PCRE2_STATIC before including <code>pcre2.h</code>. </p>
<p> The functions <code>pcre2_compile()</code> and <code>pcre2_match()</code> are used for compiling and matching regular expressions in a Perl-compatible manner. A sample program that demonstrates the simplest way of using them is provided in the file called <i>pcre2demo.c</i> in the PCRE2 source distribution. A listing of this program is given in the <code>pcre2demo</code> documentation, and the <code>pcre2sample</code> documentation describes how to compile and run it. </p>
<p> The compiling and matching functions recognize various options that are passed as bits in an options argument. There are also some more complicated parameters such as custom memory management functions and resource limits that are passed in &quot;contexts&quot; (which are just memory blocks, described below). Simple applications do not need to make use of contexts. </p>
<p> Just-in-time (JIT) compiler support is an optional feature of PCRE2 that can be built in appropriate hardware environments. It greatly speeds up the matching performance of many patterns. Programs can request that it be used if available by calling <code>pcre2_jit_compile()</code> after a pattern has been successfully compiled by <code>pcre2_compile()</code>. This does nothing if JIT support is not available. </p>
<p> More complicated programs might need to make use of the specialist functions <code>pcre2_jit_stack_create()</code>, <code>pcre2_jit_stack_free()</code>, and <code>pcre2_jit_stack_assign()</code> in order to control the JIT code&#8217;s memory usage. </p>
<p> JIT matching is automatically used by <code>pcre2_match()</code> if it is available, unless the PCRE2_NO_JIT option is set. There is also a direct interface for JIT matching, which gives improved performance at the expense of less sanity checking. The JIT-specific functions are discussed in the <code>pcre2jit</code> documentation. </p>
<p> A second matching function, <code>pcre2_dfa_match()</code>, which is not Perl-compatible, is also provided. This uses a different algorithm for the matching. The alternative algorithm finds all possible matches (at a given point in the subject), and scans the subject just once (unless there are lookaround assertions). However, this algorithm does not return captured substrings. A description of the two matching algorithms and their advantages and disadvantages is given in the <code>pcre2matching</code> documentation. There is no JIT support for <code>pcre2_dfa_match()</code>. </p>
<p> In addition to the main compiling and matching functions, there are convenience functions for extracting captured substrings from a subject string that has been matched by <code>pcre2_match()</code>. They are: </p>
<p>&nbsp;<wbr>&nbsp;<code>pcre2_substring_copy_byname()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_substring_copy_bynumber()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_substring_get_byname()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_substring_get_bynumber()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_substring_list_get()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_substring_length_byname()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_substring_length_bynumber()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_substring_nametable_scan()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre2_substring_number_from_name()</code> </p>
<p> <code>pcre2_substring_free()</code> and <code>pcre2_substring_list_free()</code> are also provided, to free memory used for extracted strings. If either of these functions is called with a NULL argument, the function returns immediately without doing anything. </p>
<p> The function <code>pcre2_substitute()</code> can be called to match a pattern and return a copy of the subject string with substitutions for parts that were matched. </p>
<p> Functions whose names begin with <code>pcre2_serialize_</code> are used for saving compiled patterns on disc or elsewhere, and reloading them later. </p>
<p> Finally, there are functions for finding out information about a compiled pattern (<code>pcre2_pattern_info()</code>) and about the configuration with which PCRE2 was built (<code>pcre2_config()</code>). </p>
<p> Functions with names ending with <code>_free()</code> are used for freeing memory blocks of various sorts. In all cases, if one of these functions is called with a NULL argument, it does nothing.</p>
<h2>String Lengths And Offsets</h2>
<p>The PCRE2 API uses string lengths and offsets into strings of code units in several places. These values are always of type PCRE2_SIZE, which is an unsigned integer type, currently always defined as <i>size_t</i>. The largest value that can be stored in such a type (that is ~(PCRE2_SIZE)0) is reserved as a special indicator for zero-terminated strings and unset offsets. Therefore, the longest string that can be handled is one less than this maximum.</p>
<h2>Newlines</h2>
<p>PCRE2 supports five different conventions for indicating line breaks in strings: a single CR (carriage return) character, a single LF (linefeed) character, the two-character sequence CRLF, any of the three preceding, or any Unicode newline sequence. The Unicode newline sequences are the three just mentioned, plus the single characters VT (vertical tab, U+000B), FF (form feed, U+000C), NEL (next line, U+0085), LS (line separator, U+2028), and PS (paragraph separator, U+2029). </p>
<p> Each of the first three conventions is used by at least one operating system as its standard newline sequence. When PCRE2 is built, a default can be specified. If it is not, the default is set to LF, which is the Unix standard. However, the newline convention can be changed by an application when calling <code>pcre2_compile()</code>, or it can be specified by special text at the start of the pattern itself; this overrides any other settings. See the <code>pcre2pattern</code> page for details of the special character sequences. </p>
<p> In the PCRE2 documentation the word &quot;newline&quot; is used to mean &quot;the character or pair of characters that indicate a line break&quot;. The choice of newline convention affects the handling of the dot, circumflex, and dollar metacharacters, the handling of #-comments in /x mode, and, when CRLF is a recognized line ending sequence, the match position advancement for a non-anchored pattern. There is more detail about this in the section on <code>pcre2_match()</code> options below. </p>
<p> The choice of newline convention does not affect the interpretation of the 
 or  escape sequences, nor does it affect what \R matches; this has its own separate convention.</p>
<h2>Multithreading</h2>
<p>In a multithreaded application it is important to keep thread-specific data separate from data that can be shared between threads. The PCRE2 library code itself is thread-safe: it contains no static or global variables. The API is designed to be fairly simple for non-threaded applications while at the same time ensuring that multithreaded applications can use it. </p>
<p> There are several different blocks of data that are used to pass information between the application and the PCRE2 libraries.</p>
<h3>The compiled pattern</h3>
<p>A pointer to the compiled form of a pattern is returned to the user when <code>pcre2_compile()</code> is successful. The data in the compiled pattern is fixed, and does not change when the pattern is matched. Therefore, it is thread-safe, that is, the same compiled pattern can be used by more than one thread simultaneously. For example, an application can compile all its patterns at the start, before forking off multiple threads that use them. However, if the just-in-time (JIT) optimization feature is being used, it needs separate memory stack areas for each thread. See the <code>pcre2jit</code> documentation for more details. </p>
<p> In a more complicated situation, where patterns are compiled only when they are first needed, but are still shared between threads, pointers to compiled patterns must be protected from simultaneous writing by multiple threads, at least until a pattern has been compiled. The logic can be something like this: </p>
<p>&nbsp;<wbr>&nbsp;Get a read-only&nbsp;(shared)&nbsp;lock&nbsp;(mutex)&nbsp;for pointer<br />
&nbsp;<wbr>&nbsp;if&nbsp;(pointer&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Get a write&nbsp;(unique)&nbsp;lock for pointer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer&nbsp;=&nbsp;pcre2_compile(&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;Release the lock<br />
&nbsp;<wbr>&nbsp;Use pointer in pcre2_match() </p>
<p> Of course, testing for compilation errors should also be included in the code. </p>
<p> If JIT is being used, but the JIT compilation is not being done immediately, (perhaps waiting to see if the pattern is used often enough) similar logic is required. JIT compilation updates a pointer within the compiled code block, so a thread must gain unique write access to the pointer before calling <code>pcre2_jit_compile()</code>. Alternatively, <code>pcre2_code_copy()</code> or <code>pcre2_code_copy_with_tables()</code> can be used to obtain a private copy of the compiled code before calling the JIT compiler.</p>
<h3>Context blocks</h3>
<p>The next main section below introduces the idea of &quot;contexts&quot; in which PCRE2 functions are called. A context is nothing more than a collection of parameters that control the way PCRE2 operates. Grouping a number of parameters together in a context is a convenient way of passing them to a PCRE2 function without using lots of arguments. The parameters that are stored in contexts are in some sense &quot;advanced features&quot; of the API. Many straightforward applications will not need to use contexts. </p>
<p> In a multithreaded application, if the parameters in a context are values that are never changed, the same context can be used by all the threads. However, if any thread needs to change any value in a context, it must make its own thread-specific copy.</p>
<h3>Match blocks</h3>
<p>The matching functions need a block of memory for storing the results of a match. This includes details of what was matched, as well as additional information such as the name of a (*MARK) setting. Each thread must provide its own copy of this memory.</p>
<h2>Pcre2 Contexts</h2>
<p>Some PCRE2 functions have a lot of parameters, many of which are used only by specialist applications, for example, those that use custom memory management or non-standard character tables. To keep function argument lists at a reasonable size, and at the same time to keep the API extensible, &quot;uncommon&quot; parameters are passed to certain functions in a <code>context</code> instead of directly. A context is just a block of memory that holds the parameter values. Applications that do not need to adjust any of the context parameters can pass NULL when a context pointer is required. </p>
<p> There are three different types of context: a general context that is relevant for several PCRE2 operations, a compile-time context, and a match-time context.</p>
<h3>The general context</h3>
<p>At present, this context just contains pointers to (and data for) external memory management functions that are called from several places in the PCRE2 library. The context is named `general&#8217; rather than specifically `memory&#8217; because in future other fields may be added. If you do not want to supply your own custom memory management functions, you do not need to bother with a general context. A general context is created by: </p>
<pre><code>pcre2_general_context *pcre2_general_context_create(</code>
<code> void *(*</code><i>private_malloc</i>)(PCRE2_SIZE, void *),
<code> void (*</code><i>private_free</i>)(void *, void *), void *<i>memory_data</i>);</pre>
<p>The two function pointers specify custom memory management functions, whose prototypes are: </p>
<p>&nbsp;<wbr>&nbsp;<code>void&nbsp;*private_malloc(PCRE2_SIZE, void&nbsp;*);</code><br />
&nbsp;<wbr>&nbsp;<code>void&nbsp;<wbr>&nbsp;private_free(void&nbsp;*, void&nbsp;*);</code> </p>
<p> Whenever code in PCRE2 calls these functions, the final argument is the value of <i>memory_data</i>. Either of the first two arguments of the creation function may be NULL, in which case the system memory management functions <i>malloc()</i> and <i>free()</i> are used. (This is not currently useful, as there are no other fields in a general context, but in future there might be.) The <i>private_malloc()</i> function is used (if supplied) to obtain memory for storing the context, and all three values are saved as part of the context. </p>
<p> Whenever PCRE2 creates a data block of any kind, the block contains a pointer to the <i>free()</i> function that matches the <i>malloc()</i> function that was used. When the time comes to free the block, this function is called. </p>
<p> A general context can be copied by calling: </p>
<pre><code>pcre2_general_context *pcre2_general_context_copy(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);</pre>
<p>The memory used for a general context should be freed by calling: </p>
<pre><code>void pcre2_general_context_free(pcre2_general_context *</code><i>gcontext</i>);</pre>
<p>If this function is passed a NULL argument, it returns immediately without doing anything.</p>
<h3>The compile context</h3>
<p>A compile context is required if you want to provide an external function for stack checking during compilation or to change the default values of any of the following compile-time parameters: </p>
<p>&nbsp;<wbr>&nbsp;What&nbsp;\R matches&nbsp;(Unicode newlines or CR, LF, CRLF only)<br />
&nbsp;<wbr>&nbsp;PCRE2&#8217;s character tables<br />
&nbsp;<wbr>&nbsp;The newline character sequence<br />
&nbsp;<wbr>&nbsp;The compile time nested parentheses limit<br />
&nbsp;<wbr>&nbsp;The maximum length of the pattern string<br />
&nbsp;<wbr>&nbsp;The extra options bits&nbsp;(none set by default) </p>
<p> A compile context is also required if you are using custom memory management. If none of these apply, just pass NULL as the context argument of <i>pcre2_compile()</i>. </p>
<p> A compile context is created, copied, and freed by the following functions: </p>
<pre><code>pcre2_compile_context *pcre2_compile_context_create(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>pcre2_compile_context *pcre2_compile_context_copy(</code>
<code> pcre2_compile_context *</code><i>ccontext</i>);
<code>void pcre2_compile_context_free(pcre2_compile_context *</code><i>ccontext</i>);</pre>
<p>A compile context is created with default values for its parameters. These can be changed by calling the following functions, which return 0 on success, or PCRE2_ERROR_BADDATA if invalid data is detected. </p>
<pre><code>int pcre2_set_bsr(pcre2_compile_context *</code><i>ccontext</i>,
<code> uint32_t </code><i>value</i>);</pre>
<p>The value must be PCRE2_BSR_ANYCRLF, to specify that \R matches only CR, LF, or CRLF, or PCRE2_BSR_UNICODE, to specify that \R matches any Unicode line ending sequence. The value is used by the JIT compiler and by the two interpreted matching functions, <i>pcre2_match()</i> and <i>pcre2_dfa_match()</i>. </p>
<pre><code>int pcre2_set_character_tables(pcre2_compile_context *</code><i>ccontext</i>,
<code> const uint8_t *</code><i>tables</i>);</pre>
<p>The value must be the result of a call to <code>pcre2_maketables()</code>, whose only argument is a general context. This function builds a set of character tables in the current locale. </p>
<pre><code>int pcre2_set_compile_extra_options(pcre2_compile_context *</code><i>ccontext</i>,
<code> uint32_t </code><i>extra_options</i>);</pre>
<p>As PCRE2 has developed, almost all the 32 option bits that are available in the <i>options</i> argument of <code>pcre2_compile()</code> have been used up. To avoid running out, the compile context contains a set of extra option bits which are used for some newer, assumed rarer, options. This function sets those bits. It always sets all the bits (either on or off). It does not modify any existing setting. The available options are defined in the section entitled &quot;Extra compile options&quot; below. </p>
<pre><code>int pcre2_set_max_pattern_length(pcre2_compile_context *</code><i>ccontext</i>,
<code> PCRE2_SIZE </code><i>value</i>);</pre>
<p>This sets a maximum length, in code units, for any pattern string that is compiled with this context. If the pattern is longer, an error is generated. This facility is provided so that applications that accept patterns from external sources can limit their size. The default is the largest number that a PCRE2_SIZE variable can hold, which is effectively unlimited. </p>
<pre><code>int pcre2_set_newline(pcre2_compile_context *</code><i>ccontext</i>,
<code> uint32_t </code><i>value</i>);</pre>
<p>This specifies which characters or character sequences are to be recognized as newlines. The value must be one of PCRE2_NEWLINE_CR (carriage return only), PCRE2_NEWLINE_LF (linefeed only), PCRE2_NEWLINE_CRLF (the two-character sequence CR followed by LF), PCRE2_NEWLINE_ANYCRLF (any of the above), PCRE2_NEWLINE_ANY (any Unicode newline sequence), or PCRE2_NEWLINE_NUL (the NUL character, that is a binary zero). </p>
<p> A pattern can override the value set in the compile context by starting with a sequence such as (*CRLF). See the <code>pcre2pattern</code> page for details. </p>
<p> When a pattern is compiled with the PCRE2_EXTENDED or PCRE2_EXTENDED_MORE option, the newline convention affects the recognition of the end of internal comments starting with #. The value is saved with the compiled pattern for subsequent use by the JIT compiler and by the two interpreted matching functions, <i>pcre2_match()</i> and <i>pcre2_dfa_match()</i>. </p>
<pre><code>int pcre2_set_parens_nest_limit(pcre2_compile_context *</code><i>ccontext</i>,
<code> uint32_t </code><i>value</i>);</pre>
<p>This parameter adjusts the limit, set when PCRE2 is built (default 250), on the depth of parenthesis nesting in a pattern. This limit stops rogue patterns using up too much system stack when being compiled. The limit applies to parentheses of all kinds, not just capturing parentheses. </p>
<pre><code>int pcre2_set_compile_recursion_guard(pcre2_compile_context *</code><i>ccontext</i>,
<code> int (*</code><i>guard_function</i>)(uint32_t, void *), void *<i>user_data</i>);</pre>
<p>There is at least one application that runs PCRE2 in threads with very limited system stack, where running out of stack is to be avoided at all costs. The parenthesis limit above cannot take account of how much stack is actually available during compilation. For a finer control, you can supply a function that is called whenever <code>pcre2_compile()</code> starts to compile a parenthesized part of a pattern. This function can check the actual stack size (or anything else that it wants to, of course). </p>
<p> The first argument to the callout function gives the current depth of nesting, and the second is user data that is set up by the last argument of <code>pcre2_set_compile_recursion_guard()</code>. The callout function should return zero if all is well, or non-zero to force an error.</p>
<h3>The match context</h3>
<p>A match context is required if you want to: </p>
<p>&nbsp;<wbr>&nbsp;Set up a callout function<br />
&nbsp;<wbr>&nbsp;Set an offset limit for matching an unanchored pattern<br />
&nbsp;<wbr>&nbsp;Change the limit on the amount of heap used when matching<br />
&nbsp;<wbr>&nbsp;Change the backtracking match limit<br />
&nbsp;<wbr>&nbsp;Change the backtracking depth limit<br />
&nbsp;<wbr>&nbsp;Set custom memory management specifically for the match </p>
<p> If none of these apply, just pass NULL as the context argument of <code>pcre2_match()</code>, <code>pcre2_dfa_match()</code>, or <code>pcre2_jit_match()</code>. </p>
<p> A match context is created, copied, and freed by the following functions: </p>
<pre><code>pcre2_match_context *pcre2_match_context_create(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>pcre2_match_context *pcre2_match_context_copy(</code>
<code> pcre2_match_context *</code><i>mcontext</i>);
<code>void pcre2_match_context_free(pcre2_match_context *</code><i>mcontext</i>);</pre>
<p>A match context is created with default values for its parameters. These can be changed by calling the following functions, which return 0 on success, or PCRE2_ERROR_BADDATA if invalid data is detected. </p>
<pre><code>int pcre2_set_callout(pcre2_match_context *</code><i>mcontext</i>,
<code> int (*</code><i>callout_function</i>)(pcre2_callout_block *, void *),
<code> void *</code><i>callout_data</i>);</pre>
<p>This sets up a callout function for PCRE2 to call at specified points during a matching operation. Details are given in the <code>pcre2callout</code> documentation. </p>
<pre><code>int pcre2_set_substitute_callout(pcre2_match_context *</code><i>mcontext</i>,
<code> int (*</code><i>callout_function</i>)(pcre2_substitute_callout_block *, void *),
<code> void *</code><i>callout_data</i>);</pre>
<p>This sets up a callout function for PCRE2 to call after each substitution made by <code>pcre2_substitute()</code>. Details are given in the section entitled &quot;Creating a new string with substitutions&quot; below. </p>
<pre><code>int pcre2_set_offset_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> PCRE2_SIZE </code><i>value</i>);</pre>
<p>The <i>offset_limit</i> parameter limits how far an unanchored search can advance in the subject string. The default value is PCRE2_UNSET. The <code>pcre2_match()</code> and <code>pcre2_dfa_match()</code> functions return PCRE2_ERROR_NOMATCH if a match with a starting point before or at the given offset is not found. The <code>pcre2_substitute()</code> function makes no more substitutions. </p>
<p> For example, if the pattern /abc/ is matched against &quot;123abc&quot; with an offset limit less than 3, the result is PCRE2_ERROR_NOMATCH. A match can never be found if the <i>startoffset</i> argument of <code>pcre2_match()</code>, <code>pcre2_dfa_match()</code>, or <code>pcre2_substitute()</code> is greater than the offset limit set in the match context. </p>
<p> When using this facility, you must set the PCRE2_USE_OFFSET_LIMIT option when calling <code>pcre2_compile()</code> so that when JIT is in use, different code can be compiled. If a match is started with a non-default match limit when PCRE2_USE_OFFSET_LIMIT is not set, an error is generated. </p>
<p> The offset limit facility can be used to track progress when searching large subject strings or to limit the extent of global substitutions. See also the PCRE2_FIRSTLINE option, which requires a match to start before or at the first newline that follows the start of matching in the subject. If this is set with an offset limit, a match must occur in the first line and also within the offset limit. In other words, whichever limit comes first is used. </p>
<pre><code>int pcre2_set_heap_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> uint32_t </code><i>value</i>);</pre>
<p>The <i>heap_limit</i> parameter specifies, in units of kibibytes (1024 bytes), the maximum amount of heap memory that <code>pcre2_match()</code> may use to hold backtracking information when running an interpretive match. This limit also applies to <code>pcre2_dfa_match()</code>, which may use the heap when processing patterns with a lot of nested pattern recursion or lookarounds or atomic groups. This limit does not apply to matching with the JIT optimization, which has its own memory control arrangements (see the <code>pcre2jit</code> documentation for more details). If the limit is reached, the negative error code PCRE2_ERROR_HEAPLIMIT is returned. The default limit can be set when PCRE2 is built; if it is not, the default is set very large and is essentially &quot;unlimited&quot;. </p>
<p> A value for the heap limit may also be supplied by an item at the start of a pattern of the form </p>
<p>&nbsp;<wbr>&nbsp;(*LIMIT_HEAP=ddd) </p>
<p> where ddd is a decimal number. However, such a setting is ignored unless ddd is less than the limit set by the caller of <code>pcre2_match()</code> or, if no such limit is set, less than the default. </p>
<p> The <code>pcre2_match()</code> function starts out using a 20KiB vector on the system stack for recording backtracking points. The more nested backtracking points there are (that is, the deeper the search tree), the more memory is needed. Heap memory is used only if the initial vector is too small. If the heap limit is set to a value less than 21 (in particular, zero) no heap memory will be used. In this case, only patterns that do not have a lot of nested backtracking can be successfully processed. </p>
<p> Similarly, for <code>pcre2_dfa_match()</code>, a vector on the system stack is used when processing pattern recursions, lookarounds, or atomic groups, and only if this is not big enough is heap memory used. In this case, too, setting a value of zero disables the use of the heap. </p>
<pre><code>int pcre2_set_match_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> uint32_t </code><i>value</i>);</pre>
<p>The <i>match_limit</i> parameter provides a means of preventing PCRE2 from using up too many computing resources when processing patterns that are not going to match, but which have a very large number of possibilities in their search trees. The classic example is a pattern that uses nested unlimited repeats. </p>
<p> There is an internal counter in <code>pcre2_match()</code> that is incremented each time round its main matching loop. If this value reaches the match limit, <code>pcre2_match()</code> returns the negative value PCRE2_ERROR_MATCHLIMIT. This has the effect of limiting the amount of backtracking that can take place. For patterns that are not anchored, the count restarts from zero for each position in the subject string. This limit also applies to <code>pcre2_dfa_match()</code>, though the counting is done in a different way. </p>
<p> When <code>pcre2_match()</code> is called with a pattern that was successfully processed by <code>pcre2_jit_compile()</code>, the way in which matching is executed is entirely different. However, there is still the possibility of runaway matching that goes on for a very long time, and so the <i>match_limit</i> value is also used in this case (but in a different way) to limit how long the matching can continue. </p>
<p> The default value for the limit can be set when PCRE2 is built; the default default is 10 million, which handles all but the most extreme cases. A value for the match limit may also be supplied by an item at the start of a pattern of the form </p>
<p>&nbsp;<wbr>&nbsp;(*LIMIT_MATCH=ddd) </p>
<p> where ddd is a decimal number. However, such a setting is ignored unless ddd is less than the limit set by the caller of <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code> or, if no such limit is set, less than the default. </p>
<pre><code>int pcre2_set_depth_limit(pcre2_match_context *</code><i>mcontext</i>,
<code> uint32_t </code><i>value</i>);</pre>
<p>This parameter limits the depth of nested backtracking in <code>pcre2_match()</code>. Each time a nested backtracking point is passed, a new memory &quot;frame&quot; is used to remember the state of matching at that point. Thus, this parameter indirectly limits the amount of memory that is used in a match. However, because the size of each memory &quot;frame&quot; depends on the number of capturing parentheses, the actual memory limit varies from pattern to pattern. This limit was more useful in versions before 10.30, where function recursion was used for backtracking. </p>
<p> The depth limit is not relevant, and is ignored, when matching is done using JIT compiled code. However, it is supported by <code>pcre2_dfa_match()</code>, which uses it to limit the depth of nested internal recursive function calls that implement atomic groups, lookaround assertions, and pattern recursions. This limits, indirectly, the amount of system stack that is used. It was more useful in versions before 10.32, when stack memory was used for local workspace vectors for recursive function calls. From version 10.32, only local variables are allocated on the stack and as each call uses only a few hundred bytes, even a small stack can support quite a lot of recursion. </p>
<p> If the depth of internal recursive function calls is great enough, local workspace vectors are allocated on the heap from version 10.32 onwards, so the depth limit also indirectly limits the amount of heap memory that is used. A recursive pattern such as /(.(?2))((?1)|)/, when matched to a very long string using <code>pcre2_dfa_match()</code>, can use a great deal of memory. However, it is probably better to limit heap usage directly by calling <code>pcre2_set_heap_limit()</code>. </p>
<p> The default value for the depth limit can be set when PCRE2 is built; if it is not, the default is set to the same value as the default for the match limit. If the limit is exceeded, <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code> returns PCRE2_ERROR_DEPTHLIMIT. A value for the depth limit may also be supplied by an item at the start of a pattern of the form </p>
<p>&nbsp;<wbr>&nbsp;(*LIMIT_DEPTH=ddd) </p>
<p> where ddd is a decimal number. However, such a setting is ignored unless ddd is less than the limit set by the caller of <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code> or, if no such limit is set, less than the default.</p>
<h2>Checking Build-Time Options</h2>
<p><code>int pcre2_config(uint32_t </code><i>what</i>, void *<i>where</i>); </p>
<p> The function <code>pcre2_config()</code> makes it possible for a PCRE2 client to discover which optional features have been compiled into the PCRE2 library. The <code>pcre2build</code> documentation has more details about these optional features. </p>
<p> The first argument for <code>pcre2_config()</code> specifies which information is required. The second argument is a pointer to memory into which the information is placed. If NULL is passed, the function returns the amount of memory that is needed for the requested information. For calls that return numerical values, the value is in bytes; when requesting these values, <i>where</i> should point to appropriately aligned memory. For calls that return strings, the required length is given in code units, not counting the terminating zero. </p>
<p> When requesting information, the returned value from <code>pcre2_config()</code> is non-negative on success, or the negative error code PCRE2_ERROR_BADOPTION if the value in the first argument is not recognized. The following information is available: </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_BSR </p>
<p> The output is a uint32_t integer whose value indicates what character sequences the \R escape sequence matches by default. A value of PCRE2_BSR_UNICODE means that \R matches any Unicode line ending sequence; a value of PCRE2_BSR_ANYCRLF means that \R matches only CR, LF, or CRLF. The default can be overridden when a pattern is compiled. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_COMPILED_WIDTHS </p>
<p> The output is a uint32_t integer whose lower bits indicate which code unit widths were selected when PCRE2 was built. The 1-bit indicates 8-bit support, and the 2-bit and 4-bit indicate 16-bit and 32-bit support, respectively. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_DEPTHLIMIT </p>
<p> The output is a uint32_t integer that gives the default limit for the depth of nested backtracking in <code>pcre2_match()</code> or the depth of nested recursions, lookarounds, and atomic groups in <code>pcre2_dfa_match()</code>. Further details are given with <code>pcre2_set_depth_limit()</code> above. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_HEAPLIMIT </p>
<p> The output is a uint32_t integer that gives, in kibibytes, the default limit for the amount of heap memory used by <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code>. Further details are given with <code>pcre2_set_heap_limit()</code> above. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_JIT </p>
<p> The output is a uint32_t integer that is set to one if support for just-in-time compiling is available; otherwise it is set to zero. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_JITTARGET </p>
<p> The <i>where</i> argument should point to a buffer that is at least 48 code units long. (The exact length required can be found by calling <code>pcre2_config()</code> with <code>where</code> set to NULL.) The buffer is filled with a string that contains the name of the architecture for which the JIT compiler is configured, for example &quot;x86 32bit (little endian + unaligned)&quot;. If JIT support is not available, PCRE2_ERROR_BADOPTION is returned, otherwise the number of code units used is returned. This is the length of the string, plus one unit for the terminating zero. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_LINKSIZE </p>
<p> The output is a uint32_t integer that contains the number of bytes used for internal linkage in compiled regular expressions. When PCRE2 is configured, the value can be set to 2, 3, or 4, with the default being 2. This is the value that is returned by <code>pcre2_config()</code>. However, when the 16-bit library is compiled, a value of 3 is rounded up to 4, and when the 32-bit library is compiled, internal linkages always use 4 bytes, so the configured value is not relevant. </p>
<p> The default value of 2 for the 8-bit and 16-bit libraries is sufficient for all but the most massive patterns, since it allows the size of the compiled pattern to be up to 65535 code units. Larger values allow larger regular expressions to be compiled by those two libraries, but at the expense of slower matching. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_MATCHLIMIT </p>
<p> The output is a uint32_t integer that gives the default match limit for <code>pcre2_match()</code>. Further details are given with <code>pcre2_set_match_limit()</code> above. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_NEWLINE </p>
<p> The output is a uint32_t integer whose value specifies the default character sequence that is recognized as meaning &quot;newline&quot;. The values are: </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_CR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Carriage return&nbsp;(CR)<br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_LF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Linefeed&nbsp;(LF)<br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_CRLF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Carriage return, linefeed&nbsp;(CRLF)<br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_ANY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Any Unicode line ending<br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_ANYCRLF&nbsp;<wbr>&nbsp;Any of CR, LF, or CRLF<br />
&nbsp;<wbr>&nbsp;PCRE2_NEWLINE_NUL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The NUL character&nbsp;(binary zero) </p>
<p> The default should normally correspond to the standard sequence for your operating system. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_NEVER_BACKSLASH_C </p>
<p> The output is a uint32_t integer that is set to one if the use of \C was permanently disabled when PCRE2 was built; otherwise it is set to zero. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_PARENSLIMIT </p>
<p> The output is a uint32_t integer that gives the maximum depth of nesting of parentheses (of any kind) in a pattern. This limit is imposed to cap the amount of system stack used when a pattern is compiled. It is specified when PCRE2 is built; the default is 250. This limit does not take into account the stack that may already be used by the calling application. For finer control over compilation stack usage, see <code>pcre2_set_compile_recursion_guard()</code>. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_STACKRECURSE </p>
<p> This parameter is obsolete and should not be used in new code. The output is a uint32_t integer that is always set to zero. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_UNICODE_VERSION </p>
<p> The <i>where</i> argument should point to a buffer that is at least 24 code units long. (The exact length required can be found by calling <code>pcre2_config()</code> with <code>where</code> set to NULL.) If PCRE2 has been compiled without Unicode support, the buffer is filled with the text &quot;Unicode not supported&quot;. Otherwise, the Unicode version string (for example, &quot;8.0.0&quot;) is inserted. The number of code units used is returned. This is the length of the string plus one unit for the terminating zero. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_UNICODE </p>
<p> The output is a uint32_t integer that is set to one if Unicode support is available; otherwise it is set to zero. Unicode support implies UTF support. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONFIG_VERSION </p>
<p> The <i>where</i> argument should point to a buffer that is at least 24 code units long. (The exact length required can be found by calling <code>pcre2_config()</code> with <code>where</code> set to NULL.) The buffer is filled with the PCRE2 version string, zero-terminated. The number of code units used is returned. This is the length of the string plus one unit for the terminating zero.</p>
<h2>Compiling A Pattern</h2>
<pre><code>pcre2_code *pcre2_compile(PCRE2_SPTR </code><i>pattern</i>, PCRE2_SIZE <i>length</i>,
<code> uint32_t </code><i>options</i>, int *<i>errorcode</i>, PCRE2_SIZE *<i>erroroffset,</i>
<code> pcre2_compile_context *</code><i>ccontext</i>);
<code>void pcre2_code_free(pcre2_code *</code><i>code</i>);
<code>pcre2_code *pcre2_code_copy(const pcre2_code *</code><i>code</i>);
<code>pcre2_code *pcre2_code_copy_with_tables(const pcre2_code *</code><i>code</i>);</pre>
<p>The <code>pcre2_compile()</code> function compiles a pattern into an internal form. The pattern is defined by a pointer to a string of code units and a length (in code units). If the pattern is zero-terminated, the length can be specified as PCRE2_ZERO_TERMINATED. The function returns a pointer to a block of memory that contains the compiled pattern and related data, or NULL if an error occurred. </p>
<p> If the compile context argument <i>ccontext</i> is NULL, memory for the compiled pattern is obtained by calling <code>malloc()</code>. Otherwise, it is obtained from the same memory function that was used for the compile context. The caller must free the memory by calling <code>pcre2_code_free()</code> when it is no longer needed. If <code>pcre2_code_free()</code> is called with a NULL argument, it returns immediately, without doing anything. </p>
<p> The function <code>pcre2_code_copy()</code> makes a copy of the compiled code in new memory, using the same memory allocator as was used for the original. However, if the code has been processed by the JIT compiler (see below), the JIT information cannot be copied (because it is position-dependent). The new copy can initially be used only for non-JIT matching, though it can be passed to <code>pcre2_jit_compile()</code> if required. If <code>pcre2_code_copy()</code> is called with a NULL argument, it returns NULL. </p>
<p> The <code>pcre2_code_copy()</code> function provides a way for individual threads in a multithreaded application to acquire a private copy of shared compiled code. However, it does not make a copy of the character tables used by the compiled pattern; the new pattern code points to the same tables as the original code. (See &quot;Locale Support&quot; below for details of these character tables.) In many applications the same tables are used throughout, so this behaviour is appropriate. Nevertheless, there are occasions when a copy of a compiled pattern and the relevant tables are needed. The <code>pcre2_code_copy_with_tables()</code> provides this facility. Copies of both the code and the tables are made, with the new code pointing to the new tables. The memory for the new tables is automatically freed when <code>pcre2_code_free()</code> is called for the new copy of the compiled code. If <code>pcre2_code_copy_with_tables()</code> is called with a NULL argument, it returns NULL. </p>
<p> NOTE: When one of the matching functions is called, pointers to the compiled pattern and the subject string are set in the match data block so that they can be referenced by the substring extraction functions after a successful match. After running a match, you must not free a compiled pattern or a subject string until after all operations on the match data block have taken place, unless, in the case of the subject string, you have used the PCRE2_COPY_MATCHED_SUBJECT option, which is described in the section entitled &quot;Option bits for <code>pcre2_match()</code>&quot; below. </p>
<p> The <i>options</i> argument for <code>pcre2_compile()</code> contains various bit settings that affect the compilation. It should be zero if none of them are required. The available options are described below. Some of them (in particular, those that are compatible with Perl, but some others as well) can also be set and unset from within the pattern (see the detailed description in the <code>pcre2pattern</code> documentation). </p>
<p> For those options that can be different in different parts of the pattern, the contents of the <i>options</i> argument specifies their settings at the start of compilation. The PCRE2_ANCHORED, PCRE2_ENDANCHORED, and PCRE2_NO_UTF_CHECK options can be set at the time of matching as well as at compile time. </p>
<p> Some additional options and less frequently required compile-time parameters (for example, the newline setting) can be provided in a compile context (as described above). </p>
<p> If <i>errorcode</i> or <i>erroroffset</i> is NULL, <code>pcre2_compile()</code> returns NULL immediately. Otherwise, the variables to which these point are set to an error code and an offset (number of code units) within the pattern, respectively, when <code>pcre2_compile()</code> returns NULL because a compilation error has occurred. The values are not defined when compilation is successful and <code>pcre2_compile()</code> returns a non-NULL value. </p>
<p> There are nearly 100 positive error codes that <code>pcre2_compile()</code> may return if it finds an error in the pattern. There are also some negative error codes that are used for invalid UTF strings when validity checking is in force. These are the same as given by <code>pcre2_match()</code> and <code>pcre2_dfa_match()</code>, and are described in the <code>pcre2unicode</code> documentation. There is no separate documentation for the positive error codes, because the textual error messages that are obtained by calling the <code>pcre2_get_error_message()</code> function (see &quot;Obtaining a textual error message&quot; below) should be self-explanatory. Macro names starting with PCRE2_ERROR_ are defined for both positive and negative error codes in <code>pcre2.h</code>. </p>
<p> The value returned in <i>erroroffset</i> is an indication of where in the pattern the error occurred. It is not necessarily the furthest point in the pattern that was read. For example, after the error &quot;lookbehind assertion is not fixed length&quot;, the error offset points to the start of the failing assertion. For an invalid UTF-8 or UTF-16 string, the offset is that of the first code unit of the failing character. </p>
<p> Some errors are not detected until the whole pattern has been scanned; in these cases, the offset passed back is the length of the pattern. Note that the offset is in code units, not characters, even in a UTF mode. It may sometimes point into the middle of a UTF-8 or UTF-16 character. </p>
<p> This code fragment shows a typical straightforward call to <code>pcre2_compile()</code>: </p>
<p>&nbsp;<wbr>&nbsp;pcre2_code&nbsp;*re;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE erroffset;<br />
&nbsp;<wbr>&nbsp;int errorcode;<br />
&nbsp;<wbr>&nbsp;re&nbsp;=&nbsp;pcre2_compile(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;^A.*Z&quot;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;the pattern&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_ZERO_TERMINATED,&nbsp;<wbr>&nbsp;/*&nbsp;the pattern is zero-terminated&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;default options&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;errorcode,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;for error code&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;erroffset,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;for error offset&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NULL);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;no compile context&nbsp;*/</p>
<h3>Main compile options</h3>
<p>The following names for option bits are defined in the <code>pcre2.h</code> header file: </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_ANCHORED </p>
<p> If this bit is set, the pattern is forced to be &quot;anchored&quot;, that is, it is constrained to match only at the first matching point in the string that is being searched (the &quot;subject string&quot;). This effect can also be achieved by appropriate constructs in the pattern itself, which is the only way to do it in Perl. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_ALLOW_EMPTY_CLASS </p>
<p> By default, for compatibility with Perl, a closing square bracket that immediately follows an opening one is treated as a data character for the class. When PCRE2_ALLOW_EMPTY_CLASS is set, it terminates the class, which therefore contains no characters and so can never match. </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_ALT_BSUX </p>
<p> This option request alternative handling of three escape sequences, which makes PCRE2&#8217;s behaviour more like ECMAscript (aka JavaScript). When it is set: </p>
<p> (1) 
