---
title: "vdir(1)"
name: "vdir"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vdir/"
description: "vdir – list directory contents"
---

<h2 class="name">NAME</h2>
<p> vdir &#8211; list directory contents </p>
<h2>SYNOPSIS</h2>
<p> <code>vdir</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> List information about the FILEs (the current directory by default). Sort entries alphabetically if none of <code>-cftuvSUX</code> nor <code>&#8211;sort</code> is specified. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> do not ignore entries starting with .</p>
<dt><code>-A</code>, <code>&#8211;almost-all</code></p>
<dd> do not list implied . and ..</p>
<dt><code>&#8211;author</code></p>
<dd> with <code>-l</code>, print the author of each file</p>
<dt><code>-b</code>, <code>&#8211;escape</code></p>
<dd> print C-style escapes for nongraphic characters</p>
<dt><code>&#8211;block-size</code>=<i>,SIZE/</i></p>
<dd> with <code>-l</code>, scale sizes by SIZE when printing them; e.g., &#8216;&#8211;block-size=M&#8217;; see SIZE format below</p>
<dt><code>-B</code>, <code>&#8211;ignore-backups</code></p>
<dd> do not list implied entries ending with ~</p>
<dt><code>-c</code></p>
<dd> with <code>-lt</code>: sort by, and show, ctime (time of last modification of file status information); with <code>-l</code>: show ctime and sort by name; otherwise: sort by ctime, newest first</p>
<dt><code>-C</code></p>
<dd> list entries by columns</p>
<dt><code>&#8211;color</code>[=<i>,WHEN/</i>]</p>
<dd> colorize the output; WHEN can be &#8216;always&#8217; (default if omitted), &#8216;auto&#8217;, or &#8216;never&#8217;; more info below</p>
<dt><code>-d</code>, <code>&#8211;directory</code></p>
<dd> list directories themselves, not their contents</p>
<dt><code>-D</code>, <code>&#8211;dired</code></p>
<dd> generate output designed for Emacs&#8217; dired mode</p>
<dt><code>-f</code></p>
<dd> do not sort, enable <code>-aU</code>, disable <code>-ls</code> <code>&#8211;color</code></p>
<dt><code>-F</code>, <code>&#8211;classify</code></p>
<dd> append indicator (one of */=&gt;@|) to entries</p>
<dt><code>&#8211;file-type</code></p>
<dd> likewise, except do not append &#8216;*&#8217;</p>
<dt><code>&#8211;format</code>=<i>,WORD/</i></p>
<dd> across <code>-x</code>, commas <code>-m</code>, horizontal <code>-x</code>, long <code>-l</code>, single-column <code>-1</code>, verbose <code>-l</code>, vertical <code>-C</code></p>
<dt><code>&#8211;full-time</code></p>
<dd> like <code>-l</code> <code>&#8211;time-style</code>=<i>,full-iso/</i></p>
<dt><code>-g</code></p>
<dd> like <code>-l</code>, but do not list owner</p>
<dt><code>&#8211;group-directories-first</code></p>
<dd> group directories before files;</p>
<dt>
<dd> can be augmented with a <code>&#8211;sort</code> option, but any use of <code>&#8211;sort</code>=<i>,none/</i> (<code>-U</code>) disables grouping</p>
<dt><code>-G</code>, <code>&#8211;no-group</code></p>
<dd> in a long listing, don&#8217;t print group names</p>
<dt><code>-h</code>, <code>&#8211;human-readable</code></p>
<dd> with <code>-l</code> and <code>-s</code>, print sizes like 1K 234M 2G etc.</p>
<dt><code>&#8211;si</code></p>
<dd> likewise, but use powers of 1000 not 1024</p>
<dt><code>-H</code>, <code>&#8211;dereference-command-line</code></p>
<dd> follow symbolic links listed on the command line</p>
<dt><code>&#8211;dereference-command-line-symlink-to-dir</code></p>
<dd> follow each command line symbolic link</p>
<dt>
<dd> that points to a directory</p>
<dt><code>&#8211;hide</code>=<i>,PATTERN/</i></p>
<dd> do not list implied entries matching shell PATTERN (overridden by <code>-a</code> or <code>-A</code>)</p>
<dt><code>&#8211;hyperlink</code>[=<i>,WHEN/</i>]</p>
<dd> hyperlink file names; WHEN can be &#8216;always&#8217; (default if omitted), &#8216;auto&#8217;, or &#8216;never&#8217;</p>
<dt><code>&#8211;indicator-style</code>=<i>,WORD/</i></p>
<dd> append indicator with style WORD to entry names: none (default), slash (<code>-p</code>), file-type (<code>&#8211;file-type</code>), classify (<code>-F</code>)</p>
<dt><code>-i</code>, <code>&#8211;inode</code></p>
<dd> print the index number of each file</p>
<dt><code>-I</code>, <code>&#8211;ignore</code>=<i>,PATTERN/</i></p>
<dd> do not list implied entries matching shell PATTERN</p>
<dt><code>-k</code>, <code>&#8211;kibibytes</code></p>
<dd> default to 1024-byte blocks for disk usage; used only with <code>-s</code> and per directory totals</p>
<dt><code>-l</code></p>
<dd> use a long listing format</p>
<dt><code>-L</code>, <code>&#8211;dereference</code></p>
<dd> when showing file information for a symbolic link, show information for the file the link references rather than for the link itself</p>
<dt><code>-m</code></p>
<dd> fill width with a comma separated list of entries</p>
<dt><code>-n</code>, <code>&#8211;numeric-uid-gid</code></p>
<dd> like <code>-l</code>, but list numeric user and group IDs</p>
<dt><code>-N</code>, <code>&#8211;literal</code></p>
<dd> print entry names without quoting</p>
<dt><code>-o</code></p>
<dd> like <code>-l</code>, but do not list group information</p>
<dt><code>-p</code>, <code>&#8211;indicator-style</code>=<i>,slash/</i></p>
<dd> append / indicator to directories</p>
<dt><code>-q</code>, <code>&#8211;hide-control-chars</code></p>
<dd> print ? instead of nongraphic characters</p>
<dt><code>&#8211;show-control-chars</code></p>
<dd> show nongraphic characters as-is (the default, unless program is &#8216;ls&#8217; and output is a terminal)</p>
<dt><code>-Q</code>, <code>&#8211;quote-name</code></p>
<dd> enclose entry names in double quotes</p>
<dt><code>&#8211;quoting-style</code>=<i>,WORD/</i></p>
<dd> use quoting style WORD for entry names: literal, locale, shell, shell-always, shell-escape, shell-escape-always, c, escape (overrides QUOTING_STYLE environment variable)</p>
<dt><code>-r</code>, <code>&#8211;reverse</code></p>
<dd> reverse order while sorting</p>
<dt><code>-R</code>, <code>&#8211;recursive</code></p>
<dd> list subdirectories recursively</p>
<dt><code>-s</code>, <code>&#8211;size</code></p>
<dd> print the allocated size of each file, in blocks</p>
<dt><code>-S</code></p>
<dd> sort by file size, largest first</p>
<dt><code>&#8211;sort</code>=<i>,WORD/</i></p>
<dd> sort by WORD instead of name: none (<code>-U</code>), size (<code>-S</code>), time (<code>-t</code>), version (<code>-v</code>), extension (<code>-X</code>)</p>
<dt><code>&#8211;time</code>=<i>,WORD/</i></p>
<dd> change the default of using modification times; access time (<code>-u</code>): atime, access, use; change time (<code>-c</code>): ctime, status; birth time: birth, creation;</p>
<dt>
<dd> with <code>-l</code>, WORD determines which time to show; with <code>&#8211;sort</code>=<i>,time/</i>, sort by WORD (newest first)</p>
<dt><code>&#8211;time-style</code>=<i>,TIME_STYLE/</i></p>
<dd> time/date format with <code>-l</code>; see TIME_STYLE below</p>
<dt><code>-t</code></p>
<dd> sort by time, newest first; see <code>&#8211;time</code></p>
<dt><code>-T</code>, <code>&#8211;tabsize</code>=<i>,COLS/</i></p>
<dd> assume tab stops at each COLS instead of 8</p>
<dt><code>-u</code></p>
<dd> with <code>-lt</code>: sort by, and show, access time; with <code>-l</code>: show access time and sort by name; otherwise: sort by access time, newest first</p>
<dt><code>-U</code></p>
<dd> do not sort; list entries in directory order</p>
<dt><code>-v</code></p>
<dd> natural sort of (version) numbers within text</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>,COLS/</i></p>
<dd> set output width to COLS. 0 means no limit</p>
<dt><code>-x</code></p>
<dd> list entries by lines instead of by columns</p>
<dt><code>-X</code></p>
<dd> sort alphabetically by entry extension</p>
<dt><code>-Z</code>, <code>&#8211;context</code></p>
<dd> print any security context of each file</p>
<dt><code>-1</code></p>
<dd> list one file per line. Avoid &#8216;
&#8217; with <code>-q</code> or <code>-b</code></p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> The SIZE argument is an integer and optional unit (example: 10K is 10*1024). Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,&#8230; (powers of 1000). Binary prefixes can be used, too: KiB=K, MiB=M, and so on. </p>
<p> The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT. FORMAT is interpreted like in <a href="/docs/linux/man/1-date/">date</a>(1). If FORMAT is FORMAT1&lt;newline&gt;FORMAT2, then FORMAT1 applies to non-recent files and FORMAT2 to recent files. TIME_STYLE prefixed with &#8216;posix-&#8216; takes effect only outside the POSIX locale. Also the TIME_STYLE environment variable sets the default style to use. </p>
<p> Using color to distinguish file types is disabled both by default and with <code>&#8211;color</code>=<i>,never/</i>. With <code>&#8211;color</code>=<i>,auto/</i>, ls emits color codes only when standard output is connected to a terminal. The LS_COLORS environment variable can change the settings. Use the dircolors command to set it.</p>
<h3>Exit status:</h3>
<dl>
<dt>0</p>
<dd> if OK,</p>
<dt>1</p>
<dd> if minor problems (e.g., cannot access subdirectory),</p>
<dt>2</p>
<dd> if serious trouble (e.g., cannot access command-line argument).</dl>
<h2>AUTHOR</h2>
<p> Written by Richard M. Stallman and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/vdir">https://www.gnu.org/software/coreutils/vdir</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) vdir invocation&#8217; </p>
<h2>Index</h2>
