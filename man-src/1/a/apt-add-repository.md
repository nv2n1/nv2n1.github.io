---
title: "apt-add-repository(1)"
name: "apt-add-repository"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-add-repository/"
description: "add-apt-repository – Adds a repository into the /etc/apt/sources.list or /etc/apt/sources.list.d or removes an existing one"
---

<h2 class="name">NAME</h2>
<p> add-apt-repository &#8211; Adds a repository into the /etc/apt/sources.list or /etc/apt/sources.list.d or removes an existing one </p>
<h2>SYNOPSIS</h2>
<p> <code>add-apt-repository </code><i>[OPTIONS]</i> <i>[LINE]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>add-apt-repository</code> is a script which adds an external APT repository to either /etc/apt/sources.list or a file in /etc/apt/sources.list.d/ or removes an already existing repository. </p>
<h2>OPTIONS</h2>
<p> Note that the <code>&#8211;list</code>, <code>&#8211;ppa</code>, <code>&#8211;cloud</code>, <code>&#8211;uri</code>, <code>&#8211;sourceslist</code>, and <code>LINE</code> parameters are mutually exclusive; only one (or none) of them may be specified.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help message and exit.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Print debug information to the command line.</p>
<dt><code>-r, &#8211;remove</code></p>
<dd> Remove the specified repository. </p>
<p> This first will disable (comment out) the matching line(s), and then any modified file(s) under sources.list.d/ will be removed if they contain only empty and commented lines. </p>
<p> Note that this performs differently when used with the <i>&#8211;enable-source</i> and/or <i>&#8211;component</i> parameters. Without either of those parameters, this removes the specified repository, including any <code>deb-src</code> line(s), and all components. If <i>&#8211;enable-source</i> is used, this disables <code>only</code> the &#8216;deb-src&#8217; line(s). If <i>&#8211;component</i> is used, this removes <code>only</code> the specified component(s), and only removes the repository if no components remain. </p>
<p> If both <i>&#8211;enable-source</i> and <i>&#8211;component</i> are used with <i>&#8211;remove</i>, the actions are performed separately: the specified component(s) will be removed from both <code>deb</code> and <code>deb-src</code> lines, and <code>deb-src</code> lines will be disabled.</p>
<dt><code>-y, &#8211;yes</code></p>
<dd> Assume yes to all queries.</p>
<dt><code>-n, &#8211;no-update</code></p>
<dd> After adding the repository, do not update the package cache.</p>
<dt><code>-l, &#8211;login</code></p>
<dd> Login to Launchpad (this is only needed for private PPAs).</p>
<dt><code>-s, &#8211;enable-source</code></p>
<dd> Allow downloading of the source packages from the repository. </p>
<p> This adds and enables a &#8216;deb-src&#8217; line for the repository. </p>
<p> If this parameter is used without any repository, it will enable all currently existing disabled source repository (<i>deb-src</i>) entries that have a corresponding enabled binary repository (<i>deb</i>) entry. </p>
<p> If this parameter is used twice without any repository, it will also add missing source repository entries for all existing binary repository (<i>deb</i>) entries.</p>
<dt><code>-c, &#8211;component</code></p>
<dd> Which component(s) should be used with the specified repository. </p>
<p> If not specified, this will default to <i>main</i>. This may be used multiple times to specify multiple components. </p>
<p> If this is used without any repository, it will add the component(s) to all currently existing (enabled) repositories, but only if listed in the main sources.list file.</p>
<dt><code>-p, &#8211;pocket</code></p>
<dd> What pocket to use. </p>
<p> Defaults to none, which is equivalent to the <i>release</i> pocket. </p>
<p> If this is used without any repository, it will add the pocket to all currently existing repositories, but only if listed in the main sources.list file. It will use the components currently configured with the release pocket, or if that is not currently configured, it will use the <i>main</i> and <i>restricted</i> components.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Show what would be done, but don&#8217;t make any changes.</p>
<dt><code>-L, &#8211;list</code></p>
<dd> List currently configured repositories. </p>
<p> This will only list enabled repositories; it will not show disabled repository lines. </p>
<p> By default, this shows only binary (<i>deb</i>) repositories. If <i>&#8211;enable-source</i> is also used, this will also show source (<i>deb-src</i>) repositories.</p>
<dt><code>-P, &#8211;ppa</code></p>
<dd> Add an Ubuntu Launchpad Personal Package Archive. </p>
<p> Must be in the format <code>ppa:USER/PPA</code>, <code>USER/PPA</code>, or <code>USER</code>. </p>
<p> The <code>USER</code> parameter should be the Launchpad team or person that owns the PPA. The <code>PPA</code> parameter should be the name of the PPA; if not provided, it defaults to &#8216;ppa&#8217;. </p>
<p> The GPG public key of the PPA will also be downloaded and added to apt&#8217;s keyring. </p>
<p> To add a private PPA, you must also use the <i>&#8211;login</i> parameter, and of course you must also be subscribed to the private PPA.</p>
<dt><code>-C, &#8211;cloud</code></p>
<dd> Add an Ubuntu Cloud Archive. </p>
<p> Must be in the format <code>cloud-archive:CANAME</code>, <code>uca:CANAME</code>, or <code>CANAME</code>. </p>
<p> The <code>CANAME</code> parameter should be the name of the Cloud Archive. The <code>CANAME</code> parameter may optionally be suffixed with the pocket, as either <code>-updates</code> or <code>-proposed</code>. If not specified, the pocket defaults to <code>-updates</code>.</p>
<dt><code>-U, &#8211;uri</code></p>
<dd> Add an archive, specified as a single URI. </p>
<p> If the URI provided is detected to be a PPA, this will operate as if the <i>&#8211;ppa</i> parameter was used.</p>
<dt><code>-S, &#8211;sourceslist</code></p>
<dd> Add an archive, specified as a full source entry line in one-line sources.list format. </p>
<p> This must follow the <i>ONE-LINE-STYLE</i> format as described in the <code>sources.list</code> manpage. </p>
<p> If the URI provided is detected to be a PPA, this will operate as if the <i>&#8211;ppa</i> parameter was used. </p>
</dl>
<h2>LINE</h2>
<p> <i>LINE</i> is a deprecated method to specify the repository to add/remove, provided only for backwards compatibility. It can be specified in any of the supported formats: sources.list line, plain uri, ppa shortcut, or cloud-archive shortcut. It can also be specified as one or more valid component(s). The script will attempt to detect which format is provided. </p>
<p> This is not recommended as the autodetection of which line format is intended can be ambiguous, but older scripts may still use this method of specifying the repository. </p>
<p> One special case of <i>LINE</i> is providing the value <code>&#8211;</code>, which will then read the <i>LINE</i> from stdin. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>add-apt-repository -P ppa:user/repository</p>
<dd>
<dt>add-apt-repository -P user/repository</p>
<dd>
<dt>add-apt-repository -C cloud-archive:queens</p>
<dd>
<dt>add-apt-repository -C uca:queens</p>
<dd>
<dt>add-apt-repository -C queens</p>
<dd>
<dt>add-apt-repository -S &#8216;deb <a rel="nofollow" href="http://myserver/path/to/repo">http://myserver/path/to/repo</a> stable main&#8217;</p>
<dd>
<dt>add-apt-repository -S deb <a rel="nofollow" href="http://myserver/path/to/repo">http://myserver/path/to/repo</a> stable main</p>
<dd>
<dt>add-apt-repository -U <a rel="nofollow" href="http://myserver/path/to/repo">http://myserver/path/to/repo</a> -c main</p>
<dd>
<dt>add-apt-repository -U <a rel="nofollow" href="https://packages.medibuntu.org">https://packages.medibuntu.org</a> -c free -c non-free</p>
<dd>
<dt>add-apt-repository -U <a rel="nofollow" href="http://extras.ubuntu.com/ubuntu">http://extras.ubuntu.com/ubuntu</a></p>
<dd>
<dt>add-apt-repository -s</p>
<dd>
<dt>add-apt-repository -L</p>
<dd>
<dt>add-apt-repository -s -r</p>
<dd>
<dt>add-apt-repository -c universe</p>
<dd>
<dt>add-apt-repository -r -c multiverse</p>
<dd>
</dl>
<h2>DEPRECATED EXAMPLES</h2>
<dl>
<dt>add-apt-repository deb <a rel="nofollow" href="http://myserver/path/to/repo">http://myserver/path/to/repo</a> stable main</p>
<dd>
<dt>add-apt-repository <a rel="nofollow" href="http://myserver/path/to/repo">http://myserver/path/to/repo</a> main</p>
<dd>
<dt>add-apt-repository <a rel="nofollow" href="https://packages.medibuntu.org">https://packages.medibuntu.org</a> free non-free</p>
<dd>
<dt>add-apt-repository <a rel="nofollow" href="http://extras.ubuntu.com/ubuntu">http://extras.ubuntu.com/ubuntu</a></p>
<dd>
<dt>add-apt-repository multiverse</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) </p>
<h2>COPYRIGHT</h2>
<p> This manual page was written by Chow Loong Jin &lt;hyperair [at] gmail.com&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses. </p>
<h2>Index</h2>
