---
title: "rhnreg_ks(8)"
name: "rhnreg_ks"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhnreg_ks/"
description: "rhnreg_ks – A program for non interactively registering systems to Red Hat Satellite."
---

<p>rhnreg_ks &#8211; A program for non interactively registering systems to Red Hat Satellite.</p>
<h2>Synopsis</h2>
<p>rhnreg_ks [<i>options</i>] </p>
<h2>Description</h2>
<p>rhnreg_ks is a utility for registering a system with the &quot;<code>Red Hat Satellite</code>&quot;. It is designed to be used in a non-interactive environment (a kickstart style install, for example). All the information can be specified on the command line or stdin. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;profilename</code></p>
<dd>Specify the profile name that should be used as an identifier for the system in Red Hat Satellite </p>
<dt><code>&#8211;username</code></p>
<dd>The username to register the system with under Red Hat Satellite. This can be an existing Red Hat Satellite username, or a new username. </p>
<dt><code>&#8211;password</code></p>
<dd>The password associated with the username specified with the <code>&#8211;username</code> option. This is an unencrypted password. </p>
<dt><code>&#8211;activationkey</code></p>
<dd>Specify/use a serial number to associate with the system. This is optional, but activation keys can really simplify the registration process. Learn more about activation keys in the online RHN documentation. </p>
<dt><code>&#8211;contactinfo</code></p>
<dd>This option has been deprecated. Please login to the server web user interface and update your contactinfo. </p>
<dt><code>&#8211;nohardware</code></p>
<dd>Do not probe or upload any hardware information. </p>
<dt><code>&#8211;nopackages</code></p>
<dd>Do not profile or upload any package information. </p>
<dt><code>&#8211;novirtinfo</code></p>
<dd>Do not profile or upload any virtualization information. </p>
<dt><code>&#8211;norhnsd</code></p>
<dd>Do not start rhnsd after completion. </p>
<dt><code>&#8211;force</code></p>
<dd>Register the system even if it has already been registered. </p>
<dt><code>&#8211;version</code></p>
<dd>Show the version of rhnreg_ks. </p>
<dt><code>&#8211;proxy</code></p>
<dd>Specify a HTTP proxy to use. </p>
<dt><code>&#8211;proxyUser</code></p>
<dd>Specify a username to use with an authenticated HTTP proxy. </p>
<dt><code>&#8211;proxyPassword</code></p>
<dd>Specify a password to use with an authenticated HTTP proxy. </p>
<dt><code>&#8211;sslCACert</code></p>
<dd>Specify a path to a SSL CA certificate to use. </p>
<dt><code>&#8211;serverUrl</code></p>
<dd>Specify a URL to as the server. </p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show a help message and exit. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sysconfig/rhn/systemid</i></p>
<dd>The digital server ID for this machine if the system has been registered onto &quot;<code>Red Hat Satellite</code>&quot;. This file does not exist otherwise. </p>
<dt><i>/etc/sysconfig/rhn/up2date</i></p>
<dd>The common configuration file used by RHN client programs. </p>
</dl>
<h2>Examples</h2>
<p>Register a new system to Red Hat Satellite:</p>
<dl>
<dd>
<pre>rhnreg_ks --profilename &quot;example_profile_name&quot; --username &quot;someexampleuser&quot; --password &quot;foobar&quot;</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rhn_check/">rhn_check</a></code>(8), <code><a href="/docs/linux/man/8-rhn_register/">rhn_register</a></code>(8), <code><a href="/docs/linux/man/8-rhnsd/">rhnsd</a></code>(8), <code><a href="/docs/linux/man/8-rhn-profile-sync/">rhn-profile-sync</a></code>(8), <code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8), <code><a href="/docs/linux/man/5-up2date/">up2date</a></code>(5). </p>
<h2>Authors</h2>
<p>See the AUTHORS file included with this software. </p>
<p> This manual page was written by Adrian Likins &lt;alikins [at] redhat.com&gt; and James Bowes &lt;jbowes [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;. </p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999-2011 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
