---
title: "wpa_supplicant(8)"
name: "wpa_supplicant"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wpa_supplicant/"
description: "wpa_supplicant – Wi-Fi Protected Access client and IEEE 802.1X supplicant"
---

<p>wpa_supplicant &#8211; Wi-Fi Protected Access client and IEEE 802.1X supplicant</p>
<h2>Synopsis</h2>
<p><code>wpa_supplicant</code> [ <code>-BddfhKLqqsTtuvW</code> ] [ <code>-i</code><i>ifname</i> ] [ <code>-c</code><i>config file</i> ] [ <code>-D</code><i>driver</i> ] [ <code>-P</code><i>PID_file</i> ] [ <code>-f</code><i>output file</i> ] </p>
<h2>Overview</h2>
<p>Wireless networks do not require physical access to the network equipment in the same way as wired networks. This makes it easier for unauthorized users to passively monitor a network and capture all transmitted frames. In addition, unauthorized use of the network is much easier. In many cases, this can happen even without user&#8217;s explicit knowledge since the wireless LAN adapter may have been configured to automatically join any available network. </p>
<p> Link-layer encryption can be used to provide a layer of security for wireless networks. The original wireless LAN standard, IEEE 802.11, included a simple encryption mechanism, WEP. However, that proved to be flawed in many areas and network protected with WEP cannot be consider secure. IEEE 802.1X authentication and frequently changed dynamic WEP keys can be used to improve the network security, but even that has inherited security issues due to the use of WEP for encryption. Wi-Fi Protected Access and IEEE 802.11i amendment to the wireless LAN standard introduce a much improved mechanism for securing wireless networks. IEEE 802.11i enabled networks that are using CCMP (encryption mechanism based on strong cryptographic algorithm AES) can finally be called secure used for applications which require efficient protection against unauthorized access. </p>
<p> <code>wpa_supplicant</code> is an implementation of the WPA Supplicant component, i.e., the part that runs in the client stations. It implements WPA key negotiation with a WPA Authenticator and EAP authentication with Authentication Server. In addition, it controls the roaming and IEEE 802.11 authentication/association of the wireless LAN driver. </p>
<p> <code>wpa_supplicant</code> is designed to be a &quot;daemon&quot; program that runs in the background and acts as the backend component controlling the wireless connection. <code>wpa_supplicant</code> supports separate frontend programs and an example text-based frontend, <code>wpa_cli</code>, is included with wpa_supplicant. </p>
<p> Before wpa_supplicant can do its work, the network interface must be available. That means that the physical device must be present and enabled, and the driver for the device must be loaded. The daemon will exit immediately if the device is not already available. </p>
<p> After <code>wpa_supplicant</code> has configured the network device, higher level configuration such as DHCP may proceed. There are a variety of ways to integrate wpa_supplicant into a machine&#8217;s networking scripts, a few of which are described in sections below. </p>
<p> The following steps are used when associating with an AP using WPA:</p>
<dl>
<dt>&bull;</p>
<dd><code>wpa_supplicant</code> requests the kernel driver to scan neighboring BSSes</p>
<dt>&bull;</p>
<dd><code>wpa_supplicant</code> selects a BSS based on its configuration</p>
<dt>&bull;</p>
<dd><code>wpa_supplicant</code> requests the kernel driver to associate with the chosen BSS</p>
<dt>&bull;</p>
<dd>If WPA-EAP: integrated IEEE 802.1X Supplicant completes EAP authentication with the authentication server (proxied by the Authenticator in the AP)</p>
<dt>&bull;</p>
<dd>If WPA-EAP: master key is received from the IEEE 802.1X Supplicant</p>
<dt>&bull;</p>
<dd>If WPA-PSK: <code>wpa_supplicant</code> uses PSK as the master session key</p>
<dt>&bull;</p>
<dd><code>wpa_supplicant</code> completes WPA 4-Way Handshake and Group Key Handshake with the Authenticator (AP)</p>
<dt>&bull;</p>
<dd><code>wpa_supplicant</code> configures encryption keys for unicast and broadcast</p>
<dt>&bull;</p>
<dd>normal data packets can be transmitted and received</dl>
<h2>Supported Features</h2>
<p>Supported WPA/IEEE 802.11i features:</p>
<dl>
<dt>&bull;</p>
<dd>WPA-PSK (&quot;WPA-Personal&quot;)</p>
<dt>&bull;</p>
<dd>WPA with EAP (e.g., with RADIUS authentication server) (&quot;WPA-Enterprise&quot;) Following authentication methods are supported with an integrate IEEE 802.1X Supplicant:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>EAP-TLS</dl>
</dl>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>EAP-PEAP/MSCHAPv2 (both PEAPv0 and PEAPv1)</p>
<dt>&bull;</p>
<dd>EAP-PEAP/TLS (both PEAPv0 and PEAPv1)</p>
<dt>&bull;</p>
<dd>EAP-PEAP/GTC (both PEAPv0 and PEAPv1)</p>
<dt>&bull;</p>
<dd>EAP-PEAP/OTP (both PEAPv0 and PEAPv1)</p>
<dt>&bull;</p>
<dd>EAP-PEAP/MD5-Challenge (both PEAPv0 and PEAPv1)</p>
<dt>&bull;</p>
<dd>EAP-TTLS/EAP-MD5-Challenge</p>
<dt>&bull;</p>
<dd>EAP-TTLS/EAP-GTC</p>
<dt>&bull;</p>
<dd>EAP-TTLS/EAP-OTP</p>
<dt>&bull;</p>
<dd>EAP-TTLS/EAP-MSCHAPv2</p>
<dt>&bull;</p>
<dd>EAP-TTLS/EAP-TLS</p>
<dt>&bull;</p>
<dd>EAP-TTLS/MSCHAPv2</p>
<dt>&bull;</p>
<dd>EAP-TTLS/MSCHAP</p>
<dt>&bull;</p>
<dd>EAP-TTLS/PAP</p>
<dt>&bull;</p>
<dd>EAP-TTLS/CHAP</p>
<dt>&bull;</p>
<dd>EAP-SIM</p>
<dt>&bull;</p>
<dd>EAP-AKA</p>
<dt>&bull;</p>
<dd>EAP-PSK</p>
<dt>&bull;</p>
<dd>EAP-PAX</p>
<dt>&bull;</p>
<dd>LEAP (note: requires special support from the driver for IEEE 802.11 authentication)</p>
<dt>&bull;</p>
<dd>(following methods are supported, but since they do not generate keying material, they cannot be used with WPA or IEEE 802.1X WEP keying)</p>
<dt>&bull;</p>
<dd>EAP-MD5-Challenge</p>
<dt>&bull;</p>
<dd>EAP-MSCHAPv2</p>
<dt>&bull;</p>
<dd>EAP-GTC</p>
<dt>&bull;</p>
<dd>EAP-OTP</dl>
</dl>
<dt>&bull;</p>
<dd>key management for CCMP, TKIP, WEP104, WEP40</p>
<dt>&bull;</p>
<dd>RSN/WPA2 (IEEE 802.11i)</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>pre-authentication</p>
<dt>&bull;</p>
<dd>PMKSA caching</dl>
</dl>
</dl>
<h2>Available Drivers</h2>
<p>A summary of available driver backends is below. Support for each of the driver backends is chosen at wpa_supplicant compile time. For a list of supported driver backends that may be used with the -D option on your system, refer to the help output of wpa_supplicant (<code>wpa_supplicant -h</code>).</p>
<dl>
<dt><code>nl80211</code></p>
<dd>Uses the modern Linux nl80211/cfg80211 netlink-based interface (most new drivers).</p>
<dt><code>wext</code></p>
<dd>Uses the legacy Linux wireless extensions ioctl-based interface (older hardware/drivers).</p>
<dt><code>wired</code></p>
<dd>wpa_supplicant wired Ethernet driver</p>
<dt><code>roboswitch</code></p>
<dd>wpa_supplicant Broadcom switch driver</p>
<dt><code>bsd</code></p>
<dd>BSD 802.11 support (Atheros, etc.).</p>
<dt><code>ndis</code></p>
<dd>Windows NDIS driver.</dl>
<h2>Command Line Options</h2>
<p>Most command line options have global scope. Some are given per interface, and are only valid if at least one <code>-i</code> option is specified, otherwise they&#8217;re ignored. Option groups for different interfaces must be separated by <code>-N</code> option.</p>
<dl>
<dt><code>-b br_ifname</code></p>
<dd>Optional bridge interface name. (Per interface)</p>
<dt><code>-B</code></p>
<dd>Run daemon in the background.</p>
<dt><code>-c filename</code></p>
<dd>Path to configuration file. (Per interface)</p>
<dt><code>-C ctrl_interface</code></p>
<dd>Path to ctrl_interface socket (Per interface. Only used if <code>-c</code> is not).</p>
<dt><code>-i ifname</code></p>
<dd>Interface to listen on. Multiple instances of this option can be present, one per interface, separated by <code>-N</code> option (see below).</p>
<dt><code>-d</code></p>
<dd>Increase debugging verbosity (<code>-dd</code> even more).</p>
<dt><code>-D driver</code></p>
<dd>Driver to use (can be multiple drivers: nl80211,wext). (Per interface, see the available options below.)</p>
<dt><code>-e entropy file</code></p>
<dd>File for <code>wpa_supplicant</code> to use to maintain its internal entropy store in over restarts.</p>
<dt><code>-f output file</code></p>
<dd>Log output to specified file instead of stdout. (This is only available if <code>wpa_supplicant</code> was built with the CONFIG_DEBUG_FILE option.)</p>
<dt><code>-g global ctrl_interface</code></p>
<dd>Path to global ctrl_interface socket. If specified, interface definitions may be omitted.</p>
<dt><code>-K</code></p>
<dd>Include keys (passwords, etc.) in debug output.</p>
<dt><code>-h</code></p>
<dd>Help. Show a usage message.</p>
<dt><code>-L</code></p>
<dd>Show license (BSD).</p>
<dt><code>-o override driver</code></p>
<dd>Override the driver parameter for new interfaces.</p>
<dt><code>-O override ctrl_interface</code></p>
<dd>Override the ctrl_interface parameter for new interfaces.</p>
<dt><code>-p</code></p>
<dd>Driver parameters. (Per interface)</p>
<dt><code>-P PID_file</code></p>
<dd>Path to PID file.</p>
<dt><code>-q</code></p>
<dd>Decrease debugging verbosity (<code>-qq</code> even less).</p>
<dt><code>-s</code></p>
<dd>Log output to syslog instead of stdout. (This is only available if <code>wpa_supplicant</code> was built with the CONFIG_DEBUG_SYSLOG option.)</p>
<dt><code>-T</code></p>
<dd>Log output to Linux tracing in addition to any other destinations. (This is only available if <code>wpa_supplicant</code> was built with the CONFIG_DEBUG_LINUX_TRACING option.)</p>
<dt><code>-t</code></p>
<dd>Include timestamp in debug messages.</p>
<dt><code>-u</code></p>
<dd>Enable DBus control interface. If enabled, interface definitions may be omitted. (This is only available if <code>wpa_supplicant</code> was built with the CONFIG_CTRL_IFACE_DBUS_NEW option.)</p>
<dt><code>-v</code></p>
<dd>Show version.</p>
<dt><code>-W</code></p>
<dd>Wait for a control interface monitor before starting.</p>
<dt><code>-N</code></p>
<dd>Start describing new interface.</dl>
<h2>Examples</h2>
<p>In most common cases, <code>wpa_supplicant</code> is started with:  </p>
<pre>wpa_supplicant -B -c/etc/wpa_supplicant.conf -iwlan0</pre>
</dl>
<p> This makes the process fork into background. The easiest way to debug problems, and to get debug log for bug reports, is to start <code>wpa_supplicant</code> on foreground with debugging enabled:  </p>
<pre>wpa_supplicant -c/etc/wpa_supplicant.conf -iwlan0 -d</pre>
</dl>
<p> If the specific driver wrapper is not known beforehand, it is possible to specify multiple comma separated driver wrappers on the command line. <code>wpa_supplicant</code> will use the first driver wrapper that is able to initialize the interface.  </p>
<pre>wpa_supplicant -Dnl80211,wext -c/etc/wpa_supplicant.conf -iwlan0</pre>
</dl>
<p> <code>wpa_supplicant</code> can control multiple interfaces (radios) either by running one process for each interface separately or by running just one process and list of options at command line. Each interface is separated with -N argument. As an example, following command would start wpa_supplicant for two interfaces:  </p>
<pre>wpa_supplicant \
 -c wpa1.conf -i wlan0 -D nl80211 -N \
 -c wpa2.conf -i ath0 -D wext</pre>
