---
title: "yac2ncid(5)"
name: "yac2ncid"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yac2ncid/"
description: "yac2ncid.conf – yac2ncid configuration file"
---

<p><code>yac2ncid.conf</code> &#8211; yac2ncid configuration file</p>
<h2>Description</h2>
<p>The <i>yac2ncid.conf</i> file contains the configuration information for <i>yac2ncid</i>. </p>
<p> The <i>ncid.conf</i> file understands 3 types of lines:</p>
<dl>
<dt><code>blank line</code></p>
<dd>skip it</p>
<dt><code>comment line, beginning with &#8216;#&#8217;</code></p>
<dd>skip it</p>
<dt><code>Variable=Argument</code></p>
<dd></dl>
<p> See yac2ncid.conf for a complete list of variables to set and what the default values are.</p>
<h2>Examples</h2>
<p>Set the NCID server IP address:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NCIDSERVER=192.168.0.1
</dl>
<p> Set a telephone line indicator:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>LINE=1212
</dl>
<h2>See Also</h2>
<p>yac2ncid.1, ncidd.8 ncidd.alias.5, ncidd.conf.5 </p>
