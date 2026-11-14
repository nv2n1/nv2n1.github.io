---
title: "wavemon(1)"
name: "wavemon"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wavemon/"
description: "wavemon – a wireless network monitor"
---

<h2>NAME</h2>
<p> wavemon &#8211; a wireless network monitor</p>
<h2>SYNOPSIS</h2>
<p> <code>wavemon [-h] [-i</code> <i>ifname</i> <code>] [-l] [-r] [-v]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>wavemon</i> is a ncurses-based monitoring application for wireless network devices. It plots levels in real-time as well as showing wireless and network related device information. Currently, wavemon is still based on the wireless extensions by Jean Tourrilhes &lt;jt [at] hpl.hp.com&gt;. </p>
<p> The <i>wavemon</i> interface splits into different &quot;screens&quot;. Each screen presents information in a specific manner. For example, the &quot;info&quot; screen shows current levels as bargraphs, whereas the &quot;level&quot; screen represents the same levels as a moving histogram. </p>
<p> On startup, you&#8217;ll see (depending on configuration) one of the different monitor screens. At the bottom, you&#8217;ll find a <i>menu-bar</i> listing the screens and their activating keys. Each screen is activated by either the corresponding function key or the key corresponding to the first character of the screen name. The following screens can be selected:</p>
<dl>
<dt><code>Info (F1 or &#8216;i&#8217;)</code></p>
<dd> This is the most comprehensive screen. It displays a condensed overview of wireless-specific parameters and network statistics, as well as bar graphs. The layout is arranged into several sub-sections. </p>
<p> The <code>Interface</code> section at the top shows information about the monitoring interface, including interface name, type, ESSID, and available encryption formats. </p>
<p> Below, in the <code>Levels</code> section, you can see up to four bargraphs showing (1) relative signal quality and (2) signal level in dBm. If the wireless driver also supports noise level information, additionally (3) noise level in dBm and (4) Signal-Noise-Ratio (SNR) in dB are shown. The colour of the signal level bargraph changes from red to yellow and green at fixed levels. If thresholds have been set, two arrows on the signal level graph will show the positions of the current thresholds. </p>
<p> The <code>Statistics</code> section displays packet and byte counters and a few other packet-related statistics. </p>
<p> The subsequent <code>Info</code> subsection lists the current operational mode and configuration of the wireless interface. What parameters are actually shown depends on the capabilities and selected mode of your network device. </p>
<p> Lastly, the <code>Network</code> section shows network-level parameters. The MAC-address is resolved from <code><a href="/docs/linux/man/5-ethers/">ethers</a></code>(5). The IPv4 address is shown in CIDR notation (RFC 4632 <i>address</i><code>/</code><i>prefix_len</i> format). Since often those two values also determine the broadcast address (last 32 &#8211; <i>prefix_len</i> bits set to 1), that address is shown only if it does not derive from the interface address and prefix length. Likewise, the interface MTU is shown only if it differs from the default Ethernet MTU of 1500 bytes.</p>
<dt><code>Level histogram (F2 or &#8216;l&#8217;)</code></p>
<dd> This is a full-screen histogram plot showing the evolution of levels with time. The screen is partitioned into a grid, with dBm levels shown in green at the right hand side (depending on configuration). At the very minimum, the evolution of the signal-level is shown. If the wireless driver also supports noise-level information, additionally a noise graph and associated SNR graph appear.</p>
<dt><code>Scan window (F3 or &#8216;s&#8217;)</code></p>
<dd> A periodically updated network scan, showing access points and other wireless clients. It is sorted depending on <i>sort_order</i> and <i>sort_ascending</i>, see <code><a href="/docs/linux/man/5-wavemonrc/">wavemonrc</a></code>(5). Each entry starts with the ESSID, followed by the colour-coded MAC address and the signal/channel information. A green/red MAC address indicates an (un-)encrypted access point, the colour changes to yellow for non-access points (in this case the mode is shown at the end of the line). The uncoloured information following the MAC address lists relative and absolute signal strengths, channel, frequency, and the mode if the node is not an access point. A status line at the bottom informs about the current sort order and a few statistics, such as most (least) crowded channels (least crowded channels are listed when sorting by descending channel). </p>
<p> The <i>sort_order</i> can also directly be changed via these keyboard shortcuts: <i>a</i>scending, <i>d</i>escending; by <i>e</i>ssid, <i>s</i>ignal, <i>c</i>hannel (<i>C</i> also with signal), or by <i>o</i>pen access (<i>O</i> also with signal). </p>
<p> Please note that gathering meaningful scan data can take several seconds.</p>
<dt><code>Preferences (F7 or &#8216;p&#8217;)</code></p>
<dd> This screen allows you to change all program options such as interface and level scale parameters, and to save the new settings to the configuration file. Select a parameter with &lt;up&gt; and &lt;down&gt;, then change the value with &lt;left&gt; and &lt;right&gt;. Please refer to <code><a href="/docs/linux/man/5-wavemonrc/">wavemonrc</a></code>(5) for an in-depth description of applicable settings.</p>
<dt><code>Help (F8 or &#8216;h&#8217;)</code></p>
<dd> This page might show an online-help.</p>
<dt><code>About (F9 or &#8216;a&#8217;)</code></p>
<dd> Release information and contact URLs.</p>
<dt><code>Quit (F10 or &#8216;q&#8217;)</p>
<dd> Exit </code><i>wavemon</i>.</dl>
<p> <code>Note:</code> some operations, such as displaying encryption information or performing scans, require <code>CAP_NET_ADMIN</code> privileges (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)). For non-root users, these can be enabled by installing <i>wavemon</i> setuid-root.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i </code><i>interface</i></p>
<dd> override autodetection and use the specified <i>interface</i>.</p>
<dt><code>-d</code></p>
<dd> dump interface parameters to stdout and exit.</p>
<dt><code>-g</code></p>
<dd> check screen <i>geometry</i>: a minimum size is required for proper display; this flag adds a check to ensure it is sufficiently large. Enable this if window does not display properly.</p>
<dt><code>-r</code></p>
<dd> generate random levels (for testing purposes).</p>
<dt><code>-h</code></p>
<dd> print help and exit.</p>
<dt><code>-v</code></p>
<dd> print version information and exit. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>LC_NUMERIC</p>
<dd> Influences the grouping of numbers if set. See also <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1).</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.wavemonrc</p>
<dd> The local per-user configuration file.</dl>
<h2>AUTHOR</h2>
<p> Written by Jan Morgenstern &lt;jan [at] jm-music.de&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Send bug reports and/or suggestions to Gerrit Renker &lt;gerrit [at] erg.abdn.ac.uk&gt;.</p>
<h2>COPYRIGHT</h2>
<p> This is free software with ABSOLUTELY NO WARRANTY. See file COPYING for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-wavemonrc/">wavemonrc</a></code>(5), <code><a href="/docs/linux/man/7-wireless/">wireless</a></code>(7), <code><a href="/docs/linux/man/5-ethers/">ethers</a></code>(5), <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
<h2>Index</h2>
