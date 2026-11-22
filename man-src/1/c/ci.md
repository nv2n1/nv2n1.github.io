---

title: "ci(1)"
name: "ci"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ci/"
description: "ci – check in RCS revisions"
---

<p> ci &#8211; check in RCS revisions</p>
<h2>SYNOPSIS</h2>
<p> <code>ci</code> [<i>options</i>]<i> file </i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>ci</code> stores new revisions into RCS files. Each file name matching an RCS suffix is taken to be an RCS file. All others are assumed to be working files containing new revisions. <code>ci</code> deposits the contents of each working file into the corresponding RCS file. If only a working file is given, <code>ci</code> tries to find the corresponding RCS file in an RCS subdirectory and then in the working file&#8217;s directory. For more details, see FILE NAMING below. </p>
<p> For <code>ci</code> to work, the caller&#8217;s login must be on the access list, except if the access list is empty or the caller is the superuser or the owner of the file. To append a new revision to an existing branch, the tip revision on that branch must be locked by the caller. Otherwise, only a new branch can be created. This restriction is not enforced for the owner of the file if non-strict locking is used (see <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1)). A lock held by someone else can be broken with the <code>rcs</code> command. </p>
<p> Unless the <code>-f</code> option is given, <code>ci</code> checks whether the revision to be deposited differs from the preceding one. If not, instead of creating a new revision <code>ci</code> reverts to the preceding one. To revert, ordinary <code>ci</code> removes the working file and any lock; <code>ci -l</code> keeps and <code>ci -u</code> removes any lock, and then they both generate a new working file much as if <code>co -l</code> or <code>co -u</code> had been applied to the preceding revision. When reverting, any <code>-n</code> and <code>-s</code> options apply to the preceding revision. </p>
<p> For each revision deposited, <code>ci</code> prompts for a log message. The log message should summarize the change and must be terminated by end-of-file or by a line containing <code>.</code>&nbsp;<wbr>by itself. If several files are checked in <code>ci</code> asks whether to reuse the previous log message. If the standard input is not a terminal, <code>ci</code> suppresses the prompt and uses the same log message for all files. See also <code>-m</code>. </p>
<p> If the RCS file does not exist, <code>ci</code> creates it and deposits the contents of the working file as the initial revision (default number: <code>1.1</code>). The access list is initialized to empty. Instead of the log message, <code>ci</code> requests descriptive text (see <code>-t</code> below). </p>
<p> The number <i>rev</i> of the deposited revision can be given by any of the options <code>-f</code>, <code>-i</code>, <code>-I</code>, <code>-j</code>, <code>-k</code>, <code>-l</code>, <code>-M</code>, <code>-q</code>, <code>-r</code>, or <code>-u</code>. <i>rev</i> can be symbolic, numeric, or mixed. Symbolic names in <i>rev</i> must already be defined; see the <code>-n</code> and <code>-N</code> options for assigning names during checkin. If <i>rev</i> is <code>$</code>, <code>ci</code> determines the revision number from keyword values in the working file. </p>
<p> If <i>rev</i> begins with a period, then the default branch (normally the trunk) is prepended to it. If <i>rev</i> is a branch number followed by a period, then the latest revision on that branch is used. </p>
<p> If <i>rev</i> is a revision number, it must be higher than the latest one on the branch to which <i>rev</i> belongs, or must start a new branch. </p>
<p> If <i>rev</i> is a branch rather than a revision number, the new revision is appended to that branch. The level number is obtained by incrementing the tip revision number of that branch. If <i>rev</i> indicates a non-existing branch, that branch is created with the initial revision numbered <i>rev</i><code>.1</code>. </p>
<p> If <i>rev</i> is omitted, <code>ci</code> tries to derive the new revision number from the caller&#8217;s last lock. If the caller has locked the tip revision of a branch, the new revision is appended to that branch. The new revision number is obtained by incrementing the tip revision number. If the caller locked a non-tip revision, a new branch is started at that revision by incrementing the highest branch number at that revision. The default initial branch and level numbers are <code>1</code>. </p>
<p> If <i>rev</i> is omitted and the caller has no lock, but owns the file and locking is not set to <i>strict</i>, then the revision is appended to the default branch (normally the trunk; see the <code>-b</code> option of <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1)). </p>
<p> Exception: On the trunk, revisions can be appended to the end, but not inserted.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code><i>rev</i></dt>
<dd> Check in revision <i>rev</i>.</dd>
<dt><code>-r</code></dt>
<dd> The bare <code>-r</code> option (without any revision) has an unusual meaning in <code>ci</code>. With other RCS commands, a bare <code>-r</code> option specifies the most recent revision on the default branch, but with <code>ci</code>, a bare <code>-r</code> option reestablishes the default behavior of releasing a lock and removing the working file, and is used to override any default <code>-l</code> or <code>-u</code> options established by shell aliases or scripts.</dd>
<dt><code>-l</code>[<i>rev</i>]</dt>
<dd> works like <code>-r</code>, except it performs an additional <code>co -l</code> for the deposited revision. Thus, the deposited revision is immediately checked out again and locked. This is useful for saving a revision although one wants to continue editing it after the checkin.</dd>
<dt><code>-u</code>[<i>rev</i>]</dt>
<dd> works like <code>-l</code>, except that the deposited revision is not locked. This lets one read the working file immediately after checkin.</dd>
<dl>
<dt>
</dt><dd>
<p> The <code>-l</code>, bare <code>-r</code>, and <code>-u</code> options are mutually exclusive and silently override each other. For example, <code>ci -u -r</code> is equivalent to <code>ci -r</code> because bare <code>-r</code> overrides <code>-u</code>.</dd></dl>
<dt><code>-f</code>[<i>rev</i>]</dt>
<dd> forces a deposit; the new revision is deposited even it is not different from the preceding one.</dd>
<dt><code>-k</code>[<i>rev</i>]</dt>
<dd> searches the working file for keyword values to determine its revision number, creation date, state, and author (see <code><a href="/docs/linux/man/1-co/">co</a></code>(1)), and assigns these values to the deposited revision, rather than computing them locally. It also generates a default login message noting the login of the caller and the actual checkin date. This option is useful for software distribution. A revision that is sent to several sites should be checked in with the <code>-k</code> option at these sites to preserve the original number, date, author, and state. The extracted keyword values and the default log message can be overridden with the options <code>-d</code>, <code>-m</code>, <code>-s</code>, <code>-w</code>, and any option that carries a revision number.</dd>
<dt><code>-q</code>[<i>rev</i>]</dt>
<dd> quiet mode; diagnostic output is not printed. A revision that is not different from the preceding one is not deposited, unless <code>-f</code> is given.</dd>
<dt><code>-i</code>[<i>rev</i>]</dt>
<dd> initial checkin; report an error if the RCS file already exists. This avoids race conditions in certain applications.</dd>
<dt><code>-j</code>[<i>rev</i>]</dt>
<dd> just checkin and do not initialize; report an error if the RCS file does not already exist.</dd>
<dt><code>-I</code>[<i>rev</i>]</dt>
<dd> interactive mode; the user is prompted and questioned even if the standard input is not a terminal.</dd>
<dt><code>-d</code>[<i>date</i>]</dt>
<dd> uses <i>date</i> for the checkin date and time. The <i>date</i> is specified in free format as explained in <code><a href="/docs/linux/man/1-co/">co</a></code>(1). This is useful for lying about the checkin date, and for <code>-k</code> if no date is available. If <i>date</i> is empty, the working file&#8217;s time of last modification is used.</dd>
<dt><code>-M</code>[<i>rev</i>]</dt>
<dd> Set the modification time on any new working file to be the date of the retrieved revision. For example, <code>ci -d -M -u</code><i>&nbsp;<wbr>f</i> does not alter <i>f</i>&#8216;s modification time, even if <i>f</i>&#8216;s contents change due to keyword substitution. Use this option with care; it can confuse <code><a href="/docs/linux/man/1-make/">make</a></code>(1).</dd>
<dt><code>-m</code>[<i>msg</i>]</dt>
<dd> uses the string <i>msg</i> as the log message for all revisions checked in. If <i>msg</i> is omitted, it defaults to &quot;*** empty log message ***&quot;. By convention, log messages that start with <code>#</code> are comments and are ignored by programs like GNU Emacs&#8217;s <code>vc</code> package. Also, log messages that start with <code>{</code><i>clumpname</i><code>}</code> (followed by white space) are meant to be clumped together if possible, even if they are associated with different files; the <code>{</code><i>clumpname</i><code>}</code> label is used only for clumping, and is not considered to be part of the log message itself.</dd>
<dt><code>-n</code><i>name</i></dt>
<dd> assigns the symbolic name <i>name</i> to the number of the checked-in revision. <code>ci</code> prints an error message if <i>name</i> is already assigned to another number.</dd>
<dt><code>-N</code><i>name</i></dt>
<dd> same as <code>-n</code>, except that it overrides a previous assignment of <i>name</i>.</dd>
<dt><code>-s</code><i>state</i></dt>
<dd> sets the state of the checked-in revision to the identifier <i>state</i>. The default state is <code>Exp</code>.</dd>
<dt><code>-t</code><i>file</i></dt>
<dd> writes descriptive text from the contents of the named <i>file</i> into the RCS file, deleting the existing text. The <i>file</i> cannot begin with <code>&#8211;</code>.</dd>
<dt><code>-t-</code><i>string</i></dt>
<dd> Write descriptive text from the <i>string</i> into the RCS file, deleting the existing text.</dd>
<dl>
<dt>
</dt><dd>
<p> The <code>-t</code> option, in both its forms, has effect only during an initial checkin; it is silently ignored otherwise. </p>
<p> During the initial checkin, if <code>-t</code> is not given, <code>ci</code> obtains the text from standard input, terminated by end-of-file or by a line containing <code>.</code>&nbsp;<wbr>by itself. The user is prompted for the text if interaction is possible; see <code>-I</code>. </p>
<p> For backward compatibility with older versions of RCS, a bare <code>-t</code> option is ignored.</dd></dl>
<dt><code>-T</code></dt>
<dd> Set the RCS file&#8217;s modification time to the new revision&#8217;s time if the former precedes the latter and there is a new revision; preserve the RCS file&#8217;s modification time otherwise. If you have locked a revision, <code>ci</code> usually updates the RCS file&#8217;s modification time to the current time, because the lock is stored in the RCS file and removing the lock requires changing the RCS file. This can create an RCS file newer than the working file in one of two ways: first, <code>ci -M</code> can create a working file with a date before the current time; second, when reverting to the previous revision the RCS file can change while the working file remains unchanged. These two cases can cause excessive recompilation caused by a <code><a href="/docs/linux/man/1-make/">make</a></code>(1) dependency of the working file on the RCS file. The <code>-T</code> option inhibits this recompilation by lying about the RCS file&#8217;s date. Use this option with care; it can suppress recompilation even when a checkin of one working file should affect another working file associated with the same RCS file. For example, suppose the RCS file&#8217;s time is 01:00, the (changed) working file&#8217;s time is 02:00, some other copy of the working file has a time of 03:00, and the current time is 04:00. Then <code>ci -d -T</code> sets the RCS file&#8217;s time to 02:00 instead of the usual 04:00; this causes <code><a href="/docs/linux/man/1-make/">make</a></code>(1) to think (incorrectly) that the other copy is newer than the RCS file.</dd>
<dt><code>-w</code><i>login</i></dt>
<dd> uses <i>login</i> for the author field of the deposited revision. Useful for lying about the author, and for <code>-k</code> if no author is available.</dd>
<dt><code>-V</code></dt>
<dd> Print RCS&#8216;s version number.</dd>
<dt><code>-V</code><i>n</i></dt>
<dd> Emulate RCS version <i>n</i>. See <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details.</dd>
<dt><code>-x</code><i>suffixes</i></dt>
<dd> specifies the suffixes for RCS files. A nonempty suffix matches any file name ending in the suffix. An empty suffix matches any file name of the form <code>RCS/</code><i>frag</i> or <i>frag1</i><code>/RCS/</code><i>frag2.</i> The <code>-x</code> option can specify a list of suffixes separated by <code>/</code>. For example, <code>-x,v/</code> specifies two suffixes: <code>,v</code> and the empty suffix. If two or more suffixes are specified, they are tried in order when looking for an RCS file; the first one that works is used for that file. If no RCS file is found but an RCS file can be created, the suffixes are tried in order to determine the new RCS file&#8217;s name. The default for <i>suffixes</i> is installation-dependent; normally it is <code>,v/</code> for hosts like Unix that permit commas in file names, and is empty (i.e. just the empty suffix) for other hosts.</dd>
<dt><code>-z</code><i>zone</i></dt>
<dd> specifies the date output format in keyword substitution, and specifies the default time zone for <i>date</i> in the <code>-d</code><i>date</i> option. The <i>zone</i> should be empty, a numeric UTC offset, or the special string <code>LT</code> for local time. The default is an empty <i>zone</i>, which uses the traditional RCS format of UTC without any time zone indication and with slashes separating the parts of the date; otherwise, times are output in ISO 8601 format with time zone indication. For example, if local time is January 11, 1990, 8pm Pacific Standard Time, eight hours west of UTC, then the time is output as follows:</dd>
<dl>
<dl>
<dt>
</dt><dd>
<pre>
<i>option</i>      <i>time output</i>
<code>-z</code>          <code>1990/01/12 04:00:00</code>          <i>(default)</i>
<code>-zLT</code>        <code>1990-01-11 20:00:00-08</code>
<code>-z+05:30</code>    <code>1990-01-12 09:30:00+05:30</code>
</pre>
</dd></dl>
<p> The <code>-z</code> option does not affect dates stored in RCS files, which are always UTC.</dl>
</dl>
<h2>FILE NAMING</h2>
<p> Pairs of RCS files and working files can be specified in three ways (see also the example section). </p>
<p> 1) Both the RCS file and the working file are given. The RCS file name is of the form <i>frag1</i><code>/</code><i>workfileX</i> and the working file name is of the form <i>frag2</i><code>/</code><i>workfile</i> where <i>frag1</i><code>/</code> and <i>frag2</i><code>/</code> are (possibly different or empty) file names, <i>workfile</i> is a file name, and <i>X</i> is an RCS suffix. If <i>X</i> is empty, <i>frag1</i><code>/</code> must start with <code>RCS/</code> or must contain <code>/RCS/</code>. </p>
<p> 2) Only the RCS file is given. Then the working file is created in the current directory and its name is derived from the RCS file name by removing <i>frag1</i><code>/</code> and the suffix <i>X</i>. </p>
<p> 3) Only the working file is given. Then <code>ci</code> considers each RCS suffix <i>X</i> in turn, looking for an RCS file of the form <i>frag2</i><code>/RCS/</code><i>workfileX</i> or (if the former is not found and <i>X</i> is nonempty) <i>frag2</i><code>/</code><i>workfileX.</i> </p>
<p> If the RCS file is specified without a file name in 1) and 2), <code>ci</code> looks for the RCS file first in the directory <code>./RCS</code> and then in the current directory. </p>
<p> <code>ci</code> reports an error if an attempt to open an RCS file fails for an unusual reason, even if the RCS file&#8217;s name is just one of several possibilities. For example, to suppress use of RCS commands in a directory <i>d</i>, create a regular file named <i>d</i><code>/RCS</code> so that casual attempts to use RCS commands in <i>d</i> fail because <i>d</i><code>/RCS</code> is not a directory.</p>
<h2>EXAMPLES</h2>
<p> Suppose <code>,v</code> is an RCS suffix and the current directory contains a subdirectory <code>RCS</code> with an RCS file <code>io.c,v</code>. Then each of the following commands check in a copy of <code>io.c</code> into <code>RCS/io.c,v</code> as the latest revision, removing <code>io.c</code>. </p>
<dl>
<dt>
</dt><dd>
<pre><code>
ci io.c;
ci RCS / io.c, v;
ci io.c, v;
ci io.c RCS / io.c, v;
ci io.c io.c, v;
ci RCS / io.c, v io.c;
ci io.c, v io.c;
</code></pre>
</dd></dl>
<p> Suppose instead that the empty suffix is an RCS suffix and the current directory contains a subdirectory <code>RCS</code> with an RCS file <code>io.c</code>. The each of the following commands checks in a new revision. </p>
<dl>
<dt>
</dt><dd>
ci io.c;<br/>
ci RCS / io.c;<br/>
ci io.c RCS / io.c;<br/>
ci RCS / io.c io.c;
</dd></dl>
<h2>FILE MODES</h2>
<p> An RCS file created by <code>ci</code> inherits the read and execute permissions from the working file. If the RCS file exists already, <code>ci</code> preserves its read and execute permissions. <code>ci</code> always turns off all write permissions of RCS files.</p>
<h2>FILES</h2>
<p> Temporary files are created in the directory containing the working file, and also in the temporary directory (see <code>TMPDIR</code> under <code>ENVIRONMENT</code>). A semaphore file or files are created in the directory containing the RCS file. With a nonempty suffix, the semaphore names begin with the first character of the suffix; therefore, do not specify an suffix whose first character could be that of a working file name. With an empty suffix, the semaphore names end with <code>_</code> so working file names should not end in <code>_</code>. </p>
<p> <code>ci</code> never changes an RCS file or working file. Normally, <code>ci</code> unlinks the file and creates a new one; but instead of breaking a chain of one or more symbolic links to an RCS file, it unlinks the destination file instead. Therefore, <code>ci</code> breaks any hard or symbolic links to any working file it changes; and hard links to RCS files are ineffective, but symbolic links to RCS files are preserved. </p>
<p> The effective user must be able to search and write the directory containing the RCS file. Normally, the real user must be able to read the RCS and working files and to search and write the directory containing the working file; however, some older hosts cannot easily switch between real and effective users, so on these hosts the effective user is used for all accesses. The effective user is the same as the real user unless your copies of <code>ci</code> and <code>co</code> have setuid privileges. As described in the next section, these privileges yield extra security if the effective user owns all RCS files and directories, and if only the effective user can write RCS directories. </p>
<p> Users can control access to RCS files by setting the permissions of the directory containing the files; only users with write access to the directory can use RCS commands to change its RCS files. For example, in hosts that allow a user to belong to several groups, one can make a group&#8217;s RCS directories writable to that group only. This approach suffices for informal projects, but it means that any group member can arbitrarily change the group&#8217;s RCS files, and can even remove them entirely. Hence more formal projects sometimes distinguish between an RCS administrator, who can change the RCS files at will, and other project members, who can check in new revisions but cannot otherwise change the RCS files.</p>
<h2>SETUID USE</h2>
<p> To prevent anybody but their RCS administrator from deleting revisions, a set of users can employ setuid privileges as follows.</p>
<dl>
<dt>&bull;</dt>
<dd> Check that the host supports RCS setuid use. Consult a trustworthy expert if there are any doubts. It is best if the <code>seteuid</code> system call works as described in Posix 1003.1a Draft 5, because RCS can switch back and forth easily between real and effective users, even if the real user is <code>root</code>. If not, the second best is if the <code>setuid</code> system call supports saved setuid (the {_POSIX_SAVED_IDS} behavior of Posix 1003.1-1990); this fails only if the real or effective user is <code>root</code>. If RCS detects any failure in setuid, it quits immediately.</dd>
<dt>&bull;</dt>
<dd> Choose a user <i>A</i> to serve as RCS administrator for the set of users. Only <i>A</i> can invoke the <code>rcs</code> command on the users&#8217; RCS files. <i>A</i> should not be <code>root</code> or any other user with special powers. Mutually suspicious sets of users should use different administrators.</dd>
<dt>&bull;</dt>
<dd> Choose a file name <i>B</i> to be a directory of files to be executed by the users.</dd>
<dt>&bull;</dt>
<dd> Have <i>A</i> set up <i>B</i> to contain copies of <code>ci</code> and <code>co</code> that are setuid to <i>A</i> by copying the commands from their standard installation directory <i>D</i> as follows:</dd></dl>
<dl>
<dt>
</dt><dd>
<pre><code>
mkdir B
            cp D /
        c[io] B
            chmod go -
    w,
    u + s B / c[io]
