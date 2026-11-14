---
title: "co(1)"
name: "co"
section: "1"
letter: "c"
url: "/docs/linux/man/1-co/"
description: "co – check out RCS revisions"
---

<h2>NAME</h2>
<p> co &#8211; check out RCS revisions</p>
<h2>SYNOPSIS</h2>
<p> <code>co</code> [<i>options</i>]<i> file </i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>co</code> retrieves a revision from each <font SIZE="-1">RCS</font> file and stores it into the corresponding working file. </p>
<p> Filenames matching an <font SIZE="-1">RCS</font> suffix denote <font SIZE="-1">RCS</font> files; all others denote working files. Names are paired as explained in <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1). </p>
<p> Revisions of an <font SIZE="-1">RCS</font> file can be checked out locked or unlocked. Locking a revision prevents overlapping updates. A revision checked out for reading or processing (e.g., compiling) need not be locked. A revision checked out for editing and later checkin must normally be locked. Checkout with locking fails if the revision to be checked out is currently locked by another user. (A lock can be broken with <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1).)&nbsp;<wbr> Checkout with locking also requires the caller to be on the access list of the <font SIZE="-1">RCS</font> file, unless he is the owner of the file or the superuser, or the access list is empty. Checkout without locking is not subject to accesslist restrictions, and is not affected by the presence of locks. </p>
<p> A revision is selected by options for revision or branch number, checkin date/time, author, or state. When the selection options are applied in combination, <code>co</code> retrieves the latest revision that satisfies all of them. If none of the selection options is specified, <code>co</code> retrieves the latest revision on the default branch (normally the trunk, see the <code>-b</code> option of <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1)). A revision or branch number can be attached to any of the options <code>-f</code>, <code>-I</code>, <code>-l</code>, <code>-M</code>, <code>-p</code>, <code>-q</code>, <code>-r</code>, or <code>-u</code>. The options <code>-d</code> (date), <code>-s</code> (state), and <code>-w</code> (author) retrieve from a single branch, the <i>selected</i> branch, which is either specified by one of <code>-f</code>, &#8230;, <code>-u</code>, or the default branch. </p>
<p> A <code>co</code> command applied to an <font SIZE="-1">RCS</font> file with no revisions creates a zero-length working file. <code>co</code> always performs keyword substitution (see below).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code>[<i>rev</i>]</p>
<dd> retrieves the latest revision whose number is less than or equal to <i>rev</i>. If <i>rev</i> indicates a branch rather than a revision, the latest revision on that branch is retrieved. If <i>rev</i> is omitted, the latest revision on the default branch (see the <code>-b</code> option of <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1)) is retrieved. If <i>rev</i> is <code>$</code>, <code>co</code> determines the revision number from keyword values in the working file. Otherwise, a revision is composed of one or more numeric or symbolic fields separated by periods. If <i>rev</i> begins with a period, then the default branch (normally the trunk) is prepended to it. If <i>rev</i> is a branch number followed by a period, then the latest revision on that branch is used. The numeric equivalent of a symbolic field is specified with the <code>-n</code> option of the commands <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) and <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1).</p>
<dt><code>-l</code>[<i>rev</i>]</p>
<dd> same as <code>-r</code>, except that it also locks the retrieved revision for the caller.</p>
<dt><code>-u</code>[<i>rev</i>]</p>
<dd> same as <code>-r</code>, except that it unlocks the retrieved revision if it was locked by the caller. If <i>rev</i> is omitted, <code>-u</code> retrieves the revision locked by the caller, if there is one; otherwise, it retrieves the latest revision on the default branch.</p>
<dt><code>-f</code>[<i>rev</i>]</p>
<dd> forces the overwriting of the working file; useful in connection with <code>-q</code>. See also <font SIZE="-1">FILE MODES</font> below.</p>
<dt><code>-kkv</code></p>
<dd> Generate keyword strings using the default form, e.g. <code>$Revision: 5.9.0 $</code> for the <code>Revision</code> keyword. A locker&#8217;s name is inserted in the value of the <code>Header</code>, <code>Id</code>, and <code>Locker</code> keyword strings only as a file is being locked, i.e. by <code>ci -l</code> and <code>co -l.</code> This is the default.</p>
<dt><code>-kkvl</code></p>
<dd> Like <code>-kkv</code>, except that a locker&#8217;s name is always inserted if the given revision is currently locked.</p>
<dt><code>-kk</code></p>
<dd> Generate only keyword names in keyword strings; omit their values. See <font SIZE="-1">KEYWORD SUBSTITUTION</font> below. For example, for the <code>Revision</code> keyword, generate the string <code>$Revision$</code> instead of <code>$Revision: 5.9.0 $</code>. This option is useful to ignore differences due to keyword substitution when comparing different revisions of a file. Log messages are inserted after <code>$Log$</code> keywords even if <code>-kk</code> is specified, since this tends to be more useful when merging changes.</p>
<dt><code>-ko</code></p>
<dd> Generate the old keyword string, present in the working file just before it was checked in. For example, for the <code>Revision</code> keyword, generate the string <code>$Revision: 1.1 $</code> instead of <code>$Revision: 5.9.0 $</code> if that is how the string appeared when the file was checked in. This can be useful for file formats that cannot tolerate any changes to substrings that happen to take the form of keyword strings.</p>
<dt><code>-kb</code></p>
<dd> Generate a binary image of the old keyword string. This acts like <code>-ko</code>, except it performs all working file input and output in binary mode. This makes little difference on Posix and Unix hosts, but on DOS-like hosts one should use <code>rcs -i -kb</code> to initialize an <font SIZE="-1">RCS</font> file intended to be used for binary files. Also, on all hosts, <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1) normally refuses to merge files when <code>-kb</code> is in effect.</p>
<dt><code>-kv</code></p>
<dd> Generate only keyword values for keyword strings. For example, for the <code>Revision</code> keyword, generate the string <code>5.9.0</code> instead of <code>$Revision: 5.9.0 $</code>. This can help generate files in programming languages where it is hard to strip keyword delimiters like <code>$Revision:&nbsp;<wbr>$</code> from a string. However, further keyword substitution cannot be performed once the keyword names are removed, so this option should be used with care. Because of this danger of losing keywords, this option cannot be combined with <code>-l</code>, and the owner write permission of the working file is turned off; to edit the file later, check it out again without <code>-kv</code>.</p>
<dt><code>-p</code>[<i>rev</i>]</p>
<dd> prints the retrieved revision on the standard output rather than storing it in the working file. This option is useful when <code>co</code> is part of a pipe.</p>
<dt><code>-q</code>[<i>rev</i>]</p>
<dd> quiet mode; diagnostics are not printed.</p>
<dt><code>-I</code>[<i>rev</i>]</p>
<dd> interactive mode; the user is prompted and questioned even if the standard input is not a terminal.</p>
<dt><code>-d</code><i>date</i></p>
<dd> retrieves the latest revision on the selected branch whose checkin date/time is less than or equal to <i>date</i>. The date and time can be given in free format. The time zone <code>LT</code> stands for local time; other common time zone names are understood. For example, the following <i>date</i>s are equivalent if local time is January 11, 1990, 8pm Pacific Standard Time, eight hours west of Coordinated Universal Time (<font SIZE="-1">UTC</font>):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>8:00 pm lt</code>
<code>4:00 AM, Jan. 12, 1990</code>             default is <font SIZE="-1">UTC</font>
<code>1990-01-12 04:00:00+00</code>             <font SIZE="-1">ISO</font> 8601 (<font SIZE="-1">UTC</font>)
<code>1990-01-11 20:00:00-08</code>             <font SIZE="-1">ISO</font> 8601 (local time)
<code>1990/01/12 04:00:00</code>                traditional <font SIZE="-1">RCS</font> format
<code>Thu Jan 11 20:00:00 1990 LT</code>        output of <code><a href="//www.systutorials.com/docs/linux/man/3-ctime/">ctime</a></code>(3) + <code>LT</code>
<code>Thu Jan 11 20:00:00 PST 1990</code>       output of <code><a href="//www.systutorials.com/docs/linux/man/1-date/">date</a></code>(1)
<code>Fri Jan 12 04:00:00 GMT 1990</code>
<code>Thu, 11 Jan 1990 20:00:00 -0800</code>    Internet RFC 822
<code>12-January-1990, 04:00 WET</code>
</pre>
</dl>
<p> Most fields in the date and time can be defaulted. The default time zone is normally <font SIZE="-1">UTC</font>, but this can be overridden by the <code>-z</code> option. The other defaults are determined in the order year, month, day, hour, minute, and second (most to least significant). At least one of these fields must be provided. For omitted fields that are of higher significance than the highest provided field, the time zone&#8217;s current values are assumed. For all other omitted fields, the lowest possible values are assumed. For example, without <code>-z</code>, the date <code>20, 10:30</code> defaults to 10:30:00 <font SIZE="-1">UTC</font> of the 20th of the <font SIZE="-1">UTC</font> time zone&#8217;s current month and year. The date/time must be quoted if it contains spaces.</dl>
<dt><code>-M</code>[<i>rev</i>]</p>
<dd> Set the modification time on the new working file to be the date of the retrieved revision. Use this option with care; it can confuse <code><a href="/docs/linux/man/1-make/">make</a></code>(1).</p>
<dt><code>-s</code><i>state</i></p>
<dd> retrieves the latest revision on the selected branch whose state is set to <i>state</i>.</p>
<dt><code>-S</code></p>
<dd> Enable <i>self-same</i> mode. In this mode, the owner of a lock is unimportant, just that it exists. Effectively, this means the user cannot check out the same revision twice.</p>
<dt><code>-T</code></p>
<dd> Preserve the modification time on the <font SIZE="-1">RCS</font> file even if the <font SIZE="-1">RCS</font> file changes because a lock is added or removed. This option can suppress extensive recompilation caused by a <code><a href="/docs/linux/man/1-make/">make</a></code>(1) dependency of some other copy of the working file on the <font SIZE="-1">RCS</font> file. Use this option with care; it can suppress recompilation even when it is needed, i.e. when the change of lock would mean a change to keyword strings in the other working file.</p>
<dt><code>-w</code>[<i>login</i>]</p>
<dd> retrieves the latest revision on the selected branch which was checked in by the user with login name <i>login</i>. If the argument <i>login</i> is omitted, the caller&#8217;s login is assumed.</p>
<dt><code>-j</code><i>joinlist</i></p>
<dd> generates a new revision which is the join of the revisions on <i>joinlist</i>. This option is largely obsoleted by <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1) but is retained for backwards compatibility.</p>
<dl>
<dt>
<dd>
<p> The <i>joinlist</i> is a comma-separated list of pairs of the form <i>rev2</i><code>:</code><i>rev3,</i> where <i>rev2</i> and <i>rev3</i> are (symbolic or numeric) revision numbers. For the initial such pair, <i>rev1</i> denotes the revision selected by the above options <code>-f</code>, &#8230;, <code>-w</code>. For all other pairs, <i>rev1</i> denotes the revision generated by the previous pair. (Thus, the output of one join becomes the input to the next.) </p>
<p> For each pair, <code>co</code> joins revisions <i>rev1</i> and <i>rev3</i> with respect to <i>rev2</i>. This means that all changes that transform <i>rev2</i> into <i>rev1</i> are applied to a copy of <i>rev3</i>. This is particularly useful if <i>rev1</i> and <i>rev3</i> are the ends of two branches that have <i>rev2</i> as a common ancestor. If <i>rev1</i>&lt;<i>rev2</i>&lt;<i>rev3</i> on the same branch, joining generates a new revision which is like <i>rev3,</i> but with all changes that lead from <i>rev1</i> to <i>rev2</i> undone. If changes from <i>rev2</i> to <i>rev1</i> overlap with changes from <i>rev2</i> to <i>rev3,</i> <code>co</code> reports overlaps as described in <code><a href="/docs/linux/man/1-merge/">merge</a></code>(1). </p>
<p> For the initial pair, <i>rev2</i> can be omitted. The default is the common ancestor. If any of the arguments indicate branches, the latest revisions on those branches are assumed. The options <code>-l</code> and <code>-u</code> lock or unlock <i>rev1</i>.</dl>
<dt><code>-V</code></p>
<dd> Print <font SIZE="-1">RCS</font>&#8216;s version number.</p>
<dt><code>-V</code><i>n</i></p>
<dd> Emulate <font SIZE="-1">RCS</font> version <i>n,</i> where <i>n</i> can be <code>3</code>, <code>4</code>, or <code>5</code>. This can be useful when interchanging <font SIZE="-1">RCS</font> files with others who are running older versions of <font SIZE="-1">RCS</font>. To see which version of <font SIZE="-1">RCS</font> your correspondents are running, have them invoke <code>rcs -V</code>; this works with newer versions of <font SIZE="-1">RCS</font>. If it doesn&#8217;t work, have them invoke <code>rlog</code> on an <font SIZE="-1">RCS</font> file; if none of the first few lines of output contain the string <code>branch:</code> it is version 3; if the dates&#8217; years have just two digits, it is version 4; otherwise, it is version 5. An <font SIZE="-1">RCS</font> file generated while emulating version 3 loses its default branch. An <font SIZE="-1">RCS</font> revision generated while emulating version 4 or earlier has a time stamp that is off by up to 13 hours. A revision extracted while emulating version 4 or earlier contains abbreviated dates of the form <i>yy</i><code>/</code><i>mm</i><code>/</code><i>dd</i> and can also contain different white space and line prefixes in the substitution for <code>$Log$</code>.</p>
<dt><code>-x</code><i>suffixes</i></p>
<dd> Use <i>suffixes</i> to characterize <font SIZE="-1">RCS</font> files. See <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) for details.</p>
<dt><code>-z</code><i>zone</i></p>
<dd> specifies the date output format in keyword substitution, and specifies the default time zone for <i>date</i> in the <code>-d</code><i>date</i> option. The <i>zone</i> should be empty, a numeric <font SIZE="-1">UTC</font> offset, or the special string <code>LT</code> for local time. The default is an empty <i>zone</i>, which uses the traditional <font SIZE="-1">RCS</font> format of <font SIZE="-1">UTC</font> without any time zone indication and with slashes separating the parts of the date; otherwise, times are output in <font SIZE="-1">ISO</font> 8601 format with time zone indication. For example, if local time is January 11, 1990, 8pm Pacific Standard Time, eight hours west of <font SIZE="-1">UTC</font>, then the time is output as follows:</p>
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
<p> The <code>-z</code> option does not affect dates stored in <font SIZE="-1">RCS</font> files, which are always <font SIZE="-1">UTC</font>.</dl>
</dl>
<h2>KEYWORD SUBSTITUTION</h2>
<p> Strings of the form <code>$</code><i>keyword</i><code>$</code> and <code>$</code><i>keyword</i><code>:</code><i>&#8230;</i><code>$</code> embedded in the text are replaced with strings of the form <code>$</code><i>keyword</i><code>:</code><i>value</i><code>$</code> where <i>keyword</i> and <i>value</i> are pairs listed below. Keywords can be embedded in literal strings or comments to identify a revision. </p>
<p> Initially, the user enters strings of the form <code>$</code><i>keyword</i><code>$</code><i>.</i> On checkout, <code>co</code> replaces these strings with strings of the form <code>$</code><i>keyword</i><code>:</code><i>value</i><code>$</code><i>.</i> If a revision containing strings of the latter form is checked back in, the value fields will be replaced during the next checkout. Thus, the keyword values are automatically updated on checkout. This automatic substitution can be modified by the <code>-k</code> options. </p>
<p> Keywords and their corresponding values:</p>
<dl>
<dt><code>$Author$</code></p>
<dd> The login name of the user who checked in the revision.</p>
<dt><code>$Date$</code></p>
<dd> The date and time the revision was checked in. With <code>-z</code><i>zone</i> a numeric time zone offset is appended; otherwise, the date is <font SIZE="-1">UTC</font>.</p>
<dt><code>$Header$</code></p>
<dd> A standard header containing the full <font SIZE="-1">RCS</font> file name, the revision number, the date and time, the author, the state, and the locker (if locked). With <code>-z</code><i>zone</i> a numeric time zone offset is appended to the date; otherwise, the date is <font SIZE="-1">UTC</font>.</p>
<dt><code>$Id$</code></p>
<dd> Same as <code>$Header$</code>, except that the <font SIZE="-1">RCS</font> file name is without the directory components.</p>
<dt><code>$Locker$</code></p>
<dd> The login name of the user who locked the revision (empty if not locked).</p>
<dt><code>$Log$</code></p>
<dd> The log message supplied during checkin, preceded by a header containing the <font SIZE="-1">RCS</font> file name, the revision number, the author, and the date and time. With <code>-z</code><i>zone</i> a numeric time zone offset is appended; otherwise, the date is <font SIZE="-1">UTC</font>. Existing log messages are <i>not</i> replaced. Instead, the new log message is inserted after <code>$Log:</code>&#8230;<code>$</code>. This is useful for accumulating a complete change log in a source file.</p>
<dl>
<dt>
<dd>
<p> Each inserted line is prefixed by the string that prefixes the <code>$Log$</code> line. For example, if the <code>$Log$</code> line is &#8220;<code>//&nbsp;<wbr>$Log: tan.cc&nbsp;<wbr>$</code>&#8221;, <font SIZE="-1">RCS</font> prefixes each line of the log with &#8220;<code>//&nbsp;<wbr></code>&#8221;. This is useful for languages with comments that go to the end of the line. The convention for other languages is to use a &#8220;<code> * </code>&#8221; prefix inside a multiline comment. For example, the initial log comment of a C program conventionally is of the following form:</p>
<dl>
<dt>
<dd>
<pre>
<code>/*
* $Log$
*/
</code></pre>
</dl>
<p> For backwards compatibility with older versions of <font SIZE="-1">RCS</font>, if the log prefix is <code>/*</code> or <code>(*</code> surrounded by optional white space, inserted log lines contain a space instead of <code>/</code> or <code>(</code>; however, this usage is obsolescent and should not be relied on.</dl>
<dt><code>$Name$</code></p>
<dd> The symbolic name used to check out the revision, if any. For example, <code>co -rJoe</code> generates <code>$Name: Joe&nbsp;<wbr>$</code>. Plain <code>co</code> generates just <code>$Name:&nbsp;<wbr>&nbsp;<wbr>$</code>.</p>
<dt><code>$RCSfile$</code></p>
<dd> The <font SIZE="-1">RCS</font> file name without directory components.</p>
<dt><code>$Revision$</code></p>
<dd> The revision number assigned to the revision.</p>
<dt><code>$Source$</code></p>
<dd> The full <font SIZE="-1">RCS</font> file name.</p>
<dt><code>$State$</code></p>
<dd> The state assigned to the revision with the <code>-s</code> option of <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1) or <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1).</dl>
<p> The following characters in keyword values are represented by escape sequences to keep keyword strings well-formed. </p>
<dl>
<dt>
<dd>
<pre>
<i>char     escape sequence</i>
tab      <code>	</code>
newline  <code>
</code>
space    <code> 
$        $
\        \</code>
</pre>
</dl>
<h2>FILE MODES</h2>
<p> The working file inherits the read and execute permissions from the <font SIZE="-1">RCS</font> file. In addition, the owner write permission is turned on, unless <code>-kv</code> is set or the file is checked out unlocked and locking is set to strict (see <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1)). </p>
<p> If a file with the name of the working file exists already and has write permission, <code>co</code> aborts the checkout, asking beforehand if possible. If the existing working file is not writable or <code>-f</code> is given, the working file is deleted without asking.</p>
<h2>FILES</h2>
<p> <code>co</code> accesses files much as <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) does, except that it does not need to read the working file unless a revision number of <code>$</code> is specified.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>RCSINIT</code></font></p>
<dd> Options prepended to the argument list, separated by spaces. A backslash escapes spaces within an option. The <font SIZE="-1"><code>RCSINIT</code></font> options are prepended to the argument lists of most <font SIZE="-1">RCS</font> commands. Useful <font SIZE="-1"><code>RCSINIT</code></font> options include <code>-q</code>, <code>-V</code>, <code>-x</code>, and <code>-z</code>.</p>
<dt><font SIZE="-1"><code>RCS_MEM_LIMIT</code></font></p>
<dd> An integer <i>lim</i>, measured in kilobytes, specifying the threshold under which commands will try to use memory-based operations for processing the <font SIZE="-1">RCS</font> file. (For <font SIZE="-1">RCS</font> files of size <i>lim</i> kilobytes or greater, RCS will use the slower standard input/output routines.) Default value is 256.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd> Name of the temporary directory. If not set, the environment variables <font SIZE="-1"><code>TMP</code></font> and <font SIZE="-1"><code>TEMP</code></font> are inspected instead and the first value found is taken; if none of them are set, a host-dependent default is used, typically <code>/tmp</code>.</dl>
<h2>DIAGNOSTICS</h2>
<p> The <font SIZE="-1">RCS</font> file name, the working file name, and the revision number retrieved are written to the diagnostic output. The exit status is zero if and only if all operations were successful.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1991, 1992, 1993, 1994, 1995 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/1-ident/">ident</a></code>(1), <code><a href="/docs/linux/man/1-make/">make</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsclean/">rcsclean</a></code>(1), <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1), <code><a href="/docs/linux/man/5-rcsfile/">rcsfile</a></code>(5). </p>
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
<h2>LIMITS</h2>
<p> Links to the <font SIZE="-1">RCS</font> and working files are not preserved. </p>
<p> There is no way to selectively suppress the expansion of keywords, except by writing them differently. In nroff and troff, this is done by embedding the null-character <code>\&amp;</code> into the keyword. </p>
<h2>Index</h2>
