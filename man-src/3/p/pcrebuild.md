---
title: "pcrebuild(3)"
name: "pcrebuild"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcrebuild/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Building Pcre</h2>
<p>PCRE is distributed with a <code>configure</code> script that can be used to build the library in Unix-like environments using the applications known as Autotools. Also in the distribution are files to support building using <code>CMake</code> instead of <code>configure</code>. The text file <code>README</code> contains general information about building with Autotools (some of which is repeated below), and also has some comments about building on various operating systems. There is a lot more information about building PCRE without using Autotools (including information about using <code>CMake</code> and building &quot;by hand&quot;) in the text file called <code>NON-AUTOTOOLS-BUILD</code>. You should consult this file as well as the <code>README</code> file if you are building in a non-Unix-like environment.</p>
<h2>Pcre Build-Time Options</h2>
<p>The rest of this document describes the optional features of PCRE that can be selected when the library is compiled. It assumes use of the <code>configure</code> script, where the optional features are selected or deselected by providing options to <code>configure</code> before running the <code>make</code> command. However, the same options can be selected in both Unix-like and non-Unix-like environments using the GUI facility of <code>cmake-gui</code> if you are using <code>CMake</code> instead of <code>configure</code> to build PCRE. </p>
<p> If you are not using Autotools or <code>CMake</code>, option selection can be done by editing the <code>config.h</code> file, or by passing parameter settings to the compiler, as described in <code>NON-AUTOTOOLS-BUILD</code>. </p>
<p> The complete list of options for <code>configure</code> (which includes the standard ones such as the selection of the installation directory) can be obtained by running </p>
<p>&nbsp;<wbr>&nbsp;./configure &#8211;help </p>
<p> The following sections include descriptions of options whose names begin with &#8211;enable or &#8211;disable. These settings specify changes to the defaults for the <code>configure</code> command. Because of the way that <code>configure</code> works, &#8211;enable and &#8211;disable always come in pairs, so the complementary option always exists as well, but as it specifies the default, it is not described.</p>
<h2>Building 8-Bit, 16-Bit And 32-Bit Libraries</h2>
<p>By default, a library called <code>libpcre</code> is built, containing functions that take string arguments contained in vectors of bytes, either as single-byte characters, or interpreted as UTF-8 strings. You can also build a separate library, called <code>libpcre16</code>, in which strings are contained in vectors of 16-bit data units and interpreted either as single-unit characters or UTF-16 strings, by adding </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-pcre16 </p>
<p> to the <code>configure</code> command. You can also build yet another separate library, called <code>libpcre32</code>, in which strings are contained in vectors of 32-bit data units and interpreted either as single-unit characters or UTF-32 strings, by adding </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-pcre32 </p>
<p> to the <code>configure</code> command. If you do not want the 8-bit library, add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-pcre8 </p>
<p> as well. At least one of the three libraries must be built. Note that the C++ and POSIX wrappers are for the 8-bit library only, and that <code>pcregrep</code> is an 8-bit program. None of these are built if you select only the 16-bit or 32-bit libraries.</p>
<h2>Building Shared And Static Libraries</h2>
<p>The Autotools PCRE building process uses <code>libtool</code> to build both shared and static libraries by default. You can suppress one of these by adding one of </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-shared<br />
&nbsp;<wbr>&nbsp;&#8211;disable-static </p>
<p> to the <code>configure</code> command, as required.</p>
<h2>C++ Support</h2>
<p>By default, if the 8-bit library is being built, the <code>configure</code> script will search for a C++ compiler and C++ header files. If it finds them, it automatically builds the C++ wrapper library (which supports only 8-bit strings). You can disable this by adding </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-cpp </p>
<p> to the <code>configure</code> command.</p>
<h2>Utf-8, Utf-16 And Utf-32 Support</h2>
<p>To build PCRE with support for UTF Unicode character strings, add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-utf </p>
<p> to the <code>configure</code> command. This setting applies to all three libraries, adding support for UTF-8 to the 8-bit library, support for UTF-16 to the 16-bit library, and support for UTF-32 to the to the 32-bit library. There are no separate options for enabling UTF-8, UTF-16 and UTF-32 independently because that would allow ridiculous settings such as requesting UTF-16 support while building only the 8-bit library. It is not possible to build one library with UTF support and another without in the same configuration. (For backwards compatibility, &#8211;enable-utf8 is a synonym of &#8211;enable-utf.) </p>
<p> Of itself, this setting does not make PCRE treat strings as UTF-8, UTF-16 or UTF-32. As well as compiling PCRE with this option, you also have have to set the PCRE_UTF8, PCRE_UTF16 or PCRE_UTF32 option (as appropriate) when you call one of the pattern compiling functions. </p>
<p> If you set &#8211;enable-utf when compiling in an EBCDIC environment, PCRE expects its input to be either ASCII or UTF-8 (depending on the run-time option). It is not possible to support both EBCDIC and UTF-8 codes in the same version of the library. Consequently, &#8211;enable-utf and &#8211;enable-ebcdic are mutually exclusive.</p>
<h2>Unicode Character Property Support</h2>
<p>UTF support allows the libraries to process character codepoints up to 0x10ffff in the strings that they handle. On its own, however, it does not provide any facilities for accessing the properties of such characters. If you want to be able to use the pattern escapes \P, \p, and \X, which refer to Unicode character properties, you must add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-unicode-properties </p>
<p> to the <code>configure</code> command. This implies UTF support, even if you have not explicitly requested it. </p>
<p> Including Unicode property support adds around 30K of tables to the PCRE library. Only the general category properties such as <i>Lu</i> and <i>Nd</i> are supported. Details are given in the <code>pcrepattern</code> documentation.</p>
<h2>Just-In-Time Compiler Support</h2>
<p>Just-in-time compiler support is included in the build by specifying </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-jit </p>
<p> This support is available only for certain hardware architectures. If this option is set for an unsupported architecture, a compile time error occurs. See the <code>pcrejit</code> documentation for a discussion of JIT usage. When JIT support is enabled, pcregrep automatically makes use of it, unless you add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-pcregrep-jit </p>
<p> to the &quot;configure&quot; command.</p>
<h2>Code Value Of Newline</h2>
<p>By default, PCRE interprets the linefeed (LF) character as indicating the end of a line. This is the normal newline character on Unix-like systems. You can compile PCRE to use carriage return (CR) instead, by adding </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-cr </p>
<p> to the <code>configure</code> command. There is also a &#8211;enable-newline-is-lf option, which explicitly specifies linefeed as the newline character. </p>
<p> Alternatively, you can specify that line endings are to be indicated by the two character sequence CRLF. If you want this, add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-crlf </p>
<p> to the <code>configure</code> command. There is a fourth option, specified by </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-anycrlf </p>
<p> which causes PCRE to recognize any of the three sequences CR, LF, or CRLF as indicating a line ending. Finally, a fifth option, specified by </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-newline-is-any </p>
<p> causes PCRE to recognize any Unicode newline sequence. </p>
<p> Whatever line ending convention is selected when PCRE is built can be overridden when the library functions are called. At build time it is conventional to use the standard for your operating system.</p>
<h2>What \R Matches</h2>
<p>By default, the sequence \R in a pattern matches any Unicode newline sequence, whatever has been selected as the line ending sequence. If you specify </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-bsr-anycrlf </p>
<p> the default is changed so that \R matches only CR, LF, or CRLF. Whatever is selected when PCRE is built can be overridden when the library functions are called.</p>
<h2>Posix Malloc Usage</h2>
<p>When the 8-bit library is called through the POSIX interface (see the <code>pcreposix</code> documentation), additional working storage is required for holding the pointers to capturing substrings, because PCRE requires three integers per substring, whereas the POSIX interface provides only two. If the number of expected substrings is small, the wrapper function uses space on the stack, because this is faster than using <code>malloc()</code> for each call. The default threshold above which the stack is no longer used is 10; it can be changed by adding a setting such as </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-posix-malloc-threshold=20 </p>
<p> to the <code>configure</code> command.</p>
<h2>Handling Very Large Patterns</h2>
<p>Within a compiled pattern, offset values are used to point from one part to another (for example, from an opening parenthesis to an alternation metacharacter). By default, in the 8-bit and 16-bit libraries, two-byte values are used for these offsets, leading to a maximum size for a compiled pattern of around 64K. This is sufficient to handle all but the most gigantic patterns. Nevertheless, some people do want to process truly enormous patterns, so it is possible to compile PCRE to use three-byte or four-byte offsets by adding a setting such as </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-link-size=3 </p>
<p> to the <code>configure</code> command. The value given must be 2, 3, or 4. For the 16-bit library, a value of 3 is rounded up to 4. In these libraries, using longer offsets slows down the operation of PCRE because it has to load additional data when handling them. For the 32-bit library the value is always 4 and cannot be overridden; the value of &#8211;with-link-size is ignored.</p>
<h2>Avoiding Excessive Stack Usage</h2>
<p>When matching with the <code>pcre_exec()</code> function, PCRE implements backtracking by making recursive calls to an internal function called <code>match()</code>. In environments where the size of the stack is limited, this can severely limit PCRE&#8217;s operation. (The Unix environment does not usually suffer from this problem, but it may sometimes be necessary to increase the maximum stack size. There is a discussion in the <code>pcrestack</code> documentation.) An alternative approach to recursion that uses memory from the heap to remember data, instead of using recursive function calls, has been implemented to work round the problem of limited stack size. If you want to build a version of PCRE that works this way, add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;disable-stack-for-recursion </p>
<p> to the <code>configure</code> command. With this configuration, PCRE will use the <code>pcre_stack_malloc</code> and <code>pcre_stack_free</code> variables to call memory management functions. By default these point to <code>malloc()</code> and <code>free()</code>, but you can replace the pointers so that your own functions are used instead. </p>
<p> Separate functions are provided rather than using <code>pcre_malloc</code> and <code>pcre_free</code> because the usage is very predictable: the block sizes requested are always the same, and the blocks are always freed in reverse order. A calling program might be able to implement optimized functions that perform better than <code>malloc()</code> and <code>free()</code>. PCRE runs noticeably more slowly when built in this way. This option affects only the <code>pcre_exec()</code> function; it is not relevant for <code>pcre_dfa_exec()</code>.</p>
<h2>Limiting Pcre Resource Usage</h2>
<p>Internally, PCRE has a function called <code>match()</code>, which it calls repeatedly (sometimes recursively) when matching a pattern with the <code>pcre_exec()</code> function. By controlling the maximum number of times this function may be called during a single matching operation, a limit can be placed on the resources used by a single call to <code>pcre_exec()</code>. The limit can be changed at run time, as described in the <code>pcreapi</code> documentation. The default is 10 million, but this can be changed by adding a setting such as </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-match-limit=500000 </p>
<p> to the <code>configure</code> command. This setting has no effect on the <code>pcre_dfa_exec()</code> matching function. </p>
<p> In some environments it is desirable to limit the depth of recursive calls of <code>match()</code> more strictly than the total number of calls, in order to restrict the maximum amount of stack (or heap, if &#8211;disable-stack-for-recursion is specified) that is used. A second limit controls this; it defaults to the value that is set for &#8211;with-match-limit, which imposes no additional constraints. However, you can set a lower limit by adding, for example, </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-match-limit-recursion=10000 </p>
<p> to the <code>configure</code> command. This value can also be overridden at run time.</p>
<h2>Creating Character Tables At Build Time</h2>
<p>PCRE uses fixed tables for processing characters whose code values are less than 256. By default, PCRE is built with a set of tables that are distributed in the file <i>pcre_chartables.c.dist</i>. These tables are for ASCII codes only. If you add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-rebuild-chartables </p>
<p> to the <code>configure</code> command, the distributed tables are no longer used. Instead, a program called <code>dftables</code> is compiled and run. This outputs the source for new set of tables, created in the default locale of your C run-time system. (This method of replacing the tables does not work if you are cross compiling, because <code>dftables</code> is run on the local host. If you need to create alternative tables when cross compiling, you will have to do so &quot;by hand&quot;.)</p>
<h2>Using Ebcdic Code</h2>
<p>PCRE assumes by default that it will run in an environment where the character code is ASCII (or Unicode, which is a superset of ASCII). This is the case for most computer operating systems. PCRE can, however, be compiled to run in an EBCDIC environment by adding </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-ebcdic </p>
<p> to the <code>configure</code> command. This setting implies &#8211;enable-rebuild-chartables. You should only use it if you know that you are in an EBCDIC environment (for example, an IBM mainframe operating system). The &#8211;enable-ebcdic option is incompatible with &#8211;enable-utf. </p>
<p> The EBCDIC character that corresponds to an ASCII LF is assumed to have the value 0x15 by default. However, in some EBCDIC environments, 0x25 is used. In such an environment you should use </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-ebcdic-nl25 </p>
<p> as well as, or instead of, &#8211;enable-ebcdic. The EBCDIC character for CR has the same value as in ASCII, namely, 0x0d. Whichever of 0x15 and 0x25 is <i>not</i> chosen as LF is made to correspond to the Unicode NEL character (which, in Unicode, is 0x85). </p>
<p> The options that select newline behaviour, such as &#8211;enable-newline-is-cr, and equivalent run-time options, refer to these character values in an EBCDIC environment.</p>
<h2>Pcregrep Options For Compressed File Support</h2>
<p>By default, <code>pcregrep</code> reads all files as plain text. You can build it so that it recognizes files whose names end in <code>.gz</code> or <code>.bz2</code>, and reads them with <code>libz</code> or <code>libbz2</code>, respectively, by adding one or both of </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-pcregrep-libz<br />
&nbsp;<wbr>&nbsp;&#8211;enable-pcregrep-libbz2 </p>
<p> to the <code>configure</code> command. These options naturally require that the relevant libraries are installed on your system. Configuration will fail if they are not.</p>
<h2>Pcregrep Buffer Size</h2>
<p><code>pcregrep</code> uses an internal buffer to hold a &quot;window&quot; on the file it is scanning, in order to be able to output &quot;before&quot; and &quot;after&quot; lines when it finds a match. The size of the buffer is controlled by a parameter whose default value is 20K. The buffer itself is three times this size, but because of the way it is used for holding &quot;before&quot; lines, the longest line that is guaranteed to be processable is the parameter size. You can change the default parameter value by adding, for example, </p>
<p>&nbsp;<wbr>&nbsp;&#8211;with-pcregrep-bufsize=50K </p>
<p> to the <code>configure</code> command. The caller of pcregrep can, however, override this value by specifying a run-time option.</p>
<h2>Pcretest Option For Libreadline Support</h2>
<p>If you add </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-pcretest-libreadline </p>
<p> to the <code>configure</code> command, <code>pcretest</code> is linked with the <code>libreadline</code> library, and when its input is from a terminal, it reads it using the <code>readline()</code> function. This provides line-editing and history facilities. Note that <code>libreadline</code> is GPL-licensed, so if you distribute a binary of <code>pcretest</code> linked in this way, there may be licensing issues. </p>
<p> Setting this option causes the <code>-lreadline</code> option to be added to the <code>pcretest</code> build. In many operating environments with a sytem-installed <code>libreadline</code> this is sufficient. However, in some environments (e.g. if an unmodified distribution version of readline is in use), some extra configuration may be necessary. The INSTALL file for <code>libreadline</code> says this: </p>
<p>&nbsp;<wbr>&nbsp;&quot;Readline uses the termcap functions, but does not link with the<br />
&nbsp;<wbr>&nbsp;termcap or curses library itself, allowing applications which link<br />
&nbsp;<wbr>&nbsp;with readline the to choose an appropriate library.&quot; </p>
<p> If your environment has not been set up so that an appropriate library is automatically included, you may need to add something like </p>
<p>&nbsp;<wbr>&nbsp;LIBS=&quot;-ncurses&quot; </p>
<p> immediately before the <code>configure</code> command.</p>
<h2>Debugging With Valgrind Support</h2>
<p>By adding the </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-valgrind </p>
<p> option to to the <code>configure</code> command, PCRE will use valgrind annotations to mark certain memory regions as unaddressable. This allows it to detect invalid memory accesses, and is mostly useful for debugging PCRE itself.</p>
<h2>Code Coverage Reporting</h2>
<p>If your C compiler is gcc, you can build a version of PCRE that can generate a code coverage report for its test suite. To enable this, you must install <code>lcov</code> version 1.6 or above. Then specify </p>
<p>&nbsp;<wbr>&nbsp;&#8211;enable-coverage </p>
<p> to the <code>configure</code> command and build PCRE in the usual way. </p>
<p> Note that using <code>ccache</code> (a caching C compiler) is incompatible with code coverage reporting. If you have configured <code>ccache</code> to run automatically on your system, you must set the environment variable </p>
<p>&nbsp;<wbr>&nbsp;CCACHE_DISABLE=1 </p>
<p> before running <code>make</code> to build PCRE, so that <code>ccache</code> is not used. </p>
<p> When &#8211;enable-coverage is used, the following addition targets are added to the <i>Makefile</i>: </p>
<p>&nbsp;<wbr>&nbsp;make coverage </p>
<p> This creates a fresh coverage report for the PCRE test suite. It is equivalent to running &quot;make coverage-reset&quot;, &quot;make coverage-baseline&quot;, &quot;make check&quot;, and then &quot;make coverage-report&quot;. </p>
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
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pcreapi/">pcreapi</a></code>(3), <code>pcre16</code>, <code>pcre32</code>, <code><a href="/docs/linux/man/3-pcre_config/">pcre_config</a></code>(3).</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 12 May 2013
Copyright (c) 1997-2013 University of Cambridge.</pre>
