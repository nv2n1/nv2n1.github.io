---
title: "mcelog-triggers(5)"
name: "mcelog-triggers"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mcelog-triggers/"
description: "mcelog.triggers – mcelog trigger scripts reference"
---

<p>mcelog.triggers &#8211; mcelog trigger scripts reference</p>
<h2>Synopsis</h2>
<p><code>/etc/mcelog/bus-error-trigger</code><br />
 <code>/etc/mcelog/cache-error-trigger</code><br />
 <code>/etc/mcelog/dimm-error-trigger</code><br />
 <code>/etc/mcelog/iomca-error-trigger</code><br />
 <code>/etc/mcelog/page-error-trigger</code><br />
 <code>/etc/mcelog/socket-memory-error-trigger</code><br />
 <code>/etc/mcelog/unknown-error-trigger</code></p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/8-mcelog/">mcelog</a>(8)</code> maintains thresholds of errors using a <i>leaky-bucket</i> algorithm. When the number of errors in a specific time window exceeds a pre-configured threshold a <i>trigger</i> will be executed. Triggers are usually shell scripts in the <code>/etc/mcelog </code> directory but can be also other internal actions. Thresholds and triggers can be configured in <code><a href="/docs/linux/man/5-mcelog-conf/">mcelog.conf</a>(5)</code> </p>
