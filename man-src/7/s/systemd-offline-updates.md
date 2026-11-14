---
title: "systemd-offline-updates(7)"
name: "systemd-offline-updates"
section: "7"
letter: "s"
url: "/docs/linux/man/7-systemd-offline-updates/"
description: "systemd.offline-updates – Implementation of offline updates in systemd"
---

<p>systemd.offline-updates &#8211; Implementation of offline updates in systemd</p>
<h2>Implementing Offline System Updates</h2>
<p>This man page describes how to implement &quot;offline&quot; system updates with systemd. By &quot;offline&quot; OS updates we mean package installations and updates that are run with the system booted into a special system update mode, in order to avoid problems related to conflicts of libraries and services that are currently running with those on disk. This document is inspired by this m[blue]<code>GNOME design whiteboard</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> The logic: </p>
<dl>
<dd>1. The package manager prepares system updates by downloading all (.rpm or .deb or whatever) packages to update off-line in a special directory /var/lib/system-update (or another directory of the package/upgrade manager&#8217;s choice).</dl>
<dl>
<dd>2. When the user OK&#8217;ed the update, the symlink /system-update is created that points to /var/lib/system-update (or wherever the directory with the upgrade files is located) and the system is rebooted. This symlink is in the root directory, since we need to check for it very early at boot, at a time where /var/ is not available yet.</dl>
<dl>
<dd>3. Very early in the new boot <code><a href="/docs/linux/man/8-systemd-system-update-generator/">systemd-system-update-generator</a></code>(8) checks whether /system-update exists. If so, it (temporarily and for this boot only) redirects (i.e. symlinks) default.target to system-update.target, a special target that pulls in the base system (i.e. sysinit.target, so that all file systems are mounted but little else) and the system update units.</dl>
<dl>
<dd>4. The system now continues to boot into default.target, and thus into system-update.target. This target pulls in all system update units. Only one service should perform an update (see the next point), and all the other ones should exit cleanly with a &quot;success&quot; return code and without doing anything. Update services should be ordered after sysinit.target so that the update starts after all file systems have been mounted.</dl>
<dl>
<dd>5. As the first step, an update service should check if the /system-update symlink points to the location used by that update service. In case it does not exist or points to a different location, the service must exit without error. It is possible for multiple update services to be installed, and for multiple update services to be launched in parallel, and only the one that corresponds to the tool that <i>created</i> the symlink before reboot should perform any actions. It is unsafe to run multiple updates in parallel.</dl>
<dl>
<dd>6. The update service should now do its job. If applicable and possible, it should create a file system snapshot, then install all packages. After completion (regardless whether the update succeeded or failed) the machine must be rebooted, for example by calling <code>systemctl reboot</code>. In addition, on failure the script should revert to the old file system snapshot (without the symlink).</dl>
<dl>
<dd>7. The update scripts should exit only after the update is finished. It is expected that the service which performs the update will cause the machine to reboot after it is done. If the system-update.target is successfully reached, i.e. all update services have run, and the /system-update symlink still exists, it will be removed and the machine rebooted as a safety measure.</dl>
<dl>
<dd>8. After a reboot, now that the /system-update symlink is gone, the generator won&#8217;t redirect default.target anymore and the system now boots into the default target again.</dl>
<h2>Recommendations</h2>
<dl>
<dd>1. To make things a bit more robust we recommend hooking the update script into system-update.target via a .wants/ symlink in the distribution package, rather than depending on <code>systemctl enable</code> in the postinst scriptlets of your package. More specifically, for your update script create a .service file, without [Install] section, and then add a symlink like /lib/systemd/system/system-update.target.wants/foobar.service → ../foobar.service to your package.</dl>
<dl>
<dd>2. Make sure to remove the /system-update symlink as early as possible in the update script to avoid reboot loops in case the update fails.</dl>
<dl>
<dd>3. Use <i>FailureAction=reboot</i> in the service file for your update script to ensure that a reboot is automatically triggered if the update fails. <i>FailureAction=</i> makes sure that the specified unit is activated if your script exits uncleanly (by non-zero error code, or signal/coredump). If your script succeeds you should trigger the reboot in your own code, for example by invoking logind&#8217;s <code>Reboot()</code> call or calling <code>systemctl reboot</code>. See <code><a href="/docs/linux/man/5-org-freedesktop-login1/">org.freedesktop.login1</a></code>(5) for details about the logind D-Bus API.</dl>
<dl>
<dd>4. The update service should declare <i>DefaultDependencies=no</i>, <i>Requires=sysinit.target</i>, <i>After=sysinit.target</i>, <i>After=system-update-pre.target</i>, <i>Before=system-update.target</i> and explicitly pull in any other services it requires.</dl>
<dl>
<dd>5. It may be desirable to always run an auxiliary unit when booting into offline-updates mode, which itself does not install updates. To do this create a .service file with <i>Wants=system-update-pre.target</i> and <i>Before=system-update-pre.target</i> and add a symlink to that file under /lib/systemd/system-update.target.wants .</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7), <code><a href="/docs/linux/man/8-systemd-system-update-generator/">systemd-system-update-generator</a></code>(8), <code><a href="/docs/linux/man/8-dnf-plugin-system-upgrade/">dnf.plugin.system-upgrade</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>GNOME design whiteboard</p>
<dl>
<dd><a rel="nofollow" href="https://wiki.gnome.org/Design/OS/SoftwareUpdates">https://wiki.gnome.org/Design/OS/SoftwareUpdates</a></dl>
