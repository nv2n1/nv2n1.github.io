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
<dt><code>directory tree</code></p>
<dd>A two-level scheme is used to avoid a linear search of a huge <font SIZE="-1">UNIX</font> system directory: <code>/etc/terminfo/c/name</code> where <i>name</i> is the name of the terminal, and <i>c</i> is the first character of <i>name</i>. Thus, <i>act4</i> can be found in the file <code>/etc/terminfo/a/act4</code>. Synonyms for the same terminal are implemented by multiple links to the same compiled file.</p>
<dt><code>hashed database</code></p>
<dd>Using Berkeley database, two types of records are stored: the terminfo data in the same format as stored in a directory tree with the terminfo&#8217;s primary name as a key, and records containing only aliases pointing to the primary name.</p>
<dd>If built to write hashed databases, <code>ncurses</code> can still read terminfo databases organized as a directory tree, but cannot write entries into the directory tree. It can write (or rewrite) entries in the hashed database.</p>
<dd><code>ncurses</code> distinguishes the two cases in the TERMINFO and TERMINFO_DIRS environment variable by assuming a directory tree for entries that correspond to an existing directory, and hashed database otherwise.</dl>
<h3>Legacy Storage Format</h3>
<p>The format has been chosen so that it will be the same on all hardware. An 8 or more bit byte is assumed, but no assumptions about byte ordering or sign extension are made. </p>
<p> The compiled file is created with the <code>tic</code> program, and read by the routine <code><a href="//www.systutorials.com/docs/linux/man/3X-setupterm/">setupterm</a></code>(3X). The file is divided into six parts:</p>
<dl>
<dd>
<dl>
<dt>a) <i>header</i>,</p>
<dd>
<dt>b) <i>terminal names</i>,</p>
<dd>
<dt>c) <i>boolean flags</i>,</p>
<dd>
<dt>d) <i>numbers</i>,</p>
<dd>
<dt>e) <i>strings</i>, and</p>
<dd>
<dt>f) <i>string table</i>.</p>
<dd></dl>
</dl>
<p> The <i>header</i> section begins the file. This section contains six short integers in the format described below. These integers are</p>
<dl>
<dd>
<dl>
<dt>(1) the <i>magic number</i> (octal 0432);</p>
<dd>
<dt>(2) the size, in bytes, of the <i>terminal names</i> section;</p>
<dd>
<dt>(3) the number of bytes in the <i>boolean flags</i> section;</p>
<dd>
<dt>(4) the number of short integers in the <i>numbers</i> section;</p>
<dd>
<dt>(5) the number of offsets (short integers) in the <i>strings</i> section;</p>
<dd>
<dt>(6) the size, in bytes, of the <i>string table</i>.</p>
<dd></dl>
</dl>
<p> The capabilities in the <i>boolean flags</i>, <i>numbers</i>, and <i>strings</i> sections are in the same order as the file &lt;term.h&gt;. </p>
<p> Short integers are signed, in the range -32768 to 32767. They are stored as two 8-bit bytes. The first byte contains the least significant 8 bits of the value, and the second byte contains the most significant 8 bits. (Thus, the value represented is 256*second+first.) This format corresponds to the hardware of the <font SIZE="-1">VAX</font> and <font SIZE="-1">PDP</font>-11 (that is, little-endian machines). Machines where this does not correspond to the hardware must read the integers as two bytes and compute the little-endian value. </p>
<p> Numbers in a terminal description, whether they are entries in the <i>numbers</i> or <i>strings</i> table, are positive integers. Boolean flags are treated as positive one-byte integers. In each case, those positive integers represent a terminal capability. The terminal compiler tic uses negative integers to handle the cases where a capability is not available:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If a capability is absent from this terminal, tic stores a -1 in the corresponding table.</p>
<dl>
<dd>The integer value -1 is represented by two bytes 0377, 0377.<br />
 Absent boolean values are represented by the byte 0 (false).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If a capability has been canceled from this terminal, tic stores a -2 in the corresponding table.</p>
<dd>The integer value -2 is represented by two bytes 0377, 0376.<br />
 The boolean value -2 is represented by the byte 0376. </p>
<p>&nbsp;.IP&nbsp;&bull;&nbsp;4 Other negative values are illegal.</dl>
<p> The <i>terminal names</i> section comes after the <i>header</i>. It contains the first line of the terminfo description, listing the various names for the terminal, separated by the &#8220;|&#8221; character. The <i>terminal names</i> section is terminated with an <font SIZE="-1">ASCII NUL</font> character. </p>
<p> The <i>boolean flags</i> section has one byte for each flag. Boolean capabilities are either 1 or 0 (true or false) according to whether the terminal supports the given capability or not. </p>
<p> Between the <i>boolean flags</i> section and the <i>number</i> section, a null byte will be inserted, if necessary, to ensure that the <i>number</i> section begins on an even byte This is a relic of the PDP-11&#8217;s word-addressed architecture, originally designed to avoid traps induced by addressing a word on an odd byte boundary. All short integers are aligned on a short word boundary. </p>
<p> The <i>numbers</i> section is similar to the <i>boolean flags</i> section. Each capability takes up two bytes, and is stored as a little-endian short integer. </p>
<p> The <i>strings</i> section is also similar. Each capability is stored as a short integer. The capability value is an index into the <i>string table</i>. </p>
<p> The <i>string table</i> is the last section. It contains all of the values of string capabilities referenced in the <i>strings</i> section. Each string is null-terminated. Special characters in ^X or 
