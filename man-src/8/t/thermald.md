---
title: "thermald(8)"
name: "thermald"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thermald/"
description: "thermald – start Linux thermal daemon"
---

<p>thermald &#8211; start Linux thermal daemon</p>
<h2>Synopsis</h2>
<p><code>thermald</code> [ <i>OPTIONS</i> ] </p>
<h2>Description</h2>
<p><code>thermald</code> is a Linux daemon used to prevent the overheating of platforms. This daemon monitors temperature and applies compensation using available cooling methods. </p>
<p> By default, it monitors CPU temperature using available CPU digital temperature sensors and maintains CPU temperature under control, before HW takes aggressive correction action. </p>
<p> Thermal daemon looks for thermal sensors and thermal cooling drivers in the Linux thermal sysfs (/sys/class/thermal) and builds a list of sensors and cooling drivers. Each of the thermal sensors can optionally be binded to a cooling driver by the in kernel drivers. In this case the Linux kernel thermal core can directly take actions based on the temperature trip points, for each sensor and associated cooling device. For example a trip temperature X in a sensor can be associates a cooling driver Y. So when the sensor temperature = X, the cooling driver &quot;Y&quot; is activated. </p>
<p> Thermal daemon allows one to change this relationship or add new one via a thermal configuration file (thermal-conf.xml). This file is automatically created (thermal-conf.xml.auto) and used, if the platform has ACPI thermal relationship table. If not this needs to be manually configured. </p>
<p> For manual configuration refer to the manual page of the thermal-conf.xml. </p>
<p> In some newer platforms the auto creation of the config file is done by a companion tool &quot;dptfxtract&quot;. This tool can be downloaded from &quot;<a rel="nofollow" href="https://github.com/intel/dptfxtract">https://github.com/intel/dptfxtract</a>&quot;. It is suggested as parts of the install process, run dptfxtract. </p>
<p> There can be multiple configuration files. User can select a configuration file via -config-file option to override the default selection. The default selection picks one of the file in the following order: </p>
<p> &#8211; /etc/thermald/thermal-conf.xml.auto </p>
<p> &#8211; /var/run/thermald/thermal-conf.xml.auto </p>
<p> &#8211; /etc/thermald/thermal-conf.xml </p>
<p> (*Assuming configure prefix=/ is used during build.) </p>
<p> There is another companion tool &quot;ThermalMonitor&quot;, which presents a graphical front end. This allows the monitoring of sensors and changing of thermal trips to give the user more control. The source code of &quot;ThermalMonitor&quot; is a part of the thermald github source, in the tools folder.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show help options.</p>
<dt><code>&#8211;version</code></p>
<dd>Print thermald version and exit.</p>
<dt><code>&#8211;no-daemon</code></p>
<dd>Don&#8217;t become a daemon: Default is daemon mode.</p>
<dt><code>&#8211;loglevel=info</code></p>
<dd>log severity: info level and up.</p>
<dt><code>&#8211;loglevel=debug</code></p>
<dd>log severity: debug level and up: Max logging.</p>
<dt><code>&#8211;poll-interval</code></p>
<dd>Poll interval in seconds: Poll for zone temperature changes. To disable polling, set to zero. Polling can only be disabled, if available temperature sensors can notify temperature change asynchronously.</p>
<dt><code>&#8211;dbus-enable</code></p>
<dd>Enable Dbus.</p>
<dt><code>&#8211;exclusive-control</code></p>
<dd>Act as exclusive thermal controller. This will use user-space governor for thermal sysfs and take over control.</p>
<dt><code>&#8211;ignore-cpuid-check</code></p>
<dd>Ignore cpuid check for supported CPU models.</p>
<dt><code>&#8211;config-file</code></p>
<dd>Specify thermal-conf.xml path and ignore default thermal-conf.xml.</p>
<dt><code>&#8211;ignore-default-control</code></p>
<dd>Ignore default CPU temperature control. Strictly follow thermal-conf.xml or thermal-conf.xml.auto.</p>
<dt><code>&#8211;workaround-enabled</code></p>
<dd>Enable special workarounds for RAPL MMIO power limit and TCC offset every 30 seconds. This helps to disable RAPL MMIO when not used and adjust TCC offset in certain Lenovo laptops.</p>
<dt><code>&#8211;disable-active-power</code></p>
<dd>Disable active power management. This will not set active power limits using RAPL MMIO. This may result in constrained performance, if the system boots up with lower power limits.</p>
<dt><code>&#8211;adaptive</code></p>
<dd>Use DPTF adaptive tables when present. This will ignore thermald config via xml files.</p>
<dt><code>&#8211;test-mode</code></p>
<dd>Force use adaptive mode and exit if not supported, instead of restarting in non adaptive mode. This option is primarily for developers.</p>
<dt><code>&#8211;systemd</code></p>
<dd>Assume that thermald is started by systemd. This will prevent running as daemon irrespective of &#8211;no-daemon option.</p>
<dt><code>&#8211;ignore-critical-trip</code></p>
<dd>If the configuration defined a critical temperature point, which is too low, this option will avoid shutting down the system on reaching this temperature limit.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-thermal-conf-xml/">thermal-conf.xml</a>(5) </p>
