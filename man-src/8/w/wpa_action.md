---
title: "wpa_action(8)"
name: "wpa_action"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wpa_action/"
description: "wpa_action – wpa_cli action script"
---

<p>wpa_action &#8211; wpa_cli action script</p>
<h2>Synopsis</h2>
<p><code>wpa_action</code> <i>IFACE ACTION</i></p>
<h2>Description</h2>
<p><code>wpa_action</code> is a shell script designed to control the <code>ifupdown</code> framework according to <i>ACTION</i> events received from <code>wpa_supplicant</code>. <code>wpa_cli</code> receives <i>CONNECTED</i> and <i>DISCONNECTED</i> events from <code>wpa_supplicant</code> via the crtl_iface socket and gives the <i>ACTION</i> event to the <code>wpa_action</code> script as an argument, along with the <i>IFACE</i> to be acted upon. <code>wpa_action</code> also receives an environment variable from <code>wpa_cli</code>, <i>WPA_ID_STR</i>, containing an alphanumeric identification string for the <i>CURRENT</i> network block. <i>WPA_ID_STR</i> is provided by the &#8216;id_str&#8217; network block option of <code>wpa_supplicant.conf</code>, and provides a means to map the <i>ACTION</i> to a <i>LOGICAL</i> interface configured in the <code>interfaces</code> file. If either the ifupdown <code>interfaces</code> or <i>ifstate</i> file cannot be found, <code>wpa_action</code> will exit silently (status 0). <code>wpa_action</code> will search the following locations for their existence: </p>
<pre> /etc/network/run/ifstate
 /run/network/ifstate
 /etc/network/interfaces</pre>
<h2>Iface</h2>
<p>Network interface to be acted upon, for example &#8216;eth1&#8217; or &#8216;wlan0&#8217;.</p>
<h2>Action</h2>
<p>An <i>ACTION</i> to be performed on the <i>IFACE</i>.</p>
<dl>
<dt><code>CONNECTED</code></p>
<dd><code>wpa_supplicant</code> has completed authentication. <code>ifup</code> <i>IFACE=WPA_ID_STR</i> is invoked and the action is logged to syslog. Network settings for the <i>LOGICAL</i> interface <i>WPA_ID_STR</i> are applied.</p>
<dt><code>DISCONNECTED</code></p>
<dd><code>wpa_supplicant</code> has detected disconnection. <code>ifdown</code> <i>IFACE=WPA_ID_STR</i> is invoked and the action is logged to syslog. Network settings for the <i>LOGICAL</i> interface <i>WPA_ID_STR</i> are undone.</p>
<dt><code>stop</code></p>
<dd>The &#8216;stop&#8217; <i>ACTION</i> is a called manually by the user, to stop the <code>wpa_cli</code> daemon, invoke <code>ifdown</code> <i>IFACE</i> (if the <i>IFACE</i> is present in the <i>ifstate</i> file) and stop the <code>wpa_supplicant</code> daemon.</p>
<dt><code>reload</code></p>
<dd>The &#8216;reload&#8217; <i>ACTION</i> can be used to reload the <code>wpa_supplicant</code> configuration file specified by <i>wpa-roam</i> . &#8216;restart&#8217; is a synonym for &#8216;reload&#8217; and can be used equally. The action is logged to <i>/var/log/wpa_action.log</i>.</dl>
<h2>Environment</h2>
<p>An alphanumeric identification string provided by the &#8216;id_str&#8217; network block option of <code>wpa_supplicant.conf</code> is exported to <code>wpa_action</code> as an environment variable, <i>WPA_ID_STR</i>. When &#8216;id_str&#8217; is not configured for the <i>CURRENT</i> network block, &#8216;default&#8217; is substituted for the absent <i>WPA_ID_STR</i> environment variable. </p>
<p> A unique network identifier, <i>WPA_ID</i>, is exported to <code>wpa_action</code>. It is the number assigned to the <i>CURRENT</i> <code>wpa_supplicant</code> network block (network_id).</p>
<h2>Usage</h2>
<p>The only reasons for <code>wpa_action</code> to be explicitly executed by the user is to stop <code>wpa_cli</code> from controlling <code>ifupdown</code> or reload the <i>wpa_supplicant.conf</i> file after editing. </p>
<dl>
<dd><code>wpa_action</code> <i>eth1 stop</i></dl>
<p> Otherwise, <code>wpa_action</code> is given as an argument to a <code>wpa_cli</code> daemon. </p>
<dl>
<dd><code>wpa_cli</code> <i>-i eth1 -a /sbin/wpa_action -B</i></dl>
<p> This can be done by using the <i>wpa-roam</i> option in the <code>interfaces</code> file. <i>wpa-roam</i> takes one argument, a user provided <code>wpa_supplicant.conf</code> file. </p>
<p> The inet <i>METHOD</i> must be &#8216;manual&#8217; for this interface, as it will be configured according to <code>wpa_cli</code> action events. Also supply a &#8216;default&#8217; <code>interfaces</code> stanza using the dhcp inet <i>METHOD</i> so that networks without an &#8216;id_str&#8217; option can fallback to attempting to receive an ip via dhcp. If one or more networks requires additional network configuration, provide an unique &#8216;id_str&#8217; for each network, and an <code>interfaces</code> stanza using the &#8216;id_str&#8217; value as a <i>LOGICAL</i> interface. The following interfaces file is configured to use dhcp for any network without an &#8216;id_str&#8217;, a static ip for the network with an &#8216;id_str&#8217; of &#8216;home_static&#8217; and dhcp plus an additional post-up command for the network with an &#8216;id_str&#8217; of &#8216;uni&#8217;. </p>
<p> An example wpa_supplicant.conf configured to roam between 3 different networks: </p>
<dl>
<dd>
<pre>network={
 ssid=&quot;foo&quot;
 id_str=&quot;uni&quot;
 key_mgmt=NONE
}
network={
 ssid=&quot;bar&quot;
 id_str=&quot;home_static&quot;
 psk=123456789...
}
network={
 ssid=&quot;&quot;
 key_mgmt=NONE
}</pre>
</dl>
<p> The corresponding <code>interfaces</code> file would contain <i>LOGICAL</i> interfaces, that correlate to each unique &#8216;id_str&#8217; provided by the configuration file: </p>
<dl>
<dd>
<pre>iface eth1 inet manual
 wpa-driver wext
 wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
iface uni inet dhcp
iface home_static inet static
 address 192.168.0.20
 netmask 255.255.255.0
 network 192.168.0.0
 broadcast 192.168.0.255
 gateway 192.168.0.1</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wpa_cli/">wpa_cli</a>(8)</code>, <code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a>(8)</code>, <code><a href="/docs/linux/man/5-wpa_supplicant-conf/">wpa_supplicant.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-ifup/">ifup</a>(8)</code>, <code><a href="/docs/linux/man/5-interfaces/">interfaces</a>(5)</code></p>
<h2>Author</h2>
<p>This manual page was written by Kel Modderman &lt;kel [at] otaku42.de&gt; for the Debian GNU system (but may be used by others).</p>
