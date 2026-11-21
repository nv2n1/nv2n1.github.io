---

title: "idevicebackup2(1)"
name: "idevicebackup2"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicebackup2/"
description: "idevicebackup2 – Create or restore backups for devices running iOS 4 or later."
---

<p> idevicebackup2 &#8211; Create or restore backups for devices running iOS 4 or later.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicebackup2</code> [OPTIONS] CMD [CMDOPTIONS] DIRECTORY </p>
<h2>DESCRIPTION</h2>
<p> Create or restore backup from the current or specified directory. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u, &#8211;udid UDID</code></dt>
<dd> target specific device by its 40-digit device UDID.</dd>
<dt><code>-s, &#8211;source UDID</code></dt>
<dd> use backup data from device specified by UDID.</dd>
<dt><code>-i, &#8211;interactive</code></dt>
<dd> request passwords interactively on the command line.</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information. </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>backup</code></dt>
<dd> create backup for the device.</dd>
<dt><code>restore</code></dt>
<dd> restore last backup to the device.</dd>
<dt><code> &#8211;system</code></dt>
<dd> restore system files, too.</dd>
<dt><code> &#8211;reboot</code></dt>
<dd> reboot the system when done.</dd>
<dt><code> &#8211;copy</code></dt>
<dd> create a copy of backup folder before restoring.</dd>
<dt><code> &#8211;settings</code></dt>
<dd> restore device settings from the backup.</dd>
<dt><code> &#8211;remove</code></dt>
<dd> remove items which are not being restored.</dd>
<dt><code> &#8211;password PWD</code></dt>
<dd> supply the password of the source backup.</dd>
<dt><code>info</code></dt>
<dd> show details about last completed backup of device.</dd>
<dt><code>list</code></dt>
<dd> list files of last completed backup in CSV format.</dd>
<dt><code>encryption on|off [PWD]</code></dt>
<dd> enable or disable backup encryption.</dd>
<dt><code>changepw [OLD NEW]</code></dt>
<dd> change backup password on target device.</dd></dl>
<h2>AUTHORS</h2>
<p> Martin Szulecki </p>
<p> Nikias Bassen </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-idevicebackup/">idevicebackup</a>(1) </p>
