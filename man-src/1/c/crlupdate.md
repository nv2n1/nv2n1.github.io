---
title: "crlupdate(1)"
name: "crlupdate"
section: "1"
letter: "c"
url: "/docs/linux/man/1-crlupdate/"
description: "crlupdate – Mono Certficate Revocation List Downloader and Updater"
---

<h2>NAME</h2>
<p> crlupdate &#8211; Mono Certficate Revocation List Downloader and Updater</p>
<h2>SYNOPSIS</h2>
<p> <code>crlupdate [-m] [-v] [-f]</code></p>
<h2>DESCRIPTION</h2>
<p> This tool allows the download of new, or update of existing, Certficate Revocation List (CRL) associated with the certificates present in the user (default) or machine stores. The CRL present in the stores are used to determine the validity of unexpired, trusted X.509 certificates. To ensure CRL are always fresh consider automating the updates using the <i>at</i> (or similar) command(s).</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-m</i></p>
<dd> Update CRL associated with certificates in the machine store. By default the tool works on the user store.</p>
<dt><i>-v</i></p>
<dd> Verbose mode. Display extra information while downloading and updating the CRL.</p>
<dt><i>-f</i></p>
<dd> Force the download of all CRL even if they are not normally due to be updated (i.e. nextUpdate is still in the future). </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>mono crlupdate.exe</code></p>
<dd> Download (if missing) or update (if existing and past due date) all CRL associated with certificates present in user store.</p>
<dt><code>mono crlupdate.exe -f -m</code></p>
<dd> Force the download of every CRL associated with certificates present in the machine store. Note that the user running this needs read/write access to the machine store or not update will occur. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011 Novell.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-certmgr/">certmgr</a>(1),</code><a href="/docs/linux/man/1-at/">at</a>(1) </p>
<h2>Index</h2>
