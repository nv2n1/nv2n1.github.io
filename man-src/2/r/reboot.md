---
title: "reboot(2)"
name: "reboot"
section: "2"
letter: "r"
url: "/docs/linux/man/2-reboot/"
description: "reboot – reboot or enable/disable Ctrl-Alt-Del"
---

<h2 class="name">NAME</h2>
<p> reboot &#8211; reboot or enable/disable Ctrl-Alt-Del </p>
<h2>SYNOPSIS</h2>
<p> /* Since kernel version 2.1.30 there are symbolic names LINUX_REBOOT_*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;for the constants and a fourth argument to the call:&nbsp;*/ </p>
<p> <code>#include &lt;unistd.h&gt;</code><br />
 <code>#include &lt;linux/reboot.h&gt;</code> </p>
<p> <code>int reboot(int </code><i>magic</i><code>, int </code><i>magic2</i><code>, int </code><i>cmd</i><code>, void *</code><i>arg</i><code>);</code> </p>
<p> /* Under glibc and most alternative libc&#8217;s (including uclibc, dietlibc,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;musl and a few others), some of the constants involved have gotten<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;symbolic names RB_*, and the library call is a 1-argument<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;wrapper around the system call:&nbsp;*/ </p>
<p> <code>#include &lt;unistd.h&gt;</code><br />
 <code>#include &lt;sys/reboot.h&gt;</code> </p>
