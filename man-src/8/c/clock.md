---
title: "clock(8)"
name: "clock"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clock/"
description: "hwclock – query or set the hardware clock (RTC)"
---

<p>hwclock &#8211; query or set the hardware clock (RTC)</p>
<h2>Synopsis</h2>
<p><code>hwclock</code> [<i>function</i>] [<i>option</i>&#8230;] </p>
<h2>Description</h2>
<p><code>hwclock</code> is a tool for accessing the Hardware Clock. You can display the current time, set the Hardware Clock to a specified time, set the Hardware Clock from the System Time, or set the System Time from the Hardware Clock. You can also run <code>hwclock</code> periodically to add or subtract time from the Hardware Clock to compensate for systematic drift (where the clock consistently loses or gains time at a certain rate when left to run). </p>
<h2>Functions</h2>
<p>You need exactly one of the following options to tell <code>hwclock</code> what function to perform: </p>
<dl>
<dt><code>-r</code>,<code>&nbsp;<wbr>&#8211;show</code></p>
<dd>Read the Hardware Clock and print the time on standard output. The time shown is always in local time, even if you keep your Hardware Clock in Coordinated Universal Time. See the <code>&#8211;utc</code> option. Showing the Hardware Clock time is the default when no function is specified. </p>
<dt><code>&#8211;set</code></p>
<dd>Set the Hardware Clock to the time given by the <code>&#8211;date</code> option.</p>
<dt><code>-s</code>,<code>&nbsp;<wbr>&#8211;hctosys</code></p>
<dd>Set the System Time from the Hardware Clock. </p>
<p> Also set the kernel&#8217;s timezone value to the local timezone as indicated by the TZ environment variable and/or <i>/usr/share/zoneinfo</i>, as <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) would interpret them. The obsolete tz_dsttime field of the kernel&#8217;s timezone value is set to DST_NONE. (For details on what this field used to mean, see <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2).) </p>
<p> This is a good option to use in one of the system startup scripts.</p>
<dt><code>-w</code>,<code>&nbsp;<wbr>&#8211;systohc</code></p>
<dd>Set the Hardware Clock to the current System Time.</p>
<dt><code>&#8211;systz</code></p>
<dd>Set the kernel&#8217;s timezone and reset the System Time based on the current timezone. </p>
<p> The system time is only reset on the first call after boot. </p>
<p> The local timezone is taken to be what is indicated by the TZ environment variable and/or <i>/usr/share/zoneinfo</i>, as <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) would interpret them. The obsolete tz_dsttime field of the kernel&#8217;s timezone value is set to DST_NONE. (For details on what this field used to mean, see <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2).) </p>
<p> This is an alternate option to <code>&#8211;hctosys</code> that does not read the hardware clock, and may be used in system startup scripts for recent 2.6 kernels where you know the System Time contains the Hardware Clock time. If the Hardware Clock is already in UTC, it is not reset.</p>
<dt><code>&#8211;adjust</code></p>
<dd>Add or subtract time from the Hardware Clock to account for systematic drift since the last time the clock was set or adjusted. See discussion below.</p>
<dt><code>&#8211;getepoch</code></p>
<dd>Print the kernel&#8217;s Hardware Clock epoch value to standard output. This is the number of years into AD to which a zero year value in the Hardware Clock refers. For example, if you are using the convention that the year counter in your Hardware Clock contains the number of full years since 1952, then the kernel&#8217;s Hardware Clock epoch value must be 1952. </p>
<p> This epoch value is used whenever <code>hwclock</code> reads or sets the Hardware Clock.</p>
<dt><code>&#8211;setepoch</code></p>
<dd>Set the kernel&#8217;s Hardware Clock epoch value to the value specified by the <code>&#8211;epoch</code> option. See the <code>&#8211;getepoch</code> option for details. </p>
<dt><code>&#8211;predict</code></p>
<dd>Predict what the RTC will read at time given by the <code>&#8211;date</code> option based on the adjtime file. This is useful for example if you need to set an RTC wakeup time to distant future and want to account for the RTC drift.</p>
<dt><code>-c</code>,<code>&nbsp;<wbr>&#8211;compare</code></p>
<dd>Periodically compare the Hardware Clock to the System Time and output the difference every 10 seconds. This will also print the frequency offset and tick.</p>
<dt><code>-h</code>,<code>&nbsp;<wbr>&#8211;help</code></p>
<dd>Display a help text and exit.</p>
<dt><code>-V</code>,<code>&nbsp;<wbr>&#8211;version</code></p>
<dd>Display the version of <code>hwclock</code> and exit. </p>
</dl>
<h2>Options</h2>
<p>The first two options apply to just a few specific functions, the others apply to most functions.</p>
<dl>
<dt><code>&#8211;date=</code><i>date_string</i></p>
<dd>You need this option if you specify the <code>&#8211;set</code> or <code>&#8211;predict</code> functions, otherwise it is ignored. It specifies the time to which to set the Hardware Clock, or the time for which to predict the Hardware Clock reading. The value of this option is an argument to the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) program. For example: </p>
<p> <code> hwclock &#8211;set &#8211;date=2011-08-14 16:45:05</code> </p>
<p> The argument must be in local time, even if you keep your Hardware Clock in Coordinated Universal time. See the <code>&#8211;utc</code> option. </p>
<dt><code>&#8211;epoch=</code><i>year</i></p>
<dd>Specifies the year which is the beginning of the Hardware Clock&#8217;s epoch, that is the number of years into AD to which a zero value in the Hardware Clock&#8217;s year counter refers. It is used together with the <code>&#8211;setepoch</code> option to set the kernel&#8217;s idea of the epoch of the Hardware Clock, or otherwise to specify the epoch for use with direct ISA access. </p>
<p> For example, on a Digital Unix machine: </p>
<p> <code> hwclock &#8211;setepoch &#8211;epoch=1952</code> </p>
<dt><code>-u</code>,<code>&nbsp;<wbr>&#8211;utc</code></p>
<dd>
<dt><code>&#8211;localtime</code></p>
<dd>Indicates that the Hardware Clock is kept in Coordinated Universal Time or local time, respectively. It is your choice whether to keep your clock in UTC or local time, but nothing in the clock tells which you&#8217;ve chosen. So this option is how you give that information to <code>hwclock</code>. </p>
<p> If you specify the wrong one of these options (or specify neither and take a wrong default), both setting and querying of the Hardware Clock will be messed up. </p>
<p> If you specify neither <code>&#8211;utc</code> nor <code>&#8211;localtime</code>, the default is whichever was specified the last time <code>hwclock</code> was used to set the clock (i.e. <code>hwclock</code> was successfully run with the <code>&#8211;set</code>, <code>&#8211;systohc</code>, or <code>&#8211;adjust</code> options), as recorded in the adjtime file. If the adjtime file doesn&#8217;t exist, the default is UTC time. </p>
<dt><code>&#8211;noadjfile</code></p>
<dd>Disables the facilities provided by <i>/etc/adjtime</i>. <code>hwclock</code> will not read nor write to that file with this option. Either <code>&#8211;utc</code> or <code>&#8211;localtime</code> must be specified when using this option. </p>
<dt><code>&#8211;adjfile=</code><i>filename</i></p>
<dd>Overrides the default /etc/adjtime. </p>
<dt><code>-f</code>,<code>&nbsp;<wbr>&#8211;rtc=</code><i>filename</i></p>
<dd>Overrides the default /dev file name, which is <i>/dev/rtc</i> on many platforms but may be <i>/dev/rtc0</i>, <i>/dev/rtc1</i>, and so on. </p>
<dt><code>&#8211;directisa</code></p>
<dd>This option is meaningful only on an ISA machine or an Alpha (which implements enough of ISA to be, roughly speaking, an ISA machine for <code>hwclock</code>&#8216;s purposes). For other machines, it has no effect. This option tells <code>hwclock</code> to use explicit I/O instructions to access the Hardware Clock. Without this option, <code>hwclock</code> will try to use the /dev/rtc device (which it assumes to be driven by the RTC device driver). If it is unable to open the device (for reading), it will use the explicit I/O instructions anyway. </p>
<dt><code>&#8211;badyear</code></p>
<dd>Indicates that the Hardware Clock is incapable of storing years outside the range 1994-1999. There is a problem in some BIOSes (almost all Award BIOSes made between 4/26/94 and 5/31/95) wherein they are unable to deal with years after 1999. If one attempts to set the year-of-century value to something less than 94 (or 95 in some cases), the value that actually gets set is 94 (or 95). Thus, if you have one of these machines, <code>hwclock</code> cannot set the year after 1999 and cannot use the value of the clock as the true time in the normal way. </p>
<p> To compensate for this (without your getting a BIOS update, which would definitely be preferable), always use <code>&#8211;badyear</code> if you have one of these machines. When <code>hwclock</code> knows it&#8217;s working with a brain-damaged clock, it ignores the year part of the Hardware Clock value and instead tries to guess the year based on the last calibrated date in the adjtime file, by assuming that date is within the past year. For this to work, you had better do a <code>hwclock &#8211;set</code> or <code>hwclock &#8211;systohc</code> at least once a year! </p>
<p> Though <code>hwclock</code> ignores the year value when it reads the Hardware Clock, it sets the year value when it sets the clock. It sets it to 1995, 1996, 1997, or 1998, whichever one has the same position in the leap year cycle as the true year. That way, the Hardware Clock inserts leap days where they belong. Again, if you let the Hardware Clock run for more than a year without setting it, this scheme could be defeated and you could end up losing a day. </p>
<p> <code>hwclock</code> warns you that you probably need <code>&#8211;badyear</code> whenever it finds your Hardware Clock set to 1994 or 1995. </p>
<dt><code>&#8211;srm</code></p>
<dd>This option is equivalent to <code>&#8211;epoch=1900</code> and is used to specify the most common epoch on Alphas with SRM console.</p>
<dt><code>&#8211;arc</code></p>
<dd>This option is equivalent to <code>&#8211;epoch=1980</code> and is used to specify the most common epoch on Alphas with ARC console (but Ruffians have epoch 1900).</p>
<dt><code>&#8211;jensen</code></p>
<dd>
<dt><code>&#8211;funky-toy</code></p>
<dd>These two options specify what kind of Alpha machine you have. They are invalid if you don&#8217;t have an Alpha and are usually unnecessary if you do, because <code>hwclock</code> should be able to determine by itself what it&#8217;s running on, at least when <i>/proc</i> is mounted. (If you find you need one of these options to make <code>hwclock</code> work, contact the maintainer to see if the program can be improved to detect your system automatically. Output of `hwclock &#8211;debug&#8217; and `cat /proc/cpuinfo&#8217; may be of interest.) </p>
<p> Option <code>&#8211;jensen</code> means you are running on a Jensen model. And <code>&#8211;funky-toy</code> means that on your machine one has to use the UF bit instead of the UIP bit in the Hardware Clock to detect a time transition. &quot;Toy&quot; in the option name refers to the Time Of Year facility of the machine. </p>
<dt><code>&#8211;test</code></p>
<dd>Do everything except actually updating the Hardware Clock or anything else. This is useful, especially in conjunction with <code>&#8211;debug</code>, in learning about <code>hwclock</code>.</p>
<dt><code>&#8211;debug</code></p>
<dd>Display a lot of information about what <code>hwclock</code> is doing internally. Some of its function is complex and this output can help you understand how the program works. </p>
</dl>
<h2>Notes</h2>
<h2>Clocks in a Linux System</h2>
<p>There are two main clocks in a Linux system: </p>
<p> <code>The Hardware Clock:</code> This is a clock that runs independently of any control program running in the CPU and even when the machine is powered off. </p>
<p> On an ISA system, this clock is specified as part of the ISA standard. The control program can read or set this clock to a whole second, but the control program can also detect the edges of the 1 second clock ticks, so the clock actually has virtually infinite precision. </p>
<p> This clock is commonly called the hardware clock, the real time clock, the RTC, the BIOS clock, and the CMOS clock. Hardware Clock, in its capitalized form, was coined for use by <code>hwclock</code> because all of the other names are inappropriate to the point of being misleading. </p>
<p> So for example, some non-ISA systems have a few real time clocks with only one of them having its own power domain. A very low power external I2C or SPI clock chip might be used with a backup battery as the hardware clock to initialize a more functional integrated real-time clock which is used for most other purposes. </p>
<p> <code>The System Time:</code> This is the time kept by a clock inside the Linux kernel and driven by a timer interrupt. (On an ISA machine, the timer interrupt is part of the ISA standard). It has meaning only while Linux is running on the machine. The System Time is the number of seconds since 00:00:00 January 1, 1970 UTC (or more succinctly, the number of seconds since 1969). The System Time is not an integer, though. It has virtually infinite precision. </p>
<p> The System Time is the time that matters. The Hardware Clock&#8217;s basic purpose in a Linux system is to keep time when Linux is not running. You initialize the System Time to the time from the Hardware Clock when Linux starts up, and then never use the Hardware Clock again. Note that in DOS, for which ISA was designed, the Hardware Clock is the only real time clock. </p>
<p> It is important that the System Time not have any discontinuities such as would happen if you used the <code><a href="//www.systutorials.com/docs/linux/man/1L-date/">date</a></code>(1L) program to set it while the system is running. You can, however, do whatever you want to the Hardware Clock while the system is running, and the next time Linux starts up, it will do so with the adjusted time from the Hardware Clock. </p>
<p> A Linux kernel maintains a concept of a local timezone for the system. But don&#8217;t be misled &#8212; almost nobody cares what timezone the kernel thinks it is in. Instead, programs that care about the timezone (perhaps because they want to display a local time for you) almost always use a more traditional method of determining the timezone: They use the TZ environment variable and/or the <i>/usr/share/zoneinfo</i> directory, as explained in the man page for <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3). However, some programs and fringe parts of the Linux kernel such as filesystems use the kernel timezone value. An example is the vfat filesystem. If the kernel timezone value is wrong, the vfat filesystem will report and set the wrong timestamps on files. </p>
<p> <code>hwclock</code> sets the kernel timezone to the value indicated by TZ and/or <i>/usr/share/zoneinfo</i> when you set the System Time using the <code>&#8211;hctosys</code> option. </p>
<p> The timezone value actually consists of two parts: 1) a field tz_minuteswest indicating how many minutes local time (not adjusted for DST) lags behind UTC, and 2) a field tz_dsttime indicating the type of Daylight Savings Time (DST) convention that is in effect in the locality at the present time. This second field is not used under Linux and is always zero. (See also <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2).)</p>
<h2>Users access and setuid</h2>
<p>Sometimes, you need to install <code>hwclock</code> setuid root. If you want users other than the superuser to be able to display the clock value using the direct ISA I/O method, install it setuid root. If you have the /dev/rtc interface on your system or are on a non-ISA system, there&#8217;s probably no need for users to use the direct ISA I/O method, so don&#8217;t bother. </p>
<p> In any case, hwclock will not allow you to set anything unless you have the superuser real uid. (This is restriction is not necessary if you haven&#8217;t installed setuid root, but it&#8217;s there for now).</p>
<h2>How hwclock Accesses the Hardware Clock</h2>
<p><code>hwclock</code> uses many different ways to get and set Hardware Clock values. The most normal way is to do I/O to the device special file /dev/rtc, which is presumed to be driven by the rtc device driver. However, this method is not always available. For one thing, the rtc driver is a relatively recent addition to Linux. Older systems don&#8217;t have it. Also, though there are versions of the rtc driver that work on DEC Alphas, there appear to be plenty of Alphas on which the rtc driver does not work (a common symptom is hwclock hanging). Moreover, recent Linux systems have more generic support for RTCs, even systems that have more than one, so you might need to override the default by specifying <i>/dev/rtc0</i> or <i>/dev/rtc1</i> instead. </p>
<p> On older systems, the method of accessing the Hardware Clock depends on the system hardware. </p>
<p> On an ISA system, <code>hwclock</code> can directly access the &quot;CMOS memory&quot; registers that constitute the clock, by doing I/O to Ports 0x70 and 0x71. It does this with actual I/O instructions and consequently can only do it if running with superuser effective userid. (In the case of a Jensen Alpha, there is no way for <code>hwclock</code> to execute those I/O instructions, and so it uses instead the /dev/port device special file, which provides almost as low-level an interface to the I/O subsystem). </p>
<p> This is a really poor method of accessing the clock, for all the reasons that user space programs are generally not supposed to do direct I/O and disable interrupts. Hwclock provides it because it is the only method available on ISA and Alpha systems which don&#8217;t have working rtc device drivers available. </p>
<p> On an m68k system, <code>hwclock</code> can access the clock via the console driver, via the device special file /dev/tty1. </p>
<p> <code>hwclock</code> tries to use /dev/rtc. If it is compiled for a kernel that doesn&#8217;t have that function or it is unable to open /dev/rtc (or the alternative special file you&#8217;ve defined on the command line) <code>hwclock</code> will fall back to another method, if available. On an ISA or Alpha machine, you can force <code>hwclock</code> to use the direct manipulation of the CMOS registers without even trying <i>/dev/rtc</i> by specifying the <code>&#8211;directisa</code> option.</p>
<h2>The Adjust Function</h2>
<p>The Hardware Clock is usually not very accurate. However, much of its inaccuracy is completely predictable &#8211; it gains or loses the same amount of time every day. This is called systematic drift. <code>hwclock</code>&#8216;s &quot;adjust&quot; function lets you make systematic corrections to correct the systematic drift. </p>
<p> It works like this: <code>hwclock</code> keeps a file, <i>/etc/adjtime</i>, that keeps some historical information. This is called the adjtime file. </p>
<p> Suppose you start with no adjtime file. You issue a <i>hwclock &#8211;set</i> command to set the Hardware Clock to the true current time. <code>Hwclock</code> creates the adjtime file and records in it the current time as the last time the clock was calibrated. 5 days later, the clock has gained 10 seconds, so you issue another <i>hwclock &#8211;set</i> command to set it back 10 seconds. <code>Hwclock</code> updates the adjtime file to show the current time as the last time the clock was calibrated, and records 2 seconds per day as the systematic drift rate. 24 hours go by, and then you issue a <i>hwclock &#8211;adjust</i> command. <code>Hwclock</code> consults the adjtime file and sees that the clock gains 2 seconds per day when left alone and that it has been left alone for exactly one day. So it subtracts 2 seconds from the Hardware Clock. It then records the current time as the last time the clock was adjusted. Another 24 hours goes by and you issue another <i>hwclock &#8211;adjust</i>. <code>Hwclock</code> does the same thing: subtracts 2 seconds and updates the adjtime file with the current time as the last time the clock was adjusted. </p>
<p> Every time you calibrate (set) the clock (using <i>&#8211;set</i> or <i>&#8211;systohc</i>), <code>hwclock</code> recalculates the systematic drift rate based on how long it has been since the last calibration, how long it has been since the last adjustment, what drift rate was assumed in any intervening adjustments, and the amount by which the clock is presently off. </p>
<p> A small amount of error creeps in any time <code>hwclock</code> sets the clock, so it refrains from making an adjustment that would be less than 1 second. Later on, when you request an adjustment again, the accumulated drift will be more than a second and <code>hwclock</code> will do the adjustment then. </p>
<p> It is good to do a <i>hwclock &#8211;adjust</i> just before the <i>hwclock &#8211;hctosys</i> at system startup time, and maybe periodically while the system is running via cron. </p>
<p> The adjtime file, while named for its historical purpose of controlling adjustments only, actually contains other information for use by hwclock in remembering information from one invocation to the next. </p>
<p> The format of the adjtime file is, in ASCII: </p>
<p> Line 1: 3 numbers, separated by blanks: 1) systematic drift rate in seconds per day, floating point decimal; 2) Resulting number of seconds since 1969 UTC of most recent adjustment or calibration, decimal integer; 3) zero (for compatibility with <code><a href="/docs/linux/man/8-clock/">clock</a></code>(8)) as a decimal integer. </p>
<p> Line 2: 1 number: Resulting number of seconds since 1969 UTC of most recent calibration. Zero if there has been no calibration yet or it is known that any previous calibration is moot (for example, because the Hardware Clock has been found, since that calibration, not to contain a valid time). This is a decimal integer. </p>
<p> Line 3: &quot;UTC&quot; or &quot;LOCAL&quot;. Tells whether the Hardware Clock is set to Coordinated Universal Time or local time. You can always override this value with options on the <code>hwclock</code> command line. </p>
<p> You can use an adjtime file that was previously used with the <code><a href="/docs/linux/man/8-clock/">clock</a></code>(8) program with <code>hwclock</code>.</p>
<h2>Automatic Hardware Clock Synchronization By the Kernel</h2>
<p>You should be aware of another way that the Hardware Clock is kept synchronized in some systems. The Linux kernel has a mode wherein it copies the System Time to the Hardware Clock every 11 minutes. This is a good mode to use when you are using something sophisticated like ntp to keep your System Time synchronized. (ntp is a way to keep your System Time synchronized either to a time server somewhere on the network or to a radio clock hooked up to your system. See RFC 1305). </p>
<p> This mode (we&#8217;ll call it &quot;11 minute mode&quot;) is off until something turns it on. The ntp daemon xntpd is one thing that turns it on. You can turn it off by running anything, including <i>hwclock &#8211;hctosys</i>, that sets the System Time the old fashioned way. </p>
<p> If your system runs with 11 minute mode on, don&#8217;t use <i>hwclock &#8211;adjust</i> or <i>hwclock &#8211;hctosys</i>. You&#8217;ll just make a mess. It is acceptable to use a <i>hwclock &#8211;hctosys</i> at startup time to get a reasonable System Time until your system is able to set the System Time from the external source and start 11 minute mode.</p>
<h2>ISA Hardware Clock Century value</h2>
<p>There is some sort of standard that defines CMOS memory Byte 50 on an ISA machine as an indicator of what century it is. <code>hwclock</code> does not use or set that byte because there are some machines that don&#8217;t define the byte that way, and it really isn&#8217;t necessary anyway, since the year-of-century does a good job of implying which century it is. </p>
<p> If you have a bona fide use for a CMOS century byte, contact the <code>hwclock</code> maintainer; an option may be appropriate. </p>
<p> Note that this section is only relevant when you are using the &quot;direct ISA&quot; method of accessing the Hardware Clock. ACPI provides a standard way to access century values, when they are supported by the hardware.</p>
<h2>Environment Variables</h2>
<p><i>TZ</i></p>
<h2>Files</h2>
<p><i>/etc/adjtime</i> <i>/usr/share/zoneinfo/</i> (<i>/usr/lib/zoneinfo</i> on old systems) <i>/dev/rtc</i> <i>/dev/rtc0</i> <i>/dev/port</i> <i>/dev/tty1</i> <i>/proc/cpuinfo</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1), <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) </p>
<h2>Authors</h2>
<p>Written by Bryan Henderson, September 1996 (bryanh [at] giraffe-data.com), based on work done on the <i>clock</i> program by Charles Hedrick, Rob Hooft, and Harald Koenig. See the source code for complete history and credits.</p>
<h2>Availability</h2>
<p>The hwclock command is part of the util-linux package and is available from <a href="ftp://ftp.kernel.org/pub/linux/utils/util-linux/.">ftp://ftp.kernel.org/pub/linux/utils/util-linux/.</a></p>
