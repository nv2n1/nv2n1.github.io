---
title: "ncidd(5)"
name: "ncidd"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ncidd/"
description: "ncidd.conf – ncidd configuration file"
---

<p><code>ncidd.conf</code> &#8211; ncidd configuration file</p>
<h2>Description</h2>
<p>The <i>ncidd.conf</i> file contains the configuration information for <i>ncidd</i>, the Network Caller ID Server. </p>
<p> The <i>ncidd.conf</i> file is used to set options. Options are set on a command line. A line is broken up into words. A word is either a string of non-blank characters, everything between double quotes, or an equal sign. </p>
<p> The <i>ncidd.conf</i> file understands 5 types of lines:</p>
<dl>
<dt><code>blank line</code></p>
<dd>skip it</p>
<dt><code>comment line, beginning with &#8216;#&#8217;</code></p>
<dd>skip it</p>
<dt><code>command lines, beginning with &#8216;send&#8217;</code></p>
<dd>send DATATYPE</p>
<dl>
<dd>where DATATYPE = cidlog, cidinfo</dl>
<dt><code>command lines, beginning with &#8216;set&#8217;</code></p>
<dd>set ITEM = VALUE [ITEM = VALUE] [&#8230;]</p>
<dl>
<dd>where ITEM = cidlog, cidlogmax, datalog, initcid, initstr, lockfile, noserial, port, ttyclocal, ttyport, ttyspeed, nomodem, verbose</dl>
</dl>
<h2>Examples</h2>
<p>Send the CID log to each client at connect:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>send cidlog
</dl>
<p> Send the ring count, at each ring, to each client</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>send cidinfo
</dl>
<pre><code>Set the modem for Caller ID:

set initcid = &quot;AT#CID=1&quot;</code></pre>
<p> Set the modem port:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>set ttyport=/dev/ttyS1
</dl>
<p> Set the Telephone Line Indicator for the modem:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>set lineid = POTS
</dl>
<p> Use a modem and possibly a Gateway to obtain the Caller ID:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>set noseriel = 0
</dl>
<p> Do not use a modem, just use a Gateway to obtain the Caller ID:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>set noseriel = 1
</dl>
<h2>See Also</h2>
<p>ncid.1, ncidtools.1, lcdncid.1, out2osd.1, ncidd.8 ncidd.alias.5 </p>
