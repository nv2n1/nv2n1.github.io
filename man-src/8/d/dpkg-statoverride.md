---
title: "dpkg-statoverride(8)"
name: "dpkg-statoverride"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dpkg-statoverride/"
description: "dpkg-statoverride – override ownership and mode of files"
---

<p>dpkg-statoverride &#8211; override ownership and mode of files</p>
<h2>Synopsis</h2>
<p><code>dpkg-statoverride</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>Description</h2>
<p>`<code>stat overrides</code>&#8216; are a way to tell <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) to use a different owner or mode for a path when a package is installed (this applies to any filesystem object that <code>dpkg</code> handles, including directories, devices, etc.). This can be used to force programs that are normally setuid to be install without a setuid flag, or only executable by a certain group. </p>
<p> <code>dpkg-statoverride</code> is a utility to manage the list of stat overrides. It has three basic functions: adding, removing and listing overrides.</p>
<h2>Commands</h2>
<dl>
<dt><code>&#8211;add</code><i> user group mode path</i></p>
<dd>Add an override for <i>path</i>. <i>path</i> does not need to exist when this command is used; the override will be stored and used later. Users and groups can be specified by their name (for example <code>root</code> or <code>nobody</code>), or by their number by prepending the number with a `<code>#</code>&#8216; (for example <code>#0</code> or <code>#65534</code>). The <i>mode</i> needs to be specified in octal. </p>
<p> If <code>&#8211;update</code> is specified and <i>path</i> exists, it is immediately set to the new owner and mode.</p>
<dt><code>&#8211;remove</code><i> path</i></p>
<dd>Remove an override for <i>path</i>, the status of <i>path</i> is left unchanged by this command.</p>
<dt><code>&#8211;list</code> [<i>glob-pattern</i>]</p>
<dd>List all overrides. If a glob pattern is specified restrict the output to overrides which match the glob. If there are no overrides or none match the glob <code>dpkg-statoverride</code> will exit with an exitcode of 1.</p>
<dt><code>&#8211;help</code></p>
<dd>Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd>Show the version and exit.</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;admindir</code><i> directory</i></p>
<dd>Change the <i>directory</i> of the <code>dpkg</code> database where the statoverride file is also stored. Defaults to <i>/var/lib/dpkg</i>.</p>
<dt><code>&#8211;force</code></p>
<dd>Force an action, even if a sanity check would otherwise prohibit it. This is necessary to override an existing override.</p>
<dt><code>&#8211;update</code></p>
<dd>Immediately try to change the <i>path</i> to the new owner and mode if it exists.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Be less verbose about what we do.</dl>
<h2>Environment</h2>
<dl>
<dt><code>DPKG_ADMINDIR</code></p>
<dd>If set and the <code>&#8211;admindir</code> option has not been specified, it will be used as the <code>dpkg</code> data directory.</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/dpkg/statoverride</i></p>
<dd>File which contains the current list of stat overrides of the system. It is located in the <code>dpkg</code> administration directory, along with other files important to <code>dpkg</code>, such as `status&#8217; or `available&#8217;.<br />
 Note: <code>dpkg-statoverride</code> preserves the old copy of this file, with extension &quot;-old&quot;, before replacing it with the new one.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
