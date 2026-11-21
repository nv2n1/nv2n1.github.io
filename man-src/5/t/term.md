---
title: "term(5)"
name: "term"
section: "5"
letter: "t"
url: "/docs/linux/man/5-term/"
description: "term – format of compiled term file."
---

<p>term &#8211; format of compiled term file.</p>
<h2>Synopsis</h2>
<p><code>term</code></p>
<h2>Description</h2>
<h3>Storage Location</h3>
<p>Compiled terminfo descriptions are placed under the directory <code>/etc/terminfo</code>. Two configurations are supported (when building the <code>ncurses</code> libraries):</p>
<dl>
<dt><code>directory tree</code></dt>
<dd>A two-level scheme is used to avoid a linear search of a huge <font SIZE="-1">UNIX</font> system directory: <code>/etc/terminfo/c/name</code> where <i>name</i> is the name of the terminal, and <i>c</i> is the first character of <i>name</i>. Thus, <i>act4</i> can be found in the file <code>/etc/terminfo/a/act4</code>. Synonyms for the same terminal are implemented by multiple links to the same compiled file.</dd>
<dt><code>hashed database</code></dt>
<dd>Using Berkeley database, two types of records are stored: the terminfo data in the same format as stored in a directory tree with the terminfo&#8217;s primary name as a key, and records containing only aliases pointing to the primary name.</dd>
<dd>If built to write hashed databases, <code>ncurses</code> can still read terminfo databases organized as a directory tree, but cannot write entries into the directory tree. It can write (or rewrite) entries in the hashed database.</dd>
<dd><code>ncurses</code> distinguishes the two cases in the TERMINFO and TERMINFO_DIRS environment variable by assuming a directory tree for entries that correspond to an existing directory, and hashed database otherwise.</dd></dl>
<h3>Legacy Storage Format</h3>
<p>The format has been chosen so that it will be the same on all hardware. An 8 or more bit byte is assumed, but no assumptions about byte ordering or sign extension are made. </p>
<p> The compiled file is created with the <code>tic</code> program, and read by the routine <code>setupterm</code>(3X). The file is divided into six parts:</p>
<dl>
<dd>
</dd><dl>
<dt>a) <i>header</i>,</dt>
<dd>
</dd><dt>b) <i>terminal names</i>,</dt>
<dd>
</dd><dt>c) <i>boolean flags</i>,</dt>
<dd>
</dd><dt>d) <i>numbers</i>,</dt>
<dd>
</dd><dt>e) <i>strings</i>, and</dt>
<dd>
</dd><dt>f) <i>string table</i>.</dt>
<dd></dd></dl>
</dl>
<p> The <i>header</i> section begins the file. This section contains six short integers in the format described below. These integers are</p>
<dl>
<dd>
</dd><dl>
<dt>(1) the <i>magic number</i> (octal 0432);</dt>
<dd>
</dd><dt>(2) the size, in bytes, of the <i>terminal names</i> section;</dt>
<dd>
</dd><dt>(3) the number of bytes in the <i>boolean flags</i> section;</dt>
<dd>
</dd><dt>(4) the number of short integers in the <i>numbers</i> section;</dt>
<dd>
</dd><dt>(5) the number of offsets (short integers) in the <i>strings</i> section;</dt>
<dd>
</dd><dt>(6) the size, in bytes, of the <i>string table</i>.</dt>
<dd></dd></dl>
</dl>
<p> The capabilities in the <i>boolean flags</i>, <i>numbers</i>, and <i>strings</i> sections are in the same order as the file &lt;term.h&gt;. </p>
<p> Short integers are signed, in the range -32768 to 32767. They are stored as two 8-bit bytes. The first byte contains the least significant 8 bits of the value, and the second byte contains the most significant 8 bits. (Thus, the value represented is 256*second+first.) This format corresponds to the hardware of the <font SIZE="-1">VAX</font> and <font SIZE="-1">PDP</font>-11 (that is, little-endian machines). Machines where this does not correspond to the hardware must read the integers as two bytes and compute the little-endian value. </p>
<p> Numbers in a terminal description, whether they are entries in the <i>numbers</i> or <i>strings</i> table, are positive integers. Boolean flags are treated as positive one-byte integers. In each case, those positive integers represent a terminal capability. The terminal compiler tic uses negative integers to handle the cases where a capability is not available:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If a capability is absent from this terminal, tic stores a -1 in the corresponding table.</p>
<dl>
<dd>The integer value -1 is represented by two bytes 0377, 0377.<br />
 Absent boolean values are represented by the byte 0 (false).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If a capability has been canceled from this terminal, tic stores a -2 in the corresponding table.</dd>
<dd>The integer value -2 is represented by two bytes 0377, 0376.<br />
 The boolean value -2 is represented by the byte 0376. </dd>
