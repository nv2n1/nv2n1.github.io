---
title: "ifplugd(5)"
name: "ifplugd"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ifplugd/"
description: "ifplugd.conf – ifplugd configuration file"
---

<p>ifplugd.conf &#8211; ifplugd configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/ifplugd/ifplugd.conf </code></p>
<h2>Description</h2>
<p>ifplugd.conf is the configuration file for ifplugd. It is a shell script that is sourced by the init script starting the daemon. It shall be used to set environment variables which are interpreted by the init script:</p>
<h2>Options</h2>
<dl>
<dt><code>INTERFACES</code></p>
<dd>Specifies the ethernet interfaces to monitor. It has to contain a space seperated list of network interfaces names. Most users will probably use &quot;eth0&quot; here, however you may add additional interfaces for monitoring more than one device. A special value is supported as well: &quot;auto&quot; will enable a more or less working auto detection of available network devices. This won&#8217;t make you happy when using network module auto loading, since it cannot detect currently unloaded network devices.</p>
<dt><code>ARGS</code></p>
<dd>Additional command line arguments for ifplugd invocation. See <code><a href="/docs/linux/man/8-ifplugd/">ifplugd</a>(8)</code> for further information.</p>
<dt><code>ARGS_</code><i>iface</i></p>
<dd>If specified for an interface this variable takes precedence over ARGS. This may be useful if more than one network device is present.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ifplugd/">ifplugd</a>(8)</code></p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xmltoman/">xmltoman</a>(1)</code> by Oliver Kurth.</p>
