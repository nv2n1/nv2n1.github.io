---
title: "corosync-qnetd(8)"
name: "corosync-qnetd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-qnetd/"
description: "corosync-qnetd – QNet daemon"
---

<p>corosync-qnetd &#8211; QNet daemon</p>
<h2>Synopsis</h2>
<p><code>corosync-qnetd [-46dfhv] [-l listen_addr] [-p listen_port] [-s tls]</code> <code>[-c client_cert_required] [-m max_clients] [-S option=value[,option2=value2,&#8230;]]</code> </p>
<h2>Description</h2>
<p><code>corosync-qnetd</code> is a daemon running outside of the cluster with the purpose of providing a vote to the <code>corosync-qdevice</code> model net. It&#8217;s designed to support multiple clusters and be almost configuration and state free. New clusters are handled dynamically and no configuration file exists. It&#8217;s also able to run as non-root user &#8211; which is recommended. Connection between the <code>corosync-qdevice</code> model net client can be optionally configured with TLS client certificate checking. The communication protocol between server and client is designed to be very simple and allow backwards compatibility.</p>
<h2>Options</h2>
<dl>
<dt><code>-4</code></p>
<dd>and its counterpart <code>-6</code> are used to force IPv4 or IPv6 communication. The default is to listen on both address families.</p>
<dt><code>-d</code></p>
<dd>Turn on debug logging. By default the messages sent to syslog are purely operational, this option sends additional debug messages. For even more detail use the <code>-d</code> parameter twice.</p>
<dt><code>-f</code></p>
<dd>Do not daemonize, run in the foreground.</p>
<dt><code>-h</code></p>
<dd>Show short help text</p>
<dt><code>-v</code></p>
<dd>Show version and supported communication protocol messages/options.</p>
<dt><code>-l</code></p>
<dd>IP address to listen on. By default the daemon listens on all addresses (wildcard).</p>
<dt><code>-p</code></p>
<dd>TCP port to listen on. Default port is 5403.</p>
<dt><code>-s</code></p>
<dd>Determines if TLS should be used and can be one of <i>on/off/required</i> (the default is <i>on</i> ). <i>on</i> means TLS is enabled but the client is not required to start TLS, <i>off</i> means TLS is completely disabled, and <i>required</i> means TLS is required. <i>on</i> and <i>required</i> require the NSS database to be properly initialized by running the <code>corosync-qnetd-certutil</code> command.</p>
<dt><code>-c</code></p>
<dd>can be set to <i>on/off.</i> This option only makes sense if TLS is enabled. When <code>-c</code> is <i>on</i> a client is required to send its client certificate (default).</p>
<dt><code>-m</code></p>
<dd>Maximum simultaneous clients. The default is 0 which means no limit.</p>
<dt><code>-S</code></p>
<dd>Set advanced settings described in its own section below. This option shouldn&#8217;t be generally used because most of the options are not safe to change.</dl>
<h2>Unprivileged User Configuration</h2>
<p>It&#8217;s generally recommended to run <code>corosync-qnetd</code> as a non root user. If you get a package from a distribution its highly possible that the packager has done all the hard work for you. If the installation is performed from source code, a few steps have to be taken. </p>
<p> First it&#8217;s necessary to create an unprivileged user/group. The following commands can be used (executed as root): </p>
<pre># groupadd -r coroqnetd
# useradd -r -g coroqnetd -d / -s /sbin/nologin -c &quot;User for corosync-qnetd&quot; coroqnetd</pre>
<p>The next step is to set the correct owner and group on /etc/corosync/qnetd and /var/run/corosync-qnetd directories. </p>
<pre># chown -R coroqnetd:coroqnetd /etc/corosync/qnetd /var/run/corosync-qnetd</pre>
<p>Some systems have the /var/run directory on a tmpfs file system which gets discarded after a reboot. The solution is to use an initscript which takes care of the /var/run/corosync-qnetd creation and sets the correct owner and permissions. For systems with systemd it&#8217;s possible to use a tmpfile.d configuration file (installed by default if systemd is enabled during corosync compilation). </p>
<p> The last step is to make sure <code>corosync-qnetd</code> is really executed as an unprivileged user. For initscript systems it&#8217;s enough to set the line COROSYNC_QNETD_RUNAS in /etc/(sysconfig|default)/corosync-qnetd file. If the file is not already installed then use the one provided in the corosync source code (init/corosync-qnetd.sysconfig.example). For systemd, overwrite/copy the corosync-qnetd.service unit file and uncomment/change the &quot;User=&quot; directive.</p>
<h2>Tls Configuration</h2>
<p>For TLS to work its necessary to create the NSS database. If pcs is used then the following steps are not needed because pcs does them automatically. </p>
<p> <code>corosync-qnetd-certutil</code> is the tool to perform required actions. Just run: </p>
<pre># corosync-qnetd-certutil -i</pre>
<p>If TLS is not required then simply edit /etc/(sysconfig|default)/corosync-qnetd or systemd unit file and add the parameter <code>-s</code> <i>off</i> in the proper place.</p>
<h2>Advanced Settings</h2>
<p>Set by the <code>-S</code> option. The default value is shown in parantheses.</p>
<dl>
<dt><code>listen_backlog</code></p>
<dd>Parameter passed to the listen syscall on the network socket. (10)</p>
<dt><code>max_client_send_buffers</code></p>
<dd>Maximum number of send buffers for one client. (32)</p>
<dt><code>max_client_send_size</code></p>
<dd>Maximum size of one send buffer (message) to be sent to a client. (32768)</p>
<dt><code>max_client_receive_size</code></p>
<dd>Maximum size of the receive buffer for a client message (maximum allowed message size received by client). (32768)</p>
<dt><code>nss_db_dir</code></p>
<dd>NSS database directory. (/etc/corosync/qnetd/nssdb)</p>
<dt><code>cert_nickname</code></p>
<dd>NSS nickname of qnetd server certificate. (QNetd Cert)</p>
<dt><code>heartbeat_interval_min</code></p>
<dd>Minimum heartbeat timeout accepted by server in ms. (1000)</p>
<dt><code>heartbeat_interval_max</code></p>
<dd>Maximum heartbeat timeout accepted by server in ms. (120000)</p>
<dt><code>dpd_enabled</code></p>
<dd>Dead peer detection enabled. (on)</p>
<dt><code>dpd_interval</code></p>
<dd>How often the DPD algorithm detects dead peers in ms. (10000)</p>
<dt><code>lock_file</code></p>
<dd>Lock file location. (/var/run/corosync-qnetd/corosync-qnetd.pid)</p>
<dt><code>local_socket_file</code></p>
<dd>Internal IPC socket file location. (/var/run/corosync-qnetd/corosync-qnetd.sock)</p>
<dt><code>local_socket_backlog</code></p>
<dd>Parameter passed to listen syscall on the local socket. (10)</p>
<dt><code>ipc_max_clients</code></p>
<dd>Maximum allowed simultaneous IPC clients. (10)</p>
<dt><code>ipc_max_receive_size</code></p>
<dd>Maximum size of a message received by IPC client. (4096)</p>
<dt><code>ipc_max_send_size</code></p>
<dd>Maximum size of a message sent to an IPC client. (10485760)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync-qnetd-tool/">corosync-qnetd-tool</a></code>(8) <code><a href="/docs/linux/man/8-corosync-qnetd-certutil/">corosync-qnetd-certutil</a></code>(8) <code><a href="/docs/linux/man/8-corosync-qdevice/">corosync-qdevice</a></code>(8)</p>
<h2>Author</h2>
<p>Jan Friesse</p>
