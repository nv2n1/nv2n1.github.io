---
title: "sfcbstage(1)"
name: "sfcbstage"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfcbstage/"
description: "sfcbstage – Script to copy provider MOF and registration files to the Small-Footprint CIM Broker (sfcb) staging area"
---

<h2>NAME</h2>
<p> sfcbstage &#8211; Script to copy provider MOF and registration files to the Small-Footprint CIM Broker (sfcb) staging area</p>
<h2>SYNOPSIS</h2>
<p> <code>sfcbstage</code> [<i>options</i>] [<i>mof&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> sfcbstage copies provider mof and registration files to the sfcb staging area. Used to add classes to sfcb offline. The class repository must be rebuilt with sfcbrepos and the sfcb CIMOM restarted before changes take effect.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code> <i>namespace</i></p>
<dd> Namespace for which the class MOFs are to be registered. Default is <i>root/cimv2</i></p>
<dt><code>-s</code> <i>stagingdir</i></p>
<dd> Path to sfcb staging area containing class MOFs and registration files Default is <i>/var/lib/sfcb/stage</i></p>
<dt><code>-r</code> <i>registrationfile</i></p>
<dd> Path to the provider registration file.</p>
<dt><code>-h</p>
<dd> Display usage information and exit.</p>
<dt></code><i>mof</i></p>
<dd> Path(s) to one or more class MOF files containing the CIM class definitions for the class(es) implemented by the provider.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DESTDIR</code></p>
<dd> If set, the value of this variable is prepended to the registration directory names. This can be useful to store the repository in a different location, i.e. when cross-compiling providers.</dl>
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
<p> <code><a href="/docs/linux/man/1-sfcbd/">sfcbd</a></code>(1), <code><a href="/docs/linux/man/1-sfcbrepos/">sfcbrepos</a></code>(1), <code><a href="/docs/linux/man/1-sfcbunstage/">sfcbunstage</a></code>(1) </p>
<h2>Index</h2>
