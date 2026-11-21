---
title: "lpstat(1)"
name: "lpstat"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpstat/"
description: "lpstat – print cups status information"
---

<h2 class="name">NAME</h2>
<p> lpstat &#8211; print cups status information </p>
<h2>SYNOPSIS</h2>
<p> <code>lpstat</code> [ <code>-E</code> ] [ <code>-H</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h </code><i>hostname</i>[<code>:</code><i>port</i>] ] [ <code>-l</code> ] [ <code>-W</code> <i>which-jobs</i> ] [ <code>-a</code> [ <i>destination(s)</i> ] ] [ <code>-c</code> [ <i>class(es)</i> ] ] [ <code>-d</code> ] [ <code>-e</code> ] [ <code>-o</code> [ <i>destination(s)</i> ] ] [ <code>-p</code> [ <i>printer(s)</i> ] ] [ <code>-r</code> ] [ <code>-R</code> ] [ <code>-s</code> ] [ <code>-t</code> ] [ <code>-u</code> [ <i>user(s)</i> ] ] [ <code>-v</code> [ <i>printer(s)</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lpstat</code> displays status information about the current classes, jobs, and printers. When run with no arguments, <code>lpstat</code> will list active jobs queued by the current user.</p>
<h2>OPTIONS</h2>
<p> The <code>lpstat</code> command supports the following options:</p>
<dl>
<dt><code>-E</code></dt>
<dd> Forces encryption when connecting to the server.</dd>
<dt><code>-H</code></dt>
<dd> Shows the server hostname and port.</dd>
<dt><code>-R</code></dt>
<dd> Shows the ranking of print jobs.</dd>
<dt><code>-U </code><i>username</i></dt>
<dd> Specifies an alternate username.</dd>
<dt><code>-W </code><i>which-jobs</i></dt>
<dd> Specifies which jobs to show, &quot;completed&quot; or &quot;not-completed&quot; (the default). This option <i>must</i> appear before the <i>-o</i> option and/or any printer names, otherwise the default (&quot;not-completed&quot;) value will be used in the request to the scheduler.</dd>
<dt><code>-a </code>[<i>printer(s)</i>]</dt>
<dd> Shows the accepting state of printer queues. If no printers are specified then all printers are listed.</dd>
<dt><code>-c </code>[<i>class(es)</i>]</dt>
<dd> Shows the printer classes and the printers that belong to them. If no classes are specified then all classes are listed.</dd>
<dt><code>-d</code></dt>
<dd> Shows the current default destination.</dd>
<dt><code>-e</code></dt>
<dd> Shows all available destinations on the local network.</dd>
<dt><code>-h </code><i>server</i>[<code>:</code><i>port</i>]</dt>
<dd> Specifies an alternate server.</dd>
<dt><code>-l</code></dt>
<dd> Shows a long listing of printers, classes, or jobs.</dd>
<dt><code>-o </code>[<i>destination(s)</i>]</dt>
<dd> Shows the jobs queued on the specified destinations. If no destinations are specified all jobs are shown.</dd>
<dt><code>-p </code>[<i>printer(s)</i>]</dt>
<dd> Shows the printers and whether they are enabled for printing. If no printers are specified then all printers are listed.</dd>
<dt><code>-r</code></dt>
<dd> Shows whether the CUPS server is running.</dd>
<dt><code>-s</code></dt>
<dd> Shows a status summary, including the default destination, a list of classes and their member printers, and a list of printers and their associated devices. This is equivalent to using the <i>-d</i>, <i>-c</i>, and <i>-v</i> options.</dd>
<dt><code>-t</code></dt>
<dd> Shows all status information. This is equivalent to using the <i>-r</i>, <i>-d</i>, <i>-c</i>, <i>-v</i>, <i>-a</i>, <i>-p</i>, and <i>-o</i> options.</dd>
<dt><code>-u </code>[<i>user(s)</i>]</dt>
<dd> Shows a list of print jobs queued by the specified users. If no users are specified, lists the jobs queued by the current user.</dd>
<dt><code>-v </code>[<i>printer(s)</i>]</dt>
<dd> Shows the printers and what device they are attached to. If no printers are specified then all printers are listed.</dd></dl>
<h2>CONFORMING TO</h2>
<p> Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, and &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive. </p>
<p> The <i>-h</i>, <i>-e</i>, <i>-E</i>, <i>-U</i>, and <i>-W</i> options are unique to CUPS. </p>
<p> The Solaris <i>-f</i>, <i>-P</i>, and <i>-S</i> options are silently ignored.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/1-lpq/">lpq</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
