---
title: "systemd-networkd-wait-online(8)"
name: "systemd-networkd-wait-online"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-networkd-wait-online/"
description: "systemd-networkd-wait-online.service, systemd-networkd-wait-online – Wait for network to come online"
---

<p>systemd-networkd-wait-online.service, systemd-networkd-wait-online &#8211; Wait for network to come online</p>
<h2>Synopsis</h2>
<p>systemd-networkd-wait-online.service </p>
<p> /lib/systemd/systemd-networkd-wait-online</p>
<h2>Description</h2>
<p><code>systemd-networkd-wait-online</code> is a oneshot system service (see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5)), that waits for the network to be configured. By default, it will wait for all links it is aware of and which are managed by <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) to be fully configured or failed, and for at least one link to be online. Here, online means that the link&#8217;s operational state is equal or higher than &quot;degraded&quot;. The threshold can be configured by <code>&#8211;operational-state=</code> option.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>-i</code> <i>INTERFACE</i>[:<i>MIN_OPERSTATE</i>[:<i>MAX_OPERSTATE</i>]], <code>&#8211;interface=</code><i>INTERFACE</i>[:<i>MIN_OPERSTATE</i>[:<i>MAX_OPERSTATE</i>]]</p>
<dl>
<dd>Network interface to wait for before deciding if the system is online. This is useful when a system has several interfaces which will be configured, but a particular one is necessary to access some network resources. When used, all other interfaces are ignored. This option may be used more than once to wait for multiple network interfaces. When this option is specified multiple times, then <code>systemd-networkd-wait-online</code> waits for all specified interfaces to be online. Optionally, required minimum and maximum operational states can be specified after a colon &quot;:&quot;. Please see <code><a href="/docs/linux/man/1-networkctl/">networkctl</a></code>(1) for possible operational states. If the operational state is not specified here, then the value from <i>RequiredForOnline=</i> in the corresponding .network file is used if present, and &quot;degraded&quot; otherwise.</dl>
<p> <code>&#8211;ignore=</code><i>INTERFACE</i></p>
<dl>
<dd>Network interfaces to be ignored when deciding if the system is online. By default, only the loopback interface is ignored. This option may be used more than once to ignore multiple network interfaces.</dl>
<p> <code>-o</code> <i>MIN_OPERSTATE</i>[:<i>MAX_OPERSTATE</i>], <code>&#8211;operational-state=</code><i>MIN_OPERSTATE</i>[:<i>MAX_OPERSTATE</i>]</p>
<dl>
<dd>Takes a minimum operational state and an optional maximum operational state. Please see <code><a href="/docs/linux/man/1-networkctl/">networkctl</a></code>(1) for possible operational states. If set, the specified value overrides <i>RequiredForOnline=</i> settings in .network files. But this does not override operational states specified in <code>&#8211;interface=</code> option.</dl>
<p> <code>-4</code>, <code>&#8211;ipv4</code></p>
<dl>
<dd>Waiting for an IPv4 address of each network interface to be configured. If this option is specified with <code>&#8211;any</code>, then <code>systemd-networkd-wait-online</code> exits with success when at least one interface becomes online and has an IPv4 address. The option is applied only for the operational state &quot;degraded&quot; or above. If neither <code>&#8211;ipv4</code> nor <code>&#8211;ipv6</code> is specified, then the value from <i>RequiredFamilyForOnline=</i> in the corresponding .network file is used if present.</dl>
<p> <code>-6</code>, <code>&#8211;ipv6</code></p>
<dl>
<dd>Waiting for an IPv6 address of each network interface to be configured. If this option is specified with <code>&#8211;any</code>, then <code>systemd-networkd-wait-online</code> exits with success when at least one interface becomes online and has an IPv6 address. The option is applied only for the operational state &quot;degraded&quot; or above. If neither <code>&#8211;ipv4</code> nor <code>&#8211;ipv6</code> is specified, then the value from <i>RequiredFamilyForOnline=</i> in the corresponding .network file is used if present.</dl>
<p> <code>&#8211;any</code></p>
<dl>
<dd>Even if several interfaces are in configuring state, <code>systemd-networkd-wait-online</code> exits with success when at least one interface becomes online. When this option is specified with <code>&#8211;interface=</code>, then <code>systemd-networkd-wait-online</code> waits for one of the specified interfaces to be online. This option is useful when some interfaces may not have carrier on boot.</dl>
<p> <code>&#8211;timeout=</code><i>SECS</i></p>
<dl>
<dd>Fail the service if the network is not online by the time the timeout elapses. A timeout of 0 disables the timeout. Defaults to 120 seconds.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Suppress log messages.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8), <code><a href="/docs/linux/man/1-networkctl/">networkctl</a></code>(1) </p>
