---
title: "pecl(1)"
name: "pecl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pecl/"
description: "pear, pecl, peardev – PEAR installer"
---

<h2>NAME</h2>
<p> pear, pecl, peardev &#8211; PEAR installer </p>
<h2>SYNOPSIS</h2>
<p> <code>pear</code> [ options ] command [command-options] &lt;parameters&gt; </p>
<p> <code>pecl</code> [ options ] command [command-options] &lt;parameters&gt; </p>
<p> <code>peardev</code> [ options ] command [command-options] &lt;parameters&gt; </p>
<h2>DESCRIPTION</h2>
<p> <code>PEAR</code> is the PHP Extension and Application Repository, found at <code><a rel="nofollow" href="http://pear.php.net.">http://pear.php.net.</a></code> </p>
<p> The <code>pear</code> command is used to install PEAR extensions. </p>
<p> The <code>pecl</code> command is used to install PECL extensions. </p>
<p> The <code>peardev</code> command is a wrapper for the <code>pear</code> command which removes the normal configured memory limit. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> increase verbosity level (default 1)</p>
<dt><code>-q</code></p>
<dd> be quiet, decrease verbosity level</p>
<dt><code>-c </code><i>file</i></p>
<dd> find user configuration in <code>file</code></p>
<dt><code>-C </code><i>file</i></p>
<dd> find system configuration in <code>file</code></p>
<dt><code>-d </code><i>foo=bar</i></p>
<dd> set user config variable <code>foo</code> to <code>bar</code></p>
<dt><code>-D </code><i>foo=bar</i></p>
<dd> set system config variable <code>foo</code> to <code>bar</code></p>
<dt><code>-G</code></p>
<dd> start in graphical (Gtk) mode</p>
<dt><code>-S</code></p>
<dd> store system configuration</p>
<dt><code>-s</code></p>
<dd> store user configuration</p>
<dt><code>-y </code><i>foo</i></p>
<dd> unset <code>foo</code> in the user configuration</p>
<dt><code>-V</code></p>
<dd> version information</p>
<dt>
<dd> <code>-h</code></p>
<dt>
<dd> <code>-?</code> display help/usage </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>build</code></p>
<dd> Build an Extension From C Source</p>
<dt><code>bundle</code></p>
<dd> Unpacks a Pecl Package <code>channel-add</code> Add a Channel</p>
<dt><code>channel-alias</code></p>
<dd> Specify an alias to a channel name</p>
<dt><code>channel-delete</code></p>
<dd> Remove a Channel From the List</p>
<dt><code>channel-discover</code></p>
<dd> Initialize a Channel from its server</p>
<dt><code>channel-info</code></p>
<dd> Retrieve Information on a Channel</p>
<dt>
<dt><code>channel-login</code></p>
<dd>
<dd> Connects and authenticates to remote channel server</p>
<dt><code>channel-logout</code></p>
<dd> Logs out from the remote channel server</p>
<dt><code>channel-update</code></p>
<dd> Update an Existing Channel</p>
<dt><code>clear-cache</code></p>
<dd> Clear Web Services Cache</p>
<dt><code>config-create</code></p>
<dd> Create a Default configuration file</p>
<dt><code>config-get</code></p>
<dd> Show One Setting</p>
<dt><code>config-help</code></p>
<dd> Show Information About Setting</p>
<dt><code>config-set</code></p>
<dd> Change Setting</p>
<dt><code>config-show</code></p>
<dd> Show All Settings</p>
<dt><code>convert</code></p>
<dd> Convert a package.xml 1.0 to package.xml 2.0 format</p>
<dt><code>cvsdiff</code></p>
<dd> Run a &quot;cvs diff&quot; for all files in a package</p>
<dt><code>cvstag</code></p>
<dd> Set CVS Release Tag</p>
<dt><code>download</code></p>
<dd> Download Package</p>
<dt><code>download-all</code></p>
<dd> Downloads each available package from the default channel</p>
<dt><code>info</code></p>
<dd> Display information about a package</p>
<dt><code>install</code></p>
<dd> Install Package</p>
<dt><code>list</code></p>
<dd> List Installed Packages In The Default Channel</p>
<dt><code>list-all</code></p>
<dd> List All Packages</p>
<dt><code>list-channels</code></p>
<dd> List Available Channels</p>
<dt><code>list-files</code></p>
<dd> List Files In Installed Package</p>
<dt><code>list-upgrades</code></p>
<dd> List Available Upgrades</p>
<dt><code>login</code></p>
<dd> Connects and authenticates to remote server [Deprecated in favor of channel-login]</p>
<dt><code>logout</code></p>
<dd> Logs out from the remote server [Deprecated in favor of channel-logout]</p>
<dt><code>make-rpm-spec</code></p>
<dd> Builds an RPM spec file from a PEAR package</p>
<dt><code>makerpm</code></p>
<dd> Builds an RPM spec file from a PEAR package</p>
<dt><code>package</code></p>
<dd> Build Package</p>
<dt><code>package-dependencies</code></p>
<dd> Show package dependencies</p>
<dt><code>package-validate</code></p>
<dd> Validate Package Consistency</p>
<dt><code>pickle</code></p>
<dd> Build PECL Package</p>
<dt><code>remote-info</code></p>
<dd> Information About Remote Packages</p>
<dt><code>remote-list</code></p>
<dd> List Remote Packages</p>
<dt><code>run-scripts</code></p>
<dd> Run Post-Install Scripts bundled with a package</p>
<dt><code>run-tests</code></p>
<dd> Run Regression Tests</p>
<dt><code>search</code></p>
<dd> Search remote package database</p>
<dt><code>shell-test</code></p>
<dd> Shell Script Test</p>
<dt><code>sign</code></p>
<dd> Sign a package distribution file</p>
<dt><code>svntag</code></p>
<dd> Set SVN Release Tag</p>
<dt><code>uninstall</code></p>
<dd> Un-install Package</p>
<dt><code>update-channels</code></p>
<dd> Update the Channel List</p>
<dt><code>upgrade</code></p>
<dd> Upgrade Package</p>
<dt><code>upgrade-all</code></p>
<dd> Upgrade All Packages [Deprecated in favor of calling upgrade with no parameters] </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pear.conf</code></p>
<dd> The system configuration file.</p>
<dt><code>$HOME/.pearrc</code></p>
<dd> The user configuration. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>To list all options, use</p>
<dd> pear help options</p>
<dt>To list all command shortcuts, use</p>
<dd> pear help shortcuts</p>
<dt>to get the help for the specified command, use</p>
<dd> pear help <i>command</i></p>
<dt>Documentation for PEAR can be found at</p>
<dd></dl>
<p> <code><a rel="nofollow" href="http://pear.php.net/manual/">http://pear.php.net/manual/</a></code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997-2009 Stig Bakken, Gregory Beaver, Helgi Þormar Þorbjörnsson, Tomas V.V.Cox, Martin Jansen. </p>
<p> All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. </p>
<h2>BUGS</h2>
<p> You can view the list of known bugs or report any new bug you found at: </p>
<p> <code><a rel="nofollow" href="http://pear.php.net/bugs/">http://pear.php.net/bugs/</a></code> </p>
<h2>Index</h2>
