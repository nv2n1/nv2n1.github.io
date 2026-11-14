---
title: "deb-extra-override(5)"
name: "deb-extra-override"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-extra-override/"
description: "deb-extra-override – Debian archive extra override file"
---

<p>deb-extra-override &#8211; Debian archive extra override file</p>
<h2>Synopsis</h2>
<p><code>override</code></p>
<h2>Description</h2>
<p>While most information about a binary/source package can be found in the control/.dsc file, all of it can be overridden when it&#8217;s exported to Packages/Sources files. The extra override file contains those overrides. </p>
<p> The extra override file has a simple whitespace-delimited format. Comments are allowed (denoted with a <code>#</code>). </p>
<dl>
<dd><i>package</i> <i>field-name</i> <i>value</i></dl>
<p> <i>package</i> is the name of the binary/source package. </p>
<p> <i>field-name</i> is the name of the field that is overridden. </p>
<p> <i>value</i> is the value to put in the field. It can contain spaces as the line is split in no more than 3 columns when it&#8217;s parsed. </p>
<p> The extra override files used to make the official Packages lists may be found in the <i>indices</i> directory on any Debian mirror.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg-scanpackages/">dpkg-scanpackages</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-scansources/">dpkg-scansources</a></code>(1), <code><a href="/docs/linux/man/1-apt-ftparchive/">apt-ftparchive</a></code>(1). </p>
