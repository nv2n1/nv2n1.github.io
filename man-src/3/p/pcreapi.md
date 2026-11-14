---
title: "pcreapi(3)"
name: "pcreapi"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcreapi/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions </p>
<pre><code>#include &lt;
pcre.h&gt;</code></pre>
<h2>Pcre Native Api Basic Functions</h2>
<pre><code>pcre *pcre_compile(const char *</code><i>pattern</i>, int <i>options</i>,
<code> const char **</code><i>errptr</i>, int *<i>erroffset</i>,
<code> const unsigned char *</code><i>tableptr</i>);
<code>pcre *pcre_compile2(const char *</code><i>pattern</i>, int <i>options</i>,
<code> int *</code><i>errorcodeptr</i>,
<code> const char **</code><i>errptr</i>, int *<i>erroffset</i>,
<code> const unsigned char *</code><i>tableptr</i>);
<code>pcre_extra *pcre_study(const pcre *</code><i>code</i>, int <i>options</i>,
<code> const char **</code><i>errptr</i>);
<code>void pcre_free_study(pcre_extra *</code><i>extra</i>);
<code>int pcre_exec(const pcre *</code><i>code</i>, const pcre_extra *<i>extra</i>,
<code> const char *</code><i>subject</i>, int <i>length</i>, int <i>startoffset</i>,
<code> int </code><i>options</i>, int *<i>ovector</i>, int <i>ovecsize</i>);
<code>int pcre_dfa_exec(const pcre *</code><i>code</i>, const pcre_extra *<i>extra</i>,
<code> const char *</code><i>subject</i>, int <i>length</i>, int <i>startoffset</i>,
<code> int </code><i>options</i>, int *<i>ovector</i>, int <i>ovecsize</i>,
<code> int *</code><i>workspace</i>, int <i>wscount</i>);</pre>
<h2>Pcre Native Api String Extraction Functions</h2>
<pre><code>int pcre_copy_named_substring(const pcre *</code><i>code</i>,
<code> const char *</code><i>subject</i>, int *<i>ovector</i>,
<code> int </code><i>stringcount</i>, const char *<i>stringname</i>,
<code> char *</code><i>buffer</i>, int <i>buffersize</i>);
<code>int pcre_copy_substring(const char *</code><i>subject</i>, int *<i>ovector</i>,
<code> int </code><i>stringcount</i>, int <i>stringnumber</i>, char *<i>buffer</i>,
<code> int </code><i>buffersize</i>);
<code>int pcre_get_named_substring(const pcre *</code><i>code</i>,
<code> const char *</code><i>subject</i>, int *<i>ovector</i>,
<code> int </code><i>stringcount</i>, const char *<i>stringname</i>,
<code> const char **</code><i>stringptr</i>);
<code>int pcre_get_stringnumber(const pcre *</code><i>code</i>,
<code> const char *</code><i>name</i>);
<code>int pcre_get_stringtable_entries(const pcre *</code><i>code</i>,
<code> const char *</code><i>name</i>, char **<i>first</i>, char **<i>last</i>);
<code>int pcre_get_substring(const char *</code><i>subject</i>, int *<i>ovector</i>,
<code> int </code><i>stringcount</i>, int <i>stringnumber</i>,
<code> const char **</code><i>stringptr</i>);
<code>int pcre_get_substring_list(const char *</code><i>subject</i>,
<code> int *</code><i>ovector</i>, int <i>stringcount</i>, const char ***<i>listptr</i>);
<code>void pcre_free_substring(const char *</code><i>stringptr</i>);
<code>void pcre_free_substring_list(const char **</code><i>stringptr</i>);</pre>
<h2>Pcre Native Api Auxiliary Functions</h2>
<pre><code>int pcre_jit_exec(const pcre *</code><i>code</i>, const pcre_extra *<i>extra</i>,
<code> const char *</code><i>subject</i>, int <i>length</i>, int <i>startoffset</i>,
<code> int </code><i>options</i>, int *<i>ovector</i>, int <i>ovecsize</i>,
<code> pcre_jit_stack *</code><i>jstack</i>);
<code>pcre_jit_stack *pcre_jit_stack_alloc(int </code><i>startsize</i>, int <i>maxsize</i>);
<code>void pcre_jit_stack_free(pcre_jit_stack *</code><i>stack</i>);
<code>void pcre_assign_jit_stack(pcre_extra *</code><i>extra</i>,
<code> pcre_jit_callback </code><i>callback</i>, void *<i>data</i>);
<code>const unsigned char *pcre_maketables(void);</code>
<code>int pcre_fullinfo(const pcre *</code><i>code</i>, const pcre_extra *<i>extra</i>,
<code> int </code><i>what</i>, void *<i>where</i>);
<code>int pcre_refcount(pcre *</code><i>code</i>, int <i>adjust</i>);
<code>int pcre_config(int </code><i>what</i>, void *<i>where</i>);
<code>const char *pcre_version(void);</code>
<code>int pcre_pattern_to_host_byte_order(pcre *</code><i>code</i>,
<code> pcre_extra *</code><i>extra</i>, const unsigned char *<i>tables</i>);</pre>
<h2>Pcre Native Api Indirected Functions</h2>
<pre><code>void *(*pcre_malloc)(size_t);</code>
<code>void (*pcre_free)(void *);</code>
<code>void *(*pcre_stack_malloc)(size_t);</code>
<code>void (*pcre_stack_free)(void *);</code>
<code>int (*pcre_callout)(pcre_callout_block *);</code>
<code>int (*pcre_stack_guard)(void);</code></pre>
<h2>Pcre 8-Bit, 16-Bit, And 32-Bit Libraries</h2>
<p>As well as support for 8-bit character strings, PCRE also supports 16-bit strings (from release 8.30) and 32-bit strings (from release 8.32), by means of two additional libraries. They can be built as well as, or instead of, the 8-bit library. To avoid too much complication, this document describes the 8-bit versions of the functions, with only occasional references to the 16-bit and 32-bit libraries. </p>
<p> The 16-bit and 32-bit functions operate in the same way as their 8-bit counterparts; they just use different data types for their arguments and results, and their names start with <code>pcre16_</code> or <code>pcre32_</code> instead of <code>pcre_</code>. For every option that has UTF8 in its name (for example, PCRE_UTF8), there are corresponding 16-bit and 32-bit names with UTF8 replaced by UTF16 or UTF32, respectively. This facility is in fact just cosmetic; the 16-bit and 32-bit option names define the same bit values. </p>
<p> References to bytes and UTF-8 in this document should be read as references to 16-bit data units and UTF-16 when using the 16-bit library, or 32-bit data units and UTF-32 when using the 32-bit library, unless specified otherwise. More details of the specific differences for the 16-bit and 32-bit libraries are given in the <code>pcre16</code> and <code>pcre32</code> pages.</p>
<h2>Pcre Api Overview</h2>
<p>PCRE has its own native API, which is described in this document. There are also some wrapper functions (for the 8-bit library only) that correspond to the POSIX regular expression API, but they do not give access to all the functionality. They are described in the <code>pcreposix</code> documentation. Both of these APIs define a set of C function calls. A C++ wrapper (again for the 8-bit library only) is also distributed with PCRE. It is documented in the <code>pcrecpp</code> page. </p>
<p> The native API C function prototypes are defined in the header file <code>pcre.h</code>, and on Unix-like systems the (8-bit) library itself is called <code>libpcre</code>. It can normally be accessed by adding <code>-lpcre</code> to the command for linking an application that uses PCRE. The header file defines the macros PCRE_MAJOR and PCRE_MINOR to contain the major and minor release numbers for the library. Applications can use these to include support for different releases of PCRE. </p>
<p> In a Windows environment, if you want to statically link an application program against a non-dll <code>pcre.a</code> file, you must define PCRE_STATIC before including <code>pcre.h</code> or <code>pcrecpp.h</code>, because otherwise the <code>pcre_malloc()</code> and <code>pcre_free()</code> exported functions will be declared <code>__declspec(dllimport)</code>, with unwanted results. </p>
<p> The functions <code>pcre_compile()</code>, <code>pcre_compile2()</code>, <code>pcre_study()</code>, and <code>pcre_exec()</code> are used for compiling and matching regular expressions in a Perl-compatible manner. A sample program that demonstrates the simplest way of using them is provided in the file called <i>pcredemo.c</i> in the PCRE source distribution. A listing of this program is given in the <code>pcredemo</code> documentation, and the <code>pcresample</code> documentation describes how to compile and run it. </p>
<p> Just-in-time compiler support is an optional feature of PCRE that can be built in appropriate hardware environments. It greatly speeds up the matching performance of many patterns. Simple programs can easily request that it be used if available, by setting an option that is ignored when it is not relevant. More complicated programs might need to make use of the functions <code>pcre_jit_stack_alloc()</code>, <code>pcre_jit_stack_free()</code>, and <code>pcre_assign_jit_stack()</code> in order to control the JIT code&#8217;s memory usage. </p>
<p> From release 8.32 there is also a direct interface for JIT execution, which gives improved performance. The JIT-specific functions are discussed in the <code>pcrejit</code> documentation. </p>
<p> A second matching function, <code>pcre_dfa_exec()</code>, which is not Perl-compatible, is also provided. This uses a different algorithm for the matching. The alternative algorithm finds all possible matches (at a given point in the subject), and scans the subject just once (unless there are lookbehind assertions). However, this algorithm does not return captured substrings. A description of the two matching algorithms and their advantages and disadvantages is given in the <code>pcrematching</code> documentation. </p>
<p> In addition to the main compiling and matching functions, there are convenience functions for extracting captured substrings from a subject string that is matched by <code>pcre_exec()</code>. They are: </p>
<p>&nbsp;<wbr>&nbsp;<code>pcre_copy_substring()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre_copy_named_substring()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre_get_substring()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre_get_named_substring()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre_get_substring_list()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre_get_stringnumber()</code><br />
&nbsp;<wbr>&nbsp;<code>pcre_get_stringtable_entries()</code> </p>
<p> <code>pcre_free_substring()</code> and <code>pcre_free_substring_list()</code> are also provided, to free the memory used for extracted strings. </p>
<p> The function <code>pcre_maketables()</code> is used to build a set of character tables in the current locale for passing to <code>pcre_compile()</code>, <code>pcre_exec()</code>, or <code>pcre_dfa_exec()</code>. This is an optional facility that is provided for specialist use. Most commonly, no special tables are passed, in which case internal tables that are generated when PCRE is built are used. </p>
<p> The function <code>pcre_fullinfo()</code> is used to find out information about a compiled pattern. The function <code>pcre_version()</code> returns a pointer to a string containing the version of PCRE and its date of release. </p>
<p> The function <code>pcre_refcount()</code> maintains a reference count in a data block containing a compiled pattern. This is provided for the benefit of object-oriented applications. </p>
<p> The global variables <code>pcre_malloc</code> and <code>pcre_free</code> initially contain the entry points of the standard <code>malloc()</code> and <code>free()</code> functions, respectively. PCRE calls the memory management functions via these variables, so a calling program can replace them if it wishes to intercept the calls. This should be done before calling any PCRE functions. </p>
<p> The global variables <code>pcre_stack_malloc</code> and <code>pcre_stack_free</code> are also indirections to memory management functions. These special functions are used only when PCRE is compiled to use the heap for remembering data, instead of recursive function calls, when running the <code>pcre_exec()</code> function. See the <code>pcrebuild</code> documentation for details of how to do this. It is a non-standard way of building PCRE, for use in environments that have limited stacks. Because of the greater use of memory management, it runs more slowly. Separate functions are provided so that special-purpose external code can be used for this case. When used, these functions always allocate memory blocks of the same size. There is a discussion about PCRE&#8217;s stack usage in the <code>pcrestack</code> documentation. </p>
<p> The global variable <code>pcre_callout</code> initially contains NULL. It can be set by the caller to a &quot;callout&quot; function, which PCRE will then call at specified points during a matching operation. Details are given in the <code>pcrecallout</code> documentation. </p>
<p> The global variable <code>pcre_stack_guard</code> initially contains NULL. It can be set by the caller to a function that is called by PCRE whenever it starts to compile a parenthesized part of a pattern. When parentheses are nested, PCRE uses recursive function calls, which use up the system stack. This function is provided so that applications with restricted stacks can force a compilation error if the stack runs out. The function should return zero if all is well, or non-zero to force an error.</p>
<h2>Newlines</h2>
<p>PCRE supports five different conventions for indicating line breaks in strings: a single CR (carriage return) character, a single LF (linefeed) character, the two-character sequence CRLF, any of the three preceding, or any Unicode newline sequence. The Unicode newline sequences are the three just mentioned, plus the single characters VT (vertical tab, U+000B), FF (form feed, U+000C), NEL (next line, U+0085), LS (line separator, U+2028), and PS (paragraph separator, U+2029). </p>
<p> Each of the first three conventions is used by at least one operating system as its standard newline sequence. When PCRE is built, a default can be specified. The default default is LF, which is the Unix standard. When PCRE is run, the default can be overridden, either when a pattern is compiled, or when it is matched. </p>
<p> At compile time, the newline convention can be specified by the <i>options</i> argument of <code>pcre_compile()</code>, or it can be specified by special text at the start of the pattern itself; this overrides any other settings. See the <code>pcrepattern</code> page for details of the special character sequences. </p>
<p> In the PCRE documentation the word &quot;newline&quot; is used to mean &quot;the character or pair of characters that indicate a line break&quot;. The choice of newline convention affects the handling of the dot, circumflex, and dollar metacharacters, the handling of #-comments in /x mode, and, when CRLF is a recognized line ending sequence, the match position advancement for a non-anchored pattern. There is more detail about this in the section on <code>pcre_exec()</code> options below. </p>
<p> The choice of newline convention does not affect the interpretation of the 
 or  escape sequences, nor does it affect what \R matches, which is controlled in a similar way, but by separate options.</p>
