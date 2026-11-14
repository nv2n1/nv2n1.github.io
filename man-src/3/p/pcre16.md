---
title: "pcre16(3)"
name: "pcre16"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre16/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions </p>
<pre><code>#include &lt;
pcre.h&gt;</code></pre>
<h2>Pcre 16-Bit Api Basic Functions</h2>
<pre><code>pcre16 *pcre16_compile(PCRE_SPTR16 </code><i>pattern</i>, int <i>options</i>,
<code> const char **</code><i>errptr</i>, int *<i>erroffset</i>,
<code> const unsigned char *</code><i>tableptr</i>);
<code>pcre16 *pcre16_compile2(PCRE_SPTR16 </code><i>pattern</i>, int <i>options</i>,
<code> int *</code><i>errorcodeptr</i>,
<code> const char **</code><i>errptr</i>, int *<i>erroffset</i>,
<code> const unsigned char *</code><i>tableptr</i>);
<code>pcre16_extra *pcre16_study(const pcre16 *</code><i>code</i>, int <i>options</i>,
<code> const char **</code><i>errptr</i>);
<code>void pcre16_free_study(pcre16_extra *</code><i>extra</i>);
<code>int pcre16_exec(const pcre16 *</code><i>code</i>, const pcre16_extra *<i>extra</i>,
<code> PCRE_SPTR16 </code><i>subject</i>, int <i>length</i>, int <i>startoffset</i>,
<code> int </code><i>options</i>, int *<i>ovector</i>, int <i>ovecsize</i>);
<code>int pcre16_dfa_exec(const pcre16 *</code><i>code</i>, const pcre16_extra *<i>extra</i>,
<code> PCRE_SPTR16 </code><i>subject</i>, int <i>length</i>, int <i>startoffset</i>,
<code> int </code><i>options</i>, int *<i>ovector</i>, int <i>ovecsize</i>,
<code> int *</code><i>workspace</i>, int <i>wscount</i>);</pre>
<h2>Pcre 16-Bit Api String Extraction Functions</h2>
<pre><code>int pcre16_copy_named_substring(const pcre16 *</code><i>code</i>,
<code> PCRE_SPTR16 </code><i>subject</i>, int *<i>ovector</i>,
<code> int </code><i>stringcount</i>, PCRE_SPTR16 <i>stringname</i>,
<code> PCRE_UCHAR16 *</code><i>buffer</i>, int <i>buffersize</i>);
<code>int pcre16_copy_substring(PCRE_SPTR16 </code><i>subject</i>, int *<i>ovector</i>,
<code> int </code><i>stringcount</i>, int <i>stringnumber</i>, PCRE_UCHAR16 *<i>buffer</i>,
<code> int </code><i>buffersize</i>);
<code>int pcre16_get_named_substring(const pcre16 *</code><i>code</i>,
<code> PCRE_SPTR16 </code><i>subject</i>, int *<i>ovector</i>,
<code> int </code><i>stringcount</i>, PCRE_SPTR16 <i>stringname</i>,
<code> PCRE_SPTR16 *</code><i>stringptr</i>);
<code>int pcre16_get_stringnumber(const pcre16 *</code><i>code</i>,
<code> PCRE_SPTR16 </code><i>name</i>);
<code>int pcre16_get_stringtable_entries(const pcre16 *</code><i>code</i>,
<code> PCRE_SPTR16 </code><i>name</i>, PCRE_UCHAR16 **<i>first</i>, PCRE_UCHAR16 **<i>last</i>);
<code>int pcre16_get_substring(PCRE_SPTR16 </code><i>subject</i>, int *<i>ovector</i>,
<code> int </code><i>stringcount</i>, int <i>stringnumber</i>,
<code> PCRE_SPTR16 *</code><i>stringptr</i>);
<code>int pcre16_get_substring_list(PCRE_SPTR16 </code><i>subject</i>,
<code> int *</code><i>ovector</i>, int <i>stringcount</i>, PCRE_SPTR16 **<i>listptr</i>);
<code>void pcre16_free_substring(PCRE_SPTR16 </code><i>stringptr</i>);
<code>void pcre16_free_substring_list(PCRE_SPTR16 *</code><i>stringptr</i>);</pre>
<h2>Pcre 16-Bit Api Auxiliary Functions</h2>
<pre><code>pcre16_jit_stack *pcre16_jit_stack_alloc(int </code><i>startsize</i>, int <i>maxsize</i>);
<code>void pcre16_jit_stack_free(pcre16_jit_stack *</code><i>stack</i>);
<code>void pcre16_assign_jit_stack(pcre16_extra *</code><i>extra</i>,
<code> pcre16_jit_callback </code><i>callback</i>, void *<i>data</i>);
<code>const unsigned char *pcre16_maketables(void);</code>
<code>int pcre16_fullinfo(const pcre16 *</code><i>code</i>, const pcre16_extra *<i>extra</i>,
<code> int </code><i>what</i>, void *<i>where</i>);
<code>int pcre16_refcount(pcre16 *</code><i>code</i>, int <i>adjust</i>);
<code>int pcre16_config(int </code><i>what</i>, void *<i>where</i>);
<code>const char *pcre16_version(void);</code>
<code>int pcre16_pattern_to_host_byte_order(pcre16 *</code><i>code</i>,
<code> pcre16_extra *</code><i>extra</i>, const unsigned char *<i>tables</i>);</pre>
<h2>Pcre 16-Bit Api Indirected Functions</h2>
<pre><code>void *(*pcre16_malloc)(size_t);</code>
<code>void (*pcre16_free)(void *);</code>
<code>void *(*pcre16_stack_malloc)(size_t);</code>
<code>void (*pcre16_stack_free)(void *);</code>
<code>int (*pcre16_callout)(pcre16_callout_block *);</code></pre>
<h2>Pcre 16-Bit Api 16-Bit-Only Function</h2>
<pre><code>int pcre16_utf16_to_host_byte_order(PCRE_UCHAR16 *</code><i>output</i>,
<code> PCRE_SPTR16 </code><i>input</i>, int <i>length</i>, int *<i>byte_order</i>,
<code> int </code><i>keep_boms</i>);</pre>
<h2>The Pcre 16-Bit Library</h2>
<p>Starting with release 8.30, it is possible to compile a PCRE library that supports 16-bit character strings, including UTF-16 strings, as well as or instead of the original 8-bit library. The majority of the work to make this possible was done by Zoltan Herczeg. The two libraries contain identical sets of functions, used in exactly the same way. Only the names of the functions and the data types of their arguments and results are different. To avoid over-complication and reduce the documentation maintenance load, most of the PCRE documentation describes the 8-bit library, with only occasional references to the 16-bit library. This page describes what is different when you use the 16-bit library. </p>
<p> WARNING: A single application can be linked with both libraries, but you must take care when processing any particular pattern to use functions from just one library. For example, if you want to study a pattern that was compiled with <code>pcre16_compile()</code>, you must do so with <code>pcre16_study()</code>, not <code>pcre_study()</code>, and you must free the study data with <code>pcre16_free_study()</code>.</p>
<h2>The Header File</h2>
<p>There is only one header file, <code>pcre.h</code>. It contains prototypes for all the functions in all libraries, as well as definitions of flags, structures, error codes, etc.</p>
<h2>The Library Name</h2>
<p>In Unix-like systems, the 16-bit library is called <code>libpcre16</code>, and can normally be accesss by adding <code>-lpcre16</code> to the command for linking an application that uses PCRE.</p>
<h2>String Types</h2>
<p>In the 8-bit library, strings are passed to PCRE library functions as vectors of bytes with the C type &quot;char *&quot;. In the 16-bit library, strings are passed as vectors of unsigned 16-bit quantities. The macro PCRE_UCHAR16 specifies an appropriate data type, and PCRE_SPTR16 is defined as &quot;const PCRE_UCHAR16 *&quot;. In very many environments, &quot;short int&quot; is a 16-bit data type. When PCRE is built, it defines PCRE_UCHAR16 as &quot;unsigned short int&quot;, but checks that it really is a 16-bit data type. If it is not, the build fails with an error message telling the maintainer to modify the definition appropriately.</p>
<h2>Structure Types</h2>
<p>The types of the opaque structures that are used for compiled 16-bit patterns and JIT stacks are <code>pcre16</code> and <code>pcre16_jit_stack</code> respectively. The type of the user-accessible structure that is returned by <code>pcre16_study()</code> is <code>pcre16_extra</code>, and the type of the structure that is used for passing data to a callout function is <code>pcre16_callout_block</code>. These structures contain the same fields, with the same names, as their 8-bit counterparts. The only difference is that pointers to character strings are 16-bit instead of 8-bit types.</p>
<h2>16-Bit Functions</h2>
<p>For every function in the 8-bit library there is a corresponding function in the 16-bit library with a name that starts with <code>pcre16_</code> instead of <code>pcre_</code>. The prototypes are listed above. In addition, there is one extra function, <code>pcre16_utf16_to_host_byte_order()</code>. This is a utility function that converts a UTF-16 character string to host byte order if necessary. The other 16-bit functions expect the strings they are passed to be in host byte order. </p>
<p> The <i>input</i> and <i>output</i> arguments of <code>pcre16_utf16_to_host_byte_order()</code> may point to the same address, that is, conversion in place is supported. The output buffer must be at least as long as the input. </p>
<p> The <i>length</i> argument specifies the number of 16-bit data units in the input string; a negative value specifies a zero-terminated string. </p>
<p> If <i>byte_order</i> is NULL, it is assumed that the string starts off in host byte order. This may be changed by byte-order marks (BOMs) anywhere in the string (commonly as the first character). </p>
<p> If <i>byte_order</i> is not NULL, a non-zero value of the integer to which it points means that the input starts off in host byte order, otherwise the opposite order is assumed. Again, BOMs in the string can change this. The final byte order is passed back at the end of processing. </p>
<p> If <i>keep_boms</i> is not zero, byte-order mark characters (0xfeff) are copied into the output string. Otherwise they are discarded. </p>
<p> The result of the function is the number of 16-bit units placed into the output buffer, including the zero terminator if the string was zero-terminated.</p>
<h2>Subject String Offsets</h2>
<p>The lengths and starting offsets of subject strings must be specified in 16-bit data units, and the offsets within subject strings that are returned by the matching functions are in also 16-bit units rather than bytes.</p>
<h2>Named Subpatterns</h2>
<p>The name-to-number translation table that is maintained for named subpatterns uses 16-bit characters. The <code>pcre16_get_stringtable_entries()</code> function returns the length of each entry in the table as the number of 16-bit data units.</p>
<h2>Option Names</h2>
<p>There are two new general option names, PCRE_UTF16 and PCRE_NO_UTF16_CHECK, which correspond to PCRE_UTF8 and PCRE_NO_UTF8_CHECK in the 8-bit library. In fact, these new options define the same bits in the options word. There is a discussion about the validity of UTF-16 strings in the <code>pcreunicode</code> page. </p>
<p> For the <code>pcre16_config()</code> function there is an option PCRE_CONFIG_UTF16 that returns 1 if UTF-16 support is configured, otherwise 0. If this option is given to <code>pcre_config()</code> or <code>pcre32_config()</code>, or if the PCRE_CONFIG_UTF8 or PCRE_CONFIG_UTF32 option is given to <code>pcre16_config()</code>, the result is the PCRE_ERROR_BADOPTION error.</p>
<h2>Character Codes</h2>
<p>In 16-bit mode, when PCRE_UTF16 is not set, character values are treated in the same way as in 8-bit, non UTF-8 mode, except, of course, that they can range from 0 to 0xffff instead of 0 to 0xff. Character types for characters less than 0xff can therefore be influenced by the locale in the same way as before. Characters greater than 0xff have only one case, and no &quot;type&quot; (such as letter or digit). </p>
<p> In UTF-16 mode, the character code is Unicode, in the range 0 to 0x10ffff, with the exception of values in the range 0xd800 to 0xdfff because those are &quot;surrogate&quot; values that are used in pairs to encode values greater than 0xffff. </p>
<p> A UTF-16 string can indicate its endianness by special code knows as a byte-order mark (BOM). The PCRE functions do not handle this, expecting strings to be in host byte order. A utility function called <code>pcre16_utf16_to_host_byte_order()</code> is provided to help with this (see above).</p>
<h2>Error Names</h2>
<p>The errors PCRE_ERROR_BADUTF16_OFFSET and PCRE_ERROR_SHORTUTF16 correspond to their 8-bit counterparts. The error PCRE_ERROR_BADMODE is given when a compiled pattern is passed to a function that processes patterns in the other mode, for example, if a pattern compiled with <code>pcre_compile()</code> is passed to <code>pcre16_exec()</code>. </p>
<p> There are new error codes whose names begin with PCRE_UTF16_ERR for invalid UTF-16 strings, corresponding to the PCRE_UTF8_ERR codes for UTF-8 strings that are described in the section entitled &quot;Reason codes for invalid UTF-8 strings&quot; in the main <code>pcreapi</code> page. The UTF-16 errors are: </p>
<p>&nbsp;<wbr>&nbsp;PCRE_UTF16_ERR1&nbsp;<wbr>&nbsp;Missing low surrogate at end of string<br />
&nbsp;<wbr>&nbsp;PCRE_UTF16_ERR2&nbsp;<wbr>&nbsp;Invalid low surrogate follows high surrogate<br />
&nbsp;<wbr>&nbsp;PCRE_UTF16_ERR3&nbsp;<wbr>&nbsp;Isolated low surrogate<br />
&nbsp;<wbr>&nbsp;PCRE_UTF16_ERR4&nbsp;<wbr>&nbsp;Non-character</p>
<h2>Error Texts</h2>
<p>If there is an error while compiling a pattern, the error text that is passed back by <code>pcre16_compile()</code> or <code>pcre16_compile2()</code> is still an 8-bit character string, zero-terminated.</p>
<h2>Callouts</h2>
<p>The <i>subject</i> and <i>mark</i> fields in the callout block that is passed to a callout function point to 16-bit vectors.</p>
<h2>Testing</h2>
<p>The <code>pcretest</code> program continues to operate with 8-bit input and output files, but it can be used for testing the 16-bit library. If it is run with the command line option <code>-16</code>, patterns and subject strings are converted from 8-bit to 16-bit before being passed to PCRE, and the 16-bit library functions are used instead of the 8-bit ones. Returned 16-bit strings are converted to 8-bit for output. If both the 8-bit and the 32-bit libraries were not compiled, <code>pcretest</code> defaults to 16-bit and the <code>-16</code> option is ignored. </p>
<p> When PCRE is being built, the <code>RunTest</code> script that is called by &quot;make check&quot; uses the <code>pcretest</code> <code>-C</code> option to discover which of the 8-bit, 16-bit and 32-bit libraries has been built, and runs the tests appropriately.</p>
<h2>Not Supported In 16-Bit Mode</h2>
<p>Not all the features of the 8-bit library are available with the 16-bit library. The C++ and POSIX wrapper functions support only the 8-bit library, and the <code>pcregrep</code> program is at present 8-bit only.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 12 May 2013
Copyright (c) 1997-2013 University of Cambridge.</pre>
