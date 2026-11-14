---
title: "dpkg-statoverride(1)"
name: "dpkg-statoverride"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-statoverride/"
description: "dpkg-statoverride – override ownership and mode of files"
---

<h2 class="name">NAME</h2>
<p> dpkg-statoverride &#8211; override ownership and mode of files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-statoverride</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> &#8220;<code>stat overrides</code>&#8221; are a way to tell <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) to use a different owner or mode for a path when a package is installed (this applies to any filesystem object that <code>dpkg</code> handles, including directories, devices, etc.). This can be used to force programs that are normally setuid to be install without a setuid flag, or only executable by a certain group. </p>
<p> <code>dpkg-statoverride</code> is a utility to manage the list of stat overrides. It has three basic functions: adding, removing and listing overrides.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>&#8211;add</code> <i>user group mode path</i></p>
<dd> Add an override for <i>path</i>. <i>path</i> does not need to exist when this command is used; the override will be stored and used later. Users and groups can be specified by their name (for example <code>root</code> or <code>nobody</code>), or by their number by prepending the number with a &#8216;<code>#</code>&#8216; (for example <code>#0</code> or <code>#65534</code>). The <i>mode</i> needs to be specified in octal. </p>
<p> If <code>&#8211;update</code> is specified and <i>path</i> exists, it is immediately set to the new owner and mode.</p>
<dt><code>&#8211;remove</code> <i>path</i></p>
<dd> Remove an override for <i>path</i>, the status of <i>path</i> is left unchanged by this command.</p>
<dt><code>&#8211;list</code> [<i>glob-pattern</i>]</p>
<dd> List all overrides. If a glob pattern is specified restrict the output to overrides which match the glob.</p>
<dt><code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;force-help</code></p>
<dd> Give help about the <code>&#8211;force-</code><i>thing</i> options (since dpkg 1.19.5).</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;admindir</code> <i>directory</i></p>
<dd> Set the administrative directory to <i>directory</i>. This is where the <i>statoverride</i> file is stored. Defaults to &laquo;<i>/var/lib/dpkg</i>&raquo;.</p>
<dt><code>&#8211;instdir</code> <i>directory</i></p>
<dd> Set the installation directory, which refers to the directory where packages get installed (since dpkg 1.19.2). Defaults to &laquo;<i>/</i>&raquo;.</p>
<dt><code>&#8211;root</code> <i>directory</i></p>
<dd> Set the root directory to <code>directory</code>, which sets the installation directory to &laquo;<i>directory</i>&raquo; and the administrative directory to &laquo;<i>directory</i><code>/var/lib/dpkg</code>&raquo; (since dpkg 1.19.2).</p>
<dt><code>&#8211;force-</code><i>things</i></p>
<dd>
<dt><code>&#8211;no-force-</code><i>things</i>, <code>&#8211;refuse-</code><i>things</i></p>
<dd> Force or refuse (<code>no-force</code> and <code>refuse</code> mean the same thing) to do some things (since dpkg 1.19.5). <i>things</i> is a comma separated list of things specified below. <code>&#8211;force-help</code> displays a message describing them. Things marked with (*) are forced by default. </p>
<p> <i>Warning: These options are mostly intended to be used by experts only. Using them without fully understanding their effects may break your whole system.</i> </p>
<p> <code>all</code>: Turns on (or off) all force options. </p>
<p> <code>statoverride-add</code>: Overwrite an existing stat override when adding it (since dpkg 1.19.5). </p>
<p> <code>statoverride-remove</code>: Ignore a missing stat override when removing it (since dpkg 1.19.5). </p>
<p> <code>security-mac</code>(*): Use platform-specific Mandatory Access Controls (<font SIZE="-1">MAC</font>) based security when installing files into the filesystem (since dpkg 1.19.5). On Linux systems the implementation uses SELinux.</p>
<dt><code>&#8211;force</code></p>
<dd> Force an action, even if a sanity check would otherwise prohibit it. This is necessary to override an existing override. This option is deprecated (since dpkg 1.19.5), it is replaced by <code>&#8211;force-all</code>.</p>
<dt><code>&#8211;update</code></p>
<dd> Immediately try to change the <i>path</i> to the new owner and mode if it exists.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Be less verbose about what we do.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> The requested action was successfully performed.</p>
<dt><code>1</code></p>
<dd> For <code>&#8211;list</code>, if there are no overrides or none match the supplied glob.</p>
<dt><code>2</code></p>
<dd> Fatal or unrecoverable error due to invalid command-line usage, or interactions with the system, such as accesses to the database, memory allocations, etc.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_ROOT</code></font></p>
<dd> If set and the <code>&#8211;instdir</code> or <code>&#8211;root</code> options have not been specified, it will be used as the filesystem root directory (since dpkg 1.19.2).</p>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></p>
<dd> If set and the <code>&#8211;admindir</code> or <code>&#8211;root</code> options have not been specified, it will be used as the <code>dpkg</code> data directory.</p>
<dt><font SIZE="-1"><code>DPKG_FORCE</code></font></p>
<dd> If set and none of the <code>&#8211;force-</code><i>&#8230;</i> options have been specified, it will be used as the force options to use (since dpkg 1.19.5).</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/dpkg/statoverride</i></p>
<dd> File which contains the current list of stat overrides of the system. It is located in the <code>dpkg</code> administration directory, along with other files important to <code>dpkg</code>, such as <i>status</i> or <i>available</i>. </p>
<p> <code>Note:</code> <code>dpkg-statoverride</code> preserves the old copy of this file, with extension &#8220;-old&#8221;, before replacing it with the new one.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
<h2>Index</h2>
