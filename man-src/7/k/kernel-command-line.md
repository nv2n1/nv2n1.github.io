---
title: "kernel-command-line(7)"
name: "kernel-command-line"
section: "7"
letter: "k"
url: "/docs/linux/man/7-kernel-command-line/"
description: "kernel-command-line – Kernel command line parameters"
---

<p>kernel-command-line &#8211; Kernel command line parameters</p>
<h2>Synopsis</h2>
<p>/proc/cmdline</p>
<h2>Description</h2>
<p>The kernel, the initial RAM disk (initrd) and basic userspace functionality may be configured at boot via kernel command line arguments. In addition, various systemd tools look at the EFI variable &quot;SystemdOptions&quot; (if available). Both sources are combined, but the kernel command line has higher priority. Please note that <i>the EFI variable is only used by systemd tools, and is ignored by the kernel and other user space tools</i>, so it is not a replacement for the kernel command line. </p>
<p> For command line parameters understood by the kernel, please see m[blue]<code>kernel-parameters.html</code>m[]<font SIZE="-2">[1]</font> and <code><a href="/docs/linux/man/7-bootparam/">bootparam</a></code>(7). </p>
<p> For command line parameters understood by the initial RAM disk, please see <code><a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a></code>(7), or the documentation of the specific initrd implementation of your installation.</p>
<h2>Core Os Command Line Arguments</h2>
<p><i>systemd.unit=</i>, <i>rd.systemd.unit=</i>, <i>systemd.dump_core</i>, <i>systemd.early_core_pattern=</i>, <i>systemd.crash_chvt</i>, <i>systemd.crash_shell</i>, <i>systemd.crash_reboot</i>, <i>systemd.confirm_spawn</i>, <i>systemd.service_watchdogs</i>, <i>systemd.show_status</i>, <i>systemd.status_unit_format=</i>, <i>systemd.log_target=</i>, <i>systemd.log_level=</i>, <i>systemd.log_location=</i>, <i>systemd.log_color</i>, <i>systemd.default_standard_output=</i>, <i>systemd.default_standard_error=</i>, <i>systemd.setenv=</i>, <i>systemd.machine_id=</i>, <i>systemd.unified_cgroup_hierarchy</i>, <i>systemd.legacy_systemd_cgroup_controller</i></p>
<dl>
<dd>Parameters understood by the system and service manager to control system behavior. For details, see <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1).</dl>
<p> <i>systemd.mask=</i>, <i>systemd.wants=</i>, <i>systemd.debug_shell</i></p>
<dl>
<dd>Additional parameters understood by <code><a href="/docs/linux/man/8-systemd-debug-generator/">systemd-debug-generator</a></code>(8), to mask or start specific units at boot, or invoke a debug shell on tty9.</dl>
<p> <i>systemd.run=</i>, <i>systemd.run_success_action=</i>, <i>systemd.run_failure_action=</i></p>
<dl>
<dd>Additional parameters understood by <code><a href="/docs/linux/man/8-systemd-run-generator/">systemd-run-generator</a></code>(8), to run a command line specified on the kernel command line as system service after booting up.</dl>
<p> <i>systemd.early_core_pattern=</i></p>
<dl>
<dd>During early boot, the generation of core dump files is disabled until a core dump handler (if any) takes over. This parameter allows specifying an absolute path where core dump files should be stored until a handler is installed. The path should be absolute and may contain specifiers, see <code><a href="/docs/linux/man/5-core/">core</a></code>(5) for details.</dl>
<p> <i>systemd.restore_state=</i></p>
<dl>
<dd>This parameter is understood by several system tools to control whether or not they should restore system state from the previous boot. For details, see <code>systemd-backlight [at] .service</code>(8) and <code><a href="/docs/linux/man/8-systemd-rfkill-service/">systemd-rfkill.service</a></code>(8).</dl>
<p> <i>systemd.volatile=</i></p>
<dl>
<dd>This parameter controls whether the system shall boot up in volatile mode. Takes a boolean argument, or the special value &quot;state&quot;. If false (the default), normal boot mode is selected, the root directory and /var/ are mounted as specified on the kernel command line or /etc/fstab, or otherwise configured. If true, full state-less boot mode is selected. In this case the root directory is mounted as volatile memory file system (&quot;tmpfs&quot;), and only /usr/ is mounted from the file system configured as root device, in read-only mode. This enables fully state-less boots were the vendor-supplied OS is used as shipped, with only default configuration and no stored state in effect, as /etc/ and /var/ (as well as all other resources shipped in the root file system) are reset at boot and lost on shutdown. If this setting is set to &quot;state&quot; the root file system is mounted read-only, however /var/ is mounted as a volatile memory file system (&quot;tmpfs&quot;), so that the system boots up with the normal configuration applied, but all state reset at boot and lost at shutdown. If this setting is set to &quot;overlay&quot; the root file system is set up as &quot;overlayfs&quot; mount combining the read-only root directory with a writable &quot;tmpfs&quot;, so that no modifications are made to disk, but the file system may be modified nonetheless with all changes being lost at reboot. For details, see <code><a href="/docs/linux/man/8-systemd-volatile-root-service/">systemd-volatile-root.service</a></code>(8) and <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8).</dl>
<p> <i>quiet</i></p>
<dl>
<dd>Parameter understood by both the kernel and the system and service manager to control console log verbosity. For details, see <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1).</dl>
<p> <i>debug</i></p>
<dl>
<dd>Parameter understood by both the kernel and the system and service manager to control console log verbosity. For details, see <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1).</dl>
<p> <i>-b</i>, <i>rd.emergency</i>, <i>emergency</i>, <i>rd.rescue</i>, <i>rescue</i>, <i>single</i>, <i>s</i>, <i>S</i>, <i>1</i>, <i>2</i>, <i>3</i>, <i>4</i>, <i>5</i></p>
<dl>
<dd>Parameters understood by the system and service manager, as compatibility and convenience options. For details, see <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1).</dl>
<p> <i>locale.LANG=</i>, <i>locale.LANGUAGE=</i>, <i>locale.LC_CTYPE=</i>, <i>locale.LC_NUMERIC=</i>, <i>locale.LC_TIME=</i>, <i>locale.LC_COLLATE=</i>, <i>locale.LC_MONETARY=</i>, <i>locale.LC_MESSAGES=</i>, <i>locale.LC_PAPER=</i>, <i>locale.LC_NAME=</i>, <i>locale.LC_ADDRESS=</i>, <i>locale.LC_TELEPHONE=</i>, <i>locale.LC_MEASUREMENT=</i>, <i>locale.LC_IDENTIFICATION=</i></p>
<dl>
<dd>Parameters understood by the system and service manager to control locale and language settings. For details, see <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1).</dl>
<p> <i>fsck.mode=</i>, <i>fsck.repair=</i></p>
<dl>
<dd>Parameters understood by the file system checker services. For details, see <code>systemd-fsck [at] .service</code>(8).</dl>
<p> <i>quotacheck.mode=</i></p>
<dl>
<dd>Parameter understood by the file quota checker service. For details, see <code><a href="/docs/linux/man/8-systemd-quotacheck-service/">systemd-quotacheck.service</a></code>(8).</dl>
<p> <i>systemd.journald.forward_to_syslog=</i>, <i>systemd.journald.forward_to_kmsg=</i>, <i>systemd.journald.forward_to_console=</i>, <i>systemd.journald.forward_to_wall=</i></p>
<dl>
<dd>Parameters understood by the journal service. For details, see <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8).</dl>
<p> <i>vconsole.keymap=</i>, <i>vconsole.keymap_toggle=</i>, <i>vconsole.font=</i>, <i>vconsole.font_map=</i>, <i>vconsole.font_unimap=</i></p>
<dl>
<dd>Parameters understood by the virtual console setup logic. For details, see <code><a href="/docs/linux/man/5-vconsole-conf/">vconsole.conf</a></code>(5).</dl>
<p> <i>udev.log_level=</i>, <i>rd.udev.log_level=</i>, <i>udev.children_max=</i>, <i>rd.udev.children_max=</i>, <i>udev.exec_delay=</i>, <i>rd.udev.exec_delay=</i>, <i>udev.event_timeout=</i>, <i>rd.udev.event_timeout=</i>, <i>udev.timeout_signal=</i>, <i>rd.udev.timeout_signal=</i>, <i>udev.blockdev_read_only</i>, <i>rd.udev.blockdev_read_only</i>, <i>net.ifnames=</i>, <i>net.naming-scheme=</i></p>
<dl>
<dd>Parameters understood by the device event managing daemon. For details, see <code><a href="/docs/linux/man/8-systemd-udevd-service/">systemd-udevd.service</a></code>(8).</dl>
<p> <i>plymouth.enable=</i></p>
<dl>
<dd>May be used to disable the Plymouth boot splash. For details, see <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8).</dl>
<p> <i>luks=</i>, <i>rd.luks=</i>, <i>luks.crypttab=</i>, <i>rd.luks.crypttab=</i>, <i>luks.name=</i>, <i>rd.luks.name=</i>, <i>luks.uuid=</i>, <i>rd.luks.uuid=</i>, <i>luks.options=</i>, <i>rd.luks.options=</i>, <i>luks.key=</i>, <i>rd.luks.key=</i></p>
<dl>
<dd>Configures the LUKS full-disk encryption logic at boot. For details, see <code><a href="/docs/linux/man/8-systemd-cryptsetup-generator/">systemd-cryptsetup-generator</a></code>(8).</dl>
<p> <i>fstab=</i>, <i>rd.fstab=</i></p>
<dl>
<dd>Configures the /etc/fstab logic at boot. For details, see <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8).</dl>
<p> <i>root=</i>, <i>rootfstype=</i>, <i>rootflags=</i>, <i>ro</i>, <i>rw</i></p>
<dl>
<dd>Configures the root file system and its file system type and mount options, as well as whether it shall be mounted read-only or read-write initially. For details, see <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8).</dl>
<p> <i>mount.usr=</i>, <i>mount.usrfstype=</i>, <i>mount.usrflags=</i></p>
<dl>
<dd>Configures the /usr file system (if required) and its file system type and mount options. For details, see <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8).</dl>
<p> <i>veritytab=</i>, <i>rd.veritytab=</i>, <i>roothash=</i>, <i>systemd.verity=</i>, <i>rd.systemd.verity=</i>, <i>systemd.verity_root_data=</i>, <i>systemd.verity_root_hash=</i>, <i>systemd.verity.root_options=</i></p>
<dl>
<dd>Configures the integrity protection root hash for the root file system, and other related parameters. For details, see <code><a href="/docs/linux/man/8-systemd-veritysetup-generator/">systemd-veritysetup-generator</a></code>(8).</dl>
<p> <i>systemd.gpt_auto=</i>, <i>rd.systemd.gpt_auto=</i></p>
<dl>
<dd>Configures whether GPT based partition auto-discovery shall be attempted. For details, see <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8).</dl>
<p> <i>systemd.default_timeout_start_sec=</i></p>
<dl>
<dd>Overwrites the default start job timeout <i>DefaultTimeoutStartSec=</i> at boot. For details, see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>systemd.watchdog_device=</i></p>
<dl>
<dd>Overwrites the watchdog device path <i>WatchdogDevice=</i>. For details, see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>systemd.cpu_affinity=</i></p>
<dl>
<dd>Overrides the CPU affinity mask for the service manager and the default for all child processes it forks. This takes precedence over <i>CPUAffinity=</i>, see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5) for details.</dl>
<p> <i>modules_load=</i>, <i>rd.modules_load=</i></p>
<dl>
<dd>Load a specific kernel module early at boot. For details, see <code><a href="/docs/linux/man/8-systemd-modules-load-service/">systemd-modules-load.service</a></code>(8).</dl>
<p> <i>resume=</i>, <i>resumeflags=</i></p>
<dl>
<dd>Enables resume from hibernation using the specified device and mount options. All <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)-like paths are supported. For details, see <code><a href="/docs/linux/man/8-systemd-hibernate-resume-generator/">systemd-hibernate-resume-generator</a></code>(8).</dl>
<p> <i>systemd.firstboot=</i></p>
<dl>
<dd>Takes a boolean argument, defaults to on. If off, <code><a href="/docs/linux/man/8-systemd-firstboot-service/">systemd-firstboot.service</a></code>(8) will not query the user for basic system settings, even if the system boots up for the first time and the relevant settings are not initialized yet. Not to be confused with <i>systemd.condition-first-boot=</i> (see below), which overrides the result of the <i>ConditionFirstBoot=</i> unit file condition, and thus controls more than just systemd-firstboot.service behaviour.</dl>
<p> <i>systemd.condition-needs-update=</i></p>
<dl>
<dd>Takes a boolean argument. If specified, overrides the result of <i>ConditionNeedsUpdate=</i> unit condition checks. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details.</dl>
<p> <i>systemd.condition-first-boot=</i></p>
<dl>
<dd>Takes a boolean argument. If specified, overrides the result of <i>ConditionFirstBoot=</i> unit condition checks. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. Not to be confused with <i>systemd.firstboot=</i> which only controls behaviour of the systemd-firstboot.service system service but has no effect on the condition check (see above).</dl>
<p> <i>systemd.clock-usec=</i></p>
<dl>
<dd>Takes a decimal, numeric timestamp in &micro;s since January 1st 1970, 00:00am, to set the system clock to. The system time is set to the specified timestamp early during boot. It is not propagated to the hardware clock (RTC).</dl>
<p> <i>systemd.random-seed=</i></p>
<dl>
<dd>Takes a base64 encoded random seed value to credit with full entropy to the kernel&#8217;s random pool during early service manager initialization. This option is useful in testing environments where delays due to random pool initialization in entropy starved virtual machines shall be avoided. </p>
<p> Note that if this option is used the seed is accessible to unprivileged programs from /proc/cmdline. This option is hence a security risk when used outside of test systems, since the (possibly) only seed used for initialization of the kernel&#8217;s entropy pool might be easily acquired by unprivileged programs. </p>
<p> It is recommended to pass 512 bytes of randomized data (as that matches the Linux kernel pool size), which may be generated with a command like the following: </p>
<dl>
<dd>
<pre>dd if=/dev/urandom bs=512 count=1 status=none | base64 -w 0</pre>
</dl>
<p> Again: do not use this option outside of testing environments, it&#8217;s a security risk elsewhere, as secret key material derived from the entropy pool can possibly be reconstructed by unprivileged programs.</dl>
<p> <i>systemd.hostname=</i></p>
<dl>
<dd>Accepts a hostname to set during early boot. If specified takes precedence over what is set in /etc/hostname. Note that this does not bar later runtime changes to the hostname, it simply controls the initial hostname set during early boot.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/7-bootparam/">bootparam</a></code>(7), <code><a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a></code>(7), <code><a href="/docs/linux/man/8-systemd-debug-generator/">systemd-debug-generator</a></code>(8), <code>systemd-fsck [at] .service</code>(8), <code><a href="/docs/linux/man/8-systemd-quotacheck-service/">systemd-quotacheck.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-vconsole-setup-service/">systemd-vconsole-setup.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-udevd-service/">systemd-udevd.service</a></code>(8), <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8), <code><a href="/docs/linux/man/8-systemd-cryptsetup-generator/">systemd-cryptsetup-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-veritysetup-generator/">systemd-veritysetup-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-volatile-root-service/">systemd-volatile-root.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-modules-load-service/">systemd-modules-load.service</a></code>(8), <code>systemd-backlight [at] .service</code>(8), <code><a href="/docs/linux/man/8-systemd-rfkill-service/">systemd-rfkill.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hibernate-resume-generator/">systemd-hibernate-resume-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-firstboot-service/">systemd-firstboot.service</a></code>(8), <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>kernel-parameters.html</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html">https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html</a></dl>
