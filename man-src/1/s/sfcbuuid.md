---
title: "sfcbuuid(1)"
name: "sfcbuuid"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfcbuuid/"
description: "sfcbuuid – Script to create a universally unique identifier for the installed Small-Footprint CIM Broker (sfcb)"
---

<h2>NAME</h2>
<p> sfcbuuid &#8211; Script to create a universally unique identifier for the installed Small-Footprint CIM Broker (sfcb)</p>
<h2>SYNOPSIS</h2>
<p> <code>sfcbuuid</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> sfcbuuid can be used to create a universally unique identifier (uuid) for sfcb. The uuid will be stored in a file (usually /var/lib/sfcb/uuid). Whenever sfcb needs to return it&#8217;s uuid to a requestor it will read the uuid file from this file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u</code> <i>uuidfile</p>
<dd> Full path name of the sfcb uuid file. Default is /var/lib/sfcb/uuid</i></p>
<dt><code>-f</p>
<dd> Remove an existing uuid file without asking for permission.</p>
<dt>-h</p>
<dd> Display usage information and exit.</dl>
<p> </code></p>
<h2>AUTHOR</h2>
<p> Viktor Mihajlovski &lt;MIHAJLOV [at] de.ibm.com&gt;</p>
<h2>BUGS</h2>
<p> The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-issues">http://lists.sourceforge.net/lists/listinfo/sblim-issues</a></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dl>
<h2>COPYRIGHT</h2>
<p> (C) Copyright IBM Corp. 2004, 2005</p>
<h2>AVAILABILITY</h2>
<p> The Small-Footprint CIM Broker (sfcb) is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sfcbd/">sfcbd</a></code>(1), </p>
<h2>Index</h2>
