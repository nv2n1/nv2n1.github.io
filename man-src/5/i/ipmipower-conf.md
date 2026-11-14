---
title: "ipmipower-conf(5)"
name: "ipmipower-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipmipower-conf/"
description: "freeipmi.conf – specify default values to FreeIPMI"
---

<p>freeipmi.conf &#8211; specify default values to FreeIPMI</p>
<h2>Description</h2>
<p>The <code>FreeIPMI</code> configuration file can be used to set alternate default values to many <code>FreeIPMI</code> tools so values don&#8217;t have to be configured on the command line. This allows users to avoid typing in a long list of command line options everytime a command is executed. It can also be used to hide usernames, passwords, and other sensitive information from the <code><a href="/docs/linux/man/1-ps/">ps</a>(1)</code> command. </p>
<p> Currently, the tools that can be configured with the configuration file are: <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8),</code> <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8),</code> <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8),</code> <code><a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8),</code> <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8),</code> and <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> </p>
<p> By default, the configuration file is stored at /etc/freeipmi//freeipmi.conf. But users may select a different configuration file at the command line with the &#8211;config-file option. </p>
<p> Values specified on the command line override the configuration values specified in the configuration file.</p>
<h2>Format</h2>
<p>The configuration options that can be specified in the configuration file are listed below. Each configuration option must be listed on a separate line. Arguments for an option are separated by any amount of whitespace. Multiple arguments are also separated by whitespace. Comments can be marked by using the pound sign (&quot;#&quot;) character, and lines can be continued on the next using backslash (&quot;\&quot;). </p>
<p> Note that it is possible to list the username, password and other potentially sensitive information in the configuration file. If this data is stored in a configuration file, system administrators should limit access to this file.</p>
<h2>General Options</h2>
<p>The following options are options generally available to all tools, although specific options may be ignored by some. (For example, <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8)</code> and <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8)</code> do not perform in-band communication, therefore they would ignore in-band communication options. Similarly <code><a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8)</code> does not perform out-of-band communication, therefore it would ignore all out-of-band options).</p>
<dl>
<dt><code>driver-type</code> <i>IPMIDRIVER</i></p>
<dd>Specify the default driver type to use.</p>
<dt><code>disable-auto-probe</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if IPMI devices should be probed for default settings.</p>
<dt><code>driver-address</code> <i>DRIVER-ADDRESS</i></p>
<dd>Specify the default in-band driver address to use.</p>
<dt><code>driver-device</code> <i>DEVICE</i></p>
<dd>Specify the default in-band driver device path to use.</p>
<dt><code>register-spacing</code> <i>REGISTER-SPACING</i></p>
<dd>Specify the default in-band driver register spacing to use.</p>
<dt><code>target-channel-number</code> <i>CHANNEL-NUMBERFR</p>
<dd>Specify the default in-band driver target channel number.</p>
<dt></i><code>target-slave-address</code> <i>SLAVE-ADDRESSFR</p>
<dd>Specify the default in-band driver target slave address.</p>
<dt></i><code>username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use.</p>
<dt><code>password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use.</p>
<dt><code>k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>session-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify the default session timeout length to use in milliseconds.</p>
<dt><code>retransmission-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify the default retransmission timeout length to use in milliseconds.</p>
<dt><code>authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use. Multiple workarounds can be specified separated by whitespace. Please see tool manpages for details about available workarounds for each tool. The following workarounds are supported: assumeio, spinpoll, idzero, forcepermsg, unexpectedauth, endianseq, noauthcodecheck, authcap, nochecksumcheck, intel20, supermicro20, sun20, opensesspriv, integritycheckvalue, assumemaxsdrrecordcount, solpayloadsize, solport, solstatus, skipchecks, assumesystemevent, discretereading, ignorescanningdisabled, assumebmcowner, ignoreauthcode, slowcommit, veryslowcommit, solchannelassumelanchannel, ignorestateflag, malformedack.</dl>
<h2>Sdr Options</h2>
<p>The following options are specific to tools that use the sensor data repository (SDR). They will be ignored by all other tools.</p>
<dl>
<dt><code>quiet-cache</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if cache creation/deletion information should not be output by default.</p>
<dt><code>sdr-cache-directory</code> <i>DIRECTORY</i></p>
<dd>Specify the default sdr cache directory to use.</dl>
<h2>Hostranged Options</h2>
<p>The following options are specific to tools that support hostranged output. They will be ignored by all other tools.</p>
<dl>
<dt><code>buffer-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if hostranged output should be buffered by default.</p>
<dt><code>consolidate-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if hostranged output should be consolidated by default.</p>
<dt><code>fanout</code> <i>COUNT</i></p>
<dd>Specify the default multiple host fanout to use.</p>
<dt><code>eliminate</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if undetected hosts should be eliminated by default.</p>
<dt><code>always-prefix</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should be always prefixed by default.</dl>
<h2>Bmc-Config Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>bmc-config-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>bmc-config-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>bmc-config-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>bmc-config-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>bmc-config-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>bmc-config-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>bmc-config-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> manpage for available workarounds.</p>
<dt><code>bmc-config-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8).</code></dl>
<h2>Bmc-Device Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>bmc-device-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>bmc-device-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>bmc-device-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>bmc-device-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>bmc-device-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>bmc-device-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>bmc-device-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8)</code> manpage for available workarounds.</dl>
<h2>Bmc-Info Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>bmc-info-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>bmc-info-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>bmc-info-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>bmc-info-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>bmc-info-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>bmc-info-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>bmc-info-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8)</code> manpage for available workarounds.</p>
<dt><code>bmc-info-interpret-oem-data</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>bmc-info</code> should attempt to interpret OEM data by default or not.</dl>
<h2>Bmc-Watchdog Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>bmc-watchdog-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8)</code> manpage for available workarounds.</p>
<dt><code>bmc-watchdog-verbose-logging</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if logging will be verbose by default.</p>
<dt><code>bmc-watchdog-no-logging</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if logging will be disabled by default.</dl>
<h2>Ipmi-Chassis Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-chassis-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-chassis-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-chassis-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-chassis-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-chassis-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-chassis-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-chassis-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8)</code> manpage for available workarounds.</dl>
<h2>Ipmi-Chassis-Config Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-chassis-config-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-chassis-config-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-chassis-config-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-chassis-config-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-chassis-config-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-chassis-config-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-chassis-config-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-chassis-config-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-chassis-config/">ipmi-chassis-config</a>(8).</code></dl>
<h2>Ipmi-Dcmi Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-dcmi-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-dcmi-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-dcmi-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-dcmi-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-dcmi-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-dcmi-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-dcmi-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-dcmi/">ipmi-dcmi</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-dcmi-interpret-oem-data</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-dcmi</code> should attempt to interpret OEM data by default or not.</dl>
<h2>Ipmi-Fru Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-fru-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-fru-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-fru-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-fru-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-fru-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-fru-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-fru-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-fru-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</code></p>
<dt><code>ipmi-fru-bridge-fru</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if FRU entries on other controllers should be read by default or not.</p>
<dt><code>ipmi-fru-interpret-oem-data</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-fru</code> should attempt to interpret OEM data by default or not.</dl>
<h2>Ipmi-Oem Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-oem-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-oem-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-oem-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-oem-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-oem-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-oem-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-oem-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-oem-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8).</code></dl>
<h2>Ipmi-Pef-Config Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-pef-config-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-pef-config-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-pef-config-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-pef-config-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-pef-config-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-pef-config-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-pef-config-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-pef-config-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8).</code></dl>
<h2>Ipmi-Pet Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-pet-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-pet-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-pet-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-pet-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-pet-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-pet-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-pet-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-pet-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-pet/">ipmi-pet</a>(8).</code></p>
<dt><code>ipmi-pet-output-event-severity</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-pet</code> should output the event severity state by default.</p>
<dt><code>ipmi-pet-output-event-state</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-pet</code> should output the event state state by default.</p>
<dt><code>ipmi-pet-event-state-config-file</code> <i>FILE</i></p>
<dd>Specify the default event state configuration file.</p>
<dt><code>ipmi-pet-interpret-oem-data</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-pet</code> should attempt to interpret OEM data by default or not.</p>
<dt><code>ipmi-pet-entity-sensor-names</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output of sensor names should include entity ids and instances by default or not.</p>
<dt><code>ipmi-pet-no-sensor-type-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output of the sensor type should be output by default or not.</p>
<dt><code>ipmi-pet-comma-separated-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should be comma separated by default or not.</p>
<dt><code>ipmi-pet-no-header-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if column headers should be output by default or not.</p>
<dt><code>ipmi-pet-non-abbreviated-units</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should have units abbreviated by default or not.</dl>
<h2>Ipmi-Raw Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-raw-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-raw-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-raw-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-raw-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-raw-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-raw-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-raw-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8)</code> manpage for available workarounds.</dl>
<h2>Ipmi-Sel Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-sel-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-sel-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-sel-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-sel-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-sel-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-sel-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-sel-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-sel-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code></p>
<dt><code>ipmi-sel-types</code> <i>TYPE-LIST</i></p>
<dd>Specify default types to show SEL events for. Multiple types can be specified separated by whitespace. Users may specify sensor types by string or by number (decimal or hex). Please see <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8)</code> <i>&#8211;list-types</i> option to see possible string input types.</p>
<dt><code>ipmi-sel-exclude-types</code> ENSOR-TYPES-LIST Specify</p>
<dd>default sensor types to not show SEL events for. Multiple sensor types can be specified separated by whitespace. Users may specify sensor types by string or by number. Please see <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8)</code> <i>&#8211;list-types</i> option to see possible string input types.</p>
<dt><code>ipmi-sel-system-event-only</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should only include system event records.</p>
<dt><code>ipmi-sel-oem-event-only</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should only include OEM event records.</p>
<dt><code>ipmi-sel-output-manufacturer-id</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output of OEM event records should include manufacturer ID by default or not.</p>
<dt><code>ipmi-sel-output-event-state</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sel</code> should output the event state state by default.</p>
<dt><code>ipmi-sel-event-state-config-file</code> <i>FILE</i></p>
<dd>Specify the default event state configuration file.</p>
<dt><code>ipmi-sel-interpret-oem-data</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sel</code> should attempt to interpret OEM data by default or not.</p>
<dt><code>ipmi-sel-output-oem-event-strings</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sel</code> should output OEM event strings by default or not.</p>
<dt><code>ipmi-sel-entity-sensor-names</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output of sensor names should include entity ids and instances by default or not.</p>
<dt><code>ipmi-sel-no-sensor-type-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output of the sensor type should be output by default or not.</p>
<dt><code>ipmi-sel-comma-separated-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should be comma separated by default or not.</p>
<dt><code>ipmi-sel-no-header-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if column headers should be output by default or not.</p>
<dt><code>ipmi-sel-non-abbreviated-units</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should have units abbreviated by default or not.</p>
<dt><code>ipmi-sel-legacy-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should be in legacy format by default or not.</dl>
<h2>Ipmi-Sensors Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-sensors-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-sensors-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-sensors-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-sensors-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-sensors-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-sensors-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-sensors-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-sensors-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code></p>
<dt><code>ipmi-sensors-quiet-readings</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if sensor reading values and thresholds should not be output by default.</p>
<dt><code>ipmi-sensors-record-ids</code> ECORD-IDS-LIST</p>
<dd>Specify default record ids to show sensor outputs for. Multiple record ids can be specified separated by whitespace.</p>
<dt><code>ipmi-sensors-exclude-record-ids</code> ECORD-IDS-LIST</p>
<dd>Specify default record ids to not show sensor outputs for. Multiple record ids can be specified separated by whitespace.</p>
<dt><code>ipmi-sensors-types</code> <i>TYPE-LIST</i></p>
<dd>Specify default types to show sensor outputs for. Multiple types can be specified separated by whitespace. Users may specify sensor types by string or by number (decimal or hex). Please see <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8)</code> <i>&#8211;list-types</i> option to see possible string input types.</p>
<dt><code>ipmi-sensors-exclude-types</code> ENSOR-TYPES-LIST Specify</p>
<dd>default sensor types to not show sensor outputs for. Multiple sensor types can be specified separated by whitespace. Users may specify sensor types by string or by number. Please see <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8)</code> <i>&#8211;list-types</i> option to see possible string input types.</p>
<dt><code>ipmi-sensors-bridge-sensors</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if non-BMC sensors should be bridged by default or not.</p>
<dt><code>ipmi-sensors-shared-sensors</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if shared sensors should be output by default or not.</p>
<dt><code>ipmi-sensors-interpret-oem-data</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sensors</code> should attempt to interpret OEM data by default or not.</p>
<dt><code>ipmi-sensors-ignore-not-available-sensors</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sensors</code> should ignore not-available (i.e. N/A) sensors by default.</p>
<dt><code>ipmi-sensors-ignore-unrecognized-events</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sensors</code> should ignore unrecognized events (i.e. &#8216;Unrecognized Event&#8217;) in sensors output by default.</p>
<dt><code>ipmi-sensors-output-event-bitmask</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sensors</code> should output event bitmasks instead of string representations by default.</p>
<dt><code>ipmi-sensors-output-sensor-state</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sensors</code> should output the sensor state by default.</p>
<dt><code>ipmi-sensors-sensor-state-config-file</code> <i>FILE</i></p>
<dd>Specify the default sensor state configuration file.</p>
<dt><code>ipmi-sensors-entity-sensor-names</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output of sensor names should include entity ids and instances by default or not.</p>
<dt><code>ipmi-sensors-output-sensor-thresholds</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if <code>ipmi-sensors</code> should output sensor thresholds by default.</p>
<dt><code>ipmi-sensors-no-sensor-type-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output of the sensor type should be output by default or not.</p>
<dt><code>ipmi-sensors-comma-separated-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should be comma separated by default or not.</p>
<dt><code>ipmi-sensors-no-header-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if column headers should be output by default or not.</p>
<dt><code>ipmi-sensors-non-abbreviated-units</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should have units abbreviated by default or not.</p>
<dt><code>ipmi-sensors-legacy-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should be in legacy format by default or not.</p>
<dt><code>ipmi-sensors-ipmimonitoring-legacy-output</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if output should be in <code>ipmimonitoring</code> legacy format by default or not.</dl>
<h2>Ipmi-Sensors-Config Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmi-sensors-config-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmi-sensors-config-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmi-sensors-config-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmi-sensors-config-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmi-sensors-config-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmi-sensors-config-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmi-sensors-config-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmi-sensors-config-verbose-count</code> <i>COUNT</i></p>
<dd>Specify default verbose count to use for <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code></dl>
<h2>Ipmiconsole Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmiconsole-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmiconsole-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmiconsole-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmiconsole-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmiconsole-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmiconsole-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmiconsole-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmiconsole-escape-char</code> <i>CHAR</i></p>
<dd>Specify the default escape character.</p>
<dt><code>ipmiconsole-dont-steal</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if in use SOL sessions should not be stolen by default.</p>
<dt><code>ipmiconsole-serial-keepalive</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if serial keepalive should be enabled by default.</p>
<dt><code>ipmiconsole-serial-keepalive-empty</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if serial keepalive empty should be enabled by default.</p>
<dt><code>ipmiconsole-sol-payload-instance</code> <i>NUM</i></p>
<dd>Specify the default SOL payload instance.</p>
<dt><code>ipmiconsole-deactivate-all-instances</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if SOL deactivate should deactivate all instances by default.</p>
<dt><code>ipmiconsole-lock-memory</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if memory should be locked by default.</dl>
<h2>Ipmipower Options</h2>
<p>The following options are specific to <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> They will be ignored by other tools.</p>
<dl>
<dt><code>ipmipower-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use for <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> If specified, will override the general option <code>username</code> above.</p>
<dt><code>ipmipower-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use for <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> If specified, will override the general option <code>password</code> above.</p>
<dt><code>ipmipower-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use for <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> If specified, will override the general option <code>k_g</code> above. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>ipmipower-authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the default authentication type to use for <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> If specified, will override the general option <code>authentication-type</code> above. The following authentication types are supported: NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5.</p>
<dt><code>ipmipower-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use for <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> If specified, will override the general option <code>cipher-suite-id</code> above. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>ipmipower-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use for <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> If specified, will override the general option <code>privilege-level</code> above. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>ipmipower-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use for <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8).</code> If specified, will override the general options <code>workaround-flags</code> above. Multiple workarounds can be specified separated by whitespace. Please see <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8)</code> manpage for available workarounds.</p>
<dt><code>ipmipower-on-if-off</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if on-if-off functionality is enabled or disabled by default.</p>
<dt><code>ipmipower-wait-until-on</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if wait-until-on functionality is enabled or disabled by default.</p>
<dt><code>ipmipower-wait-until-off</code> <i>ENABLE|DISABLE</i></p>
<dd>Specify if wait-until-off functionality is enabled or disabled by default.</p>
<dt><code>ipmipower-oem-power-type</code> <i>OEM-POWER-TYPE</i></p>
<dd>Specify OEM power type to be used.</p>
<dt><code>ipmipower-retransmission-wait-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify the default retransmission wait timeout length to use in milliseconds.</p>
<dt><code>ipmipower-retransmission-backoff-count</code> <i>COUNT</i></p>
<dd>Specify the default retransmission backoff count to use for retransmissions.</p>
<dt><code>ipmipower-ping-interval</code> <i>MILLISECONDS</i></p>
<dd>Specify the default ping interval length to use in milliseconds.</p>
<dt><code>ipmipower-ping-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify the default ping timeout length to use in milliseconds.</p>
<dt><code>ipmipower-ping-packet-count</code> <i>COUNT</i></p>
<dd>Specify the default ping packet count size to use.</p>
<dt><code>ipmipower-ping-percent</code> <i>PERCENT</i></p>
<dd>Specify the default ping percent value to use.</p>
<dt><code>ipmipower-ping-consec-count</code> <i>COUNT</i></p>
<dd>Specify the default ping consecutive count value to use.</dl>
<h2>Files</h2>
<p>/etc/freeipmi//freeipmi.conf</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2003-2012 FreeIPMI Core Team. </p>
<p> FreeIPMI is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8), <a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8), <a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8), <a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8), <a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8), <a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8), <a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8), <a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8), <a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8), <a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8), <a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8), <a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8), <a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8), <a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
