---
title: "udiskie-umount(8)"
name: "udiskie-umount"
section: "8"
letter: "u"
url: "/docs/linux/man/8-udiskie-umount/"
description: "udiskie – automounter for removable media"
---

<p>udiskie &#8211; automounter for removable media</p>
<h2>Synopsis</h2>
<p><i>udiskie</i> [OPTIONS] </p>
<p> <i>udiskie-mount</i> [OPTIONS] (-a | DEVICE&#8230;) </p>
<p> <i>udiskie-umount</i> [OPTIONS] (-a | PATH&#8230;)</p>
<h2>Description</h2>
<p><code>udiskie</code> is a front-end for UDisks written in python. Its main purpose is automatically mounting removable media, such as CDs or flash drives. It has optional mount notifications, a GTK tray icon and user level CLIs for manual mount and unmount operations. The media will be mounted in a new directory under <i>/media</i> or <i>/run/media/USER/</i>, using the device name if possible.</p>
<h2>Common Options</h2>
<p><code>-h, &#8211;help</code></p>
<dl>
<dd>Show help message and exit.</dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dd>Show help message and exit.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>Verbose output.</dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dd>Quiet output.</dl>
<p> <code>-0, &#8211;udisks-auto</code></p>
<dl>
<dd>Auto discover UDisks version (default). Prefers UDisks2 if both are available.</dl>
<p> <code>-1, &#8211;use-udisks1</code></p>
<dl>
<dd>Use UDisks1 as DBus backend.</dl>
<p> <code>-2, &#8211;use-udisks2</code></p>
<dl>
<dd>Use UDisks2 as DBus backend.</dl>
<p> <code>-c FILE, &#8211;config=FILE</code></p>
<dl>
<dd>Specify config file.</dl>
<p> <code>-C, &#8211;no-config</code></p>
<dl>
<dd>Don&#8217;t use any config file.</dl>
<h2>Shared Mount And Daemon Options</h2>
<p><code>-p COMMAND, &#8211;password-prompt=COMMAND</code></p>
<dl>
<dd>Password retrieval command. The string is formatted with a Device object as its first argument.</dl>
<p> <code>-P, &#8211;no-password-prompt</code></p>
<dl>
<dd>Disable unlocking of LUKS devices.</dl>
<h2>Daemon Options</h2>
<p><code>-a, &#8211;automount</code></p>
<dl>
<dd>Enable automounting new devices (default).</dl>
<p> <code>-A, &#8211;no-automount</code></p>
<dl>
<dd>Disable automounting new devices.</dl>
<p> <code>-n, &#8211;notify</code></p>
<dl>
<dd>Enable pop-up notifications (default).</dl>
<p> <code>-N, &#8211;disable-notify</code></p>
<dl>
<dd>Disable pop-up notifications.</dl>
<p> <code>-t, &#8211;tray</code></p>
<dl>
<dd>Show tray icon.</dl>
<p> <code>-s, &#8211;smart-tray</code></p>
<dl>
<dd>Show tray icon that automatically hides when there is no action available.</dl>
<p> <code>-T, &#8211;no-tray</code></p>
<dl>
<dd>Disable tray icon (default).</dl>
<p> <code>-f PROGRAM, &#8211;file-manager=PROGRAM</code></p>
<dl>
<dd>Set program to open mounted directories. Default is &#8216;xdg-open&#8217;. Pass an empty string to disable this feature. This option is deprecated and will probably be replaced by a python commands file.</dl>
<p> <code>-F, &#8211;no-file-manager</code></p>
<dl>
<dd>Disable browsing.</dl>
<h2>Mount Options</h2>
<p><code>-a, &#8211;all</code></p>
<dl>
<dd>Mount all handled devices.</dl>
<p> <code>-r, &#8211;recursive</code></p>
<dl>
<dd>Recursively mount cleartext partitions after unlocking a LUKS device. This will happen by default when running the udiskie daemon.</dl>
<p> <code>-R, &#8211;no-recursive</code></p>
<dl>
<dd>Disable recursive mounting (default).</dl>
<p> <code>-o OPTIONS, &#8211;options=OPTIONS</code></p>
<dl>
<dd>Set mount options.</dl>
<h2>Unmount Options</h2>
<p><code>-a, &#8211;all</code></p>
<dl>
<dd>Unmount all handled devices.</dl>
<p> <code>-d, &#8211;detach</code></p>
<dl>
<dd>Detach drive by e.g. powering down its physical port.</dl>
<p> <code>-D, &#8211;no-detach</code></p>
<dl>
<dd>Don&#8217;t detach drive (default).</dl>
<p> <code>-e, &#8211;eject</code></p>
<dl>
<dd>Eject media from the drive, e.g CDROM.</dl>
<p> <code>-E, &#8211;no-eject</code></p>
<dl>
<dd>Don&#8217;t eject media (default).</dl>
<p> <code>-f, &#8211;force</code></p>
<dl>
<dd>Force removal (recursive unmounting).</dl>
<p> <code>-F, &#8211;no-force</code></p>
<dl>
<dd>Don&#8217;t force removal (default).</dl>
<p> <code>-l, &#8211;lock</code></p>
<dl>
<dd>Lock device after unmounting (default).</dl>
<p> <code>-L, &#8211;no-lock</code></p>
<dl>
<dd>Don&#8217;t lock device.</dl>
<h2>Example Usage</h2>
<p>Start <code>udiskie</code> in <i>~/.xinitrc</i>: </p>
<dl>
<dd>
<pre>udiskie &amp;</pre>
</dl>
<p> Unmount media and power down USB device: </p>
<dl>
<dd>
<pre>udiskie-umount --detach /media/Sticky</pre>
</dl>
<p> Mount all media: </p>
<dl>
<dd>
<pre>udiskie-mount -a</pre>
</dl>
<p> Mount <i>/dev/sdb1</i>: </p>
<dl>
<dd>
<pre>udiskie-mount /dev/sdb1</pre>
</dl>
<h2>Configuration</h2>
<p>The file <i>.config/udiskie/config.yml</i> can be used to configure defaults for command line parameters and customize further settings. The actual path may differ depending on <i>$XDG_CONFIG_HOME</i>. The file format is YAML, see <a rel="nofollow" href="http://en.wikipedia.org/wiki/YAML.">http://en.wikipedia.org/wiki/YAML.</a> If you don&#8217;t want to install PyYAML, it is possible to use an equivalent JSON file with the name <i>config.json</i> instead. </p>
<dl>
<dd>
<pre># This is an example (nonsense) configuration file for udiskie.
program_options:
 # Configure defaults for command line options
 udisks_version: 2 # [int] Specify the version of udisks
 # to be used. Set to 0 to use automatic
 # discovery.
 tray: auto # [bool] Enable the tray icon. &quot;auto&quot;
 # means auto-hide the tray icon when
 # there are no handled devices.
 automount: false # [bool] Enable automatic mounting.
 notify: true # [bool] Enable notifications.
 file_manager: xdg-open
 # [string] Set program to open directories. It will be invoked
 # with the folder path as its # command line first argument.
 password_prompt: [&quot;gnome-keyring-query&quot;, &quot;get&quot;, &quot;{.id_uuid}&quot;]
 # [string|list] Set command to retrieve passwords. If specified
 # as a list it defines the ARGV array for the program call. If
 # specified as a string, it will be expanded in a shell-like
 # manner. Each string will be formatted using str.format with a
 # Device object as the first argument. For a list of device
 # attributes, see below. The two special string values
 # &quot;builtin:gui&quot; and &quot;builtin:tty&quot; signify to use udiskie's
 # builtin password prompt.
mount_options:
 # List of mount option rules. Only the first matching entry is
 # used. Each item can match any combination of device attributes
 # (see below). Additionally, it must define an 'options' list. An
 # item without any device attributes serves as a catch-all rule.
- id_type: vfat # match file system type
 options: ro # list of mount options
- id_uuid: 9d53-13ba # match by device UUID
 options: [noexec, nodev] # mount options can be given as list
ignore_device:
 # Customize udiskie's ignore rules. This config entry has the
 # same structure as *mount_options*, the only difference being
 # that the action is defined by the 'ignore' field which is a
 # boolean defaulting to true. The rules defined here are simply
 # prepended to the builtin ignore rules, so that it is possible
 # to completely overwrite the defaults by specifying a catch-all
 # rule.
- id_uuid: abcd-ef01 # ignore this device
- device_file: /dev/dm-5
 ignore: false # never ignore this device
notifications:
 # Customize which notifications are shown for how long. Possible
 # values are:
 # positive number timeout in seconds
 # false disable
 # -1 use the libnotify default timeout
 timeout: 1.5 # set the default for all notifications
 # Specify only if you want to overwrite the the default:
 device_mounted: 5 # mount notification
 device_unmounted: false # unmount notification
 device_added: false # device has appeared
 device_removed: false # device has disappeared
 device_unlocked: -1 # encrypted device was unlocked
 device_locked: -1 # encrypted device was locked
 job_failed: -1 # mount/unlock/.. has failed
notification_actions:
 # Define which actions should be shown on notifications. Note that there
 # are currently only a limited set of actions available for each
 # notification. Events that are not explicitly specified show the default
 # set of actions. Specify an empty list if you don't want to see any
 # notification for the specified event:
 device_mounted: [browse]
 device_added: [mount]
icon_names:
 # Customize the icon set used by the tray widget. Each entry
 # specifies a list of icon names. The first installed icon from
 # that list will be used.
 media: [drive-removable-media, media-optical]
 browse: [document-open, folder-open]
 mount: [udiskie-mount]
 unmount: [udiskie-unmount]
 unlock: [udiskie-unlock]
 lock: [udiskie-lock]
 eject: [udiskie-eject, media-eject]
 detach: [udiskie-detach]
 quit: [application-exit]</pre>
</dl>
<p> All keys are optional. Reasonable defaults are used if you leave them unspecified.</p>
<h2>Device Attributes</h2>
<p>Some of the config entries make use of Device attributes. The following list of attributes is currently availabe, but there is no guarantee that they will remain available: </p>
<dl>
<dd>
<pre>Attribute Hint/Example</pre>
</dl>
<dl>
<dd>
<pre>is_drive
is_block
is_partition_table
is_partition
is_filesystem
is_luks
is_toplevel
is_detachable
is_ejectable
has_media
device_file block device path, e.g. &quot;/dev/sdb1&quot;
device_presentation display string, e.g. &quot;/dev/sdb1&quot;
device_id unique, persistent device identifer
id_usage E.g. &quot;filesystem&quot; or &quot;crypto&quot;
is_crypto
is_ignored
id_type E.g. &quot;ext4&quot; or &quot;crypto_LUKS&quot;
id_label device label
id_uuid device UUID
is_luks_cleartext
is_external udisks flag HintSystem=false
is_systeminternal udisks flag HintSystem=true
is_mounted
mount_paths list of mount paths
is_unlocked
in_use device or any of its children mounted</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-udisks/">udisks</a></code>(1) </p>
<p> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/udisks/">http://www.freedesktop.org/wiki/Software/udisks/</a></p>
<h2>Contact</h2>
<p>You can use the github issues to report any issues you encounter, ask general questions or suggest new features. There is also a public mailing list on sourceforge if you prefer email: </p>
<p> <a rel="nofollow" href="https://github.com/coldfix/udiskie/issues">https://github.com/coldfix/udiskie/issues</a> </p>
<p> <a rel="nofollow" href="http://lists.coldfix.de/mailman/listinfo/udiskie">http://lists.coldfix.de/mailman/listinfo/udiskie</a></p>
