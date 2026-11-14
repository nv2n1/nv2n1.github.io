---
title: "lintian-info(1)"
name: "lintian-info"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lintian-info/"
description: "lintian-info – give detailed information about Lintian’s error tags"
---

<h2 class="name">NAME</h2>
<p> lintian-info &#8211; give detailed information about Lintian&#8217;s error tags </p>
<h2>SYNOPSIS</h2>
<p> <code>lintian-info</code> [<i>log-file</i>&#8230;] </p>
<p> <code>lintian-info</code> <code>&#8211;tags</code> <i>tag</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>lintian-info</code> command parses the output of the <code>lintian</code> command and gives verbose information about the listed Lintian error tags, parses a Lintian override file and gives verbose information about the tags included, or (if given the <code>-t</code> or <code>&#8211;tags</code> option) explains a given tag or tags. </p>
<p> If no log-file is specified on the command line, this command expects its input on stdin. Thus, the output of <code>lintian</code> can either be piped through <code>lintian-info</code> or a log file produced by <code>lintian</code> can be processed with this command. (Note, though, that the <code>lintian</code> command has a command line option <code>-i</code> to display the same results as <code>lintian-info</code>, so you will not normally need to pipe the output of <code>lintian</code> into this command.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;annotate</code></p>
<dd> Read from standard input or any files specified on the command line and search the input for lines formatted like Lintian override entries. For each one that was found, display verbose information about that tag.</p>
<dt><code>-l</code>, <code>&#8211;list-tags</code></p>
<dd> List all tags Lintian knows about in sorted order.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>&#8211;include-dir</code> dir</p>
<dd> Use dir as an additional &#8220;Lintian root&#8221;. The directory is expected have a similar layout to the <font SIZE="-1">LINTIAN_ROOT</font> (if it exists), but does not need to be a full self-contained root. </p>
<p> Unlike <code>lintian</code>, <code>lintian-info</code> will <i>not</i> load any code from these additional directories. </p>
<p> This option may appear more than once; each time adding an additional directory. </p>
<p> <code>Note</code>: This option should be the very first if given.</p>
<dt><code>&#8211;profile</code> prof</p>
<dd> Use the severities from the vendor profile prof when displaying tags. If the profile name does not contain a slash, the default profile for that vendor is chosen. </p>
<p> If not specified, <code>lintian-info</code> loads the best profile for the current vendor. </p>
<p> Please Refer to the Lintian User Manual for the full documentation of profiles.</p>
<dt><code>-t</code>, <code>&#8211;tag</code>, <code>&#8211;tags</code></p>
<dd> Rather than treating them as log file names, treat any command-line options as tag names and display the descriptions of each tag.</p>
<dt><code>&#8211;user-dirs</code>, <code>&#8211;no-user-dirs</code></p>
<dd> By default, <code>lintian</code> will check <i></i>$HOME<i></i> and <i>/etc</i> for files supplied by the user or the local sysadmin (e.g. profiles). This default can be disabled (and re-enabled) by using <code>&#8211;no-user-dirs</code> (and <code>&#8211;user-dirs</code>, respectively). </p>
<p> These option can appear multiple times, in which case the of them to appear determines the result. </p>
<p> <code>Note</code>: This option should be the very first if given.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>-t</code> or <code>&#8211;tags</code> was given and one or more of the tags specified were unknown, this command returns the exit code 1. Otherwise, it always returns with exit code 0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> Niels Thykier &lt;niels [at] thykier.net&gt; </p>
<p> Richard Braakman &lt;dark [at] xs4all.nl&gt; </p>
<p> Christian Schwarz &lt;schwarz [at] monet.m.isar.de&gt; </p>
<h2>Index</h2>
