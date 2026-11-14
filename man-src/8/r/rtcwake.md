---
title: "rtcwake(8)"
name: "rtcwake"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rtcwake/"
description: "rtcwake – enter a system sleep state until specified wakeup time"
---

<p>rtcwake &#8211; enter a system sleep state until specified wakeup time</p>
<h2>Synopsis</h2>
<p><code>rtcwake</code> [options] [<code>-d</code> <i>device</i>] [<code>-m</code> <i>standby_mode</i>] {<code>-s</code> <i>seconds</i>|<code>-t</code> <i>time_t</i>}</p>
<h2>Description</h2>
<p>This program is used to enter a system sleep state and to automatically wake from it at a specified time. </p>
<p> This uses cross-platform Linux interfaces to enter a system sleep state, and leave it no later than a specified time. It uses any RTC framework driver that supports standard driver model wakeup flags. </p>
<p> This is normally used like the old <code>apmsleep</code> utility, to wake from a suspend state like ACPI S1 (standby) or S3 (suspend-to-RAM). Most platforms can implement those without analogues of BIOS, APM, or ACPI. </p>
<p> On some systems, this can also be used like <code>nvram-wakeup</code>, waking from states like ACPI S4 (suspend to disk). Not all systems have persistent media that are appropriate for such suspend modes. </p>
<p> Note that alarm functionality depends on hardware; not every RTC is able to setup an alarm up to 24 hours in the future. </p>
<p> The suspend setup may be interrupted by active hardware; for example wireless USB input devices that continue to send events for some fraction of a second after the return key is pressed. <code>rtcwake</code> tries to avoid this problem and it waits to terminal to settle down before entering a system sleep.</p>
<h2>Options</h2>
<p><code>-A</code>, <code>&#8211;adjfile</code> <i>file</i></p>
<dl>
<dd>Specify an alternative path to the adjust file.</dl>
<p> <code>-a</code>, <code>&#8211;auto</code></p>
<dl>
<dd>Read the clock mode (whether the hardware clock is set to UTC or local time) from the <i>adjtime</i> file, where <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) stores that information. This is the default.</dl>
<p> <code>&#8211;date</code> <i>timestamp</i></p>
<dl>
<dd>Set the wakeup time to the value of the timestamp. Format of the timestamp can be any of the following:</dl>
<table BORDER>
<tr VALIGN=top>
<td>
<p> YYYYMMDDhhmmss </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> YYYY-MM-DD hh:mm:ss </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> YYYY-MM-DD hh:mm </td>
<td>
<p> (seconds will be set to 00)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> YYYY-MM-DD </td>
<td>
<p> (time will be set to 00:00:00)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hh:mm:ss </td>
<td>
<p> (date will be set to today)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hh:mm </td>
<td>
<p> (date will be set to today, seconds to 00)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> tomorrow </td>
<td>
<p> (time is set to 00:00:00)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> +5min </td>
<td>
</td>
</tr>
</table>
<p> <code>-d</code>, <code>&#8211;device</code> <i>device</i></p>
<dl>
<dd>Use the specified <i>device</i> instead of <code>rtc0</code> as realtime clock. This option is only relevant if your system has more than one RTC. You may specify <code>rtc1</code>, <code>rtc2</code>, &#8230; here.</dl>
<p> <code>-l</code>, <code>&#8211;local</code></p>
<dl>
<dd>Assume that the hardware clock is set to local time, regardless of the contents of the <i>adjtime</i> file.</dl>
<p> <code>&#8211;list-modes</code></p>
<dl>
<dd>List available <code>&#8211;mode</code> option arguments.</dl>
<p> <code>-m</code>, <code>&#8211;mode</code> <i>mode</i></p>
<dl>
<dd>Go into the given standby state. Valid values for <i>mode</i> are: </p>
<p> <code>standby</code></p>
<dl>
<dd>ACPI state S1. This state offers minimal, though real, power savings, while providing a very low-latency transition back to a working system. This is the default mode.</dl>
<p> <code>freeze</code></p>
<dl>
<dd>The processes are frozen, all the devices are suspended and all the processors idled. This state is a general state that does not need any platform-specific support, but it saves less power than Suspend-to-RAM, because the system is still in a running state. (Available since Linux 3.9.)</dl>
<p> <code>mem</code></p>
<dl>
<dd>ACPI state S3 (Suspend-to-RAM). This state offers significant power savings as everything in the system is put into a low-power state, except for memory, which is placed in self-refresh mode to retain its contents.</dl>
<p> <code>disk</code></p>
<dl>
<dd>ACPI state S4 (Suspend-to-disk). This state offers the greatest power savings, and can be used even in the absence of low-level platform support for power management. This state operates similarly to Suspend-to-RAM, but includes a final step of writing memory contents to disk.</dl>
<p> <code>off</code></p>
<dl>
<dd>ACPI state S5 (Poweroff). This is done by calling &#8216;/sbin/shutdown&#8217;. Not officially supported by ACPI, but it usually works.</dl>
<p> <code>no</code></p>
<dl>
<dd>Don&#8217;t suspend, only set the RTC wakeup time.</dl>
<p> <code>on</code></p>
<dl>
<dd>Don&#8217;t suspend, but read the RTC device until an alarm time appears. This mode is useful for debugging.</dl>
<p> <code>disable</code></p>
<dl>
<dd>Disable a previously set alarm.</dl>
<p> <code>show</code></p>
<dl>
<dd>Print alarm information in format: &quot;alarm: off|on &lt;time&gt;&quot;. The time is in ctime() output format, e.g., &quot;alarm: on Tue Nov 16 04:48:45 2010&quot;.</dl>
</dl>
<p> <code>-n</code>, <code>&#8211;dry-run</code></p>
<dl>
<dd>This option does everything apart from actually setting up the alarm, suspending the system, or waiting for the alarm.</dl>
<p> <code>-s</code>, <code>&#8211;seconds</code> <i>seconds</i></p>
<dl>
<dd>Set the wakeup time to <i>seconds</i> in the future from now.</dl>
<p> <code>-t</code>, <code>&#8211;time</code> <i>time_t</i></p>
<dl>
<dd>Set the wakeup time to the absolute time <i>time_t</i>. <i>time_t</i> is the time in seconds since 1970-01-01, 00:00 UTC. Use the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) tool to convert between human-readable time and <i>time_t</i>.</dl>
<p> <code>-u</code>, <code>&#8211;utc</code></p>
<dl>
<dd>Assume that the hardware clock is set to UTC (Universal Time Coordinated), regardless of the contents of the <i>adjtime</i> file.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Be verbose.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Notes</h2>
<p>Some PC systems can&#8217;t currently exit sleep states such as <code>mem</code> using only the kernel code accessed by this driver. They need help from userspace code to make the framebuffer work again.</p>
<h2>Files</h2>
<p><i>/etc/adjtime</i></p>
<h2>History</h2>
<p>The program was posted several times on LKML and other lists before appearing in kernel commit message for Linux 2.6 in the GIT commit 87ac84f42a7a580d0dd72ae31d6a5eb4bfe04c6d.</p>
<h2>Authors</h2>
<p>The program was written by and improved by</p>
<h2>Copyright</h2>
<p>This is free software. You may redistribute copies of it under the terms of the <i>GNU General Public License</i> &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8), <code><a href="/docs/linux/man/1-date/">date</a></code>(1)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>rtcwake</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
