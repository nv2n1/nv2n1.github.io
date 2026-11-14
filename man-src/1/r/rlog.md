---
title: "rlog(1)"
name: "rlog"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rlog/"
description: "rlog – print log messages and other information about RCS files"
---

<h2>NAME</h2>
<p> rlog &#8211; print log messages and other information about <font SIZE="-1">RCS</font> files</p>
<h2>SYNOPSIS</h2>
<p> <code>rlog</code> [<i> options </i>]<i> file </i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>rlog</code> prints information about <font SIZE="-1">RCS</font> files. </p>
<p> Filenames matching an <font SIZE="-1">RCS</font> suffix denote <font SIZE="-1">RCS</font> files; all others denote working files. Names are paired as explained in <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1). </p>
<p> <code>rlog</code> prints the following information for each <font SIZE="-1">RCS</font> file: <font SIZE="-1">RCS</font> file name, working file name, head (i.e., the number of the latest revision on the trunk), default branch, access list, locks, symbolic names, suffix, total number of revisions, number of revisions selected for printing, and descriptive text. This is followed by entries for the selected revisions in reverse chronological order for each branch. For each revision, <code>rlog</code> prints revision number, author, date/time, state, number of lines added/deleted (with respect to the previous revision), locker of the revision (if any), and log message. All times are displayed in Coordinated Universal Time (<font SIZE="-1">UTC</font>) by default; this can be overridden with <code>-z</code>. Without options, <code>rlog</code> prints complete information. The options below restrict this output.</p>
<dl>
<dt><code>-L</code></p>
<dd> Ignore <font SIZE="-1">RCS</font> files that have no locks set. This is convenient in combination with <code>-h</code>, <code>-l</code>, and <code>-R</code>.</p>
<dt><code>-R</code></p>
<dd> Print only the name of the <font SIZE="-1">RCS</font> file. This is convenient for translating a working file name into an <font SIZE="-1">RCS</font> file name.</p>
<dt><code>-h</code></p>
<dd> Print only the <font SIZE="-1">RCS</font> file name, working file name, head, default branch, access list, locks, symbolic names, and suffix.</p>
<dt><code>-t</code></p>
<dd> Print the same as <code>-h</code>, plus the descriptive text.</p>
<dt><code>-N</code></p>
<dd> Do not print the symbolic names.</p>
<dt><code>-b</code></p>
<dd> Print information about the revisions on the default branch, normally the highest branch on the trunk.</p>
<dt><code>-d</code><i>dates</i></p>
<dd> Print information about revisions with a checkin date/time in the ranges given by the semicolon-separated list of <i>dates</i>. A range of the form <i>d1</i><code>&lt;</code><i>d2</i> or <i>d2</i><code>&gt;</code><i>d1</i> selects the revisions that were deposited between <i>d1</i> and <i>d2</i> exclusive. A range of the form <code>&lt;</code><i>d</i> or <i>d</i><code>&gt;</code> selects all revisions earlier than <i>d</i>. A range of the form <i>d</i><code>&lt;</code> or <code>&gt;</code><i>d</i> selects all revisions dated later than <i>d</i>. If <code>&lt;</code> or <code>&gt;</code> is followed by <code>=</code> then the ranges are inclusive, not exclusive. A range of the form <i>d</i> selects the single, latest revision dated <i>d</i> or earlier. The date/time strings <i>d</i>, <i>d1</i>, and <i>d2</i> are in the free format explained in <code><a href="/docs/linux/man/1-co/">co</a></code>(1). Quoting is normally necessary, especially for <code>&lt;</code> and <code>&gt;</code>. Note that the separator is a semicolon.</p>
<dt><code>-l</code>[<i>lockers</i>]</p>
<dd> Print information about locked revisions only. In addition, if the comma-separated list <i>lockers</i> of login names is given, ignore all locks other than those held by the <i>lockers</i>. For example, <code>rlog -L -R -lwft RCS/*</code> prints the name of <font SIZE="-1">RCS</font> files locked by the user <code>wft</code>.</p>
<dt><code>-r</code>[<i>revisions</i>]</p>
<dd> prints information about revisions given in the comma-separated list <i>revisions</i> of revisions and ranges. A range <i>rev1</i><code>:</code><i>rev2</i> means revisions <i>rev1</i> to <i>rev2</i> on the same branch, <code>:</code><i>rev</i> means revisions from the beginning of the branch up to and including <i>rev</i>, and <i>rev</i><code>:</code> means revisions starting with <i>rev</i> to the end of the branch containing <i>rev</i>. An argument that is a branch means all revisions on that branch. A range of branches means all revisions on the branches in that range. A branch followed by a <code>.</code> means the latest revision in that branch. A bare <code>-r</code> with no <i>revisions</i> means the latest revision on the default branch, normally the trunk.</p>
<dt><code>-s</code><i>states</i></p>
<dd> prints information about revisions whose state attributes match one of the states given in the comma-separated list <i>states</i>.</p>
<dt><code>-w</code>[<i>logins</i>]</p>
<dd> prints information about revisions checked in by users with login names appearing in the comma-separated list <i>logins</i>. If <i>logins</i> is omitted, the user&#8217;s login is assumed.</p>
<dt><code>-q</code></p>
<dd> This option has no effect; it is provided for consistency with other commands.</p>
<dt><code>-T</code></p>
<dd> This option has no effect; it is present for compatibility with other <font SIZE="-1">RCS</font> commands.</p>
<dt><code>-V</code></p>
<dd> Print <font SIZE="-1">RCS</font>&#8216;s version number.</p>
<dt><code>-V</code><i>n</i></p>
<dd> Emulate <font SIZE="-1">RCS</font> version <i>n</i> when generating logs. See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for more.</p>
<dt><code>-x</code><i>suffixes</i></p>
<dd> Use <i>suffixes</i> to characterize <font SIZE="-1">RCS</font> files. See <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) for details.</dl>
<p> <code>rlog</code> prints the intersection of the revisions selected with the options <code>-d</code>, <code>-l</code>, <code>-s</code>, and <code>-w</code>, intersected with the union of the revisions selected by <code>-b</code> and <code>-r</code>.</p>
<dl>
<dt><code>-z</code><i>zone</i></p>
<dd> specifies the date output format, and specifies the default time zone for <i>date</i> in the <code>-d</code><i>dates</i> option. The <i>zone</i> should be empty, a numeric <font SIZE="-1">UTC</font> offset, or the special string <code>LT</code> for local time. The default is an empty <i>zone</i>, which uses the traditional <font SIZE="-1">RCS</font> format of <font SIZE="-1">UTC</font> without any time zone indication and with slashes separating the parts of the date; otherwise, times are output in <font SIZE="-1">ISO</font> 8601 format with time zone indication. For example, if local time is January 11, 1990, 8pm Pacific Standard Time, eight hours west of <font SIZE="-1">UTC</font>, then the time is output as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<i>option</i>      <i>time output</i>
<code>-z</code>          <code>1990/01/12 04:00:00</code>          <i>(default)</i>
<code>-zLT</code>        <code>1990-01-11 20:00:00-08</code>
<code>-z+05:30</code>    <code>1990-01-12 09:30:00+05:30</code>
</pre>
</dl>
</dl>
</dl>
<h2>EXAMPLES</h2>
<pre>
<code>    rlog  -L  -R  RCS/*</code>
<code>    rlog  -L  -h  RCS/*</code>
<code>    rlog  -L  -l  RCS/*</code>
<code>    rlog  RCS/*</code>
</pre>
<p> The first command prints the names of all <font SIZE="-1">RCS</font> files in the subdirectory <code>RCS</code> that have locks. The second command prints the headers of those files, and the third prints the headers plus the log messages of the locked revisions. The last command prints complete information.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>RCSINIT</code></font></p>
<dd> Options prepended to the argument list, separated by spaces. A backslash escapes spaces within an option. The <font SIZE="-1"><code>RCSINIT</code></font> options are prepended to the argument lists of most <font SIZE="-1">RCS</font> commands. Useful <font SIZE="-1"><code>RCSINIT</code></font> options include <code>-q</code>, <code>-V</code>, <code>-x</code>, and <code>-z</code>.</p>
<dt><font SIZE="-1"><code>RCS_MEM_LIMIT</code></font></p>
<dd> An integer <i>lim</i>, measured in kilobytes, specifying the threshold under which commands will try to use memory-based operations for processing the <font SIZE="-1">RCS</font> file. (For <font SIZE="-1">RCS</font> files of size <i>lim</i> kilobytes or greater, RCS will use the slower standard input/output routines.) Default value is 256.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd> Name of the temporary directory. If not set, the environment variables <font SIZE="-1"><code>TMP</code></font> and <font SIZE="-1"><code>TEMP</code></font> are inspected instead and the first value found is taken; if none of them are set, a host-dependent default is used, typically <code>/tmp</code>.</dl>
<h2>DIAGNOSTICS</h2>
<p> The exit status is zero if and only if all operations were successful.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1991, 1992, 1993, 1994, 1995 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-ident/">ident</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/5-rcsfile/">rcsfile</a></code>(5). </p>
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
<p> The separator for revision ranges in the <code>-r</code> option used to be <code>&#8211;</code> instead of <code>:</code>, but this leads to confusion when symbolic names contain <code>&#8211;</code>. For backwards compatibility <code>rlog -r</code> still supports the old <code>&#8211;</code> separator, but it warns about this obsolete use. </p>
<h2>Index</h2>
