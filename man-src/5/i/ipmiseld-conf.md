---
title: "ipmiseld-conf(5)"
name: "ipmiseld-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipmiseld-conf/"
description: "ipmiseld.conf – ipmiseld configuration file"
---

<p>ipmiseld.conf &#8211; ipmiseld configuration file</p>
<h2>Description</h2>
<p>The <code>ipmiseld</code> configuration file configures the <code>ipmiseld</code> daemon. </p>
<p> The default configuration file loaded is /etc/freeipmi//ipmiseld.conf. </p>
<p> The configuration options that can be specified in the configuration file are listed below. Each configuration option must be listed on a separate line. Arguments for an option are separated by any amount of whitespace. Multiple arguments are also separated by whitespace. Comments can be marked by using the pound sign (&quot;#&quot;) character, and lines can be continued on the next using backslash (&quot;\&quot;). </p>
<p> Note that it is possible to list the username, password and other potentially sensitive information in the configuration file. If this data is stored in a configuration file, system administrators should limit access to this file.</p>
<h2>Ipmiseld Configuration Options</h2>
<dl>
<dt><code>driver-type</code> <i>IPMIDRIVER</i></p>
<dd>Specify the driver type to use.</p>
<dt><code>disable-auto-probe</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if IPMI devices should be probed for settings.</p>
<dt><code>driver-address</code> <i>DRIVER-ADDRESS</i></p>
<dd>Specify the in-band driver address to use.</p>
<dt><code>driver-device</code> <i>DEVICE</i></p>
<dd>Specify the in-band driver device path to use.</p>
<dt><code>register-spacing</code> <i>REGISTER-SPACING</i></p>
<dd>Specify the in-band driver register spacing to use.</p>
<dt><code>target-channel-number</code> <i>CHANNEL-NUMBERFR</p>
<dd>Specify the in-band driver target channel number.</p>
<dt></i><code>target-slave-address</code> <i>SLAVE-ADDRESSFR</p>
<dd>Specify the in-band driver target slave address.</p>
<dt></i><code>hostname</code> <i>IPMIHOST1,IPMIHOST2,&#8230;</i></p>
<dd>Specify the remote host(s) to communicate with. Multiple hostnames may be separated by comma or may be specified in a range format.</p>
<dt><code>username</code> <i>USERNAME</i></p>
<dd>Specify the username to use.</p>
<dt><code>password</code> <i>PASSWORD</i></p>
<dd>Specify the password to use.</p>
<dt><code>k_g</code> <i>str</i></p>
<dd>Specify the BMC key (K_g) to use. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>session-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify the session timeout length to use in milliseconds.</p>
<dt><code>retransmission-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify the retransmission timeout length to use in milliseconds.</p>
<dt><code>authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the authentication type to use. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the cipher suite id to use. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the privilege type to use. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify workaround flags to use. Multiple workarounds can be specified separated by whitespace. Please see tool manpages for details about available workarounds for each tool. The following workarounds are supported: assumeio, spinpoll, idzero, forcepermsg, unexpectedauth, endianseq, authcap, intel20, supermicro20, sun20, opensesspriv, integritycheckvalue, assumesystemevent.</p>
<dt><code>verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code></p>
<dt><i>sensors-types</i> <i>TYPE-LIST</i></p>
<dd>Specify sensor types of SEL events to log. Multiple types can be specified separated by whitespace. Users may specify sensor types by string or by number (decimal or hex). Please see <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8)</code> <i>&#8211;list-types</i> option to see possible string input types.</p>
<dt><i>exclude-sensor-types</i> ENSOR-TYPES-LIST</p>
<dd>Specify sensor types of SEL events to not log. default sensor types to not show sensor outputs for. Multiple sensor types can be specified separated by whitespace. Users may specify sensor types by string or by number. Please see <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8)</code> <i>&#8211;list-types</i> option to see possible string input types.</p>
<dt><code>system-event-only</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should only include system event records.</p>
<dt><code>oem-event-only</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should only include OEM event records.</p>
<dt><code>event-state-config-file</code> <i>FILE</i></p>
<dd>Specify the event state configuration file.</p>
<dt><code>interpret-oem-data</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmiseld</code> should attempt to interpret OEM data or not.</p>
<dt><code>entity-sensor-names</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output of sensor names should include entity ids and instances or not.</p>
<dt><code>non-abbreviated-units</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should have units abbreviated by default or not.</p>
<dt><code>event-state-filter</code> <i>FILTERSTRING</i></p>
<dd>Specify event states to be filtered out and not logged.</p>
<dt><code>&#8211;warning-threshold</code> <i>PERCENTINT</i></p>
<dd>Specify SEL fullness warning threshold as an integer percentage.</p>
<dt><code>&#8211;clear-threshold</code> <i>PERCENTINT</i></p>
<dd>Specify SEL fullness clear threshold as an integer percentage.</p>
<dt><code>system-event-format</code> <i>FORMATSTRING</i></p>
<dd>Specify the format of the log output when a SEL system event is encountered.</p>
<dt><code>oem-timestamped-event-format</code> <i>FORMATSTRING</i></p>
<dd>Specify the format of the log output when a SEL OEM timestamped event is encountered.</p>
<dt><code>oem-non-timestamped-event-format</code> <i>FORMATSTRING</i></p>
<dd>Specify the format of the log output when a SEL OEM non-timestamped event is encountered.</p>
<dt><code>poll-interval</code> <i>SECONDS</i></p>
<dd>Specify the poll interval to check the SEL for new events.</p>
<dt><code>log-facility</code> <i>STRING</i></p>
<dd>Specify the log facility to use.</p>
<dt><code>log-priority</code> <i>STRING</i></p>
<dd>Specify the log priority to use.</p>
<dt><code>cache-directory</code> <i>DIRECTORY</i></p>
<dd>Specify the cache directory to use.</p>
<dt><code>ignore-sdr</code> <i>DISABLE</i></p>
<dd>Specify if the SDR should be ignored.</p>
<dt><code>re-download-sdr</code> <i>DISABLE</i></p>
<dd>Specify if the SDR should be re-downloaded on start.</p>
<dt><code>clear-sel</code> <i>DISABLE</i></p>
<dd>Specify if the SEL should be cleared on start.</p>
<dt><code>threadpool-count</code> <i>NUM</i></p>
<dd>Specify the threadpool count for parallel SEL polling.</dl>
<h2>Files</h2>
<p>/etc/freeipmi//ipmiseld.conf</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2012 Lawrence Livermore National Security, LLC.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiseld/">ipmiseld</a>(8), <a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