<p>&nbsp;.IP&nbsp;&bull;&nbsp;4 Other negative values are illegal.</dl>
<p> The <i>terminal names</i> section comes after the <i>header</i>. It contains the first line of the terminfo description, listing the various names for the terminal, separated by the &#8220;|&#8221; character. The <i>terminal names</i> section is terminated with an <font SIZE="-1">ASCII NUL</font> character. </p>
<p> The <i>boolean flags</i> section has one byte for each flag. Boolean capabilities are either 1 or 0 (true or false) according to whether the terminal supports the given capability or not. </p>
<p> Between the <i>boolean flags</i> section and the <i>number</i> section, a null byte will be inserted, if necessary, to ensure that the <i>number</i> section begins on an even byte This is a relic of the PDP-11&#8217;s word-addressed architecture, originally designed to avoid traps induced by addressing a word on an odd byte boundary. All short integers are aligned on a short word boundary. </p>
<p> The <i>numbers</i> section is similar to the <i>boolean flags</i> section. Each capability takes up two bytes, and is stored as a little-endian short integer. </p>
<p> The <i>strings</i> section is also similar. Each capability is stored as a short integer. The capability value is an index into the <i>string table</i>. </p>
<p> The <i>string table</i> is the last section. It contains all of the values of string capabilities referenced in the <i>strings</i> section. Each string is null-terminated. Special characters in ^X or \c notation are stored in their interpreted form, not the printing representation. Padding information $&lt;nn&gt; and parameter information %x are stored intact in uninterpreted form.  </p>
<h3>EXTENDED STORAGE FORMAT</h3>
<p> The previous section describes the conventional terminfo binary format. With some minor variations of the offsets (see PORTABILITY), the same binary format is used in all modern UNIX systems. Each system uses a predefined set of boolean, number or string capabilities. </p>
<p> The <code>ncurses</code> libraries and applications support extended terminfo binary format, allowing users to define capabilities which are loaded at runtime. This extension is made possible by using the fact that the other implementations stop reading the terminfo data when they have reached the end of the size given in the header. <code>ncurses</code> checks the size, and if it exceeds that due to the predefined data, continues to parse according to its own scheme. </p>
<p> First, it reads the extended header (5 short integers): </p>
<dl>
<dd>  </dd>
<dl>
<dt>(1)</dt>
<dd> <p> count of extended boolean capabilities </p>
 </dd>
<dt>(2)</dt>
<dd> <p> count of extended numeric capabilities </p>
 </dd>
<dt>(3)</dt>
<dd> <p> count of extended string capabilities </p>
 </dd>
<dt>(4)</dt>
<dd> <p> count of the items in extended string table </p>
 </dd>
<dt>(5)</dt>
<dd> <p> size of the extended string table in bytes </p>
 </dd></dl>
