---
title: "rcsfreeze(1)"
name: "rcsfreeze"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcsfreeze/"
description: "rcsfreeze – freeze a configuration of sources checked in under RCS"
---

<h2>NAME</h2>
<p> rcsfreeze &#8211; freeze a configuration of sources checked in under RCS</p>
<h2>SYNOPSIS</h2>
<p> <code>rcsfreeze</code> [<i>name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>rcsfreeze</code> assigns a symbolic revision number to a set of <font SIZE="-1">RCS</font> files that form a valid configuration. </p>
<p> The idea is to run <code>rcsfreeze</code> each time a new version is checked in. A unique symbolic name (<code>C_</code><i>number,</i> where <i>number</i> is increased each time <code>rcsfreeze</code> is run) is then assigned to the most recent revision of each <font SIZE="-1">RCS</font> file of the main trunk. </p>
<p> An optional <i>name</i> argument to <code>rcsfreeze</code> gives a symbolic name to the configuration. The unique identifier is still generated and is listed in the log file but it will not appear as part of the symbolic revision name in the actual <font SIZE="-1">RCS</font> files. </p>
<p> A log message is requested from the user for future reference. </p>
<p> The shell script works only on all <font SIZE="-1">RCS</font> files at one time. All changed files must be checked in already. Run <i><a href="/docs/linux/man/1-rcsclean/">rcsclean</a></i>(1) first and see whether any sources remain in the current directory.</p>
<h2>FILES</h2>
<dl>
<dt><code>RCS/.rcsfreeze.ver</code></p>
<dd> version number</p>
<dt><code>RCS/.rcsfreeze.log</code></p>
<dd> log messages, most recent first</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>RCSINIT</code></font></p>
<dd> Options prepended to the argument list, separated by spaces. A backslash escapes spaces within an option. The <font SIZE="-1"><code>RCSINIT</code></font> options are prepended to the argument lists of most <font SIZE="-1">RCS</font> commands. Useful <font SIZE="-1"><code>RCSINIT</code></font> options include <code>-q</code>, <code>-V</code>, <code>-x</code>, and <code>-z</code>.</p>
<dt><font SIZE="-1"><code>RCS_MEM_LIMIT</code></font></p>
<dd> An integer <i>lim</i>, measured in kilobytes, specifying the threshold under which commands will try to use memory-based operations for processing the <font SIZE="-1">RCS</font> file. (For <font SIZE="-1">RCS</font> files of size <i>lim</i> kilobytes or greater, RCS will use the slower standard input/output routines.) Default value is 256.</p>
<dt><font SIZE="-1"><code>TMPDIR</code></font></p>
<dd> Name of the temporary directory. If not set, the environment variables <font SIZE="-1"><code>TMP</code></font> and <font SIZE="-1"><code>TEMP</code></font> are inspected instead and the first value found is taken; if none of them are set, a host-dependent default is used, typically <code>/tmp</code>.</dl>
<h2>AUTHOR</h2>
<p> Stephan v. Bechtolsheim</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsclean/">rcsclean</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1). </p>
<p> Walter F. Tichy, <font SIZE="-1">RCS</font>A System for Version Control, <i>SoftwarePractice &amp; Experience</i> <code>15</code>, 7 (July 1985), 637-654. </p>
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
<p> <code>rcsfreeze</code> does not check whether any sources are checked out and modified. </p>
<p> Although both working and <font SIZE="-1">RCS</font> file names are accepted, they are not paired as usual with RCS commands. </p>
<p> Error checking is rudimentary. </p>
<p> <code>rcsfreeze</code> is just an optional example shell script, and should not be taken too seriously. See <font SIZE="-1">CVS</font> for a more complete solution. </p>
<h2>Index</h2>
