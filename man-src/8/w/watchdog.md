---
title: "watchdog(8)"
name: "watchdog"
section: "8"
letter: "w"
url: "/docs/linux/man/8-watchdog/"
description: "watchdog – a software watchdog daemon"
---

<p>watchdog &#8211; a software watchdog daemon</p>
<h2>Synopsis</h2>
<p><code>watchdog</code> [<code>-F</code>|<code>&#8211;foreground</code>] [<code>-f</code>|<code>&#8211;force</code>] [<code>-c</code> <i>filename</i>|<code>&#8211;config-file</code> <i>filename</i>] [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-s</code>|<code>&#8211;sync</code>] [<code>-b</code>|<code>&#8211;softboot</code>] [<code>-q</code>|<code>&#8211;no-action</code>]</p>
<h2>Description</h2>
<p>The Linux kernel can reset the system if serious problems are detected. This can be implemented via special watchdog hardware, or via a slightly less reliable software-only watchdog inside the kernel. Either way, there needs to be a daemon that tells the kernel the system is working fine. If the daemon stops doing that, the system is reset. </p>
<p> <code>watchdog </code> is such a daemon. It opens <i>/dev/watchdog</i>, and keeps writing to it often enough to keep the kernel from resetting, at least once per minute. Each write delays the reboot time another minute. After a minute of inactivity the watchdog hardware will cause the reset. In the case of the software watchdog the ability to reboot will depend on the state of the machines and interrupts. </p>
<p> The watchdog daemon can be stopped without causing a reboot if the device <i>/dev/watchdog</i> is closed correctly, unless your kernel is compiled with the <i>CONFIG_WATCHDOG_NOWAYOUT</i> option enabled.</p>
<h2>Tests</h2>
<p>The watchdog daemon does several tests to check the system status:</p>
<dl>
<dt>&bull;</p>
<dd>Is the process table full?</p>
<dt>&bull;</p>
<dd>Is there enough free memory?</p>
<dt>&bull;</p>
<dd>Are some files accessible?</p>
<dt>&bull;</p>
<dd>Have some files changed within a given interval?</p>
<dt>&bull;</p>
<dd>Is the average work load too high?</p>
<dt>&bull;</p>
<dd>Has a file table overflow occurred?</p>
<dt>&bull;</p>
<dd>Is a process still running? The process is specified by a pid file.</p>
<dt>&bull;</p>
<dd>Do some IP addresses answer to ping?</p>
<dt>&bull;</p>
<dd>Do network interfaces receive traffic?</p>
<dt>&bull;</p>
<dd>Is the temperature too high? (Temperature data not always available.)</p>
<dt>&bull;</p>
<dd>Execute a user defined command to do arbitrary tests.</p>
<dt>&bull;</p>
<dd>Execute one or more test/repair commands found in /etc/watchdog.d. These commands are called with the argument <code>test</code> or <code>repair</code>.</dl>
<p> If any of these checks fail watchdog will cause a shutdown. Should any of these tests except the user defined binary last longer than one minute the machine will be rebooted, too.</p>
<h2>Options</h2>
<p>Available command line options are the following:</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Set verbose mode. Only implemented if compiled with <i>SYSLOG </i> feature. This mode will log each several infos in <i>LOG_DAEMON </i> with priority <i>LOG_INFO.</i> This is useful if you want to see exactly what happened until the watchdog rebooted the system. Currently it logs the temperature (if available), the load average, the change date of the files it checks and how often it went to sleep.</p>
<dt><code>-s</code>, <code>&#8211;sync</code></p>
<dd>Try to synchronize the filesystem every time the process is awake. Note that the system is rebooted if for any reason the synchronizing lasts longer than a minute.</p>
<dt><code>-b</code>, <code>&#8211;softboot</code></p>
<dd>Soft-boot the system if an error occurs during the main loop, e.g. if a given file is not accessible via the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) call. Note that this does not apply to the opening of <i>/dev/watchdog </i> and <i>/proc/loadavg</i>, which are opened before the main loop starts.</p>
<dt><code>-F</code>, <code>&#8211;foreground</code></p>
<dd>Run in foreground mode, useful for running under systemd (for example).</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Force the usage of the interval given or the maximal load average given in the config file.</p>
<dt><code>-c</code> <i>config-file</i>, <code>&#8211;config-file</code> <i>config-file</i></p>
<dd>Use <i>config-file</i> as the configuration file instead of the default <i>/etc/watchdog.conf</i>.</p>
<dt><code>-q</code>, <code>&#8211;no-action</code></p>
<dd>Do not reboot or halt the machine. This is for testing purposes. All checks are executed and the results are logged as usual, but no action is taken. Also your hardware card or the kernel software watchdog driver is not enabled. Temperature checking is also disabled since this triggers the hardware watchdog on some cards.</dl>
<h2>Function</h2>
<p>After <code>watchdog </code> starts, it puts itself into the background and then tries all checks specified in its configuration file in turn. Between each two tests it will write to the kernel device to prevent a reset. After finishing all tests watchdog goes to sleep for some time. The kernel drivers expects a write to the watchdog device every minute. Otherwise the system will be reset. As a default <code>watchdog </code> will sleep for only 1 second so it triggers the device early enough. </p>
<p> Under high system load <code>watchdog </code> might be swapped out of memory and may fail to make it back in in time. Under these circumstances the Linux kernel will reset the machine. To make sure you won&#8217;t get unnecessary reboots make sure you have the variable <i>realtime</i> set to <i>yes </i> in the configuration file <i>watchdog.conf</i>. This adds real time support to <code>watchdog</code>: it will lock itself into memory and there should be no problem even under the highest of loads. </p>
<p> On system running out of memory the kernel will try to free enough memory by killing process. The <code>watchdog</code> daemon itself is exempted from this so-called out-of-memory killer. </p>
<p> Also you can specify a maximal allowed load average. Once this load average is reached the system is rebooted. You may specify maximal load averages for 1 minute, 5 minutes or 15 minutes. The default values is to disable this test. Be careful not to set this parameter too low. To set a value less then the predefined minimal value of 2, you have to use the <code>-f </code> option. </p>
<p> You can also specify a minimal amount of virtual memory you want to have available as free. As soon as more virtual memory is used action is taken by <code>watchdog</code>. Note, however, that watchdog does not distinguish between different types of memory usage. It just checks for free virtual memory. </p>
<p> If you have a watchdog card with temperature sensor you can specify the maximal allowed temperature. Once this temperature is reached the system is halted. The default value is 120. There is no unit conversion so make sure you use the same unit as your hardware. <code>watchdog </code> will issue warnings once the temperature increases 90%, 95% and 98% of this temperature. </p>
<p> When using file mode <code>watchdog </code> will try to <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) the given files. Errors returned by stat will <code>not</code> cause a reboot. For a reboot the stat call has to last at least one minute. This may happen if the file is located on an NFS mounted filesystem. If your system relies on an NFS mounted filesystem you might try this option. However, in such a case the <i>sync </i> option may not work if the NFS server is not answering. </p>
<p> <code>watchdog</code> can read the pid from a pid file and see whether the process still exists. If not, action is taken by <code>watchdog</code>. So you can for instance restart the server from your <i>repair-binary</i>. See the Systemd section below for additinal information. </p>
<p> <code>watchdog </code> will try periodically to fork itself to see whether the process table is full. This process will leave a zombie process until watchdog wakes up again and catches it; this is harmless, don&#8217;t worry about it. </p>
<p> In ping mode <code>watchdog </code> tries to ping the given IP addresses. These addresses do not have to be a single machine. It is possible to ping to a broadcast address instead to see if at least one machine in a subnet is still living. </p>
<p> <code>Do not use this broadcast ping unless your MIS person a) knows about it and</code> <code>b) has given you explicit permission to use it!</code> </p>
<p> <code>watchdog </code> will send out three ping packages and wait up to &lt;interval&gt; seconds for the reply with &lt;interval&gt; being the time it goes to sleep between two times triggering the watchdog device. Thus a unreachable network will not cause a hard reset but a soft reboot. </p>
<p> You can also test passively for an unreachable network by just monitoring a given interface for traffic. If no traffic arrives the network is considered unreachable causing a soft reboot or action from the repair binary. </p>
<p> To start the watchdog when network is available see the Systemd section below. </p>
<p> <code>watchdog can run an external command for user-defined tests. A return code</code> not equal 0 means an error occured and watchdog should react. If the external command is killed by an uncaught signal this is considered an error by watchdog too. The command may take longer than the time slice defined for the kernel device without a problem. However, error messages are generated into the syslog facility. If you have enabled softboot on error the machine will be rebooted if the binary doesn&#8217;t exit in half the time <code>watchdog </code> sleeps between two tries triggering the kernel device. </p>
<p> If you specify a repair binary it will be started instead of shutting down the system. If this binary is not able to fix the problem <code>watchdog </code> will still cause a reboot afterwards. </p>
<p> If the machine is halted an email is sent to notify a human that the machine is going down. Starting with version 4.4 <code>watchdog </code> will also notify the human in charge if the machine is rebooted.</p>
<h2>Soft Reboot</h2>
<p>A soft reboot (i.e. controlled shutdown and reboot) is initiated for every error that is found. Since there might be no more processes available, watchdog does it all by himself. That means:</p>
<dl>
<dt>1.</p>
<dd>Kill all processes with SIGTERM.</p>
<dt>2.</p>
<dd>After a short pause kill all remaining processes with SIGKILL.</p>
<dt>3.</p>
<dd>Record a shutdown entry in wtmp.</p>
<dt>4.</p>
<dd>Save the random seed from <i>/dev/urandom</i>. If the device is non-existant or there is no filename for saving this step is skipped.</p>
<dt>5.</p>
<dd>Turn off accounting.</p>
<dt>6.</p>
<dd>Turn off quota and swap.</p>
<dt>7.</p>
<dd>Unmount all partitions except the root partition.</p>
<dt>8.</p>
<dd>Remount the root partition read-only.</p>
<dt>9.</p>
<dd>Shut down all network interfaces.</p>
<dt>10.</p>
<dd>Finally reboot.</dl>
<h2>Check Binary</h2>
<p>If the return code of the check binary is not zero <code>watchdog </code> will assume an error and reboot the system. Be careful with this if you are using the real-time properties of watchdog since <code>watchdog </code> will wait for the return of this binary before proceeding. An positive exit code is interpreted as an system error code (see <i>errno.h </i> for details). Negative values are special to <code>watchdog</code>:</p>
<dl>
<dt>-1</p>
<dd>Reboot the system. This is not exactly an error message but a command to <code>watchdog</code>. If the return code is -1 <code>watchdog </code> will not try to run a shutdown script instead.</p>
<dt>-2</p>
<dd>Reset the system. This is not exactly an error message but a command to <code>watchdog</code>. If the return code is -2 <code>watchdog will simply refuse to write the</code> kernel device again.</p>
<dt>-3</p>
<dd>Maximum load average exceeded.</p>
<dt>-4</p>
<dd>The temperature inside is too high.</p>
<dt>-5</p>
<dd><i>/proc/loadavg </i> contains no (or not enough) data.</p>
<dt>-6</p>
<dd>The given file was not changed in the given interval.</p>
<dt>-7</p>
<dd><i>/proc/meminfo </i> contains invalid data.</p>
<dt>-8</p>
<dd>Child process was killed by a signal.</p>
<dt>-9</p>
<dd>Child process did not return in time.</p>
<dt>-10</p>
<dd>Free for personal use.</dl>
<p> With enforcing SELinux policy please use the /usr/libexec/watchdog/scripts/ for your test-binary configuration.</p>
<h2>Repair Binary</h2>
<p>The repair binary is started with one parameter: the error number that caused <code>watchdog </code> to initiate the boot process. After trying to repair the system the binary should exit with 0 if the system was successfully repaired and thus there is no need to boot anymore. A return value not equal 0 tells <code>watchdog </code> to reboot. The return code of the repair binary should be the error number of the error causing <code>watchdog </code> to reboot. Be careful with this if you are using the real-time properties since <code>watchdog </code> will wait for the return of this binary before proceeding. </p>
<p> With enforcing SELinux policy please use the /usr/libexec/watchdog/scripts/ for your repair-binary configuration.</p>
<h2>Test Directory</h2>
<p>Executables placed in the test directory are discovered by watchdog on startup and are automatically executed. They are bounded time-wise by the test-timeout directive in watchdog.conf. </p>
<p> These executables are called with either &quot;test&quot; as the first argument (if a test is being performed) or &quot;repair&quot; as the first argument (if a repair for a previously-failed &quot;test&quot; operation on is being performed). </p>
<p> The as with test binaries and repair binaries, expected exit codes for a successful test or repair operation is always zero. </p>
<p> If an executable&#8217;s test operation fails, the same executable is automatically called with the &quot;repair&quot; argument as well as the return code of the previously-failed test operation. </p>
<p> For example, if the following execution returns 42: </p>
<p>&nbsp;<wbr>/etc/watchdog.d/my-test test </p>
<p> The watchdog daemon will attempt to repair the problem by calling: </p>
<p>&nbsp;<wbr>/etc/watchdog.d/my-test repair 42 </p>
<p> This enables administrators and application developers to make intelligent test/repair commands. If the &quot;repair&quot; operation is not required (or is not likely to succeed), it is important that the author of the command return a non-zero value so the machine will still reboot as expected. </p>
<p> Note that the watchdog daemon may interpret and act upon any of the reserved return codes noted in the Check Binary section prior to calling a given command in &quot;repair&quot; mode.</p>
<h2>Systemd</h2>
<p>To start watchdog after the network is available: </p>
<p> systemctl disable watchdog<br />
 systemctl enable NetworkManager-wait-online<br />
 systemctl enable watchdog-ping </p>