</code></pre>
</dd></dl>
<dl>
<dt>&bull;</dt>
<dd> Have each user prepend <i>B</i> to their command search path as follows:</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
<code>PATH=</code><i>B</i><code>:$PATH;  export  PATH</code>  # ordinary shell
<code>set  path=(</code><i>B</i>  <code>$path)</code>  # C shell
</pre>
</dd></dl>
<dl>
<dt>&bull;</dt>
<dd> Have <i>A</i> create each RCS directory <i>R</i> with write access only to <i>A</i> as follows:</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
<code>mkdir</code>  <i>R</i>
<code>chmod  go-w</code>  <i>R</i>
</pre>
</dd></dl>
<dl>
<dt>&bull;</dt>
<dd> If you want to let only certain users read the RCS files, put the users into a group <i>G</i>, and have <i>A</i> further protect the RCS directory as follows:</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
<code>chgrp</code>  <i>G  R</i>
<code>chmod  g-w,o-rwx</code>  <i>R</i>
</pre>
</dd></dl>
<dl>
<dt>&bull;</dt>
<dd> Have <i>A</i> copy old RCS files (if any) into <i>R</i>, to ensure that <i>A</i> owns them.</dd>
<dt>&bull;</dt>
<dd> An RCS file&#8217;s access list limits who can check in and lock revisions. The default access list is empty, which grants checkin access to anyone who can read the RCS file. If you want limit checkin access, have <i>A</i> invoke <code>rcs -a</code> on the file; see <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1). In particular, <code>rcs -e -a</code><i>A</i> limits access to just <i>A</i>.</dd>
<dt>&bull;</dt>
<dd> Have <i>A</i> initialize any new RCS files with <code>rcs -i</code> before initial checkin, adding the <code>-a</code> option if you want to limit checkin access.</dd>
<dt>&bull;</dt>
<dd> Give setuid privileges only to <code>ci</code>, <code>co</code>, and <code>rcsclean</code>; do not give them to <code>rcs</code> or to any other command.</dd>
<dt>&bull;</dt>
<dd> Do not use other setuid commands to invoke RCS commands; setuid is trickier than you think!</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>RCSINIT</code></dt>
<dd> Options prepended to the argument list, separated by spaces. A backslash escapes spaces within an option. The <code>RCSINIT</code> options are prepended to the argument lists of most RCS commands. Useful <code>RCSINIT</code> options include <code>-q</code>, <code>-V</code>, <code>-x</code>, and <code>-z</code>.</dd>
<dt><code>RCS_MEM_LIMIT</code></dt>
<dd> An integer <i>lim</i>, measured in kilobytes, specifying the threshold under which commands will try to use memory-based operations for processing the RCS file. (For RCS files of size <i>lim</i> kilobytes or greater, RCS will use the slower standard input/output routines.) Default value is 256.</dd>
<dt><code>TMPDIR</code></dt>
<dd> Name of the temporary directory. If not set, the environment variables <code>TMP</code> and <code>TEMP</code> are inspected instead and the first value found is taken; if none of them are set, a host-dependent default is used, typically <code>/tmp</code>.</dd></dl>
<h2>DIAGNOSTICS</h2>
<p> For each revision, <code>ci</code> prints the RCS file, the working file, and the number of both the deposited and the preceding revision. The exit status is zero if and only if all operations were successful.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br/>
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br/>
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br/>
 Copyright &#169; 1990, 1991, 1992, 1993, 1994, 1995 Paul Eggert.<br/>
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1), <code><a href="/docs/linux/man/1-ident/">ident</a></code>(1), <code><a href="/docs/linux/man/1-make/">make</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsclean/">rcsclean</a></code>(1), <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/5-rcsfile/">rcsfile</a></code>(5). </p>
<p> Walter F. Tichy, RCS&#8211;A System for Version Control, <i>Software&#8211;Practice &amp; Experience</i> <code>15</code>, 7 (July 1985), 637-654. </p>
<p> The full documentation for RCS is maintained as a Texinfo manual. If the <code><a href="/docs/linux/man/1-info/">info</a></code>(1) and RCS programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info rcs</code></dd></dl>
<p> should give you access to the complete manual. Additionally, the RCS homepage:</p>
<dl>
<dt>
</dt><dd> <code><a rel="nofollow" href="http://www.gnu.org/software/rcs/">http://www.gnu.org/software/rcs/</a></code></dd></dl>
<p> has news and links to the latest release, development site, etc. </p>
