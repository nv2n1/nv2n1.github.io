---
title: "idevicebackup(1)"
name: "idevicebackup"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicebackup/"
description: "idevicebackup – Create or restore backup for devices."
---

<h2>NAME</h2>
<p> idevicebackup &#8211; Create or restore backup for devices.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicebackup</code> [OPTIONS] CMD [DIRECTORY] </p>
<h2>DESCRIPTION</h2>
<p> Create or restore backup from the current or specified directory. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u, &#8211;udid UDID</code></p>
<dd> target specific device by its 40-digit device UDID.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> enable communication debugging.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> prints usage information. </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>backup</code></p>
<dd> saves a device backup into DIRECTORY.</p>
<dt><code>restore</code></p>
<dd> restores a device backup from DIRECTORY. </p>
</dl>
<h2>AUTHORS</h2>
<p> Martin Szulecki </p>
<p> Nikias Bassen </p>
<p> Man page written to conform with Debian by Julien Lavergne. </p>
<h2>Index</h2>
