---
title: "apcupsd(8)"
name: "apcupsd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apcupsd/"
description: "apcupsd – a daemon for controlling most APC UPSes"
---

<p><code>apcupsd </code> &#8211; a daemon for controlling most APC UPSes</p>
<h2>Synopsis</h2>
<p>[-<code>b </code> ] [-<code>d </code><i>level | &#8211;</i><code>-debug </code><i>level</i> ] [-<code>f </code><i>file | &#8211;</i><code>-config-file </code><i>file</i> ] [-<code>P </code><i>file | &#8211;</i><code>-pid-file </code><i>file</i> ] [-<code>p | -kill-on-powerfail | t | -term-on-powerfail</code> ] [-<code>R</code> ]<br />
 [-<code>k | -killpower | -hibernate | o | -power-off </code> ]<br />
 [-<code>h | -help</code> ]<br />
 [-<code>V | -version</code> ] </p>
<h2>Description</h2>
<p>The daemon controls the operation of most American Power Conversion Corp (APC) UPSes. During a power failure, informs users about the loss of utility power and that a shutdown may occur. If utility power is not restored, a system shutdown will follow when the battery is exhausted, a specified timeout expires, a specified battery charge percentage is reached, or a specified battery runtime (based on internal UPS calculations and determined by power consumption rates) expires. If the utility power is restored before one of the these shutdown conditions is met, will inform users of this and the shutdown will generally be cancelled. Refer to the Implementation Notes section below for situations in which the shutdown may not be cancelled. The meaning of the command line options is as follows:</p>
<dl>
<dt><code>-b</code></p>
<dd>Run in the foreground, do not detach and become a daemon.</p>
<dt><code>-d </code><i>level &#8211;</i><code>-debug </code><i>level</i></p>
<dd>Set debugging output level where level is a number greater than zero.</p>
<dt><code>-f </code><i>file &#8211;</i><code>-config-file </code><i>file</i></p>
<dd>Load the specified configuration file. The default configuration file is /etc/apcupsd/apcupsd.conf It must be changed when running more than one copy of on the same computer to control multiple UPSes.</p>
<dt><code>-k | &#8211;killpower | -hibernate</code></p>
<dd>Power down the UPS in hibernate mode after a 10 second delay. This option is normally only used by itself to power down the UPS after a system shutdown has almost completed. In hibernate mode, the UPS will again supply power to the system when the utility power returns.</p>
<dt><code>-o | -power-off</code></p>
<dd>Power down UPS completely. The UPS will not supply power to the system when the utility power returns.</p>
<dt><code>-P </code><i>file &#8211;</i><code>-pid-file </code><i>file</i></p>
<dd>Create the specified process ID file. The default is /var/run/apcupsd.pid It must be changed when running more than one copy of on the same computer to control multiple UPSes.</p>
<dt><code>-p -kill-on-powerfail</code></p>
<dd>commands the UPS to power down in hibernate mode just before starts the system shutdown. This relies on the grace shutdown delay of a Smart-UPS being long enough to allow the system to shutdown completely before the UPS shuts off the power to the system and goes into hibernate mode. This shutdown grace delay is a programmable value stored in a Smart-UPS EEPROM which can be changed using <a href="/docs/linux/man/8-apctest/">apctest</a>(8). In hibernate mode, the UPS will again supply power to the system when the utility power returns. Refer to apcupsd.conf5 for an alternative method using the KILLDELAY configuration directive and the only method available when using a Back-UPS or other UPS operating in simple signalling mode.</p>
<dt><code>-t -term-on-powerfail</code></p>
<dd>exits immediately when it issues the system shutdown command. This behaviour is useful for those systems where it is not possible to insert commands in a halt script to issue the killpower command. Without this option, will wait for the SIGTERM signal from the system shutdown process before exiting.</p>
<dt><code>-R</code></p>
<dd>Put a UPS which runs in smart signalling mode by default (eg a Smart-UPS) into simple signalling mode.</p>
<dt><code>-v -version</code></p>
<dd>Prints the version number and the program help.</p>
<dt><code>-h -help</code></p>
<dd>Prints the program help.  The daemon supports a networking mode called Network Information Server (NIS) &#8212; not related to Sun&#8217;s NIS/YP &#8212; in which the daemon serves status and event information to clients over a network. See the &quot;Running The Network Information Server&quot; section of the apcupsd manual for more information and configuration details on this mode. The daemon also supports a Smart-UPS in SNMP mode provided an APC Web/SNMP or APC PowerNet SNMP card is installed in the UPS&#8217;s SmartSlot. For more information and configuration details on this mode, refer to the &quot;Support for SNMP UPSes&quot; section of the apcupsd manual. </p>
<h2>Implementation Notes</h2>
<p>The shutdown is made by calls to the script /etc/apcupsd/apccontrol by the daemon. Consequently, no changes to /etc/inittab are necessary on Linux as there is no communication between the daemon and the <a href="/docs/linux/man/1-init/">init</a>(1) process. Installation of the daemon modifies the halt script so that at the end of the shutdown process, the daemon will be re-executed to power off the UPS in hibernate mode. </p>
<p> On some operating systems (eg FreeBSD) there is no halt script so apccontrol must be modified to cause the daemon to power off the UPS after a delay. Alternatives are to use the &#8211;kill-on-powerfail command on the command line or refer to apcupsd.conf5 for details of the KILLDELAY configuration directive.</p>
<h2>Configuration</h2>
<p>It will almost certainly be necessary to customise the configuration information in the /etc/apcupsd/apcupsd.conf configuration file to suit your configuration and desired UPS behaviour. </p>
<p> For information on the configuration directives and the format of the configuration file, refer to apcupsd.conf5.</p>
<h2>Events</h2>
<p>generates events when certain conditions occur. These events are sent to the system log and, optionally, to the temporary events file ( /var/log/apcupsd.events ) They also generate a call to the /etc/apcupsd/apccontrol script which in turn will call any custom scripts placed in the /etc/apcupsd directory which may override apccontrol&#8217;s default behaviour. For details of the events and customising apccontrol&#8217;s behaviour, refer to <a href="/docs/linux/man/8-apccontrol/">apccontrol</a>(8).</p>
<h2>Data File Format</h2>
<p>If the DATATIME configuration directive is set to non-zero, will log a data record at the interval defined by the DATATIME directive. This data record is in a format similar to the APC PowerChute software data file format.</p>
<h2>Status Report Format</h2>
<p>The status report output format is simple ASCII. Generally there is a single piece of information on each line of output. The content varies based on the model of UPS being used and, in some cases, the firmware version. This status report is also optionally written the the /etc/apcupsd/apcupsd.status file. Refer to <a href="/docs/linux/man/8-apcaccess/">apcaccess</a>(8) for full details of the status report output.</p>
<h2>Files</h2>
<p>/etc/apcupsd/apcupsd.conf default configuration file </p>
<p> /var/run/apcupsd.pid default process ID file </p>
<p> /var/log/apcupsd.status optional status file </p>
<p> /var/log/apcupsd.events default events file</p>
<h2>See Also</h2>
<p>apcupsd.conf5, <a href="/docs/linux/man/8-apcaccess/">apcaccess</a>(8), <a href="/docs/linux/man/8-apccontrol/">apccontrol</a>(8), <a href="/docs/linux/man/8-apctest/">apctest</a>(8). The HTML apcupsd manual installed on your system or available online at <a rel="nofollow" href="http://www.apcupsd.org/">http://www.apcupsd.org/</a> </p>
<h2>Authors</h2>
<h3>This page</h3>
<p>An Trevor Roydhouse (current) An Andre M. Hedrick An Christopher J. Reimer</p>
<h3>Software</h3>
<p>An Adam Kropelin (current Project Manager and Code Maintainer) An Kern Sibbald (former Project Manager and Code Maintainer) An Riccardo Facchetti (former Project Manager and Code Maintainer) An Andre M. Hedrick (Project Founder and former Code Maintainer)</p>
<h3>Contributors</h3>
<p>An enormous number of users who have devoted their time and energy to this project &#8212; thanks.</p>
