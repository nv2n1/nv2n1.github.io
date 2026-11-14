---
title: "rcsintro(1)"
name: "rcsintro"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcsintro/"
description: "rcsintro – introduction to RCS commands"
---

<h2>NAME</h2>
<p> rcsintro &#8211; introduction to RCS commands</p>
<h2>DESCRIPTION</h2>
<p> The Revision Control System (<font SIZE="-1">RCS</font>) manages multiple revisions of files. <font SIZE="-1">RCS</font> automates the storing, retrieval, logging, identification, and merging of revisions. <font SIZE="-1">RCS</font> is useful for text that is revised frequently, for example programs, documentation, graphics, papers, and form letters. </p>
<p> The basic user interface is extremely simple. The novice only needs to learn two commands: <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1) and <code><a href="/docs/linux/man/1-co/">co</a></code>(1). <code>ci</code>, short for &#8220;check in&#8221;, deposits the contents of a file into an archival file called an <font SIZE="-1">RCS</font> file. An <font SIZE="-1">RCS</font> file contains all revisions of a particular file. <code>co</code>, short for &#8220;check out&#8221;, retrieves revisions from an <font SIZE="-1">RCS</font> file.</p>
<h3>Functions of <font SIZE="-1">RCS</font></h3>
<dl>
<dt>*</p>
<dd> Store and retrieve multiple revisions of text. <font SIZE="-1">RCS</font> saves all old revisions in a space efficient way. Changes no longer destroy the original, because the previous revisions remain accessible. Revisions can be retrieved according to ranges of revision numbers, symbolic names, dates, authors, and states.</p>
<dt>*</p>
<dd> Maintain a complete history of changes. <font SIZE="-1">RCS</font> logs all changes automatically. Besides the text of each revision, <font SIZE="-1">RCS</font> stores the author, the date and time of check-in, and a log message summarizing the change. The logging makes it easy to find out what happened to a module, without having to compare source listings or having to track down colleagues.</p>
<dt>*</p>
<dd> Resolve access conflicts. When two or more programmers wish to modify the same revision, <font SIZE="-1">RCS</font> alerts the programmers and prevents one modification from corrupting the other.</p>
<dt>*</p>
<dd> Maintain a tree of revisions. <font SIZE="-1">RCS</font> can maintain separate lines of development for each module. It stores a tree structure that represents the ancestral relationships among revisions.</p>
<dt>*</p>
<dd> Merge revisions and resolve conflicts. Two separate lines of development of a module can be coalesced by merging. If the revisions to be merged affect the same sections of code, <font SIZE="-1">RCS</font> alerts the user about the overlapping changes.</p>
<dt>*</p>
<dd> Control releases and configurations. Revisions can be assigned symbolic names and marked as released, stable, experimental, etc. With these facilities, configurations of modules can be described simply and directly.</p>
<dt>*</p>
<dd> Automatically identify each revision with name, revision number, creation time, author, etc. The identification is like a stamp that can be embedded at an appropriate place in the text of a revision. The identification makes it simple to determine which revisions of which modules make up a given configuration.</p>
<dt>*</p>
<dd> Minimize secondary storage. <font SIZE="-1">RCS</font> needs little extra space for the revisions (only the differences). If intermediate revisions are deleted, the corresponding deltas are compressed accordingly.</dl>
<h3>Getting Started with <font SIZE="-1">RCS</font></h3>
<p> Suppose you have a file <code>f.c</code> that you wish to put under control of <font SIZE="-1">RCS</font>. If you have not already done so, make an <font SIZE="-1">RCS</font> directory with the command</p>
<dl>
<dt>
<dd> <code>mkdir RCS</code></dl>
<p> Then invoke the check-in command</p>
<dl>
<dt>
<dd> <code>ci f.c</code></dl>
<p> This command creates an <font SIZE="-1">RCS</font> file in the <code>RCS</code> directory, stores <code>f.c</code> into it as revision 1.1, and deletes <code>f.c</code>. It also asks you for a description. The description should be a synopsis of the contents of the file. All later check-in commands will ask you for a log entry, which should summarize the changes that you made. </p>
<p> Files in the <font SIZE="-1">RCS</font> directory are called <font SIZE="-1">RCS</font> files; the others are called working files. To get back the working file <code>f.c</code> in the previous example, use the check-out command</p>
<dl>
<dt>
<dd> <code>co f.c</code></dl>
<p> This command extracts the latest revision from the <font SIZE="-1">RCS</font> file and writes it into <code>f.c</code>. If you want to edit <code>f.c</code>, you must lock it as you check it out with the command</p>
<dl>
<dt>
<dd> <code>co -l f.c</code></dl>
<p> You can now edit <code>f.c</code>. </p>
<p> Suppose after some editing you want to know what changes that you have made. The command</p>
<dl>
<dt>
<dd> <code>rcsdiff f.c</code></dl>
<p> tells you the difference between the most recently checked-in version and the working file. You can check the file back in by invoking</p>
<dl>
<dt>
<dd> <code>ci f.c</code></dl>
<p> This increments the revision number properly. </p>
<p> If <code>ci</code> complains with the message</p>
<dl>
<dt>
<dd> <code>ci error: no lock set by </code><i>your name</i></dl>
<p> then you have tried to check in a file even though you did not lock it when you checked it out. Of course, it is too late now to do the check-out with locking, because another check-out would overwrite your modifications. Instead, invoke</p>
<dl>
<dt>
<dd> <code>rcs -l f.c</code></dl>
<p> This command will lock the latest revision for you, unless somebody else got ahead of you already. In this case, you&#8217;ll have to negotiate with that person. </p>
<p> Locking assures that you, and only you, can check in the next update, and avoids nasty problems if several people work on the same file. Even if a revision is locked, it can still be checked out for reading, compiling, etc. All that locking prevents is a <i>check-in</i> by anybody but the locker. </p>
<p> If your <font SIZE="-1">RCS</font> file is private, i.e., if you are the only person who is going to deposit revisions into it, strict locking is not needed and you can turn it off. If strict locking is turned off, the owner of the <font SIZE="-1">RCS</font> file need not have a lock for check-in; all others still do. Turning strict locking off and on is done with the commands</p>
<dl>
<dt>
<dd> <code>rcs -U f.c</code> and <code>rcs -L f.c</code></dl>
<p> If you don&#8217;t want to clutter your working directory with <font SIZE="-1">RCS</font> files, create a subdirectory called <code>RCS</code> in your working directory, and move all your <font SIZE="-1">RCS</font> files there. <font SIZE="-1">RCS</font> commands will look first into that directory to find needed files. All the commands discussed above will still work, without any modification. (Actually, pairs of <font SIZE="-1">RCS</font> and working files can be specified in three ways: (a) both are given, (b) only the working file is given, (c) only the <font SIZE="-1">RCS</font> file is given. Both <font SIZE="-1">RCS</font> and working files may have arbitrary path prefixes; <font SIZE="-1">RCS</font> commands pair them up intelligently.) </p>
<p> To avoid the deletion of the working file during check-in (in case you want to continue editing or compiling), invoke</p>
<dl>
<dt>
<dd> <code>ci -l f.c</code> or <code>ci -u f.c</code></dl>
<p> These commands check in <code>f.c</code> as usual, but perform an implicit check-out. The first form also locks the checked in revision, the second one doesn&#8217;t. Thus, these options save you one check-out operation. The first form is useful if you want to continue editing, the second one if you just want to read the file. Both update the identification markers in your working file (see below). </p>
<p> You can give <code>ci</code> the number you want assigned to a checked in revision. Assume all your revisions were numbered 1.1, 1.2, 1.3, etc., and you would like to start release 2. The command</p>
<dl>
<dt>
<dd> <code>ci -r2 f.c</code> or <code>ci -r2.1 f.c</code></dl>
<p> assigns the number 2.1 to the new revision. From then on, <code>ci</code> will number the subsequent revisions with 2.2, 2.3, etc. The corresponding <code>co</code> commands</p>
<dl>
<dt>
<dd> <code>co -r2 f.c</code> and <code>co -r2.1 f.c</code></dl>
<p> retrieve the latest revision numbered 2.<i>x</i> and the revision 2.1, respectively. <code>co</code> without a revision number selects the latest revision on the <i>trunk</i>, i.e. the highest revision with a number consisting of two fields. Numbers with more than two fields are needed for branches. For example, to start a branch at revision 1.3, invoke</p>
<dl>
<dt>
<dd> <code>ci -r1.3.1 f.c</code></dl>
<p> This command starts a branch numbered 1 at revision 1.3, and assigns the number 1.3.1.1 to the new revision. For more information about branches, see <code><a href="/docs/linux/man/5-rcsfile/">rcsfile</a></code>(5).</p>
<h3>Automatic Identification</h3>
<p> <font SIZE="-1">RCS</font> can put special strings for identification into your source and object code. To obtain such identification, place the marker</p>
<dl>
<dt>
<dd> <code>$Id$</code></dl>
<p> into your text, for instance inside a comment. <font SIZE="-1">RCS</font> will replace this marker with a string of the form</p>
<dl>
<dt>
<dd> <code>$Id:</code><i> filename revision date time author state </i><code>$</code></dl>
<p> With such a marker on the first page of each module, you can always see with which revision you are working. <font SIZE="-1">RCS</font> keeps the markers up to date automatically. To propagate the markers into your object code, simply put them into literal character strings. In C, this is done as follows:</p>
<dl>
<dt>
<dd> <code> static char rcsid[] = &quot;$Id$&quot;; </code></dl>
<p> The command <code>ident</code> extracts such markers from any file, even object code and dumps. Thus, <code>ident</code> lets you find out which revisions of which modules were used in a given program. </p>
<p> You may also find it useful to put the marker <code>$Log$</code> into your text, inside a comment. This marker accumulates the log messages that are requested during check-in. Thus, you can maintain the complete history of your file directly inside it. There are several additional identification markers; see <code><a href="/docs/linux/man/1-co/">co</a></code>(1) for details.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.3; Release Date: 1993/11/03.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy.<br />
 Copyright &#169; 1990, 1991, 1992, 1993 Paul Eggert.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ci/">ci</a>(1), <a href="/docs/linux/man/1-co/">co</a>(1), <a href="/docs/linux/man/1-ident/">ident</a>(1), <a href="/docs/linux/man/1-rcs/">rcs</a>(1), <a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a>(1), <a href="/docs/linux/man/1-rcsintro/">rcsintro</a>(1), <a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a>(1), <a href="/docs/linux/man/1-rlog/">rlog</a>(1)<br />
 Walter F. Tichy, <font SIZE="-1">RCS</font>&#8211;A System for Version Control, <i>Software&#8211;Practice &amp; Experience</i> <code>15</code>, 7 (July 1985), 637-654. </p>
<h2>Index</h2>
<dt><a href="#lbAG">IDENTIFICATION</a></p>
<dd>
<dt><a href="#lbAH">SEE ALSO</a></p>
<dd></dl>
