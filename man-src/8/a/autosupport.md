---
title: "autosupport(8)"
name: "autosupport"
section: "8"
letter: "a"
url: "/docs/linux/man/8-autosupport/"
description: "autosupport — interactive script to provide Digium[tm]’s support with information"
---

<p><code>autosupport</code> &#8212; interactive script to provide Digium[tm]&#8217;s support with information</p>
<h2>Synopsis</h2>
<p><code>autosupport</code> </p>
<h2>Description</h2>
<p><code>autosupport</code> is a script that is normally run by a user contacting Digium&#8217;s support to automate gathering support information. It will probe the system for some configuration and run-time information, and will also prompt the user for some optional access information (IP address, login and password). The information is written to /root/digiuminfo.txt which the user is expected to attach to a support ticket to Digium. The script must be run as root. </p>
<h2>Files</h2>
<p><code>/root/digiuminfo.txt</code></p>
<dl>
<dd>The output of the script goes there</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-asterisk/">asterisk</a>(8) </p>
<h2>Author</h2>
<p>autosupport was written by John Bigelow &lt;support [at] digium.com&gt;. This manual page was written by Tzafrir Cohen &lt;tzafrir.cohen [at] xorcom.com&gt; Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
