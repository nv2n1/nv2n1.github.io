---
title: "gfal-sum(1)"
name: "gfal-sum"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-sum/"
description: "gfal-sum – Calculate checksum of a file"
---

<h2>NAME</h2>
<p> gfal-sum &#8211; Calculate checksum of a file</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-sum</code> [ <i>OPTIONS</i> ] <i>FILE CHECKSUM_TYPE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-sum</code> Calculates the checksum of the specified file, using a specified checksum algoritm. The supported algorithm depend on the protocol and endpoint. Some examples are <i>ADLER32</i> , <i>CRC32</i><br />
&nbsp;<wbr>and <i>MD5</i> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> show help about the command.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> output version information and exit.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> verbose mode. Repeat up to 3 times for the most verbose mode.</dd>
<dt><code>-D, &#8211;definition</code></dt>
<dd> define properties for gfal2.</dd>
<dt><code>-C, &#8211;client-info</code></dt>
<dd> provide custom client-side information</dd>
<dt><code>-t, &#8211;timeout</code></dt>
<dd> global timeout for the execution of the command. Command is interrupted if time expires before it finishes. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gfal-sum</code></dt>
<dd> <a href="srm://endpoint.cern.ch/path/file">srm://endpoint.cern.ch/path/file</a> ADLER32 </dd>
</dl>
<h2>FILES</h2>
<p> <i>/etc/gfal2.d/*</i></p>
<dl>
<dt>
</dt><dd> All configuration files in this directory affect the behavior of the underlying gfal2. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Duarte Meneses &lt;duarte.meneses [at] cern.ch&gt;<br />
 Adrien Devresse &lt;adrien.devresse [at] cern.ch&gt;<br />
 Alejandro Alvarez Ayllon &lt;alejandro.alvarez.ayllon [at] cern.ch&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gfal-cat/">gfal-cat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-copy/">gfal-copy</a></code>(1), <code><a href="/docs/linux/man/1-gfal-ls/">gfal-ls</a></code>(1), <code><a href="/docs/linux/man/1-gfal-mkdir/">gfal-mkdir</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rename/">gfal-rename</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rm/">gfal-rm</a></code>(1), <code><a href="/docs/linux/man/1-gfal-save/">gfal-save</a></code>(1), <code>gfal-stat</code>(1), <code><a href="/docs/linux/man/1-gfal-xattr/">gfal-xattr</a></code>(1) </p>
<h2>Index</h2>
