---

title: "vdir(1)"
name: "vdir"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vdir/"
description: "vdir – list directory contents"
---

<p> vdir &#8211; list directory contents </p>
<h2>SYNOPSIS</h2>
<p> <code>vdir</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> List information about the FILEs (the current directory by default). Sort entries alphabetically if none of <code>-cftuvSUX</code> nor <code>&#8211;sort</code> is specified. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> do not ignore entries starting with .</dd>
<dt><code>-A</code>, <code>&#8211;almost-all</code></dt>
<dd> do not list implied . and ..</dd>
<dt><code>&#8211;author</code></dt>
<dd> with <code>-l</code>, print the author of each file</dd>
<dt><code>-b</code>, <code>&#8211;escape</code></dt>
<dd> print C-style escapes for nongraphic characters</dd>
<dt><code>&#8211;block-size</code>=<i>,SIZE/</i></dt>
<dd> with <code>-l</code>, scale sizes by SIZE when printing them; e.g., &#8216;&#8211;block-size=M&#8217;; see SIZE format below</dd>
<dt><code>-B</code>, <code>&#8211;ignore-backups</code></dt>
<dd> do not list implied entries ending with ~</dd>
<dt><code>-c</code></dt>
<dd> with <code>-lt</code>: sort by, and show, ctime (time of last modification of file status information); with <code>-l</code>: show ctime and sort by name; otherwise: sort by ctime, newest first</dd>
<dt><code>-C</code></dt>
<dd> list entries by columns</dd>
<dt><code>&#8211;color</code>[=<i>,WHEN/</i>]</dt>
<dd> colorize the output; WHEN can be &#8216;always&#8217; (default if omitted), &#8216;auto&#8217;, or &#8216;never&#8217;; more info below</dd>
<dt><code>-d</code>, <code>&#8211;directory</code></dt>
<dd> list directories themselves, not their contents</dd>
<dt><code>-D</code>, <code>&#8211;dired</code></dt>
<dd> generate output designed for Emacs&#8217; dired mode</dd>
<dt><code>-f</code></dt>
<dd> do not sort, enable <code>-aU</code>, disable <code>-ls</code> <code>&#8211;color</code></dd>
<dt><code>-F</code>, <code>&#8211;classify</code></dt>
<dd> append indicator (one of */=&gt;@|) to entries</dd>
<dt><code>&#8211;file-type</code></dt>
<dd> likewise, except do not append &#8216;*&#8217;</dd>
<dt><code>&#8211;format</code>=<i>,WORD/</i></dt>
<dd> across <code>-x</code>, commas <code>-m</code>, horizontal <code>-x</code>, long <code>-l</code>, single-column <code>-1</code>, verbose <code>-l</code>, vertical <code>-C</code></dd>
<dt><code>&#8211;full-time</code></dt>
<dd> like <code>-l</code> <code>&#8211;time-style</code>=<i>,full-iso/</i></dd>
<dt><code>-g</code></dt>
<dd> like <code>-l</code>, but do not list owner</dd>
<dt><code>&#8211;group-directories-first</code></dt>
<dd> group directories before files;</dd>
<dt>
</dt><dd> can be augmented with a <code>&#8211;sort</code> option, but any use of <code>&#8211;sort</code>=<i>,none/</i> (<code>-U</code>) disables grouping</dd>
<dt><code>-G</code>, <code>&#8211;no-group</code></dt>
<dd> in a long listing, don&#8217;t print group names</dd>
<dt><code>-h</code>, <code>&#8211;human-readable</code></dt>
<dd> with <code>-l</code> and <code>-s</code>, print sizes like 1K 234M 2G etc.</dd>
<dt><code>&#8211;si</code></dt>
<dd> likewise, but use powers of 1000 not 1024</dd>
<dt><code>-H</code>, <code>&#8211;dereference-command-line</code></dt>
<dd> follow symbolic links listed on the command line</dd>
<dt><code>&#8211;dereference-command-line-symlink-to-dir</code></dt>
<dd> follow each command line symbolic link</dd>
<dt>
</dt><dd> that points to a directory</dd>
<dt><code>&#8211;hide</code>=<i>,PATTERN/</i></dt>
<dd> do not list implied entries matching shell PATTERN (overridden by <code>-a</code> or <code>-A</code>)</dd>
<dt><code>&#8211;hyperlink</code>[=<i>,WHEN/</i>]</dt>
<dd> hyperlink file names; WHEN can be &#8216;always&#8217; (default if omitted), &#8216;auto&#8217;, or &#8216;never&#8217;</dd>
<dt><code>&#8211;indicator-style</code>=<i>,WORD/</i></dt>
<dd> append indicator with style WORD to entry names: none (default), slash (<code>-p</code>), file-type (<code>&#8211;file-type</code>), classify (<code>-F</code>)</dd>
<dt><code>-i</code>, <code>&#8211;inode</code></dt>
<dd> print the index number of each file</dd>
<dt><code>-I</code>, <code>&#8211;ignore</code>=<i>,PATTERN/</i></dt>
<dd> do not list implied entries matching shell PATTERN</dd>
<dt><code>-k</code>, <code>&#8211;kibibytes</code></dt>
<dd> default to 1024-byte blocks for disk usage; used only with <code>-s</code> and per directory totals</dd>
<dt><code>-l</code></dt>
<dd> use a long listing format</dd>
<dt><code>-L</code>, <code>&#8211;dereference</code></dt>
<dd> when showing file information for a symbolic link, show information for the file the link references rather than for the link itself</dd>
<dt><code>-m</code></dt>
<dd> fill width with a comma separated list of entries</dd>
<dt><code>-n</code>, <code>&#8211;numeric-uid-gid</code></dt>
<dd> like <code>-l</code>, but list numeric user and group IDs</dd>
<dt><code>-N</code>, <code>&#8211;literal</code></dt>
<dd> print entry names without quoting</dd>
<dt><code>-o</code></dt>
<dd> like <code>-l</code>, but do not list group information</dd>
<dt><code>-p</code>, <code>&#8211;indicator-style</code>=<i>,slash/</i></dt>
<dd> append / indicator to directories</dd>
<dt><code>-q</code>, <code>&#8211;hide-control-chars</code></dt>
<dd> print ? instead of nongraphic characters</dd>
<dt><code>&#8211;show-control-chars</code></dt>
<dd> show nongraphic characters as-is (the default, unless program is &#8216;ls&#8217; and output is a terminal)</dd>
<dt><code>-Q</code>, <code>&#8211;quote-name</code></dt>
<dd> enclose entry names in double quotes</dd>
<dt><code>&#8211;quoting-style</code>=<i>,WORD/</i></dt>
<dd> use quoting style WORD for entry names: literal, locale, shell, shell-always, shell-escape, shell-escape-always, c, escape (overrides QUOTING_STYLE environment variable)</dd>
<dt><code>-r</code>, <code>&#8211;reverse</code></dt>
<dd> reverse order while sorting</dd>
<dt><code>-R</code>, <code>&#8211;recursive</code></dt>
<dd> list subdirectories recursively</dd>
<dt><code>-s</code>, <code>&#8211;size</code></dt>
<dd> print the allocated size of each file, in blocks</dd>
<dt><code>-S</code></dt>
<dd> sort by file size, largest first</dd>
<dt><code>&#8211;sort</code>=<i>,WORD/</i></dt>
<dd> sort by WORD instead of name: none (<code>-U</code>), size (<code>-S</code>), time (<code>-t</code>), version (<code>-v</code>), extension (<code>-X</code>)</dd>
<dt><code>&#8211;time</code>=<i>,WORD/</i></dt>
<dd> change the default of using modification times; access time (<code>-u</code>): atime, access, use; change time (<code>-c</code>): ctime, status; birth time: birth, creation;</dd>
<dt>
</dt><dd> with <code>-l</code>, WORD determines which time to show; with <code>&#8211;sort</code>=<i>,time/</i>, sort by WORD (newest first)</dd>
<dt><code>&#8211;time-style</code>=<i>,TIME_STYLE/</i></dt>
<dd> time/date format with <code>-l</code>; see TIME_STYLE below</dd>
<dt><code>-t</code></dt>
<dd> sort by time, newest first; see <code>&#8211;time</code></dd>
<dt><code>-T</code>, <code>&#8211;tabsize</code>=<i>,COLS/</i></dt>
<dd> assume tab stops at each COLS instead of 8</dd>
<dt><code>-u</code></dt>
<dd> with <code>-lt</code>: sort by, and show, access time; with <code>-l</code>: show access time and sort by name; otherwise: sort by access time, newest first</dd>
<dt><code>-U</code></dt>
<dd> do not sort; list entries in directory order</dd>
<dt><code>-v</code></dt>
<dd> natural sort of (version) numbers within text</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>,COLS/</i></dt>
<dd> set output width to COLS. 0 means no limit</dd>
<dt><code>-x</code></dt>
<dd> list entries by lines instead of by columns</dd>
<dt><code>-X</code></dt>
<dd> sort alphabetically by entry extension</dd>
<dt><code>-Z</code>, <code>&#8211;context</code></dt>
<dd> print any security context of each file</dd>
<dt><code>-1</code></dt>
<dd> list one file per line. Avoid &#8216;
&#8217; with <code>-q</code> or <code>-b</code></dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> The SIZE argument is an integer and optional unit (example: 10K is 10*1024). Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,&#8230; (powers of 1000). Binary prefixes can be used, too: KiB=K, MiB=M, and so on. </p>
<p> The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT. FORMAT is interpreted like in <a href="/docs/linux/man/1-date/">date</a>(1). If FORMAT is FORMAT1&lt;newline&gt;FORMAT2, then FORMAT1 applies to non-recent files and FORMAT2 to recent files. TIME_STYLE prefixed with &#8216;posix-&#8216; takes effect only outside the POSIX locale. Also the TIME_STYLE environment variable sets the default style to use. </p>
<p> Using color to distinguish file types is disabled both by default and with <code>&#8211;color</code>=<i>,never/</i>. With <code>&#8211;color</code>=<i>,auto/</i>, ls emits color codes only when standard output is connected to a terminal. The LS_COLORS environment variable can change the settings. Use the dircolors command to set it.</p>
<h3>Exit status:</h3>
<dl>
<dt>0</dt>
<dd> if OK,</dd>
<dt>1</dt>
<dd> if minor problems (e.g., cannot access subdirectory),</dd>
<dt>2</dt>
<dd> if serious trouble (e.g., cannot access command-line argument).</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Richard M. Stallman and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br/>
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/vdir">https://www.gnu.org/software/coreutils/vdir</a>&gt;<br/>
 or available locally via: info &#8216;(coreutils) vdir invocation&#8217; </p>
