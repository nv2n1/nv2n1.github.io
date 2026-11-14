---
title: "systemd-firstboot(1)"
name: "systemd-firstboot"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-firstboot/"
description: "systemd-firstboot, systemd-firstboot.service – Initialize basic system settings on or before the first boot-up of a system"
---

<h2 class="name">NAME</h2>
<p> systemd-firstboot, systemd-firstboot.service &#8211; Initialize basic system settings on or before the first boot-up of a system </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-firstboot</code> [OPTIONS&#8230;]</dl>
<dd>systemd-firstboot.service</p>
<h2>DESCRIPTION</h2>
<p> <code>systemd-firstboot</code> initializes the most basic system settings interactively on the first boot, or optionally non-interactively when a system image is created. The following settings may be set up: </p>
<dl>
<dt>
<dd> &bull; The system locale, more specifically the two locale variables <i>LANG=</i> and <i>LC_MESSAGES</i></dl>
<dl>
<dt>
<dd> &bull; The system time zone</dl>
<dl>
<dt>
<dd> &bull; The system host name</dl>
<dl>
<dt>
<dd> &bull; The machine ID of the system</dl>
<dl>
<dt>
<dd> &bull; The root user&#8217;s password</dl>
<p> Each of the fields may either be queried interactively from the users, set non-interactively on the tool&#8217;s command line, or be copied from a host system that is used to set up the system image. </p>
<p> If a setting is already initialized it will not be overwritten and the user will not be prompted for the setting. </p>
<p> Note that this tool operates directly on the file system and does not involve any running system services, unlike <code><a href="/docs/linux/man/1-localectl/">localectl</a></code>(1), <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1) or <code><a href="/docs/linux/man/1-hostnamectl/">hostnamectl</a></code>(1). This allows <code>systemd-firstboot</code> to operate on mounted but not booted disk images and in early boot. It is not recommended to use <code>systemd-firstboot</code> on the running system while it is up.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;root=</code><i>root</i></p>
<dl>
<dt>
<dd> Takes a directory path as an argument. All paths will be prefixed with the given alternate <i>root</i> path, including config search paths. This is useful to operate on a system image mounted to the specified directory instead of the host system itself.</dl>
<p> <code>&#8211;locale=</code><i>LOCALE</i>, <code>&#8211;locale-messages=</code><i>LOCALE</i></p>
<dl>
<dt>
<dd> Sets the system locale, more specifically the <i>LANG=</i> and <i>LC_MESSAGES</i> settings. The argument should be a valid locale identifier, such as &quot;de_DE.UTF-8&quot;. This controls the <code><a href="/docs/linux/man/5-locale-conf/">locale.conf</a></code>(5) configuration file.</dl>
<p> <code>&#8211;timezone=</code><i>TIMEZONE</i></p>
<dl>
<dt>
<dd> Sets the system time zone. The argument should be a valid time zone identifier, such as &quot;Europe/Berlin&quot;. This controls the <code><a href="/docs/linux/man/5-localtime/">localtime</a></code>(5) symlink.</dl>
<p> <code>&#8211;hostname=</code><i>HOSTNAME</i></p>
<dl>
<dt>
<dd> Sets the system hostname. The argument should be a host name, compatible with DNS. This controls the <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5) configuration file.</dl>
<p> <code>&#8211;machine-id=</code><i>ID</i></p>
<dl>
<dt>
<dd> Sets the system&#8217;s machine ID. This controls the <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) file.</dl>
<p> <code>&#8211;root-password=</code><i>PASSWORD</i>, <code>&#8211;root-password-file=</code><i>PATH</i></p>
<dl>
<dt>
<dd> Sets the password of the system&#8217;s root user. This creates a <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5) file. This setting exists in two forms: <code>&#8211;root-password=</code> accepts the password to set directly on the command line, <code>&#8211;root-password-file=</code> reads it from a file. Note that it is not recommended specifying passwords on the command line as other users might be able to see them simply by invoking <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1).</dl>
<p> <code>&#8211;prompt-locale</code>, <code>&#8211;prompt-timezone</code>, <code>&#8211;prompt-hostname</code>, <code>&#8211;prompt-root-password</code></p>
<dl>
<dt>
<dd> Prompt the user interactively for a specific basic setting. Note that any explicit configuration settings specified on the command line take precedence, and the user is not prompted for it.</dl>
<p> <code>&#8211;prompt</code></p>
<dl>
<dt>
<dd> Query the user for locale, timezone, hostname and root password. This is equivalent to specifying <code>&#8211;prompt-locale</code>, <code>&#8211;prompt-timezone</code>, <code>&#8211;prompt-hostname</code>, <code>&#8211;prompt-root-password</code> in combination.</dl>
<p> <code>&#8211;copy-locale</code>, <code>&#8211;copy-timezone</code>, <code>&#8211;copy-root-password</code></p>
<dl>
<dt>
<dd> Copy a specific basic setting from the host. This only works in combination with <code>&#8211;root=</code> (see above).</dl>
<p> <code>&#8211;copy</code></p>
<dl>
<dt>
<dd> Copy locale, time zone and root password from the host. This is equivalent to specifying <code>&#8211;copy-locale</code>, <code>&#8211;copy-timezone</code>, <code>&#8211;copy-root-password</code> in combination.</dl>
<p> <code>&#8211;setup-machine-id</code></p>
<dl>
<dt>
<dd> Initialize the system&#8217;s machine ID to a random ID. This only works in combination with <code>&#8211;root=</code>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-locale-conf/">locale.conf</a></code>(5), <code><a href="/docs/linux/man/5-localtime/">localtime</a></code>(5), <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/1-systemd-machine-id-setup/">systemd-machine-id-setup</a></code>(1), <code><a href="/docs/linux/man/1-localectl/">localectl</a></code>(1), <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1), <code><a href="/docs/linux/man/1-hostnamectl/">hostnamectl</a></code>(1) </p>
<h2>Index</h2>
