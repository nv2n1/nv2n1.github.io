---
title: "osinfo-install-script(1)"
name: "osinfo-install-script"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo-install-script/"
description: "osinfo-install-script – generate a script for automated installation"
---

<h2 class="name">NAME</h2>
<p> osinfo-install-script &#8211; generate a script for automated installation </p>
<h2>SYNOPSIS</h2>
<p> osinfo-install-script [<font SIZE="-1">OPTIONS&#8230;</font>] MEDIA-FILE|OS-ID</p>
<h2>DESCRIPTION</h2>
<p> Generate a script suitable for performing an automated installation of <tt>&quot;MEDIA_FILE&quot;</tt> or <tt>&quot;OS-ID&quot;</tt>. <tt>&quot;MEDIA_FILE&quot;</tt> should be a path to an installer or live media (typically an <font SIZE="-1">ISO</font> file). <tt>&quot;OS-ID&quot;</tt> should be a <font SIZE="-1">URI</font> identifying the operating system, or its short <font SIZE="-1">ID.</font> </p>
<p> By default a script will be generated for a <tt>&quot;JEOS&quot;</tt> style install.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;profile=NAME</code></p>
<dd> Choose the installation script profile. Defaults to <tt>&quot;jeos&quot;</tt>, but can also be <tt>&quot;desktop&quot;</tt>, or a site specific profile name</p>
<dt><code>&#8211;config=key=value</code></p>
<dd> Set the configuration parameter <tt>&quot;key&quot;</tt> to <tt>&quot;value&quot;</tt>.</dl>
<h2>CONFIGURATION KEYS</h2>
<p> The following configuration keys are available</p>
<dl>
<dt>&quot;hardware-arch&quot;</p>
<dd> The hardware architecture</p>
<dt>&quot;l10n-timezone&quot;</p>
<dd> The local timezone</p>
<dt>&quot;l10n-keyboard&quot;</p>
<dd> The local keyboard layout</p>
<dt>&quot;l10n-language&quot;</p>
<dd> The local language</p>
<dt>&quot;admin-password&quot;</p>
<dd> The administrator password</p>
<dt>&quot;user-password&quot;</p>
<dd> The user password</p>
<dt>&quot;user-login&quot;</p>
<dd> The user login name</p>
<dt>&quot;user-realname&quot;</p>
<dd> The user real name</p>
<dt>&quot;user-autologin&quot;</p>
<dd> Whether to automatically login the user</p>
<dt>&quot;user-admin&quot;</p>
<dd> Whether to give the user administrative privileges</p>
<dt>&quot;reg-product-key&quot;</p>
<dd> The software registration key</p>
<dt>&quot;reg-login&quot;</p>
<dd> The software registration user login</p>
<dt>&quot;reg-password&quot;</p>
<dd> The software registration user password</dl>
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
<p> <tt>&quot;osinfo-install-script&quot;</tt> is distributed under the termsof the <font SIZE="-1">GNU LGPL</font> v2 license. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font> </p>
<h2>Index</h2>