<h2>Multithreading</h2>
<p>The PCRE functions can be used in multi-threading applications, with the proviso that the memory management functions pointed to by <code>pcre_malloc</code>, <code>pcre_free</code>, <code>pcre_stack_malloc</code>, and <code>pcre_stack_free</code>, and the callout and stack-checking functions pointed to by <code>pcre_callout</code> and <code>pcre_stack_guard</code>, are shared by all threads. </p>
<p> The compiled form of a regular expression is not altered during matching, so the same compiled pattern can safely be used by several threads at once. </p>
<p> If the just-in-time optimization feature is being used, it needs separate memory stack areas for each thread. See the <code>pcrejit</code> documentation for more details.</p>
<h2>Saving Precompiled Patterns For Later Use</h2>
<p>The compiled form of a regular expression can be saved and re-used at a later time, possibly by a different program, and even on a host other than the one on which it was compiled. Details are given in the <code>pcreprecompile</code> documentation, which includes a description of the <code>pcre_pattern_to_host_byte_order()</code> function. However, compiling a regular expression with one version of PCRE for use with a different version is not guaranteed to work and may cause crashes.</p>
<h2>Checking Build-Time Options</h2>
<p><code>int pcre_config(int </code><i>what</i>, void *<i>where</i>); </p>
<p> The function <code>pcre_config()</code> makes it possible for a PCRE client to discover which optional features have been compiled into the PCRE library. The <code>pcrebuild</code> documentation has more details about these optional features. </p>
<p> The first argument for <code>pcre_config()</code> is an integer, specifying which information is required; the second argument is a pointer to a variable into which the information is placed. The returned value is zero on success, or the negative error code PCRE_ERROR_BADOPTION if the value in the first argument is not recognized. The following information is available: </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_UTF8 </p>
<p> The output is an integer that is set to one if UTF-8 support is available; otherwise it is set to zero. This value should normally be given to the 8-bit version of this function, <code>pcre_config()</code>. If it is given to the 16-bit or 32-bit version of this function, the result is PCRE_ERROR_BADOPTION. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_UTF16 </p>
<p> The output is an integer that is set to one if UTF-16 support is available; otherwise it is set to zero. This value should normally be given to the 16-bit version of this function, <code>pcre16_config()</code>. If it is given to the 8-bit or 32-bit version of this function, the result is PCRE_ERROR_BADOPTION. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_UTF32 </p>
<p> The output is an integer that is set to one if UTF-32 support is available; otherwise it is set to zero. This value should normally be given to the 32-bit version of this function, <code>pcre32_config()</code>. If it is given to the 8-bit or 16-bit version of this function, the result is PCRE_ERROR_BADOPTION. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_UNICODE_PROPERTIES </p>
<p> The output is an integer that is set to one if support for Unicode character properties is available; otherwise it is set to zero. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_JIT </p>
<p> The output is an integer that is set to one if support for just-in-time compiling is available; otherwise it is set to zero. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_JITTARGET </p>
<p> The output is a pointer to a zero-terminated &quot;const char *&quot; string. If JIT support is available, the string contains the name of the architecture for which the JIT compiler is configured, for example &quot;x86 32bit (little endian + unaligned)&quot;. If JIT support is not available, the result is NULL. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_NEWLINE </p>
<p> The output is an integer whose value specifies the default character sequence that is recognized as meaning &quot;newline&quot;. The values that are supported in ASCII/Unicode environments are: 10 for LF, 13 for CR, 3338 for CRLF, -2 for ANYCRLF, and -1 for ANY. In EBCDIC environments, CR, ANYCRLF, and ANY yield the same values. However, the value for LF is normally 21, though some EBCDIC environments use 37. The corresponding values for CRLF are 3349 and 3365. The default should normally correspond to the standard sequence for your operating system. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_BSR </p>
<p> The output is an integer whose value indicates what character sequences the \R escape sequence matches by default. A value of 0 means that \R matches any Unicode line ending sequence; a value of 1 means that \R matches only CR, LF, or CRLF. The default can be overridden when a pattern is compiled or matched. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_LINK_SIZE </p>
<p> The output is an integer that contains the number of bytes used for internal linkage in compiled regular expressions. For the 8-bit library, the value can be 2, 3, or 4. For the 16-bit library, the value is either 2 or 4 and is still a number of bytes. For the 32-bit library, the value is either 2 or 4 and is still a number of bytes. The default value of 2 is sufficient for all but the most massive patterns, since it allows the compiled pattern to be up to 64K in size. Larger values allow larger regular expressions to be compiled, at the expense of slower matching. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_POSIX_MALLOC_THRESHOLD </p>
<p> The output is an integer that contains the threshold above which the POSIX interface uses <code>malloc()</code> for output vectors. Further details are given in the <code>pcreposix</code> documentation. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_PARENS_LIMIT </p>
<p> The output is a long integer that gives the maximum depth of nesting of parentheses (of any kind) in a pattern. This limit is imposed to cap the amount of system stack used when a pattern is compiled. It is specified when PCRE is built; the default is 250. This limit does not take into account the stack that may already be used by the calling application. For finer control over compilation stack usage, you can set a pointer to an external checking function in <code>pcre_stack_guard</code>. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_MATCH_LIMIT </p>
<p> The output is a long integer that gives the default limit for the number of internal matching function calls in a <code>pcre_exec()</code> execution. Further details are given with <code>pcre_exec()</code> below. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_MATCH_LIMIT_RECURSION </p>
<p> The output is a long integer that gives the default limit for the depth of recursion when calling the internal matching function in a <code>pcre_exec()</code> execution. Further details are given with <code>pcre_exec()</code> below. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CONFIG_STACKRECURSE </p>
<p> The output is an integer that is set to one if internal recursion when running <code>pcre_exec()</code> is implemented by recursive function calls that use the stack to remember their state. This is the usual way that PCRE is compiled. The output is zero if PCRE was compiled to use blocks of data on the heap instead of recursive function calls. In this case, <code>pcre_stack_malloc</code> and <code>pcre_stack_free</code> are called to manage memory blocks on the heap, thus avoiding the use of the stack.</p>
<h2>Compiling A Pattern</h2>
<pre><code>pcre *pcre_compile(const char *</code><i>pattern</i>, int <i>options</i>,
<code> const char **</code><i>errptr</i>, int *<i>erroffset</i>,
<code> const unsigned char *</code><i>tableptr</i>);
<code>pcre *pcre_compile2(const char *</code><i>pattern</i>, int <i>options</i>,
<code> int *</code><i>errorcodeptr</i>,
<code> const char **</code><i>errptr</i>, int *<i>erroffset</i>,
<code> const unsigned char *</code><i>tableptr</i>);</pre>
<p>Either of the functions <code>pcre_compile()</code> or <code>pcre_compile2()</code> can be called to compile a pattern into an internal form. The only difference between the two interfaces is that <code>pcre_compile2()</code> has an additional argument, <i>errorcodeptr</i>, via which a numerical error code can be returned. To avoid too much repetition, we refer just to <code>pcre_compile()</code> below, but the information applies equally to <code>pcre_compile2()</code>. </p>
<p> The pattern is a C string terminated by a binary zero, and is passed in the <i>pattern</i> argument. A pointer to a single block of memory that is obtained via <code>pcre_malloc</code> is returned. This contains the compiled code and related data. The <code>pcre</code> type is defined for the returned block; this is a typedef for a structure whose contents are not externally defined. It is up to the caller to free the memory (via <code>pcre_free</code>) when it is no longer required. </p>
<p> Although the compiled code of a PCRE regex is relocatable, that is, it does not depend on memory location, the complete <code>pcre</code> data block is not fully relocatable, because it may contain a copy of the <i>tableptr</i> argument, which is an address (see below). </p>
<p> The <i>options</i> argument contains various bit settings that affect the compilation. It should be zero if no options are required. The available options are described below. Some of them (in particular, those that are compatible with Perl, but some others as well) can also be set and unset from within the pattern (see the detailed description in the <code>pcrepattern</code> documentation). For those options that can be different in different parts of the pattern, the contents of the <i>options</i> argument specifies their settings at the start of compilation and execution. The PCRE_ANCHORED, PCRE_BSR_<i>xxx</i>, PCRE_NEWLINE_<i>xxx</i>, PCRE_NO_UTF8_CHECK, and PCRE_NO_START_OPTIMIZE options can be set at the time of matching as well as at compile time. </p>
<p> If <i>errptr</i> is NULL, <code>pcre_compile()</code> returns NULL immediately. Otherwise, if compilation of a pattern fails, <code>pcre_compile()</code> returns NULL, and sets the variable pointed to by <i>errptr</i> to point to a textual error message. This is a static string that is part of the library. You must not try to free it. Normally, the offset from the start of the pattern to the data unit that was being processed when the error was discovered is placed in the variable pointed to by <i>erroffset</i>, which must not be NULL (if it is, an immediate error is given). However, for an invalid UTF-8 or UTF-16 string, the offset is that of the first data unit of the failing character. </p>
<p> Some errors are not detected until the whole pattern has been scanned; in these cases, the offset passed back is the length of the pattern. Note that the offset is in data units, not characters, even in a UTF mode. It may sometimes point into the middle of a UTF-8 or UTF-16 character. </p>
<p> If <code>pcre_compile2()</code> is used instead of <code>pcre_compile()</code>, and the <i>errorcodeptr</i> argument is not NULL, a non-zero error code number is returned via this argument in the event of an error. This is in addition to the textual error message. Error codes and messages are listed below. </p>
<p> If the final argument, <i>tableptr</i>, is NULL, PCRE uses a default set of character tables that are built when PCRE is compiled, using the default C locale. Otherwise, <i>tableptr</i> must be an address that is the result of a call to <code>pcre_maketables()</code>. This value is stored with the compiled pattern, and used again by <code>pcre_exec()</code> and <code>pcre_dfa_exec()</code> when the pattern is matched. For more discussion, see the section on locale support below. </p>
<p> This code fragment shows a typical straightforward call to <code>pcre_compile()</code>: </p>
<p>&nbsp;<wbr>&nbsp;pcre&nbsp;*re;<br />
&nbsp;<wbr>&nbsp;const char&nbsp;*error;<br />
&nbsp;<wbr>&nbsp;int erroffset;<br />
&nbsp;<wbr>&nbsp;re&nbsp;=&nbsp;pcre_compile(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;^A.*Z&quot;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;the pattern&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;default options&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;error,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;for error message&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;erroffset,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;for error offset&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NULL);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;use default character tables&nbsp;*/ </p>
<p> The following names for option bits are defined in the <code>pcre.h</code> header file: </p>
<p>&nbsp;<wbr>&nbsp;PCRE_ANCHORED </p>
<p> If this bit is set, the pattern is forced to be &quot;anchored&quot;, that is, it is constrained to match only at the first matching point in the string that is being searched (the &quot;subject string&quot;). This effect can also be achieved by appropriate constructs in the pattern itself, which is the only way to do it in Perl. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_AUTO_CALLOUT </p>
<p> If this bit is set, <code>pcre_compile()</code> automatically inserts callout items, all with number 255, before each pattern item. For discussion of the callout facility, see the <code>pcrecallout</code> documentation. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_BSR_ANYCRLF<br />
&nbsp;<wbr>&nbsp;PCRE_BSR_UNICODE </p>
<p> These options (which are mutually exclusive) control what the \R escape sequence matches. The choice is either to match only CR, LF, or CRLF, or to match any Unicode newline sequence. The default is specified when PCRE is built. It can be overridden from within the pattern, or by setting an option when a compiled pattern is matched. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_CASELESS </p>
<p> If this bit is set, letters in the pattern match both upper and lower case letters. It is equivalent to Perl&#8217;s /i option, and it can be changed within a pattern by a (?i) option setting. In UTF-8 mode, PCRE always understands the concept of case for characters whose values are less than 128, so caseless matching is always possible. For characters with higher values, the concept of case is supported if PCRE is compiled with Unicode property support, but not otherwise. If you want to use caseless matching for characters 128 and above, you must ensure that PCRE is compiled with Unicode property support as well as with UTF-8 support. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_DOLLAR_ENDONLY </p>
<p> If this bit is set, a dollar metacharacter in the pattern matches only at the end of the subject string. Without this option, a dollar also matches immediately before a newline at the end of the string (but not before any other newlines). The PCRE_DOLLAR_ENDONLY option is ignored if PCRE_MULTILINE is set. There is no equivalent to this option in Perl, and no way to set it within a pattern. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_DOTALL </p>
<p> If this bit is set, a dot metacharacter in the pattern matches a character of any value, including one that indicates a newline. However, it only ever matches one character, even if newlines are coded as CRLF. Without this option, a dot does not match when the current position is at a newline. This option is equivalent to Perl&#8217;s /s option, and it can be changed within a pattern by a (?s) option setting. A negative class such as [^a] always matches newline characters, independent of the setting of this option. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_DUPNAMES </p>
<p> If this bit is set, names used to identify capturing subpatterns need not be unique. This can be helpful for certain types of pattern when it is known that only one instance of the named subpattern can ever be matched. There are more details of named subpatterns below; see also the <code>pcrepattern</code> documentation. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_EXTENDED </p>
<p> If this bit is set, most white space characters in the pattern are totally ignored except when escaped or inside a character class. However, white space is not allowed within sequences such as (?&gt; that introduce various parenthesized subpatterns, nor within a numerical quantifier such as {1,3}. However, ignorable white space is permitted between an item and a following quantifier and between a quantifier and a following + that indicates possessiveness. </p>
<p> White space did not used to include the VT character (code 11), because Perl did not treat this character as white space. However, Perl changed at release 5.18, so PCRE followed at release 8.34, and VT is now treated as white space. </p>
<p> PCRE_EXTENDED also causes characters between an unescaped # outside a character class and the next newline, inclusive, to be ignored. PCRE_EXTENDED is equivalent to Perl&#8217;s /x option, and it can be changed within a pattern by a (?x) option setting. </p>
<p> Which characters are interpreted as newlines is controlled by the options passed to <code>pcre_compile()</code> or by a special sequence at the start of the pattern, as described in the section entitled &quot;Newline conventions&quot; in the <code>pcrepattern</code> documentation. Note that the end of this type of comment is a literal newline sequence in the pattern; escape sequences that happen to represent a newline do not count. </p>
<p> This option makes it possible to include comments inside complicated patterns. Note, however, that this applies only to data characters. White space characters may never appear within special character sequences in a pattern, for example within the sequence (?( that introduces a conditional subpattern. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_EXTRA </p>
<p> This option was invented in order to turn on additional functionality of PCRE that is incompatible with Perl, but it is currently of very little use. When set, any backslash in a pattern that is followed by a letter that has no special meaning causes an error, thus reserving these combinations for future expansion. By default, as in Perl, a backslash followed by a letter with no special meaning is treated as a literal. (Perl can, however, be persuaded to give an error for this, by running it with the -w option.) There are at present no other features controlled by this option. It can also be set by a (?X) option setting within a pattern. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_FIRSTLINE </p>
<p> If this option is set, an unanchored pattern is required to match before or at the first newline in the subject string, though the matched text may continue over the newline. </p>
<p>&nbsp;<wbr>&nbsp;PCRE_JAVASCRIPT_COMPAT </p>
<p> If this option is set, PCRE&#8217;s behaviour is changed in some ways so that it is compatible with JavaScript rather than Perl. The changes are as follows: </p>
<p> (1) A lone closing square bracket in a pattern causes a compile-time error, because this is illegal in JavaScript (by default it is treated as a data character). Thus, the pattern AB]CD becomes illegal when this option is set. </p>
<p> (2) At run time, a back reference to an unset subpattern group matches an empty string (by default this causes the current matching alternative to fail). A pattern such as (\1)(a) succeeds when this option is set (assuming it can find an &quot;a&quot; in the subject), whereas it fails by default, for Perl compatibility. </p>
<p> (3) 
