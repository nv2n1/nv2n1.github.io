---
title: "dpkg-divert(1)"
name: "dpkg-divert"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-divert/"
description: "dpkg-divert – override a package’s version of a file"
---

<h2 class="name">NAME</h2>
<p> dpkg-divert &#8211; override a package&#8217;s version of a file </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-divert</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-divert</code> is the utility used to set up and update the list of diversions. </p>
<p> File <i>diversions</i> are a way of forcing <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) not to install a file into its location, but to a <i>diverted</i> location. Diversions can be used through the Debian package scripts to move a file away when it causes a conflict. System administrators can also use it to override some package&#8217;s configuration file, or whenever some files (which aren&#8217;t marked as &#8220;conffiles&#8221;) need to be preserved by <code>dpkg</code>, when installing a newer version of a package which contains those files.</p>
<h2>COMMANDS</h2>
<dl>
<dt>[<code>&#8211;add</code>] <i>file</i></p>
<dd> Add a diversion for <i>file</i>. The file is currently not renamed, see <code>&#8211;rename</code>.</p>
<dt><code>&#8211;remove</code> <i>file</i></p>
<dd> Remove a diversion for <i>file</i>. The file is currently not renamed, see <code>&#8211;rename</code>.</p>
<dt><code>&#8211;list</code> <i>glob-pattern</i></p>
<dd> List diversions matching <i>glob-pattern</i>.</p>
<dt><code>&#8211;listpackage</code> <i>file</i></p>
<dd> Print the name of the package that diverts <i>file</i> (since dpkg 1.15.0). Prints <font SIZE="-1">LOCAL</font> if <i>file</i> is locally diverted and nothing if <i>file</i> is not diverted.</p>
<dt><code>&#8211;truename</code> <i>file</i></p>
<dd> Print the real name for a diverted file.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;admindir</code> <i>directory</i></p>
<dd> Set the administrative directory to <i>directory</i>. Defaults to &laquo;<i>/var/lib/dpkg</i>&raquo;.</p>
<dt><code>&#8211;instdir</code> <i>directory</i></p>
<dd> Set the installation directory, which refers to the directory where packages get installed (since dpkg 1.19.2). Defaults to &laquo;<i>/</i>&raquo;.</p>
<dt><code>&#8211;root</code> <i>directory</i></p>
<dd> Set the root directory to <code>directory</code>, which sets the installation directory to &laquo;<i>directory</i>&raquo; and the administrative directory to &laquo;<i>directory</i><code>/var/lib/dpkg</code>&raquo; (since dpkg 1.19.2).</p>
<dt><code>&#8211;divert</code> <i>divert-to</i></p>
<dd> <i>divert-to</i> is the location where the versions of <i>file</i>, as provided by other packages, will be diverted.</p>
<dt><code>&#8211;local</code></p>
<dd> Specifies that all packages&#8217; versions of this file are diverted. This means, that there are no exceptions, and whatever package is installed, the file is diverted. This can be used by an admin to install a locally modified version.</p>
<dt><code>&#8211;package</code> <i>package</i></p>
<dd> <i>package</i> is the name of a package whose copy of <i>file</i> will not be diverted. i.e. <i>file</i> will be diverted for all packages except <i>package</i>.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Quiet mode, i.e. no verbose output.</p>
<dt><code>&#8211;rename</code></p>
<dd> Actually move the file aside (or back). <code>dpkg-divert</code> will abort operation in case the destination file already exists. This is the common behavior used for diversions of files from the non-<code>Essential</code> package set (see <code>&#8211;no-rename</code> for more details).</p>
<dt><code>&#8211;no-rename</code></p>
<dd> Specifies that the file should not be renamed while adding or removing the diversion into the database (since dpkg 1.19.1). This is intended for diversions of files from the <code>Essential</code> package set, where the temporary disappearance of the original file is not acceptable, as it can render the system non-functional. This is the default behavior, but that will change in the dpkg 1.20.x cycle.</p>
<dt><code>&#8211;test</code></p>
<dd> Test mode, i.e. don&#8217;t actually perform any changes, just demonstrate.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> The requested action was successfully performed.</p>
<dt><code>2</code></p>
<dd> Fatal or unrecoverable error due to invalid command-line usage, or interactions with the system, such as accesses to the database, memory allocations, etc.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_ROOT</code></font></p>
<dd> If set and the <code>&#8211;instdir</code> or <code>&#8211;root</code> options have not been specified, it will be used as the filesystem root directory (since dpkg 1.19.2).</p>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></p>
<dd> If set and the <code>&#8211;admindir</code> or <code>&#8211;root</code> options have not been specified, it will be used as the <code>dpkg</code> data directory.</p>
<dt><font SIZE="-1"><code>DPKG_MAINTSCRIPT_PACKAGE</code></font></p>
<dd> If set and the <code>&#8211;local</code> and <code>&#8211;package</code> options have not been specified, <code>dpkg-divert</code> will use it as the package name.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/dpkg/diversions</i></p>
<dd> File which contains the current list of diversions of the system. It is located in the <code>dpkg</code> administration directory, along with other files important to <code>dpkg</code>, such as <i>status</i> or <i>available</i>. </p>
<p> <code>Note:</code> <code>dpkg-divert</code> preserves the old copy of this file, with extension <i>-old</i>, before replacing it with the new one.</dl>
<h2>NOTES</h2>
<p> When adding, default is <code>&#8211;local</code> and <code>&#8211;divert</code> <i>original</i><code>.distrib</code>. When removing, <code>&#8211;package</code> or <code>&#8211;local</code> and <code>&#8211;divert</code> must match if specified. </p>
<p> Directories can&#8217;t be diverted with <code>dpkg-divert</code>. </p>
<p> Care should be taken when diverting shared libraries, <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8) creates a symbolic link based on the <font SIZE="-1">DT_SONAME</font> field embedded in the library. Because <code>ldconfig</code> doesn&#8217;t honour diverts (only <code>dpkg</code> does), the symlink may end up pointing at the diverted library, if a diverted library has the same <font SIZE="-1">SONAME</font> as the undiverted one.</p>
<h2>EXAMPLES</h2>
<p> To divert all copies of a <i>/usr/bin/example</i> to <i>/usr/bin/example.foo</i>, i.e. directs all packages providing <i>/usr/bin/example</i> to install it as <i>/usr/bin/example.foo</i>, performing the rename if required: </p>
<pre>
 dpkg-divert --divert /usr/bin/example.foo --rename /usr/bin/example
</pre>
<p> To remove that diversion: </p>
<pre>
 dpkg-divert --rename --remove /usr/bin/example
</pre>
<p> To divert any package trying to install <i>/usr/bin/example</i> to <i>/usr/bin/example.foo</i>, except your own <i>wibble</i> package: </p>
<pre>
 dpkg-divert --package wibble --divert /usr/bin/example.foo \
    --rename /usr/bin/example
</pre>
<p> To remove that diversion: </p>
<pre>
 dpkg-divert --package wibble --rename --remove /usr/bin/example
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
<h2>Index</h2>
