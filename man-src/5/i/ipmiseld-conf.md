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
<dt><code>driver-type</code> <i>IPMIDRIVER</i></dt>
<dd>Specify the driver type to use.</dd>
<dt><code>disable-auto-probe</code> <i>ENABLE|DISABLE</i></dt>
<dd>Specify if IPMI devices should be probed for settings.</dd>
<dt><code>driver-address</code> <i>DRIVER-ADDRESS</i></dt>
<dd>Specify the in-band driver address to use.</dd>
<dt><code>driver-device</code> <i>DEVICE</i></dt>
<dd>Specify the in-band driver device path to use.</dd>
<dt><code>register-spacing</code> <i>REGISTER-SPACING</i></dt>
<dd>Specify the in-band driver register spacing to use.</dd>
<dt><code>target-channel-number</code> <i>CHANNEL-NUMBERFR</dt>
<dd>Specify the in-band driver target channel number.</dd>
<dt></i><code>target-slave-address</code> <i>SLAVE-ADDRESSFR</dt>
<dd>Specify the in-band driver target slave address.</dd>
<dt></i><code>hostname</code> <i>IPMIHOST1,IPMIHOST2,&#8230;</i></dt>
<dd>Specify the remote host(s) to communicate with. Multiple hostnames may be separated by comma or may be specified in a range format.</dd>
<dt><code>username</code> <i>USERNAME</i></dt>
<dd>Specify the username to use.</dd>
<dt><code>password</code> <i>PASSWORD</i></dt>
<dd>Specify the password to use.</dd>
<dt><code>k_g</code> <i>str</i></dt>
<dd>Specify the BMC key (K_g) to use. Prefix with &#8216;0x&#8217; to enter the key in hex.</dd>
<dt><code>session-timeout</code> <i>MILLISECONDS</i></dt>
<dd>Specify the session timeout length to use in milliseconds.</dd>
<dt><code>retransmission-timeout</code> <i>MILLISECONDS</i></dt>
<dd>Specify the retransmission timeout length to use in milliseconds.</dd>
<dt><code>authentication-type</code> <i>AUTHENTICATION-TYPE</i></dt>
<dd>Specify the authentication type to use. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</dd>
<dt><code>cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></dt>
<dd>Specify the cipher suite id to use. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</dd>
<dt><code>privilege-level</code> <i>PRIVILEGE-LEVEL</i></dt>
<dd>Specify the privilege type to use. The following privilege levels are supported: USER, OPERATOR, ADMIN.</dd>
<dt><code>workaround-flags</code> <i>WORKAROUNDS</i></dt>
<dd>Specify workaround flags to use. Multiple workarounds can be specified separated by whitespace. Please see tool manpages for details about available workarounds for each tool. The following workarounds are supported: assumeio, spinpoll, idzero, forcepermsg, unexpectedauth, endianseq, authcap, intel20, supermicro20, sun20, opensesspriv, integritycheckvalue, assumesystemevent.</dd>
<dt><code>verbose-count</code> <i>COUNT</i></dt>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code></dd>
<dt><i>sensors-types</i> <i>TYPE-LIST</i></dt>
<dd>Specify sensor types of SEL events to log. Multiple types can be specified separated by whitespace. Users may specify sensor types by string or by number (decimal or hex). Please see <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8)</code> <i>&#8211;list-types</i> option to see possible string input types.</dd>
<dt><i>exclude-sensor-types</i> ENSOR-TYPES-LIST</dt>
<dd>Specify sensor types of SEL events to not log. default sensor types to not show sensor outputs for. Multiple sensor types can be specified separated by whitespace. Users may specify sensor types by string or by number. Please see <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8)</code> <i>&#8211;list-types</i> option to see possible string input types.</dd>
<dt><code>system-event-only</code> <i>ENABLE|DISABLE</i></dt>
<dd>Specify if output should only include system event records.</dd>
<dt><code>oem-event-only</code> <i>ENABLE|DISABLE</i></dt>
<dd>Specify if output should only include OEM event records.</dd>
<dt><code>event-state-config-file</code> <i>FILE</i></dt>
<dd>Specify the event state configuration file.</dd>
<dt><code>interpret-oem-data</code> <i>ENABLE|DISABLE</i></dt>
<dd>Specify if <code>ipmiseld</code> should attempt to interpret OEM data or not.</dd>
<dt><code>entity-sensor-names</code> <i>ENABLE|DISABLE</i></dt>
<dd>Specify if output of sensor names should include entity ids and instances or not.</dd>
<dt><code>non-abbreviated-units</code> <i>ENABLE|DISABLE</i></dt>
<dd>Specify if output should have units abbreviated by default or not.</dd>
<dt><code>event-state-filter</code> <i>FILTERSTRING</i></dt>
<dd>Specify event states to be filtered out and not logged.</dd>
<dt><code>&#8211;warning-threshold</code> <i>PERCENTINT</i></dt>
<dd>Specify SEL fullness warning threshold as an integer percentage.</dd>
<dt><code>&#8211;clear-threshold</code> <i>PERCENTINT</i></dt>
<dd>Specify SEL fullness clear threshold as an integer percentage.</dd>
<dt><code>system-event-format</code> <i>FORMATSTRING</i></dt>
<dd>Specify the format of the log output when a SEL system event is encountered.</dd>
<dt><code>oem-timestamped-event-format</code> <i>FORMATSTRING</i></dt>
<dd>Specify the format of the log output when a SEL OEM timestamped event is encountered.</dd>
<dt><code>oem-non-timestamped-event-format</code> <i>FORMATSTRING</i></dt>
<dd>Specify the format of the log output when a SEL OEM non-timestamped event is encountered.</dd>
<dt><code>poll-interval</code> <i>SECONDS</i></dt>
<dd>Specify the poll interval to check the SEL for new events.</dd>
<dt><code>log-facility</code> <i>STRING</i></dt>
<dd>Specify the log facility to use.</dd>
<dt><code>log-priority</code> <i>STRING</i></dt>
<dd>Specify the log priority to use.</dd>
<dt><code>cache-directory</code> <i>DIRECTORY</i></dt>
<dd>Specify the cache directory to use.</dd>
<dt><code>ignore-sdr</code> <i>DISABLE</i></dt>
<dd>Specify if the SDR should be ignored.</dd>
<dt><code>re-download-sdr</code> <i>DISABLE</i></dt>
<dd>Specify if the SDR should be re-downloaded on start.</dd>
<dt><code>clear-sel</code> <i>DISABLE</i></dt>
<dd>Specify if the SEL should be cleared on start.</dd>
<dt><code>threadpool-count</code> <i>NUM</i></dt>
<dd>Specify the threadpool count for parallel SEL polling.</dd></dl>
<h2>Files</h2>
<p>/etc/freeipmi//ipmiseld.conf</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2012 Lawrence Livermore National Security, LLC.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiseld/">ipmiseld</a>(8), <a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
