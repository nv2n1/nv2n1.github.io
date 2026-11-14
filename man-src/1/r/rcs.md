---
title: "rcs(1)"
name: "rcs"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcs/"
description: "rcs – change RCS file attributes"
---

<h2>NAME</h2>
<p> rcs &#8211; change <font SIZE="-1">RCS</font> file attributes</p>
<h2>SYNOPSIS</h2>
<p> <code>rcs</code> <i>options file </i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>rcs</code> creates new <font SIZE="-1">RCS</font> files or changes attributes of existing ones. An <font SIZE="-1">RCS</font> file contains multiple revisions of text, an access list, a change log, descriptive text, and some control attributes. For <code>rcs</code> to work, the caller&#8217;s login name must be on the access list, except if the access list is empty, the caller is the owner of the file or the superuser, or the <code>-i</code> option is present. </p>
<p> Filenames matching an <font SIZE="-1">RCS</font> suffix denote <font SIZE="-1">RCS</font> files; all others denote working files. Names are paired as explained in <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1). Revision numbers use the syntax described in <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd> Create and initialize a new <font SIZE="-1">RCS</font> file, but do not deposit any revision. If the <font SIZE="-1">RCS</font> file name has no directory component, try to place it first into the subdirectory <code>./RCS</code>, and then into the current directory. If the <font SIZE="-1">RCS</font> file already exists, print an error message.</p>
<dt><code>-a</code><i>logins</i></p>
<dd> Append the login names appearing in the comma-separated list <i>logins</i> to the access list of the <font SIZE="-1">RCS</font> file.</p>
<dt><code>-A</code><i>oldfile</i></p>
<dd> Append the access list of <i>oldfile</i> to the access list of the <font SIZE="-1">RCS</font> file.</p>
<dt><code>-e</code>[<i>logins</i>]</p>
<dd> Erase the login names appearing in the comma-separated list <i>logins</i> from the access list of the <font SIZE="-1">RCS</font> file. If <i>logins</i> is omitted, erase the entire access list.</p>
<dt><code>-b</code>[<i>rev</i>]</p>
<dd> Set the default branch to <i>rev</i>. If <i>rev</i> is omitted, the default branch is reset to the (dynamically) highest branch on the trunk.</p>
<dt><code>-c</code><i>string</i></p>
<dd> Set the comment leader to <i>string</i>. An initial <code>ci</code>, or an <code>rcs -i</code> without <code>-c</code>, guesses the comment leader from the suffix of the working file name.</p>
<dl>
<dt>
<dd>
<p> This option is obsolescent, since <font SIZE="-1">RCS</font> normally uses the preceding <code>$Log$</code> line&#8217;s prefix when inserting log lines during checkout (see <code><a href="/docs/linux/man/1-co/">co</a></code>(1)). However, older versions of <font SIZE="-1">RCS</font> use the comment leader instead of the <code>$Log$</code> line&#8217;s prefix, so if you plan to access a file with both old and new versions of <font SIZE="-1">RCS</font>, make sure its comment leader matches its <code>$Log$</code> line prefix.</dl>
<dt><code>-k</code><i>subst</i></p>
<dd> Set the default keyword substitution to <i>subst</i>. The effect of keyword substitution is described in <code><a href="/docs/linux/man/1-co/">co</a></code>(1). Giving an explicit <code>-k</code> option to <code>co</code>, <code>rcsdiff</code>, and <code>rcsmerge</code> overrides this default. Beware <code>rcs -kv,</code> because <code>-kv</code> is incompatible with <code>co -l.</code> Use <code>rcs -kkv</code> to restore the normal default keyword substitution.</p>
<dt><code>-l</code>[<i>rev</i>]</p>
<dd> Lock the revision with number <i>rev</i>. If a branch is given, lock the latest revision on that branch. If <i>rev</i> is omitted, lock the latest revision on the default branch. Locking prevents overlapping changes. If someone else already holds the lock, the lock is broken as with <code>rcs -u</code> (see below).</p>
<dt><code>-u</code>[<i>rev</i>]</p>
<dd> Unlock the revision with number <i>rev</i>. If a branch is given, unlock the latest revision on that branch. If <i>rev</i> is omitted, remove the latest lock held by the caller. Normally, only the locker of a revision can unlock it. Somebody else unlocking a revision breaks the lock. If RCS was configured <code>&#8211;with-mailer</code>, then this causes a mail message to be sent to the original locker. The message contains a commentary solicited from the breaker. The commentary is terminated by end-of-file or by a line containing <code>.</code>&nbsp;<wbr>by itself.</p>
<dt><code>-L</code></p>
<dd> Set locking to <i>strict</i>. Strict locking means that the owner of an <font SIZE="-1">RCS</font> file is not exempt from locking for checkin. This option should be used for files that are shared.</p>
<dt><code>-U</code></p>
<dd> Set locking to non-strict. Non-strict locking means that the owner of a file need not lock a revision for checkin. This option should <i>not</i> be used for files that are shared. Whether default locking is strict is determined by your system administrator, but it is normally strict.</p>
<dt><code>-m</code><i>rev</i><code>:</code>[<i>msg</i>]</p>
<dd> Replace revision <i>rev</i>&#8216;s log message with <i>msg</i>. If <i>msg</i> is omitted, it defaults to &quot;*** empty log message ***&quot;.</p>
<dt><code>-M</code></p>
<dd> Do not send mail when breaking somebody else&#8217;s lock. This option is not meant for casual use; it is meant for programs that warn users by other means, and invoke <code>rcs -u</code> only as a low-level lock-breaking operation.</p>
<dt><code>-n</code><i>name</i>[<code>:</code>[<i>rev</i>]]</p>
<dd> Associate the symbolic name <i>name</i> with the branch or revision <i>rev</i>. Delete the symbolic name if both <code>:</code> and <i>rev</i> are omitted; otherwise, print an error message if <i>name</i> is already associated with another number. If <i>rev</i> is symbolic, it is expanded before association. A <i>rev</i> consisting of a branch number followed by a <code>.</code> stands for the current latest revision in the branch. A <code>:</code> with an empty <i>rev</i> stands for the current latest revision on the default branch, normally the trunk. For example, <code>rcs -n</code><i>name</i><code>: RCS/*</code> associates <i>name</i> with the current latest revision of all the named <font SIZE="-1">RCS</font> files; this contrasts with <code>rcs -n</code><i>name</i><code>:$&nbsp;<wbr>RCS/*</code> which associates <i>name</i> with the revision numbers extracted from keyword strings in the corresponding working files.</p>
<dt><code>-N</code><i>name</i>[<code>:</code>[<i>rev</i>]]</p>
<dd> Act like <code>-n</code>, except override any previous assignment of <i>name</i>.</p>
<dt><code>-o</code><i>range</i></p>
<dd> deletes (&#8220;outdates&#8221;) the revisions given by <i>range</i>. A range consisting of a single revision number means that revision. A range consisting of a branch number means the latest revision on that branch. A range of the form <i>rev1</i><code>:</code><i>rev2</i> means revisions <i>rev1</i> to <i>rev2</i> on the same branch, <code>:</code><i>rev</i> means from the beginning of the branch containing <i>rev</i> up to and including <i>rev</i>, and <i>rev</i><code>:</code> means from revision <i>rev</i> to the end of the branch containing <i>rev</i>. None of the outdated revisions can have branches or locks.</p>
<dt><code>-q</code></p>
<dd> Run quietly; do not print diagnostics.</p>
<dt><code>-I</code></p>
<dd> Run interactively, even if the standard input is not a terminal.</p>
<dt><code>-s</code><i>state</i>[:<i>rev</i>]</p>
<dd> Set the state attribute of the revision <i>rev</i> to <i>state</i>. If <i>rev</i> is a branch number, assume the latest revision on that branch. If <i>rev</i> is omitted, assume the latest revision on the default branch. Any identifier is acceptable for <i>state</i>. A useful set of states is <code>Exp</code> (for experimental), <code>Stab</code> (for stable), and <code>Rel</code> (for released). By default, <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) sets the state of a revision to <code>Exp</code>.</p>
<dt><code>-t</code>[<i>file</i>]</p>
<dd> Write descriptive text from the contents of the named <i>file</i> into the <font SIZE="-1">RCS</font> file, deleting the existing text. The <i>file</i> name cannot begin with <code>&#8211;</code>. If <i>file</i> is omitted, obtain the text from standard input, terminated by end-of-file or by a line containing <code>.</code>&nbsp;<wbr>by itself. Prompt for the text if interaction is possible; see <code>-I</code>. With <code>-i</code>, descriptive text is obtained even if <code>-t</code> is not given.</p>
<dt><code>-t-</code><i>string</i></p>
<dd> Write descriptive text from the <i>string</i> into the <font SIZE="-1">RCS</font> file, deleting the existing text.</p>
<dt><code>-T</code></p>
<dd> Preserve the modification time on the <font SIZE="-1">RCS</font> file unless a revision is removed. This option can suppress extensive recompilation caused by a <code><a href="/docs/linux/man/1-make/">make</a></code>(1) dependency of some copy of the working file on the <font SIZE="-1">RCS</font> file. Use this option with care; it can suppress recompilation even when it is needed, i.e. when a change to the <font SIZE="-1">RCS</font> file would mean a change to keyword strings in the working file.</p>
<dt><code>-V</code></p>
<dd> Print <font SIZE="-1">RCS</font>&#8216;s version number.</p>
<dt><code>-V</code><i>n</i></p>
<dd> Emulate <font SIZE="-1">RCS</font> version <i>n</i>. See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details.</p>
<dt><code>-x</code><i>suffixes</i></p>
<dd> Use <i>suffixes</i> to characterize <font SIZE="-1">RCS</font> files. See <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) for details.</p>
<dt><code>-z</code><i>zone</i></p>
<dd> Use <i>zone</i> as the default time zone. This option has no effect; it is present for compatibility with other <font SIZE="-1">RCS</font> commands.</dl>
<p> At least one explicit option must be given, to ensure compatibility with future planned extensions to the <code>rcs</code> command.</p>
<h2>COMPATIBILITY</h2>
<p> The <code>-b</code><i>rev</i> option generates an <font SIZE="-1">RCS</font> file that cannot be parsed by <font SIZE="-1">RCS</font> version 3 or earlier. </p>
<p> The <code>-k</code><i>subst</i> options (except <code>-kkv</code>) generate an <font SIZE="-1">RCS</font> file that cannot be parsed by <font SIZE="-1">RCS</font> version 4 or earlier. </p>
<p> Use <code>rcs -V</code><i>n</i> to make an <font SIZE="-1">RCS</font> file acceptable to <font SIZE="-1">RCS</font> version <i>n</i> by discarding information that would confuse version <i>n</i>. </p>
<p> <font SIZE="-1">RCS</font> version 5.5 and earlier does not support the <code>-x</code> option, and requires a <code>,v</code> suffix on an <font SIZE="-1">RCS</font> file name.</p>
<h2>FILES</h2>
<p> <code>rcs</code> accesses files much as <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) does, except that it uses the effective user for all accesses, it does not write the working file or its directory, and it does not even read the working file unless a revision number of <code>$</code> is specified.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>RCSINIT</code></font></p>
<dd> Options prepended to the argument list, separated by spaces. A backslash escapes spaces within an option. The <font SIZE="-1"><code>RCSINIT</code></font> options are prepended to the argument lists of most <font SIZE="-1">RCS</font> commands. Useful <font SIZE="-1"><code>RCSINIT</code></font> options include <code>-q</code>, <code>-V</code>, <code>-x</code>, and <code>-z</code>.</p>
<dt><font SIZE="-1"><code>RCS_MEM_LIMIT</code></font></p>
<dd> An integer <i>lim</i>, measured in kilobytes, specifying the threshold under which commands will try to use memory-based operations for processing the <font SIZE="-1">RCS</font> file. (For <font SIZE="-1">RCS</font> files of size <i>lim</i> kilobytes or greater, RCS will use the slower standard input/output routines.) Default value is 256.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd> Name of the temporary directory. If not set, the environment variables <font SIZE="-1"><code>TMP</code></font> and <font SIZE="-1"><code>TEMP</code></font> are inspected instead and the first value found is taken; if none of them are set, a host-dependent default is used, typically <code>/tmp</code>.</dl>
<h2>DIAGNOSTICS</h2>
<p> The <font SIZE="-1">RCS</font> file name and the revisions outdated are written to the diagnostic output. The exit status is zero if and only if all operations were successful.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1991, 1992, 1993, 1994, 1995 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), <code><a href="/docs/linux/man/1-ident/">ident</a></code>(1), <code><a href="/docs/linux/man/1-rcsclean/">rcsclean</a></code>(1), <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1), <code><a href="/docs/linux/man/5-rcsfile/">rcsfile</a></code>(5). </p>
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
<p> A catastrophe (e.g. a system crash) can cause <font SIZE="-1">RCS</font> to leave behind a semaphore file that causes later invocations of <font SIZE="-1">RCS</font> to claim that the <font SIZE="-1">RCS</font> file is in use. To fix this, remove the semaphore file. A semaphore file&#8217;s name typically begins with <code>,</code> or ends with <code>_</code>. </p>
<p> The separator for revision ranges in the <code>-o</code> option used to be <code>&#8211;</code> instead of <code>:</code>, but this leads to confusion when symbolic names contain <code>&#8211;</code>. For backwards compatibility <code>rcs -o</code> still supports the old <code>&#8211;</code> separator, but it warns about this obsolete use. </p>
<p> Symbolic names need not refer to existing revisions or branches. For example, the <code>-o</code> option does not remove symbolic names for the outdated revisions; you must use <code>-n</code> to remove the names. </p>
<h2>Index</h2>
