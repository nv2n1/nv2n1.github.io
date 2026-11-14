---
title: "octave-bug(1)"
name: "octave-bug"
section: "1"
letter: "o"
url: "/docs/linux/man/1-octave-bug/"
description: "octave-bug – report a bug in GNU Octave"
---

<h2>NAME</h2>
<p> octave-bug &#8211; report a bug in GNU Octave</p>
<h2>SYNOPSIS</h2>
<p> <code>octave-bug</code> [<code>-s</code> <i>subject</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>octave-bug</code> is a shell script to help the user compose and mail bug reports concerning Octave in a standard format. <code>octave-bug</code> is typically invoked by the Octave command <code>bug_report</code> which is intended to be called interactively from within Octave. This provides the best way to submit a bug report for Octave. It creates a template bug report file and starts an editor on that file. The bug report will be sent to the bug-octave mailing list once the editing has been completed (this assumes of course that your system can use email). However, the user could also call <code>octave-bug</code> outside of Octave. </p>
<p> Please read the `Bugs&#8217; chapter in the Octave manual to find out how to submit a bug report that will enable the Octave maintainers to fix the problem. If you are unable to use the bug_report command, send your message to the bug-octave mailing list, bug [at] octave.org.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s&nbsp;<wbr></code><i>subject</i></p>
<dd> Specify a subject line for the bug report. Spaces in the subject must be quoted.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>octave-bug </code> uses the environment variables <code>USER,</code> <code>EDITOR,</code> and <code>PAGER </code> which can be used for customization.</p>
<h2>VERSION</h2>
<p> This document was last revised for Octave version 2.0.16.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-octave/">octave</a></code>(1), <code><a href="/docs/linux/man/1-bashbug/">bashbug</a></code>(1)</p>
<h2>AUTHOR</h2>
<pre>
John W. Eaton
&lt;jwe [at] octave.org&gt;
</pre>
<h2>Index</h2>
