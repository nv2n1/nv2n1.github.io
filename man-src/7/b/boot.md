---
title: "boot(7)"
name: "boot"
section: "7"
letter: "b"
url: "/docs/linux/man/7-boot/"
description: "boot – System bootup process based on UNIX System V Release 4"
---

<p>boot &#8211; System bootup process based on UNIX System V Release 4</p>
<h2>Description</h2>
<p>The <code>bootup process</code> (or &quot;<code>boot sequence</code>&quot;) varies in details among systems, but can be roughly divided into phases controlled by the following components:</p>
<dl>
<dt>1.</p>
<dd>hardware</p>
<dt>2.</p>
<dd>operating system (OS) loader</p>
<dt>3.</p>
<dd>kernel</p>
<dt>4.</p>
<dd>root user-space process (<i>init</i> and <i>inittab</i>)</p>
<dt>5.</p>
<dd>boot scripts</dl>
<p> Each of these is described below in more detail.</p>
<h3>Hardware</h3>
<p>After power-on or hard reset, control is given to a program stored in read-only memory (normally PROM); for historical reasons involving the personal computer, this program is often called &quot;the <code>BIOS</code>&quot;. </p>
<p> This program normally performs a basic self-test of the machine and accesses nonvolatile memory to read further parameters. This memory in the PC is battery-backed CMOS memory, so most people refer to it as &quot;the <code>CMOS</code>&quot;; outside of the PC world, it is usually called &quot;the <code>NVRAM</code>&quot; (nonvolatile RAM). </p>
<p> The parameters stored in the NVRAM vary among systems, but as a minimum, they should specify which device can supply an OS loader, or at least which devices may be probed for one; such a device is known as &quot;the <code>boot device</code>&quot;. The hardware boot stage loads the OS loader from a fixed position on the boot device, and then transfers control to it.</p>
<dl>
<dt>Note:</p>
<dd>The device from which the OS loader is read may be attached via a network, in which case the details of booting are further specified by protocols such as DHCP, TFTP, PXE, Etherboot, etc.</dl>
<h3>OS loader</h3>
<p>The main job of the OS loader is to locate the kernel on some device, load it, and run it. Most OS loaders allow interactive use, in order to enable specification of an alternative kernel (maybe a backup in case the one last compiled isn&#8217;t functioning) and to pass optional parameters to the kernel. </p>
<p> In a traditional PC, the OS loader is located in the initial 512-byte block of the boot device; this block is known as &quot;the <code>MBR</code>&quot; (Master Boot Record). </p>
<p> In most systems, the OS loader is very limited due to various constraints. Even on non-PC systems, there are some limitations on the size and complexity of this loader, but the size limitation of the PC MBR (512 bytes, including the partition table) makes it almost impossible to squeeze much functionality into it. </p>
<p> Therefore, most systems split the role of loading the OS between a primary OS loader and a secondary OS loader; this secondary OS loader may be located within a larger portion of persistent storage, such as a disk partition. </p>
<p> In Linux, the OS loader is often either <code><a href="/docs/linux/man/8-lilo/">lilo</a></code>(8) or <code><a href="/docs/linux/man/8-grub/">grub</a></code>(8).</p>
<h3>Kernel</h3>
<p>When the kernel is loaded, it initializes various components of the computer and operating system; each portion of software responsible for such a task is usually consider &quot;a <code>driver</code>&quot; for the applicable component. The kernel starts the virtual memory swapper (it is a kernel process, called &quot;kswapd&quot; in a modern Linux kernel), and mounts some filesystem at the root path, <i>/</i>. </p>
<p> Some of the parameters that may be passed to the kernel relate to these activities (for example, the default root filesystem can be overridden); for further information on Linux kernel parameters, read <code><a href="/docs/linux/man/7-bootparam/">bootparam</a></code>(7). </p>
<p> Only then does the kernel create the initial userland process, which is given the number 1 as its <code>PID</code> (process ID). Traditionally, this process executes the program <i>/sbin/init</i>, to which are passed the parameters that haven&#8217;t already been handled by the kernel.</p>
<h3>Root user-space process</h3>
<dl>
<dt>Note:</p>
<dd>The following description applies to an OS based on UNIX System V Release 4. However, a number of widely used systems have adopted a related but fundamentally different approach known as <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), for which the bootup process is detailed in its associated <code><a href="/docs/linux/man/7-bootup/">bootup</a></code>(7).</dl>
<p> When <i>/sbin/init</i> starts, it reads <i>/etc/inittab</i> for further instructions. This file defines what should be run when the <i>/sbin/init</i> program is instructed to enter a particular <i>run-level</i>, giving the administrator an easy way to establish an environment for some usage; each run-level is associated with a set of services (for example, run-level <code>S</code> is <i>single-user</i> mode, and run-level <code>2</code> entails running most network services). </p>
<p> The administrator may change the current run-level via <code><a href="/docs/linux/man/1-init/">init</a></code>(1), and query the current run-level via <code><a href="/docs/linux/man/8-runlevel/">runlevel</a></code>(8). </p>
<p> However, since it is not convenient to manage individual services by editing this file, <i>/etc/inittab</i> only bootstraps a set of scripts that actually start/stop the individual services.</p>
<h3>Boot scripts</h3>
<dl>
<dt>Note:</p>
<dd>The following description applies to an OS based on UNIX System V Release 4. However, a number of widely used systems (Slackware Linux, FreeBSD, OpenBSD) have a somewhat different scheme for boot scripts.</dl>
<p> For each managed service (mail, nfs server, cron, etc.), there is a single startup script located in a specific directory (<i>/etc/init.d</i> in most versions of Linux). Each of these scripts accepts as a single argument the word &quot;start&quot; (causing it to start the service) or the word &quot;stop&quot; (causing it to stop the service). The script may optionally accept other &quot;convenience&quot; parameters (e.g., &quot;restart&quot; to stop and then start, &quot;status&quot; to display the service status, etc.). Running the script without parameters displays the possible arguments.</p>
<h3>Sequencing directories</h3>
<p>To make specific scripts start/stop at specific run-levels and in a specific order, there are <i>sequencing directories</i>, normally of the form <i>/etc/rc[0-6S].d</i>. In each of these directories, there are links (usually symbolic) to the scripts in the <i>/etc/init.d</i> directory. </p>
<p> A primary script (usually <i>/etc/rc</i>) is called from <code><a href="/docs/linux/man/5-inittab/">inittab</a></code>(5); this primary script calls each service&#8217;s script via a link in the relevant sequencing directory. Each link whose name begins with &#8216;S&#8217; is called with the argument &quot;start&quot; (thereby starting the service). Each link whose name begins with &#8216;K&#8217; is called with the argument &quot;stop&quot; (thereby stopping the service). </p>
<p> To define the starting or stopping order within the same run-level, the name of a link contains an <code>order-number</code>. Also, for clarity, the name of a link usually ends with the name of the service to which it refers. For example, the link <i>/etc/rc2.d/S80sendmail</i> starts the sendmail service on runlevel 2. This happens after <i>/etc/rc2.d/S12syslog</i> is run but before <i>/etc/rc2.d/S90xfs</i> is run. </p>
<p> To manage these links is to manage the boot order and run-levels; under many systems, there are tools to help with this task (e.g., <code><a href="/docs/linux/man/8-chkconfig/">chkconfig</a></code>(8)).</p>
<h3>Boot configuration</h3>
<p>A program that provides a service is often called a &quot;<code>daemon</code>&quot;. Usually, a daemon may receive various command-line options and parameters. To allow a system administrator to change these inputs without editing an entire boot script, some separate configuration file is used, and is located in a specific directory where an associated boot script may find it (<i>/etc/sysconfig</i> on older Red Hat systems). </p>
<p> In older UNIX systems, such a file contained the actual command line options for a daemon, but in modern Linux systems (and also in HP-UX), it just contains shell variables. A boot script in <i>/etc/init.d</i> reads and includes its configuration file (that is, it &quot;<code>sources</code>&quot; its configuration file) and then uses the variable values.</p>
<h2>Files</h2>
<p><i>/etc/init.d/</i>, <i>/etc/rc[S0-6].d/</i>, <i>/etc/sysconfig/</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-init/">init</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-inittab/">inittab</a></code>(5), <code><a href="/docs/linux/man/7-bootparam/">bootparam</a></code>(7), <code><a href="/docs/linux/man/7-bootup/">bootup</a></code>(7), <code><a href="/docs/linux/man/8-runlevel/">runlevel</a></code>(8), <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
