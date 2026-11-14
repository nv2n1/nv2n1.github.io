---
title: "networkmanager(8)"
name: "networkmanager"
section: "8"
letter: "n"
url: "/docs/linux/man/8-networkmanager/"
description: "NetworkManager – network management daemon"
---

<p>NetworkManager &#8211; network management daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>NetworkManager </code><code>[OPTIONS&#8230;]</code></dl>
<h2>Description</h2>
<dd>The NetworkManager daemon attempts to make networking configuration and operation as painless and automatic as possible by managing the primary network connection and other network interfaces, like Ethernet, Wi-Fi, and Mobile Broadband devices. NetworkManager will connect any network device when a connection for that device becomes available, unless that behavior is disabled. Information about networking is exported via a D-Bus interface to any interested application, providing a rich API with which to inspect and control network settings and operation.</p>
<h2>Dispatcher Scripts</h2>
<p>NetworkManager-dispatcher service can execute scripts for the user in response to network events. See <code><a href="/docs/linux/man/8-networkmanager-dispatcher/">NetworkManager-dispatcher</a></code>(8) manual.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;version</code> | <code>-V</code></p>
<dl>
<dd>Print the NetworkManager software version and exit.</dl>
<p> <code>&#8211;help</code> | <code>-h</code></p>
<dl>
<dd>Print NetworkManager&#8217;s available options and exit.</dl>
<p> <code>&#8211;no-daemon</code> | <code>-n</code></p>
<dl>
<dd>Do not daemonize.</dl>
<p> <code>&#8211;debug</code> | <code>-d</code></p>
<dl>
<dd>Do not daemonize, and direct log output to the controlling terminal in addition to syslog.</dl>
<p> <code>&#8211;pid-file</code> | <code>-p</code></p>
<dl>
<dd>Specify location of a PID file. The PID file is used for storing PID of the running process and prevents running multiple instances.</dl>
<p> <code>&#8211;state-file</code></p>
<dl>
<dd>Specify file for storing state of the NetworkManager persistently. If not specified, the default value of /var/lib/NetworkManager/NetworkManager.state is used.</dl>
<p> <code>&#8211;config</code></p>
<dl>
<dd>Specify configuration file to set up various settings for NetworkManager. If not specified, the default value of /etc/NetworkManager/NetworkManager.conf is used with a fallback to the older &#8216;nm-system-settings.conf&#8217; if located in the same directory. See <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5) for more information on configuration file.</dl>
<p> <code>&#8211;configure-and-quit</code> [initrd]</p>
<dl>
<dd>Quit after all devices reach a stable state. The optional initrd parameter enables mode, where no processes are left running after NetworkManager stops, which is useful for running from an initial ramdisk on rearly boot.</dl>
<p> <code>&#8211;plugins</code></p>
<dl>
<dd>List plugins used to manage system-wide connection settings. This list has preference over plugins specified in the configuration file. See main.plugins setting in <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5) for supported options.</dl>
<p> <code>&#8211;log-level</code></p>
<dl>
<dd>Sets how much information NetworkManager sends to the log destination (usually syslog&#8217;s &quot;daemon&quot; facility). By default, only informational, warning, and error messages are logged. See the section on logging in <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5) for more information.</dl>
<p> <code>&#8211;log-domains</code></p>
<dl>
<dd>A comma-separated list specifying which operations are logged to the log destination (usually syslog). By default, most domains are logging-enabled. See the section on logging in <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5) for more information.</dl>
<p> <code>&#8211;print-config</code></p>
<dl>
<dd>Print the NetworkManager configuration to stdout and exit.</dl>
<h2>Udev Properties</h2>
<p><code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) device manager is used for the network device discovery. The following property influences how NetworkManager manages the devices: </p>
<p> <i>NM_UNMANAGED</i></p>
<dl>
<dd>If set to &quot;1&quot; or &quot;true&quot;, the device is configured as unmanaged by NetworkManager. Note that the user still can explicitly overrule this configuration via means like <code>nmcli device set &quot;$DEVICE&quot; managed yes</code> or &quot;device*.managed=1&quot; in NetworkManager.conf.</dl>
<h2>Signals</h2>
<p>NetworkManager process handles the following signals: </p>
<p> <i>SIGHUP</i></p>
<dl>
<dd>The signal causes a reload of NetworkManager&#8217;s configuration. Note that not all configuration parameters can be changed at runtime and therefore some changes may be applied only after the next restart of the daemon. A SIGHUP also involves further reloading actions, like doing a DNS update and restarting the DNS plugin. The latter can be useful for example when using the dnsmasq plugin and changing its configuration in /etc/NetworkManager/dnsmasq.d. However, it also means this will shortly interrupt name resolution. In the future, there may be further actions added. A SIGHUP means to update NetworkManager configuration and reload everything that is supported. Note that this does not reload connections from disk. For that there is a D-Bus API and nmcli&#8217;s reload action</dl>
<p> <i>SIGUSR1</i></p>
<dl>
<dd>The signal forces a rewrite of DNS configuration. Contrary to SIGHUP, this does not restart the DNS plugin and will not interrupt name resolution. When NetworkManager is not managing DNS, the signal forces a restart of operations that depend on the DNS configuration (like the resolution of the system hostname via reverse DNS, or the resolution of WireGuard peers); therefore, it can be used to tell NetworkManager that the content of resolv.conf was changed externally. In the future, further actions may be added. A SIGUSR1 means to write out data like resolv.conf, or refresh a cache. It is a subset of what is done for SIGHUP without reloading configuration from disk.</dl>
<p> <i>SIGUSR2</i></p>
<dl>
<dd>The signal has no effect at the moment but is reserved for future use.</dl>
<p> An alternative to a signal to reload configuration is the Reload D-Bus call. It allows for more fine-grained selection of what to reload, it only returns after the reload is complete, and it is guarded by PolicyKit.</p>
<h2>Debugging</h2>
<p>NetworkManager only configures your system. So when your networking setup doesn&#8217;t work as expected, the first step is to look at your system to understand what is actually configured, and whether that is correct. The second step is to find out how to tell NetworkManager to do the right thing. </p>
<p> You can for example try to <code>ping</code> hosts (by IP address or DNS name), look at <code>ip link show</code>, <code>ip address show</code> and <code>ip route show</code>, and look at /etc/resolv.conf for name resolution issues. Also look at the connection profiles that you have configured in NetworkManager (<code>nmcli connection</code> and <code>nmcli connection show &quot;$PROFILE&quot;</code>) and the configured interfaces (<code>nmcli device</code>). </p>
<p> If that does not suffice, look at the logfiles of NetworkManager. NetworkManager logs to syslog, so depending on your system configuration you can call <code>journalctl</code> to get the logs. By default, NetworkManager logs are not verbose and thus not very helpful for investigating a problem in detail. You can change the logging level at runtime with <code>nmcli general logging level TRACE domains ALL</code>. But usually a better way is to collect full logs from the start, by configuring level=TRACE in NetworkManager.conf. See <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5) manual. Note that trace logs of NetworkManager are verbose and systemd-journald might rate limit some lines. Possibly disable rate limiting first with the RateLimitIntervalSec and RateLimitBurst options of journald (see <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5) manual).</p>
<h2>/Var/Lib/Networkmanager/Secret_Key And /Etc/Machine-Id</h2>
<p>The identity of a machine is important as various settings depend on it. For example, ipv6.addr-gen-mode=stable and ethernet.cloned-mac-address=stable generate identifiers by hashing the machine&#8217;s identity. See also the connection.stable-id connection property which is a per-profile seed that gets hashed with the machine identity for generating such addresses and identifiers. </p>
<p> If you backup and restore a machine, the identity of the machine probably should be preserved. In that case, preserve the files /var/lib/NetworkManager/secret_key and /etc/machine-id. On the other hand, if you clone a virtual machine, you probably want that the clone has a different identity. There is already existing tooling on Linux for handling /etc/machine-id (see <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5)). </p>
<p> The identity of the machine is determined by the /var/lib/NetworkManager/secret_key. If such a file does not exist, NetworkManager will create a file with random content. To generate a new identity just delete the file and after restart a new file will be created. The file should be read-only to root and contain at least 16 bytes that will be used to seed the various places where a stable identifier is used. </p>
<p> Since 1.16.0, NetworkManager supports a version 2 of secret-keys. For such keys /var/lib/NetworkManager/secret_key starts with ASCII &quot;nm-v2:&quot; followed by at least 32 bytes of random data. Also, recent versions of NetworkManager always create such kinds of secret-keys, when the file does not yet exist. With version 2 of the secret-key, /etc/machine-id is also hashed as part of the generation for addresses and identifiers. The advantage is that you can keep /var/lib/NetworkManager/secret_key stable, and only regenerate /etc/machine-id when cloning a VM.</p>
<h2>Bugs</h2>
<p>Please report any bugs you find in NetworkManager at the m[blue]<code>NetworkManager issue tracker</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>See Also</h2>
<p>m[blue]<code>NetworkManager home page</code>m[]<font SIZE="-2">[2]</font>, <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5), <code><a href="/docs/linux/man/8-networkmanager-dispatcher/">NetworkManager-dispatcher</a></code>(8), <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7), <code><a href="/docs/linux/man/1-nm-online/">nm-online</a></code>(1), <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5), <code><a href="/docs/linux/man/1-nm-applet/">nm-applet</a></code>(1), <code><a href="/docs/linux/man/1-nm-connection-editor/">nm-connection-editor</a></code>(1), <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>NetworkManager issue tracker</p>
<dl>
<dd><a rel="nofollow" href="https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues">https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues</a></dl>
<dt> 2.</p>
<dd>NetworkManager home page</p>
<dl>
<dd><a rel="nofollow" href="https://networkmanager.dev">https://networkmanager.dev</a></dl>
