---
title: "getschema(1)"
name: "getschema"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getschema/"
description: "getSchema – Script to download DMTF CIM Schema for Small-Footprint CIM Broker (sfcb)"
---

<p>getSchema &#8211; Script to download DMTF CIM Schema for Small-Footprint CIM Broker (sfcb)</p>
<h2>Synopsis</h2>
<p><code>getSchema</code> [<code>-f</code>] <i>schemadir</i></p>
<h2>Description</h2>
<p>getSchema is a small script to automatically downlaod and install the latest CIM Schema from the DMTF website. The CIM Schema is required by the Small-Footprint CIM Broker (sfcb) to be able to install and register new classes. getSchema uses curl to fetch the CIM Schema tarball.</p>
<h2>Options</h2>
<p>Supported command line options are:</p>
<dl>
<dt><i>schemadir</i></p>
<dd>Path to download the CIM Schema tarball and extract all the CIM classes. Default is <i>/usr/share/sfcb</i></p>
<dt><code>-f</code></p>
<dd>Force option. Without this option you will be prompted if an existing schema is already found in the target <i>schemadir</i>. Setting this option will reinstall the new CIM Schema without prompting.</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/sfcb/getSchema.sh</i></p>
<dd>The getSchema script.</p>
<dt><i>/usr/share/sfcb/CIM/CIM_Schema.mof</i></p>
<dd>CIM Schema</dl>
<h2>Prequisites</h2>
<p>Requires curl</p>
<h2>Author</h2>
<p>Adrian Schuur &lt;schuur [at] de.ibm.com&gt;</p>
<h2>Bugs</h2>
<p>The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dd><a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-issues">http://lists.sourceforge.net/lists/listinfo/sblim-issues</a></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dd><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dl>
<h2>Copyright</h2>
<p>(C) Copyright IBM Corp. 2004, 2005</p>
<h2>Availability</h2>
<p>The Small-Footprint CIM Broker (sfcb) is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dd><a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sfcbd/">sfcbd</a></code>(1)</p>
