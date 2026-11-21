---
title: "ideviceinstaller(1)"
name: "ideviceinstaller"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ideviceinstaller/"
description: "ideviceinstaller – Manage iDevice apps"
---

<h2>SYNOPSIS</h2>
<p> <code>ideviceinstaller</code> [OPTIONS] </p>
<h2>DESCRIPTION</h2>
<p> Allows to install, upgrade, uninstall, archive, restore and enumerate installed or archived apps on iDevices. </p>
<h2>OPTIONS</h2>
<h3>General options:</h3>
<dl>
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-U, &#8211;uuid UUID</code></dt>
<dd> target specific device by its 40-digit device UUID.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information </dd>
</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-l, &#8211;list-apps</code></dt>
<dd> list apps installed on the device. </dd>
<dl>
<dt>
</dt><dd> <code>Additional options:</code></dd>
<dl>
<dt>-o list_user</dt>
<dd> list user apps only (apps installed by the user) <code>This is the default.</code></dd>
<dt>-o list_system</dt>
<dd> list system apps only (apps available from the system firmware)</dd>
<dt>-o list_all</dt>
<dd> list all types of apps</dd>
<dt>-o xml</dt>
<dd> print output in xml format (PList)</dd></dl>
</dl>
<dt><code>-i, &#8211;install ARCHIVE</code></dt>
<dd> install app from a package file specified by ARCHIVE. </dd>
<dt><code>-u, &#8211;uninstall APPID</code></dt>
<dd> uninstall app specified by APPID. </dd>
<dt><code>-g, &#8211;upgrade APPID</code></dt>
<dd> upgrade app specified by APPID. </dd>
<dt><code>-r, &#8211;restore APPID</code></dt>
<dd> restore archived app specified by APPID. </dd>
<dt><code>-L, &#8211;list-archives</code></dt>
<dd> list archived applications on the device. </dd>
<dl>
<dt>
</dt><dd> <code>Additional options:</code></dd>
<dl>
<dt>-o xml</dt>
<dd> print output in xml format (PList)</dd></dl>
</dl>
<dt><code>-a, &#8211;archive APPID</code></dt>
<dd> archive app specified by APPID. </dd>
<dl>
<dt>
</dt><dd> <code>Additional options:</code></dd>
<dl>
<dt>-o uninstall</dt>
<dd> uninstall the package after making an archive</dd>
<dt>-o app_only</dt>
<dd> archive application data only</dd>
<dt>-o copy=PATH</dt>
<dd> copy the app archive to directory PATH when done</dd>
<dt>-o remove</dt>
<dd> only valid when copy=PATH is used: remove after copy</dd></dl>
</dl>
<dt><code>-R, &#8211;remove-archive APPID</code></dt>
<dd> remove app archive specified by APPID. </dd>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Martin Szulecki. </p>
