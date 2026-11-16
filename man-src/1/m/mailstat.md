---
title: "mailstat(1)"
name: "mailstat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mailstat/"
description: "mailstat – shows mail-arrival statistics"
---

<h2 class="name">NAME</h2>
<p> mailstat &#8211; shows mail-arrival statistics </p>
<h2>SYNOPSIS</h2>
<p> <code>mailstat</code> [-klmots] [logfile]</p>
<h2>DESCRIPTION</h2>
<p> <code>mailstat</code> parses a procmail-generated $LOGFILE and displays a summary about the messages delivered to all folders (total size, average size, nr of messages). The $LOGFILE is truncated to zero length, unless the <code>-k</code> option is used. Exit code 0 if mail arrived, 1 if no mail arrived.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-k</i></dt>
<dd> keep logfile intact</dd>
<dt><i>-l</i></dt>
<dd> long display format</dd>
<dt><i>-m</i></dt>
<dd> merge any errors into one line</dd>
<dt><i>-o</i></dt>
<dd> use the old logfile</dd>
<dt><i>-t</i></dt>
<dd> terse display format</dd>
<dt><i>-s</i></dt>
<dd> silent in case of no mail</dd></dl>
<h2>NOTES</h2>
<p> Customise to your heart&#8217;s content, this program is only provided as a guideline.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Santiago Vila &lt;sanvila [at] debian.org&gt; for the Debian GNU/Linux distribution (but may be used by others). </p>
<h2>Index</h2>
