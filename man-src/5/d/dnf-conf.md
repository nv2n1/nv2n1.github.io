---
title: "dnf-conf(5)"
name: "dnf-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dnf-conf/"
description: "dnf.conf – DNF Configuration Reference"
---

<p>dnf.conf &#8211; DNF Configuration Reference</p>
<h2>Description</h2>
<p><i>DNF</i> by default uses the global configuration file at <code>/etc/dnf/dnf.conf</code> and all *.repo files found under <code>/etc/yum.repos.d</code>. The latter is typically used for repository configuration. </p>
<p> There are two types of sections in the configuration files: main and repository. Main defines all global configuration options. There should be only one main section. The repository sections define the configuration for each (remote or local) repository.</p>
<h2>[Main] Options</h2>
<dl>
<dt><code>best</code></p>
<dd>boolean </p>
<p> When upgrading a package, always try to install its highest version available, even only to find out some of its deps are not satisfiable. Enable this if you want to experience broken dependencies in the repositories firsthand. The default is False.</p>
<dt><code>clean_requirements_on_remove</code></p>
<dd>boolean </p>
<p> Remove dependencies that are no longer used during <code>dnf remove</code>. A package only qualifies for removal via <code>clean_requirements_on_remove</code> if it was installed through DNF but not on explicit user request, i.e. it was pulled in as a dependency. The default is True.</p>
<dt><code>debuglevel</code></p>
<dd>integer </p>
<p> Debug messages output level, in the range 0 to 10. The higher the number the more debug output is put to stdout. Default is 2.</p>
<dt><code>errorlevel</code></p>
<dd>integer </p>
<p> Error messages output level, in the range 0 to 10. The higher the number the more error output is put to stderr. Default is 2. This is deprecated in DNF.</p>
<dt><code>installonlypkgs</code></p>
<dd>list </p>
<p> List of provide names of packages that should only ever be installed, never upgraded. Kernels in particular fall into this category.</p>
<dt><code>installonly_limit</code></p>
<dd>integer </p>
<p> Number of installonly packages allowed to be installed concurrently. Defaults to 3.</p>
<dt><code>keepcache</code></p>
<dd>boolean </p>
<p> Keep downloaded packages in the cache. The default is False.</p>
<dt><code>metadata_timer_sync</code></p>
<dd>time in seconds </p>
<p> The minimal period between two consecutive <code>makecache timer</code> runs. The command will stop immediately if it&#8217;s less than this time period since its last run. Does not affect simple <code>makecache</code> run. Use <code>0</code> to completely disable automatic metadata synchronizing. The default corresponds to three hours.</p>
<dt><code>pluginpath</code></p>
<dd>list </p>
<p> List of directories that are searched for plugins to load. Plugins found in <i>any of the directories</i> in this configuration option are used. The default contains a Python version-specific path.</dl>
<h2>Repo Options</h2>
<dl>
<dt><code>cost</code></p>
<dd>integer </p>
<p> The relative cost of accessing this repository, defaulting to 1000. If the same package can be downloaded from two or more repositories, the repository with the lowest cost is preferred.</p>
<dt><code>gpgkey</code></p>
<dd>list of strings </p>
<p> URLs of a GPG key files that can be used for signing metadata and packages of this repository, empty by default. If a file can not be verified using the already imported keys, import of keys from this option is attempted and the keys are then used for verification.</p>
<dt><code>priority</code></p>
<dd>integer </p>
<p> The priority value of this repository, default is 99. If there is more than one candidate package for a particular operation, the one from a repo with <i>the lowest priority value</i> is picked, possibly despite being less convenient otherwise (e.g. by being a lower version).</p>
<dt><code>skip_if_unavailable</code></p>
<dd>boolean </p>
<p> If enabled, DNF will continue running and disable the repository that couldn&#8217;t be contacted for any reason when downloading metadata. This option doesn&#8217;t affect skipping of unavailable packages after dependency resolution. To check inaccessibility of repository use it in combination with <i>refresh command line option</i>. The default is True.</dl>
<h2>Options For Both [Main] And Repo</h2>
<p>Some options can be applied in either the main section, per repository, or in a combination. The value provided in the main section is used for all repositories as the default value and concrete repositories can override it in their configuration.</p>
<dl>
<dt><code>bandwidth</code></p>
<dd>storage size </p>
<p> Total bandwidth available for downloading. Meaningful when used with the <i>throttle option</i>. Storage size is in bytes by default but can be specified with a unit of storage. Valid units are &#8216;k&#8217;, &#8216;M&#8217;, &#8216;G&#8217;.</p>
<dt><code>deltarpm</code></p>
<dd>boolean </p>
<p> When enabled, DNF will save bandwidth by downloading much smaller delta RPM files, rebuilding them to RPM locally. However, this is quite CPU and I/O intensive. Default is True.</p>
<dt><code>enablegroups</code></p>
<dd>boolean </p>
<p> Determines whether DNF will allow the use of package groups for this repository. Default is True (package groups are allowed).</p>
<dt><code>exclude</code></p>
<dd>list </p>
<p> Exclude packages of this repository, specified by a name or a glob and separated by a comma, from all operations. Can be disabled using <code>&#8211;disableexcludes</code> command line switch.</p>
<dt><code>fastestmirror</code></p>
<dd>boolean </p>
<p> If enabled a metric is used to find the fastest available mirror. This overrides the order provided by the mirrorlist/metalink file itself. This file is often dynamically generated by the server to provide the best download speeds and enabling fastestmirror overrides this. The default is False.</p>
<dt><code>gpgcheck</code></p>
<dd>boolean </p>
<p> Whether to perform GPG signature check on packages found in this repository. The default is False.</p>
<dt><code>include</code></p>
<dd>list </p>
<p> Include packages of this repository, specified by a name or a glob and separated by a comma, from all operations. Inverse of <i>exclude</i>, DNF will exclude any package in the repo. that doesn&#8217;t match this list. This works in conjunction with exclude and doesn&#8217;t override it, so if you &#8216;exclude=*.i386&#8217; and &#8216;include=python*&#8217; then only packages starting with python that do not have an i386 arch. will be seen by DNF in this repo. Can be disabled using <code>&#8211;disableexcludes</code> command line switch.</p>
<dt><code>ip_resolve</code></p>
<dd>IP address type </p>
<p> Determines how DNF resolves host names. Set this to &#8216;4&#8217;/&#8217;IPv4&#8242; or &#8216;6&#8217;/&#8217;IPv6&#8242; to resolve to IPv4 or IPv6 addresses only. By default, DNF resolves to either addresses.</p>
<dt><code>metadata_expire</code></p>
<dd>time in seconds </p>
<p> The period after which the remote repository is checked for metadata update and in the positive case the local metadata cache is updated. The default corresponds to 48 hours. Set this to <code>-1</code> or <code>never</code> to make the repo never considered expired.</p>
<dt><code>minrate</code></p>
<dd>storage size </p>
<p> This sets the low speed threshold in bytes per second. If the server is sending data at the same or slower speed than this value for at least <i>timeout option</i> seconds, DNF aborts the connection. The default is 0. Valid units are &#8216;k&#8217;, &#8216;M&#8217;, &#8216;G&#8217;.</p>
<dt><code>proxy</code></p>
<dd>string </p>
<p> URL of a proxy server to connect through. If none is specified then direct connection is used (the default).</p>
<dt><code>proxy_username</code></p>
<dd>string </p>
<p> The username to use for connecting to the proxy server. Empty by default.</p>
<dt><code>proxy_password</code></p>
<dd>string </p>
<p> The password to use for connecting to the proxy server. Empty by default.</p>
<dt><code>repo_gpgcheck</code></p>
<dd>boolean </p>
<p> Whether to perform GPG signature check on this repository&#8217;s metadata. The default is False.</p>
<dt><code>sslverify</code></p>
<dd>boolean </p>
<p> When enabled, remote SSL connections are verified. If the client can not be authenticated connecting fails and the given repo is not used further. On False, SSL connections can be used but are not verified. Default is True.</p>
<dt><code>throttle</code></p>
<dd>storage size </p>
<p> Limits the downloading speed. It might be an absolute value or a percentage, relative to the value of the <i>bandwidth option</i> option. <code>0</code> means no throttling (the default). The absolute value is in bytes by default but can be specified with a unit of storage. Valid units are &#8216;k&#8217;, &#8216;M&#8217;, &#8216;G&#8217;.</p>
<dt><code>timeout</code></p>
<dd>time in seconds </p>
<p> Number of seconds to wait for a connection before timing out. Used in combination with <i>minrate option</i> option. Defaults to 30 seconds.</dl>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd><i><a href="/docs/linux/man/8-dnf/">dnf</a>(8)</i>, <i>DNF Command Reference</i></dl>
<h2>Author</h2>
<p>See AUTHORS in DNF source distribution.</p>
<h2>Copyright</h2>
<p>2012-2014, Red Hat, Licensed under GPLv2+</p>
