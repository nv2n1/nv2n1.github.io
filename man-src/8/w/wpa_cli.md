---
title: "wpa_cli(8)"
name: "wpa_cli"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wpa_cli/"
description: "wpa_cli – WPA command line client"
---

<p>wpa_cli &#8211; WPA command line client</p>
<h2>Synopsis</h2>
<p><code>wpa_cli</code> [ <code>-p </code><i>path to ctrl sockets</i> ] [ <code>-g </code><i>path to global ctrl_interface socket</i> ] [ <code>-i </code><i>ifname</i> ] [ <code>-hvB</code> ] [ <code>-a </code><i>action file</i> ] [ <code>-P </code><i>pid file</i> ] [ <code>-G </code><i>ping interval</i> ] [ <i>command &#8230;</i> ] </p>
<h2>Overview</h2>
<p>wpa_cli is a text-based frontend program for interacting with wpa_supplicant. It is used to query current status, change configuration, trigger events, and request interactive user input. </p>
<p> wpa_cli can show the current authentication status, selected security mode, dot11 and dot1x MIBs, etc. In addition, it can configure some variables like EAPOL state machine parameters and trigger events like reassociation and IEEE 802.1X logoff/logon. wpa_cli provides a user interface to request authentication information, like username and password, if these are not included in the configuration. This can be used to implement, e.g., one-time-passwords or generic token card authentication where the authentication is based on a challenge-response that uses an external device for generating the response. </p>
<p> The control interface of wpa_supplicant can be configured to allow non-root user access (ctrl_interface GROUP= parameter in the configuration file). This makes it possible to run wpa_cli with a normal user account. </p>
<p> wpa_cli supports two modes: interactive and command line. Both modes share the same command set and the main difference is in interactive mode providing access to unsolicited messages (event messages, username/password requests). </p>
<p> Interactive mode is started when wpa_cli is executed without including the command as a command line parameter. Commands are then entered on the wpa_cli prompt. In command line mode, the same commands are entered as command line arguments for wpa_cli.</p>
<h2>Interactive Authentication Parameters Request</h2>
<p>When wpa_supplicant need authentication parameters, like username and password, which are not present in the configuration file, it sends a request message to all attached frontend programs, e.g., wpa_cli in interactive mode. wpa_cli shows these requests with &quot;CTRL-REQ-&lt;type&gt;-&lt;id&gt;:&lt;text&gt;&quot; prefix. &lt;type&gt; is IDENTITY, PASSWORD, or OTP (one-time-password). &lt;id&gt; is a unique identifier for the current network. &lt;text&gt; is description of the request. In case of OTP request, it includes the challenge from the authentication server. </p>
<p> The reply to these requests can be given with <code>identity</code>, <code>password</code>, and <code>otp</code> commands. &lt;id&gt; needs to be copied from the matching request. <code>password</code> and <code>otp</code> commands can be used regardless of whether the request was for PASSWORD or OTP. The main difference between these two commands is that values given with <code>password</code> are remembered as long as wpa_supplicant is running whereas values given with <code>otp</code> are used only once and then forgotten, i.e., wpa_supplicant will ask frontend for a new value for every use. This can be used to implement one-time-password lists and generic token card -based authentication. </p>
<p> Example request for password and a matching reply: </p>
<dl>
<dd>
<pre>CTRL-REQ-PASSWORD-1:Password needed for SSID foobar
&gt; password 1 mysecretpassword</pre>
</dd></dl>
<p> Example request for generic token card challenge-response: </p>
<dl>
<dd>
<pre>CTRL-REQ-OTP-2:Challenge 1235663 needed for SSID foobar
&gt; otp 2 9876</pre>
</dd></dl>
<h2>Command Arguments</h2>
<dl>
<dt><code>-p path</code></dt>
<dd>Change the path where control sockets should be found.</dd>
<dt><code>-g control socket path</code></dt>
<dd>Connect to the global control socket at the indicated path rather than an interface-specific control socket.</dd>
<dt><code>-i ifname</code></dt>
<dd>Specify the interface that is being configured. By default, choose the first interface found with a control socket in the socket path.</dd>
<dt><code>-h</code></dt>
<dd>Help. Show a usage message.</dd>
<dt><code>-v</code></dt>
<dd>Show version information.</dd>
<dt><code>-B</code></dt>
<dd>Run as a daemon in the background.</dd>
<dt><code>-a file</code></dt>
<dd>Run in daemon mode executing the action file based on events from wpa_supplicant. The specified file will be executed with the first argument set to interface name and second to &quot;CONNECTED&quot; or &quot;DISCONNECTED&quot; depending on the event. This can be used to execute networking tools required to configure the interface. </dd>
<p> Additionally, three environmental variables are available to the file: WPA_CTRL_DIR, WPA_ID, and WPA_ID_STR. WPA_CTRL_DIR contains the absolute path to the ctrl_interface socket. WPA_ID contains the unique network_id identifier assigned to the active network, and WPA_ID_STR contains the content of the id_str option.</p>
<dt><code>-P file</code></dt>
<dd>Set the location of the PID file.</dd>
<dt><code>-G ping interval</code></dt>
<dd>Set the interval (in seconds) at which wpa_cli pings the supplicant.</dd>
<dt><code>command</code></dt>
<dd>Run a command. The available commands are listed in the next section.</dd></dl>
<h2>Commands</h2>
<p>The following commands are available:</p>
<dl>
<dt><code>status</code></dt>
<dd>get current WPA/EAPOL/EAP status</dd>
<dt><code>mib</code></dt>
<dd>get MIB variables (dot1x, dot11)</dd>
<dt><code>help</code></dt>
<dd>show this usage help</dd>
<dt><code>interface [ifname]</code></dt>
<dd>show interfaces/select interface</dd>
<dt><code>level &lt;debug level&gt;</code></dt>
<dd>change debug level</dd>
<dt><code>license</code></dt>
<dd>show full wpa_cli license</dd>
<dt><code>logoff</code></dt>
<dd>IEEE 802.1X EAPOL state machine logoff</dd>
<dt><code>logon</code></dt>
<dd>IEEE 802.1X EAPOL state machine logon</dd>
<dt><code>set</code></dt>
<dd>set variables (shows list of variables when run without arguments)</dd>
<dt><code>pmksa</code></dt>
<dd>show PMKSA cache</dd>
<dt><code>reassociate</code></dt>
<dd>force reassociation</dd>
<dt><code>reconfigure</code></dt>
<dd>force wpa_supplicant to re-read its configuration file</dd>
<dt><code>preauthenticate &lt;BSSID&gt;</code></dt>
<dd>force preauthentication</dd>
<dt><code>identity &lt;network id&gt; &lt;identity&gt;</code></dt>
<dd>configure identity for an SSID</dd>
<dt><code>password &lt;network id&gt; &lt;password&gt;</code></dt>
<dd>configure password for an SSID</dd>
<dt><code>pin &lt;network id&gt; &lt;pin&gt;</code></dt>
<dd>configure pin for an SSID</dd>
<dt><code>otp &lt;network id&gt; &lt;password&gt;</code></dt>
<dd>configure one-time-password for an SSID</dd>
<dt><code>bssid &lt;network id&gt; &lt;BSSID&gt;</code></dt>
<dd>set preferred BSSID for an SSID</dd>
<dt><code>list_networks</code></dt>
<dd>list configured networks</dd>
<dt><code>terminate</code></dt>
<dd>terminate <code>wpa_supplicant</code></dd>
<dt><code>quit</code></dt>
<dd>exit wpa_cli</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8)</p>
<h2>Legal</h2>
<p>wpa_supplicant is copyright (c) 2003-2022, Jouni Malinen &lt;j@w1.fi&gt; and contributors. All Rights Reserved. </p>
<p> This program is licensed under the BSD license (the one with advertisement clause removed).</p>
