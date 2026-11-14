---
title: "incron-conf(5)"
name: "incron-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-incron-conf/"
description: "/etc/incron.conf – main config file for inotify cron (incron)"
---

<p>/etc/incron.conf &#8211; main config file for inotify cron (incron)</p>
<h2>Description</h2>
<p>The file <i>/etc/incron.conf</i> contains default settings for the program <code>incrond.</code> Each line holds a single value pair in the form <i>option</i> = <i>value</i>. Comment lines must have a hash sign (#) in the first line. </p>
<p> The valid configuration options are:</p>
<dl>
<dt><code>system_table_dir</code></p>
<dd>This directory is examined by incrond for system table files. <code>Default</code>:<i>/etc/incron.d</i></p>
<dt><code>user_table_dir</code></p>
<dd>This directory is examined by incrond for user table files. <code>Default</code>:<i>/var/spool/incron</i></p>
<dt><code>allowed_users</code></p>
<dd>This file contains users allowed to use incron. <code>Default</code>:<i>/etc/incron.allow</i></p>
<dt><code>denied_users</code></p>
<dd>This file contains users denied to use incron. <code>Default</code>:<i>/etc/incron.deny</i></p>
<dt><code>lockfile_dir</code></p>
<dd>This directory is used for creating a lock avoiding to run multiple instances of incrond. <code>Default</code>:<i>/var/run</i></p>
<dt><code>lockfile_name</code></p>
<dd>This name (appended by &#8216;.pid&#8217;) is used for creating a lock avoiding to run multiple instances of incrond. <code>Default</code>:<i>incrond</i></p>
<dt><code>editor</code></p>
<dd>This name or path is used to run as an editor for editing incron tables. Default <i>no editor</i> is given, system editor used, this option overide this.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-incrond/">incrond</a>(8), <a href="/docs/linux/man/1-incrontab/">incrontab</a>(1), <a href="/docs/linux/man/5-incrontab/">incrontab</a>(5)</p>
<h2>Author</h2>
<p>Lukas Jelinek &lt;lukas [at] aiken.cz&gt; (please report bugs to <a rel="nofollow" href="http://bts.aiken.cz">http://bts.aiken.cz</a> or &lt;bugs [at] aiken.cz&gt;).</p>
<h2>Copying</h2>
<p>This program is free software. It can be used, redistributed and/or modified under the terms of the GNU General Public License, version 2.</p>
