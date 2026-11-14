---
title: "tree(1)"
name: "tree"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tree/"
description: "tree – list contents of directories in a tree-like format."
---

<h2 class="name">NAME</h2>
<p> tree &#8211; list contents of directories in a tree-like format. </p>
<h2>SYNOPSIS</h2>
<p> <code>tree</code> [<code>-acdfghilnpqrstuvxACDFJQNSUX</code>] [<code>-L</code> <i>level</i> [<code>-R</code>]] [<code>-H</code> <i>basehref</i>] [<code>-T</code> <i>title</i>] [<code>-o</code> <i>filename</i>] [<code>-P</code> <i>pattern</i>] [<code>-I</code> <i>pattern</i>] [<code>&#8211;gitignore</code>] [<code>&#8211;matchdirs</code>] [<code>&#8211;metafirst</code>] [<code>&#8211;ignore-case</code>] [<code>&#8211;nolinks</code>] [<code>&#8211;inodes</code>] [<code>&#8211;device</code>] [<code>&#8211;sort</code>[<code>=</code>]<i>name</i>] [<code>&#8211;dirsfirst</code>] [<code>&#8211;filesfirst</code>] [<code>&#8211;filelimit</code> <i>#</i>] [<code>&#8211;si</code>] [<code>&#8211;du</code>] [<code>&#8211;prune</code>] [<code>&#8211;timefmt</code>[<code>=</code>]<i>format</i>] [<code>&#8211;fromfile</code>] [<code>&#8211;info</code>] [<code>&#8211;noreport</code>] [<code>&#8211;version</code>] [<code>&#8211;help</code>] [<code>&#8212;</code>] [<i>directory</i> &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <i>Tree</i> is a recursive directory listing program that produces a depth indented listing of files, which is colorized ala <i>dircolors</i> if the <code>LS_COLORS</code> environment variable is set and output is to tty. With no arguments, <i>tree</i> lists the files in the current directory. When directory arguments are given, <i>tree</i> lists all the files and/or directories found in the given directories each in turn. Upon completion of listing all files/directories found, <i>tree</i> returns the total number of files and/or directories listed. </p>
<p> By default, when a symbolic link is encountered, the path that the symbolic link refers to is printed after the name of the link in the format: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;name -&gt;&nbsp;real-path </p>
<p> If the `<code>-l</code>&#8216; option is given and the symbolic link refers to an actual directory, then <i>tree</i> will follow the path of the symbolic link as if it were a real directory. </p>
<h2>OPTIONS</h2>
<p> <i>Tree</i> understands the following command line switches: </p>
<h2>LISTING OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> All files are printed. By default tree does not print hidden files (those beginning with a dot `.&#8217;). In no event does tree print the file system constructs `.&#8217; (current directory) and `..&#8217; (previous directory).</dl>
<dl>
<dt><code>-d</code></p>
<dd> List directories only.</dl>
<dl>
<dt><code>-l</code></p>
<dd> Follows symbolic links if they point to directories, as if they were directories. Symbolic links that will result in recursion are avoided when detected.</dl>
<dl>
<dt><code>-f</code></p>
<dd> Prints the full path prefix for each file.</dl>
<dl>
<dt><code>-x</code></p>
<dd> Stay on the current file-system only. Ala <code>find </code><i>-xdev</i>.</dl>
<dl>
<dt><code>-L </code><i>level</i></p>
<dd> Max display depth of the directory tree.</dl>
<dl>
<dt><code>-R</code></p>
<dd> Recursively cross down the tree each <i>level</i> directories (see <code>-L</code> option), and at each of them execute <code>tree</code> again adding `-o 00Tree.html&#8217; as a new option.</dl>
<dl>
<dt><code>-P </code><i>pattern</i></p>
<dd> List only those files that match the wild-card <i>pattern</i>. You may have multiple -P options. Note: you must use the <i>-a</i> option to also consider those files beginning with a dot `.&#8217; for matching. Valid wildcard operators are `*&#8217; (any zero or more characters), `**` (any zero or more characters as well as null /&#8217;s, i.e. /**/ may match a single /), `?&#8217; (any single character), `[&#8230;]&#8217; (any single character listed between brackets (optional &#8211; (dash) for character range may be used: ex: [A-Z]), and `[^&#8230;]&#8217; (any single character not listed in brackets) and `|&#8217; separates alternate patterns. A &#8216;/&#8217; at the end of the pattern matches directories, but not files.</dl>
<dl>
<dt><code>-I </code><i>pattern</i></p>
<dd> Do not list those files that match the wild-card <i>pattern</i>. You may have multiple -I options. See <i>-P</i> above for information on wildcard patterns.</dl>
<dl>
<dt><code>&#8211;gitignore</code></p>
<dd> Uses git <code>.gitignore</code> files for filtering files and directories. Also uses <code>$GIT_DIR/info/exclude</code> if present.</dl>
<dl>
<dt><code>&#8211;ignore-case</code></p>
<dd> If a match pattern is specified by the <code>-P</code> or <code>-I</code> option, this will cause the pattern to match without regards to the case of each letter.</dl>
<dl>
<dt><code>&#8211;matchdirs</code></p>
<dd> If a match pattern is specified by the <code>-P</code> option, this will cause the pattern to be applied to directory names (in addition to filenames). In the event of a match on the directory name, matching is disabled for the directory&#8217;s contents. If the <code>&#8211;prune</code> option is used, empty folders that match the pattern will not be pruned.</dl>
<dl>
<dt><code>&#8211;metafirst</code></p>
<dd> Print the meta-data information at the beginning of the line rather than after the indentation lines.</dl>
<dl>
<dt><code>&#8211;prune</code></p>
<dd> Makes tree prune empty directories from the output, useful when used in conjunction with <code>-P</code> or <code>-I</code>. See <code>BUGS AND NOTES</code> below for more information on this option.</dl>
<dl>
<dt><code>&#8211;info</code></p>
<dd> Prints file comments found in .info files. See <code>.INFO FILES</code> below for more information on the format of .info files.</dl>
<dl>
<dt><code>&#8211;noreport</code></p>
<dd> Omits printing of the file and directory report at the end of the tree listing.</dl>
<dl>
<dt><code>&#8211;charset </code><i>charset</i></p>
<dd> Set the character set to use when outputting HTML and for line drawing.</dl>
<dl>
<dt><code>&#8211;filelimit </code><i>#</i></p>
<dd> Do not descend directories that contain more than <i>#</i> entries.</dl>
<dl>
<dt><code>&#8211;timefmt </code><i>format</i></p>
<dd> Prints (implies -D) and formats the date according to the format string which uses the <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) syntax.</dl>
<dl>
<dt><code>-o </code><i>filename</i></p>
<dd> Send output to <i>filename</i>.</dl>
<h2>FILE OPTIONS</h2>
<dl>
<dt><code>-q</code></p>
<dd> Print non-printable characters in filenames as question marks instead of the default.</dl>
<dl>
<dt><code>-N</code></p>
<dd> Print non-printable characters as is instead of as escaped octal numbers.</dl>
<dl>
<dt><code>-Q</code></p>
<dd> Quote the names of files in double quotes.</dl>
<dl>
<dt><code>-p</code></p>
<dd> Print the file type and permissions for each file (as per ls -l).</dl>
<dl>
<dt><code>-u</code></p>
<dd> Print the username, or UID # if no username is available, of the file.</dl>
<dl>
<dt><code>-g</code></p>
<dd> Print the group name, or GID # if no group name is available, of the file.</dl>
<dl>
<dt><code>-s</code></p>
<dd> Print the size of each file in bytes along with the name.</dl>
<dl>
<dt><code>-h</code></p>
<dd> Print the size of each file but in a more human readable way, e.g. appending a size letter for kilobytes (K), megabytes (M), gigabytes (G), terabytes (T), petabytes (P) and exabytes (E).</dl>
<dl>
<dt><code>&#8211;si</code></p>
<dd> Like <code>-h</code> but use SI units (powers of 1000) instead.</dl>
<dl>
<dt><code>&#8211;du</code></p>
<dd> For each directory report its size as the accumulation of sizes of all its files and sub-directories (and their files, and so on). The total amount of used space is also given in the final report (like the &#8216;du -c&#8217; command.) This option requires tree to read the entire directory tree before emitting it, see <code>BUGS AND NOTES</code> below. Implies <code>-s</code>.</dl>
<dl>
<dt><code>-D</code></p>
<dd> Print the date of the last modification time or if <code>-c</code> is used, the last status change time for the file listed.</dl>
<dl>
<dt><code>-F</code></p>
<dd> Append a `/&#8217; for directories, a `=&#8217; for socket files, a `*&#8217; for executable files, a `&gt;&#8217; for doors (Solaris) and a `|&#8217; for FIFO&#8217;s, as per ls -F</dl>
<dl>
<dt><code>&#8211;inodes</code></p>
<dd> Prints the inode number of the file or directory</dl>
<dl>
<dt><code>&#8211;device</code></p>
<dd> Prints the device number to which the file or directory belongs</dl>
<h2>SORTING OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Sort the output by version.</dl>
<dl>
<dt><code>-t</code></p>
<dd> Sort the output by last modification time instead of alphabetically.</dl>
<dl>
<dt><code>-c</code></p>
<dd> Sort the output by last status change instead of alphabetically. Modifies the <code>-D</code> option (if used) to print the last status change instead of modification time.</dl>
<dl>
<dt><code>-U</code></p>
<dd> Do not sort. Lists files in directory order. Disables <code>&#8211;dirsfirst</code>.</dl>
<dl>
<dt><code>-r</code></p>
<dd> Sort the output in reverse order. This is a meta-sort that alter the above sorts. This option is disabled when <code>-U</code> is used.</dl>
<dl>
<dt><code>&#8211;dirsfirst</code></p>
<dd> List directories before files. This is a meta-sort that alters the above sorts. This option is disabled when <code>-U</code> is used.</dl>
<dl>
<dt><code>&#8211;filesfirst</code></p>
<dd> List files before directories. This is a meta-sort that alters the above sorts. This option is disabled when <code>-U</code> is used.</dl>
<dl>
<dt><code>&#8211;sort</code>[<code>=</code>]<i>type</i></p>
<dd> Sort the output by <i>type</i> instead of name. Possible values are: <code>ctime</code> (<code>-c</code>), <code>mtime</code> (<code>-t), size</code>, or <code>version</code> (<code>-v). </p>
</dl>
<p> </code></p>
<h2>GRAPHICS OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd> Makes tree not print the indentation lines, useful when used in conjunction with the <code>-f</code> option. Also removes as much whitespace as possible when used with the <code>-J</code> or <code>-x</code> options.</dl>
<dl>
<dt><code>-A</code></p>
<dd> Turn on ANSI line graphics hack when printing the indentation lines.</dl>
<dl>
<dt><code>-S</code></p>
<dd> Turn on CP437 line graphics (useful when using Linux console mode fonts). This option is now equivalent to `&#8211;charset=IBM437&#8242; and may eventually be depreciated.</dl>
<dl>
<dt><code>-n</code></p>
<dd> Turn colorization off always, over-ridden by the <code>-C</code> option, however overrides CLICOLOR_FORCE if present.</dl>
<dl>
<dt><code>-C</code></p>
<dd> Turn colorization on always, using built-in color defaults if the LS_COLORS or TREE_COLORS environment variables are not set. Useful to colorize output to a pipe.</dl>
<h2>XML/JSON/HTML OPTIONS</h2>
<dl>
<dt><code>-X</code></p>
<dd> Turn on XML output. Outputs the directory tree as an XML formatted file.</dl>
<dl>
<dt><code>-J</code></p>
<dd> Turn on JSON output. Outputs the directory tree as a JSON formatted array.</dl>
<dl>
<dt><code>-H </code><i>basehref</i></p>
<dd> Turn on HTML output, including HTTP references. Useful for ftp sites. <i>basehref</i> gives the base ftp location when using HTML output. That is, the local directory may be `/local/ftp/pub&#8217;, but it must be referenced as `<a href="ftp://hostname.organization.domain/pub'">ftp://hostname.organization.domain/pub&#8217;</a> (<i>basehref</i> should be `<a href="ftp://hostname.organization.domain'">ftp://hostname.organization.domain&#8217;</a>). Hint: don&#8217;t use ANSI lines with this option, and don&#8217;t give more than one directory in the directory list. If you wish to use colors via CSS style-sheet, use the -C option in addition to this option to force color output.</dl>
<dl>
<dt><code>-T </code><i>title</i></p>
<dd> Sets the title and H1 header string in HTML output mode.</dl>
<dl>
<dt><code>&#8211;nolinks</code></p>
<dd> Turns off hyperlinks in HTML output.</dl>
<h2>INPUT OPTIONS</h2>
<p> <code>&#8211;fromfile</code> Reads a directory listing from a file rather than the file-system. Paths provided on the command line are files to read from rather than directories to search. The dot (.) directory indicates that tree should read paths from standard input. NOTE: this is only suitable for reading the output of a program such as find, not &#8216;tree -fi&#8217; as symlinks cannot (at least as yet) be distinguished from files that simply contain &#8216; -&gt; &#8216; as part of the filename. </p>
<h2>MISC OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Outputs a verbose usage listing.</dl>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Outputs the version of tree.</dl>
<dl>
<dt><code>&#8212;</code></p>
<dd> Option processing terminator. No further options will be processed after this.</dl>
<h2>.INFO FILES</h2>
<p> <code>.info</code> files are similiar to .gitignore files, if a .info file is found while scanning a directory it is read and added to a stack of .info information. Each file is composed of comments (lines starting with hash marks (#),) or wild-card patterns which may match a file relative to the directory the .info file is found in. If a file should match a pattern, the tab indented comment that follows the pattern is used as the file comment. A comment is terminated by a non-tab indented line. Multiple patterns, each to a line, may share the same comment. </p>
<h2>FILES</h2>
<p> <code>/etc/DIR_COLORS</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>System color database.</p>
<p> <code>~/.dircolors</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Users color database.</p>
<p> <code>.gitignore</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Git exclusion file</p>
<p> <code>$GIT_DIR/info/exclude</code><tt>&nbsp;<wbr>&nbsp;</tt>Global git file exclusion list</p>
<p> <code>.info</code><tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>File comment file</p>
<p> <code>/usr/share/finfo/global_info</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Global file comment file</p>
<h2>ENVIRONMENT</h2>
<p> <code>LS_COLORS</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Color information created by dircolors</p>
<p> <code>TREE_COLORS</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Uses this for color information over LS_COLORS if it is set.</p>
<p> <code>TREE_CHARSET</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Character set for tree to use in HTML mode.</p>
<p> <code>CLICOLOR</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Enables colorization even if TREE_COLORS or LS_COLORS is not set.</p>
<p> <code>CLICOLOR_FORCE</code><tt>&nbsp;</tt>Always enables colorization (effectively -C)</p>
<p> <code>LC_CTYPE</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Locale for filename output.</p>
<p> <code>LC_TIME</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Locale for timefmt output, see <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3).</p>
<p> <code>TZ</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Timezone for timefmt output, see <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3).</p>
<p> <code>STDDATA_FD</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Enable the stddata feature, optionally set descriptor to use.</p>
<h2>AUTHOR</h2>
<p> Steve Baker (ice [at] mama.indstate.edu)<br />
 HTML output hacked by Francesc Rocher (rocher [at] econ.udg.es)<br />
 Charsets and OS/2 support by Kyosuke Tokoro (NBG01720 [at] nifty.ne.jp) </p>
<h2>BUGS AND NOTES</h2>
<p> Tree does not prune &quot;empty&quot; directories when the -P and -I options are used by default. Use the &#8211;prune option. </p>
<p> The -h and &#8211;si options round to the nearest whole number unlike the ls implementations which rounds up always. </p>
<p> Pruning files and directories with the -I, -P and &#8211;filelimit options will lead to incorrect file/directory count reports. </p>
<p> The &#8211;prune and &#8211;du options cause tree to accumulate the entire tree in memory before emitting it. For large directory trees this can cause a significant delay in output and the use of large amounts of memory. </p>
<p> The timefmt expansion buffer is limited to a ridiculously large 255 characters. Output of time strings longer than this will be undefined, but are guaranteed to not exceed 255 characters. </p>
<p> XML/JSON trees are not colored, which is a bit of a shame. </p>
<p> Probably more. </p>
<p> As of version 2.0.0, in Linux, tree will attempt to automatically output a compact JSON tree on file descriptor 3 (what I call stddata,) if present and the environment variable STDDATA_FD is defined or set to a positive non-zero file descriptor value to use to output on. It is hoped that some day a better Linux/Unix shell may take advantage of this feature, though BSON would probably be a better format for this. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dircolors/">dircolors</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-du/">du</a></code>(1), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5) </p>
<h2>Index</h2>
