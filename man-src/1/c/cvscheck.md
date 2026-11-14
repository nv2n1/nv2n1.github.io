---
title: "cvscheck(1)"
name: "cvscheck"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvscheck/"
description: "cvscheck – Offline status report for files in a checked-out CVS module."
---

<h2 class="name">NAME</h2>
<p> cvscheck &#8211; Offline status report for files in a checked-out CVS module. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cvscheck</code> [<i>dir</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>cvscheck</code></p>
<dd>prints information about the status of your local CVS checkout without communicating with the server. This means it is extremely fast and does not require a network connection. </p>
<p> The given directory and all of its subdirectories will be processed recursively. If no directory is given, the current directory and its recursed subdirectories will be used. </p>
<p> Each file with an interesting status will be printed with a status character in front of its name. The status characters are as follows. </p>
<p> ? foobar.c</p>
<dl>
<dt>
<dd> The file is not known to CVS</dl>
<p> M foobar.c</p>
<dl>
<dt>
<dd> The file is definitely locally modified</dl>
<p> m foobar.c</p>
<dl>
<dt>
<dd> The file <i>might</i> have local changes. You should <code>diff</code> with the server to make sure.</dl>
<p> C foobar.c</p>
<dl>
<dt>
<dd> The file has a CVS conflict and therefore cannot be committed.</dl>
<p> U foobar.c</p>
<dl>
<dt>
<dd> This file is in CVS but is missing in your local checkout.</dl>
<p> T foobar.c</p>
<dl>
<dt>
<dd> This file has an unusual sticky CVS tag.</dl>
<p> A foobar.c</p>
<dl>
<dt>
<dd> You have done a <code>cvs</code><code>add</code> for this file, but have not yet committed it.</dl>
<p> R foobar.c</p>
<dl>
<dt>
<dd> You have done a <code>cvs</code><code>rm</code> for this file, but have not yet committed it.</dl>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cvs/">cvs</a>(1)</p>
<h2>AUTHORS</h2>
<p> cvscheck was written by Dirk Müller&lt;mueller [at] kde.org&gt; and Sirtaj.Singh.Kang; &lt;taj [at] kde.org&gt; </p>
<p> This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
