---
title: "dspam_logrotate(1)"
name: "dspam_logrotate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dspam_logrotate/"
description: "dspam_logrotate – Rotate DSPAM logfiles"
---

<h2 class="name">NAME</h2>
<p> dspam_logrotate &#8211; Rotate DSPAM logfiles</p>
<h2>SYNOPSIS</h2>
<p> <code>dspam_logrotate</code> <code>-a age </code>[-v]&nbsp;<wbr>[[<code>-l </code>[<i>logfile</i>]]|[<code>-d </code>[<i>dir</i>]]] </p>
<h2>DESCRIPTION</h2>
<p> <code>dspam_logrotate</code> can be used to rotate DSPAM system log and/or the user logs. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a age</code></p>
<dd> All log entries older than &#8216;age&#8217; days will be removed. </p>
<dt><code>-v</code></p>
<dd> Print verbose output. </p>
<dt><code>-l</code><i>&nbsp;<wbr>logfile</i></p>
<dd> A list of one or more files to process. </p>
<dt><code>-d</code><i>&nbsp;<wbr>dir</i></p>
<dd> The home directory of DSPAM or the root path where user logs are located. </p>
</dl>
<h2>EXIT VALUE</h2>
<dl>
<dt><code>0</code></p>
<dd> Operation was successful.</p>
<dt><code>other</code></p>
<dd> Operation resulted in an error. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 DSPAM Project<br />
 All rights reserved. </p>
<p> For more information, see <a rel="nofollow" href="http://dspam.sourceforge.net.">http://dspam.sourceforge.net.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dspam/">dspam</a></code>(1), <code><a href="/docs/linux/man/1-dspam_admin/">dspam_admin</a></code>(1), <code><a href="/docs/linux/man/1-dspam_clean/">dspam_clean</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_dump/">dspam_dump</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_stats/">dspam_stats</a></code>(1), <code><a href="/docs/linux/man/1-dspam_train/">dspam_train</a></code>(1) </p>
<h2>Index</h2>
