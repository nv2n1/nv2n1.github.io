---
title: "nm-online(1)"
name: "nm-online"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nm-online/"
description: "nm-online – ask NetworkManager whether the network is connected"
---

<h2 class="name">NAME</h2>
<p> nm-online &#8211; ask NetworkManager whether the network is connected </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nm-online</code> [<i>OPTIONS</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>nm-online</code></p>
<dd>is a utility to find out whether we are online. It is done by asking NetworkManager about its status. When run, <code>nm-online</code> waits until NetworkManager reports an active connection, or specified timeout expires. On exit, the returned status code should be checked (see the return codes below). </p>
<p> This tool is not very useful to call directly. It is however used by NetworkManager-wait-online.service with &#8211;wait-for-startup argument. This is used to delay the service and indirectly network-online.target, until networking is up. Don&#8217;t order your own systemd services after NetworkManager-wait-online.service directly. Instead if necessary, order your services after network-online.target. Even better is to have your services react to network changes dynamically and don&#8217;t order them with respect to network-online.target at all. </p>
<p> By default, connections have the ipv4.may-fail and ipv6.may-fail properties set to yes; this means that NetworkManager waits for one of the two address families to complete configuration before considering the connection activated. If you need a specific address family configured before network-online.target is reached, set the corresponding may-fail property to no.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code> | <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help information.</dl>
<p> <code>-q</code> | <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Don&#8217;t print anything.</dl>
<p> <code>-s</code> | <code>&#8211;wait-for-startup</code></p>
<dl>
<dt>
<dd> Wait for NetworkManager startup to complete, rather than waiting for network connectivity specifically. Startup is considered complete once NetworkManager has activated (or attempted to activate) every auto-activate connection which is available given the current network state. This corresponds to the moment when NetworkManager logs &quot;startup complete&quot;. This mode is generally only useful at boot time. After startup has completed, <code>nm-online -s</code> will just return immediately, regardless of the current network state. </p>
<p> There are various ways to affect when startup complete is reached. For example, by setting a connection profile to autoconnect, such a profile possibly will activate during startup and thus delay startup complete being reached. Also, a profile is considered ready when it fully reached the logical connected state in NetworkManager. That means, properties like ipv4.may-fail and ipv6.may-fail affect whether a certain address family is required. Also, the connection property connection.wait-device-timeout affects whether to wait for the driver to detect a certain device. Generally, a failure of NetworkManager-wait-online.service indicates a configuration error, where NetworkManager won&#8217;t be able to reach the desired connectivity state during startup. An example for that are bridge or bond master profiles, that get autoconnected but without activating any slaves. Such master devices hang in activating state indefinitely, and cause NetworkManager-wait-online.service to fail.</dl>
<p> <code>-t</code> | <code>&#8211;timeout</code> <i>seconds</i></p>
<dl>
<dt>
<dd> Time to wait for a connection, in seconds. If the option is not provided, the environment variable NM_ONLINE_TIMEOUT is honored. The default timeout is 30 seconds.</dl>
<p> <code>-x</code> | <code>&#8211;exit</code></p>
<dl>
<dt>
<dd> Exit immediately if NetworkManager is not running or connecting.</dl>
<h2>EXIT STATUS</h2>
<p> <code>nm-online</code> exits with status 0 if it succeeds, a value greater than 0 is returned if an error occurs. </p>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success &#8211; already online or connection established within given timeout.</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Offline or not online within given timeout.</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> Unknown or unspecified error.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8). </p>
<h2>Index</h2>
