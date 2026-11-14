---
title: "wicd(8)"
name: "wicd"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wicd/"
description: "Wicd – Wired and Wireless Network Connection Manager"
---

<p><code>Wicd</code> &#8211; Wired and Wireless Network Connection Manager</p>
<h2>Theory Of Operation</h2>
<p>Wicd is designed to give the user as much control over behavior of network connections as possible. Every network, both wired and wireless, has its own profile with its own configuration options and connection behavior. Wicd will try to automatically connect only to networks the user specifies it should try, with a preference first to a wired network, then to wireless. </p>
<p> For wired connections, users have many options for determining what network settings to use. Wicd allows creation of an unlimited number of wired profiles, each of which has its own unique settings. The user can choose to automatically connect to a selected default profile, choose a profile from a pop-up window every time wicd connects, or have wicd automatically choose the last profile used to manually connect. </p>
<p> For wireless connections, users can select any number of wireless networks to automatically connect; wicd will choose the one with the highest signal strength to try to connect. </p>
<p> If the user chooses, wicd will try to automatically reconnect when it detects that a connection is lost. If the last known connection state is wired, wicd will first try to reconnect to the wired network, and if it is not available, wicd will try any available wireless networks which have automatic connection enabled. If the last known connection state is wireless, wicd will first try to reconnect to the previously connected network (even if that network does not have automatic connection enabled), and should that fail, it will try both a wired connection and any available wireless networks which have automatic connection enabled. </p>
<p> Wicd uses built-in linux wireless-tools, such as ifconfig and iwconfig, to get and configure network info. There is some flexibility in its use of DHCP, providing support for dhclient, dhcpcd, and pump. Wicd uses wpa_supplicant to handle all wireless encryption settings, and uses a template-based system to create the configuration files used by wpa_supplicant. These templates can be edited, and new templates can be created by the user and imported into wicd, allowing connection to networks with uncommon encryption settings.</p>
<h2>Structure</h2>
<p>Wicd has two major parts: the daemon, which runs with root privileges; and the user interface, which runs with normal user privileges. The two parts run as separate processes and make use of D-Bus to communicate. </p>
<p> The daemon is responsible for making and configuring connections, reading and writing configuration files and logs, and monitoring the connection status. The daemon&#8217;s job is split between two processes: wicd-daemon.py and monitor.py. All the connection status monitoring, as well as the auto-reconnection logic, takes place in monitor.py. Everything else is done by wicd-daemon.py. </p>
<p> The user interface (stored in wicd-gtk), which is made up of a tray icon, a main GUI window, and its child dialogs, gets configuration and network info from the daemon either by querying it using the methods in the daemon&#8217;s dbus interface or by receiving signals emitted from the daemon over D-Bus. Any configuration changes made in the user interface are passed back to the daemon, which actually applies the changes and writes them to configuration files. </p>
<p> Since the user interface just queries for connection and configuration info from the daemon, it is possible to run wicd without the GUI at all. Also, the daemon is started by wicd&#8217;s init script during system startup (before any user logs in), making it possible to use wicd with &quot;headless&quot; machines.</p>
<h2>Usage Hints</h2>
<p><code>Choosing Alternate Tools</code><br />
 Wicd supports several alternatives regarding the networking tools on linux. In the &quot;External Programs&quot; tab of the Preferences menu, you can choose your preferred DHCP client, link detection tool, and routing tool if the defaults aren&#8217;t suitable for your particular distribution or system. </p>
<p> <code>Custom Scripts</code><br />
 If you need to run any custom commands before or after connecting to or disconnecting from a network, Wicd supports this; however, you will need to have a graphical sudo helper installed (currently supported are kdesu, gksu, and ktsuss). Also see /etc/wicd/scripts/ in FILES.<br />
 If you do not have a graphical sudo helper installed, you still have the ability to use custom scripts, but you will have to set them up manually. See <a href="/docs/linux/man/5-wicd-wired-settings-conf/">wicd-wired-settings.conf</a>(5) and/or <a href="/docs/linux/man/5-wicd-wireless-settings-conf/">wicd-wireless-settings.conf</a>(5) for more information on how to do so. </p>
