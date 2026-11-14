---
title: "pcre2(3)"
name: "pcre2"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Introduction</h2>
<p>PCRE2 is the name used for a revised API for the PCRE library, which is a set of functions, written in C, that implement regular expression pattern matching using the same syntax and semantics as Perl, with just a few differences. After nearly two decades, the limitations of the original API were making development increasingly difficult. The new API is more extensible, and it was simplified by abolishing the separate &quot;study&quot; optimizing function; in PCRE2, patterns are automatically optimized where possible. Since forking from PCRE1, the code has been extensively refactored and new features introduced. </p>
<p> As well as Perl-style regular expression patterns, some features that appeared in Python and the original PCRE before they appeared in Perl are available using the Python syntax. There is also some support for one or two .NET and Oniguruma syntax items, and there are options for requesting some minor changes that give better ECMAScript (aka JavaScript) compatibility. </p>
<p> The source code for PCRE2 can be compiled to support 8-bit, 16-bit, or 32-bit code units, which means that up to three separate libraries may be installed. The original work to extend PCRE to 16-bit and 32-bit code units was done by Zoltan Herczeg and Christian Persch, respectively. In all three cases, strings can be interpreted either as one character per code unit, or as UTF-encoded Unicode, with support for Unicode general category properties. Unicode support is optional at build time (but is the default). However, processing strings as UTF code units must be enabled explicitly at run time. The version of Unicode in use can be discovered by running </p>
<p>&nbsp;<wbr>&nbsp;pcre2test -C </p>
<p> The three libraries contain identical sets of functions, with names ending in _8, _16, or _32, respectively (for example, <code>pcre2_compile_8()</code>). However, by defining PCRE2_CODE_UNIT_WIDTH to be 8, 16, or 32, a program that uses just one code unit width can be written using generic names such as <code>pcre2_compile()</code>, and the documentation is written assuming that this is the case. </p>
<p> In addition to the Perl-compatible matching function, PCRE2 contains an alternative function that matches the same compiled patterns in a different way. In certain circumstances, the alternative function has some advantages. For a discussion of the two matching algorithms, see the <code>pcre2matching</code> page. </p>
<p> Details of exactly which Perl regular expression features are and are not supported by PCRE2 are given in separate documents. See the <code>pcre2pattern</code> and <code>pcre2compat</code> pages. There is a syntax summary in the <code>pcre2syntax</code> page. </p>
<p> Some features of PCRE2 can be included, excluded, or changed when the library is built. The <code>pcre2_config()</code> function makes it possible for a client to discover which features are available. The features themselves are described in the <code>pcre2build</code> page. Documentation about building PCRE2 for various operating systems can be found in the <code>README</code> and <code>NON-AUTOTOOLS_BUILD</code> files in the source distribution. </p>
<p> The libraries contains a number of undocumented internal functions and data tables that are used by more than one of the exported external functions, but which are not intended for use by external callers. Their names all begin with &quot;_pcre2&quot;, which hopefully will not provoke any name clashes. In some environments, it is possible to control which external symbols are exported when a shared library is built, and in these cases the undocumented symbols are not exported.</p>
<h2>Security Considerations</h2>
<p>If you are using PCRE2 in a non-UTF application that permits users to supply arbitrary patterns for compilation, you should be aware of a feature that allows users to turn on UTF support from within a pattern. For example, an 8-bit pattern that begins with &quot;(*UTF)&quot; turns on UTF-8 mode, which interprets patterns and subjects as strings of UTF-8 code units instead of individual 8-bit characters. This causes both the pattern and any data against which it is matched to be checked for UTF-8 validity. If the data string is very long, such a check might use sufficiently many resources as to cause your application to lose performance. </p>
<p> One way of guarding against this possibility is to use the <code>pcre2_pattern_info()</code> function to check the compiled pattern&#8217;s options for PCRE2_UTF. Alternatively, you can set the PCRE2_NEVER_UTF option when calling <code>pcre2_compile()</code>. This causes a compile time error if the pattern contains a UTF-setting sequence. </p>
<p> The use of Unicode properties for character types such as \d can also be enabled from within the pattern, by specifying &quot;(*UCP)&quot;. This feature can be disallowed by setting the PCRE2_NEVER_UCP option. </p>
<p> If your application is one that supports UTF, be aware that validity checking can take time. If the same data string is to be matched many times, you can use the PCRE2_NO_UTF_CHECK option for the second and subsequent matches to avoid running redundant checks. </p>
<p> The use of the \C escape sequence in a UTF-8 or UTF-16 pattern can lead to problems, because it may leave the current matching point in the middle of a multi-code-unit character. The PCRE2_NEVER_BACKSLASH_C option can be used by an application to lock out the use of \C, causing a compile-time error if it is encountered. It is also possible to build PCRE2 with the use of \C permanently disabled. </p>
<p> Another way that performance can be hit is by running a pattern that has a very large search tree against a string that will never match. Nested unlimited repeats in a pattern are a common example. PCRE2 provides some protection against this: see the <code>pcre2_set_match_limit()</code> function in the <code>pcre2api</code> page. There is a similar function called <code>pcre2_set_depth_limit()</code> that can be used to restrict the amount of memory that is used.</p>
<h2>User Documentation</h2>
<p>The user documentation for PCRE2 comprises a number of different sections. In the &quot;man&quot; format, each of these is a separate &quot;man page&quot;. In the HTML format, each is a separate page, linked from the index page. In the plain text format, the descriptions of the <code>pcre2grep</code> and <code>pcre2test</code> programs are in files called <code>pcre2grep.txt</code> and <code>pcre2test.txt</code>, respectively. The remaining sections, except for the <code>pcre2demo</code> section (which is a program listing), and the short pages for individual functions, are concatenated in <code>pcre2.txt</code>, for ease of searching. The sections are as follows: </p>
<p>&nbsp;<wbr>&nbsp;pcre2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;this document<br />
&nbsp;<wbr>&nbsp;pcre2-config&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;show PCRE2 installation configuration information<br />
&nbsp;<wbr>&nbsp;pcre2api&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of PCRE2&#8217;s native C API<br />
&nbsp;<wbr>&nbsp;pcre2build&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;building PCRE2<br />
&nbsp;<wbr>&nbsp;pcre2callout&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of the pattern callout feature<br />
&nbsp;<wbr>&nbsp;pcre2compat&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of Perl compatibility<br />
&nbsp;<wbr>&nbsp;pcre2convert&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of pattern conversion functions<br />
&nbsp;<wbr>&nbsp;pcre2demo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a demonstration C program that uses PCRE2<br />
&nbsp;<wbr>&nbsp;pcre2grep&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;description of the&nbsp;<code>pcre2grep</code>&nbsp;command&nbsp;(8-bit only)<br />
&nbsp;<wbr>&nbsp;pcre2jit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of just-in-time optimization support<br />
&nbsp;<wbr>&nbsp;pcre2limits&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of size and other limits<br />
&nbsp;<wbr>&nbsp;pcre2matching&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of the two matching algorithms<br />
&nbsp;<wbr>&nbsp;pcre2partial&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of the partial matching facility<br />
&nbsp;<wbr>&nbsp;pcre2pattern&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;syntax and semantics of supported regular<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;expression patterns<br />
&nbsp;<wbr>&nbsp;pcre2perform&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of performance issues<br />
&nbsp;<wbr>&nbsp;pcre2posix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the POSIX-compatible C API for the 8-bit library<br />
&nbsp;<wbr>&nbsp;pcre2sample&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of the pcre2demo program<br />
&nbsp;<wbr>&nbsp;pcre2serialize&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of pattern serialization<br />
&nbsp;<wbr>&nbsp;pcre2syntax&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;quick syntax reference<br />
&nbsp;<wbr>&nbsp;pcre2test&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;description of the&nbsp;<code>pcre2test</code>&nbsp;command<br />
&nbsp;<wbr>&nbsp;pcre2unicode&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of Unicode and UTF support </p>
<p> In the &quot;man&quot; and HTML formats, there is also a short page for each C library function, listing its arguments and results.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<p>Putting an actual email address here is a spam magnet. If you want to email me, use my two initials, followed by the two digits 10, at the domain cam.ac.uk.</p>
<h2>Revision</h2>
<pre>Last updated: 17 September 2018
Copyright (c) 1997-2018 University of Cambridge.</pre>
