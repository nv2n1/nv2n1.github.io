---
title: "rcsmerge(1)"
name: "rcsmerge"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcsmerge/"
description: "rcsmerge – merge RCS revisions"
---

<h2>NAME</h2>
<p> rcsmerge &#8211; merge RCS revisions</p>
<h2>SYNOPSIS</h2>
<p> <code>rcsmerge</code> [<i>options</i>]<i> file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>rcsmerge</code> incorporates the changes between two revisions of an <font SIZE="-1">RCS</font> file into the corresponding working file. </p>
<p> Filenames matching an <font SIZE="-1">RCS</font> suffix denote <font SIZE="-1">RCS</font> files; all others denote working files. Names are paired as explained in <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1). </p>
<p> At least one revision must be specified with one of the options described below, usually <code>-r</code>. At most two revisions may be specified. If only one revision is specified, the latest revision on the default branch (normally the highest branch on the trunk) is assumed for the second revision. Revisions may be specified numerically or symbolically. </p>
<p> <code>rcsmerge</code> prints a warning if there are overlaps, and delimits the overlapping regions as explained in <code><a href="/docs/linux/man/1-merge/">merge</a></code>(1). The command is useful for incorporating changes into a checked-out revision.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Output conflicts using the <code>-A</code> style of <code><a href="/docs/linux/man/1-diff3/">diff3</a></code>(1), if supported by <code>diff3</code>. This merges all changes leading from <i>file2</i> to <i>file3</i> into <i>file1</i>, and generates the most verbose output.</p>
<dt><code>-E</code>, <code>-e</code></p>
<dd> These options specify conflict styles that generate less information than <code>-A</code>. See <code><a href="/docs/linux/man/1-diff3/">diff3</a></code>(1) for details. The default is <code>-E</code>. With <code>-e</code>, <code>rcsmerge</code> does not warn about conflicts.</p>
<dt><code>-k</code><i>subst</i></p>
<dd> Use <i>subst</i> style keyword substitution. See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details. For example, <code>-kk -r1.1 -r1.2</code> ignores differences in keyword values when merging the changes from <code>1.1</code> to <code>1.2</code>. It normally does not make sense to merge binary files as if they were text, so <code>rcsmerge</code> refuses to merge files if <code>-kb</code> expansion is used.</p>
<dt><code>-p</code>[<i>rev</i>]</p>
<dd> Send the result to standard output instead of overwriting the working file.</p>
<dt><code>-q</code>[<i>rev</i>]</p>
<dd> Run quietly; do not print diagnostics.</p>
<dt><code>-r</code>[<i>rev</i>]</p>
<dd> Merge with respect to revision <i>rev</i>. Here an empty <i>rev</i> stands for the latest revision on the default branch, normally the head.</p>
<dt><code>-T</code></p>
<dd> This option has no effect; it is present for compatibility with other <font SIZE="-1">RCS</font> commands.</p>
<dt><code>-V</code></p>
<dd> Print <font SIZE="-1">RCS</font>&#8216;s version number.</p>
<dt><code>-V</code><i>n</i></p>
<dd> Emulate <font SIZE="-1">RCS</font> version <i>n</i>. See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details.</p>
<dt><code>-x</code><i>suffixes</i></p>
<dd> Use <i>suffixes</i> to characterize <font SIZE="-1">RCS</font> files. See <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) for details.</p>
<dt><code>-z</code><i>zone</i></p>
<dd> Use <i>zone</i> as the time zone for keyword substitution. See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details.</dl>
<h2>EXAMPLES</h2>
<p> Suppose you have released revision 2.8 of <code>f.c</code>. Assume furthermore that after you complete an unreleased revision 3.4, you receive updates to release 2.8 from someone else. To combine the updates to 2.8 and your changes between 2.8 and 3.4, put the updates to 2.8 into file f.c and execute </p>
<p> <code> rcsmerge -p -r2.8 -r3.4 f.c &gt;f.merged.c</code> </p>
<p> Then examine <code>f.merged.c</code>. Alternatively, if you want to save the updates to 2.8 in the <font SIZE="-1">RCS</font> file, check them in as revision 2.8.1.1 and execute <code>co -j:</code> </p>
<p> <code> ci -r2.8.1.1 f.c</code><br />
 <code> co -r3.4 -j2.8:2.8.1.1 f.c</code> </p>
<p> As another example, the following command undoes the changes between revision 2.4 and 2.8 in your currently checked out revision in <code>f.c</code>. </p>
<p> <code> rcsmerge -r2.8 -r2.4 f.c</code> </p>
<p> Note the order of the arguments, and that <code>f.c</code> will be overwritten.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>RCSINIT</code></font></p>
<dd> Options prepended to the argument list, separated by spaces. A backslash escapes spaces within an option. The <font SIZE="-1"><code>RCSINIT</code></font> options are prepended to the argument lists of most <font SIZE="-1">RCS</font> commands. Useful <font SIZE="-1"><code>RCSINIT</code></font> options include <code>-q</code>, <code>-V</code>, <code>-x</code>, and <code>-z</code>.</p>
<dt><font SIZE="-1"><code>RCS_MEM_LIMIT</code></font></p>
<dd> An integer <i>lim</i>, measured in kilobytes, specifying the threshold under which commands will try to use memory-based operations for processing the <font SIZE="-1">RCS</font> file. (For <font SIZE="-1">RCS</font> files of size <i>lim</i> kilobytes or greater, RCS will use the slower standard input/output routines.) Default value is 256.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd> Name of the temporary directory. If not set, the environment variables <font SIZE="-1"><code>TMP</code></font> and <font SIZE="-1"><code>TEMP</code></font> are inspected instead and the first value found is taken; if none of them are set, a host-dependent default is used, typically <code>/tmp</code>.</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is 0 for no overlaps, 1 for some overlaps, 2 for trouble.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1991, 1992, 1993, 1994, 1995 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-ident/">ident</a></code>(1), <code><a href="/docs/linux/man/1-merge/">merge</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1), <code><a href="/docs/linux/man/5-rcsfile/">rcsfile</a></code>(5). </p>
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
