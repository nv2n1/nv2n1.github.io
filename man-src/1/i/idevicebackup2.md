---
title: "idevicebackup2(1)"
name: "idevicebackup2"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicebackup2/"
description: "idevicebackup2 – Create or restore backups for devices running iOS 4 or later."
---

<h2>NAME</h2>
<p> idevicebackup2 &#8211; Create or restore backups for devices running iOS 4 or later.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicebackup2</code> [OPTIONS] CMD [CMDOPTIONS] DIRECTORY </p>
<h2>DESCRIPTION</h2>
<p> Create or restore backup from the current or specified directory. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u, &#8211;udid UDID</code></p>
<dd> target specific device by its 40-digit device UDID.</p>
<dt><code>-s, &#8211;source UDID</code></p>
<dd> use backup data from device specified by UDID.</p>
<dt><code>-i, &#8211;interactive</code></p>
<dd> request passwords interactively on the command line.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> enable communication debugging.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> prints usage information. </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>backup</code></p>
<dd> create backup for the device.</p>
<dt><code>restore</code></p>
<dd> restore last backup to the device.</p>
<dt><code> &#8211;system</code></p>
<dd> restore system files, too.</p>
<dt><code> &#8211;reboot</code></p>
<dd> reboot the system when done.</p>
<dt><code> &#8211;copy</code></p>
<dd> create a copy of backup folder before restoring.</p>
<dt><code> &#8211;settings</code></p>
<dd> restore device settings from the backup.</p>
<dt><code> &#8211;remove</code></p>
<dd> remove items which are not being restored.</p>
<dt><code> &#8211;password PWD</code></p>
<dd> supply the password of the source backup.</p>
<dt><code>info</code></p>
<dd> show details about last completed backup of device.</p>
<dt><code>list</code></p>
<dd> list files of last completed backup in CSV format.</p>
<dt><code>encryption on|off [PWD]</code></p>
<dd> enable or disable backup encryption.</p>
<dt><code>changepw [OLD NEW]</code></p>
<dd> change backup password on target device.</dl>
<h2>AUTHORS</h2>
<p> Martin Szulecki </p>
<p> Nikias Bassen </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-idevicebackup/">idevicebackup</a>(1) </p>
<h2>Index</h2>
