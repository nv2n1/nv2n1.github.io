---
title: "mdmflexiserver(1)"
name: "mdmflexiserver"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdmflexiserver/"
description: "mdmflexiserver – start a MDM session using the MDM flexible server mechanism"
---

<h2 class="name">NAME</h2>
<p> mdmflexiserver &#8211; start a MDM session using the MDM flexible server mechanism </p>
<h2>SYNOPSIS</h2>
<p> <code>mdmflexiserver</code> <font SIZE="-1">GNOME</font> options mdmflexiserver options</p>
<h2>DESCRIPTION</h2>
<p> The <i>flexi server</i> mechanism allows to run <font SIZE="-1">MDM</font> sessions on demand.</p>
<h2>OPTIONS</h2>
<p> In addition to the common Gtk and <font SIZE="-1">GNOME</font> options, <code>mdmflexiserver</code> accepts the following options:</p>
<dl>
<dt><code>-c</code> <i>command</i>, <code>&#8211;command</code>=<i>command</i></p>
<dd> Send the specified protocol command to mdm</p>
<dt><code>-l</code>, <code>&#8211;no-lock</code></p>
<dd> Do not lock current screen</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Debugging output</p>
<dt><code>-a</code>, <code>&#8211;authenticate</code></p>
<dd> Authenticate before running <code>&#8211;command</code></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-mdm/">mdm</a></i>(8)</p>
<h2>AUTHORS</h2>
<p> <code>mdmflexiserver</code> is part of the <font SIZE="-1"><code>MDM</code></font> software package. This manpage was written by Yann Dirson &lt;dirson [at] debian.org&gt; for the Debian system, but may be used by others. </p>
<h2>Index</h2>
