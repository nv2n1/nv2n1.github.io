---
title: "llvm-ar-14(1)"
name: "llvm-ar-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-ar-14/"
description: "llvm-ar – LLVM archiver"
---

<h2 class="name">NAME</h2>
<p> llvm-ar &#8211; LLVM archiver </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-ar</code> [-]{dmpqrstx}[abcDilLNoOPsSTuUvV] [relpos] [count] archive [files…]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-ar</code> command is similar to the common Unix utility, <code>ar</code>. It archives several files, such as objects and LLVM bitcode files into a single archive library that can be linked into a program. However, the archive can contain any kind of file. By default, <code>llvm-ar</code> generates a symbol table that makes linking faster because only the symbol table needs to be consulted, not each individual file member of the archive. </p>
<p> The <code>llvm-ar</code> command can be used to <i>read</i> archive files in SVR4, GNU, BSD and Darwin format, and <i>write</i> in the GNU, BSD, and Darwin style archive files. If an SVR4 format archive is used with the <i>r</i> (replace), <i>d</i> (delete), <i>m</i> (move) or <i>q</i> (quick update) operations, the archive will be reconstructed in the format defined by <i>&#8211;format</i>. </p>
<p> Here’s where <code>llvm-ar</code> departs from previous <code>ar</code> implementations: </p>
<p> <i>The following option is not supported</i> [f] &#8211; truncate inserted filenames </p>
<p> <i>The following options are ignored for compatibility</i> –plugin=&lt;string&gt; &#8211; load a plugin which adds support for other file formats </p>
<p> [l] &#8211; ignored in <code>ar</code> </p>
<p> <i>Symbol Table</i> Since <code>llvm-ar</code> supports bitcode files, the symbol table it creates includes both native and bitcode symbols. </p>
<p> <i>Deterministic Archives</i> By default, <code>llvm-ar</code> always uses zero for timestamps and UIDs/GIDs to write archives in a deterministic mode. This is equivalent to the <i>D</i> modifier being enabled by default. If you wish to maintain compatibility with other <code>ar</code> implementations, you can pass the <i>U</i> modifier to write actual timestamps and UIDs/GIDs. </p>
<p> <i>Windows Paths</i> When on Windows <code>llvm-ar</code> treats the names of archived <i>files</i> in the same case sensitive manner as the operating system. When on a non-Windows machine <code>llvm-ar</code> does not consider character case.</p>
<h2>OPTIONS</h2>
<p> <code>llvm-ar</code> operations are compatible with other <code>ar</code> implementations. However, there are a few modifiers (<i>L</i>) that are not found in other <code>ar</code> implementations. The options for <code>llvm-ar</code> specify a single basic Operation to perform on the archive, a variety of Modifiers for that Operation, the name of the archive file, and an optional list of file names. If the <i>files</i> option is not specified, it generally means either “none” or “all” members, depending on the operation. The Options, Operations and Modifiers are explained in the sections below. </p>
<p> The minimal set of options is at least one operator and the name of the archive.</p>
<h3>Operations</h3>
<dl>
<dt><code>d [NT]</code></p>
<dd> Delete files from the <code>archive</code>. The <i>N</i> and <i>T</i> modifiers apply to this operation. The <i>files</i> options specify which members should be removed from the archive. It is not an error if a specified file does not appear in the archive. If no <i>files</i> are specified, the archive is not modified.</p>
<dt><code>m [abi]</code></p>
<dd> Move files from one location in the <code>archive</code> to another. The <i>a</i>, <i>b</i>, and <i>i</i> modifiers apply to this operation. The <i>files</i> will all be moved to the location given by the modifiers. If no modifiers are used, the files will be moved to the end of the archive. If no <i>files</i> are specified, the archive is not modified.</p>
<dt><code>p [v]</code></p>
<dd> Print <i>files</i> to the standard output stream. If no <i>files</i> are specified, the entire <code>archive</code> is printed. With the <i>v</i> modifier, <code>llvm-ar</code> also prints out the name of the file being output. Printing binary files is ill-advised as they might confuse your terminal settings. The <i>p</i> operation never modifies the archive.</p>
<dt><code>q [LT]</code></p>
<dd> Quickly append files to the end of the <code>archive</code> without removing duplicates. If no <i>files</i> are specified, the archive is not modified. The behavior when appending one archive to another depends upon whether the <i>L</i> and <i>T</i> modifiers are used:</p>
<dt>&bull;</p>
<dd> Appending a regular archive to a regular archive will append the archive file. If the <i>L</i> modifier is specified the members will be appended instead.</p>
<dt>&bull;</p>
<dd> Appending a regular archive to a thin archive requires the <i>T</i> modifier and will append the archive file. The <i>L</i> modifier is not supported.</p>
<dt>&bull;</p>
<dd> Appending a thin archive to a regular archive will append the archive file. If the <i>L</i> modifier is specified the members will be appended instead.</p>
<dt>&bull;</p>
<dd> Appending a thin archive to a thin archive will always quick append its members.</p>
<dt><code>r [abTu]</code></p>
<dd> Replace existing <i>files</i> or insert them at the end of the <code>archive</code> if they do not exist. The <i>a</i>, <i>b</i>, <i>T</i> and <i>u</i> modifiers apply to this operation. If no <i>files</i> are specified, the archive is not modified. </p>
<p> t[v] .. option:: t [vO] Print the table of contents. Without any modifiers, this operation just prints the names of the members to the standard output stream. With the <i>v</i> modifier, <code>llvm-ar</code> also prints out the file type (B=bitcode, S=symbol table, blank=regular file), the permission mode, the owner and group, are ignored when extracting <i>files</i> and set to placeholder values when adding size, and the date. With the <i>O</i> modifier, display member offsets. If any <i>files</i> are specified, the listing is only for those files. If no <i>files</i> are specified, the table of contents for the whole archive is printed.</p>
<dt><code>V</code></p>
<dd> A synonym for the <i>&#8211;version</i> option.</p>
<dt><code>x [oP]</code></p>
<dd> Extract <code>archive</code> members back to files. The <i>o</i> modifier applies to this operation. This operation retrieves the indicated <i>files</i> from the archive and writes them back to the operating system’s file system. If no <i>files</i> are specified, the entire archive is extracted.</dl>
<h3>Modifiers (operation specific)</h3>
<p> The modifiers below are specific to certain operations. See the Operations section to determine which modifiers are applicable to which operations.</p>
<dl>
<dt><code>a</code></p>
<dd> When inserting or moving member files, this option specifies the destination of the new files as being after the <i>relpos</i> member. If <i>relpos</i> is not found, the files are placed at the end of the <code>archive</code>. <i>relpos</i> cannot be consumed without either <i>a</i>, <i>b</i> or <i>i</i>.</p>
<dt><code>b</code></p>
<dd> When inserting or moving member files, this option specifies the destination of the new files as being before the <i>relpos</i> member. If <i>relpos</i> is not found, the files are placed at the end of the <code>archive</code>. <i>relpos</i> cannot be consumed without either <i>a</i>, <i>b</i> or <i>i</i>. This modifier is identical to the <i>i</i> modifier.</p>
<dt><code>i</code></p>
<dd> A synonym for the <i>b</i> option.</p>
<dt><code>L</code></p>
<dd> When quick appending an <code>archive</code>, instead quick append its members. This is a feature for <code>llvm-ar</code> that is not found in gnu-ar.</p>
<dt><code>N</code></p>
<dd> When extracting or deleting a member that shares its name with another member, the <i>count</i> parameter allows you to supply a positive whole number that selects the instance of the given name, with “1” indicating the first instance. If <i>N</i> is not specified the first member of that name will be selected. If <i>count</i> is not supplied, the operation fails.*count* cannot be</p>
<dt><code>o</code></p>
<dd> When extracting files, use the modification times of any <i>files</i> as they appear in the <code>archive</code>. By default <i>files</i> extracted from the archive use the time of extraction.</p>
<dt><code>O</code></p>
<dd> Display member offsets inside the archive.</p>
<dt><code>T</code></p>
<dd> Alias for <code>&#8211;thin</code>. In many ar implementations <code>T</code> has a different meaning, as specified by X/Open System interface.</p>
<dt><code>v</code></p>
<dd> When printing <i>files</i> or the <code>archive</code> table of contents, this modifier instructs <code>llvm-ar</code> to include additional information in the output.</dl>
<h3>Modifiers (generic)</h3>
<p> The modifiers below may be applied to any operation.</p>
<dl>
<dt><code>c</code></p>
<dd> For the <i>r</i> (replace)and <i>q</i> (quick update) operations, <code>llvm-ar</code> will always create the archive if it doesn’t exist. Normally, <code>llvm-ar</code> will print a warning message indicating that the <code>archive</code> is being created. Using this modifier turns off that warning.</p>
<dt><code>D</code></p>
<dd> Use zero for timestamps and UIDs/GIDs. This is set by default.</p>
<dt><code>P</code></p>
<dd> Use full paths when matching member names rather than just the file name. This can be useful when manipulating an <code>archive</code> generated by another archiver, as some allow paths as member names. This is the default behavior for thin archives.</p>
<dt><code>s</code></p>
<dd> This modifier requests that an archive index (or symbol table) be added to the <code>archive</code>, as if using ranlib. The symbol table will contain all the externally visible functions and global variables defined by all the bitcode files in the archive. By default <code>llvm-ar</code> generates symbol tables in archives. This can also be used as an operation.</p>
<dt><code>S</code></p>
<dd> This modifier is the opposite of the <i>s</i> modifier. It instructs <code>llvm-ar</code> to not build the symbol table. If both <i>s</i> and <i>S</i> are used, the last modifier to occur in the options will prevail.</p>
<dt><code>u</code></p>
<dd> Only update <code>archive</code> members with <i>files</i> that have more recent timestamps.</p>
<dt><code>U</code></p>
<dd> Use actual timestamps and UIDs/GIDs.</dl>
<h3>Other</h3>
<dl>
<dt><code>&#8211;format=&lt;type&gt;</code></p>
<dd> This option allows for default, gnu, darwin or bsd <code>&lt;type&gt;</code> to be selected. When creating an <code>archive</code>, <code>&lt;type&gt;</code> will default to that of the host machine.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a summary of command-line options and their meanings.</p>
<dt><code>-M</code></p>
<dd> This option allows for MRI scripts to be read through the standard input stream. No other options are compatible with this option.</p>
<dt><code>&#8211;rsp-quoting=&lt;type&gt;</code></p>
<dd>
<dt><code>This option selects the quoting style &#8220;&lt;type&gt;&#8220; for response files, either</code></p>
<dd>
<dt><code>&#8220;posix&#8220; or &#8220;windows&#8220;. The default when on Windows is &#8220;windows&#8220;, otherwise the</code></p>
<dd>
<dt><code>default is &#8220;posix&#8220;.</code></p>
<dd>
<dt><code>&#8211;thin</code></p>
<dd> When creating or modifying an archive, this option specifies that the <code>archive</code> will be thin. By default, archives are not created as thin archives and when modifying a thin archive, it will be converted to a regular archive.</p>
<dt><code>&#8211;version</code></p>
<dd> Display the version of the <code>llvm-ar</code> executable.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options and commands from response file <code>&lt;FILE&gt;</code>.</dl>
<h2>MRI SCRIPTS</h2>
<p> <code>llvm-ar</code> understands a subset of the MRI scripting interface commonly supported by archivers following in the ar tradition. An MRI script contains a sequence of commands to be executed by the archiver. The <i>-M</i> option allows for an MRI script to be passed to <code>llvm-ar</code> through the standard input stream. </p>
<p> Note that <code>llvm-ar</code> has known limitations regarding the use of MRI scripts:</p>
<dl>
<dt>&bull;</p>
<dd> Each script can only create one archive.</p>
<dt>&bull;</p>
<dd> Existing archives can not be modified.</dl>
<h3>MRI Script Commands</h3>
<p> Each command begins with the command’s name and must appear on its own line. Some commands have arguments, which must be separated from the name by whitespace. An MRI script should begin with either a <i>CREATE</i> or <i>CREATETHIN</i> command and will typically end with a <i>SAVE</i> command. Any text after either ‘*’ or ‘;’ is treated as a comment.</p>
<dl>
<dt><code>CREATE archive</code></p>
<dd> Begin creation of a regular archive with the specified name. Subsequent commands act upon this <code>archive</code>.</p>
<dt><code>CREATETHIN archive</code></p>
<dd> Begin creation of a thin archive with the specified name. Subsequent commands act upon this <code>archive</code>.</p>
<dt><code>ADDLIB archive</code></p>
<dd> Append the contents of <code>archive</code> to the current archive.</p>
<dt><code>ADDMOD &lt;file&gt;</code></p>
<dd> Append <code>&lt;file&gt;</code> to the current archive.</p>
<dt><code>DELETE &lt;file&gt;</code></p>
<dd> Delete the member of the current archive whose file name, excluding directory components, matches <code>&lt;file&gt;</code>.</p>
<dt><code>SAVE</code></p>
<dd> Write the current archive to the path specified in the previous <i>CREATE</i>/<i>CREATETHIN</i> command.</p>
<dt><code>END</code></p>
<dd> Ends the MRI script (optional).</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-ar</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
