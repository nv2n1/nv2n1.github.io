---
title: "rcsdiff(1)"
name: "rcsdiff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcsdiff/"
description: "rcsdiff – compare RCS revisions"
---

<h2>NAME</h2>
<p> rcsdiff &#8211; compare RCS revisions</p>
<h2>SYNOPSIS</h2>
<p> <code>rcsdiff</code> [ <code>-k</code><i>subst</i> ] [ <code>-q</code> ] [ <code>-r</code><i>rev1</i> [ <code>-r</code><i>rev2</i> ] ] [ <code>-T</code> ] [ <code>-V</code>[<i>n</i>] ] [ <code>-x</code><i>suffixes</i> ] [ <code>-z</code><i>zone</i> ] [ <i>diff options</i> ] <i>file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>rcsdiff</code> runs <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) to compare two revisions of each <font SIZE="-1">RCS</font> file given. </p>
<p> Filenames matching an <font SIZE="-1">RCS</font> suffix denote <font SIZE="-1">RCS</font> files; all others denote working files. Names are paired as explained in <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1). </p>
<p> The option <code>-q</code> suppresses diagnostic output. Zero, one, or two revisions may be specified with <code>-r</code>. The option <code>-k</code><i>subst</i> affects keyword substitution when extracting revisions, as described in <code><a href="/docs/linux/man/1-co/">co</a></code>(1); for example, <code>-kk -r1.1 -r1.2</code> ignores differences in keyword values when comparing revisions <code>1.1</code> and <code>1.2</code>. To avoid excess output from locker name substitution, <code>-kkvl</code> is assumed if (1) at most one revision option is given, (2) no <code>-k</code> option is given, (3) <code>-kkv</code> is the default keyword substitution, and (4) the working file&#8217;s mode would be produced by <code>co -l.</code> See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details about <code>-T</code>, <code>-V</code>, <code>-x</code> and <code>-z</code>. Otherwise, all options of <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) that apply to regular files are accepted, with the same meaning as for <code>diff</code>. </p>
<p> If both <i>rev1</i> and <i>rev2</i> are omitted, <code>rcsdiff</code> compares the latest revision on the default branch (by default the trunk) with the contents of the corresponding working file. This is useful for determining what you changed since the last checkin. </p>
<p> If <i>rev1</i> is given, but <i>rev2</i> is omitted, <code>rcsdiff</code> compares revision <i>rev1</i> of the <font SIZE="-1">RCS</font> file with the contents of the corresponding working file. </p>
<p> If both <i>rev1</i> and <i>rev2</i> are given, <code>rcsdiff</code> compares revisions <i>rev1</i> and <i>rev2</i> of the <font SIZE="-1">RCS</font> file. </p>
<p> Both <i>rev1</i> and <i>rev2</i> may be given numerically or symbolically.</p>
<h2>EXAMPLE</h2>
<p> The command </p>
<p> <code> rcsdiff f.c</code> </p>
<p> compares the latest revision on the default branch of the <font SIZE="-1">RCS</font> file to the contents of the working file <code>f.c</code>.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>RCSINIT</code></font></p>
<dd> Options prepended to the argument list, separated by spaces. A backslash escapes spaces within an option. The <font SIZE="-1"><code>RCSINIT</code></font> options are prepended to the argument lists of most <font SIZE="-1">RCS</font> commands. Useful <font SIZE="-1"><code>RCSINIT</code></font> options include <code>-q</code>, <code>-V</code>, <code>-x</code>, and <code>-z</code>.</p>
<dt><font SIZE="-1"><code>RCS_MEM_LIMIT</code></font></p>
<dd> An integer <i>lim</i>, measured in kilobytes, specifying the threshold under which commands will try to use memory-based operations for processing the <font SIZE="-1">RCS</font> file. (For <font SIZE="-1">RCS</font> files of size <i>lim</i> kilobytes or greater, RCS will use the slower standard input/output routines.) Default value is 256.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd> Name of the temporary directory. If not set, the environment variables <font SIZE="-1"><code>TMP</code></font> and <font SIZE="-1"><code>TEMP</code></font> are inspected instead and the first value found is taken; if none of them are set, a host-dependent default is used, typically <code>/tmp</code>.</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is 0 for no differences during any comparison, 1 for some differences, 2 for trouble.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1991, 1992, 1993 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/1-ident/">ident</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1). </p>
<p> Walter F. Tichy, <font SIZE="-1">RCS</font>&#8211;A System for Version Control, <i>Software&#8211;Practice &amp; Experience</i> <code>15</code>, 7 (July 1985), 637-654. </p>
<p> The full documentation for <font SIZE="-1">RCS</font> is maintained as a Texinfo manual. If the <code><a href="/docs/linux/man/1-info/">info</a></code>(1) and <font SIZE="-1">RCS</font> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info rcs</code></dl>
<p> should give you access to the complete manual. Additionally, the <font SIZE="-1">RCS</font> homepage:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://www.gnu.org/software/rcs/">http://www.gnu.org/software/rcs/</a></code></dl>
<p> has news and links to the latest release, development site, etc. </p>
<h2>Index</h2>
