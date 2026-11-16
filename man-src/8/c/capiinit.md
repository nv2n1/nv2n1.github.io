---
title: "capiinit(8)"
name: "capiinit"
section: "8"
letter: "c"
url: "/docs/linux/man/8-capiinit/"
description: "capiinit – start or stop CAPI-capable ISDN cards"
---

<p>capiinit &#8211; start or stop CAPI-capable ISDN cards</p>
<h2>Synopsis</h2>
<p>capiinit [OPTIONS] start | stop | show | status | prepare | reload | activate | deactivate </p>
<p> capiinit [OPTIONS] activate|deactivate cardname </p>
<p> capiinit [OPTIONS] activate|deactivate driver [cardname]</p>
<h2>Description</h2>
<p><code>capiinit</code> is called with one of the following actions:</p>
<dl>
<dt><code>start</code></dt>
<dd>Load all modules and initialize all cards (loading the firmware), which are configured in <i>/etc/isdn/capi.conf</i>.</dd>
<dt><code>stop</code></dt>
<dd>Reset all cards and unload modules.</dd>
<dt><code>show</code></dt>
<dd>Show the current configuration.</dd>
<dt><code>status</code></dt>
<dd>Show the current status.</dd>
<dt><code>prepare</code></dt>
<dd>Load all modules.</dd>
<dt><code>activate</code></dt>
<dd>Initialize all cards.</dd>
<dt><code>activate</code> <i>cardname</i></dt>
<dd>Initialize one card (i.e.: c4-ec00).</dd>
<dt><code>activate</code> <i>driver</i> [<i>cardnumber</i>]</dt>
<dd>Initialize one card.</dd>
<dt><code>deactivate</code></dt>
<dd>Reset all cards.</dd>
<dt><code>deactivate</code> <i>cardname</i></dt>
<dd>Reset one card (i.e.: c4-ec00).</dd>
<dt><code>deactivate</code> <i>driver</i> [<i>cardnumber</i>]</dt>
<dd>Reset one card.</dd>
<dt><code>reload</code></dt>
<dd>Reset all cards and initialize them again.</dd></dl>
<p> Firmware files are searched in this order in the following directories: <i>/usr/share/isdn/`uname -r`</i>, <i>/usr/share/isdn</i>, <i>/usr/lib/isdn</i>, <i>/lib/isdn</i>. There is a sample config in /etc/isdn/capi.conf. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> <i>filename</i>, <code>&#8211;config</code> <i>filename</i></dt>
<dd>Use <i>filename</i> as config file (default is /etc/isdn/capi.conf).</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd>Save patch values for debugging purposes.</dd>
<dt><code>-s</code>, <code>&#8211;silent</code></dt>
<dd>Don&#8217;t show status information.</dd></dl>
<h2>Author</h2>
<p>Manpage written from C source by Paul Slootman &lt;paul [at] debian.org&gt;, updated by Matthias Klose &lt;m@klose.in-berlin.de&gt;.</p>
