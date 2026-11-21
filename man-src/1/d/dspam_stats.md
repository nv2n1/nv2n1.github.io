---

title: "dspam_stats(1)"
name: "dspam_stats"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dspam_stats/"
description: "dspam_stats – display spam statistics"
---

<p> <code>dspam_stats</code> [<code>&#8211;profile</code>=PROFILE][<code>-HhrSst</code>] [<i>username</i>] </p>
<p> <code>dspam_stats</code> displays the spam filtering statistics for one or all users on the system. Displays TP (True Positives (Spam)), TN (True Negatives (Innocent)), FP (False Positives), FN (False Negatives), SC (Spam Corpusfed) and NC (Nonspam Corpusfed). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&nbsp;<wbr>&#8211;profile=</code><i>PROFILE</i></dt>
<dd> Specify a storage profile from dspam.conf. The storage profile selected will be used for all database connectivity. See dspam.conf for more information. </dd>
<dt><code>-H</code></dt>
<dd> Uses multi-line, human-readable output displaying the fully-qualified names for each class of totals, instead of their abbreviated terms.<br />
&nbsp;<wbr></dd>
<dt><code>-h</code></dt>
<dd> Displays help syntax </dd>
<dt><code>-r</code></dt>
<dd> Resets the current snapshot </dd>
<dt><code>-s</code></dt>
<dd> Displays stats since last snapshot (instead of since epoch) </dd>
<dt><code>-S</code></dt>
<dd> Displays accuracy percentages in addition to stats </dd>
<dt><code>-t</code></dt>
<dd> Displays a total of all statistics displayed </dd>
<dt><code>[username]</code></dt>
<dd> Specifies the username to query. If no username is provided, all users will be queried. </dd>
</dl>
<h2>EXIT VALUE</h2>
<dl>
<dt><code>0</code></dt>
<dd> Operation was successful.</dd>
<dt><code>other</code></dt>
<dd> Operation resulted in an error. </dd>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 DSPAM Project<br />
 All rights reserved. </p>
<p> For more information, see <a rel="nofollow" href="http://dspam.sourceforge.net.">http://dspam.sourceforge.net.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dspam/">dspam</a></code>(1), <code><a href="/docs/linux/man/1-dspam_admin/">dspam_admin</a></code>(1), <code><a href="/docs/linux/man/1-dspam_clean/">dspam_clean</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_dump/">dspam_dump</a></code>(1), <code><a href="/docs/linux/man/1-dspam_logrotate/">dspam_logrotate</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_train/">dspam_train</a></code>(1) </p>
