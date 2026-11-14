---
title: "pcre2build(3)"
name: "pcre2build"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2build/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Building Pcre2</h2>
<p>PCRE2 is distributed with a <code>configure</code> script that can be used to build the library in Unix-like environments using the applications known as Autotools. Also in the distribution are files to support building using <code>CMake</code> instead of <code>configure</code>. The text file <code>README</code> contains general information about building with Autotools (some of which is repeated below), and also has some comments about building on various operating systems. There is a lot more information about building PCRE2 without using Autotools (including information about using <code>CMake</code> and building &quot;by hand&quot;) in the text file called <code>NON-AUTOTOOLS-BUILD</code>. You should consult this file as well as the <code>README</code> file if you are building in a non-Unix-like environment.</p>
<h2>Pcre2 Build-Time Options</h2>
<p>The rest of this document describes the optional features of PCRE2 that can be selected when the library is compiled. It assumes use of the <code>configure</code> script, where the optional features are selected or deselected by providing options to <code>configure</code> before running the <code>make</code> command. However, the same options can be selected in both Unix-like and non-Unix-like environments if you are using <code>CMake</code> instead of <code>configure</code> to build PCRE2. </p>
<p> If you are not using Autotools or <code>CMake</code>, option selection can be done by editing the <code>config.h</code> file, or by passing parameter settings to the compiler, as described in <code>NON-AUTOTOOLS-BUILD</code>. </p>
<p> The complete list of options for <code>configure</code> (which includes the standard ones such as the selection of the installation directory) can be obtained by running </p>
<p>&nbsp;<wbr>&nbsp;./configure &#8211;help </p>
<p> The following sections include descriptions of &quot;on/off&quot; options whose names begin with &#8211;enable or &#8211;disable. Because of the way that <code>configure</code> works, &#8211;enable and &#8211;disable always come in pairs, so the complementary option always exists as well, but as it specifies the default, it is not described. Options that specify values have names that start with &#8211;with. At the end of a <code>configure</code> run, a summary of the configuration is output.</p>
<h2>Building 8-Bit, 16-Bit And 32-Bit Libraries</h2>
<p>By default, a library called <code>libpcre2-8</code> is built, containing functions that take string arguments contained in arrays of bytes, interpreted either as single-byte characters, or UTF-8 strings. You can also build two other libraries, called <code>libpcre2-16</code> and <code>libpcre2-32</code>, which process strings that are contained in arrays of 16-bit and 32-bit code units, respectively. These can be interpreted either as single-unit characters or UTF-16/UTF-32 strings. To build these additional libraries, add one or both of the following to the <code>configure</code> command: </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-pcre2-16<br />
&nbsp;<wbr>&nbsp;&#8211;enable-pcre2-32 </p>
<p> If you do not want the 8-bit library, add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-pcre2-8 </p>
<p> as well. At least one of the three libraries must be built. Note that the POSIX wrapper is for the 8-bit library only, and that <code>pcre2grep</code> is an 8-bit program. Neither of these are built if you select only the 16-bit or 32-bit libraries.</p>
<h2>Building Shared And Static Libraries</h2>
<p>The Autotools PCRE2 building process uses <code>libtool</code> to build both shared and static libraries by default. You can suppress an unwanted library by adding one of </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-shared<br />
&nbsp;<wbr>&nbsp;&#8211;disable-static </p>
<p> to the <code>configure</code> command.</p>
<h2>Unicode And Utf Support</h2>
<p>By default, PCRE2 is built with support for Unicode and UTF character strings. To build it without Unicode support, add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-unicode </p>
<p> to the <code>configure</code> command. This setting applies to all three libraries. It is not possible to build one library with Unicode support, and another without, in the same configuration. </p>
<p> Of itself, Unicode support does not make PCRE2 treat strings as UTF-8, UTF-16 or UTF-32. To do that, applications that use the library can set the PCRE2_UTF option when they call <code>pcre2_compile()</code> to compile a pattern. Alternatively, patterns may be started with (*UTF) unless the application has locked this out by setting PCRE2_NEVER_UTF. </p>
<p> UTF support allows the libraries to process character code points up to 0x10ffff in the strings that they handle. Unicode support also gives access to the Unicode properties of characters, using pattern escapes such as \P, \p, and \X. Only the general category properties such as <i>Lu</i> and <i>Nd</i> are supported. Details are given in the <code>pcre2pattern</code> documentation. </p>
<p> Pattern escapes such as \d and \w do not by default make use of Unicode properties. The application can request that they do by setting the PCRE2_UCP option. Unless the application has set PCRE2_NEVER_UCP, a pattern may also request this by starting with (*UCP).</p>
<h2>Disabling The Use Of \C</h2>
<p>The \C escape sequence, which matches a single code unit, even in a UTF mode, can cause unpredictable behaviour because it may leave the current matching point in the middle of a multi-code-unit character. The application can lock it out by setting the PCRE2_NEVER_BACKSLASH_C option when calling <code>pcre2_compile()</code>. There is also a build-time option </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-never-backslash-C </p>
<p> (note the upper case C) which locks out the use of \C entirely.</p>
<h2>Just-In-Time Compiler Support</h2>
<p>Just-in-time (JIT) compiler support is included in the build by specifying </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-jit </p>
<p> This support is available only for certain hardware architectures. If this option is set for an unsupported architecture, a building error occurs. If in doubt, use </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-jit=auto </p>
<p> which enables JIT only if the current hardware is supported. You can check if JIT is enabled in the configuration summary that is output at the end of a <code>configure</code> run. If you are enabling JIT under SELinux you may also want to add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-jit-sealloc </p>
<p> which enables the use of an execmem allocator in JIT that is compatible with SELinux. This has no effect if JIT is not enabled. See the <code>pcre2jit</code> documentation for a discussion of JIT usage. When JIT support is enabled, pcre2grep automatically makes use of it, unless you add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-pcre2grep-jit </p>
<p> to the &quot;configure&quot; command.</p>
<h2>Newline Recognition</h2>
<p>By default, PCRE2 interprets the linefeed (LF) character as indicating the end of a line. This is the normal newline character on Unix-like systems. You can compile PCRE2 to use carriage return (CR) instead, by adding </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-cr </p>
<p> to the <code>configure</code> command. There is also an &#8211;enable-newline-is-lf option, which explicitly specifies linefeed as the newline character. </p>
<p> Alternatively, you can specify that line endings are to be indicated by the two-character sequence CRLF (CR immediately followed by LF). If you want this, add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-crlf </p>
<p> to the <code>configure</code> command. There is a fourth option, specified by </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-anycrlf </p>
<p> which causes PCRE2 to recognize any of the three sequences CR, LF, or CRLF as indicating a line ending. A fifth option, specified by </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-any </p>
<p> causes PCRE2 to recognize any Unicode newline sequence. The Unicode newline sequences are the three just mentioned, plus the single characters VT (vertical tab, U+000B), FF (form feed, U+000C), NEL (next line, U+0085), LS (line separator, U+2028), and PS (paragraph separator, U+2029). The final option is </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-nul </p>
<p> which causes NUL (binary zero) to be set as the default line-ending character. </p>
<p> Whatever default line ending convention is selected when PCRE2 is built can be overridden by applications that use the library. At build time it is recommended to use the standard for your operating system.</p>
<h2>What \R Matches</h2>
<p>By default, the sequence \R in a pattern matches any Unicode newline sequence, independently of what has been selected as the line ending sequence. If you specify </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-bsr-anycrlf </p>
<p> the default is changed so that \R matches only CR, LF, or CRLF. Whatever is selected when PCRE2 is built can be overridden by applications that use the library.</p>
<h2>Handling Very Large Patterns</h2>
<p>Within a compiled pattern, offset values are used to point from one part to another (for example, from an opening parenthesis to an alternation metacharacter). By default, in the 8-bit and 16-bit libraries, two-byte values are used for these offsets, leading to a maximum size for a compiled pattern of around 64 thousand code units. This is sufficient to handle all but the most gigantic patterns. Nevertheless, some people do want to process truly enormous patterns, so it is possible to compile PCRE2 to use three-byte or four-byte offsets by adding a setting such as </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-link-size=3 </p>
<p> to the <code>configure</code> command. The value given must be 2, 3, or 4. For the 16-bit library, a value of 3 is rounded up to 4. In these libraries, using longer offsets slows down the operation of PCRE2 because it has to load additional data when handling them. For the 32-bit library the value is always 4 and cannot be overridden; the value of &#8211;with-link-size is ignored.</p>
<h2>Limiting Pcre2 Resource Usage</h2>
<p>The <code>pcre2_match()</code> function increments a counter each time it goes round its main loop. Putting a limit on this counter controls the amount of computing resource used by a single call to <code>pcre2_match()</code>. The limit can be changed at run time, as described in the <code>pcre2api</code> documentation. The default is 10 million, but this can be changed by adding a setting such as </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-match-limit=500000 </p>
<p> to the <code>configure</code> command. This setting also applies to the <code>pcre2_dfa_match()</code> matching function, and to JIT matching (though the counting is done differently). </p>
<p> The <code>pcre2_match()</code> function starts out using a 20KiB vector on the system stack to record backtracking points. The more nested backtracking points there are (that is, the deeper the search tree), the more memory is needed. If the initial vector is not large enough, heap memory is used, up to a certain limit, which is specified in kibibytes (units of 1024 bytes). The limit can be changed at run time, as described in the <code>pcre2api</code> documentation. The default limit (in effect unlimited) is 20 million. You can change this by a setting such as </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-heap-limit=500 </p>
<p> which limits the amount of heap to 500 KiB. This limit applies only to interpretive matching in <code>pcre2_match()</code> and <code>pcre2_dfa_match()</code>, which may also use the heap for internal workspace when processing complicated patterns. This limit does not apply when JIT (which has its own memory arrangements) is used. </p>
<p> You can also explicitly limit the depth of nested backtracking in the <code>pcre2_match()</code> interpreter. This limit defaults to the value that is set for &#8211;with-match-limit. You can set a lower default limit by adding, for example, </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-match-limit_depth=10000 </p>
<p> to the <code>configure</code> command. This value can be overridden at run time. This depth limit indirectly limits the amount of heap memory that is used, but because the size of each backtracking &quot;frame&quot; depends on the number of capturing parentheses in a pattern, the amount of heap that is used before the limit is reached varies from pattern to pattern. This limit was more useful in versions before 10.30, where function recursion was used for backtracking. </p>
<p> As well as applying to <code>pcre2_match()</code>, the depth limit also controls the depth of recursive function calls in <code>pcre2_dfa_match()</code>. These are used for lookaround assertions, atomic groups, and recursion within patterns. The limit does not apply to JIT matching.</p>
<h2>Creating Character Tables At Build Time</h2>
<p>PCRE2 uses fixed tables for processing characters whose code points are less than 256. By default, PCRE2 is built with a set of tables that are distributed in the file <i>src/pcre2_chartables.c.dist</i>. These tables are for ASCII codes only. If you add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-rebuild-chartables </p>
<p> to the <code>configure</code> command, the distributed tables are no longer used. Instead, a program called <code>dftables</code> is compiled and run. This outputs the source for new set of tables, created in the default locale of your C run-time system. This method of replacing the tables does not work if you are cross compiling, because <code>dftables</code> is run on the local host. If you need to create alternative tables when cross compiling, you will have to do so &quot;by hand&quot;.</p>
<h2>Using Ebcdic Code</h2>
<p>PCRE2 assumes by default that it will run in an environment where the character code is ASCII or Unicode, which is a superset of ASCII. This is the case for most computer operating systems. PCRE2 can, however, be compiled to run in an 8-bit EBCDIC environment by adding </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-ebcdic &#8211;disable-unicode </p>
<p> to the <code>configure</code> command. This setting implies &#8211;enable-rebuild-chartables. You should only use it if you know that you are in an EBCDIC environment (for example, an IBM mainframe operating system). </p>
<p> It is not possible to support both EBCDIC and UTF-8 codes in the same version of the library. Consequently, &#8211;enable-unicode and &#8211;enable-ebcdic are mutually exclusive. </p>
<p> The EBCDIC character that corresponds to an ASCII LF is assumed to have the value 0x15 by default. However, in some EBCDIC environments, 0x25 is used. In such an environment you should use </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-ebcdic-nl25 </p>
<p> as well as, or instead of, &#8211;enable-ebcdic. The EBCDIC character for CR has the same value as in ASCII, namely, 0x0d. Whichever of 0x15 and 0x25 is <i>not</i> chosen as LF is made to correspond to the Unicode NEL character (which, in Unicode, is 0x85). </p>
<p> The options that select newline behaviour, such as &#8211;enable-newline-is-cr, and equivalent run-time options, refer to these character values in an EBCDIC environment.</p>
<h2>Pcre2Grep Support For External Scripts</h2>
<p>By default <code>pcre2grep</code> supports the use of callouts with string arguments within the patterns it is matching. There are two kinds: one that generates output using local code, and another that calls an external program or script. If &#8211;disable-pcre2grep-callout-fork is added to the <code>configure</code> command, only the first kind of callout is supported; if &#8211;disable-pcre2grep-callout is used, all callouts are completely ignored. For more details of <code>pcre2grep</code> callouts, see the <code>pcre2grep</code> documentation.</p>
<h2>Pcre2Grep Options For Compressed File Support</h2>
<p>By default, <code>pcre2grep</code> reads all files as plain text. You can build it so that it recognizes files whose names end in <code>.gz</code> or <code>.bz2</code>, and reads them with <code>libz</code> or <code>libbz2</code>, respectively, by adding one or both of </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-pcre2grep-libz<br />
&nbsp;<wbr>&nbsp;&#8211;enable-pcre2grep-libbz2 </p>
<p> to the <code>configure</code> command. These options naturally require that the relevant libraries are installed on your system. Configuration will fail if they are not.</p>
<h2>Pcre2Grep Buffer Size</h2>
<p><code>pcre2grep</code> uses an internal buffer to hold a &quot;window&quot; on the file it is scanning, in order to be able to output &quot;before&quot; and &quot;after&quot; lines when it finds a match. The default starting size of the buffer is 20KiB. The buffer itself is three times this size, but because of the way it is used for holding &quot;before&quot; lines, the longest line that is guaranteed to be processable is the notional buffer size. If a longer line is encountered, <code>pcre2grep</code> automatically expands the buffer, up to a specified maximum size, whose default is 1MiB or the starting size, whichever is the larger. You can change the default parameter values by adding, for example, </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-pcre2grep-bufsize=51200<br />
&nbsp;<wbr>&nbsp;&#8211;with-pcre2grep-max-bufsize=2097152 </p>
<p> to the <code>configure</code> command. The caller of pcre2grep can override these values by using &#8211;buffer-size and &#8211;max-buffer-size on the command line.</p>
<h2>Pcre2Test Option For Libreadline Support</h2>
<p>If you add one of </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-pcre2test-libreadline<br />
&nbsp;<wbr>&nbsp;&#8211;enable-pcre2test-libedit </p>
<p> to the <code>configure</code> command, <code>pcre2test</code> is linked with the <code>libreadline</code> or<code>libedit</code> library, respectively, and when its input is from a terminal, it reads it using the <code>readline()</code> function. This provides line-editing and history facilities. Note that <code>libreadline</code> is GPL-licensed, so if you distribute a binary of <code>pcre2test</code> linked in this way, there may be licensing issues. These can be avoided by linking instead with <code>libedit</code>, which has a BSD licence. </p>
<p> Setting &#8211;enable-pcre2test-libreadline causes the <code>-lreadline</code> option to be added to the <code>pcre2test</code> build. In many operating environments with a sytem-installed readline library this is sufficient. However, in some environments (e.g. if an unmodified distribution version of readline is in use), some extra configuration may be necessary. The INSTALL file for <code>libreadline</code> says this: </p>
<p>&nbsp;<wbr>&nbsp;&quot;Readline uses the termcap functions, but does not link with<br />
&nbsp;<wbr>&nbsp;the termcap or curses library itself, allowing applications<br />
&nbsp;<wbr>&nbsp;which link with readline the to choose an appropriate library.&quot; </p>
<p> If your environment has not been set up so that an appropriate library is automatically included, you may need to add something like </p>
<p>&nbsp;<wbr>&nbsp;LIBS=&quot;-ncurses&quot; </p>
<p> immediately before the <code>configure</code> command.</p>
<h2>Including Debugging Code</h2>
<p>If you add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-debug </p>
<p> to the <code>configure</code> command, additional debugging code is included in the build. This feature is intended for use by the PCRE2 maintainers.</p>
<h2>Debugging With Valgrind Support</h2>
<p>If you add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-valgrind </p>
<p> to the <code>configure</code> command, PCRE2 will use valgrind annotations to mark certain memory regions as unaddressable. This allows it to detect invalid memory accesses, and is mostly useful for debugging PCRE2 itself.</p>
<h2>Code Coverage Reporting</h2>
<p>If your C compiler is gcc, you can build a version of PCRE2 that can generate a code coverage report for its test suite. To enable this, you must install <code>lcov</code> version 1.6 or above. Then specify </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-coverage </p>
<p> to the <code>configure</code> command and build PCRE2 in the usual way. </p>
<p> Note that using <code>ccache</code> (a caching C compiler) is incompatible with code coverage reporting. If you have configured <code>ccache</code> to run automatically on your system, you must set the environment variable </p>
<p>&nbsp;<wbr>&nbsp;CCACHE_DISABLE=1 </p>
<p> before running <code>make</code> to build PCRE2, so that <code>ccache</code> is not used. </p>
<p> When &#8211;enable-coverage is used, the following addition targets are added to the <i>Makefile</i>: </p>
<p>&nbsp;<wbr>&nbsp;make coverage </p>
<p> This creates a fresh coverage report for the PCRE2 test suite. It is equivalent to running &quot;make coverage-reset&quot;, &quot;make coverage-baseline&quot;, &quot;make check&quot;, and then &quot;make coverage-report&quot;. </p>
<p>&nbsp;<wbr>&nbsp;make coverage-reset </p>
<p> This zeroes the coverage counters, but does nothing else. </p>
<p>&nbsp;<wbr>&nbsp;make coverage-baseline </p>
<p> This captures baseline coverage information. </p>
<p>&nbsp;<wbr>&nbsp;make coverage-report </p>
<p> This creates the coverage report. </p>
<p>&nbsp;<wbr>&nbsp;make coverage-clean-report </p>
<p> This removes the generated coverage report without cleaning the coverage data itself. </p>
<p>&nbsp;<wbr>&nbsp;make coverage-clean-data </p>
<p> This removes the captured coverage data without removing the coverage files created at compile time (*.gcno). </p>
<p>&nbsp;<wbr>&nbsp;make coverage-clean </p>
<p> This cleans all coverage data including the generated coverage report. For more information about code coverage, see the <code>gcov</code> and <code>lcov</code> documentation.</p>
<h2>Disabling The Z And T Formatting Modifiers</h2>
<p>The C99 standard defines formatting modifiers z and t for size_t and ptrdiff_t values, respectively. By default, PCRE2 uses these modifiers in environments other than Microsoft Visual Studio when __STDC_VERSION__ is defined and has a value greater than or equal to 199901L (indicating C99). However, there is at least one environment that claims to be C99 but does not support these modifiers. If </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-percent-zt </p>
<p> is specified, no use is made of the z or t modifiers. Instead or %td or %zu, %lu is used, with a cast for size_t values.</p>
<h2>Support For Fuzzers</h2>
<p>There is a special option for use by people who want to run fuzzing tests on PCRE2: </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-fuzz-support </p>
<p> At present this applies only to the 8-bit library. If set, it causes an extra library called libpcre2-fuzzsupport.a to be built, but not installed. This contains a single function called LLVMFuzzerTestOneInput() whose arguments are a pointer to a string and the length of the string. When called, this function tries to compile the string as a pattern, and if that succeeds, to match it. This is done both with no options and with some random options bits that are generated from the string. </p>
<p> Setting &#8211;enable-fuzz-support also causes a binary called <code>pcre2fuzzcheck</code> to be created. This is normally run under valgrind or used when PCRE2 is compiled with address sanitizing enabled. It calls the fuzzing function and outputs information about what it is doing. The input strings are specified by arguments: if an argument starts with &quot;=&quot; the rest of it is a literal input string. Otherwise, it is assumed to be a file name, and the contents of the file are the test string.</p>
<h2>Obsolete Option</h2>
<p>In versions of PCRE2 prior to 10.30, there were two ways of handling backtracking in the <code>pcre2_match()</code> function. The default was to use the system stack, but if </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-stack-for-recursion </p>
<p> was set, memory on the heap was used. From release 10.30 onwards this has changed (the stack is no longer used) and this option now does nothing except give a warning.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pcre2api/">pcre2api</a></code>(3), <code><a href="/docs/linux/man/3-pcre2-config/">pcre2-config</a></code>(3).</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 03 March 2019
Copyright (c) 1997-2019 University of Cambridge.</pre>
