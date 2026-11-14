---
title: "gfal-ls(1)"
name: "gfal-ls"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-ls/"
description: "gfal-ls – list directory contents or file information"
---

<h2>NAME</h2>
<p> gfal-ls &#8211; list directory contents or file information</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-ls [-h] [-V] [-v] [-D DEFINITION] [-C CLIENT-INFO] [-t TIMEOUT] [-a] [-l] [-d] [-H] file</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-ls</code> List information about the file. Depending on the implementation, some information from the long listing, such as group and user ids, might not be available and will be displayed as 0. When listing several files or directories, if one returns an error, the execution is canceled. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> show help about the command</p>
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
<dt><code>-a, &#8211;all</code></p>
<dd> don&#8217;t hide files with name starting in &#8216;.&#8217;.</p>
<dt><code>-l, &#8211;long</code></p>
<dd> long listing format. Following columns are displayed for each entry: mode, number of links, group id, user id, last modification time, size and name.</p>
<dt><code>-d, &#8211;directory</code></p>
<dd> list directory entries instead of its contents.</p>
<dt><code>-H, &#8211;human-readable</code></p>
<dd> with -l, print sizes in human readable format (e.g., 1K 234M 2G).</p>
<dt><code>&#8211;time-style</code></p>
<dd> time style. supports locale, iso, long-iso and full-iso (partially)</p>
<dt><code>&#8211;full-time</code></p>
<dd> equivalent to &#8211;time-style=full-iso</p>
<dt><code>&#8211;color</code></p>
<dd> enable or disable color output. supports always, never, auto. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Long listing of all files:</p>
<dd> <code>gfal-ls</code> -laH <a href="srm://endpoint.cern.ch/path/file">srm://endpoint.cern.ch/path/file</a></dl>
<dl>
<dt>List a directory instead of its contents:</p>
<dd> <code>gfal-ls</code> -d file:///tmp </p>
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
<p> <code><a href="/docs/linux/man/1-gfal-cat/">gfal-cat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-copy/">gfal-copy</a></code>(1), <code><a href="/docs/linux/man/1-gfal-mkdir/">gfal-mkdir</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rename/">gfal-rename</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rm/">gfal-rm</a></code>(1), <code><a href="/docs/linux/man/1-gfal-save/">gfal-save</a></code>(1), <code><a href="/docs/linux/man/1-gfal-stat/">gfal-stat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-sum/">gfal-sum</a></code>(1), <code><a href="/docs/linux/man/1-gfal-xattr/">gfal-xattr</a></code>(1) </p>
<h2>Index</h2>
