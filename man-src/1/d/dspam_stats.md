---
title: "dspam_stats(1)"
name: "dspam_stats"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dspam_stats/"
description: "dspam_stats – display spam statistics"
---

<h2 class="name">NAME</h2>
<p> dspam_stats &#8211; display spam statistics</p>
<h2>SYNOPSIS</h2>
<p> <code>dspam_stats</code> [<code>&#8211;profile</code>=PROFILE][<code>-HhrSst</code>] [<i>username</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>dspam_stats</code> displays the spam filtering statistics for one or all users on the system. Displays TP (True Positives (Spam)), TN (True Negatives (Innocent)), FP (False Positives), FN (False Negatives), SC (Spam Corpusfed) and NC (Nonspam Corpusfed). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&nbsp;<wbr>&#8211;profile=</code><i>PROFILE</i></p>
<dd> Specify a storage profile from dspam.conf. The storage profile selected will be used for all database connectivity. See dspam.conf for more information. </p>
<dt><code>-H</code></p>
<dd> Uses multi-line, human-readable output displaying the fully-qualified names for each class of totals, instead of their abbreviated terms.<br />
&nbsp;<wbr></p>
<dt><code>-h</code></p>
<dd> Displays help syntax </p>
<dt><code>-r</code></p>
<dd> Resets the current snapshot </p>
<dt><code>-s</code></p>
<dd> Displays stats since last snapshot (instead of since epoch) </p>
<dt><code>-S</code></p>
<dd> Displays accuracy percentages in addition to stats </p>
<dt><code>-t</code></p>
<dd> Displays a total of all statistics displayed </p>
<dt><code>[username]</code></p>
<dd> Specifies the username to query. If no username is provided, all users will be queried. </p>
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
<p> <code><a href="/docs/linux/man/1-dspam/">dspam</a></code>(1), <code><a href="/docs/linux/man/1-dspam_admin/">dspam_admin</a></code>(1), <code><a href="/docs/linux/man/1-dspam_clean/">dspam_clean</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_dump/">dspam_dump</a></code>(1), <code><a href="/docs/linux/man/1-dspam_logrotate/">dspam_logrotate</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_train/">dspam_train</a></code>(1) </p>
<h2>Index</h2>
