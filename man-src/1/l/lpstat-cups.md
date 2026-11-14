---
title: "lpstat-cups(1)"
name: "lpstat-cups"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpstat-cups/"
description: "lpstat – print cups status information"
---

<h2>NAME</h2>
<p> lpstat &#8211; print cups status information</p>
<h2>SYNOPSIS</h2>
<p> <code>lpstat</code> [ -E ] [ -H ] [ -U <i>username</i> ] [ -h <i>hostname[:port]</i> ] [ -l ] [ -W <i>which-jobs</i> ] [ -a [ <i>destination(s)</i> ] ] [ -c [ <i>class(es)</i> ] ] [ -d ] [ -o [ <i>destination(s)</i> ] ] [ -p [ <i>printer(s)</i> ] ] [ -r ] [ -R ] [ -s ] [ -t ] [ -u [ <i>user(s)</i> ] ] [ -v [ <i>printer(s)</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>lpstat</i> displays status information about the current classes, jobs, and printers. When run with no arguments, <i>lpstat</i> will list jobs queued by the current user.</p>
<h2>OPTIONS</h2>
<p> The <i>lpstat</i> command supports the following options:</p>
<dl>
<dt>-E</p>
<dd>
 Forces encryption when connecting to the server.</p>
<dt>-H</p>
<dd>
 Shows the server hostname and port.</p>
<dt>-R</p>
<dd>
 Shows the ranking of print jobs.</p>
<dt>-U username</p>
<dd>
 Specifies an alternate username.</p>
<dt>-W which-jobs</p>
<dd>
 Specifies which jobs to show, <i>completed</i> or <i>not-completed</i> (the default). This option <i>must</i> appear before the <i>-o</i> option and/or any printer names, otherwise the default (not-completed) value will be used in the request to the scheduler.</p>
<dt>-a [printer(s)]</p>
<dd>
 Shows the accepting state of printer queues. If no printers are specified then all printers are listed.</p>
<dt>-c [class(es)]</p>
<dd>
 Shows the printer classes and the printers that belong to them. If no classes are specified then all classes are listed.</p>
<dt>-d</p>
<dd>
 Shows the current default destination.</p>
<dt>-h server[:port]</p>
<dd>
 Specifies an alternate server.</p>
<dt>-l</p>
<dd>
 Shows a long listing of printers, classes, or jobs.</p>
<dt>-o [destination(s)]</p>
<dd>
 Shows the jobs queue on the specified destinations. If no destinations are specified all jobs are shown.</p>
<dt>-p [printer(s)]</p>
<dd>
 Shows the printers and whether or not they are enabled for printing. If no printers are specified then all printers are listed.</p>
<dt>-r</p>
<dd>
 Shows whether the CUPS server is running.</p>
<dt>-s</p>
<dd>
 Shows a status summary, including the default destination, a list of classes and their member printers, and a list of printers and their associated devices. This is equivalent to using the &quot;-d&quot;, &quot;-c&quot;, and &quot;-v&quot; options.</p>
<dt>-t</p>
<dd>
 Shows all status information. This is equivalent to using the &quot;-r&quot;, &quot;-d&quot;, &quot;-c&quot;, &quot;-v&quot;, &quot;-a&quot;, &quot;-p&quot;, and &quot;-o&quot; options.</p>
<dt>-u [user(s)]</p>
<dd>
 Shows a list of print jobs queued by the specified users. If no users are specified, lists the jobs queued by the current user.</p>
<dt>-v [printer(s)]</p>
<dd>
 Shows the printers and what device they are attached to. If no printers are specified then all printers are listed.</dl>
<h2>COMPATIBILITY</h2>
<p> Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, and &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive. </p>
<p> The &quot;-h&quot;, &quot;-E&quot;, &quot;-U&quot;, and &quot;-W&quot; options are unique to CUPS. </p>
<p> The Solaris &quot;-f&quot;, &quot;-P&quot;, and &quot;-S&quot; options are silently ignored.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-cancel/">cancel</a>(1)</i>, <i><a href="/docs/linux/man/1-lp/">lp</a>(1)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2013 by Apple Inc. </p>
<h2>Index</h2>
