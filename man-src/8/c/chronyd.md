---
title: "chronyd(8)"
name: "chronyd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chronyd/"
description: "chronyd – chrony daemon"
---

<p>chronyd &#8211; chrony daemon</p>
<h2>Synopsis</h2>
<p><code>chronyd</code> [<i>OPTION</i>]&#8230; [<i>DIRECTIVE</i>]&#8230;</p>
<h2>Description</h2>
<p><code>chronyd</code> is a daemon for synchronisation of the system clock. It can synchronise the clock with NTP servers, reference clocks (e.g. a GPS receiver), and manual input using wristwatch and keyboard via <code>chronyc</code>. It can also operate as an NTPv4 (RFC 5905) server and peer to provide a time service to other computers in the network. </p>
<p> If no configuration directives are specified on the command line, <code>chronyd</code> will read them from a configuration file. The compiled-in default location of the file is <i>/etc/chrony.conf</i>. </p>
<p> Information messages and warnings will be logged to syslog.</p>
<h2>Options</h2>
<p><code>-4</code></p>
<dl>
<dd>With this option hostnames will be resolved only to IPv4 addresses and only IPv4 sockets will be created.</dl>
<p> <code>-6</code></p>
<dl>
<dd>With this option hostnames will be resolved only to IPv6 addresses and only IPv6 sockets will be created.</dl>
<p> <code>-f</code> <i>file</i></p>
<dl>
<dd>This option can be used to specify an alternate location for the configuration file (default <i>/etc/chrony.conf</i>).</dl>
<p> <code>-n</code></p>
<dl>
<dd>When run in this mode, the program will not detach itself from the terminal.</dl>
<p> <code>-d</code></p>
<dl>
<dd>When run in this mode, the program will not detach itself from the terminal, and all messages will be sent to the terminal instead of to syslog. When <code>chronyd</code> was compiled with debugging support, this option can be used twice to print also debugging messages.</dl>
<p> <code>-q</code></p>
<dl>
<dd>When run in this mode, <code>chronyd</code> will set the system clock once and exit. It will not detach from the terminal.</dl>
<p> <code>-Q</code></p>
<dl>
<dd>This option is similar to <code>-q</code>, but it will only print the offset without any corrections of the clock.</dl>
<p> <code>-r</code></p>
<dl>
<dd>This option will try to reload and then delete files containing sample histories for each of the servers and reference clocks being used. These histories are created by using the <code>dump</code> command in <code>chronyc</code>, or by setting the <code>dumponexit</code> directive in the configuration file. This option is useful if you want to stop and restart <code>chronyd</code> briefly for any reason, e.g. to install a new version. However, it should be used only on systems where the kernel can maintain clock compensation whilst not under <code>chronyd</code>&#8216;s control (i.e. Linux, FreeBSD, NetBSD and Solaris).</dl>
<p> <code>-R</code></p>
<dl>
<dd>When this option is used, the <code>initstepslew</code> directive and the <code>makestep</code> directive used with a positive limit will be ignored. This option is useful when restarting <code>chronyd</code> and can be used in conjunction with the <code>-r</code> option.</dl>
<p> <code>-s</code></p>
<dl>
<dd>This option will set the system clock from the computer&#8217;s real-time clock (RTC) or to the last modification time of the file specified by the <code>driftfile</code> directive. Real-time clocks are supported only on Linux. </p>
<p> If used in conjunction with the <code>-r</code> flag, <code>chronyd</code> will attempt to preserve the old samples after setting the system clock from the RTC. This can be used to allow <code>chronyd</code> to perform long term averaging of the gain or loss rate across system reboots, and is useful for systems with intermittent access to network that are shut down when not in use. For this to work well, it relies on <code>chronyd</code> having been able to determine accurate statistics for the difference between the RTC and system clock last time the computer was on. </p>
<p> If the last modification time of the drift file is later than both the current time and the RTC time, the system time will be set to it to restore the time when <code>chronyd</code> was previously stopped. This is useful on computers that have no RTC or the RTC is broken (e.g. it has no battery).</dl>
<p> <code>-t</code> <i>timeout</i></p>
<dl>
<dd>This option sets a timeout (in seconds) after which <code>chronyd</code> will exit. If the clock is not synchronised, it will exit with a non-zero status. This is useful with the <code>-q</code> or <code>-Q</code> option to shorten the maximum time waiting for measurements, or with the <code>-r</code> option to limit the time when <code>chronyd</code> is running, but still allow it to adjust the frequency of the system clock.</dl>
<p> <code>-u</code> <i>user</i></p>
<dl>
<dd>This option sets the name of the system user to which <code>chronyd</code> will switch after start in order to drop root privileges. It overrides the <code>user</code> directive (default <i>chrony</i>). </p>
<p> On Linux, <code>chronyd</code> needs to be compiled with support for the <code>libcap</code> library. On macOS, FreeBSD, NetBSD and Solaris <code>chronyd</code> forks into two processes. The child process retains root privileges, but can only perform a very limited range of privileged system calls on behalf of the parent.</dl>
<p> <code>-F</code> <i>level</i></p>
<dl>
<dd>This option configures a system call filter when <code>chronyd</code> is compiled with support for the Linux secure computing (seccomp) facility. In level 1 the process is killed when a forbidden system call is made, in level -1 the SYSSIG signal is thrown instead and in level 0 the filter is disabled (default 0). </p>
<p> It&#8217;s recommended to enable the filter only when it&#8217;s known to work on the version of the system where <code>chrony</code> is installed as the filter needs to allow also system calls made from libraries that <code>chronyd</code> is using (e.g. libc) and different versions or implementations of the libraries may make different system calls. If the filter is missing some system call, <code>chronyd</code> could be killed even in normal operation.</dl>
<p> <code>-P</code> <i>priority</i></p>
<dl>
<dd>On Linux, this option will select the SCHED_FIFO real-time scheduler at the specified priority (which must be between 0 and 100). On macOS, this option must have either a value of 0 (the default) to disable the thread time constraint policy or 1 for the policy to be enabled. Other systems do not support this option.</dl>
<p> <code>-m</code></p>
<dl>
<dd>This option will lock <code>chronyd</code> into RAM so that it will never be paged out. This mode is only supported on Linux.</dl>
<p> <code>-v</code></p>
<dl>
<dd>With this option <code>chronyd</code> will print version number to the terminal and exit.</dl>
<h2>Files</h2>
<p><i>/etc/chrony.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chronyc/">chronyc</a>(1)</code>, <code><a href="/docs/linux/man/5-chrony-conf/">chrony.conf</a>(5)</code></p>
<h2>Bugs</h2>
<p>For instructions on how to report bugs, please visit &lt;URL: <a rel="nofollow" href="https://chrony.tuxfamily.org/">https://chrony.tuxfamily.org/</a> &gt;.</p>
<h2>Authors</h2>
<p>chrony was written by Richard Curnow, Miroslav Lichvar, and others.</p>
