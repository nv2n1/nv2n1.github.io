---
title: "up2date(5)"
name: "up2date"
section: "5"
letter: "u"
url: "/docs/linux/man/5-up2date/"
description: "up2date – Configuration file for Red Hat Satellite client programs."
---

<p>up2date &#8211; Configuration file for Red Hat Satellite client programs. </p>
<h2>Description</h2>
<p>Red Hat Satellite client programs, such as <code><a href="/docs/linux/man/8-rhn_check/">rhn_check</a>(8)</code>, use a common configuration file at <i>/etc/sysconfig/rhn/up2date</i>. </p>
<h2>Options</h2>
<dl>
<dt><code>enableProxy</code></dt>
<dd>Use a HTTP Proxy. Can be either 0 (False) or 1 (True). </dd>
<dt><code>serverURL</code></dt>
<dd>Remote server URL </dd>
<dt><code>debug</code></dt>
<dd>Whether or not debugging is enabled. Can be either 0 (False) or 1 (True). </dd>
<dt><code>systemIdPath</code></dt>
<dd>Location of system id file. Expects the path of a file on disk. </dd>
<dt><code>versionOverride</code></dt>
<dd>Override the automatically determined system version. Expects a string or blank (do not override the version). </dd>
<dt><code>httpProxy</code></dt>
<dd>HTTP proxy in host:port format, e.g. squid.redhat.com:3128 </dd>
<dt><code>proxyUser</code></dt>
<dd>The username for an authenticated proxy. </dd>
<dt><code>proxyPassword</code></dt>
<dd>The password to use for an authenticated proxy. </dd>
<dt><code>enableProxyAuth</code></dt>
<dd>To use an authenticated proxy or not. Can be either 0 (False) or 1 (True). </dd>
<dt><code>networkRetries</code></dt>
<dd>Number of attempts to make at network connections before giving up. Expects a positive integer. </dd>
<dt><code>sslCACert</code></dt>
<dd>The CA cert used to verify the ssl server. Expects the path of a file on disk. </dd>
<dt><code>noReboot</code></dt>
<dd>Disable the reboot action. Can be either 0 (False) or 1 (True). </dd>
<dt><code>disallowConfChanges</code></dt>
<dd>Config options that can not be overwritten by a config update action. Expects a semi-colon separated list of config option names.</dd>
<dt><code>hostedWhitelist</code></dt>
<dd>Override the default list of URLs the RHN Register client treats as official RHN hosted servers. This only affects the RHN Register graphical- and text-based clients, as it changes some of the options that appear. This option is included for testing purposes only. </dd>
<dt><code>retrieveOnly</code></dt>
<dd>If set to 1 (True), package installs done through rhn_check will only download the package, the package will not be installed.
</dd></dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sysconfig/rhn/up2date</i></dt>
<dd>The location of this configuration file </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rhn_check/">rhn_check</a></code>(8), <code><a href="/docs/linux/man/8-rhn_register/">rhn_register</a></code>(8), <code><a href="/docs/linux/man/8-rhnreg_ks/">rhnreg_ks</a></code>(8), <code><a href="/docs/linux/man/8-rhnsd/">rhnsd</a></code>(8), <code><a href="/docs/linux/man/8-rhn-profile-sync/">rhn-profile-sync</a></code>(8), <code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8), <code><a href="/docs/linux/man/5-rhnplugin-conf/">rhnplugin.conf</a></code>(5). </p>
<h2>Authors</h2>
<p>See the AUTHORS file included with this software. </p>
<p> This manual page was written by James Bowes &lt;jbowes [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;. </p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999-2010 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
