---
title: "gfal-rm(1)"
name: "gfal-rm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-rm/"
description: "gfal-rm – Remove files or directories"
---

<h2>NAME</h2>
<p> gfal-rm &#8211; Remove files or directories</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-rm</code> [ <code>-h</code> ] [ <code>-V</code> ] [ <code>-v</code> ] [ <code>-D</code> <i>DEFINITION</i> ] [ <code>-C</code> <i>CLIENT-INFO</i> ] [ <code>-t</code> <i>TIMEOUT</i> ] [ <code>-r</code> ] <i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-rm</code> Removes each specified file or directory. By default, it does not remove directories. To delete a directory, &#8211;recursive needs to be given, in which case all given directories are removed too along with all their contents. </p>
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
<dd> global timeout for the execution of the command. Command is interrupted if time expires before it finishes.</dd>
<dt><code>-r, &#8211;recursive</code></dt>
<dd> also remove directories and their contents recursively.</dd>
<dt><code>&#8211;bulk</code></dt>
<dd> perform bulk deletion. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gfal-rm</code></dt>
<dd> file:///tmp/test</dd></dl>
<dl>
<dt><code>gfal-rm</code></dt>
<dd> -r <a href="srm://endpoint.cern.ch/path/directory">srm://endpoint.cern.ch/path/directory</a> </dd>
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
<p> <code><a href="/docs/linux/man/1-gfal-cat/">gfal-cat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-copy/">gfal-copy</a></code>(1), <code><a href="/docs/linux/man/1-gfal-ls/">gfal-ls</a></code>(1), <code><a href="/docs/linux/man/1-gfal-mkdir/">gfal-mkdir</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rename/">gfal-rename</a></code>(1), <code><a href="/docs/linux/man/1-gfal-save/">gfal-save</a></code>(1), <code>gfal-stat</code>(1), <code><a href="/docs/linux/man/1-gfal-sum/">gfal-sum</a></code>(1), <code><a href="/docs/linux/man/1-gfal-xattr/">gfal-xattr</a></code>(1) </p>
