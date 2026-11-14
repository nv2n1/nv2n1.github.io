---
title: "sip2ncid(5)"
name: "sip2ncid"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sip2ncid/"
description: "sip2ncid.conf – sip2ncid configuration file"
---

<p><code>sip2ncid.conf</code> &#8211; sip2ncid configuration file</p>
<h2>Description</h2>
<p>The <i>sip2ncid.conf</i> file contains the configuration information for <i>sip2ncid</i>, the Network Caller ID Server. </p>
<p> The <i>sip2ncid.conf</i> file is used to set options. Options are set on a command line. A line is broken up into words. A word is either a string of non-blank characters, everything between double quotes, or an equal sign. </p>
<p> The <i>sip2ncid.conf</i> file understands 5 types of lines:</p>
<dl>
<dt><code>blank line</code></p>
<dd>skip it</p>
<dt><code>comment line, beginning with &#8216;#&#8217;</code></p>
<dd>skip it</p>
<dt><code>command lines, beginning with &#8216;set&#8217;</code></p>
<dd>set ITEM = VALUE [ITEM = VALUE] [&#8230;]</p>
<dl>
<dd>where ITEM = pidfile, verbose, ncidhost, ncidport, siphost, sipport</dl>
</dl>
<h2>Examples</h2>
<p>Set the verbose level to 3</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>set verbose = 3
</dl>
<p> Set the SIP port to 5061</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>set sipport = 5061
</dl>
<h2>See Also</h2>
<p>sip2ncid.8, ncidd.8, ncidd.conf.5 </p>
