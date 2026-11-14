---
title: "ncidrotate(5)"
name: "ncidrotate"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ncidrotate/"
description: "ncidrotate.conf – ncidrotate configuration file"
---

<p><code>ncidrotate.conf</code> &#8211; ncidrotate configuration file</p>
<h2>Description</h2>
<p>The <i>ncidrotate.conf</i> file contains the configuration information for <i>ncidrotate</i>, the Network Caller ID Client. </p>
<p> The <i>ncidrotate.conf</i> file understands 3 types of lines:</p>
<dl>
<dt><code>blank line</code></p>
<dd>skip it</p>
<dt><code>comment line, beginning with &#8216;#&#8217;</code></p>
<dd>skip it</p>
<dt><code>Variable=Argument</code></p>
<dd></dl>
<p> There is only one variable expected to change: Lines2keep. The other variables should not be changed. See ncidrotate.conf for a complete list of variables to set and what the default values are.</p>
<h2>Examples</h2>
<p>Keep 10 lines in cidcall.log after rotation</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Lines2keep=10
</dl>
<h2>See Also</h2>
<p>ncidrotate.1, ncidd.8, sip2ncid.8 </p>
