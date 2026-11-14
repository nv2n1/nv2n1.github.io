---
title: "gfal-mkdir(1)"
name: "gfal-mkdir"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-mkdir/"
description: "gfal-mkdir – make directories"
---

<h2>NAME</h2>
<p> gfal-mkdir &#8211; make directories</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-mkdir</code> [ <code>-h</code> ] [ <code>-V</code> ] [ <code>-v</code> ] [ <code>-D</code> <i>DEFINITION</i> ] [ <code>-C</code> <i>CLIENT-INFO</i> ] [ <code>-t</code> <i>TIMEOUT</i> ] [ <code>-p</code> ] <i>DIRECTORY</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-mkdir</code> Create the DIRECTORY(ies), if they do not already exist. By default, it creates them with mode 0755. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> show help about the command.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> output version information and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> verbose mode. Repeat up to 3 times for the most verbose mode.</p>
<dt><code>-D, &#8211;definition</code></p>
<dd> define properties for gfal2.</p>
<dt><code>-C, &#8211;client-info</code></p>
<dd> provide custom client-side information</p>
<dt><code>-t, &#8211;timeout</code></p>
<dd> global timeout for the execution of the command. Command is interrupted if time expires before it finishes.</p>
<dt><code>-m, &#8211;mode</code></p>
<dd> set file mode (as in chmod). If not specified, 0755 is used. Depending on the storage implementation, it might not be used.</p>
<dt><code>-p, &#8211;parents</code></p>
<dd> no error if existing, make parent directories as needed. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gfal-mkdir</code></p>
<dd> -p -m 0700 file:///tmp/path1/path2</dl>
<dl>
<dt><code>gfal-mkdir</code></p>
<dd> <a href="srm://endpoint.cern.ch/path/directory1">srm://endpoint.cern.ch/path/directory1</a> <a href="srm://endpoint.cern.ch/path/directory2">srm://endpoint.cern.ch/path/directory2</a> </p>
</dl>
<h2>FILES</h2>
<p> <i>/etc/gfal2.d/*</i></p>
<dl>
<dt>
<dd> All configuration files in this directory affect the behavior of the underlying gfal2. </p>
</dl>
<h2>AUTHORS</h2>
<p> Duarte Meneses &lt;duarte.meneses [at] cern.ch&gt;<br />
 Adrien Devresse &lt;adrien.devresse [at] cern.ch&gt;<br />
 Alejandro Alvarez Ayllon &lt;alejandro.alvarez.ayllon [at] cern.ch&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gfal-cat/">gfal-cat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-copy/">gfal-copy</a></code>(1), <code><a href="/docs/linux/man/1-gfal-ls/">gfal-ls</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rename/">gfal-rename</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rm/">gfal-rm</a></code>(1), <code><a href="/docs/linux/man/1-gfal-save/">gfal-save</a></code>(1), <code><a href="/docs/linux/man/1-gfal-stat/">gfal-stat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-sum/">gfal-sum</a></code>(1), <code><a href="/docs/linux/man/1-gfal-xattr/">gfal-xattr</a></code>(1) </p>
<h2>Index</h2>
