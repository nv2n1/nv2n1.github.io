---
title: "ninjahelper(1)"
name: "ninjahelper"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ninjahelper/"
description: "NINJAHELPER – A menu driven curses-based interface to walk you through backupninja configuration."
---

<h2 class="name">NAME</h2>
<p> NINJAHELPER &#8211; A menu driven curses-based interface to walk you through backupninja configuration. </p>
<h2>SYNOPSIS</h2>
<p> <code>ninjahelper</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Ninjahelper</code> is an helper script to walk you through configuration of the backup tasks for backupninja. It is a curses based &quot;wizard&quot; with an intuitive menu-driven interface. </p>
<h2>ADDING NEW HELPERS</h2>
<p> To add an additional &#8216;wizard&#8217; to ninjahelper, follow these steps:</p>
<dl>
<dt>(1)</p>
<dd> create a file in the handlers directory (eg. /usr/share/backupninja) using the .helper extension. For example, if you wish to create a helper for the handler &quot;blue&quot;, create the file /usr/share/backupninja/blue.helper.</p>
<dt>(2)</p>
<dd> next, add your helper to the global HELPERS variable and define the main function for your helper (the function name is always &lt;helper&gt;_wizard). To use the blue.helper as an example: HELPERS=&quot;$HELPERS blue:description_of_this_helper&quot;<br />
&nbsp;<wbr>blue_wizard()&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8230; do work here &#8230;<br />
&nbsp;<wbr>}</p>
<dt>(3)</p>
<dd> look at the existing helpers to see how they are written. Try to re-use functions, such as the dialog functions that are defined in easydialog.sh, or the vserver functions defined in lib/vserver.</p>
<dt>(4)</p>
<dd> test, re-test, and test again. Try to break the helper by going backwards, try to think like someone who has no idea how to configure your handler would think, try to make your helper as simple as possible. Walk like a cat, become your shadow, don&#8217;t let your senses betray you. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-backupninja/">backupninja</a></code>(1), <code><a href="/docs/linux/man/5-backupninja-conf/">backupninja.conf</a></code>(5), <code><a href="/docs/linux/man/5-backup-d/">backup.d</a></code>(5), </p>
<h2>AUTHOR</h2>
<p> BACKUPNINJA was written by the riseup.net collective. </p>
<h2>Index</h2>
