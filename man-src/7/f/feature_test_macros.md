---
title: "feature_test_macros(7)"
name: "feature_test_macros"
section: "7"
letter: "f"
url: "/docs/linux/man/7-feature_test_macros/"
description: "feature_test_macros – feature test macros"
---

<p>feature_test_macros &#8211; feature test macros</p>
<h2>Description</h2>
<p>Feature test macros allow the programmer to control the definitions that are exposed by system header files when a program is compiled. <code>NOTE:</code> In order to be effective, a feature test macro <i>must be defined before including any header files</i>. This can be done either in the compilation command (<i>cc -DMACRO=value</i>) or by defining the macro within the source code before including any headers. The requirement that the macro must be defined before including any header file exists because header files may freely include one another. Thus, for example, in the following lines, defining the <code>_GNU_SOURCE</code> macro may have no effect because the header <i>&lt;abc.h&gt;</i> itself includes <i>&lt;xyz.h&gt;</i> (POSIX explicitly allows this): </p>
<pre><code>#include &lt;abc.h&gt;
#define _GNU_SOURCE
#include &lt;xyz.h&gt;</code></pre>
<p> Some feature test macros are useful for creating portable applications, by preventing nonstandard definitions from being exposed. Other macros can be used to expose nonstandard definitions that are not exposed by default. The precise effects of each of the feature test macros described below can be ascertained by inspecting the <i>&lt;features.h&gt;</i> header file. <code>Note</code>: applications do <i>not</i> need to directly include <i>&lt;features.h&gt;</i>; indeed, doing so is actively discouraged. See NOTES.</p>
<h3>Specification of feature test macro requirements in manual pages</h3>
<p>When a function requires that a feature test macro is defined, the manual page SYNOPSIS typically includes a note of the following form (this example from the <code><a href="/docs/linux/man/2-acct/">acct</a></code>(2) manual page): #include &lt;unistd.h&gt;<br />
int acct(const char *filename);</dl>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>acct</code>(): _BSD_SOURCE || (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE&nbsp;&lt;&nbsp;500) The <code>||</code> means that in order to obtain the declaration of <code><a href="/docs/linux/man/2-acct/">acct</a></code>(2) from <i>&lt;unistd.h&gt;</i>, <i>either</i> of the following macro definitions must be made before including any header files: #define _BSD_SOURCE<br />
#define _XOPEN_SOURCE        /* or any value &lt; 500 */ Alternatively, equivalent definitions can be included in the compilation command: cc -D_BSD_SOURCE cc -D_XOPEN_SOURCE # Or any value &lt; 500 Note that, as described below, <code>some feature test macros are defined by default</code>, so that it may not always be necessary to explicitly specify the feature test macro(s) shown in the SYNOPSIS. In a few cases, manual pages use a shorthand for expressing the feature test macro requirements (this example from <code><a href="/docs/linux/man/2-readahead/">readahead</a></code>(2)): #define _GNU_SOURCE</p>
<p>#include &lt;fcntl.h&gt; <code>ssize_t readahead(int </code><i>fd</i><code>, off64_t *</code><i>offset</i><code>, size_t </code><i>count</i><code>);</code></dl>
<p> This format is employed in cases where only a single feature test macro can be used to expose the function declaration, and that macro is not defined by default.</p>
<h3>Feature test macros understood by glibc</h3>
<p>The paragraphs below explain how feature test macros are handled in Linux glibc 2.<i>x</i>, <i>x</i> &gt; 0. First, though a summary of a few details for the impatient:</p>
<dl>
<dt>*</p>
<dd>The macros that you most likely need to use in modern source code are <code>_POSIX_C_SOURCE</code> (for definitions from various versions of POSIX.1), <code>_XOPEN_SOURCE</code> (for definitions from various versions of SUS), <code>_GNU_SOURCE</code> (for GNU and/or Linux specific stuff), and <code>_DEFAULT_SOURCE</code> (to get definitions that would normally be provided by default).</p>
<dt>*</p>
<dd>Certain macros are defined with default values. Thus, although one or more macros may be indicated as being required in the SYNOPSIS of a man page, it may not be necessary to define them explicitly. Full details of the defaults are given later in this man page.</p>
<dt>*</p>
<dd>Defining <code>_XOPEN_SOURCE</code> with a value of 600 or greater produces the same effects as defining <code>_POSIX_C_SOURCE</code> with a value of 200112L or greater. Where one sees</p>
<dd>_POSIX_C_SOURCE &gt;= 200112L</p>
<dd>in the feature test macro requirements in the SYNOPSIS of a man page, it is implicit that the following has the same effect:</p>
<dd>_XOPEN_SOURCE &gt;= 600</p>
<dt>*</p>
<dd>Defining <code>_XOPEN_SOURCE</code> with a value of 700 or greater produces the same effects as defining <code>_POSIX_C_SOURCE</code> with a value of 200809L or greater. Where one sees</p>
<dd>_POSIX_C_SOURCE &gt;= 200809L</p>
<dd>in the feature test macro requirements in the SYNOPSIS of a man page, it is implicit that the following has the same effect:</p>
<dd>_XOPEN_SOURCE &gt;= 700</dl>
<p> Linux glibc understands the following feature test macros:</p>
<dl>
<dt><code>__STRICT_ANSI__</code></p>
<dd>ISO Standard C. This macro is implicitly defined by <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) when invoked with, for example, the <i>-std=c99</i> or <i>-ansi</i> flag.</p>
<dt><code>_POSIX_C_SOURCE</code></p>
<dd>Defining this macro causes header files to expose definitions as follows:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>The value 1 exposes definitions conforming to POSIX.1-1990 and ISO C (1990).</p>
<dt>&bull;</p>
<dd>The value 2 or greater additionally exposes definitions for POSIX.2-1992.</p>
<dt>&bull;</p>
<dd>The value 199309L or greater additionally exposes definitions for POSIX.1b (real-time extensions).</p>
<dt>&bull;</p>
<dd>The value 199506L or greater additionally exposes definitions for POSIX.1c (threads).</p>
<dt>&bull;</p>
<dd>(Since glibc 2.3.3) The value 200112L or greater additionally exposes definitions corresponding to the POSIX.1-2001 base specification (excluding the XSI extension). This value also causes C95 (since glibc 2.12) and C99 (since glibc 2.10) features to be exposed (in other words, the equivalent of defining <code>_ISOC99_SOURCE</code>).</p>
<dt>&bull;</p>
<dd>(Since glibc 2.10) The value 200809L or greater additionally exposes definitions corresponding to the POSIX.1-2008 base specification (excluding the XSI extension).</dl>
</dl>
<dt><code>_POSIX_SOURCE</code></p>
<dd>Defining this obsolete macro with any value is equivalent to defining <code>_POSIX_C_SOURCE</code> with the value 1.</p>
<dd>Since this macro is obsolete, its usage is generally not documented when discussing feature test macro requirements in the man pages.</p>
<dt><code>_XOPEN_SOURCE</code></p>
<dd>Defining this macro causes header files to expose definitions as follows:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Defining with any value exposes definitions conforming to POSIX.1, POSIX.2, and XPG4.</p>
<dt>&bull;</p>
<dd>The value 500 or greater additionally exposes definitions for SUSv2 (UNIX 98).</p>
<dt>&bull;</p>
<dd>(Since glibc 2.2) The value 600 or greater additionally exposes definitions for SUSv3 (UNIX 03; i.e., the POSIX.1-2001 base specification plus the XSI extension) and C99 definitions.</p>
<dt>&bull;</p>
<dd>(Since glibc 2.10) The value 700 or greater additionally exposes definitions for SUSv4 (i.e., the POSIX.1-2008 base specification plus the XSI extension).</dl>
</dl>
<dd>If <code>__STRICT_ANSI__</code> is not defined, or <code>_XOPEN_SOURCE</code> is defined with a value greater than or equal to 500 <i>and</i> neither <code>_POSIX_SOURCE</code> nor <code>_POSIX_C_SOURCE</code> is explicitly defined, then the following macros are implicitly defined:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>_POSIX_SOURCE</code> is defined with the value 1.</p>
<dt>&bull;</p>
<dd><code>_POSIX_C_SOURCE</code> is defined, according to the value of <code>_XOPEN_SOURCE</code>:</p>
<dl>
<dd>
<dl>
<dt><code>_XOPEN_SOURCE</code> &lt; 500</p>
<dd><code>_POSIX_C_SOURCE</code> is defined with the value 2.</p>
<dt>500 &lt;= <code>_XOPEN_SOURCE</code> &lt; 600</p>
<dd><code>_POSIX_C_SOURCE</code> is defined with the value 199506L.</p>
<dt>600 &lt;= <code>_XOPEN_SOURCE</code> &lt; 700</p>
<dd><code>_POSIX_C_SOURCE</code> is defined with the value 200112L.</p>
<dt>700 &lt;= <code>_XOPEN_SOURCE</code> (since glibc 2.10)</p>
<dd><code>_POSIX_C_SOURCE</code> is defined with the value 200809L.</dl>
</dl>
</dl>
</dl>
<dd>In addition, defining <code>_XOPEN_SOURCE</code> with a value of 500 or greater produces the same effects as defining <code>_XOPEN_SOURCE_EXTENDED</code>.</p>
<dt><code>_XOPEN_SOURCE_EXTENDED</code></p>
<dd>If this macro is defined, <i>and</i> <code>_XOPEN_SOURCE</code> is defined, then expose definitions corresponding to the XPG4v2 (SUSv1) UNIX extensions (UNIX 95). Defining <code>_XOPEN_SOURCE</code> with a value of 500 or more also produces the same effect as defining <code>_XOPEN_SOURCE_EXTENDED</code>. Use of <code>_XOPEN_SOURCE_EXTENDED</code> in new source code should be avoided.</p>
<dd>Since defining <code>_XOPEN_SOURCE</code> with a value of 500 or more has the same effect as defining <code>_XOPEN_SOURCE_EXTENDED</code>, the latter (obsolete) feature test macro is generally not described in the SYNOPSIS in man pages.</p>
<dt><code>_ISOC99_SOURCE</code> (since glibc 2.1.3)</p>
<dd>Exposes declarations consistent with the ISO C99 standard.</p>
<dd>Earlier glibc 2.1.x versions recognized an equivalent macro named <code>_ISOC9X_SOURCE</code> (because the C99 standard had not then been finalized). Although the use of this macro is obsolete, glibc continues to recognize it for backward compatibility.</p>
<dd>Defining <code>_ISOC99_SOURCE</code> also exposes ISO C (1990) Amendment 1 (&quot;C95&quot;) definitions. (The primary change in C95 was support for international character sets.)</p>
<dd>Invoking the C compiler with the option <i>-std=c99</i> produces the same effects as defining this macro.</p>
<dt><code>_ISOC11_SOURCE</code> (since glibc 2.16)</p>
<dd>Exposes declarations consistent with the ISO C11 standard. Defining this macro also enables C99 and C95 features (like <code>_ISOC99_SOURCE</code>).</p>
<dd>Invoking the C compiler with the option <i>-std=c11</i> produces the same effects as defining this macro.</p>
<dt><code>_LARGEFILE64_SOURCE</code></p>
<dd>Expose definitions for the alternative API specified by the LFS (Large File Summit) as a &quot;transitional extension&quot; to the Single UNIX Specification. (See The alternative API consists of a set of new objects (i.e., functions and types) whose names are suffixed with &quot;64&quot; (e.g., <i>off64_t</i> versus <i>off_t</i>, <code>lseek64</code>() versus <code>lseek</code>(), etc.). New programs should not employ this macro; instead <i>_FILE_OFFSET_BITS=64</i> should be employed.</p>
<dt><code>_LARGEFILE_SOURCE</code></p>
<dd>This macro was historically used to expose certain functions (specifically <code><a href="/docs/linux/man/3-fseeko/">fseeko</a></code>(3) and <code><a href="/docs/linux/man/3-ftello/">ftello</a></code>(3)) that address limitations of earlier APIs (<code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) and <code><a href="/docs/linux/man/3-ftell/">ftell</a></code>(3)) that use <i>long</i> for file offsets. This macro is implicitly defined if <code>_XOPEN_SOURCE</code> is defined with a value greater than or equal to 500. New programs should not employ this macro; defining <code>_XOPEN_SOURCE</code> as just described or defining <code>_FILE_OFFSET_BITS</code> with the value 64 is the preferred mechanism to achieve the same result.</p>
<dt><code>_FILE_OFFSET_BITS</code></p>
<dd>Defining this macro with the value 64 automatically converts references to 32-bit functions and data types related to file I/O and filesystem operations into references to their 64-bit counterparts. This is useful for performing I/O on large files (&gt; 2 Gigabytes) on 32-bit systems. (Defining this macro permits correctly written programs to use large files with only a recompilation being required.)</p>
<dd>64-bit systems naturally permit file sizes greater than 2 Gigabytes, and on those systems this macro has no effect.</p>
<dt><code>_BSD_SOURCE</code> (deprecated since glibc 2.20)</p>
<dd>Defining this macro with any value causes header files to expose BSD-derived definitions.</p>
<dd>In glibc versions up to and including 2.18, defining this macro also causes BSD definitions to be preferred in some situations where standards conflict, unless one or more of <code>_SVID_SOURCE</code>, <code>_POSIX_SOURCE</code>, <code>_POSIX_C_SOURCE</code>, <code>_XOPEN_SOURCE</code>, <code>_XOPEN_SOURCE_EXTENDED</code>, or <code>_GNU_SOURCE</code> is defined, in which case BSD definitions are disfavored. Since glibc 2.19, <code>_BSD_SOURCE</code> no longer causes BSD definitions to be preferred in case of conflicts.</p>
<dd>Since glibc 2.20, this macro is deprecated. It now has the same effect as defining <code>_DEFAULT_SOURCE</code>, but generates a compile-time warning (unless <code>_DEFAULT_SOURCE</code> is also defined). Use <code>_DEFAULT_SOURCE</code> instead. To allow code that requires <code>_BSD_SOURCE</code> in glibc 2.19 and earlier and <code>_DEFAULT_SOURCE</code> in glibc 2.20 and later to compile without warnings, define <i>both</i> <code>_BSD_SOURCE</code> and <code>_DEFAULT_SOURCE</code>.</p>
<dt><code>_SVID_SOURCE</code> (deprecated since glibc 2.20)</p>
<dd>Defining this macro with any value causes header files to expose System V-derived definitions. (SVID == System V Interface Definition; see <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7).)</p>
<dd>Since glibc 2.20, this macro is deprecated in the same fashion as <code>_BSD_SOURCE</code>.</p>
<dt><code>_DEFAULT_SOURCE</code> (since glibc 2.19)</p>
<dd>This macro can be defined to ensure that the &quot;default&quot; definitions are provided even when the defaults would otherwise be disabled, as happens when individual macros are explicitly defined, or the compiler is invoked in one of its &quot;standard&quot; modes (e.g., <i>cc -std=c99</i>). Defining <code>_DEFAULT_SOURCE</code> without defining other individual macros or invoking the compiler in one of its &quot;standard&quot; modes has no effect.</p>
<dd>The &quot;default&quot; definitions comprise those required by POSIX.1-2008 and ISO C99, as well as various definitions originally derived from BSD and System V. On glibc 2.19 and earlier, these defaults were approximately equivalent to explicitly defining the following:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cc -D_BSD_SOURCE -D_SVID_SOURCE -D_POSIX_C_SOURCE=200809</p>
<dt><code>_ATFILE_SOURCE</code> (since glibc 2.4)</p>
<dd>Defining this macro with any value causes header files to expose declarations of a range of functions with the suffix &quot;at&quot;; see <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2). Since glibc 2.10, this macro is also implicitly defined if <code>_POSIX_C_SOURCE</code> is defined with a value greater than or equal to 200809L.</p>
<dt><code>_GNU_SOURCE</code></p>
<dd>Defining this macro (with any value) implicitly defines <code>_ATFILE_SOURCE</code>, <code>_LARGEFILE64_SOURCE</code>, <code>_ISOC99_SOURCE</code>, <code>_XOPEN_SOURCE_EXTENDED</code>, <code>_POSIX_SOURCE</code>, <code>_POSIX_C_SOURCE</code> with the value 200809L (200112L in glibc versions before 2.10; 199506L in glibc versions before 2.5; 199309L in glibc versions before 2.1) and <code>_XOPEN_SOURCE</code> with the value 700 (600 in glibc versions before 2.10; 500 in glibc versions before 2.2). In addition, various GNU-specific extensions are also exposed.</p>
<dd>Since glibc 2.19, defining <code>_GNU_SOURCE</code> also has the effect of implicitly defining <code>_DEFAULT_SOURCE</code>. In glibc versions before 2.20, defining <code>_GNU_SOURCE</code> also had the effect of implicitly defining <code>_BSD_SOURCE</code> and <code>_SVID_SOURCE</code>.</p>
<dt><code>_REENTRANT</code></p>
<dd>Historically, on various C libraries it was necessary to define this macro in all multithreaded code. (Some C libraries may still require this.) In glibc, this macro also exposed definitions of certain reentrant functions.</p>
<dd>However, glibc has been thread-safe by default for many years; since glibc 2.3, the only effect of defining <code>_REENTRANT</code> has been to enable one or two of the same declarations that are also enabled by defining <code>_POSIX_C_SOURCE</code> with a value of 199606L or greater.</p>
<dd><code>_REENTRANT</code> is now obsolete. In glibc 2.25 and later, defining <code>_REENTRANT</code> is equivalent to defining <code>_POSIX_C_SOURCE</code> with the value 199606L. If a higher POSIX conformance level is selected by any other means (such as <code>_POSIX_C_SOURCE</code> itself, <code>_XOPEN_SOURCE</code>, <code>_DEFAULT_SOURCE</code>, or <code>_GNU_SOURCE</code>), then defining <code>_REENTRANT</code> has no effect.</p>
<dd>This macro is automatically defined if one compiles with <i>cc -pthread</i>.</p>
<dt><code>_THREAD_SAFE</code></p>
<dd>Synonym for the (deprecated) <code>_REENTRANT</code>, provided for compatibility with some other implementations.</p>
<dt><code>_FORTIFY_SOURCE</code> (since glibc 2.3.4)</p>
<dd>Defining this macro causes some lightweight checks to be performed to detect some buffer overflow errors when employing various string and memory manipulation functions (for example, <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3), <code><a href="/docs/linux/man/3-stpcpy/">stpcpy</a></code>(3), <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3), <code><a href="/docs/linux/man/3-strcat/">strcat</a></code>(3), <code><a href="/docs/linux/man/3-strncat/">strncat</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), <code><a href="/docs/linux/man/3-snprintf/">snprintf</a></code>(3), <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3), <code><a href="/docs/linux/man/3-vsnprintf/">vsnprintf</a></code>(3), <code><a href="/docs/linux/man/3-gets/">gets</a></code>(3), and wide character variants thereof). For some functions, argument consistency is checked; for example, a check is made that <code><a href="/docs/linux/man/2-open/">open</a></code>(2) has been supplied with a <i>mode</i> argument when the specified flags include <code>O_CREAT</code>. Not all problems are detected, just some common cases.</p>
<dd>If <code>_FORTIFY_SOURCE</code> is set to 1, with compiler optimization level 1 (<i>gcc -O1</i>) and above, checks that shouldn&#8217;t change the behavior of conforming programs are performed. With <code>_FORTIFY_SOURCE</code> set to 2, some more checking is added, but some conforming programs might fail.</p>
<dd>Some of the checks can be performed at compile time (via macros logic implemented in header files), and result in compiler warnings; other checks take place at run time, and result in a run-time error if the check fails.</p>
<dd>Use of this macro requires compiler support, available with <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) since version 4.0.</dl>
<h3>Default definitions, implicit definitions, and combining definitions</h3>
<p>If no feature test macros are explicitly defined, then the following feature test macros are defined by default: <code>_BSD_SOURCE</code> (in glibc 2.19 and earlier), <code>_SVID_SOURCE</code> (in glibc 2.19 and earlier), <code>_DEFAULT_SOURCE</code> (since glibc 2.19), <code>_POSIX_SOURCE</code>, and <code>_POSIX_C_SOURCE</code>=200809L (200112L in glibc versions before 2.10; 199506L in glibc versions before 2.4; 199309L in glibc versions before 2.1). If any of <code>__STRICT_ANSI__</code>, <code>_ISOC99_SOURCE</code>, <code>_ISOC11_SOURCE</code> (since glibc 2.18), <code>_POSIX_SOURCE</code>, <code>_POSIX_C_SOURCE</code>, <code>_XOPEN_SOURCE</code>, <code>_XOPEN_SOURCE_EXTENDED</code> (in glibc 2.11 and earlier), <code>_BSD_SOURCE</code> (in glibc 2.19 and earlier), or <code>_SVID_SOURCE</code> (in glibc 2.19 and earlier) is explicitly defined, then <code>_BSD_SOURCE</code>, <code>_SVID_SOURCE</code>, and <code>_DEFAULT_SOURCE</code> are not defined by default. If <code>_POSIX_SOURCE</code> and <code>_POSIX_C_SOURCE</code> are not explicitly defined, and either <code>__STRICT_ANSI__</code> is not defined or <code>_XOPEN_SOURCE</code> is defined with a value of 500 or more, then</p>
<dl>
<dt>*</p>
<dd><code>_POSIX_SOURCE</code> is defined with the value 1; and</p>
<dt>*</p>
<dd><code>_POSIX_C_SOURCE</code> is defined with one of the following values:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>2, if <code>_XOPEN_SOURCE</code> is defined with a value less than 500;</p>
<dt>&bull;</p>
<dd>199506L, if <code>_XOPEN_SOURCE</code> is defined with a value greater than or equal to 500 and less than 600; or</p>
<dt>&bull;</p>
<dd>(since glibc 2.4) 200112L, if <code>_XOPEN_SOURCE</code> is defined with a value greater than or equal to 600 and less than 700.</p>
<dt>&bull;</p>
<dd>(Since glibc 2.10) 200809L, if <code>_XOPEN_SOURCE</code> is defined with a value greater than or equal to 700.</p>
<dt>&bull;</p>
<dd>Older versions of glibc do not know about the values 200112L and 200809L for <code>_POSIX_C_SOURCE</code>, and the setting of this macro will depend on the glibc version.</p>
<dt>&bull;</p>
<dd>If <code>_XOPEN_SOURCE</code> is undefined, then the setting of <code>_POSIX_C_SOURCE</code> depends on the glibc version: 199506L, in glibc versions before 2.4; 200112L, in glibc 2.4 to 2.9; and 200809L, since glibc 2.10.</dl>
</dl>
</dl>
<p> Multiple macros can be defined; the results are additive.</p>
<h2>Conforming To</h2>
<p>POSIX.1 specifies <code>_POSIX_C_SOURCE</code>, <code>_POSIX_SOURCE</code>, and <code>_XOPEN_SOURCE</code>. </p>
<p> <code>_XOPEN_SOURCE_EXTENDED</code> was specified by XPG4v2 (aka SUSv1), but is not present in SUSv2 and later. <code>_FILE_OFFSET_BITS</code> is not specified by any standard, but is employed on some other implementations. </p>
<p> <code>_BSD_SOURCE</code>, <code>_SVID_SOURCE</code>, <code>_DEFAULT_SOURCE</code>, <code>_ATFILE_SOURCE</code>, <code>_GNU_SOURCE</code>, <code>_FORTIFY_SOURCE</code>, <code>_REENTRANT</code>, and <code>_THREAD_SAFE</code> are specific to Linux (glibc).</p>
<h2>Notes</h2>
<p><i>&lt;features.h&gt;</i> is a Linux/glibc-specific header file. Other systems have an analogous file, but typically with a different name. This header file is automatically included by other header files as required: it is not necessary to explicitly include it in order to employ feature test macros. </p>
<p> According to which of the above feature test macros are defined, <i>&lt;features.h&gt;</i> internally defines various other macros that are checked by other glibc header files. These macros have names prefixed by two underscores (e.g., <code>__USE_MISC</code>). Programs should <i>never</i> define these macros directly: instead, the appropriate feature test macro(s) from the list above should be employed.</p>
<h2>Examples</h2>
<p>The program below can be used to explore how the various feature test macros are set depending on the glibc version and what feature test macros are explicitly set. The following shell session, on a system with glibc 2.10, shows some examples of what we would see: $ <code>cc ftm.c</code> $ <code>./a.out</code> _POSIX_SOURCE defined _POSIX_C_SOURCE defined: 200809L _BSD_SOURCE defined _SVID_SOURCE defined _ATFILE_SOURCE defined $ <code>cc -D_XOPEN_SOURCE=500 ftm.c</code> $ <code>./a.out</code> _POSIX_SOURCE defined _POSIX_C_SOURCE defined: 199506L _XOPEN_SOURCE defined: 500 $ <code>cc -D_GNU_SOURCE ftm.c</code> $ <code>./a.out</code> _POSIX_SOURCE defined _POSIX_C_SOURCE defined: 200809L _ISOC99_SOURCE defined _XOPEN_SOURCE defined: 700 _XOPEN_SOURCE_EXTENDED defined _LARGEFILE64_SOURCE defined _BSD_SOURCE defined _SVID_SOURCE defined _ATFILE_SOURCE defined _GNU_SOURCE defined</p>
<h3>Program source</h3>
<p>/* ftm.c */ #include &lt;stdint.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;unistd.h&gt;<br />
#include &lt;stdlib.h&gt; int main(int argc, char *argv[]) { #ifdef _POSIX_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_POSIX_SOURCE defined
&quot;); #endif #ifdef _POSIX_C_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_POSIX_C_SOURCE defined:&nbsp;%jdL
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;_POSIX_C_SOURCE); #endif #ifdef _ISOC99_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_ISOC99_SOURCE defined
&quot;); #endif #ifdef _ISOC11_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_ISOC11_SOURCE defined
&quot;); #endif #ifdef _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_XOPEN_SOURCE defined:&nbsp;%d
&quot;,&nbsp;_XOPEN_SOURCE); #endif #ifdef _XOPEN_SOURCE_EXTENDED<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_XOPEN_SOURCE_EXTENDED defined
&quot;); #endif #ifdef _LARGEFILE64_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_LARGEFILE64_SOURCE defined
&quot;); #endif #ifdef _FILE_OFFSET_BITS<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_FILE_OFFSET_BITS defined:&nbsp;%d
&quot;,&nbsp;_FILE_OFFSET_BITS); #endif #ifdef _BSD_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_BSD_SOURCE defined
&quot;); #endif #ifdef _SVID_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_SVID_SOURCE defined
&quot;); #endif #ifdef _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_DEFAULT_SOURCE defined
&quot;); #endif #ifdef _ATFILE_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_ATFILE_SOURCE defined
&quot;); #endif #ifdef _GNU_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_GNU_SOURCE defined
&quot;); #endif #ifdef _REENTRANT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_REENTRANT defined
&quot;); #endif #ifdef _THREAD_SAFE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_THREAD_SAFE defined
&quot;); #endif #ifdef _FORTIFY_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;_FORTIFY_SOURCE defined
&quot;); #endif </p>
<pre><code>exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-libc/">libc</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7), <code><a href="/docs/linux/man/7-system_data_types/">system_data_types</a></code>(7) </p>
<p> The section &quot;Feature Test Macros&quot; under <i>info libc</i>. </p>
<p> <i>/usr/include/features.h</i></p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
