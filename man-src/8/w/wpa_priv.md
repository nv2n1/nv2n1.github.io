---
title: "wpa_priv(8)"
name: "wpa_priv"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wpa_priv/"
description: "wpa_priv – wpa_supplicant privilege separation helper"
---

<p>wpa_priv &#8211; wpa_supplicant privilege separation helper</p>
<h2>Synopsis</h2>
<p><code>wpa_priv</code> [ <code>-c </code><i>ctrl path</i> ] [ <code>-Bdd</code> ] [ <code>-P </code><i>pid file</i> ] [ <code>driver:ifname </code><i>[driver:ifname &#8230;]</i> ]</p>
<h2>Overview</h2>
<p><code>wpa_priv</code> is a privilege separation helper that minimizes the size of <code>wpa_supplicant</code> code that needs to be run with root privileges. </p>
<p> If enabled, privileged operations are done in the wpa_priv process while leaving rest of the code (e.g., EAP authentication and WPA handshakes) to operate in an unprivileged process (wpa_supplicant) that can be run as non-root user. Privilege separation restricts the effects of potential software errors by containing the majority of the code in an unprivileged process to avoid the possibility of a full system compromise. </p>
<p> <code>wpa_priv</code> needs to be run with network admin privileges (usually, root user). It opens a UNIX domain socket for each interface that is included on the command line; any other interface will be off limits for <code>wpa_supplicant</code> in this kind of configuration. After this, <code>wpa_supplicant</code> can be run as a non-root user (e.g., all standard users on a laptop or as a special non-privileged user account created just for this purpose to limit access to user files even further).</p>
<h2>Example Configuration</h2>
<p>The following steps are an example of how to configure <code>wpa_priv</code> to allow users in the <code>wpapriv</code> group to communicate with <code>wpa_supplicant</code> with privilege separation: </p>
<p> Create user group (e.g., wpapriv) and assign users that should be able to use wpa_supplicant into that group. </p>
<p> Create /var/run/wpa_priv directory for UNIX domain sockets and control user access by setting it accessible only for the wpapriv group: </p>
<dl>
<dd>
<pre>mkdir /var/run/wpa_priv
chown root:wpapriv /var/run/wpa_priv
chmod 0750 /var/run/wpa_priv</pre>
</dl>
<p> Start <code>wpa_priv</code> as root (e.g., from system startup scripts) with the enabled interfaces configured on the command line: </p>
<dl>
<dd>
<pre>wpa_priv -B -c /var/run/wpa_priv -P /var/run/wpa_priv.pid wext:wlan0</pre>
</dl>
<p> Run <code>wpa_supplicant</code> as non-root with a user that is in the wpapriv group: </p>
<dl>
<dd>
<pre>wpa_supplicant -i ath0 -c wpa_supplicant.conf</pre>
</dl>
<h2>Command Arguments</h2>
<dl>
<dt><code>-c ctrl path</code></p>
<dd>Specify the path to wpa_priv control directory (Default: /var/run/wpa_priv/).</p>
<dt><code>-B</code></p>
<dd>Run as a daemon in the background.</p>
<dt><code>-P file</code></p>
<dd>Set the location of the PID file.</p>
<dt><code>driver:ifname [driver:ifname &#8230;]</code></p>
<dd>The &lt;driver&gt; string dictates which of the supported <code>wpa_supplicant</code> driver backends is to be used. To get a list of supported driver types see wpa_supplicant help (e.g, wpa_supplicant -h). The driver backend supported by most good drivers is <code>wext</code>. </p>
<p> The &lt;ifname&gt; string specifies which network interface is to be managed by <code>wpa_supplicant</code> (e.g., wlan0 or ath0). </p>
<p> <code>wpa_priv</code> does not use the network interface before <code>wpa_supplicant</code> is started, so it is fine to include network interfaces that are not available at the time wpa_priv is started. wpa_priv can control multiple interfaces with one process, but it is also possible to run multiple <code>wpa_priv</code> processes at the same time, if desired.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8)</p>
<h2>Legal</h2>
<p>wpa_supplicant is copyright (c) 2003-2016, Jouni Malinen &lt;j@w1.fi&gt; and contributors. All Rights Reserved. </p>
<p> This program is licensed under the BSD license (the one with advertisement clause removed).</p>