<p> When using custom service pid check with custom service systemd unit file please be aware the &quot;Requires=&quot; does dependent service deactivation. Using &quot;Before=watchdog.service&quot; or &quot;Before=watchdog-ping.service&quot; in the custom service unit file may be the desired operation instead. See systemd.unit documentation for more details.</p>
<h2>Selinux</h2>
<p>The directories /etc/watchdog.d/ and /usr/libexec/watchdog/scripts/ are recognized locations for custom executables.</p>
<h2>Bugs</h2>
<p>None known so far.</p>
<h2>Authors</h2>
<p>The original code is an example written by Alan Cox &lt;alan [at] lxorguk.ukuu.org.uk&gt;, the author of the kernel driver. All additions were written by Michael Meskes &lt;meskes [at] debian.org&gt;. Johnie Ingram &lt;johnie [at] netgod.net&gt; had the idea of testing the load average. He also took over the Debian specific work. Dave Cinege &lt;dcinege [at] psychosis.com&gt; brought up some hardware watchdog issues and helped testing this stuff.</p>
<h2>Files</h2>
<dl>
<dt><i>/dev/watchdog </i></p>
<dd>The watchdog device.</p>
<dt><i>/var/run/watchdog.pid </i></p>
<dd>The pid file of the running <code>watchdog</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-watchdog-conf/">watchdog.conf</a></code>(5),<code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) </p>