</dl>
<p> The count- and size-values for the extended string table include the extended capability <i>names</i> as well as extended capability <i>values</i>. </p>
<p> Using the counts and sizes, <code>ncurses</code> allocates arrays and reads data for the extended capabilities in the same order as the header information. </p>
<p> The extended string table contains values for string capabilities. After the end of these values, it contains the names for each of the extended capabilities in order, e.g., booleans, then numbers and finally strings. </p>
<p> Applications which manipulate terminal data can use the definitions described in <code><a href="/docs/linux/man/3X-term_variables/">term_variables</a></code>(3X) which associate the long capability names with members of a <code>TERMTYPE</code> structure.  </p>
<h3>EXTENDED NUMBER FORMAT</h3>
<p> On occasion, 16-bit signed integers are not large enough. With <code>ncurses</code> 6.1, a new format was introduced by making a few changes to the legacy format: <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 a different magic number (octal 01036) <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 changing the type for the <i>number</i> array from signed 16-bit integers to signed 32-bit integers. </p>
<p> To maintain compatibility, the library presents the same data structures to direct users of the <code>TERMTYPE</code> structure as in previous formats. However, that cannot provide callers with the extended numbers. The library uses a similar but hidden data structure <code>TERMTYPE2</code> to provide data for the terminfo functions.  </p>
<h2>PORTABILITY</h2>
<h3>setupterm</h3>
<p> Note that it is possible for <code>setupterm</code> to expect a different set of capabilities than are actually present in the file. Either the database may have been updated since <code>setupterm</code> was recompiled (resulting in extra unrecognized entries in the file) or the program may have been recompiled more recently than the database was updated (resulting in missing entries). The routine <code>setupterm</code> must be prepared for both possibilities &#8211; this is why the numbers and sizes are included. Also, new capabilities must always be added at the end of the lists of boolean, number, and string capabilities.  </p>
<h3>Binary format</h3>
<p> X/Open Curses does not specify a format for the terminfo database. UNIX System V curses used a directory-tree of binary files, one per terminal description. </p>
<p> Despite the consistent use of little-endian for numbers and the otherwise self-describing format, it is not wise to count on portability of binary terminfo entries between commercial UNIX versions. The problem is that there are at least three versions of terminfo (under HP-UX, AIX, and OSF/1) which diverged from System V terminfo after SVr1, and have added extension capabilities to the string table that (in the binary format) collide with System V and XSI Curses extensions. See <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) for detailed discussion of terminfo source compatibility issues. </p>
<p> This implementation is by default compatible with the binary terminfo format used by Solaris curses, except in a few less-used details where it was found that the latter did not match X/Open Curses. The format used by the other Unix versions can be matched by building ncurses with different configuration options.  </p>
<h3>Magic codes</h3>
<p> The magic number in a binary terminfo file is the first 16-bits (two bytes). Besides making it more reliable for the library to check that a file is terminfo, utilities such as <code>file</code> also use that to tell what the file-format is. System V defined more than one magic number, with 0433, 0435 as screen-dumps (see <code><a href="/docs/linux/man/5-scr_dump/">scr_dump</a></code>(5)). This implementation uses 01036 as a continuation of that sequence, but with a different high-order byte to avoid confusion.  </p>
<h3>The TERMTYPE structure</h3>
<p> Direct access to the <code>TERMTYPE</code> structure is provided for legacy applications. Portable applications should use the <code>tigetflag</code> and related functions described in <code><a href="/docs/linux/man/3X-curs_terminfo/">curs_terminfo</a></code>(3X) for reading terminal capabilities.  </p>
<h3>Mixed-case terminal names</h3>
<p> A small number of terminal descriptions use uppercase characters in their names. If the underlying filesystem ignores the difference between uppercase and lowercase, <code>ncurses</code> represents the ``first character&#8217;&#8216; of the terminal name used as the intermediate level of a directory tree in (two-character) hexadecimal form.  </p>
<h2>EXAMPLE</h2>
<p> As an example, here is a description for the Lear-Siegler ADM-3, a popular though rather stupid early terminal: <br />
&nbsp;.sp <br />
&nbsp;.in&nbsp;+4 </p>
<pre><code>adm3a|lsi adm3a,
        am,
        cols#80, lines#24,
        bel=^G, clear=&nbsp;32$&lt;1&gt;, cr=^M, cub1=^H, cud1=^J,
        cuf1=^L, cup=\E=%p1%{32}%+%c%p2%{32}%+%c, cuu1=^K,
        home=^^, ind=^J,
 .sp .in +4
and a hexadecimal dump of the compiled terminal description:
 .sp .in +4<font SIZE="-2">0000 1a 01 10 00 02 00 03 00 82 00 31 00 61 64 6d 33 ........ ..1.adm3
0010 61 7c 6c 73 69 20 61 64 6d 33 61 00 00 01 50 00 a|lsi ad m3a...P.
0020 ff ff 18 00 ff ff 00 00 02 00 ff ff ff ff 04 00 ........ ........
0030 ff ff ff ff ff ff ff ff 0a 00 25 00 27 00 ff ff ........ ..%.'...
0040 29 00 ff ff ff ff 2b 00 ff ff 2d 00 ff ff ff ff ).....+. ..-.....
0050 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
0060 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
0070 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
0080 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
0090 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
00a0 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
00b0 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
00c0 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
00d0 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
00e0 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
00f0 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
0100 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
0110 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ........ ........
0120 ff ff ff ff ff ff 2f 00 07 00 0d 00 1a 24 3c 31 ....../. .....$&lt;1
0130 3e 00 1b 3d 25 70 31 25 7b 33 32 7d 25 2b 25 63 &gt;..=%p1% {32}%+%c
0140 25 70 32 25 7b 33 32 7d 25 2b 25 63 00 0a 00 1e %p2%{32} %+%c....
0150 00 08 00 0c 00 0b 00 0a 00 ........ .</font>
</code></pre>
<p> <br />
&nbsp;.in -4 </p>
<h2>LIMITS</h2>
<p> Some limitations: <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 total compiled entries cannot exceed 4096 bytes in the legacy format. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 total compiled entries cannot exceed 32768 bytes in the extended format. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 the name field cannot exceed 128 bytes. </p>
<p> Compiled entries are limited to 32768 bytes because offsets into the <i>strings table</i> use two-byte integers. The legacy format could have supported 32768-byte entries, but was limited a virtual memory page&#8217;s 4096 bytes.  </p>
<h2>FILES</h2>
<p> /etc/terminfo/*/*<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>compiled terminal capability database<br />
  </p>
<h2>SEE ALSO</h2>
<p> <code>ncurses</code>(3NCURSES), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5).  </p>
<h2>AUTHORS</h2>
<p> Thomas E. Dickey <br />
 extended terminfo format for ncurses 5.0 <br />
 hashed database support for ncurses 5.6 <br />
 extended number support for ncurses 6.1 </p>
<p> Eric S. Raymond <br />
 documented legacy terminfo format, e.g., from pcurses. </p>
<h2>Index</h2>
