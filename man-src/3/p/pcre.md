---
title: "pcre(3)"
name: "pcre"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre/"
description: "PCRE – Perl-compatible regular expressions (original API)"
---

<p>PCRE &#8211; Perl-compatible regular expressions (original API)</p>
<h2>Please Take Note</h2>
<p>This document relates to PCRE releases that use the original API, with library names libpcre, libpcre16, and libpcre32. January 2015 saw the first release of a new API, known as PCRE2, with release numbers starting at 10.00 and library names libpcre2-8, libpcre2-16, and libpcre2-32. The old libraries (now called PCRE1) are still being maintained for bug fixes, but there will be no new development. New projects are advised to use the new PCRE2 libraries.</p>
<h2>Introduction</h2>
<p>The PCRE library is a set of functions that implement regular expression pattern matching using the same syntax and semantics as Perl, with just a few differences. Some features that appeared in Python and PCRE before they appeared in Perl are also available using the Python syntax, there is some support for one or two .NET and Oniguruma syntax items, and there is an option for requesting some minor changes that give better JavaScript compatibility. </p>
<p> Starting with release 8.30, it is possible to compile two separate PCRE libraries: the original, which supports 8-bit character strings (including UTF-8 strings), and a second library that supports 16-bit character strings (including UTF-16 strings). The build process allows either one or both to be built. The majority of the work to make this possible was done by Zoltan Herczeg. </p>
<p> Starting with release 8.32 it is possible to compile a third separate PCRE library that supports 32-bit character strings (including UTF-32 strings). The build process allows any combination of the 8-, 16- and 32-bit libraries. The work to make this possible was done by Christian Persch. </p>
<p> The three libraries contain identical sets of functions, except that the names in the 16-bit library start with <code>pcre16_</code> instead of <code>pcre_</code>, and the names in the 32-bit library start with <code>pcre32_</code> instead of <code>pcre_</code>. To avoid over-complication and reduce the documentation maintenance load, most of the documentation describes the 8-bit library, with the differences for the 16-bit and 32-bit libraries described separately in the <code>pcre16</code> and <code>pcre32</code> pages. References to functions or structures of the form <i>pcre[16|32]_xxx</i> should be read as meaning &quot;<i>pcre_xxx</i> when using the 8-bit library, <i>pcre16_xxx</i> when using the 16-bit library, or <i>pcre32_xxx</i> when using the 32-bit library&quot;. </p>
<p> The current implementation of PCRE corresponds approximately with Perl 5.12, including support for UTF-8/16/32 encoded strings and Unicode general category properties. However, UTF-8/16/32 and Unicode support has to be explicitly enabled; it is not the default. The Unicode tables correspond to Unicode release 6.3.0. </p>
<p> In addition to the Perl-compatible matching function, PCRE contains an alternative function that matches the same compiled patterns in a different way. In certain circumstances, the alternative function has some advantages. For a discussion of the two matching algorithms, see the <code>pcrematching</code> page. </p>
<p> PCRE is written in C and released as a C library. A number of people have written wrappers and interfaces of various kinds. In particular, Google Inc. have provided a comprehensive C++ wrapper for the 8-bit library. This is now included as part of the PCRE distribution. The <code>pcrecpp</code> page has details of this interface. Other people&#8217;s contributions can be found in the <i>Contrib</i> directory at the primary FTP site, which is: </p>
<p> <a href="ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre">ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre</a> </p>
<p> Details of exactly which Perl regular expression features are and are not supported by PCRE are given in separate documents. See the <code>pcrepattern</code> and <code>pcrecompat</code> pages. There is a syntax summary in the <code>pcresyntax</code> page. </p>
<p> Some features of PCRE can be included, excluded, or changed when the library is built. The <code>pcre_config()</code> function makes it possible for a client to discover which features are available. The features themselves are described in the <code>pcrebuild</code> page. Documentation about building PCRE for various operating systems can be found in the <code>README</code> and <code>NON-AUTOTOOLS_BUILD</code> files in the source distribution. </p>
<p> The libraries contains a number of undocumented internal functions and data tables that are used by more than one of the exported external functions, but which are not intended for use by external callers. Their names all begin with &quot;_pcre_&quot; or &quot;_pcre16_&quot; or &quot;_pcre32_&quot;, which hopefully will not provoke any name clashes. In some environments, it is possible to control which external symbols are exported when a shared library is built, and in these cases the undocumented symbols are not exported.</p>
<h2>Security Considerations</h2>
<p>If you are using PCRE in a non-UTF application that permits users to supply arbitrary patterns for compilation, you should be aware of a feature that allows users to turn on UTF support from within a pattern, provided that PCRE was built with UTF support. For example, an 8-bit pattern that begins with &quot;(*UTF8)&quot; or &quot;(*UTF)&quot; turns on UTF-8 mode, which interprets patterns and subjects as strings of UTF-8 characters instead of individual 8-bit characters. This causes both the pattern and any data against which it is matched to be checked for UTF-8 validity. If the data string is very long, such a check might use sufficiently many resources as to cause your application to lose performance. </p>
<p> One way of guarding against this possibility is to use the <code>pcre_fullinfo()</code> function to check the compiled pattern&#8217;s options for UTF. Alternatively, from release 8.33, you can set the PCRE_NEVER_UTF option at compile time. This causes an compile time error if a pattern contains a UTF-setting sequence. </p>
<p> If your application is one that supports UTF, be aware that validity checking can take time. If the same data string is to be matched many times, you can use the PCRE_NO_UTF[8|16|32]_CHECK option for the second and subsequent matches to save redundant checks. </p>
<p> Another way that performance can be hit is by running a pattern that has a very large search tree against a string that will never match. Nested unlimited repeats in a pattern are a common example. PCRE provides some protection against this: see the PCRE_EXTRA_MATCH_LIMIT feature in the <code>pcreapi</code> page.</p>
<h2>User Documentation</h2>
<p>The user documentation for PCRE comprises a number of different sections. In the &quot;man&quot; format, each of these is a separate &quot;man page&quot;. In the HTML format, each is a separate page, linked from the index page. In the plain text format, the descriptions of the <code>pcregrep</code> and <code>pcretest</code> programs are in files called <code>pcregrep.txt</code> and <code>pcretest.txt</code>, respectively. The remaining sections, except for the <code>pcredemo</code> section (which is a program listing), are concatenated in <code>pcre.txt</code>, for ease of searching. The sections are as follows: </p>
<p>&nbsp;<wbr>&nbsp;pcre&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;this document<br />
&nbsp;<wbr>&nbsp;pcre-config&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;show PCRE installation configuration information<br />
&nbsp;<wbr>&nbsp;pcre16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of the 16-bit library<br />
&nbsp;<wbr>&nbsp;pcre32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of the 32-bit library<br />
&nbsp;<wbr>&nbsp;pcreapi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of PCRE&#8217;s native C API<br />
&nbsp;<wbr>&nbsp;pcrebuild&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;building PCRE<br />
&nbsp;<wbr>&nbsp;pcrecallout&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of the callout feature<br />
&nbsp;<wbr>&nbsp;pcrecompat&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of Perl compatibility<br />
&nbsp;<wbr>&nbsp;pcrecpp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of the C++&nbsp;wrapper for the 8-bit library<br />
&nbsp;<wbr>&nbsp;pcredemo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a demonstration C program that uses PCRE<br />
&nbsp;<wbr>&nbsp;pcregrep&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;description of the&nbsp;<code>pcregrep</code>&nbsp;command&nbsp;(8-bit only)<br />
&nbsp;<wbr>&nbsp;pcrejit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of the just-in-time optimization support<br />
&nbsp;<wbr>&nbsp;pcrelimits&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of size and other limits<br />
&nbsp;<wbr>&nbsp;pcrematching&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of the two matching algorithms<br />
&nbsp;<wbr>&nbsp;pcrepartial&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of the partial matching facility<br />
&nbsp;<wbr>&nbsp;pcrepattern&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;syntax and semantics of supported<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regular expressions<br />
&nbsp;<wbr>&nbsp;pcreperform&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of performance issues<br />
&nbsp;<wbr>&nbsp;pcreposix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the POSIX-compatible C API for the 8-bit library<br />
&nbsp;<wbr>&nbsp;pcreprecompile&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details of saving and re-using precompiled patterns<br />
&nbsp;<wbr>&nbsp;pcresample&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of the pcredemo program<br />
&nbsp;<wbr>&nbsp;pcrestack&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of stack usage<br />
&nbsp;<wbr>&nbsp;pcresyntax&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;quick syntax reference<br />
&nbsp;<wbr>&nbsp;pcretest&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;description of the&nbsp;<code>pcretest</code>&nbsp;testing command<br />
&nbsp;<wbr>&nbsp;pcreunicode&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;discussion of Unicode and UTF-8/16/32 support </p>
<p> In the &quot;man&quot; and HTML formats, there is also a short page for each C library function, listing its arguments and results.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.</pre>
<p>Putting an actual email address here seems to have been a spam magnet, so I&#8217;ve taken it away. If you want to email me, use my two initials, followed by the two digits 10, at the domain cam.ac.uk.</p>
<h2>Revision</h2>
<pre>Last updated: 10 February 2015
Copyright (c) 1997-2015 University of Cambridge.</pre>
