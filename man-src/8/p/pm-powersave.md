---
title: "pm-powersave(8)"
name: "pm-powersave"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pm-powersave/"
description: "pm-powersave – Put your computer into low power mode"
---

<p>pm-powersave &#8211; Put your computer into low power mode</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pm-powersave</code> [{<code>true</code>&nbsp;<wbr>|&nbsp;<wbr><code>false</code>}] [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<dd>This manual page documents briefly the <code>pm-powersave</code> command. </p>
<p> <code>pm-powersave</code> can be used to set your system into low power mode.</p>
<h2>Options</h2>
<p><code>true</code></p>
<dl>
<dd>Put the computer into low power mode to reduce energy consumption and extend your laptop&#8217;s battery life.</dl>
<p> <code>false</code></p>
<dl>
<dd>Turn off low power mode.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show the help.</dl>
<h2>Files</h2>
<p>/etc/pm/power.d/, /usr/lib/pm-utils/power.d/</p>
<dl>
<dd>When you run <code>pm-powersave</code> it combines the scripts in these two directories and executes them in sorted order. If both directories contain a script with the same name, the one in /etc/pm/power.d/ has a higher precedence and only this one will be executed. </p>
<p> Therefore to disable a script from /usr/lib/pm-utils/power.d/ simply create an empty file in /etc/pm/power.d/ with the same name and without the executable bit set.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pm-suspend/">pm-suspend</a></code>(8), <code><a href="/docs/linux/man/8-pm-hibernate/">pm-hibernate</a></code>(8)</p>
<h2>Author</h2>
<p><code>Michael Biebl</code> &lt;biebl [at] debian.org&gt;</p>
<dl>
<dd>Manpage author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Michael Biebl </p>
<p> This manual page was originally written for the Debian(TM) system, and has been adopted by the pm-utils project. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or (at your option) any later version published by the Free Software Foundation.</p>
