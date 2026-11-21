---

title: "gfal-ls(1)"
name: "gfal-ls"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-ls/"
description: "gfal-ls – list directory contents or file information"
---

<p> gfal-ls &#8211; list directory contents or file information</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-ls [-h] [-V] [-v] [-D DEFINITION] [-C CLIENT-INFO] [-t TIMEOUT] [-a] [-l] [-d] [-H] file</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-ls</code> List information about the file. Depending on the implementation, some information from the long listing, such as group and user ids, might not be available and will be displayed as 0. When listing several files or directories, if one returns an error, the execution is canceled. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> show help about the command</dd>
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
<dt><code>-a, &#8211;all</code></dt>
<dd> don&#8217;t hide files with name starting in &#8216;.&#8217;.</dd>
<dt><code>-l, &#8211;long</code></dt>
<dd> long listing format. Following columns are displayed for each entry: mode, number of links, group id, user id, last modification time, size and name.</dd>
<dt><code>-d, &#8211;directory</code></dt>
<dd> list directory entries instead of its contents.</dd>
<dt><code>-H, &#8211;human-readable</code></dt>
<dd> with -l, print sizes in human readable format (e.g., 1K 234M 2G).</dd>
<dt><code>&#8211;time-style</code></dt>
<dd> time style. supports locale, iso, long-iso and full-iso (partially)</dd>
<dt><code>&#8211;full-time</code></dt>
<dd> equivalent to &#8211;time-style=full-iso</dd>
<dt><code>&#8211;color</code></dt>
<dd> enable or disable color output. supports always, never, auto. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Long listing of all files:</dt>
<dd> <code>gfal-ls</code> -laH <a href="srm://endpoint.cern.ch/path/file">srm://endpoint.cern.ch/path/file</a></dd></dl>
<dl>
<dt>List a directory instead of its contents:</dt>
<dd> <code>gfal-ls</code> -d file:///tmp </dd>
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
<p> <code><a href="/docs/linux/man/1-gfal-cat/">gfal-cat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-copy/">gfal-copy</a></code>(1), <code><a href="/docs/linux/man/1-gfal-mkdir/">gfal-mkdir</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rename/">gfal-rename</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rm/">gfal-rm</a></code>(1), <code><a href="/docs/linux/man/1-gfal-save/">gfal-save</a></code>(1), <code>gfal-stat</code>(1), <code><a href="/docs/linux/man/1-gfal-sum/">gfal-sum</a></code>(1), <code><a href="/docs/linux/man/1-gfal-xattr/">gfal-xattr</a></code>(1) </p>
