---
title: "loader-conf(5)"
name: "loader-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-loader-conf/"
description: "loader.conf – Configuration file for systemd-boot"
---

<p>loader.conf &#8211; Configuration file for systemd-boot</p>
<h2>Synopsis</h2>
<p><i>ESP</i>/loader/loader.conf, <i>ESP</i>/loader/entries/*.conf</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7) will read <i>ESP</i>/loader/loader.conf and any files with the &quot;.conf&quot; extension under <i>ESP</i>/loader/entries/ on the EFI system partition (ESP). </p>
<p> Each configuration file must consist of an option name, followed by whitespace, and the option value. &quot;#&quot; may be used to start a comment line. Empty and comment lines are ignored. </p>
<p> Boolean arguments may be written as &quot;yes&quot;/&quot;y&quot;/&quot;true&quot;/&quot;1&quot; or &quot;no&quot;/&quot;n&quot;/&quot;false&quot;/&quot;0&quot;.</p>
<h2>Options</h2>
<p>The following configuration options in loader.conf are understood: </p>
<p> default</p>
<dl>
<dd>A glob pattern to select the default entry. The default entry may be changed in the boot menu itself, in which case the name of the selected entry will be stored as an EFI variable, overriding this option.</dl>
<p> timeout</p>
<dl>
<dd>How long the boot menu should be shown before the default entry is booted, in seconds. This may be changed in the boot menu itself and will be stored as an EFI variable in that case, overriding this option. </p>
<p> If the timeout is disabled, the default entry will be booted immediately. The menu can be shown by pressing and holding a key before systemd-boot is launched.</dl>
<p> console-mode</p>
<dl>
<dd>This option configures the resolution of the console. Takes a number or one of the special values listed below. The following values may be used: </p>
<p> 0</p>
<dl>
<dd>Standard UEFI 80&#215;25 mode</dl>
<p> 1</p>
<dl>
<dd>80&#215;50 mode, not supported by all devices</dl>
<p> 2</p>
<dl>
<dd>the first non-standard mode provided by the device firmware, if any</dl>
<p> auto</p>
<dl>
<dd>Pick a suitable mode automatically using heuristics</dl>
<p> max</p>
<dl>
<dd>Pick the highest-numbered available mode</dl>
<p> keep</p>
<dl>
<dd>Keep the mode selected by firmware (the default)</dl>
</dl>
<p> editor</p>
<dl>
<dd>Takes a boolean argument. Enable (the default) or disable the editor. The editor should be disabled if the machine can be accessed by unauthorized persons.</dl>
<p> auto-entries</p>
<dl>
<dd>Takes a boolean argument. Enable (the default) or disable entries for other boot entries found on the boot partition. In particular, this may be useful when loader entries are created to show replacement descriptions for those entries.</dl>
<p> auto-firmware</p>
<dl>
<dd>Takes a boolean argument. Enable (the default) or disable the &quot;Reboot into firmware&quot; entry.</dl>
<p> random-seed-mode</p>
<dl>
<dd>Takes one of &quot;off&quot;, &quot;with-system-token&quot; and &quot;always&quot;. If &quot;off&quot; no random seed data is read off the ESP, nor passed to the OS. If &quot;with-system-token&quot; (the default) <code>systemd-boot</code> will read a random seed from the ESP (from the file /loader/random-seed) only if the <i>LoaderSystemToken</i> EFI variable is set, and then derive the random seed to pass to the OS from the combination. If &quot;always&quot; the boot loader will do so even if <i>LoaderSystemToken</i> is not set. This mode is useful in environments where protection against OS image reuse is not a concern, and the random seed shall be used even with no further setup in place. Use <code>bootctl random-seed</code> to initialize both the random seed file in the ESP and the system token EFI variable. </p>
<p> See m[blue]<code>Random Seeds</code>m[]<font SIZE="-2">[1]</font> for further information.</dl>
<h2>Example</h2>
<dl>
<dd>
<pre># /boot/efi/loader/loader.conf
timeout 0
default 01234567890abcdef1234567890abdf0-*
editor no</pre>
</dl>
<p> The menu will not be shown by default (the menu can still be shown by pressing and holding a key during boot). One of the entries with files with a name starting with &quot;01234567890abcdef1234567890abdf0-&quot; will be selected by default. If more than one entry matches, the one with the highest priority will be selected (generally the one with the highest version number). The editor will be disabled, so it is not possible to alter the kernel command line.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7), <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Random Seeds</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/RANDOM_SEEDS">https://systemd.io/RANDOM_SEEDS</a></dl>