<p> <code>Automatically Connecting to Networks</code><br />
 Wicd uses the BSSID to recognize a particular network (and thus to decide whether it should automatically connect to it). If you are on a network that has many different access points which all have the same ESSID (many universities have such networks), there is an option in the &quot;Advanced Settings&quot; to &quot;Use these settings for all networks sharing this essid.&quot; With this option enabled, Wicd will autoconnect to that network, regardless of which node it sees.</p>
<h2>Files</h2>
<p><code>/etc/wicd/manager-settings.conf</code><br />
 This file contains global settings for Wicd.<br />
 See this file&#8217;s own man page for more information about it. </p>
<p> <code>/etc/wicd/wired-settings.conf</code><br />
 This file contains settings related to the wired interface.<br />
 See this file&#8217;s own man page for more information about it. </p>
<p> <code>/etc/wicd/wireless-settings.conf</code><br />
 This file contains settings related to the wireless interface.<br />
 See this file&#8217;s own man page for more information about it. </p>
<p> <code>/etc/wicd/dhclient.conf.template</code><br />
 This is used to generate /var/lib/wicd/dhclient.conf during Wicd activity, if you&#8217;re using <a href="/docs/linux/man/1-dhclient/">dhclient</a>(1) as DHCP client. See <a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5) for more information. </p>
<p> <code>/etc/wicd/encryption/templates/</code><br />
 This directory contains various templates for encrypted (WEP, WPA, etcetera) connections. If none of them fit your needs, you may create your own and add it to this directory. If you do this, please contact the authors (see below) of Wicd. </p>
<p> <code>/etc/wicd/scripts/</code><br />
 Dropping a script in the relevant directory will cause it to be executed when the specified event is preformed upon connection or disconnect from or to any network. Please note that pre/post disconnect scripts may be executed multiple times on already-disconnected interfaces.<br />
 The scripts will be passed different parameters, depending if Wicd is acting on a wired or a wireless network. In the former case, &quot;wired wired wired&quot; will be passed (three times, just for compatibility with the wireless case). If Wicd is acting on a wireless network, it will pass &quot;wireless ESSID BSSID&quot; to the script.<br />
 Available directories are:<br />
 /etc/wicd/scripts/predisconnect<br />
 /etc/wicd/scripts/postdisconnect<br />
 /etc/wicd/scripts/preconnect<br />
 /etc/wicd/scripts/postconnect </p>
<p> <code>/var/lib/wicd/configurations/</code><br />
 This directory contains individual configuration files for each encrypted network you set up in Wicd. </p>
<p> <code>/var/log/wicd/</code><br />
 This directory contains logfiles of Wicd&#8217;s activity. Please refer to the log if you are having connection or other problems.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-wicd-manager-settings-conf/">wicd-manager-settings.conf</a></code>(5), <code><a href="/docs/linux/man/5-wicd-wired-settings-conf/">wicd-wired-settings.conf</a></code>(5), <code><a href="/docs/linux/man/5-wicd-wireless-settings-conf/">wicd-wireless-settings.conf</a></code>(5), <code><a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a></code>(5), <code><a href="/docs/linux/man/8-wicd-curses/">wicd-curses</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8), <code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8), <code><a href="/docs/linux/man/8-route/">route</a></code>(8), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-mii-tool/">mii-tool</a></code>(8), <code><a href="/docs/linux/man/8-ethtool/">ethtool</a></code>(8), <code><a href="/docs/linux/man/8-dhclient/">dhclient</a></code>(8), <code><a href="/docs/linux/man/8-dhcpcd/">dhcpcd</a></code>(8), <code><a href="/docs/linux/man/8-pump/">pump</a></code>(8). </p>
<h2>Wicd Authors</h2>
<p>Adam Blackburn &lt;compwiz18 [at] gmail.com&gt;<br />
 Dan O&#8217;Reilly &lt;oreilldf [at] gmail.com&gt;<br />
 Andrew Psaltis &lt;ampsaltis [at] gmail.com&gt; (curses client)<br />
 David Paleino &lt;d.paleino [at] gmail.com&gt;</p>
<h2>Manpage Author</h2>
<p>Robby Workman &lt;rworkman [at] slackware.com&gt;</p>
