---
title: "gfal-xattr(1)"
name: "gfal-xattr"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-xattr/"
description: "gfal-xattr – show or set attributes of a file"
---

<h2>NAME</h2>
<p> gfal-xattr &#8211; show or set attributes of a file</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-xattr</code> [ <i>OPTION</i> ]&#8230; <i>FILE</i> [ <i>ATTRIBUTE</i> [= <i>VALUE</i> ]] </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-xattr</code> Display attributes of a file or set them to a new value. This command comes in three forms, making it possible, for a specified file, to list all attribute and corresponding values, display the value of a particular attribute or assign a new value to a particular attribute &#8211; see examples.</p>
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
<dt><code>FILE</code></dt>
<dd> file URI</dd>
<dt><code>ATTRIBUTE</code></dt>
<dd> optional argument, specifying a attribute to get or set. If no attribute is given, all attributes and corresponding values are displayed.</dd>
<dt><code>VALUE</code></dt>
<dd> if a attribute is given, a new value can optionally be assigned to it. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Show all attributes and values of a file:</dt>
<dd> <code>gfal-xattr</code> <a href="srm://endpoint.cern.ch/path/file">srm://endpoint.cern.ch/path/file</a></dd></dl>
<dl>
<dt>Show the value of a particular attribute:</dt>
<dd> <code>gfal-xattr</code> <a href="srm://endpoint.cern.ch/path/file">srm://endpoint.cern.ch/path/file</a> user.status</dd></dl>
<dl>
<dt>Set a new value to an attribute:</dt>
<dd> <code>gfal-xattr</code> <a href="srm://endpoint.cern.ch/path/file">srm://endpoint.cern.ch/path/file</a> user.status=new_value</dd></dl>
<dl>
<dt>Typically, you can get the transport urls (turls) with the user.replicas attribute:</dt>
<dd> <a href="srm://endpoint.cern.ch/path/file">srm://endpoint.cern.ch/path/file</a> user.replicas </dd>
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
<p> <code><a href="/docs/linux/man/1-gfal-cat/">gfal-cat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-copy/">gfal-copy</a></code>(1), <code><a href="/docs/linux/man/1-gfal-ls/">gfal-ls</a></code>(1), <code><a href="/docs/linux/man/1-gfal-mkdir/">gfal-mkdir</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rename/">gfal-rename</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rm/">gfal-rm</a></code>(1), <code><a href="/docs/linux/man/1-gfal-save/">gfal-save</a></code>(1), <code>gfal-stat</code>(1), <code><a href="/docs/linux/man/1-gfal-sum/">gfal-sum</a></code>(1) </p>
