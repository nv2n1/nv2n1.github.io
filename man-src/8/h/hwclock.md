---
title: "hwclock(8)"
name: "hwclock"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hwclock/"
description: "hwclock – time clocks utility"
---

<p>hwclock &#8211; time clocks utility</p>
<h2>Synopsis</h2>
<p><code>hwclock</code> [<i>function</i>] [<i>option</i>&#8230;]</p>
<h2>Description</h2>
<p><code>hwclock</code> is an administration tool for the time clocks. It can: display the Hardware Clock time; set the Hardware Clock to a specified time; set the Hardware Clock from the System Clock; set the System Clock from the Hardware Clock; compensate for Hardware Clock drift; correct the System Clock timescale; set the kernel&#8217;s timezone, NTP timescale, and epoch (Alpha only); and predict future Hardware Clock values based on its drift rate. </p>
<p> Since v2.26 important changes were made to the <code>&#8211;hctosys</code> function and the <code>&#8211;directisa</code> option, and a new option <code>&#8211;update-drift</code> was added. See their respective descriptions below.</p>
<h2>Functions</h2>
<p>The following functions are mutually exclusive, only one can be given at a time. If none is given, the default is <code>&#8211;show</code>. </p>
<p> <code>-a, &#8211;adjust</code></p>
<dl>
<dd>Add or subtract time from the Hardware Clock to account for systematic drift since the last time the clock was set or adjusted. See the discussion below, under <code>The Adjust Function</code>.</dl>
<p> <code>&#8211;getepoch</code>; <code>&#8211;setepoch</code></p>
<dl>
<dd>These functions are for Alpha machines only, and are only available through the Linux kernel RTC driver. </p>
<p> They are used to read and set the kernel&#8217;s Hardware Clock epoch value. Epoch is the number of years into AD to which a zero year value in the Hardware Clock refers. For example, if the machine&#8217;s BIOS sets the year counter in the Hardware Clock to contain the number of full years since 1952, then the kernel&#8217;s Hardware Clock epoch value must be 1952. </p>
<p> The <code>&#8211;setepoch</code> function requires using the <code>&#8211;epoch</code> option to specify the year. For example: </p>
<p> <code>hwclock &#8211;setepoch &#8211;epoch=1952</code> </p>
<p> The RTC driver attempts to guess the correct epoch value, so setting it may not be required. </p>
<p> This epoch value is used whenever <code>hwclock</code> reads or sets the Hardware Clock on an Alpha machine. For ISA machines the kernel uses the fixed Hardware Clock epoch of 1900.</dl>
<p> <code>&#8211;predict</code></p>
<dl>
<dd>Predict what the Hardware Clock will read in the future based upon the time given by the <code>&#8211;date</code> option and the information in <i>/etc/adjtime</i>. This is useful, for example, to account for drift when setting a Hardware Clock wakeup (aka alarm). See <code><a href="/docs/linux/man/8-rtcwake/">rtcwake</a></code>(8). </p>
<p> Do not use this function if the Hardware Clock is being modified by anything other than the current operating system&#8217;s <code>hwclock</code> command, such as &#8217;11 minute mode&#8217; or from dual-booting another OS.</dl>
<p> <code>-r</code>, <code>&#8211;show</code>; <code>&#8211;get</code></p>
<dl>
<dd>Read the Hardware Clock and print its time to standard output in the <code>ISO 8601</code> format. The time shown is always in local time, even if you keep your Hardware Clock in UTC. See the <code>&#8211;localtime</code> option. </p>
<p> Showing the Hardware Clock time is the default when no function is specified. </p>
<p> The <code>&#8211;get</code> function also applies drift correction to the time read, based upon the information in <i>/etc/adjtime</i>. Do not use this function if the Hardware Clock is being modified by anything other than the current operating system&#8217;s <code>hwclock</code> command, such as &#8217;11 minute mode&#8217; or from dual-booting another OS.</dl>
<p> <code>-s</code>, <code>&#8211;hctosys</code></p>
<dl>
<dd>Set the System Clock from the Hardware Clock. The time read from the Hardware Clock is compensated to account for systematic drift before using it to set the System Clock. See the discussion below, under <code>The Adjust Function</code>. </p>
<p> The System Clock must be kept in the UTC timescale for date-time applications to work correctly in conjunction with the timezone configured for the system. If the Hardware Clock is kept in local time then the time read from it must be shifted to the UTC timescale before using it to set the System Clock. The <code>&#8211;hctosys</code> function does this based upon the information in the <i>/etc/adjtime</i> file or the command line arguments <code>&#8211;localtime</code> and <code>&#8211;utc</code>. Note: no daylight saving adjustment is made. See the discussion below, under <code>LOCAL vs UTC</code>. </p>
<p> The kernel also keeps a timezone value, the <code>&#8211;hctosys</code> function sets it to the timezone configured for the system. The system timezone is configured by the TZ environment variable or the <i>/etc/localtime</i> file, as <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) would interpret them. The obsolete <i>tz_dsttime</i> field of the kernel&#8217;s timezone value is set to zero. (For details on what this field used to mean, see <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2).) </p>
<p> When used in a startup script, making the <code>&#8211;hctosys</code> function the first caller of <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2) from boot, it will set the NTP &#8217;11 minute mode&#8217; timescale via the <i>persistent_clock_is_local</i> kernel variable. If the Hardware Clock&#8217;s timescale configuration is changed then a reboot is required to inform the kernel. See the discussion below, under <code>Automatic Hardware Clock Synchronization by the Kernel</code>. </p>
<p> This is a good function to use in one of the system startup scripts before the file systems are mounted read/write. </p>
<p> This function should never be used on a running system. Jumping system time will cause problems, such as corrupted filesystem timestamps. Also, if something has changed the Hardware Clock, like NTP&#8217;s &#8217;11 minute mode&#8217;, then <code>&#8211;hctosys</code> will set the time incorrectly by including drift compensation. </p>
<p> Drift compensation can be inhibited by setting the drift factor in <i>/etc/adjtime</i> to zero. This setting will be persistent as long as the <code>&#8211;update-drift</code> option is not used with <code>&#8211;systohc</code> at shutdown (or anywhere else). Another way to inhibit this is by using the <code>&#8211;noadjfile</code> option when calling the <code>&#8211;hctosys</code> function. A third method is to delete the <i>/etc/adjtime</i> file. <code>Hwclock</code> will then default to using the UTC timescale for the Hardware Clock. If the Hardware Clock is ticking local time it will need to be defined in the file. This can be done by calling <code>hwclock &#8211;localtime &#8211;adjust</code>; when the file is not present this command will not actually adjust the Clock, but it will create the file with local time configured, and a drift factor of zero. </p>
<p> A condition under which inhibiting <code>hwclock</code>&#8216;s drift correction may be desired is when dual-booting multiple operating systems. If while this instance of Linux is stopped, another OS changes the Hardware Clock&#8217;s value, then when this instance is started again the drift correction applied will be incorrect. </p>
<p> For <code>hwclock</code>&#8216;s drift correction to work properly it is imperative that nothing changes the Hardware Clock while its Linux instance is not running.</dl>
<p> <code>&#8211;set</code></p>
<dl>
<dd>Set the Hardware Clock to the time given by the <code>&#8211;date</code> option, and update the timestamps in <i>/etc/adjtime</i>. With the <code>&#8211;update-drift</code> option also (re)calculate the drift factor. Try it without the option if <code>&#8211;set</code> fails. See <code>&#8211;update-drift</code> below.</dl>
<p> <code>&#8211;systz</code></p>
<dl>
<dd>This is an alternate to the <code>&#8211;hctosys</code> function that does not read the Hardware Clock nor set the System Clock; consequently there is not any drift correction. It is intended to be used in a startup script on systems with kernels above version 2.6 where you know the System Clock has been set from the Hardware Clock by the kernel during boot. </p>
<p> It does the following things that are detailed above in the <code>&#8211;hctosys</code> function: </p>
<dl>
<dd>&bull; Corrects the System Clock timescale to UTC as needed. Only instead of accomplishing this by setting the System Clock, <code>hwclock</code> simply informs the kernel and it handles the change.</dl>
<dl>
<dd>&bull; Sets the kernel&#8217;s NTP &#8217;11 minute mode&#8217; timescale.</dl>
<dl>
<dd>&bull; Sets the kernel&#8217;s timezone.</dl>
</dl>
<p> The first two are only available on the first call of <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2) after boot. Consequently this option only makes sense when used in a startup script. If the Hardware Clocks timescale configuration is changed then a reboot would be required to inform the kernel. </p>
<p> <code>-w</code>, <code>&#8211;systohc</code></p>
<dl>
<dd>Set the Hardware Clock from the System Clock, and update the timestamps in <i>/etc/adjtime</i>. With the <code>&#8211;update-drift</code> option also (re)calculate the drift factor. Try it without the option if <code>&#8211;systohc</code> fails. See <code>&#8211;update-drift</code> below.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Options</h2>
<p><code>&#8211;adjfile=</code><i>filename</i></p>
<dl>
<dd>Override the default <i>/etc/adjtime</i> file path.</dl>
<p> <code>&#8211;date=</code><i>date_string</i></p>
<dl>
<dd>This option must be used with the <code>&#8211;set</code> or <code>&#8211;predict</code> functions, otherwise it is ignored. </p>
<p> <code>hwclock &#8211;set &#8211;date=&#8217;16:45&#8242;</code> </p>
<p> <code>hwclock &#8211;predict &#8211;date=&#8217;2525-08-14 07:11:05&#8242;</code> </p>
<p> The argument must be in local time, even if you keep your Hardware Clock in UTC. See the <code>&#8211;localtime</code> option. Therefore, the argument should not include any timezone information. It also should not be a relative time like &quot;+5 minutes&quot;, because <code>hwclock</code>&#8216;s precision depends upon correlation between the argument&#8217;s value and when the enter key is pressed. Fractional seconds are silently dropped. This option is capable of understanding many time and date formats, but the previous parameters should be observed.</dl>
<p> <code>&#8211;delay=</code><i>seconds</i></p>
<dl>
<dd>This option can be used to overwrite the internally used delay when setting the clock time. The default is 0.5 (500ms) for rtc_cmos, for another RTC types the delay is 0. If RTC type is impossible to determine (from sysfs) then it defaults also to 0.5 to be backwardly compatible. </p>
<p> The 500ms default is based on commonly used MC146818A-compatible (x86) hardware clock. This Hardware Clock can only be set to any integer time plus one half second. The integer time is required because there is no interface to set or get a fractional second. The additional half second delay is because the Hardware Clock updates to the following second precisely 500 ms after setting the new time. Unfortunately, this behavior is hardware specific and in same cases another delay is required.</dl>
<p> <code>-D</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Use <code>&#8211;verbose</code>. The <code>&#8211;debug</code> option has been deprecated and may be repurposed or removed in a future release.</dl>
<p> <code>&#8211;directisa</code></p>
<dl>
<dd>This option is meaningful for ISA compatible machines in the x86 and x86_64 family. For other machines, it has no effect. This option tells <code>hwclock</code> to use explicit I/O instructions to access the Hardware Clock. Without this option, <code>hwclock</code> will use the rtc device file, which it assumes to be driven by the Linux RTC device driver. As of v2.26 it will no longer automatically use directisa when the rtc driver is unavailable; this was causing an unsafe condition that could allow two processes to access the Hardware Clock at the same time. Direct hardware access from userspace should only be used for testing, troubleshooting, and as a last resort when all other methods fail. See the <code>&#8211;rtc</code> option.</dl>
<p> <code>&#8211;epoch=</code><i>year</i></p>
<dl>
<dd>This option is required when using the <code>&#8211;setepoch</code> function. The minimum <i>year</i> value is 1900. The maximum is system dependent (<code>ULONG_MAX &#8211; 1</code>).</dl>
<p> <code>-f</code>, <code>&#8211;rtc=</code><i>filename</i></p>
<dl>
<dd>Override <code>hwclock</code>&#8216;s default rtc device file name. Otherwise it will use the first one found in this order: <i>/dev/rtc0</i>, <i>/dev/rtc</i>, <i>/dev/misc/rtc</i>. For <code>IA-64:</code> <i>/dev/efirtc</i> <i>/dev/misc/efirtc</i></dl>
<p> <code>-l</code>, <code>&#8211;localtime</code>; <code>-u</code>, <code>&#8211;utc</code></p>
<dl>
<dd>Indicate which timescale the Hardware Clock is set to. </p>
<p> The Hardware Clock may be configured to use either the UTC or the local timescale, but nothing in the clock itself says which alternative is being used. The <code>&#8211;localtime</code> or <code>&#8211;utc</code> options give this information to the <code>hwclock</code> command. If you specify the wrong one (or specify neither and take a wrong default), both setting and reading the Hardware Clock will be incorrect. </p>
<p> If you specify neither <code>&#8211;utc</code> nor <code>&#8211;localtime</code> then the one last given with a set function (<code>&#8211;set</code>, <code>&#8211;systohc</code>, or <code>&#8211;adjust</code>), as recorded in <i>/etc/adjtime</i>, will be used. If the adjtime file doesn&#8217;t exist, the default is UTC. </p>
<p> Note: daylight saving time changes may be inconsistent when the Hardware Clock is kept in local time. See the discussion below, under <code>LOCAL vs UTC</code>.</dl>
<p> <code>&#8211;noadjfile</code></p>
<dl>
<dd>Disable the facilities provided by <i>/etc/adjtime</i>. <code>hwclock</code> will not read nor write to that file with this option. Either <code>&#8211;utc</code> or <code>&#8211;localtime</code> must be specified when using this option.</dl>
<p> <code>&#8211;test</code></p>
<dl>
<dd>Do not actually change anything on the system, that is, the Clocks or <i>/etc/adjtime</i> (<code>&#8211;verbose</code> is implicit with this option).</dl>
<p> <code>&#8211;update-drift</code></p>
<dl>
<dd>Update the Hardware Clock&#8217;s drift factor in <i>/etc/adjtime</i>. It can only be used with <code>&#8211;set</code> or <code>&#8211;systohc</code>. </p>
<p> A minimum four hour period between settings is required. This is to avoid invalid calculations. The longer the period, the more precise the resulting drift factor will be. </p>
<p> This option was added in v2.26, because it is typical for systems to call <code>hwclock &#8211;systohc</code> at shutdown; with the old behavior this would automatically (re)calculate the drift factor which caused several problems: </p>
<dl>
<dd>&bull; When using NTP with an &#8217;11 minute mode&#8217; kernel the drift factor would be clobbered to near zero.</dl>
<dl>
<dd>&bull; It would not allow the use of &#8216;cold&#8217; drift correction. With most configurations using &#8216;cold&#8217; drift will yield favorable results. Cold, means when the machine is turned off which can have a significant impact on the drift factor.</dl>
<dl>
<dd>&bull; (Re)calculating drift factor on every shutdown delivers suboptimal results. For example, if ephemeral conditions cause the machine to be abnormally hot the drift factor calculation would be out of range.</dl>
<dl>
<dd>&bull; Significantly increased system shutdown times (as of v2.31 when not using <code>&#8211;update-drift</code> the RTC is not read).</dl>
</dl>
<p> Having <code>hwclock</code> calculate the drift factor is a good starting point, but for optimal results it will likely need to be adjusted by directly editing the <i>/etc/adjtime</i> file. For most configurations once a machine&#8217;s optimal drift factor is crafted it should not need to be changed. Therefore, the old behavior to automatically (re)calculate drift was changed and now requires this option to be used. See the discussion below, under <code>The Adjust Function</code>. </p>
<p> This option requires reading the Hardware Clock before setting it. If it cannot be read, then this option will cause the set functions to fail. This can happen, for example, if the Hardware Clock is corrupted by a power failure. In that case, the clock must first be set without this option. Despite it not working, the resulting drift correction factor would be invalid anyway. </p>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Display more details about what <code>hwclock</code> is doing internally.</dl>
<h2>Notes</h2>
<h3>Clocks in a Linux System</h3>
<p>There are two types of date-time clocks: </p>
<p> <code>The Hardware Clock:</code> This clock is an independent hardware device, with its own power domain (battery, capacitor, etc), that operates when the machine is powered off, or even unplugged. </p>
<p> On an ISA compatible system, this clock is specified as part of the ISA standard. A control program can read or set this clock only to a whole second, but it can also detect the edges of the 1 second clock ticks, so the clock actually has virtually infinite precision. </p>
<p> This clock is commonly called the hardware clock, the real time clock, the RTC, the BIOS clock, and the CMOS clock. Hardware Clock, in its capitalized form, was coined for use by <code>hwclock</code>. The Linux kernel also refers to it as the persistent clock. </p>
<p> Some non-ISA systems have a few real time clocks with only one of them having its own power domain. A very low power external I2C or SPI clock chip might be used with a backup battery as the hardware clock to initialize a more functional integrated real-time clock which is used for most other purposes. </p>
<p> <code>The System Clock:</code> This clock is part of the Linux kernel and is driven by a timer interrupt. (On an ISA machine, the timer interrupt is part of the ISA standard.) It has meaning only while Linux is running on the machine. The System Time is the number of seconds since 00:00:00 January 1, 1970 UTC (or more succinctly, the number of seconds since 1969 UTC). The System Time is not an integer, though. It has virtually infinite precision. </p>
<p> The System Time is the time that matters. The Hardware Clock&#8217;s basic purpose is to keep time when Linux is not running so that the System Clock can be initialized from it at boot. Note that in DOS, for which ISA was designed, the Hardware Clock is the only real time clock. </p>
<p> It is important that the System Time not have any discontinuities such as would happen if you used the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) program to set it while the system is running. You can, however, do whatever you want to the Hardware Clock while the system is running, and the next time Linux starts up, it will do so with the adjusted time from the Hardware Clock. Note: currently this is not possible on most systems because <code>hwclock &#8211;systohc</code> is called at shutdown. </p>
<p> The Linux kernel&#8217;s timezone is set by <code>hwclock</code>. But don&#8217;t be misled &#8212; almost nobody cares what timezone the kernel thinks it is in. Instead, programs that care about the timezone (perhaps because they want to display a local time for you) almost always use a more traditional method of determining the timezone: They use the <code>TZ</code> environment variable or the <i>/etc/localtime</i> file, as explained in the man page for <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3). However, some programs and fringe parts of the Linux kernel such as filesystems use the kernel&#8217;s timezone value. An example is the vfat filesystem. If the kernel timezone value is wrong, the vfat filesystem will report and set the wrong timestamps on files. Another example is the kernel&#8217;s NTP &#8217;11 minute mode&#8217;. If the kernel&#8217;s timezone value and/or the <i>persistent_clock_is_local</i> variable are wrong, then the Hardware Clock will be set incorrectly by &#8217;11 minute mode&#8217;. See the discussion below, under <code>Automatic Hardware Clock Synchronization by the Kernel</code>. </p>
<p> <code>hwclock</code> sets the kernel&#8217;s timezone to the value indicated by <code>TZ</code> or <i>/etc/localtime</i> with the <code>&#8211;hctosys</code> or <code>&#8211;systz</code> functions. </p>
<p> The kernel&#8217;s timezone value actually consists of two parts: 1) a field tz_minuteswest indicating how many minutes local time (not adjusted for DST) lags behind UTC, and 2) a field tz_dsttime indicating the type of Daylight Savings Time (DST) convention that is in effect in the locality at the present time. This second field is not used under Linux and is always zero. See also <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2).</p>
<h3>Hardware Clock Access Methods</h3>
<p><code>hwclock</code> uses many different ways to get and set Hardware Clock values. The most normal way is to do I/O to the rtc device special file, which is presumed to be driven by the rtc device driver. Also, Linux systems using the rtc framework with udev, are capable of supporting multiple Hardware Clocks. This may bring about the need to override the default rtc device by specifying one with the <code>&#8211;rtc</code> option. </p>
<p> However, this method is not always available as older systems do not have an rtc driver. On these systems, the method of accessing the Hardware Clock depends on the system hardware. </p>
<p> On an ISA compatible system, <code>hwclock</code> can directly access the &quot;CMOS memory&quot; registers that constitute the clock, by doing I/O to Ports 0x70 and 0x71. It does this with actual I/O instructions and consequently can only do it if running with superuser effective userid. This method may be used by specifying the <code>&#8211;directisa</code> option. </p>
<p> This is a really poor method of accessing the clock, for all the reasons that userspace programs are generally not supposed to do direct I/O and disable interrupts. <code>hwclock</code> provides it for testing, troubleshooting, and because it may be the only method available on ISA systems which do not have a working rtc device driver.</p>
<h3>The Adjust Function</h3>
<p>The Hardware Clock is usually not very accurate. However, much of its inaccuracy is completely predictable &#8211; it gains or loses the same amount of time every day. This is called systematic drift. <code>hwclock</code>&#8216;s <code>&#8211;adjust</code> function lets you apply systematic drift corrections to the Hardware Clock. </p>
<p> It works like this: <code>hwclock</code> keeps a file, <i>/etc/adjtime</i>, that keeps some historical information. This is called the adjtime file. </p>
<p> Suppose you start with no adjtime file. You issue a <code>hwclock &#8211;set</code> command to set the Hardware Clock to the true current time. <code>hwclock</code> creates the adjtime file and records in it the current time as the last time the clock was calibrated. Five days later, the clock has gained 10 seconds, so you issue a <code>hwclock &#8211;set &#8211;update-drift</code> command to set it back 10 seconds. <code>hwclock</code> updates the adjtime file to show the current time as the last time the clock was calibrated, and records 2 seconds per day as the systematic drift rate. 24 hours go by, and then you issue a <code>hwclock &#8211;adjust</code> command. <code>hwclock</code> consults the adjtime file and sees that the clock gains 2 seconds per day when left alone and that it has been left alone for exactly one day. So it subtracts 2 seconds from the Hardware Clock. It then records the current time as the last time the clock was adjusted. Another 24 hours go by and you issue another <code>hwclock &#8211;adjust</code>. <code>hwclock</code> does the same thing: subtracts 2 seconds and updates the adjtime file with the current time as the last time the clock was adjusted. </p>
<p> When you use the <code>&#8211;update-drift</code> option with <code>&#8211;set</code> or <code>&#8211;systohc</code>, the systematic drift rate is (re)calculated by comparing the fully drift corrected current Hardware Clock time with the new set time, from that it derives the 24 hour drift rate based on the last calibrated timestamp from the adjtime file. This updated drift factor is then saved in <i>/etc/adjtime</i>. </p>
<p> A small amount of error creeps in when the Hardware Clock is set, so <code>&#8211;adjust</code> refrains from making any adjustment that is less than 1 second. Later on, when you request an adjustment again, the accumulated drift will be more than 1 second and <code>&#8211;adjust</code> will make the adjustment including any fractional amount. </p>
<p> <code>hwclock &#8211;hctosys</code> also uses the adjtime file data to compensate the value read from the Hardware Clock before using it to set the System Clock. It does not share the 1 second limitation of <code>&#8211;adjust</code>, and will correct sub-second drift values immediately. It does not change the Hardware Clock time nor the adjtime file. This may eliminate the need to use <code>&#8211;adjust</code>, unless something else on the system needs the Hardware Clock to be compensated.</p>
<h3>The Adjtime File</h3>
<p>While named for its historical purpose of controlling adjustments only, it actually contains other information used by <code>hwclock</code> from one invocation to the next. </p>
<p> The format of the adjtime file is, in ASCII: </p>
<p> Line 1: Three numbers, separated by blanks: 1) the systematic drift rate in seconds per day, floating point decimal; 2) the resulting number of seconds since 1969 UTC of most recent adjustment or calibration, decimal integer; 3) zero (for compatibility with <code><a href="/docs/linux/man/8-clock/">clock</a></code>(8)) as a floating point decimal. </p>
<p> Line 2: One number: the resulting number of seconds since 1969 UTC of most recent calibration. Zero if there has been no calibration yet or it is known that any previous calibration is moot (for example, because the Hardware Clock has been found, since that calibration, not to contain a valid time). This is a decimal integer. </p>
<p> Line 3: &quot;UTC&quot; or &quot;LOCAL&quot;. Tells whether the Hardware Clock is set to Coordinated Universal Time or local time. You can always override this value with options on the <code>hwclock</code> command line. </p>
<p> You can use an adjtime file that was previously used with the <code><a href="/docs/linux/man/8-clock/">clock</a></code>(8) program with <code>hwclock</code>.</p>
<h3>Automatic Hardware Clock Synchronization by the Kernel</h3>
<p>You should be aware of another way that the Hardware Clock is kept synchronized in some systems. The Linux kernel has a mode wherein it copies the System Time to the Hardware Clock every 11 minutes. This mode is a compile time option, so not all kernels will have this capability. This is a good mode to use when you are using something sophisticated like NTP to keep your System Clock synchronized. (NTP is a way to keep your System Time synchronized either to a time server somewhere on the network or to a radio clock hooked up to your system. See RFC 1305.) </p>
<p> If the kernel is compiled with the &#8217;11 minute mode&#8217; option it will be active when the kernel&#8217;s clock discipline is in a synchronized state. When in this state, bit 6 (the bit that is set in the mask 0x0040) of the kernel&#8217;s <i>time_status</i> variable is unset. This value is output as the &#8216;status&#8217; line of the <code>adjtimex &#8211;print</code> or <code>ntptime</code> commands. </p>
<p> It takes an outside influence, like the NTP daemon to put the kernel&#8217;s clock discipline into a synchronized state, and therefore turn on &#8217;11 minute mode&#8217;. It can be turned off by running anything that sets the System Clock the old fashioned way, including <code>hwclock &#8211;hctosys</code>. However, if the NTP daemon is still running, it will turn &#8217;11 minute mode&#8217; back on again the next time it synchronizes the System Clock. </p>
<p> If your system runs with &#8217;11 minute mode&#8217; on, it may need to use either <code>&#8211;hctosys</code> or <code>&#8211;systz</code> in a startup script, especially if the Hardware Clock is configured to use the local timescale. Unless the kernel is informed of what timescale the Hardware Clock is using, it may clobber it with the wrong one. The kernel uses UTC by default. </p>
<p> The first userspace command to set the System Clock informs the kernel what timescale the Hardware Clock is using. This happens via the <i>persistent_clock_is_local</i> kernel variable. If <code>&#8211;hctosys</code> or <code>&#8211;systz</code> is the first, it will set this variable according to the adjtime file or the appropriate command-line argument. Note that when using this capability and the Hardware Clock timescale configuration is changed, then a reboot is required to notify the kernel. </p>
<p> <code>hwclock &#8211;adjust</code> should not be used with NTP &#8217;11 minute mode&#8217;.</p>
<h3>ISA Hardware Clock Century value</h3>
<p>There is some sort of standard that defines CMOS memory Byte 50 on an ISA machine as an indicator of what century it is. <code>hwclock</code> does not use or set that byte because there are some machines that don&#8217;t define the byte that way, and it really isn&#8217;t necessary anyway, since the year-of-century does a good job of implying which century it is. </p>
<p> If you have a bona fide use for a CMOS century byte, contact the <code>hwclock</code> maintainer; an option may be appropriate. </p>
<p> Note that this section is only relevant when you are using the &quot;direct ISA&quot; method of accessing the Hardware Clock. ACPI provides a standard way to access century values, when they are supported by the hardware.</p>
<h2>Date-Time Configuration</h2>
<h3>Keeping Time without External Synchronization</h3>
<p>This discussion is based on the following conditions: </p>
<dl>
<dd>&bull; Nothing is running that alters the date-time clocks, such as NTP daemon or a cron job.&quot;</dl>
<dl>
<dd>&bull; The system timezone is configured for the correct local time. See below, under <code>POSIX vs &#8216;RIGHT&#8217;</code>.</dl>
<dl>
<dd>&bull; Early during startup the following are called, in this order: <code>adjtimex &#8211;tick</code> <i>value</i> <code>&#8211;frequency</code> <i>value</i> <code>hwclock &#8211;hctosys</code></dl>
<dl>
<dd>&bull; During shutdown the following is called: <code>hwclock &#8211;systohc</code> </p>
<dl>
<dd>&bull; Systems without <code>adjtimex</code> may use <code>ntptime</code>.</dl>
</dl>
<p> Whether maintaining precision time with NTP daemon or not, it makes sense to configure the system to keep reasonably good date-time on its own. </p>
<p> The first step in making that happen is having a clear understanding of the big picture. There are two completely separate hardware devices running at their own speed and drifting away from the &#8216;correct&#8217; time at their own rates. The methods and software for drift correction are different for each of them. However, most systems are configured to exchange values between these two clocks at startup and shutdown. Now the individual device&#8217;s time keeping errors are transferred back and forth between each other. Attempt to configure drift correction for only one of them, and the other&#8217;s drift will be overlaid upon it. </p>
<p> This problem can be avoided when configuring drift correction for the System Clock by simply not shutting down the machine. This, plus the fact that all of <code>hwclock</code>&#8216;s precision (including calculating drift factors) depends upon the System Clock&#8217;s rate being correct, means that configuration of the System Clock should be done first. </p>
<p> The System Clock drift is corrected with the <code><a href="/docs/linux/man/8-adjtimex/">adjtimex</a></code>(8) command&#8217;s <code>&#8211;tick</code> and <code>&#8211;frequency</code> options. These two work together: tick is the coarse adjustment and frequency is the fine adjustment. (For systems that do not have an <code>adjtimex</code> package, <code>ntptime -f</code> <i>ppm</i> may be used instead.) </p>
<p> Some Linux distributions attempt to automatically calculate the System Clock drift with <code>adjtimex</code>&#8216;s compare operation. Trying to correct one drifting clock by using another drifting clock as a reference is akin to a dog trying to catch its own tail. Success may happen eventually, but great effort and frustration will likely precede it. This automation may yield an improvement over no configuration, but expecting optimum results would be in error. A better choice for manual configuration would be <code>adjtimex</code>&#8216;s <code>&#8211;log</code> options. </p>
<p> It may be more effective to simply track the System Clock drift with <code>sntp</code>, or <code>date -Ins</code> and a precision timepiece, and then calculate the correction manually. </p>
<p> After setting the tick and frequency values, continue to test and refine the adjustments until the System Clock keeps good time. See <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2) for more information and the example demonstrating manual drift calculations. </p>
<p> Once the System Clock is ticking smoothly, move on to the Hardware Clock. </p>
<p> As a rule, cold drift will work best for most use cases. This should be true even for 24/7 machines whose normal downtime consists of a reboot. In that case the drift factor value makes little difference. But on the rare occasion that the machine is shut down for an extended period, then cold drift should yield better results. </p>
<p> <code>Steps to calculate cold drift:</code> </p>
<p> 1</p>
<dl>
<dd><code>Ensure that NTP daemon will not be launched at startup.</code></dl>
<p> 2</p>
<dl>
<dd>The <i>System Clock</i> time must be correct at shutdown!</dl>
<p> 3</p>
<dl>
<dd>Shut down the system.</dl>
<p> 4</p>
<dl>
<dd>Let an extended period pass without changing the Hardware Clock.</dl>
<p> 5</p>
<dl>
<dd>Start the system.</dl>
<p> 6</p>
<dl>
<dd>Immediately use <code>hwclock</code> to set the correct time, adding the <code>&#8211;update-drift</code> option.</dl>
<p> Note: if step 6 uses <code>&#8211;systohc</code>, then the System Clock must be set correctly (step 6a) just before doing so. </p>
<p> Having <code>hwclock</code> calculate the drift factor is a good starting point, but for optimal results it will likely need to be adjusted by directly editing the <i>/etc/adjtime</i> file. Continue to test and refine the drift factor until the Hardware Clock is corrected properly at startup. To check this, first make sure that the System Time is correct before shutdown and then use <code>sntp</code>, or <code>date -Ins</code> and a precision timepiece, immediately after startup.</p>
<h3>LOCAL vs UTC</h3>
<p>Keeping the Hardware Clock in a local timescale causes inconsistent daylight saving time results: </p>
<dl>
<dd>&bull; If Linux is running during a daylight saving time change, the time written to the Hardware Clock will be adjusted for the change.</dl>
<dl>
<dd>&bull; If Linux is NOT running during a daylight saving time change, the time read from the Hardware Clock will NOT be adjusted for the change.</dl>
<p> The Hardware Clock on an ISA compatible system keeps only a date and time, it has no concept of timezone nor daylight saving. Therefore, when <code>hwclock</code> is told that it is in local time, it assumes it is in the &#8216;correct&#8217; local time and makes no adjustments to the time read from it. </p>
<p> Linux handles daylight saving time changes transparently only when the Hardware Clock is kept in the UTC timescale. Doing so is made easy for system administrators as <code>hwclock</code> uses local time for its output and as the argument to the <code>&#8211;date</code> option. </p>
<p> POSIX systems, like Linux, are designed to have the System Clock operate in the UTC timescale. The Hardware Clock&#8217;s purpose is to initialize the System Clock, so also keeping it in UTC makes sense. </p>
<p> Linux does, however, attempt to accommodate the Hardware Clock being in the local timescale. This is primarily for dual-booting with older versions of MS Windows. From Windows 7 on, the RealTimeIsUniversal registry key is supposed to be working properly so that its Hardware Clock can be kept in UTC.</p>
<h3>POSIX vs &#8216;RIGHT&#8217;</h3>
<p>A discussion on date-time configuration would be incomplete without addressing timezones, this is mostly well covered by <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3). One area that seems to have no documentation is the &#8216;right&#8217; directory of the Time Zone Database, sometimes called tz or zoneinfo. </p>
<p> There are two separate databases in the zoneinfo system, posix and &#8216;right&#8217;. &#8216;Right&#8217; (now named zoneinfo-leaps) includes leap seconds and posix does not. To use the &#8216;right&#8217; database the System Clock must be set to (UTC + leap seconds), which is equivalent to (TAI &#8211; 10). This allows calculating the exact number of seconds between two dates that cross a leap second epoch. The System Clock is then converted to the correct civil time, including UTC, by using the &#8216;right&#8217; timezone files which subtract the leap seconds. Note: this configuration is considered experimental and is known to have issues. </p>
<p> To configure a system to use a particular database all of the files located in its directory must be copied to the root of <i>/usr/share/zoneinfo</i>. Files are never used directly from the posix or &#8216;right&#8217; subdirectories, e.g., TZ=&#8217;<i>right/Europe/Dublin</i>&#8216;. This habit was becoming so common that the upstream zoneinfo project restructured the system&#8217;s file tree by moving the posix and &#8216;right&#8217; subdirectories out of the zoneinfo directory and into sibling directories: </p>
<p> <i>/usr/share/zoneinfo</i>, <i>/usr/share/zoneinfo-posix</i>, <i>/usr/share/zoneinfo-leaps</i> </p>
<p> Unfortunately, some Linux distributions are changing it back to the old tree structure in their packages. So the problem of system administrators reaching into the &#8216;right&#8217; subdirectory persists. This causes the system timezone to be configured to include leap seconds while the zoneinfo database is still configured to exclude them. Then when an application such as a World Clock needs the South_Pole timezone file; or an email MTA, or <code>hwclock</code> needs the UTC timezone file; they fetch it from the root of <i>/usr/share/zoneinfo</i> , because that is what they are supposed to do. Those files exclude leap seconds, but the System Clock now includes them, causing an incorrect time conversion. </p>
<p> Attempting to mix and match files from these separate databases will not work, because they each require the System Clock to use a different timescale. The zoneinfo database must be configured to use either posix or &#8216;right&#8217;, as described above, or by assigning a database path to the <i>TZDIR</i> environment variable.</p>
<h2>Exit Status</h2>
<p>One of the following exit values will be returned: </p>
<p> <code>EXIT_SUCCESS</code> (&#8216;0&#8217; on POSIX systems)</p>
<dl>
<dd>Successful program execution.</dl>
<p> <code>EXIT_FAILURE</code> (&#8216;1&#8217; on POSIX systems)</p>
<dl>
<dd>The operation failed or the command syntax was not valid.</dl>
<h2>Environment</h2>
<p><code>TZ</code></p>
<dl>
<dd>If this variable is set its value takes precedence over the system configured timezone.</dl>
<p> <code>TZDIR</code></p>
<dl>
<dd>If this variable is set its value takes precedence over the system configured timezone database directory path.</dl>
<h2>Files</h2>
<p><i>/etc/adjtime</i></p>
<dl>
<dd>The configuration and state file for hwclock.</dl>
<p> <i>/etc/localtime</i></p>
<dl>
<dd>The system timezone file.</dl>
<p> <i>/usr/share/zoneinfo/</i></p>
<dl>
<dd>The system timezone database directory.</dl>
<p> Device files <code>hwclock</code> may try for Hardware Clock access: <i>/dev/rtc0</i> <i>/dev/rtc</i> <i>/dev/misc/rtc</i> <i>/dev/efirtc</i> <i>/dev/misc/efirtc</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/8-adjtimex/">adjtimex</a></code>(8), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="//www.systutorials.com/docs/linux/man/1p-crontab/">crontab</a></code>(1p), <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3)</p>
<h2>Authors</h2>
<p>Written by September 1996, based on work done on the <code><a href="/docs/linux/man/8-clock/">clock</a></code>(8) program by Charles Hedrick, Rob Hooft, and Harald Koenig. See the source code for complete history and credits.</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>hwclock</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
