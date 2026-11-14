---
title: "dpkg-maintscript-helper(1)"
name: "dpkg-maintscript-helper"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-maintscript-helper/"
description: "dpkg-maintscript-helper – works around known dpkg limitations in maintainer scripts"
---

<h2 class="name">NAME</h2>
<p> dpkg-maintscript-helper &#8211; works around known dpkg limitations in maintainer scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-maintscript-helper</code> <i>command</i> [<i>parameter</i>&#8230;] <code>&#8212;</code> <i>maint-script-parameter</i>&#8230;</p>
<h2>COMMANDS AND PARAMETERS</h2>
<dl>
<dt><code>supports</code> <i>command</i></p>
<dd>
<dt><code>rm_conffile</code> <i>conffile</i> [<i>prior-version</i> [<i>package</i>]]</p>
<dd>
<dt><code>mv_conffile</code> <i>old-conffile</i> <i>new-conffile</i> [<i>prior-version</i> [<i>package</i>]]</p>
<dd>
<dt><code>symlink_to_dir</code> <i>pathname</i> <i>old-target</i> [<i>prior-version</i> [<i>package</i>]]</p>
<dd>
<dt><code>dir_to_symlink</code> <i>pathname</i> <i>new-target</i> [<i>prior-version</i> [<i>package</i>]]</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> This program is designed to be run within maintainer scripts to achieve some tasks that <code>dpkg</code> can&#8217;t (yet) handle natively either because of design decisions or due to current limitations. </p>
<p> Many of those tasks require coordinated actions from several maintainer scripts (<code>preinst</code>, <code>postinst</code>, <code>prerm</code>, <code>postrm</code>). To avoid mistakes the same call simply needs to be put in all scripts and the program will automatically adapt its behaviour based on the environment variable <font SIZE="-1"><code>DPKG_MAINTSCRIPT_NAME</code></font> and on the maintainer scripts arguments that you have to forward after a double hyphen.</p>
<h2>COMMON PARAMETERS</h2>
<dl>
<dt><i>prior-version</i></p>
<dd> Defines the latest version of the package whose upgrade should trigger the operation. It is important to calculate <i>prior-version</i> correctly so that the operations are correctly performed even if the user rebuilt the package with a local version. If <i>prior-version</i> is empty or omitted, then the operation is tried on every upgrade (note: it&#8217;s safer to give the version and have the operation tried only once). </p>
<p> If the conffile has not been shipped for several versions, and you are now modifying the maintainer scripts to clean up the obsolete file, <i>prior-version</i> should be based on the version of the package that you are now preparing, not the first version of the package that lacked the conffile. This applies to all other actions in the same way. </p>
<p> For example, for a conffile removed in version <code>2.0-1</code> of a package, <i>prior-version</i> should be set to <code>2.0-1~</code>. This will cause the conffile to be removed even if the user rebuilt the previous version <code>1.0-1</code> as <code>1.0-1local1</code>. Or a package switching a path from a symlink (shipped in version <code>1.0-1</code>) to a directory (shipped in version <code>2.0-1</code>), but only performing the actual switch in the maintainer scripts in version <code>3.0-1</code>, should set <i>prior-version</i> to <code>3.0-1~</code>.</p>
<dt><i>package</i></p>
<dd> The package name owning the pathname(s). When the package is &#8220;Multi-Arch: same&#8221; this parameter must include the architecture qualifier, otherwise it should <code>not</code> usually include the architecture qualifier (as it would disallow cross-grades, or switching from being architecture specific to architecture <code>all</code> or vice versa). If the parameter is empty or omitted, the <font SIZE="-1"><code>DPKG_MAINTSCRIPT_PACKAGE</code></font> and <font SIZE="-1"><code>DPKG_MAINTSCRIPT_ARCH</code></font> environment variables (as set by <code>dpkg</code> when running the maintainer scripts) will be used to generate an arch-qualified package name.</p>
<dt><code>&#8212;</code></p>
<dd> All the parameters of the maintainer scripts have to be forwarded to the program after <code>&#8212;</code>.</dl>
<h2>CONFFILE RELATED TASKS</h2>
<p> When upgrading a package, <code>dpkg</code> will not automatically remove a conffile (a configuration file for which <code>dpkg</code> should preserve user changes) if it is not present in the newer version. There are two principal reasons for this; the first is that the conffile could&#8217;ve been dropped by accident and the next version could restore it, users wouldn&#8217;t want their changes thrown away. The second is to allow packages to transition files from a dpkg-maintained conffile to a file maintained by the package&#8217;s maintainer scripts, usually with a tool like debconf or ucf. </p>
<p> This means that if a package is intended to rename or remove a conffile, it must explicitly do so and <code>dpkg-maintscript-helper</code> can be used to implement graceful deletion and moving of conffiles within maintainer scripts.</p>
<h3>Removing a conffile</h3>
<p> Note: This can be replaced in most cases by the <tt>&quot;remove-on-upgrade&quot;</tt> flag in <i>DEBIAN/conffiles</i> (since dpkg 1.20.6), see <code><a href="/docs/linux/man/5-deb-conffiles/">deb-conffiles</a></code>(5). </p>
<p> If a conffile is completely removed, it should be removed from disk, unless the user has modified it. If there are local modifications, they should be preserved. If the package upgrades aborts, the newly obsolete conffile should not disappear. </p>
<p> All of this is implemented by putting the following shell snippet in the <code>preinst</code>, <code>postinst</code> and <code>postrm</code> maintainer scripts: </p>
<dl>
<dt>
<dd>
<p>&nbsp;dpkg-maintscript-helper rm_conffile&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>conffile</i>&nbsp;<i>prior-version</i>&nbsp;<i>package</i>&nbsp;&#8212;&nbsp;&#8220;$@&#8221;</dl>
<p> <i>conffile</i> is the filename of the conffile to remove. </p>
<p> Current implementation: in the <code>preinst</code>, it checks if the conffile was modified and renames it either to <i>conffile</i><code>.dpkg-remove</code> (if not modified) or to <i>conffile</i><code>.dpkg-backup</code> (if modified). In the <code>postinst</code>, the latter file is renamed to <i>conffile</i><code>.dpkg-bak</code> and kept for reference as it contains user modifications but the former will be removed. If the package upgrade aborts, the <code>postrm</code> reinstalls the original conffile. During purge, the <code>postrm</code> will also delete the <code>.dpkg-bak</code> file kept up to now.</p>
<h3>Renaming a conffile</h3>
<p> If a conffile is moved from one location to another, you need to make sure you move across any changes the user has made. This may seem a simple change to the <code>preinst</code> script at first, however that will result in the user being prompted by <code>dpkg</code> to approve the conffile edits even though they are not responsible of them. </p>
<p> Graceful renaming can be implemented by putting the following shell snippet in the <code>preinst</code>, <code>postinst</code> and <code>postrm</code> maintainer scripts: </p>
<dl>
<dt>
<dd>
<p>&nbsp;dpkg-maintscript-helper mv_conffile&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>old-conffile</i>&nbsp;<i>new-conffile</i>&nbsp;<i>prior-version</i>&nbsp;<i>package</i>&nbsp;&#8212;&nbsp;&#8220;$@&#8221;</dl>
<p> <i>old-conffile</i> and <i>new-conffile</i> are the old and new name of the conffile to rename. </p>
<p> Current implementation: the <code>preinst</code> checks if the conffile has been modified, if yes it&#8217;s left on place otherwise it&#8217;s renamed to <i>old-conffile</i><code>.dpkg-remove</code>. On configuration, the <code>postinst</code> removes <i>old-conffile</i><code>.dpkg-remove</code> and renames <i>old-conffile</i> to <i>new-conffile</i> if <i>old-conffile</i> is still available. On abort-upgrade/abort-install, the <code>postrm</code> renames <i>old-conffile</i><code>.dpkg-remove</code> back to <i>old-conffile</i> if required.</p>
<h2>SYMLINK AND DIRECTORY SWITCHES</h2>
<p> When upgrading a package, <code>dpkg</code> will not automatically switch a symlink to a directory or vice-versa. Downgrades are not supported and the path will be left as is.</p>
<h3>Switching a symlink to directory</h3>
<p> If a symlink is switched to a real directory, you need to make sure before unpacking that the symlink is removed. This may seem a simple change to the <code>preinst</code> script at first, however that will result in some problems in case of admin local customization of the symlink or when downgrading the package. </p>
<p> Graceful renaming can be implemented by putting the following shell snippet in the <code>preinst</code>, <code>postinst</code> and <code>postrm</code> maintainer scripts: </p>
<dl>
<dt>
<dd>
<p>&nbsp;dpkg-maintscript-helper symlink_to_dir&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>pathname</i>&nbsp;<i>old-target</i>&nbsp;<i>prior-version</i>&nbsp;<i>package</i>&nbsp;&#8212;&nbsp;&#8220;$@&#8221;</dl>
<p> <i>pathname</i> is the absolute name of the old symlink (the path will be a directory at the end of the installation) and <i>old-target</i> is the target name of the former symlink at <i>pathname</i>. It can either be absolute or relative to the directory containing <i>pathname</i>. </p>
<p> Current implementation: the <code>preinst</code> checks if the symlink exists and points to <i>old-target</i>, if not then it&#8217;s left in place, otherwise it&#8217;s renamed to <i>pathname</i><code>.dpkg-backup</code>. On configuration, the <code>postinst</code> removes <i>pathname</i><code>.dpkg-backup</code> if <i>pathname</i><code>.dpkg-backup</code> is still a symlink. On abort-upgrade/abort-install, the <code>postrm</code> renames <i>pathname</i><code>.dpkg-backup</code> back to <i>pathname</i> if required.</p>
<h3>Switching a directory to symlink</h3>
<p> If a real directory is switched to a symlink, you need to make sure before unpacking that the directory is removed. This may seem a simple change to the <code>preinst</code> script at first, however that will result in some problems in case the directory contains conffiles, pathnames owned by other packages, locally created pathnames, or when downgrading the package. </p>
<p> Graceful switching can be implemented by putting the following shell snippet in the <code>preinst</code>, <code>postinst</code> and <code>postrm</code> maintainer scripts: </p>
<dl>
<dt>
<dd>
<p>&nbsp;dpkg-maintscript-helper dir_to_symlink&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>pathname</i>&nbsp;<i>new-target</i>&nbsp;<i>prior-version</i>&nbsp;<i>package</i>&nbsp;&#8212;&nbsp;&#8220;$@&#8221;</dl>
<p> <i>pathname</i> is the absolute name of the old directory (the path will be a symlink at the end of the installation) and <i>new-target</i> is the target of the new symlink at <i>pathname</i>. It can either be absolute or relative to the directory containing <i>pathname</i>. </p>
<p> Current implementation: the <code>preinst</code> checks if the directory exists, does not contain conffiles, pathnames owned by other packages, or locally created pathnames, if not then it&#8217;s left in place, otherwise it&#8217;s renamed to <i>pathname</i><code>.dpkg-backup</code>, and an empty staging directory named <i>pathname</i> is created, marked with a file so that dpkg can track it. On configuration, the <code>postinst</code> finishes the switch if <i>pathname</i><code>.dpkg-backup</code> is still a directory and <i>pathname</i> is the staging directory; it removes the staging directory mark file, moves the newly created files inside the staging directory to the symlink target <i>new-target</i>/, replaces the now empty staging directory <i>pathname</i> with a symlink to <i>new-target</i>, and removes <i>pathname</i><code>.dpkg-backup</code>. On abort-upgrade/abort-install, the <code>postrm</code> renames <i>pathname</i><code>.dpkg-backup</code> back to <i>pathname</i> if required.</p>
<h2>INTEGRATION IN PACKAGES</h2>
<p> When using a packaging helper, please check if it has native <code>dpkg-maintscript-helper</code> integration, which might make your life easier. See for example <code><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></code>(1). </p>
<p> Given that <code>dpkg-maintscript-helper</code> is used in the <code>preinst</code>, using it unconditionally requires a pre-dependency to ensure that the required version of <code>dpkg</code> has been unpacked before. The required version depends on the command used, for <code>rm_conffile</code> and <code>mv_conffile</code> it is 1.15.7.2, for <code>symlink_to_dir</code> and <code>dir_to_symlink</code> it is 1.17.14: </p>
<pre>
 Pre-Depends: dpkg (&gt;= 1.17.14)
</pre>
<p> But in many cases the operation done by the program is not critical for the package, and instead of using a pre-dependency we can call the program only if we know that the required command is supported by the currently installed <code>dpkg</code>: </p>
<dl>
<dt>
<dd>
<p>&nbsp;if dpkg-maintscript-helper supports&nbsp;<i>command</i>;&nbsp;then<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dpkg-maintscript-helper&nbsp;<i>command</i>&nbsp;&#8230;<br />
&nbsp;fi</dl>
<p> The command <code>supports</code> will return 0 on success, 1 otherwise. The <code>supports</code> command will check if the environment variables as set by dpkg and required by the script are present, and will consider it a failure in case the environment is not sufficient.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_ROOT</code></font></p>
<dd> If set, it will be used as the filesystem root directory.</p>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></p>
<dd> If set, it will be used as the <code>dpkg</code> data directory.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.19.1). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></code>(1). </p>
<h2>Index</h2>