<p> <code>int reboot(int </code><i>cmd</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>reboot</code>() call reboots the system, or enables/disables the reboot keystroke (abbreviated CAD, since the default is Ctrl-Alt-Delete; it can be changed using <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1)). </p>
<p> This system call fails (with the error <code>EINVAL</code>) unless <i>magic</i> equals <code>LINUX_REBOOT_MAGIC1</code> (that is, 0xfee1dead) and <i>magic2</i> equals <code>LINUX_REBOOT_MAGIC2</code> (that is, 672274793). However, since 2.1.17 also <code>LINUX_REBOOT_MAGIC2A</code> (that is, 85072278) and since 2.1.97 also <code>LINUX_REBOOT_MAGIC2B</code> (that is, 369367448) and since 2.5.71 also <code>LINUX_REBOOT_MAGIC2C</code> (that is, 537993216) are permitted as values for <i>magic2</i>. (The hexadecimal values of these constants are meaningful.) </p>
<p> The <i>cmd</i> argument can have the following values:</p>
<dl>
<dt><code>LINUX_REBOOT_CMD_CAD_OFF</code></p>
<dd> (<code>RB_DISABLE_CAD</code>, 0). CAD is disabled. This means that the CAD keystroke will cause a <code>SIGINT</code> signal to be sent to init (process 1), whereupon this process may decide upon a proper action (maybe: kill all processes, sync, reboot).</p>
<dt><code>LINUX_REBOOT_CMD_CAD_ON</code></p>
<dd> (<code>RB_ENABLE_CAD</code>, 0x89abcdef). CAD is enabled. This means that the CAD keystroke will immediately cause the action associated with <code>LINUX_REBOOT_CMD_RESTART</code>.</p>
<dt><code>LINUX_REBOOT_CMD_HALT</code></p>
<dd> (<code>RB_HALT_SYSTEM</code>, 0xcdef0123; since Linux 1.1.76). The message &quot;System halted.&quot; is printed, and the system is halted. Control is given to the ROM monitor, if there is one. If not preceded by a <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), data will be lost.</p>
<dt><code>LINUX_REBOOT_CMD_KEXEC</code></p>
<dd> (<code>RB_KEXEC</code>, 0x45584543, since Linux 2.6.13). Execute a kernel that has been loaded earlier with <code><a href="/docs/linux/man/2-kexec_load/">kexec_load</a></code>(2). This option is available only if the kernel was configured with <code>CONFIG_KEXEC</code>.</p>
<dt><code>LINUX_REBOOT_CMD_POWER_OFF</code></p>
<dd> (<code>RB_POWER_OFF</code>, 0x4321fedc; since Linux 2.1.30). The message &quot;Power down.&quot; is printed, the system is stopped, and all power is removed from the system, if possible. If not preceded by a <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), data will be lost.</p>
<dt><code>LINUX_REBOOT_CMD_RESTART</code></p>
<dd> (<code>RB_AUTOBOOT</code>, 0x1234567). The message &quot;Restarting system.&quot; is printed, and a default restart is performed immediately. If not preceded by a <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), data will be lost.</p>
<dt><code>LINUX_REBOOT_CMD_RESTART2</code></p>
<dd> (0xa1b2c3d4; since Linux 2.1.30). The message &quot;Restarting system with command &#8216;%s&#8217;&quot; is printed, and a restart (using the command string given in <i>arg</i>) is performed immediately. If not preceded by a <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), data will be lost.</p>
<dt><code>LINUX_REBOOT_CMD_SW_SUSPEND</code></p>
<dd> (<code>RB_SW_SUSPEND</code>, 0xd000fce1; since Linux 2.5.18). The system is suspended (hibernated) to disk. This option is available only if the kernel was configured with <code>CONFIG_HIBERNATION</code>.</dl>
<p> Only the superuser may call <code>reboot</code>(). </p>
<p> The precise effect of the above actions depends on the architecture. For the i386 architecture, the additional argument does not do anything at present (2.1.122), but the type of reboot can be determined by kernel command-line arguments (&quot;reboot=&#8230;&quot;) to be either warm or cold, and either hard or through the BIOS.</p>
<h3>Behavior inside PID namespaces</h3>
<p> Since Linux 3.4, if <code>reboot</code>() is called from a PID namespace other than the initial PID namespace with one of the <i>cmd</i> values listed below, it performs a &quot;reboot&quot; of that namespace: the &quot;init&quot; process of the PID namespace is immediately terminated, with the effects described in <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7). </p>
<p> The values that can be supplied in <i>cmd</i> when calling <code>reboot</code>() in this case are as follows:</p>
<dl>
<dt><code>LINUX_REBOOT_CMD_RESTART</code>, <code>LINUX_REBOOT_CMD_RESTART2</code></p>
<dd> The &quot;init&quot; process is terminated, and <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) in the parent process reports that the child was killed with a <code>SIGHUP</code> signal.</p>
<dt><code>LINUX_REBOOT_CMD_POWER_OFF</code>, <code>LINUX_REBOOT_CMD_HALT</code></p>
<dd> The &quot;init&quot; process is terminated, and <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) in the parent process reports that the child was killed with a <code>SIGINT</code> signal.</dl>
<p> For the other <i>cmd</i> values, <code>reboot</code>() returns -1 and <i>errno</i> is set to <code>EINVAL</code>.</p>
<h2>RETURN VALUE</h2>
<p> For the values of <i>cmd</i> that stop or restart the system, a successful call to <code>reboot</code>() does not return. For the other <i>cmd</i> values, zero is returned on success. In all cases, -1 is returned on failure, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Problem with getting user-space data under <code>LINUX_REBOOT_CMD_RESTART2</code>.</p>
<dt><code>EINVAL</code></p>
<dd> Bad magic numbers or <i>cmd</i>.</p>
<dt><code>EPERM</code></p>
<dd> The calling process has insufficient privilege to call <code>reboot</code>(); the caller must have the <code>CAP_SYS_BOOT</code> inside its user namespace.</dl>
<h2>CONFORMING TO</h2>
<p> <code>reboot</code>() is Linux-specific, and should not be used in programs intended to be portable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/2-kexec_load/">kexec_load</a></code>(2), <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), <code><a href="/docs/linux/man/7-bootparam/">bootparam</a></code>(7), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/8-ctrlaltdel/">ctrlaltdel</a></code>(8), <code><a href="/docs/linux/man/8-halt/">halt</a></code>(8), <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
