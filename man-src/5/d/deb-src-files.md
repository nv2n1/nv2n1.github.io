---
title: "deb-src-files(5)"
name: "deb-src-files"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-src-files/"
description: "deb-src-files – Debian distribute files format"
---

<p>deb-src-files &#8211; Debian distribute files format</p>
<h2>Synopsis</h2>
<p><code>debian/files</code></p>
<h2>Description</h2>
<p>This file contains the list of artifacts that are to be distributed via the <code>.changes</code> control file. </p>
<p> The <i>debian/files</i> file has a simple whitespace-delimited format. </p>
<dl>
<dd><i>filename</i> <i>section</i> <i>priority</i> [ <i>keyword=value&#8230;</i> ]</dl>
<p> <i>filename</i> is the name of the artifact to distribute. </p>
<p> <i>section</i> and <i>priority</i> correspond to the respective control fields available in the .deb. The allowed values are specific to each distribution archive. </p>
<p> <i>keyword=value&#8230;</i> corresponds to an optional whitespace-delimited list of attributes for this entry. The only currently supported keyword is <code>automatic</code> with value <code>yes</code>, to mark automatically generated files.</p>
<h2>Notes</h2>
<p>This file is not intended to be modified directly, please use one of <code>dpkg-gencontrol</code> or <code>dpkg-distaddfile</code> to add entries to it.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg-genchanges/">dpkg-genchanges</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-distaddfile/">dpkg-distaddfile</a></code>(1). </p>
