---
title: "ncid(5)"
name: "ncid"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ncid/"
description: "ncid.conf – ncid configuration file"
---

<p><code>ncid.conf</code> &#8211; ncid configuration file</p>
<h2>Description</h2>
<p>The <i>ncid.conf</i> file contains the configuration information for <i>ncid</i>, the Network Caller ID Client. Use <i>ncid.conf</i> to configure ncid everytime it is started, but use <i>ncidmodules.conf</i> to configure ncid for a particular output module. For example, use <i>ncid.conf</i> to configure ncid for the server address, but use <i>ncidmodules.conf</i> to configure ncid to for ncid-page. </p>
<p> The <i>ncid.conf</i> file is a tcl/tk configuration file used to set options. </p>
<p> The <i>ncid.conf</i> file understands 3 types of lines:</p>
<dl>
<dt><code>blank line</code></p>
<dd>skip it</p>
<dt><code>comment line, beginning with &#8216;#&#8217;</code></p>
<dd>skip it</p>
<dt><code>command lines, beginning with &#8216;set&#8217;</code></p>
<dd></dl>
<p> See ncid.conf for a complete list of variables to set and what the default values are.</p>
<h2>Examples</h2>
<p>Set ncid to use the page output module:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>set EXTPROG <i>ncid-page</i>
</dl>
<p> Set ncid to format its output for the US and include the 1. The number output display will be 1-XXX-XXX-XXXX instead of XXX-XXX-XXXX:</p>
<dl>
<dd>&nbsp;<wbr>set NoOne&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0</dl>
<p> Set ncid to format its number output display for Sweden: The number output display will be 0X-XXXXXXXX, 0XX-XXXXXXX, 0XXX-XXXXX, etc:</p>
<dl>
<dd>&nbsp;<wbr>set Country&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;SE&quot;</dl>
<h2>See Also</h2>
<p>ncid.1, ncidtools.1, lcdncid.1, out2osd.1, ncidd.8 ncidd.alias.5, ncidd.conf.5 </p>