<p> Trigger will run as the user configured for mcelog in <i>mcelog.conf,</i> by default root. The default trigger action can be overridden by specifying a different trigger script in the configuration file. Actions in addition to the default trigger (like notifying an administrator) can be put into the respective <i>/etc/mcelog/*.local</i> script which is executed after the default action. This allows updating the default scripts without overriding local actions. All trigger actions are also logged to syslog. </p>
<p> <code>The DIMM and socket memory error triggers</code> </p>
<p> The <code>/etc/mcelog/dimm-error-trigger</code> and <code>/etc/mcelog/socket-memory-error-trigger</code> scripts are executed when a DIMM or a CPU socket exceeds a configured corrected or uncorrected memory error threshold. The thresholds are configured in the <code>mcelog.conf</code> <i>[dimm]</i> and <i>[socket]</i> sections. The default triggers log a warning message in the system log. The triggers are only executed when mcelog runs as a daemon. </p>
<p> Arguments are passed as environment variables </p>
<table>
<tr VALIGN=top>
<td>THRESHOLD</td>
<td>human readable threshold status
</td>
</tr>
<tr VALIGN=top>
<td>MESSAGE</td>
<td>Human readable consolidated error message
</td>
</tr>
<tr VALIGN=top>
<td>TOTALCOUNT</td>
<td>total corrected or uncorrected count of errors for current DIMM depending on what triggered the event
</td>
</tr>
<tr VALIGN=top>
<td>LOCATION</td>
<td>Consolidated location as a single string
</td>
</tr>
<tr VALIGN=top>
<td>DMI_LOCATION</td>
<td>DIMM location from DMI/SMBIOS if available
</td>
</tr>
<tr VALIGN=top>
<td>DMI_NAME</td>
<td>DIMM identifier from DMI/SMBIOS if available
</td>
</tr>
<tr VALIGN=top>
<td>DIMM</td>
<td>DIMM number reported by hardware
</td>
</tr>
<tr VALIGN=top>
<td>CHANNEL</td>
<td>Channel number reported by hardware
</td>
</tr>
<tr VALIGN=top>
<td>SOCKETID</td>
<td>Socket ID of CPU that includes the memory controller with the DIMM
</td>
</tr>
<tr VALIGN=top>
<td>CECOUNT</td>
<td>Total corrected error count for DIMM
</td>
</tr>
<tr VALIGN=top>
<td>UCCOUNT</td>
<td>Total uncorrected error count for DIMM
</td>
</tr>
<tr VALIGN=top>
<td>LASTEVENT</td>
<td>Time stamp of event that triggered threshold (in time_t format, seconds)
</td>
</tr>
<tr VALIGN=top>
<td>THRESHOLD_COUNT</td>
<td>Total umber of events in current threshold time period of specific type
</td>
</tr>
</table>
<p> After the default action local actions in <code>/etc/mcelog/dimm-error-trigger.local</code> or respective <code>/etc/mcelog/socket-memory-error-trigger.local</code> are executed. </p>
<p> <code>The page error trigger</code> </p>
<p> The <code>/etc/mcelog/page-error-trigger </code> script is executed by mcelog in daemon mode when a page in memory exceeds a pre-configured corrected or uncorrected error threshold. mcelog internally also implements offlining the page through the kernel. This is configured through the <i>[page]</i> section of <code><a href="/docs/linux/man/5-mcelog-conf/">mcelog.conf</a>(5)</code> </p>
<p> The environment arguments are the same as for the <i>dimm-error-trigger</i> script </p>
<p> After the default action local actions in <i>/etc/mcelog/page-error-trigger.loccal are executed.</i> </p>
<p> <code>The cache error trigger</code> </p>
<p> The <i>/etc/mcelog/cache-error-trigger</i> shell script is called for cache error handling in daemon mode when a CPU reports excessive corrected cache errors. This could be a indication for future uncorrected errors. </p>
<p> This trigger is configured through the <code>[cache]</code> section in the <code><a href="/docs/linux/man/5-mcelog-conf/">mcelog.conf</a>(5)</code> configuration file. The threshold is defined by the CPU. The default trigger offlines the affected CPU cores, unless it is the last core running. </p>
<p> Arguments are passed as environment variables </p>
<table>
<tr VALIGN=top>
<td>MESSAGE</td>
<td>Human readable error message
</td>
</tr>
<tr VALIGN=top>
<td>CPU</td>
<td>Linux CPU number that triggered the error
</td>
</tr>
<tr VALIGN=top>
<td>LEVEL</td>
<td>Cache level affected by error
</td>
</tr>
<tr VALIGN=top>
<td>TYPE</td>
<td>Cache type affected by error (Data,Instruction,Generic)
</td>
</tr>
<tr VALIGN=top>
<td>AFFECTED_CPUS</td>
<td>List of CPUs sharing the affected cache
</td>
</tr>
<tr VALIGN=top>
<td>SOCKETID</td>
<td>Socket ID of affected CPU
</td>
</tr>
</table>
<p> After the default action local actions in <i>/etc/mcelog/cache-error-trigger.local are executed.</i> </p>
<p> <code>The bus-uc-threshold-trigger</code> </p>
<p> The <code>bus-uc-threshold-trigger</code> runs on uncorrected errors on a IO bus. It is configured through the <code>bus-uc-threshold-trigger</code> and <code>bus-uc-threshold-trigger-threshold</code> options in <i>/etc/<a href="/docs/linux/man/5-mcelog-conf/">mcelog.conf</a>(5). </i> By default it logs a message with the error location to the system log. After the default action local actions in <i>/etc/mcelog/bus-uc-error-trigger.local </i> are executed. </p>
<p> Arguments are passed as environment variables </p>
<table>
<tr VALIGN=top>
<td>MESSAGE</td>
<td>Human readable consolidated error message.
</td>
</tr>
<tr VALIGN=top>
<td>LOCATION</td>
<td>Consolidated location as a single string
</td>
</tr>
<tr VALIGN=top>
<td>SOCKETID</td>
<td>Socket ID of CPU that includes the memory controller with the DIMM
</td>
</tr>
<tr VALIGN=top>
<td>LEVEL</td>
<td>Interconnect level
</td>
</tr>
<tr VALIGN=top>
<td>PARTICIPATION</td>
<td>Processor Participation (Originator, Responder or Observer)
</td>
</tr>
<tr VALIGN=top>
<td>REQUEST</td>
<td>Request type (read, write, prefetch, etc.)
</td>
</tr>
<tr VALIGN=top>
<td>ORIGIN </td>
<td>Memory or IO
</td>
</tr>
<tr VALIGN=top>
<td>TIMEOUT</td>
<td>The request timed out or not
</td>
</tr>
</table>
<p> <code>The iomca-error-trigger</code> </p>
<p> The <code>iomca-error-trigger</code> runs when a socket receives bus or interconnect errors. It is configured through the <code>iomca-error-trigger </code> and <code>iomca-error-trigger-threshold</code> options in <i>/etc/mcelog.conf. By default it logs a message with the error location to the system log.</i> After the default action local actions in <i>/etc/mcelog/iomca-error-trigger.local are executed.</i> </p>
<p> Arguments are passed as environment variables </p>
<table>
<tr VALIGN=top>
<td>MESSAGE</td>
<td>Human readable consolidated error message
</td>
</tr>
<tr VALIGN=top>
<td>LOCATION</td>
<td>Consolidated location as a single string
</td>
</tr>
<tr VALIGN=top>
<td>SOCKETID</td>
<td>Socket ID of CPU that includes the memory controller with the DIMM
</td>
</tr>
<tr VALIGN=top>
<td>CPU</td>
<td>Linux CPU number that triggered the error
</td>
</tr>
<tr VALIGN=top>
<td>SET</td>
<td>PCI segment number
</td>
</tr>
<tr VALIGN=top>
<td>BUS</td>
<td>PCI bus number
</td>
</tr>
<tr VALIGN=top>
<td>DEVICE</td>
<td>PCI device number
</td>
</tr>
<tr VALIGN=top>
<td>FUNCTION</td>
<td>PCI function number
</td>
</tr>
</table>
<p> <code>The unknown-error-trigger</code> </p>
<p> The <code>unknown-error-trigger</code> runs on any errors not otherwise categorized. It is configured through the <code>unknown-error-trigger</code> and <code>unknown-error-trigger-threshold</code> options in <i>/etc/mcelog.conf. </i> By default it logs a message to the system log. After the default action local actions in <i>/etc/mcelog/unknown-error-trigger.local </i> are executed. </p>
<p> Arguments are passed as environment variables </p>
<table>
<tr VALIGN=top>
<td>MESSAGE</td>
<td>Human readable consolidated error message
</td>
</tr>
<tr VALIGN=top>
<td>LOCATION</td>
<td>Consolidated location as a single string
</td>
</tr>
<tr VALIGN=top>
<td>SOCKETID</td>
<td>Socket ID of CPU that includes the memory controller with the DIMM
</td>
</tr>
<tr VALIGN=top>
<td>CPU</td>
<td>Linux CPU number that triggered the error
</td>
</tr>
<tr VALIGN=top>
<td>STATUS</td>
<td>IA32_MCi_STATUS register value
</td>
</tr>
<tr VALIGN=top>
<td>ADDR</td>
<td>IA32_MCi_ADDR register value
</td>
</tr>
<tr VALIGN=top>
<td>MISC</td>
<td>IA32_MCi_MISC register value
</td>
</tr>
<tr VALIGN=top>
<td>MCGSTATUS</td>
<td>IA32_MCG_STATUS register value
</td>
</tr>
<tr VALIGN=top>
<td>MCGCAP</td>
<td>IA32_MCG_CAP register value
</td>
</tr>
</table>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://www.mcelog.org">http://www.mcelog.org</a> <code><a href="/docs/linux/man/8-mcelog/">mcelog</a>(8),</code> <code><a href="/docs/linux/man/5-mcelog-conf/">mcelog.conf</a>(5)</code> </p>
