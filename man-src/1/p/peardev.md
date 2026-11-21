---

title: "peardev(1)"
name: "peardev"
section: "1"
letter: "p"
url: "/docs/linux/man/1-peardev/"
description: "pear, pecl, peardev – PEAR installer"
---

<h2>NAME</h2>
<p> pear, pecl, peardev &#8211; PEAR installer </p>
<p> <code>pear</code> [ options ] command [command-options] &lt;parameters&gt; </p>
<p> <code>pecl</code> [ options ] command [command-options] &lt;parameters&gt; </p>
<p> <code>peardev</code> [ options ] command [command-options] &lt;parameters&gt; </p>
<p> <code>PEAR</code> is the PHP Extension and Application Repository, found at <code><a rel="nofollow" href="http://pear.php.net.">http://pear.php.net.</a></code> </p>
<p> The <code>pear</code> command is used to install PEAR extensions. </p>
<p> The <code>pecl</code> command is used to install PECL extensions. </p>
<p> The <code>peardev</code> command is a wrapper for the <code>pear</code> command which removes the normal configured memory limit. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> increase verbosity level (default 1)</dd>
<dt><code>-q</code></dt>
<dd> be quiet, decrease verbosity level</dd>
<dt><code>-c </code><i>file</i></dt>
<dd> find user configuration in <code>file</code></dd>
<dt><code>-C </code><i>file</i></dt>
<dd> find system configuration in <code>file</code></dd>
<dt><code>-d </code><i>foo=bar</i></dt>
<dd> set user config variable <code>foo</code> to <code>bar</code></dd>
<dt><code>-D </code><i>foo=bar</i></dt>
<dd> set system config variable <code>foo</code> to <code>bar</code></dd>
<dt><code>-G</code></dt>
<dd> start in graphical (Gtk) mode</dd>
<dt><code>-S</code></dt>
<dd> store system configuration</dd>
<dt><code>-s</code></dt>
<dd> store user configuration</dd>
<dt><code>-y </code><i>foo</i></dt>
<dd> unset <code>foo</code> in the user configuration</dd>
<dt><code>-V</code></dt>
<dd> version information</dd>
<dt>
</dt><dd> <code>-h</code></dd>
<dt>
</dt><dd> <code>-?</code> display help/usage </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>build</code></dt>
<dd> Build an Extension From C Source</dd>
<dt><code>bundle</code></dt>
<dd> Unpacks a Pecl Package <code>channel-add</code> Add a Channel</dd>
<dt><code>channel-alias</code></dt>
<dd> Specify an alias to a channel name</dd>
<dt><code>channel-delete</code></dt>
<dd> Remove a Channel From the List</dd>
<dt><code>channel-discover</code></dt>
<dd> Initialize a Channel from its server</dd>
<dt><code>channel-info</code></dt>
<dd> Retrieve Information on a Channel</dd>
<dt>
</dt><dt><code>channel-login</code></dt>
<dd>
</dd><dd> Connects and authenticates to remote channel server</dd>
<dt><code>channel-logout</code></dt>
<dd> Logs out from the remote channel server</dd>
<dt><code>channel-update</code></dt>
<dd> Update an Existing Channel</dd>
<dt><code>clear-cache</code></dt>
<dd> Clear Web Services Cache</dd>
<dt><code>config-create</code></dt>
<dd> Create a Default configuration file</dd>
<dt><code>config-get</code></dt>
<dd> Show One Setting</dd>
<dt><code>config-help</code></dt>
<dd> Show Information About Setting</dd>
<dt><code>config-set</code></dt>
<dd> Change Setting</dd>
<dt><code>config-show</code></dt>
<dd> Show All Settings</dd>
<dt><code>convert</code></dt>
<dd> Convert a package.xml 1.0 to package.xml 2.0 format</dd>
<dt><code>cvsdiff</code></dt>
<dd> Run a &quot;cvs diff&quot; for all files in a package</dd>
<dt><code>cvstag</code></dt>
<dd> Set CVS Release Tag</dd>
<dt><code>download</code></dt>
<dd> Download Package</dd>
<dt><code>download-all</code></dt>
<dd> Downloads each available package from the default channel</dd>
<dt><code>info</code></dt>
<dd> Display information about a package</dd>
<dt><code>install</code></dt>
<dd> Install Package</dd>
<dt><code>list</code></dt>
<dd> List Installed Packages In The Default Channel</dd>
<dt><code>list-all</code></dt>
<dd> List All Packages</dd>
<dt><code>list-channels</code></dt>
<dd> List Available Channels</dd>
<dt><code>list-files</code></dt>
<dd> List Files In Installed Package</dd>
<dt><code>list-upgrades</code></dt>
<dd> List Available Upgrades</dd>
<dt><code>login</code></dt>
<dd> Connects and authenticates to remote server [Deprecated in favor of channel-login]</dd>
<dt><code>logout</code></dt>
<dd> Logs out from the remote server [Deprecated in favor of channel-logout]</dd>
<dt><code>make-rpm-spec</code></dt>
<dd> Builds an RPM spec file from a PEAR package</dd>
<dt><code>makerpm</code></dt>
<dd> Builds an RPM spec file from a PEAR package</dd>
<dt><code>package</code></dt>
<dd> Build Package</dd>
<dt><code>package-dependencies</code></dt>
<dd> Show package dependencies</dd>
<dt><code>package-validate</code></dt>
<dd> Validate Package Consistency</dd>
<dt><code>pickle</code></dt>
<dd> Build PECL Package</dd>
<dt><code>remote-info</code></dt>
<dd> Information About Remote Packages</dd>
<dt><code>remote-list</code></dt>
<dd> List Remote Packages</dd>
<dt><code>run-scripts</code></dt>
<dd> Run Post-Install Scripts bundled with a package</dd>
<dt><code>run-tests</code></dt>
<dd> Run Regression Tests</dd>
<dt><code>search</code></dt>
<dd> Search remote package database</dd>
<dt><code>shell-test</code></dt>
<dd> Shell Script Test</dd>
<dt><code>sign</code></dt>
<dd> Sign a package distribution file</dd>
<dt><code>svntag</code></dt>
<dd> Set SVN Release Tag</dd>
<dt><code>uninstall</code></dt>
<dd> Un-install Package</dd>
<dt><code>update-channels</code></dt>
<dd> Update the Channel List</dd>
<dt><code>upgrade</code></dt>
<dd> Upgrade Package</dd>
<dt><code>upgrade-all</code></dt>
<dd> Upgrade All Packages [Deprecated in favor of calling upgrade with no parameters] </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pear.conf</code></dt>
<dd> The system configuration file.</dd>
<dt><code>$HOME/.pearrc</code></dt>
<dd> The user configuration. </dd>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>To list all options, use</dt>
<dd> pear help options</dd>
<dt>To list all command shortcuts, use</dt>
<dd> pear help shortcuts</dd>
<dt>to get the help for the specified command, use</dt>
<dd> pear help <i>command</i></dd>
<dt>Documentation for PEAR can be found at</dt>
<dd></dd></dl>
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
