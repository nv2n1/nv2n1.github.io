---
title: "mcelog(8)"
name: "mcelog"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mcelog/"
description: "mcelog – Decode kernel machine check log on x86 machines"
---

<p>mcelog &#8211; Decode kernel machine check log on x86 machines</p>
<h2>Synopsis</h2>
<p>mcelog [options] [device]<br />
 mcelog [options] &#8211;daemon<br />
 mcelog [options] &#8211;client<br />
 mcelog [options] &#8211;ascii </p>
<p> mcelog [options] &#8211;is-cpu-supported<br />
 mcelog &#8211;version</p>
<h2>Description</h2>
<p>X86 CPUs report errors detected by the CPU as <i>machine check events (MCEs). </i> These can be data corruption detected in the CPU caches, in main memory by an integrated memory controller, data transfer errors on the front side bus or CPU interconnect or other internal errors. Possible causes can be cosmic radiation, instable power supplies, cooling problems, broken hardware, running systems out of specification, or bad luck. Most errors can be corrected by the CPU by internal error correction mechanisms. Uncorrected errors cause machine check exceptions which may kill processes or panic the machine. A small number of corrected errors is usually not a cause for worry, but a large number can indicate future failure. When a corrected or recovered error happens the x86 kernel writes a record describing the MCE into a internal ring buffer available through the <i>/dev/mcelog</i> device <i>mcelog </i> retrieves errors from <i>/dev/mcelog, </i> decodes them into a human readable format and prints them on the standard output or optionally into the system log. Optionally it can also take more options like keeping statistics or triggering shell scripts on specific events. By default mcelog supports offlining memory pages with persistent corrected errors, offlining CPU cores if they developed cache problems, and otherwise logging specific events to the system log after they crossed a threshold. The normal operating modi for mcelog are running as a regular cron job (traditional way, deprecated), running as a trigger directly executed by the kernel, or running as a daemon with the <i>&#8211;daemon</i> option. When an uncorrected machine check error happens that the kernel cannot recover from then it will usually panic the system. In this case when there was a warm reset after the panic mcelog should pick up the machine check errors after reboot. This is not possible after a cold reset. In addition mcelog can be used on the command line to decode the kernel output for a fatal machine check panic in text format using the <i>&#8211;ascii</i> option. This is typically used to decode the panic console output of a fatal machine check, if the system was power cycled or mcelog didn&#8217;t run immediately after reboot. When the panic triggers a kdump kexec crash kernel the crash kernel boot up script should log the machine checks to disk, otherwise they might be lost. Note that after mcelog retrieves an error the kernel doesn&#8217;t store it anymore (different from <i><a href="/docs/linux/man/1-dmesg/">dmesg</a>(1)),</i> so the output should be always saved somewhere and mcelog not run in uncontrolled ways. When invoked with the <i>&#8211;is-cpu-supported</i> option mcelog exits with code 0 if the current CPU is supported, 1 otherwise. </p>
<h2>Options</h2>
<p>When the <code>&#8211;syslog</code> option is specified redirect output to system log. The <code>&#8211;syslog-error</code> option causes the normal machine checks to be logged as <i>LOG_ERR</i> (implies <i>&#8211;syslog</i> ). Normally only fatal errors or high level remarks are logged with error level. High level one line summaries of specific errors are also logged to the syslog by default unless mcelog operates in <i>&#8211;ascii </i> mode. </p>
<p> When the <code>&#8211;logfile=file</code> option is specified append log output to the specified file. With the <code>&#8211;no-syslog</code> option mcelog will never log anything to the syslog. </p>
<p> When the <code>&#8211;cpu=cputype</code> option is specified set the to be decoded CPU to <i>cputype. </i> See <i>mcelog &#8211;help</i> for a list of valid CPUs. Note that specifying an incorrect CPU can lead to incorrect decoding output. Default is either the CPU of the machine that reported the machine check (needs a newer kernel version) or the CPU of the machine mcelog is running on, so normally this option doesn&#8217;t have to be used. Older versions of mcelog had separate options for different CPU types. These are still implemented, but deprecated and undocumented now. </p>
<p> With the <code>&#8211;dmi</code> option mcelog will look up the DIMMs reported in machine checks in the <i>SMBIOS/DMI</i> tables of the BIOS and map the DIMMs to board identifiers. This only works when the BIOS reports the identifiers correctly. Unfortunately often the information reported by the BIOS is either subtly or obviously wrong or useless. This option requires that mcelog has read access to /dev/mem (normally requires root) and runs on the same machine in the same hardware configuration as when the machine check event happened. </p>
<p> When <code>&#8211;ignorenodev</code> is specified then mcelog will exit silently when the device cannot be opened. This is useful in virtualized environment with limited devices. </p>
<p> When <code>&#8211;filter</code> is specified <i>mcelog</i> will filter out known broken machine check events (default on). When the <code>&#8211;no-filter</code> option is specified mcelog does not filter events. </p>
<p> When <code>&#8211;raw</code> is specified <i>mcelog</i> will not decode, but just dump the mcelog in a raw hex format. This can be useful for automatic post processing. </p>
<p> When a device is specified the machine check logs are read from device instead of the default <i>/dev/mcelog.</i> </p>
<p> With the <code>&#8211;ascii</code> option mcelog decodes a fatal machine check panic generated by the kernel (&quot;CPU n: Machine Check Exception &#8230;&quot;) in ASCII from standard input and exits afterwards. Note that when the panic comes from a different machine than where mcelog is running on you might need to specify the correct cputype on older kernels. On newer kernels which output the <i>PROCESSOR</i> field this is not needed anymore. </p>
<p> When the <code>&#8211;file filename</code> option is specified <i>mcelog &#8211;ascii</i> will read the ASCII machine check record from input file <i>filename</i> instead of standard input. </p>
<p> With the <code>&#8211;config-file file</code> option mcelog reads the specified config file. Default is <i>/etc/mcelog/mcelog.conf</i> See also <i>CONFIG FILE</i> below. </p>
<p> With the <code>&#8211;daemon</code> option mcelog will run in the background. This gives the fastest reaction time and is the recommended operating mode. If an output option isn&#8217;t selected ( <i>&#8211;logfile</i> or <i>&#8211;syslog</i> or <i>&#8211;syslog-error</i> ), this option implies <i>&#8211;logfile=/var/log/mcelog. </i> Important messages will be logged as one-liner summaries to syslog unless <i>&#8211;no-syslog </i> is given. The option <i>&#8211;foreground</i> will prevent mcelog from giving up the terminal in daemon mode. This is intended for debugging. </p>
<p> With the <code>&#8211;client</code> option mcelog will query a running daemon for accumulated errors. </p>
<p> With the <code>&#8211;cpumhz=mhz</code> option assume the CPU has <i>mhz</i> frequency for decoding the time of the event using the CPU time stamp counter. This also forces decoding. Note this can be unreliable. on some systems with CPU frequency scaling or deep C states, where the CPU time stamp counter does not increase linearly. By default the frequency of the current CPU is used when mcelog determines it is safe to use. Newer kernels report the time directly in the event and don&#8217;t need this anymore. </p>
<p> The <code>&#8211;pidfile file</code> option writes the process id of the daemon into file <i>file.</i> Only valid in daemon mode. </p>
<p> Mcelog will enable extended error reporting from the memory controller on processors that support it unless you tell it not to with the <code>&#8211;no-imc-log</code> option. You might need this option when decoding old logs from a system where this mode was not enabled. </p>
<p> <code>&#8211;version</code> displays the version of mcelog and exits.</p>
<h2>Config File</h2>
<p>mcelog supports a config file to set defaults. Command line options override the config file. By default the config file is read from <i>/etc/mcelog/mcelog.conf</i> unless overridden with the <i>&#8211;config-file</i> option. </p>
<p> The general format is <i>optionname = value</i> White space is not allowed in value currently, except at the end where it is dropped Comments start with #. </p>
<p> All command line options that are not commands can be specified in the config file. For example t to enable the <i>&#8211;no-syslog</i> option use <i>no-syslog = yes </i> (or no to disable). When the option has a argument use <i>logfile = /tmp/logfile</i> </p>
<p> For more information on the config file please see <code><a href="/docs/linux/man/5-mcelog-conf/">mcelog.conf</a>(5).</code></p>
<h2>Notes</h2>
<p>The kernel prefers old messages over new. If the log buffer overflows only old ones will be kept. The exact output in the log file depends on the CPU, unless the &#8211;raw option is used. mcelog will report serious errors to the syslog during decoding. </p>
<h2>Signals</h2>
<p>When <i>mcelog</i> runs in daemon mode and receives a <i>SIGUSR1</i> it will close and reopen the log files. This can be used to rotate logs without restarting the daemon.</p>
<h2>Files</h2>
<p>/dev/mcelog (char 10, minor 227) </p>
<p> /etc/mcelog/mcelog.conf </p>
<p> /var/log/mcelog </p>
<p> /var/run/mcelog.pid</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-mcelog-conf/">mcelog.conf</a>(5),</code> <code><a href="/docs/linux/man/5-mcelog-triggers/">mcelog.triggers</a>(5)</code> <a rel="nofollow" href="http://www.mcelog.org">http://www.mcelog.org</a> AMD x86-64 architecture programmer&#8217;s manual, Volume 2, System programming Intel 64 and IA32 Architectures Software Developer&#8217;s manual, Volume 3, System programming guide Chapter 15 and 16. <a rel="nofollow" href="http://www.intel.com/sdm">http://www.intel.com/sdm</a> Datasheet of your CPU. </p>
