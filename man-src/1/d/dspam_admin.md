---
title: "dspam_admin(1)"
name: "dspam_admin"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dspam_admin/"
description: "dspam_admin – Alter DSPAM users preferences"
---

<h2 class="name">NAME</h2>
<p> dspam_admin &#8211; Alter DSPAM users preferences</p>
<h2>SYNOPSIS</h2>
<p> <code>dspam_admin</code> [<code>&#8211;profile</code>=PROFILE] [<i>function</i>] [<i>argument</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>dspam_admin</code> is used to alter DSPAM user&#8217;s preferences. </p>
<h2>OPTIONS</h2>
<dl>
<dt>Add a Preference:</p>
<dd><code>add preference&nbsp;<wbr></code>[<i>user</i>] [<i>attrib</i>] [<i>value</i>]</p>
<dt>Set/change a Preference:</p>
<dd><code>change preference&nbsp;<wbr></code>[<i>user</i>] [<i>attrib</i>] [<i>value</i>]</p>
<dt>Delete a Preference:</p>
<dd><code>delete preference&nbsp;<wbr></code>[<i>user</i>] [<i>attrib</i>] [<i>value</i>]</p>
<dt>List Preferences:</p>
<dd><code>list preference&nbsp;<wbr></code>[<i>user</i>] [<i>attrib</i>] [<i>value</i>]</p>
<dt>Aggregate Preferences:</p>
<dd><code>aggregate preference&nbsp;<wbr></code>[<i>user</i>]</p>
</dl>
<p> Use&nbsp;<wbr><code>default&nbsp;<wbr></code>as username to modify the default (uid 0) user preference. </p>
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
<p> <code><a href="/docs/linux/man/1-dspam/">dspam</a></code>(1), <code><a href="/docs/linux/man/1-dspam_clean/">dspam_clean</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_dump/">dspam_dump</a></code>(1), <code><a href="/docs/linux/man/1-dspam_logrotate/">dspam_logrotate</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_stats/">dspam_stats</a></code>(1), <code><a href="/docs/linux/man/1-dspam_train/">dspam_train</a></code>(1) </p>
<h2>Index</h2>
