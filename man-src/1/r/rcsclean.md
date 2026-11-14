---
title: "rcsclean(1)"
name: "rcsclean"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcsclean/"
description: "rcsclean – clean up working files"
---

<h2>NAME</h2>
<p> rcsclean &#8211; clean up working files</p>
<h2>SYNOPSIS</h2>
<p> <code>rcsclean</code> [<i>options</i>] [ <i>file</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>rcsclean</code> removes files that are not being worked on. <code>rcsclean -u</code> also unlocks and removes files that are being worked on but have not changed. </p>
<p> For each <i>file</i> given, <code>rcsclean</code> compares the working file and a revision in the corresponding <font SIZE="-1">RCS</font> file. If it finds a difference, it does nothing. Otherwise, it first unlocks the revision if the <code>-u</code> option is given, and then removes the working file unless the working file is writable and the revision is locked. It logs its actions by outputting the corresponding <code>rcs -u</code> and <code>rm -f</code> commands on the standard output. </p>
<p> Files are paired as explained in <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1). If no <i>file</i> is given, all working files in the current directory are cleaned. Filenames matching an <font SIZE="-1">RCS</font> suffix denote <font SIZE="-1">RCS</font> files; all others denote working files. </p>
<p> The number of the revision to which the working file is compared may be attached to any of the options <code>-n</code>, <code>-q</code>, <code>-r</code>, or <code>-u</code>. If no revision number is specified, then if the <code>-u</code> option is given and the caller has one revision locked, <code>rcsclean</code> uses that revision; otherwise <code>rcsclean</code> uses the latest revision on the default branch, normally the root. </p>
<p> <code>rcsclean</code> is useful for <code>clean</code> targets in makefiles. See also <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), which prints out the differences, and <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), which normally reverts to the previous revision if a file was not changed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code><i>subst</i></p>
<dd> Use <i>subst</i> style keyword substitution when retrieving the revision for comparison. See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details.</p>
<dt><code>-n</code>[<i>rev</i>]</p>
<dd> Do not actually remove any files or unlock any revisions. Using this option will tell you what <code>rcsclean</code> would do without actually doing it.</p>
<dt><code>-q</code>[<i>rev</i>]</p>
<dd> Do not log the actions taken on standard output.</p>
<dt><code>-r</code>[<i>rev</i>]</p>
<dd> This option has no effect other than specifying the revision for comparison.</p>
<dt><code>-T</code></p>
<dd> Preserve the modification time on the <font SIZE="-1">RCS</font> file even if the <font SIZE="-1">RCS</font> file changes because a lock is removed. This option can suppress extensive recompilation caused by a <code><a href="/docs/linux/man/1-make/">make</a></code>(1) dependency of some other copy of the working file on the <font SIZE="-1">RCS</font> file. Use this option with care; it can suppress recompilation even when it is needed, i.e. when the lock removal would mean a change to keyword strings in the other working file.</p>
<dt><code>-u</code>[<i>rev</i>]</p>
<dd> Unlock the revision if it is locked and no difference is found.</p>
<dt><code>-V</code></p>
<dd> Print <font SIZE="-1">RCS</font>&#8216;s version number.</p>
<dt><code>-V</code><i>n</i></p>
<dd> Emulate <font SIZE="-1">RCS</font> version <i>n</i>. See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details.</p>
<dt><code>-x</code><i>suffixes</i></p>
<dd> Use <i>suffixes</i> to characterize <font SIZE="-1">RCS</font> files. See <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) for details.</p>
<dt><code>-z</code><i>zone</i></p>
<dd> Use <i>zone</i> as the time zone for keyword substitution; see <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> <code> rcsclean *.c *.h </code></dl>
<p> removes all working files ending in <code>.c</code> or <code>.h</code> that were not changed since their checkout. </p>
<dl>
<dt>
<dd> <code> rcsclean </code></dl>
<p> removes all working files in the current directory that were not changed since their checkout.</p>
<h2>FILES</h2>
<p> <code>rcsclean</code> accesses files much as <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) does.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>RCSINIT</code></font></p>
<dd> Options prepended to the argument list, separated by spaces. A backslash escapes spaces within an option. The <font SIZE="-1"><code>RCSINIT</code></font> options are prepended to the argument lists of most <font SIZE="-1">RCS</font> commands. Useful <font SIZE="-1"><code>RCSINIT</code></font> options include <code>-q</code>, <code>-V</code>, <code>-x</code>, and <code>-z</code>.</p>
<dt><font SIZE="-1"><code>RCS_MEM_LIMIT</code></font></p>
<dd> An integer <i>lim</i>, measured in kilobytes, specifying the threshold under which commands will try to use memory-based operations for processing the <font SIZE="-1">RCS</font> file. (For <font SIZE="-1">RCS</font> files of size <i>lim</i> kilobytes or greater, RCS will use the slower standard input/output routines.) Default value is 256.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd> Name of the temporary directory. If not set, the environment variables <font SIZE="-1"><code>TMP</code></font> and <font SIZE="-1"><code>TEMP</code></font> are inspected instead and the first value found is taken; if none of them are set, a host-dependent default is used, typically <code>/tmp</code>.</dl>
<h2>DIAGNOSTICS</h2>
<p> The exit status is zero if and only if all operations were successful. Missing working files and <font SIZE="-1">RCS</font> files are silently ignored.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1991, 1992, 1993 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-ident/">ident</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1), <code><a href="/docs/linux/man/5-rcsfile/">rcsfile</a></code>(5). </p>
<p> Walter F. Tichy, <font SIZE="-1">RCS</font>&#8211;A System for Version Control, <i>Software&#8211;Practice &amp; Experience</i> <code>15</code>, 7 (July 1985), 637-654. </p>
<p> The full documentation for <font SIZE="-1">RCS</font> is maintained as a Texinfo manual. If the <code><a href="/docs/linux/man/1-info/">info</a></code>(1) and <font SIZE="-1">RCS</font> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info rcs</code></dl>
<p> should give you access to the complete manual. Additionally, the <font SIZE="-1">RCS</font> homepage:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://www.gnu.org/software/rcs/">http://www.gnu.org/software/rcs/</a></code></dl>
<p> has news and links to the latest release, development site, etc.</p>
<h2>BUGS</h2>
<p> At least one <i>file</i> must be given in older Unix versions that do not provide the needed directory scanning operations. </p>
<h2>Index</h2>
