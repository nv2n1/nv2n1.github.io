---

title: "ppa-purge(1)"
name: "ppa-purge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppa-purge/"
description: "ppa-purge – disables a PPA and reverts to official packages"
---

<p> <code>ppa-purge [-h | [-d &lt;distribution&gt;] [-s &lt;host&gt;] [-p &lt;ppaname&gt;] &lt;ppa:&lt;ppaowner[/ppaname&gt;]&gt;]</code> </p>
<p> This script provides a bash shell script capable of automatically downgrading all packages in a given PPA back to the ubuntu versions. </p>
<p> You have to run it using root privileges because of the package manager. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Display usage help.</dd>
<dt><code>-p</code> <i>PPA name</i></dt>
<dd> Name of the PPA to be reset, the default value is ppa.</dd>
<dt>
</dt><dd> <code>-s</code> <i>PPA host</i> Address of the repository server, the default value is ppa.launchpad.net. </dd>
</dl>
<h2>COPYRIGHT</h2>
<p> This manual page is Copyright 2010 Lorenzo De Liso &lt;blackz [at] ubuntu.com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 or any later version published by the Free Software Foundation. </p>
