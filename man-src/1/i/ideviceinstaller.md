---
title: "ideviceinstaller(1)"
name: "ideviceinstaller"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ideviceinstaller/"
description: "ideviceinstaller – Manage iDevice apps"
---

<h2 class="name">NAME</h2>
<p> ideviceinstaller &#8211; Manage iDevice apps </p>
<h2>SYNOPSIS</h2>
<p> <code>ideviceinstaller</code> [OPTIONS] </p>
<h2>DESCRIPTION</h2>
<p> Allows to install, upgrade, uninstall, archive, restore and enumerate installed or archived apps on iDevices. </p>
<h2>OPTIONS</h2>
<h3>General options:</h3>
<dl>
<dt><code>-d, &#8211;debug</code></p>
<dd> enable communication debugging.</p>
<dt><code>-U, &#8211;uuid UUID</code></p>
<dd> target specific device by its 40-digit device UUID.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> prints usage information </p>
</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-l, &#8211;list-apps</code></p>
<dd> list apps installed on the device. </p>
<dl>
<dt>
<dd> <code>Additional options:</code></p>
<dl>
<dt>-o list_user</p>
<dd> list user apps only (apps installed by the user) <code>This is the default.</code></p>
<dt>-o list_system</p>
<dd> list system apps only (apps available from the system firmware)</p>
<dt>-o list_all</p>
<dd> list all types of apps</p>
<dt>-o xml</p>
<dd> print output in xml format (PList)</dl>
</dl>
<dt><code>-i, &#8211;install ARCHIVE</code></p>
<dd> install app from a package file specified by ARCHIVE. </p>
<dt><code>-u, &#8211;uninstall APPID</code></p>
<dd> uninstall app specified by APPID. </p>
<dt><code>-g, &#8211;upgrade APPID</code></p>
<dd> upgrade app specified by APPID. </p>
<dt><code>-r, &#8211;restore APPID</code></p>
<dd> restore archived app specified by APPID. </p>
<dt><code>-L, &#8211;list-archives</code></p>
<dd> list archived applications on the device. </p>
<dl>
<dt>
<dd> <code>Additional options:</code></p>
<dl>
<dt>-o xml</p>
<dd> print output in xml format (PList)</dl>
</dl>
<dt><code>-a, &#8211;archive APPID</code></p>
<dd> archive app specified by APPID. </p>
<dl>
<dt>
<dd> <code>Additional options:</code></p>
<dl>
<dt>-o uninstall</p>
<dd> uninstall the package after making an archive</p>
<dt>-o app_only</p>
<dd> archive application data only</p>
<dt>-o copy=PATH</p>
<dd> copy the app archive to directory PATH when done</p>
<dt>-o remove</p>
<dd> only valid when copy=PATH is used: remove after copy</dl>
</dl>
<dt><code>-R, &#8211;remove-archive APPID</code></p>
<dd> remove app archive specified by APPID. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Martin Szulecki. </p>
<h2>Index</h2>
