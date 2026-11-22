---

title: "osinfo-install-script(1)"
name: "osinfo-install-script"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo-install-script/"
description: "osinfo-install-script – generate a script for automated installation"
---

<p> osinfo-install-script &#8211; generate a script for automated installation </p>
<h2>SYNOPSIS</h2>
<p> osinfo-install-script [OPTIONS&#8230;] MEDIA-FILE|OS-ID</p>
<h2>DESCRIPTION</h2>
<p> Generate a script suitable for performing an automated installation of <tt>&quot;MEDIA_FILE&quot;</tt> or <tt>&quot;OS-ID&quot;</tt>. <tt>&quot;MEDIA_FILE&quot;</tt> should be a path to an installer or live media (typically an ISO file). <tt>&quot;OS-ID&quot;</tt> should be a URI identifying the operating system, or its short ID. </p>
<p> By default a script will be generated for a <tt>&quot;JEOS&quot;</tt> style install.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;profile=NAME</code></dt>
<dd> Choose the installation script profile. Defaults to <tt>&quot;jeos&quot;</tt>, but can also be <tt>&quot;desktop&quot;</tt>, or a site specific profile name</dd>
<dt><code>&#8211;config=key=value</code></dt>
<dd> Set the configuration parameter <tt>&quot;key&quot;</tt> to <tt>&quot;value&quot;</tt>.</dd></dl>
<h2>CONFIGURATION KEYS</h2>
<p> The following configuration keys are available</p>
<dl>
<dt>&quot;hardware-arch&quot;</dt>
<dd> The hardware architecture</dd>
<dt>&quot;l10n-timezone&quot;</dt>
<dd> The local timezone</dd>
<dt>&quot;l10n-keyboard&quot;</dt>
<dd> The local keyboard layout</dd>
<dt>&quot;l10n-language&quot;</dt>
<dd> The local language</dd>
<dt>&quot;admin-password&quot;</dt>
<dd> The administrator password</dd>
<dt>&quot;user-password&quot;</dt>
<dd> The user password</dd>
<dt>&quot;user-login&quot;</dt>
<dd> The user login name</dd>
<dt>&quot;user-realname&quot;</dt>
<dd> The user real name</dd>
<dt>&quot;user-autologin&quot;</dt>
<dd> Whether to automatically login the user</dd>
<dt>&quot;user-admin&quot;</dt>
<dd> Whether to give the user administrative privileges</dd>
<dt>&quot;reg-product-key&quot;</dt>
<dd> The software registration key</dd>
<dt>&quot;reg-login&quot;</dt>
<dd> The software registration user login</dd>
<dt>&quot;reg-password&quot;</dt>
<dd> The software registration user password</dd></dl>
<h2>EXAMPLE USAGE</h2>
<p> The following usage generates a Fedora 16 kickstart script </p>
<pre><code>
#osinfo - install - script-- profile jeos-- config l10n - timezone = GMT-- config l10n - keyboard = uk-- config l10n - language = en_GB-- config admin - password = 123456 --config user - login = berrange-- config user - password = 123456 --config user - realname = "Daniel P Berrange" fedora16
</code></pre>
<h2>EXIT STATUS</h2>
<p> The exit status will be 0 if an install script is generated, or 1 on error</p>
<h2>AUTHORS</h2>
<p> Daniel P. Berrange &lt;berrange [at] redhat.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012 Red Hat, Inc.</p>
<h2>LICENSE</h2>
<p> <tt>&quot;osinfo-install-script&quot;</tt> is distributed under the termsof the GNU LGPL v2 license. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE </p>