</dl>
<h2>Os Requirements</h2>
<p>Current hardware/software requirements:</p>
<dl>
<dt>&bull;</p>
<dd>Linux kernel 2.6.30 or higher with nl80211/cfg80211 support</p>
<dt>&bull;</p>
<dd>Linux kernel 2.4.x or higher with Linux Wireless Extensions v15 or newer</p>
<dt>&bull;</p>
<dd>FreeBSD 6-CURRENT</p>
<dt>&bull;</p>
<dd>Microsoft Windows with WinPcap (at least WinXP, may work with other versions)</dl>
<h2>Supported Drivers</h2>
<dl>
<dt><code>Linux nl80211/cfg80211</code></p>
<dd>This is the preferred driver for Linux.</p>
<dt><code>Linux wireless extensions</code></p>
<dd>In theory, any driver that supports Linux wireless extensions can be used with IEEE 802.1X (i.e., not WPA) when using ap_scan=0 option in configuration file.</p>
<dt><code>Wired Ethernet drivers</code></p>
<dd>Use ap_scan=0.</p>
<dt><code>BSD net80211 layer (e.g., Atheros driver)</code></p>
<dd>At the moment, this is for FreeBSD 6-CURRENT branch.</p>
<dt><code>Windows NDIS</code></p>
<dd>The current Windows port requires WinPcap (<a rel="nofollow" href="http://winpcap.polito.it/">http://winpcap.polito.it/</a>). See README-Windows.txt for more information.</dl>
<p> wpa_supplicant was designed to be portable for different drivers and operating systems. Hopefully, support for more wlan cards and OSes will be added in the future. See developer.txt for more information about the design of wpa_supplicant and porting to other drivers. One main goal is to add full WPA/WPA2 support to Linux wireless extensions to allow new drivers to be supported without having to implement new driver-specific interface code in wpa_supplicant.</p>
<h2>Architecture</h2>
<p>The <code>wpa_supplicant</code> system consists of the following components:</p>
<dl>
<dt><i>wpa_supplicant.conf</i></p>
<dd>the configuration file describing all networks that the user wants the computer to connect to.</p>
<dt><code>wpa_supplicant</code></p>
<dd>the program that directly interacts with the network interface.</p>
<dt><code>wpa_cli</code></p>
<dd>the client program that provides a high-level interface to the functionality of the daemon.</p>
<dt><code>wpa_passphrase</code></p>
<dd>a utility needed to construct <i>wpa_supplicant.conf</i> files that include encrypted passwords.</dl>
<h2>Quick Start</h2>
<p>First, make a configuration file, e.g. <i>/etc/wpa_supplicant.conf</i>, that describes the networks you are interested in. See <code><a href="/docs/linux/man/5-wpa_supplicant-conf/">wpa_supplicant.conf</a></code>(5) for details. </p>
<p> Once the configuration is ready, you can test whether the configuration works by running <code>wpa_supplicant</code> with following command to start it on foreground with debugging enabled: </p>
<dl>
<dd>
<pre>wpa_supplicant -iwlan0 -c/etc/wpa_supplicant.conf -d</pre>
</dl>
<p> Assuming everything goes fine, you can start using following command to start <code>wpa_supplicant</code> on background without debugging: </p>
<dl>
<dd>
<pre>wpa_supplicant -iwlan0 -c/etc/wpa_supplicant.conf -B</pre>
</dl>
<p> Please note that if you included more than one driver interface in the build time configuration (.config), you may need to specify which interface to use by including -D&lt;driver name&gt; option on the command line.</p>
<h2>Interface To Pcmcia-Cs/Cardmrg</h2>
<p>For example, following small changes to pcmcia-cs scripts can be used to enable WPA support: </p>
<p> Add MODE=&quot;Managed&quot; and WPA=&quot;y&quot; to the network scheme in <i>/etc/pcmcia/wireless.opts</i>. </p>
<p> Add the following block to the end of <code>start</code> action handler in <i>/etc/pcmcia/wireless</i>: </p>
<dl>
<dd>
<pre>if [ &quot;$WPA&quot; = &quot;y&quot; -a -x /usr/local/bin/wpa_supplicant ]; then
 /usr/local/bin/wpa_supplicant -B -c/etc/wpa_supplicant.conf -i$DEVICE
fi</pre>
</dl>
<p> Add the following block to the end of <code>stop</code> action handler (may need to be separated from other actions) in <i>/etc/pcmcia/wireless</i>: </p>
<dl>
<dd>
<pre>if [ &quot;$WPA&quot; = &quot;y&quot; -a -x /usr/local/bin/wpa_supplicant ]; then
 killall wpa_supplicant
fi</pre>
</dl>
<p> This will make <code>cardmgr</code> start <code>wpa_supplicant</code> when the card is plugged in.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wpa_background/">wpa_background</a></code>(8) <code><a href="/docs/linux/man/5-wpa_supplicant-conf/">wpa_supplicant.conf</a></code>(5) <code><a href="/docs/linux/man/8-wpa_cli/">wpa_cli</a></code>(8) <code><a href="/docs/linux/man/8-wpa_passphrase/">wpa_passphrase</a></code>(8)</p>
<h2>Legal</h2>
<p>wpa_supplicant is copyright (c) 2003-2022, Jouni Malinen &lt;j@w1.fi&gt; and contributors. All Rights Reserved. </p>
<p> This program is licensed under the BSD license (the one with advertisement clause removed).</p>
