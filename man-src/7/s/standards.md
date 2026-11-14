---
title: "standards(7)"
name: "standards"
section: "7"
letter: "s"
url: "/docs/linux/man/7-standards/"
description: "standards – C and UNIX Standards"
---

<p>standards &#8211; C and UNIX Standards</p>
<h2>Description</h2>
<p>The CONFORMING TO section that appears in many manual pages identifies various standards to which the documented interface conforms. The following list briefly describes these standards.</p>
<dl>
<dt><code>V7</code></p>
<dd>Version 7 (also known as Seventh Edition) UNIX, released by AT&amp;T/Bell Labs in 1979. After this point, UNIX systems diverged into two main dialects: BSD and System V.</p>
<dt><code>4.2BSD</code></p>
<dd>This is an implementation standard defined by the 4.2 release of the <i>Berkeley Software Distribution,</i> released by the University of California at Berkeley. This was the first Berkeley release that contained a TCP/IP stack and the sockets API. 4.2BSD was released in 1983.</p>
<dd>Earlier major BSD releases included <i>3BSD</i> (1980), <i>4BSD</i> (1980), and <i>4.1BSD</i> (1981).</p>
<dt><code>4.3BSD</code></p>
<dd>The successor to 4.2BSD, released in 1986.</p>
<dt><code>4.4BSD</code></p>
<dd>The successor to 4.3BSD, released in 1993. This was the last major Berkeley release.</p>
<dt><code>System V</code></p>
<dd>This is an implementation standard defined by AT&amp;T&#8217;s milestone 1983 release of its commercial System V (five) release. The previous major AT&amp;T release was <i>System III</i>, released in 1981.</p>
<dt><code>System V release 2 (SVr2)</code></p>
<dd>This was the next System V release, made in 1985. The SVr2 was formally described in the <i>System V Interface Definition version 1</i> (<i>SVID 1</i>) published in 1985.</p>
<dt><code>System V release 3 (SVr3)</code></p>
<dd>This was the successor to SVr2, released in 1986. This release was formally described in the <i>System V Interface Definition version 2</i> (<i>SVID 2</i>).</p>
<dt><code>System V release 4 (SVr4)</code></p>
<dd>This was the successor to SVr3, released in 1989. This version of System V is described in the &quot;Programmer&#8217;s Reference Manual: Operating System API (Intel processors)&quot; (Prentice-Hall 1992, ISBN 0-13-951294-2) This release was formally described in the <i>System V Interface Definition version 3</i> (<i>SVID 3</i>), and is considered the definitive System V release.</p>
<dt><code>SVID 4</code></p>
<dd>System V Interface Definition version 4, issued in 1995. Available online at</p>
<dt><code>C89</code></p>
<dd>This was the first C language standard, ratified by ANSI (American National Standards Institute) in 1989 (<i>X3.159-1989</i>). Sometimes this is known as <i>ANSI C</i>, but since C99 is also an ANSI standard, this term is ambiguous. This standard was also ratified by ISO (International Standards Organization) in 1990 (<i>ISO/IEC 9899:1990</i>), and is thus occasionally referred to as <i>ISO C90</i>.</p>
<dt><code>C99</code></p>
<dd>This revision of the C language standard was ratified by ISO in 1999 (<i>ISO/IEC 9899:1999</i>). Available online at</p>
<dt><code>C11</code></p>
<dd>This revision of the C language standard was ratified by ISO in 2011 (<i>ISO/IEC 9899:2011</i>).</p>
<dd><code>LFS</code> The Large File Summit specification, completed in 1996. This specification defined mechanisms that allowed 32-bit systems to support the use of large files (i.e., 64-bit file offsets). See</p>
<dt><code>POSIX.1-1988</code></p>
<dd>This was the first POSIX standard, ratified by IEEE as IEEE Std 1003.1-1988, and subsequently adopted (with minor revisions) as an ISO standard in 1990. The term &quot;POSIX&quot; was coined by Richard Stallman.</p>
<dt><code>POSIX.1-1990</code></p>
<dd>&quot;Portable Operating System Interface for Computing Environments&quot;. IEEE 1003.1-1990 part 1, ratified by ISO in 1990 (<i>ISO/IEC 9945-1:1990</i>).</p>
<dt><code>POSIX.2</code></p>
<dd>IEEE Std 1003.2-1992, describing commands and utilities, ratified by ISO in 1993 (<i>ISO/IEC 9945-2:1993</i>).</p>
<dt><code>POSIX.1b</code> (formerly known as <i>POSIX.4</i>)</p>
<dd>IEEE Std 1003.1b-1993, describing real-time facilities for portable operating systems, ratified by ISO in 1996 (<i>ISO/IEC 9945-1:1996</i>).</p>
<dt><code>POSIX.1c (formerly known as </code><i>POSIX.4a</i>)</p>
<dd>IEEE Std 1003.1c-1995, which describes the POSIX threads interfaces.</p>
<dt><code>POSIX.1d</code></p>
<dd>IEEE Std 1003.1c-1999, which describes additional real-time extensions.</p>
<dt><code>POSIX.1g</code></p>
<dd>IEEE Std 1003.1g-2000, which describes networking APIs (including sockets).</p>
<dt><code>POSIX.1j</code></p>
<dd>IEEE Std 1003.1j-2000, which describes advanced real-time extensions.</p>
<dt><code>POSIX.1-1996</code></p>
<dd>A 1996 revision of POSIX.1 which incorporated POSIX.1b and POSIX.1c.</p>
<dt><code>XPG3</code></p>
<dd>Released in 1989, this was the first release of the X/Open Portability Guide to be based on a POSIX standard (POSIX.1-1988). This multivolume guide was developed by the X/Open Group, a multivendor consortium.</p>
<dt><code>XPG4</code></p>
<dd>A revision of the X/Open Portability Guide, released in 1992. This revision incorporated POSIX.2.</p>
<dt><code>XPG4v2</code></p>
<dd>A 1994 revision of XPG4. This is also referred to as <i>Spec 1170</i>, where 1170 referred to the number of interfaces defined by this standard.</p>
<dt><code>SUS (SUSv1)</code></p>
<dd>Single UNIX Specification. This was a repackaging of XPG4v2 and other X/Open standards (X/Open Curses Issue 4 version 2, X/Open Networking Service (XNS) Issue 4). Systems conforming to this standard can be branded <i>UNIX 95</i>.</p>
<dt><code>SUSv2</code></p>
<dd>Single UNIX Specification version 2. Sometimes also referred to (incorrectly) as <i>XPG5</i>. This standard appeared in 1997. Systems conforming to this standard can be branded <i>UNIX 98</i>. See also</p>
<dt><code>POSIX.1-2001, SUSv3</code></p>
<dd>This was a 2001 revision and consolidation of the POSIX.1, POSIX.2, and SUS standards into a single document, conducted under the auspices of the Austin Group The standard is available online at</p>
<dd>The standard defines two levels of conformance: <i>POSIX conformance</i>, which is a baseline set of interfaces required of a conforming system; and <i>XSI Conformance,</i> which additionally mandates a set of interfaces (the &quot;XSI extension&quot;) which are only optional for POSIX conformance. XSI-conformant systems can be branded <i>UNIX 03</i>.</p>
<dd>The POSIX.1-2001 document is broken into four parts:</p>
<dd><code>XBD</code>: Definitions, terms and concepts, header file specifications.</p>
<dd><code>XSH</code>: Specifications of functions (i.e., system calls and library functions in actual implementations).</p>
<dd><code>XCU</code>: Specifications of commands and utilities (i.e., the area formerly described by POSIX.2).</p>
<dd><code>XRAT</code>: Informative text on the other parts of the standard.</p>
<dd>POSIX.1-2001 is aligned with C99, so that all of the library functions standardized in C99 are also standardized in POSIX.1-2001.</p>
<dd>The Single UNIX Specification version 3 (SUSv3) comprises the Base Specifications containing XBD, XSH, XCU, and XRAT as above, plus X/Open Curses Issue 4 version 2 as an extra volume that is not in POSIX.1-2001.</p>
<dd>Two Technical Corrigenda (minor fixes and improvements) of the original 2001 standard have occurred: TC1 in 2003 and TC2 in 2004.</p>
<dt><code>POSIX.1-2008, SUSv4</code></p>
<dd>Work on the next revision of POSIX.1/SUS was completed and ratified in 2008. The standard is available online at</p>
<dd>The changes in this revision are not as large as those that occurred for POSIX.1-2001/SUSv3, but a number of new interfaces are added and various details of existing specifications are modified. Many of the interfaces that were optional in POSIX.1-2001 become mandatory in the 2008 revision of the standard. A few interfaces that are present in POSIX.1-2001 are marked as obsolete in POSIX.1-2008, or removed from the standard altogether.</p>
<dd>The revised standard is structured in the same way as its predecessor. The Single UNIX Specification version 4 (SUSv4) comprises the Base Specifications containing XBD, XSH, XCU, and XRAT, plus X/Open Curses Issue 7 as an extra volume that is not in POSIX.1-2008.</p>
<dd>Again there are two levels of conformance: the baseline <i>POSIX Conformance</i>, and <i>XSI Conformance</i>, which mandates an additional set of interfaces beyond those in the base specification.</p>
<dd>In general, where the CONFORMING TO section of a manual page lists POSIX.1-2001, it can be assumed that the interface also conforms to POSIX.1-2008, unless otherwise noted.</p>
<dd>Technical Corrigendum 1 (minor fixes and improvements) of this standard was released in 2013.</p>
<dd>Technical Corrigendum 2 of this standard was released in 2016.</p>
<dd>Further information can be found on the Austin Group web site,</p>
<dt><code>SUSv4 2016 edition</code></p>
<dd>This is equivalent to POSIX.1-2008, with the addition of Technical Corrigenda 1 and 2 and the XCurses specification.</p>
<dt><code>POSIX.1-2017</code></p>
<dd>This revision of POSIX is technically identical to POSIX.1-2008 with Technical Corrigenda 1 and 2 applied.</p>
<dt><code>SUSv4 2018 edition</code></p>
<dd>This is equivalent to POSIX.1-2017, with the addition of the XCurses specification.</dl>
<p> The interfaces documented in POSIX.1/SUS are available as manual pages under sections 0p (header files), 1p (commands), and 3p (functions); thus one can write &quot;man 3p open&quot;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-getconf/">getconf</a></code>(1), <code><a href="/docs/linux/man/3-confstr/">confstr</a></code>(3), <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7), <code><a href="/docs/linux/man/7-libc/">libc</a></code>(7), <code><a href="/docs/linux/man/7-posixoptions/">posixoptions</a></code>(7), <code><a href="/docs/linux/man/7-system_data_types/">system_data_types</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
