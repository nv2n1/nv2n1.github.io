---
title: "ntpdate(8)"
name: "ntpdate"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntpdate/"
description: "ntpdate – set the date and time via NTP"
---

<p>ntpdate &#8211; set the date and time via NTP</p>
<h2>&nbsp;<wbr></h2>
<p>Disclaimer: The functionality of this program is now available in the <code>ntpd</code> program. See the <code>-q</code> command line option in the <code>ntpd</code> &#8211; Network Time Protocol (NTP) daemon page. After a suitable period of mourning, the <code>ntpdate</code> program is to be retired from this distribution </p>
<h2>Synopsis</h2>
<p><code>ntpdate [ -46bBdqsuv ] [ -a </code><i>key</i><code> ] [ -e </code><i>authdelay</i><code> ] [ -k </code><i>keyfile</i><code> ] [ -o </code><i>version</i><code> ] [ -p </code><i>samples</i><code> ] [ -t </code><i>timeout</i><code> ] [ -U </code><i>user_name</i><code> ] </code><i>server</i><code> [ &#8230; ]</code> </p>
<h2>Description</h2>
<p><code>ntpdate</code> sets the local date and time by polling the Network Time Protocol (NTP) server(s) given as the <i>server</i> arguments to determine the correct time. It must be run as root on the local host. A number of samples are obtained from each of the servers specified and a subset of the NTP clock filter and selection algorithms are applied to select the best of these. Note that the accuracy and reliability of <code>ntpdate</code> depends on the number of servers, the number of polls each time it is run and the interval between runs. <code>ntpdate</code> can be run manually as necessary to set the host clock, or it can be run from the host startup script to set the clock at boot time. This is useful in some cases to set the clock initially before starting the NTP daemon <code>ntpd</code>46 It is also possible to run <code>ntpdate</code> from a <code>cron</code> script. However, it is important to note that <code>ntpdate</code> with contrived <code>cron</code> scripts is no substitute for the NTP daemon, which uses sophisticated algorithms to maximize accuracy and reliability while minimizing resource use. Finally, since <code>ntpdate</code> does not discipline the host clock frequency as does <code>ntpd</code>, the accuracy using <code>ntpdate</code> is limited. Time adjustments are made by <code>ntpdate</code> in one of two ways. If <code>ntpdate</code> determines the clock is in error more than 0.5 second it will simply step the time by calling the system <code>settimeofday()</code> routine. If the error is less than 0.5 seconds, it will slew the time by calling the system <code>adjtime()</code> routine. The latter technique is less disruptive and more accurate when the error is small, and works quite well when <code>ntpdate</code> is run by <code>cron</code> every hour or two. <code>ntpdate</code> will decline to set the date if an NTP server daemon (e.g., <code>ntpd</code>) is running on the same host. When running <code>ntpdate</code> on a regular basis from <code>cron</code> as an alternative to running a daemon, doing so once every hour or two will result in precise enough timekeeping to avoid stepping the clock. Note that in contexts where a host name is expected, a <code>-4</code> qualifier preceding the host name forces DNS resolution to the IPv4 namespace, while a <code>-6</code> qualifier forces DNS resolution to the IPv6 namespace. If NetInfo support is compiled into <code>ntpdate</code>, then the <code>server</code> argument is optional if <code>ntpdate</code> can find a time server in the NetInfo configuration for <code>ntpd</code>46 </p>
<h2>Command Line Options</h2>
<dl>
<dd>
<dl>
<dt><code>-4</code></p>
<dd>Force DNS resolution of following host names on the command line to the IPv4 namespace.</p>
<dt><code>-6</code></p>
<dd>Force DNS resolution of following host names on the command line to the IPv6 namespace.</p>
<dt><code>-a </code><i>key</i></p>
<dd>Enable the authentication function and specify the key identifier to be used for authentication as the argument <i>key</i>46 The keys and key identifiers must match in both the client and server key files. The default is to disable the authentication function.</p>
<dt><code>-B</code></p>
<dd>Force the time to always be slewed using the adjtime() system call, even if the measured offset is greater than +-500 ms. The default is to step the time using settimeofday() if the offset is greater than +-500 ms. Note that, if the offset is much greater than +-500 ms in this case, that it can take a long time (hours) to slew the clock to the correct value. During this time. the host should not be used to synchronize clients.</p>
<dt><code>-b</code></p>
<dd>Force the time to be stepped using the settimeofday() system call, rather than slewed (default) using the adjtime() system call. This option should be used when called from a startup file at boot time.</p>
<dt><code>-d</code></p>
<dd>Enable the debugging mode, in which <code>ntpdate</code> will go through all the steps, but not adjust the local clock. Information useful for general debugging will also be printed.</p>
<dt><code>-e </code><i>authdelay</i></p>
<dd>Specify the processing delay to perform an authentication function as the value <i>authdelay</i>, in seconds and fraction (see <code>ntpd</code> for details). This number is usually small enough to be negligible for most purposes, though specifying a value may improve timekeeping on very slow CPU&#8217;s.</p>
<dt><code>-k </code><i>keyfile</i></p>
<dd>Specify the path for the authentication key file as the string <i>keyfile</i>46 The default is <code>/etc/ntp/keys</code>46 This file should be in the format described in <code>ntpd</code>46</p>
<dt><code>-o </code><i>version</i></p>
<dd>Specify the NTP version for outgoing packets as the integer <i>version</i>, which can be 1 or 2. The default is 4. This allows <code>ntpdate</code> to be used with older NTP versions.</p>
<dt><code>-p </code><i>samples</i></p>
<dd>Specify the number of samples to be acquired from each server as the integer <i>samples</i>, with values from 1 to 8 inclusive. The default is 4.</p>
<dt><i></i><code>-q</code><i></i></p>
<dd>Query only &#8211; don&#8217;t set the clock.</p>
<dt><code>-s</code></p>
<dd>Divert logging output from the standard output (default) to the system <code>syslog</code> facility. This is designed primarily for convenience of <code>cron</code> scripts.</p>
<dt><code>-t </code><i>timeout</i></p>
<dd>Specify the maximum time waiting for a server response as the value <i>timeout</i>, in seconds and fraction. The value is is rounded to a multiple of 0.2 seconds. The default is 1 second, a value suitable for polling across a LAN.</p>
<dt><code>-u</code></p>
<dd>Direct <code>ntpdate</code> to use an unprivileged port for outgoing packets. This is most useful when behind a firewall that blocks incoming traffic to privileged ports, and you want to synchronize with hosts beyond the firewall. Note that the <code>-d</code> option always uses unprivileged ports.</p>
<dt><code>&#8211;</code><i>v</i></p>
<dd>Be verbose. This option will cause <code>ntpdate</code>&#8216;s version identification string to be logged.</p>
<dt><code>-U </code><i>user_name</i></p>
<dd>ntpdate process drops root privileges and changes user ID to <i>user_name</i> and group ID to the primary group of <i>server_user</i>46</dl>
</dl>
<h2>Diagnostics</h2>
<p><code>ntpdate</code>&#8216;s exit status is zero if it finds a server and updates the clock, and nonzero otherwise.</p>
<h2>Files</h2>
<p><code>/etc/ntp/keys</code> &#8211; encryption keys used by <code>ntpdate</code>46</p>
<h2>Bugs</h2>
<p>The slew adjustment is actually 50% larger than the measured offset, since this (it is argued) will tend to keep a badly drifting clock more accurate. This is probably not a good idea and may cause a troubling hunt for some values of the kernel variables <code>tick</code> and <code>tickadj</code>46</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpd/">ntpd</a>(8) The official HTML documentation. This file was automatically generated from HTML source. </p>
