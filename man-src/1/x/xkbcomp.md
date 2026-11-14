---
title: "xkbcomp(1)"
name: "xkbcomp"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xkbcomp/"
description: "xkbcomp – compile XKB keyboard description"
---

<h2 class="name">NAME</h2>
<p> xkbcomp &#8211; compile XKB keyboard description </p>
<h2>SYNOPSIS</h2>
<p> <code>xkbcomp</code> [option] source [ destination ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xkbcomp</i> keymap compiler converts a description of an XKB keymap into one of several output formats. The most common use for xkbcomp is to create a compiled keymap file (.xkm extension) which can be read directly by XKB-capable X servers or utilities. The keymap compiler can also produce C header files or XKB source files. The C header files produced by xkbcomp can be included by X servers or utilities that need a built-in default keymap. The XKB source files produced by <i>xkbcomp</i> are fully resolved and can be used to verify that the files which typically make up an XKB keymap are merged correctly or to create a single file which contains a complete description of the keymap. </p>
<p> The <i>source</i> may specify an X display, or an <i>.xkb</i> or <i>.xkm</i> file; unless explicitly specified, the format of <i>destination</i> depends on the format of the source. Compiling a <i>.xkb</i> (keymap source) file generates a <i>.xkm</i> (compiled keymap file) by default. If the source is a <i>.xkm</i> file or an X display, <i>xkbcomp</i> generates a keymap source file by default. </p>
<p> If the <i>destination</i> is an X display, the keymap for the display is updated with the compiled keymap. </p>
<p> The name of the <i>destination</i> is usually computed from the name of the source, with the extension replaced as appropriate. When compiling a single map from a file which contains several maps, <i>xkbcomp</i> constructs the destination file name by appending an appropriate extension to the name of the map to be used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Show all keyboard information, reporting implicit or derived information as a comment. Only affects <i>.xkb</i> format output.</p>
<dt><code>-C</code></p>
<dd> Produce a C header file as output (.h extension).</p>
<dt><code>-dflts</code></p>
<dd> Compute defaults for any missing components, such as key names.</p>
<dt><code>-em1 </code><i>msg</i></p>
<dd> Print <i>msg</i> before printing first error message.</p>
<dt><code>-emp </code><i>msg</i></p>
<dd> Print <i>msg</i> at the start of each message line.</p>
<dt><code>-eml </code><i>msg</i></p>
<dd> If there were any errors, print <i>msg</i> before exiting.</p>
<dt><code>-help, -?</code></p>
<dd> Show available options.</p>
<dt><code>-I</code><i>dir</i></p>
<dd> Specifies top-level directories to be searched for files included by the keymap description. After all directories specified by -I options have been searched, the current directory and finally, the default xkb directory /usr/share/X11/xkb will be searched. </p>
<p> To prevent the current and default directories from being searched, use the -I option alone (i.e. without a directory), before any -I options that specify the directories you do want searched.</p>
<dt><code>-i&nbsp;</code><i>deviceid</i></p>
<dd> If <i>source</i> or <i>destination</i> is a valid X display, load the keymap from/into the device with the specified ID (not name).</p>
<dt><code>-l</code></p>
<dd> List maps that specify the <i>map</i> pattern in any files listed on the command line (not implemented yet).</p>
<dt><code>-m&nbsp;</code><i>name</i></p>
<dd> Specifies a map to be compiled from an file with multiple entries.</p>
<dt><code>-merge</code></p>
<dd> Merge the compiled information with the map from the server (not implemented yet).</p>
<dt><code>-o&nbsp;</code><i>name</i></p>
<dd> Specifies a name for the generated output file. The default is the name of the source file with an appropriate extension for the output format.</p>
<dt><code>-opt&nbsp;</code><i>parts</i></p>
<dd> Specifies a list of optional parts. Compilation errors in any optional parts are not fatal. Parts may consist of any combination of the letters <i>c</i>, <i>g</i>,<i>k</i>,<i>s</i>,<i>t</i> which specify the compatibility map, geometry, keycodes, symbols and types, respectively.</p>
<dt><code>-R</code><i>dir</i></p>
<dd> Specifies the root directory for relative path names.</p>
<dt><code>-synch</code></p>
<dd> Force synchronization for X requests.</p>
<dt><code>-version</code></p>
<dd> Print version number.</p>
<dt><code>-w&nbsp;</code><i>lvl</i></p>
<dd> Controls the reporting of warnings during compilation. A warning level of 0 disables all warnings; a warning level of 10 enables them all.</p>
<dt><code>-xkb</code></p>
<dd> Generate a source description of the keyboard as output (.xkb extension).</p>
<dt><code>-xkm</code></p>
<dd> Generate a compiled keymap file as output (.xkm extension).</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1994, Silicon Graphics Computer Systems and X Consortium, Inc.<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Erik Fortune, Silicon Graphics </p>
<h2>Index</h2>
