---
title: "freeipmi(7)"
name: "freeipmi"
section: "7"
letter: "f"
url: "/docs/linux/man/7-freeipmi/"
description: "FreeIPMI – FreeIPMI overview"
---

<p>FreeIPMI &#8211; FreeIPMI overview</p>
<h2>Introduction</h2>
<p>FreeIPMI provides in-band and out-of-band IPMI software based on the IPMI v1.5/2.0 specification.</p>
<h2>What is IPMI?</h2>
<p>The IPMI specification defines a set of interfaces for platform management and is implemented by a number vendors for system management. The features of IPMI that most users will be interested in are sensor monitoring, system event monitoring, power control, and serial-over-LAN (SOL). The FreeIPMI tools and libraries listed below should provide users with the ability to access and utilize these and many other features of IPMI.</p>
<h2>Getting Started with IPMI</h2>
<p>IPMI can be used in-band (i.e. running on a machine locally) or out-of-band (i.e. connecting remotely). </p>
<p> Most FreeIPMI tools can operate in-band by using one of the in-band drivers included. These in-band drivers include a direct KCS interface driver, a Linux SSIF driver through the SSIF device (i.e. /dev/i2c-0), the OpenIPMI Linux kernel driver (i.e. /dev/ipmi0), and the Sun/Solaris BMC driver (i.e. /dev/bmc). If your system requires the use of installed drivers, those appropriate modules must be installed ahead of time. However, most systems should automatically load these drivers when appropriate. </p>
<p> Under most scenarios, the FreeIPMI tools should automatically discover which in-band interface to use and the proper settings to use. Users may execute the tools on the command line to begin using them. Some motherboards may require you to determine driver type, addresses, paths, etc. on your own and pass them as command line options to the tools. You may use <code><a href="/docs/linux/man/8-ipmi-locate/">ipmi-locate</a>(8)</code> to help determine this information. Other tools such as <code><a href="/docs/linux/man/8-dmidecode/">dmidecode</a>(8)</code> may also provide this information. </p>
<p> To use IPMI out-of-band with tools such as <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8)</code> or <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8),</code> the remote machine&#8217;s BMC must first be configured for out of band communication. Typically, this involves setting a username, password, IP address, MAC address, and a few other parameters. This can be done using the tool <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> Additional information on how to configure with <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> can be found in the <code><a href="/docs/linux/man/5-bmc-config-conf/">bmc-config.conf</a>(5)</code> manpage. Some vendors may pre-configure their motherboards with default values so that <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> can be used remotely to configure the machine. However, most of the time, the BMC must be configured in-band before out-of-band access can be allowed (for example, the correct IP address and MAC address must be configured). </p>
<p> In order to remotely connect to a machine, you typically must specify the host, username, and password for the tool in order to connect. Depending on configuration settings, a K_g key, privilege level, authentication type, cipher suite id, or protocol version may need to be specified. </p>
<p> Some vendors may have not implemented IPMI properly and a workaround must be specified into FreeIPMI to ensure the tool can execute properly. For example, a fair number of vendors have populated their FRU records with invalid checksums. To properly ignore these set of checksums a <i>skipchecks</i> workaround has been added to <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> Please see each of the tool manpages to see a list of available workarounds. </p>
<p> Additional information, examples, and general trouble-shooting can be found in each of the tool manpages.</p>
<h2>General Use</h2>
<p>The primary tools that most users of FreeIPMI will be interested in for system management are the following: </p>
<p> <code>Ipmi-sensors</code> </p>
<p> A tool to read IPMI sensor readings to aid in system monitoring. </p>
<p> <code>Ipmi-sel</code> </p>
<p> A tool to read and manage IPMI System Event Log (SEL) records to aid in system debugging. </p>
<p> <code>Ipmipower</code> </p>
<p> A tool for remote power control. </p>
<p> <code>Ipmiconsole</code> </p>
<p> A tool for Serial-over-Lan (SOL) console access. </p>
<p> Many other tools and libraries are listed below that cover additional features and areas of IPMI. </p>
<p> Additional information, examples, and general trouble-shooting can be found in each of the tool manpages.</p>
<h2>Configuration</h2>
<p>In order to avoid typing in a long list of command line options to specify IPMI communication requirements everytime a command is executed (e.g. driver paths, usernames, passwords, etc.), an alternate set of default values can be set for most FreeIPMI tools in the FreeIPMI configuration file. See <code><a href="/docs/linux/man/5-freeipmi-conf/">freeipmi.conf</a>(5)</code> for more information.</p>
<h2>HPC Support</h2>
<p>Much of FreeIPMI was written with HPC support in mind. The configuration tools ( <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8),</code> and <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8)</code> ) come with file input/output support so that configuration can be copied and verified across nodes in a cluster. Most tools (like <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8)</code> and <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8)</code> ) come with hostrange support so multiple hosts can be specified on the command line at the same time and IPMI can be executed against the hosts in parallel. See tool manpages for more information. Also see the document <i>freeipmi-hostrange.txt</i> for detailed usage and explanation. <code><a href="/docs/linux/man/8-ipmi-sensors/">Ipmi-sensors</a>(8)</code> and the <code><a href="/docs/linux/man/3-libipmimonitoring/">libipmimonitoring</a>(3)</code> library support the ability to interpret sensor readings as well as just reporting them. By mapping sensor readings into NOMINAL, WARNING, or CRITICAL states, it makes monitoring sensors easier across large numbers of nodes.</p>
<h2>Development</h2>
<p>For information on the libraries that can be used to program IPMI applications with, please see <code><a href="/docs/linux/man/3-libfreeipmi/">libfreeipmi</a>(3),</code> <code><a href="/docs/linux/man/3-libipmiconsole/">libipmiconsole</a>(3),</code> <code><a href="/docs/linux/man/3-libipmimonitoring/">libipmimonitoring</a>(3),</code> <code>and <a href="/docs/linux/man/3-libipmidetect/">libipmidetect</a>(3).</code> Or see the document <i>freeipmi-libraries.txt</i>.</p>
<h2>Project Tools</h2>
<p>The following tools are distributed and supported by FreeIPMI. </p>
<p> <code>Bmc-info</code> </p>
<p> A tool to read information about a BMC such as device version numbers, device support, and globally unique IDs (guids). </p>
<p> <code>Bmc-config</code> </p>
<p> A tool to configure general BMC and IPMI information. Supports configuration of usernames, passwords, networking information, security, Serial-over-LAN (SOL), and other core fields. </p>
<p> <code>Bmc-watchdog</code> </p>
<p> A tool/daemon to manage a BMC Watchdog. This tool is typically used for system timeout management and automatic system restarts in the event of a system crash. </p>
<p> <code>Ipmi-chassis</code> </p>
<p> A tool to manage/monitor a chassis, such as chassis power, identification (i.e. LED control), and status. </p>
<p> <code>Ipmi-fru</code> </p>
<p> A tool to read field replaceable unit (FRU) information from a motherboard/machine. </p>
<p> <code>Ipmi-sel</code> </p>
<p> A tool to read and manage IPMI System Event Log (SEL) records. SEL records store system event information and may be useful for debugging problems. </p>
<p> <code>Ipmi-sensors</code> </p>
<p> A tool to read IPMI sensor readings and sensor data repository (SDR) information. </p>
<p> <code>Ipmipower</code> </p>
<p> A tool for remote power control. </p>
<p> <code>Ipmiconsole</code> </p>
<p> A tool for Serial-over-Lan (SOL) console access. </p>
<p> <code>Ipmi-raw</code> </p>
<p> A tool that provides hex input/output of IPMI commands. </p>
<p> <code>Ipmi-locate</code> </p>
<p> A tool that can probe for information about the location of a BMC device, such as device addresses. </p>
<p> <code>Ipmi-chassis-config</code> </p>
<p> A tool to configure IPMI chassis information. Supports configuration of boot device, power restore policy, and other chassis related fields. </p>
<p> <code>Ipmi-pef-config</code> </p>
<p> A tool to configure Platform Event Filtering (PEF) information. </p>
<p> <code>Ipmi-pet</code> </p>
<p> A tool to parse and interpret Platform Event Traps (PET). </p>
<p> <code>Ipmi-sensors-config</code> </p>
<p> A tool to configure IPMI sensors. Supports configuration of sensor thresholds, sensor events, and other sensor related fields. </p>
<p> <code>Ipmi-dcmi</code> </p>
<p> A tool to perform Data Center Manageability Interface (DCMI) IPMI extension commands. Supports extensions for asset management and power usage management. </p>
<p> <code>Bmc-device</code> </p>
<p> A tool to perform advanced BMC commands, such as resetting the BMC, configuring ACPI, configuring SDR/SEL time, manually generating events, re-arming sensors, and configuring manufacturer settings. </p>
<p> <code>Ipmiping</code> </p>
<p> An IPMI ping tool for debugging. </p>
<p> <code>Rmcpping</code> </p>
<p> A RMCP ping tool for debugging. </p>
<p> <code>Ipmi-oem</code> </p>
<p> An IPMI tool for OEM specific commands. </p>
<p> <code>Ipmidetect/Ipmidetectd</code> </p>
<p> A tool and daemon for IPMI node detection. </p>
<p> <code>Ipmiseld</code> </p>
<p> A daemon that regularly polls the SEL and stores the events to the local syslog. </p>
<p> Additional information, examples, and general trouble-shooting can be found in each of the tool manpages.</p>
<h2>Project Libraries</h2>
<p>The following libraries are distributed and supported by FreeIPMI. </p>
<p> <code>Libfreeipmi</code> </p>
<p> A C library that includes KCS, SSIF, OpenIPMI Linux, and Solaris BMC drivers, IPMI 1.5 and IPMI 2.0 LAN communication interfaces, IPMI packet building utilities, IPMI command utilities, and utilities for reading/interpreting/managing IPMI. </p>
<p> <code>Libipmiconsole</code> </p>
<p> A library for Serial-over-Lan (SOL) console access. SOL console access is abstracted into a file descriptor interface, so users may read and write console data through a file descriptor. </p>
<p> <code>Libipmimonitoring</code> </p>
<p> A library for sensor monitoring that abstracts away most IPMI details. </p>
<p> <code>Libipmidetect</code> </p>
<p> A library for IPMI node detection.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2003-2012 FreeIPMI Core Team. </p>
<p> FreeIPMI is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-libfreeipmi/">libfreeipmi</a>(3), <a href="/docs/linux/man/3-libipmiconsole/">libipmiconsole</a>(3), <a href="/docs/linux/man/3-libipmidetect/">libipmidetect</a>(3), <a href="/docs/linux/man/3-libipmimonitoring/">libipmimonitoring</a>(3), <a href="/docs/linux/man/5-freeipmi-conf/">freeipmi.conf</a>(5), <a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8), <a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8), <a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8), <a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8), <a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8), <a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8), <a href="/docs/linux/man/8-ipmi-locate/">ipmi-locate</a>(8), <a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8), <a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8), <a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8), <a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8), <a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8), <a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8), <a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8), <a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8), <a href="/docs/linux/man/8-ipmidetect/">ipmidetect</a>(8), <a href="/docs/linux/man/8-ipmiping/">ipmiping</a>(8), <a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8), <a href="/docs/linux/man/8-rmcpping/">rmcpping</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
