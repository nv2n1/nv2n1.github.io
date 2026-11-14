---
title: "ar(1)"
name: "ar"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ar/"
description: "ar – create, modify, and extract from archives"
---

<h2 class="name">NAME</h2>
<p> ar &#8211; create, modify, and extract from archives </p>
<h2>SYNOPSIS</h2>
<p> ar [<code>-X32_64</code>] [<code>&#8211;</code>]<i>p</i>[<i>mod</i>] [<code>&#8211;plugin</code> <i>name</i>] [<code>&#8211;target</code> <i>bfdname</i>] [<code>&#8211;output</code> <i>dirname</i>] [<code>&#8211;record-libdeps</code> <i>libdeps</i>] [<code>&#8211;thin</code>] [<i>relpos</i>] [<i>count</i>] <i>archive</i> [<i>member</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <font SIZE="-1">GNU</font> <code>ar</code> program creates, modifies, and extracts from archives. An <i>archive</i> is a single file holding a collection of other files in a structure that makes it possible to retrieve the original individual files (called <i>members</i> of the archive). </p>
<p> The original files&#8217; contents, mode (permissions), timestamp, owner, and group are preserved in the archive, and can be restored on extraction. </p>
<p> <font SIZE="-1">GNU</font> <code>ar</code> can maintain archives whose members have names of any length; however, depending on how <code>ar</code> is configured on your system, a limit on member-name length may be imposed for compatibility with archive formats maintained with other tools. If it exists, the limit is often 15 characters (typical of formats related to a.out) or 16 characters (typical of formats related to coff). </p>
<p> <code>ar</code> is considered a binary utility because archives of this sort are most often used as <i>libraries</i> holding commonly needed subroutines. Since libraries often will depend on other libraries, <code>ar</code> can also record the dependencies of a library when the <code>&#8211;record-libdeps</code> option is specified. </p>
<p> <code>ar</code> creates an index to the symbols defined in relocatable object modules in the archive when you specify the modifier <code>s</code>. Once created, this index is updated in the archive whenever <code>ar</code> makes a change to its contents (save for the <code>q</code> update operation). An archive with such an index speeds up linking to the library, and allows routines in the library to call each other without regard to their placement in the archive. </p>
<p> You may use <code>nm -s</code> or <code>nm &#8211;print-armap</code> to list this index table. If an archive lacks the table, another form of <code>ar</code> called <code>ranlib</code> can be used to add just the table. </p>
<p> <font SIZE="-1">GNU</font> <code>ar</code> can optionally create a <i>thin</i> archive, which contains a symbol index and references to the original copies of the member files of the archive. This is useful for building libraries for use within a local build tree, where the relocatable objects are expected to remain available, and copying the contents of each object would only waste time and space. </p>
<p> An archive can either be <i>thin</i> or it can be normal. It cannot be both at the same time. Once an archive is created its format cannot be changed without first deleting it and then creating a new archive in its place. </p>
<p> Thin archives are also <i>flattened</i>, so that adding one thin archive to another thin archive does not nest it, as would happen with a normal archive. Instead the elements of the first archive are added individually to the second archive. </p>
<p> The paths to the elements of the archive are stored relative to the archive itself. </p>
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
<p> Since the point of this operation is speed, implementations of <code>ar</code> have the option of not updating the archive&#8217;s symbol table if one exists. Too many different systems however assume that symbol tables are always up-to-date, so <font SIZE="-1">GNU</font> <code>ar</code> will rebuild the table even with a quick append. </p>
<p> Note &#8211; <font SIZE="-1">GNU</font> <code>ar</code> treats the command <code>qs</code> as a synonym for <code>r</code> &#8211; replacing already existing files in the archive and appending new ones at the end.</p>
<dt><code>r</code></p>
<dd> Insert the files <i>member</i>&#8230; into <i>archive</i> (with <i>replacement</i>). This operation differs from <code>q</code> in that any previously existing members are deleted if their names match those being added. </p>
<p> If one of the files named in <i>member</i>&#8230; does not exist, <code>ar</code> displays an error message, and leaves undisturbed any existing members of the archive matching that name. </p>
<p> By default, new members are added at the end of the file; but you may use one of the modifiers <code>a</code>, <code>b</code>, or <code>i</code> to request placement relative to some existing member. </p>
<p> The modifier <code>v</code> used with this operation elicits a line of output for each file inserted, along with one of the letters <code>a</code> or <code>r</code> to indicate whether the file was appended (no old member deleted) or replaced.</p>
<dt><code>s</code></p>
<dd> Add an index to the archive, or update it if it already exists. Note this command is an exception to the rule that there can only be one command letter, as it is possible to use it as either a command or a modifier. In either case it does the same thing.</p>
<dt><code>t</code></p>
<dd> Display a <i>table</i> listing the contents of <i>archive</i>, or those of the files listed in <i>member</i>&#8230; that are present in the archive. Normally only the member name is shown, but if the modifier <code>O</code> is specified, then the corresponding offset of the member is also displayed. Finally, in order to see the modes (permissions), timestamp, owner, group, and size the <code>v</code> modifier should be included. </p>
<p> If you do not specify a <i>member</i>, all files in the archive are listed. </p>
<p> If there is more than one file with the same name (say, <code>fie</code>) in an archive (say <code>b.a</code>), <code>ar t b.a fie</code> lists only the first instance; to see them all, you must ask for a complete listing&#8212;in our example, <code>ar t b.a</code>.</p>
<dt><code>x</code></p>
<dd> <i>Extract</i> members (named <i>member</i>) from the archive. You can use the <code>v</code> modifier with this operation, to request that <code>ar</code> list each name as it extracts it. </p>
<p> If you do not specify a <i>member</i>, all files in the archive are extracted. </p>
<p> Files cannot be extracted from a thin archive, and there are restrictions on extracting from archives created with <code>P</code>: The paths must not be absolute, may not contain <tt>&quot;..&quot;</tt>, and any subdirectories in the paths must exist. If it is desired to avoid these restrictions then used the <code>&#8211;output</code> option to specify an output directory.</dl>
<p> A number of modifiers (<i>mod</i>) may immediately follow the <i>p</i> keyletter, to specify variations on an operation&#8217;s behavior:</p>
<dl>
<dt><code>a</code></p>
<dd> Add new files <i>after</i> an existing member of the archive. If you use the modifier <code>a</code>, the name of an existing archive member must be present as the <i>relpos</i> argument, before the <i>archive</i> specification.</p>
<dt><code>b</code></p>
<dd> Add new files <i>before</i> an existing member of the archive. If you use the modifier <code>b</code>, the name of an existing archive member must be present as the <i>relpos</i> argument, before the <i>archive</i> specification. (same as <code>i</code>).</p>
<dt><code>c</code></p>
<dd> <i>Create</i> the archive. The specified <i>archive</i> is always created if it did not exist, when you request an update. But a warning is issued unless you specify in advance that you expect to create it, by using this modifier.</p>
<dt><code>D</code></p>
<dd> Operate in <i>deterministic</i> mode. When adding files and the archive index use zero for UIDs, GIDs, timestamps, and use consistent file modes for all files. When this option is used, if <code>ar</code> is used with identical options and identical input files, multiple runs will create identical output files regardless of the input files&#8217; owners, groups, file modes, or modification times. </p>
<p> If <i>binutils</i> was configured with <code>&#8211;enable-deterministic-archives</code>, then this mode is on by default. It can be disabled with the <code>U</code> modifier, below.</p>
<dt><code>f</code></p>
<dd> Truncate names in the archive. <font SIZE="-1">GNU</font> <code>ar</code> will normally permit file names of any length. This will cause it to create archives which are not compatible with the native <code>ar</code> program on some systems. If this is a concern, the <code>f</code> modifier may be used to truncate file names when putting them in the archive.</p>
<dt><code>i</code></p>
<dd> Insert new files <i>before</i> an existing member of the archive. If you use the modifier <code>i</code>, the name of an existing archive member must be present as the <i>relpos</i> argument, before the <i>archive</i> specification. (same as <code>b</code>).</p>
<dt><code>l</code></p>
<dd> Specify dependencies of this library. The dependencies must immediately follow this option character, must use the same syntax as the linker command line, and must be specified within a single argument. I.e., if multiple items are needed, they must be quoted to form a single command line argument. For example <code>L &#8220;-L/usr/local/lib -lmydep1 -lmydep2&#8221;</code></p>
<dt><code>N</code></p>
<dd> Uses the <i>count</i> parameter. This is used if there are multiple entries in the archive with the same name. Extract or delete instance <i>count</i> of the given name from the archive.</p>
<dt><code>o</code></p>
<dd> Preserve the <i>original</i> dates of members when extracting them. If you do not specify this modifier, files extracted from the archive are stamped with the time of extraction.</p>
<dt><code>O</code></p>
<dd> Display member offsets inside the archive. Use together with the <code>t</code> option.</p>
<dt><code>P</code></p>
<dd> Use the full path name when matching or storing names in the archive. Archives created with full path names are not <font SIZE="-1">POSIX</font> compliant, and thus may not work with tools other than up to date <font SIZE="-1">GNU</font> tools. Modifying such archives with <font SIZE="-1">GNU</font> <code>ar</code> without using <code>P</code> will remove the full path names unless the archive is a thin archive. Note that <code>P</code> may be useful when adding files to a thin archive since <code>r</code> without <code>P</code> ignores the path when choosing which element to replace. Thus </p>
<pre>
        ar rcST archive.a subdir/file1 subdir/file2 file1
</pre>
<p> will result in the first <tt>&quot;subdir/file1&quot;</tt> being replaced with <tt>&quot;file1&quot;</tt> from the current directory. Adding <code>P</code> will prevent this replacement.</p>
<dt><code>s</code></p>
<dd> Write an object-file index into the archive, or update an existing one, even if no other change is made to the archive. You may use this modifier flag either with any operation, or alone. Running <code>ar s</code> on an archive is equivalent to running <code>ranlib</code> on it.</p>
<dt><code>S</code></p>
<dd> Do not generate an archive symbol table. This can speed up building a large library in several steps. The resulting archive can not be used with the linker. In order to build a symbol table, you must omit the <code>S</code> modifier on the last execution of <code>ar</code>, or you must run <code>ranlib</code> on the archive.</p>
<dt><code>T</code></p>
<dd> Deprecated alias for <code>&#8211;thin</code>. <code>T</code> is not recommended because in many ar implementations <code>T</code> has a different meaning, as specified by X/Open System Interface.</p>
<dt><code>u</code></p>
<dd> Normally, <code>ar r</code>&#8230; inserts all files listed into the archive. If you would like to insert <i>only</i> those of the files you list that are newer than existing members of the same names, use this modifier. The <code>u</code> modifier is allowed only for the operation <code>r</code> (replace). In particular, the combination <code>qu</code> is not allowed, since checking the timestamps would lose any speed advantage from the operation <code>q</code>.</p>
<dt><code>U</code></p>
<dd> Do <i>not</i> operate in <i>deterministic</i> mode. This is the inverse of the <code>D</code> modifier, above: added files and the archive index will get their actual <font SIZE="-1">UID, GID,</font> timestamp, and file mode values. </p>
<p> This is the default unless <i>binutils</i> was configured with <code>&#8211;enable-deterministic-archives</code>.</p>
<dt><code>v</code></p>
<dd> This modifier requests the <i>verbose</i> version of an operation. Many operations display additional information, such as filenames processed, when the modifier <code>v</code> is appended.</p>
<dt><code>V</code></p>
<dd> This modifier shows the version number of <code>ar</code>.</dl>
<p> The <code>ar</code> program also supports some command-line options which are neither modifiers nor actions, but which do change its behaviour in specific ways:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Displays the list of command-line options supported by <code>ar</code> and then exits.</p>
<dt><code>&#8211;version</code></p>
<dd> Displays the version information of <code>ar</code> and then exits.</p>
<dt><code>-X32_64</code></p>
<dd> <code>ar</code> ignores an initial option spelled <code>-X32_64</code>, for compatibility with <font SIZE="-1">AIX.</font> The behaviour produced by this option is the default for <font SIZE="-1">GNU</font> <code>ar</code>. <code>ar</code> does not support any of the other <code>-X</code> options; in particular, it does not support <code>-X32</code> which is the default for <font SIZE="-1">AIX</font> <code>ar</code>.</p>
<dt><code>&#8211;plugin</code> <i>name</i></p>
<dd> The optional command-line switch <code>&#8211;plugin</code> <i>name</i> causes <code>ar</code> to load the plugin called <i>name</i> which adds support for more file formats, including object files with link-time optimization information. </p>
<p> This option is only available if the toolchain has been built with plugin support enabled. </p>
<p> If <code>&#8211;plugin</code> is not provided, but plugin support has been enabled then <code>ar</code> iterates over the files in <i>${libdir}/bfd-plugins</i> in alphabetic order and the first plugin that claims the object in question is used. </p>
<p> Please note that this plugin search directory is <i>not</i> the one used by <code>ld</code>&#8216;s <code>-plugin</code> option. In order to make <code>ar</code> use the linker plugin it must be copied into the <i>${libdir}/bfd-plugins</i> directory. For <font SIZE="-1">GCC</font> based compilations the linker plugin is called <i>liblto_plugin.so.0.0.0</i>. For Clang based compilations it is called <i>LLVMgold.so</i>. The <font SIZE="-1">GCC</font> plugin is always backwards compatible with earlier versions, so it is sufficient to just copy the newest one.</p>
<dt><code>&#8211;target</code> <i>target</i></p>
<dd> The optional command-line switch <code>&#8211;target</code> <i>bfdname</i> specifies that the archive members are in an object code format different from your system&#8217;s default format. See</p>
<dt><code>&#8211;output</code> <i>dirname</i></p>
<dd> The <code>&#8211;output</code> option can be used to specify a path to a directory into which archive members should be extracted. If this option is not specified then the current directory will be used. </p>
<p> Note &#8211; although the presence of this option does imply a <code>x</code> extraction operation that option must still be included on the command line.</p>
<dt><code>&#8211;record-libdeps</code> <i>libdeps</i></p>
<dd> The <code>&#8211;record-libdeps</code> option is identical to the <code>l</code> modifier, just handled in long form.</p>
<dt><code>&#8211;thin</code></p>
<dd> Make the specified <i>archive</i> a <i>thin</i> archive. If it already exists and is a regular archive, the existing members must be present in the same directory as <i>archive</i>.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nm/">nm</a></code>(1), <code><a href="/docs/linux/man/1-ranlib/">ranlib</a></code>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
