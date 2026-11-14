---
title: "arm-gp2x-linux-ar(1)"
name: "arm-gp2x-linux-ar"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm-gp2x-linux-ar/"
description: "ar – create, modify, and extract from archives"
---

<h2>NAME</h2>
<p> ar &#8211; create, modify, and extract from archives</p>
<h2>SYNOPSIS</h2>
<p> ar [<code>-X32_64</code>] [<code>&#8211;</code>]<i>p</i>[<i>mod</i> [<i>relpos</i>] [<i>count</i>]] <i>archive</i> [<i>member</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <font SIZE="-1">GNU</font> <code>ar</code> program creates, modifies, and extracts from archives. An <i>archive</i> is a single file holding a collection of other files in a structure that makes it possible to retrieve the original individual files (called <i>members</i> of the archive). </p>
<p> The original files&#8217; contents, mode (permissions), timestamp, owner, and group are preserved in the archive, and can be restored on extraction. </p>
<p> <font SIZE="-1">GNU</font> <code>ar</code> can maintain archives whose members have names of any length; however, depending on how <code>ar</code> is configured on your system, a limit on member-name length may be imposed for compatibility with archive formats maintained with other tools. If it exists, the limit is often 15 characters (typical of formats related to a.out) or 16 characters (typical of formats related to coff). </p>
<p> <code>ar</code> is considered a binary utility because archives of this sort are most often used as <i>libraries</i> holding commonly needed subroutines. </p>
<p> <code>ar</code> creates an index to the symbols defined in relocatable object modules in the archive when you specify the modifier <code>s</code>. Once created, this index is updated in the archive whenever <code>ar</code> makes a change to its contents (save for the <code>q</code> update operation). An archive with such an index speeds up linking to the library, and allows routines in the library to call each other without regard to their placement in the archive. </p>
<p> You may use <code>nm -s</code> or <code>nm &#8211;print-armap</code> to list this index table. If an archive lacks the table, another form of <code>ar</code> called <code>ranlib</code> can be used to add just the table. </p>
<p> <font SIZE="-1">GNU</font> <code>ar</code> is designed to be compatible with two different facilities. You can control its activity using command-line options, like the different varieties of <code>ar</code> on Unix systems; or, if you specify the single command-line option <code>-M</code>, you can control it with a script supplied via standard input, like the <font SIZE="-1">MRI</font> &#8220;librarian&#8221; program.</p>
<h2>OPTIONS</h2>
<p> <font SIZE="-1">GNU</font> <code>ar</code> allows you to mix the operation code <i>p</i> and modifier flags <i>mod</i> in any order, within the first command-line argument. </p>
<p> If you wish, you may begin the first command-line argument with a dash. </p>
<p> The <i>p</i> keyletter specifies what operation to execute; it may be any of the following, but you must specify only one of them:</p>
<dl>
<dt><code>d</code></p>
<dd> <i>Delete</i> modules from the archive. Specify the names of modules to be deleted as <i>member</i>&#8230;; the archive is untouched if you specify no files to delete. </p>
<p> If you specify the <code>v</code> modifier, <code>ar</code> lists each module as it is deleted.</p>
<dt><code>m</code></p>
<dd> Use this operation to <i>move</i> members in an archive. </p>
<p> The ordering of members in an archive can make a difference in how programs are linked using the library, if a symbol is defined in more than one member. </p>
<p> If no modifiers are used with <tt>&quot;m&quot;</tt>, any members you name in the <i>member</i> arguments are moved to the <i>end</i> of the archive; you can use the <code>a</code>, <code>b</code>, or <code>i</code> modifiers to move them to a specified place instead.</p>
<dt><code>p</code></p>
<dd> <i>Print</i> the specified members of the archive, to the standard output file. If the <code>v</code> modifier is specified, show the member name before copying its contents to standard output. </p>
<p> If you specify no <i>member</i> arguments, all the files in the archive are printed.</p>
<dt><code>q</code></p>
<dd> <i>Quick append</i>; Historically, add the files <i>member</i>&#8230; to the end of <i>archive</i>, without checking for replacement. </p>
<p> The modifiers <code>a</code>, <code>b</code>, and <code>i</code> do <i>not</i> affect this operation; new members are always placed at the end of the archive. </p>
<p> The modifier <code>v</code> makes <code>ar</code> list each file as it is appended. </p>
<p> Since the point of this operation is speed, the archive&#8217;s symbol table index is not updated, even if it already existed; you can use <code>ar s</code> or <code>ranlib</code> explicitly to update the symbol table index. </p>
<p> However, too many different systems assume quick append rebuilds the index, so <font SIZE="-1">GNU</font> <code>ar</code> implements <code>q</code> as a synonym for <code>r</code>.</p>
<dt><code>r</code></p>
<dd> Insert the files <i>member</i>&#8230; into <i>archive</i> (with <i>replacement</i>). This operation differs from <code>q</code> in that any previously existing members are deleted if their names match those being added. </p>
<p> If one of the files named in <i>member</i>&#8230; does not exist, <code>ar</code> displays an error message, and leaves undisturbed any existing members of the archive matching that name. </p>
<p> By default, new members are added at the end of the file; but you may use one of the modifiers <code>a</code>, <code>b</code>, or <code>i</code> to request placement relative to some existing member. </p>
<p> The modifier <code>v</code> used with this operation elicits a line of output for each file inserted, along with one of the letters <code>a</code> or <code>r</code> to indicate whether the file was appended (no old member deleted) or replaced.</p>
<dt><code>t</code></p>
<dd> Display a <i>table</i> listing the contents of <i>archive</i>, or those of the files listed in <i>member</i>&#8230; that are present in the archive. Normally only the member name is shown; if you also want to see the modes (permissions), timestamp, owner, group, and size, you can request that by also specifying the <code>v</code> modifier. </p>
<p> If you do not specify a <i>member</i>, all files in the archive are listed. </p>
<p> If there is more than one file with the same name (say, <code>fie</code>) in an archive (say <code>b.a</code>), <code>ar t b.a fie</code> lists only the first instance; to see them all, you must ask for a complete listing&#8212;in our example, <code>ar t b.a</code>.</p>
<dt><code>x</code></p>
<dd> <i>Extract</i> members (named <i>member</i>) from the archive. You can use the <code>v</code> modifier with this operation, to request that <code>ar</code> list each name as it extracts it. </p>
<p> If you do not specify a <i>member</i>, all files in the archive are extracted.</dl>
<p> A number of modifiers (<i>mod</i>) may immediately follow the <i>p</i> keyletter, to specify variations on an operation&#8217;s behavior:</p>
<dl>
<dt><code>a</code></p>
<dd> Add new files <i>after</i> an existing member of the archive. If you use the modifier <code>a</code>, the name of an existing archive member must be present as the <i>relpos</i> argument, before the <i>archive</i> specification.</p>
<dt><code>b</code></p>
<dd> Add new files <i>before</i> an existing member of the archive. If you use the modifier <code>b</code>, the name of an existing archive member must be present as the <i>relpos</i> argument, before the <i>archive</i> specification. (same as <code>i</code>).</p>
<dt><code>c</code></p>
<dd> <i>Create</i> the archive. The specified <i>archive</i> is always created if it did not exist, when you request an update. But a warning is issued unless you specify in advance that you expect to create it, by using this modifier.</p>
<dt><code>f</code></p>
<dd> Truncate names in the archive. <font SIZE="-1">GNU</font> <code>ar</code> will normally permit file names of any length. This will cause it to create archives which are not compatible with the native <code>ar</code> program on some systems. If this is a concern, the <code>f</code> modifier may be used to truncate file names when putting them in the archive.</p>
<dt><code>i</code></p>
<dd> Insert new files <i>before</i> an existing member of the archive. If you use the modifier <code>i</code>, the name of an existing archive member must be present as the <i>relpos</i> argument, before the <i>archive</i> specification. (same as <code>b</code>).</p>
<dt><code>l</code></p>
<dd> This modifier is accepted but not used.</p>
<dt><code>N</code></p>
<dd> Uses the <i>count</i> parameter. This is used if there are multiple entries in the archive with the same name. Extract or delete instance <i>count</i> of the given name from the archive.</p>
<dt><code>o</code></p>
<dd> Preserve the <i>original</i> dates of members when extracting them. If you do not specify this modifier, files extracted from the archive are stamped with the time of extraction.</p>
<dt><code>P</code></p>
<dd> Use the full path name when matching names in the archive. <font SIZE="-1">GNU</font> <code>ar</code> can not create an archive with a full path name (such archives are not <font SIZE="-1">POSIX</font> complaint), but other archive creators can. This option will cause <font SIZE="-1">GNU</font> <code>ar</code> to match file names using a complete path name, which can be convenient when extracting a single file from an archive created by another tool.</p>
<dt><code>s</code></p>
<dd> Write an object-file index into the archive, or update an existing one, even if no other change is made to the archive. You may use this modifier flag either with any operation, or alone. Running <code>ar s</code> on an archive is equivalent to running <code>ranlib</code> on it.</p>
<dt><code>S</code></p>
<dd> Do not generate an archive symbol table. This can speed up building a large library in several steps. The resulting archive can not be used with the linker. In order to build a symbol table, you must omit the <code>S</code> modifier on the last execution of <code>ar</code>, or you must run <code>ranlib</code> on the archive.</p>
<dt><code>u</code></p>
<dd> Normally, <code>ar r</code>&#8230; inserts all files listed into the archive. If you would like to insert <i>only</i> those of the files you list that are newer than existing members of the same names, use this modifier. The <code>u</code> modifier is allowed only for the operation <code>r</code> (replace). In particular, the combination <code>qu</code> is not allowed, since checking the timestamps would lose any speed advantage from the operation <code>q</code>.</p>
<dt><code>v</code></p>
<dd> This modifier requests the <i>verbose</i> version of an operation. Many operations display additional information, such as filenames processed, when the modifier <code>v</code> is appended.</p>
<dt><code>V</code></p>
<dd> This modifier shows the version number of <code>ar</code>.</dl>
<p> <code>ar</code> ignores an initial option spelt <code>-X32_64</code>, for compatibility with <font SIZE="-1">AIX</font>. The behaviour produced by this option is the default for <font SIZE="-1">GNU</font> <code>ar</code>. <code>ar</code> does not support any of the other <code>-X</code> options; in particular, it does not support <code>-X32</code> which is the default for <font SIZE="-1">AIX</font> <code>ar</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1), <i><a href="/docs/linux/man/1-ranlib/">ranlib</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
