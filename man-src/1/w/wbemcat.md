---
title: "wbemcat(1)"
name: "wbemcat"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wbemcat/"
description: "wbemcat – a multi-protocol CIM-XML client"
---

<h2>NAME</h2>
<p> wbemcat &#8211; a multi-protocol CIM-XML client </p>
<h2>SYNOPSIS</h2>
<p> <code>wbemcatX</code> [<i>options</i>] [<i>FILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Utility to send raw CIM-XML request <i>FILE</i> to the a CIMOM and display the response/results. Default CIMOM is <i><a rel="nofollow" href="http://localhost:5988">http://localhost:5988</a></i>. If no input file is specified then get XML data from stdin. This used to be the wbemcatX utility before it officially replaced the original.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code>, <code>&#8211;protocol</code>=<i>PROTOCOL</i></p>
<dd> Protocol with which to connect. Default=<i>http</i></p>
<dt><code>-h</code>, <code>&#8211;host</code>=<i>HOSTNAME</i></p>
<dd> Name of host running the CIMOM. Default=<i>localhost</i></p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> Port that the CIMOM is listening on. Default=<i>5988</i></p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Display help message and exit.</dl>
<h2>PREREQUISITES</h2>
<h2>AUTHOR</h2>
<p> Sean Swehla &lt;smswehla [at] linux.vnet.ibm.com&gt;</p>
<h2>CONTRIBUTORS</h2>
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
<p> (C) Copyright IBM Corp. 2009</p>
<h2>AVAILABILITY</h2>
<p> The Small-Footprint CIM Broker (sfcb) is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xmltest/">xmltest</a>(1)</code> <code><a href="/docs/linux/man/1-wbemcat/">wbemcat</a>(1)</code> </p>
<h2>Index</h2>
