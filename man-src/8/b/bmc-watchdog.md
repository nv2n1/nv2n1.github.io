---
title: "bmc-watchdog(8)"
name: "bmc-watchdog"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bmc-watchdog/"
description: "bmc-watchdog – BMC watchdog timer daemon and control utility"
---

<p>bmc-watchdog &#8211; BMC watchdog timer daemon and control utility</p>
<h2>Synopsis</h2>
<p><code>bmc-watchdog</code> command [<i>OPTION</i>&#8230;] [<i>COMMAND_OPTIONS</i>&#8230;]</p>
<h2>Description</h2>
<p><code>bmc-watchdog</code> controls a Baseboard Management Controller (BMC) watchdog timer. The <code>bmc-watchdog</code> tool typically executes as a cronjob or daemon to manage the watchdog timer. A user must be root in order to run <code>bmc-watchdog.</code> </p>
<p> Listed below are <code>bmc-watchdog</code> details, option details, examples, and known issues. For a general introduction to FreeIPMI please see <code><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7).</code></p>
<h2>Bmc Watchdog Details</h2>
<p>A BMC watchdog timer is part of the Intelligent Platform Management Interface (IPMI) specification and is only available to BMCs that are compliant with IPMI. When a BMC watchdog timer is started, it begins counting down to zero from some positive number of seconds. When the timer hits zero, the timer will execute a pre-configured pre-timeout interrupt and/or timeout action. </p>
<p> In order to stop the pre-timeout interrupt or timeout action from being executed, the watchdog timer must be periodically reset back to its initial beginning value. </p>
<p> The BMC watchdog timer automatically stops itself when the machine is rebooted. Therefore, when a machine is brought up, the BMC watchdog timer must be setup again before it can be used. </p>
<p> Typically, a BMC watchdog timer is used to automatically reset a machine that has crashed. When the operating system first starts up, the BMC timer is set to its initial countdown value. At periodic intervals, when the operating system is functioning properly, the watchdog timer can be reset by the OS or a userspace program. Thus, the timer never counts down to zero. When the system crashes, the timer cannot be reset by the OS or userspace program. Eventually, the timer will countdown to zero and reset the machine. </p>
<p> See EXAMPLES below for examples of how bmc-watchdog is commonly used.</p>
<h2>Commands</h2>
<p>The following commands are available to <code>bmc-watchdog.</code></p>
<dl>
<dt><code>-s</code>, <code>&#8211;set</code></p>
<dd>Set BMC Watchdog Configuration. BMC watchdog timer configuration values can be set using the set command options listed below under SET OPTIONS. If a particular configuration parameter is not specified on the command line, the current configuration of that parameter will not be changed.</p>
<dt><code>-g</code>, <code>&#8211;get</code></p>
<dd>Get BMC Watchdog Configuration and State. The current configuration and state is printed to standard output.</p>
<dt><code>-r</code>, <code>&#8211;reset</code></p>
<dd>Reset BMC Watchdog Timer.</p>
<dt><code>-t</code>, <code>&#8211;start</code></p>
<dd>Start BMC Watchdog Timer. Does nothing if the timer is currently running. Identical to <code>&#8211;reset</code> command when the timer is stopped with the exception of the start command options listed below under START OPTIONS.</p>
<dt><code>-y</code>, <code>&#8211;stop</code></p>
<dd>Stop BMC Watchdog Timer. Stops the current timer.</p>
<dt><code>-c</code>, <code>&#8211;clear</code></p>
<dd>Clear BMC Watchdog Configuration. Clears all configuration values for the watchdog timer, except for timer use, which is kept at its current value.</p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd>Run <code>bmc-watchdog</code> as a daemon. Configurable BMC watchdog timer options are listed below under DAEMON OPTIONS. The configuration values are set once, then the daemon will reset the timer at specified periodic intervals. The daemon can be stopped using the <code>&#8211;stop</code> command, <code>&#8211;clear</code> command, or by setting the stop_timer flag on the <code>&#8211;set</code> command.</dl>
<h2>General Options</h2>
<p>The following options are general options for configuring IPMI communication and executing general tool commands. These options are generic and can be used by any command.</p>
<dl>
<dt><code>-D</code> <i>IPMIDRIVER</i>, <code>&#8211;driver-type</code>=<i>IPMIDRIVER</i></p>
<dd>Specify the driver type to use instead of doing an auto selection. The currently available inband drivers are KCS, SSIF, OPENIPMI, and SUNBMC.</p>
<dt><code>&#8211;disable-auto-probe</code></p>
<dd>Do not probe in-band IPMI devices for default settings.</p>
<dt><code>&#8211;driver-address</code>=<i>DRIVER-ADDRESS</i></p>
<dd>Specify the in-band driver address to be used instead of the probed value. <i>DRIVER-ADDRESS</i> should be prefixed with &quot;0x&quot; for a hex value and &#8216;0&#8217; for an octal value.</p>
<dt><code>&#8211;driver-device</code>=<i>DEVICE</i></p>
<dd>Specify the in-band driver device path to be used instead of the probed path.</p>
<dt><code>&#8211;register-spacing</code>=<i>REGISTER-SPACING</i></p>
<dd>Specify the in-band driver register spacing instead of the probed value. Argument is in bytes (i.e. 32bit register spacing = 4)</p>
<dt><code>&#8211;target-channel-number</code>=<i>CHANNEL-NUMBERFR</p>
<dd>Specify the in-band driver target channel number to send IPMI requests to.</p>
<dt></i><code>&#8211;target-slave-address</code>=<i>SLAVE-ADDRESSFR</p>
<dd>Specify the in-band driver target slave number to send IPMI requests to.</p>
<dt></i><code>-v</code>, <code>&#8211;verbose-logging</code></p>
<dd>Increase verbosity of logging.</p>
<dt><code>-n</code>, <code>&#8211;no-logging</code></p>
<dd>Turns off all logging done by <code>bmc-watchdog.</code></p>
<dt><code>&#8211;config-file</code>=<i>FILE</i></p>
<dd>Specify an alternate configuration file.</p>
<dt><code>-W</code> <i>WORKAROUNDS</i>, <code>&#8211;workaround-flags</code>=<i>WORKAROUNDS</i></p>
<dd>Specify workarounds to vendor compliance issues. Multiple workarounds can be specified separated by commas. A special command line flag of &quot;none&quot;, will indicate no workarounds (may be useful for overriding configured defaults). See WORKAROUNDS below for a list of available workarounds.</p>
<dt><code>&#8211;debug</code></p>
<dd>Turn on debugging.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Output a help list and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd>Output a usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output the program version and exit.</dl>
<h2>Set Options</h2>
<p>The following options can be used by the set command to set or clear various BMC watchdog configuration parameters.</p>
<dl>
<dt><code>-u</code> <i>INT</i>, <code>&#8211;timer-use</code>=<i>INT</i></p>
<dd>Set timer use. The timer use value can be set to one of the following: 1 = BIOS FRB2, 2 = BIOS POST, 3 = OS_LOAD, 4 = SMS OS, 5 = OEM.</p>
<dt><code>-m</code> <i>INT</i>, <code>&#8211;stop-timer</code>=<i>INT</i></p>
<dd>Set Stop Timer Flag. A flag value of 0 stops the current BMC watchdog timer. A value of 1 doesn&#8217;t turn off the current watchdog timer.</p>
<dt><code>-l</code> <i>INT</i>, <code>&#8211;log</code>=<i>INT</i></p>
<dd>Set Log Flag. A flag value of 0 turns logging on. A value of 1 turns logging off.</p>
<dt><code>-a</code> <i>INT</i>, <code>&#8211;timeout-action</code>=<i>INT</i></p>
<dd>Set timeout action. The timeout action can be set to one of the following: 0 = No action, 1 = Hard Reset, 2 = Power Down, 3 = Power Cycle.</p>
<dt><code>-p</code> <i>INT</i>, <code>&#8211;pre-timeout-interrupt</code>=<i>INT</i></p>
<dd>Set pre-timeout interrupt. The pre timeout interrupt can be set to one of the following: 0 = None, 1 = SMI, 2 = NMI, 3 = Messaging Interrupt.</p>
<dt><code>-z</code> <i>SECONDS</i>, <code>&#8211;pre-timeout-interval=</code><i>SECONDS</i></p>
<dd>Set pre-timeout interval in seconds.</p>
<dt><code>-F</code>, <code>&#8211;clear-bios-frb2</code></p>
<dd>Clear BIOS FRB2 Timer Use Flag.</p>
<dt><code>-P</code>, <code>&#8211;clear-bios-post</code></p>
<dd>Clear BIOS POST Timer Use Flag.</p>
<dt><code>-L</code>, <code>&#8211;clear-os-load</code></p>
<dd>Clear OS Load Timer Use Flag.</p>
<dt><code>-S</code>, <code>&#8211;clear-sms-os</code></p>
<dd>Clear SMS/OS Timer Use Flag.</p>
<dt><code>-O</code>, <code>&#8211;clear-oem</code></p>
<dd>Clear OEM Timer Use Flag.</p>
<dt><code>-i</code> <i>SECONDS</i>, <code>&#8211;initial-countdown</code>=<i>SECONDS</i></p>
<dd>Set initial countdown in seconds.</p>
<dt><code>-w</code>, <code>&#8211;start-after-set</code></p>
<dd>Start timer after set command if timer is stopped. This is typically used when <code>bmc-watchdog</code> is used as a cronjob. This can be used to automatically start the timer after it has been set the first time.</p>
<dt><code>-x</code>, <code>&#8211;reset-after-set</code></p>
<dd>Reset timer after set command if timer is running.</p>
<dt><code>-j</code>, <code>&#8211;start-if-stopped</code></p>
<dd>Don&#8217;t execute set command if timer is stopped, just start timer.</p>
<dt><code>-k</code>, <code>&#8211;reset-if-running</code></p>
<dd>Don&#8217;t execute set command if timer is running, just reset timer. This is typically used when <code>bmc-watchdog</code> is used as a cronjob. This can be used to reset the timer after it has been initially started.</dl>
<h2>Start Options</h2>
<p>The following options can be used by the start command.</p>
<dl>
<dt><code>-G</code> <i>INT</i>, <code>&#8211;gratuitous-arp</code>=<i>INT</i></p>
<dd>Suspend or don&#8217;t suspend gratuitous ARPs while the BMC timer is running. A flag value of 1 suspends gratuitous ARPs. A value of 0 will not suspend gratuitous ARPs. If this option is not specified, gratuitous ARPs will not be suspended.</p>
<dt><code>-A</code> <i>INT</i>, <code>&#8211;arp-response</code>=<i>INT</i></p>
<dd>Suspend or don&#8217;t suspend BMC-generated ARP responses while the BMC timer is running. A flag value of 1 suspends ARP responses. A value of 0 will not suspend ARP responses. If this option is not specified, ARP responses will not be suspended.</dl>
<h2>Daemon Options</h2>
<p>The following options can be used by the daemon command to set the initial BMC watchdog configuration parameters.</p>
<dl>
<dt><code>-u</code> <i>INT</i>, <code>&#8211;timer-use</code>=<i>INT</i></p>
<dd>Set timer use. The timer use value can be set to one of the following: 1 = BIOS FRB2, 2 = BIOS POST, 3 = OS_LOAD, 4 = SMS OS, 5 = OEM.</p>
<dt><code>-l</code> <i>INT</i>, <code>&#8211;log</code>=<i>INT</i></p>
<dd>Set Log Flag. A flag value of 0 turns logging on. A value of 1 turns logging off.</p>
<dt><code>-a</code> <i>INT</i>, <code>&#8211;timeout-action</code>=<i>INT</i></p>
<dd>Set timeout action. The timeout action can be set to one of the following: 0 = No action, 1 = Hard Reset, 2 = Power Down, 3 = Power Cycle.</p>
<dt><code>-p</code> <i>INT</i>, <code>&#8211;pre-timeout-interrupt</code>=<i>INT</i></p>
<dd>Set pre-timeout interrupt. The pre timeout interrupt can be set to one of the following: 0 = None, 1 = SMI, 2 = NMI, 3 = Messaging Interrupt.</p>
<dt><code>-z</code> <i>SECONDS</i>, <code>&#8211;pre-timeout-interval</code>=<i>SECONDS</i></p>
<dd>Set pre-timeout interval in seconds.</p>
<dt><code>-F</code>, <code>&#8211;clear-bios-frb2</code></p>
<dd>Clear BIOS FRB2 Timer Use Flag.</p>
<dt><code>-P</code>, <code>&#8211;clear-bios-post</code></p>
<dd>Clear BIOS POST Timer Use Flag.</p>
<dt><code>-L</code>, <code>&#8211;clear-os-load</code></p>
<dd>Clear OS Load Timer Use Flag.</p>
<dt><code>-S</code>, <code>&#8211;clear-sms-os</code></p>
<dd>Clear SMS/OS Timer Use Flag.</p>
<dt><code>-O</code>, <code>&#8211;clear-oem</code></p>
<dd>Clear OEM Timer Use Flag.</p>
<dt><code>-i</code> <i>SECONDS</i>, <code>&#8211;initial-countdown</code>=<i>SECONDS</i></p>
<dd>Set initial countdown in seconds.</p>
<dt><code>-G</code> <i>INT</i>, <code>&#8211;gratuitous-arp</code>=<i>INT</i></p>
<dd>Suspend or don&#8217;t suspend gratuitous ARPs while the BMC timer is running. A flag value of 1 suspends gratuitous ARPs. A value of 0 will not suspend gratuitous ARPs. If this option is not specified, gratuitous ARPs will not be suspended.</p>
<dt><code>-A</code> <i>INT</i>, <code>&#8211;arp-response</code>=<i>INT</i></p>
<dd>Suspend or don&#8217;t suspend BMC-generated ARP responses while the BMC timer is running. A flag value of 1 suspends ARP responses. A value of 0 will not suspend ARP responses. If this option is not specified, ARP responses will not be suspended.</p>
<dt><code>-e</code>, <code>&#8211;reset-period</code></p>
<dd>Time interval to wait before resetting timer. The default is 60 seconds.</dl>
<h2>Errors</h2>
<p>Errors are logged to syslog.</p>
<h2>Workarounds</h2>
<p>With so many different vendors implementing their own IPMI solutions, different vendors may implement their IPMI protocols incorrectly. The following describes a number of workarounds currently available to handle discovered compliance issues. When possible, workarounds have been implemented so they will be transparent to the user. However, some will require the user to specify a workaround be used via the -W option. </p>
<p> The hardware listed below may only indicate the hardware that a problem was discovered on. Newer versions of hardware may fix the problems indicated below. Similar machines from vendors may or may not exhibit the same problems. Different vendors may license their firmware from the same IPMI firmware developer, so it may be worthwhile to try workarounds listed below even if your motherboard is not listed. </p>
<p> If you believe your hardware has an additional compliance issue that needs a workaround to be implemented, please contact the FreeIPMI maintainers on &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;. </p>
<p> <i>assumeio</i> &#8211; This workaround flag will assume inband interfaces communicate with system I/O rather than being memory-mapped. This will work around systems that report invalid base addresses. Those hitting this issue may see &quot;device not supported&quot; or &quot;could not find inband device&quot; errors. Issue observed on HP ProLiant DL145 G1. </p>
<p> <i>spinpoll</i> &#8211; This workaround flag will inform some inband drivers (most notably the KCS driver) to spin while polling rather than putting the process to sleep. This may significantly improve the wall clock running time of tools because an operating system scheduler&#8217;s granularity may be much larger than the time it takes to perform a single IPMI message transaction. However, by spinning, your system may be performing less useful work by not contexting out the tool for a more useful task. </p>
<p> <i>ignorestateflag</i> &#8211; This workaround option will ignore the BMC timer state flag (indicating if the timer is running or stopped) when running in daemon mode. On some BMCs, the flag is broken and will never report that a BMC timer is running, even if it is. The workaround will take notice of changes in the countdown seconds to determine if a timer is running or stopped. With this type of implementation, the reset-period must be large enough to ensure minor fluctuations in the countdown will not affect the workaround. Due to the implementation of this workaround, if another process stops the watchdog timer, it may be detectable. This option is confirmed to work around compliances issues on Sun x4100, x4200, and x4500.</p>
<h2>Examples</h2>
<p>Setup a bmc-watchdog daemon that resets the machine after 15 minutes (900 seconds) if the OS has crashed (see default bmc-watchdog rc script /etc/init.d/bmc-watchdog for a more complete example):<br />
&nbsp;<wbr>&nbsp;<wbr>bmc-watchdog -d -u 4 -p 0 -a 1 -i 900</p>
<h2>Diagnostics</h2>
<p>Upon successful execution, exit status is 0. On error, exit status is 1.</p>
<h2>Known Issues</h2>
<p><code>Bmc-watchdog</code> may fail to reset the watchdog timer if it is not scheduled properly. It is always recommended that <code>bmc-watchdog</code> be executed with a high scheduling priority. </p>
<p> On some machines, the hardware based SMI Handler may disable a processor after a watchdog timer timeout if the timer use is set to something other than SMS/OS.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2004-2007 The Regents of the University of California. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
