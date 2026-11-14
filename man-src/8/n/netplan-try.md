---
title: "netplan-try(8)"
name: "netplan-try"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netplan-try/"
description: "netplan-try – try a configuration, optionally rolling it back"
---

<p>netplan-try &#8211; try a configuration, optionally rolling it back</p>
<h2>Synopsis</h2>
<p>netplan [-debug] try -h | -help </p>
<p> netplan [-debug] try [-config-file CONFIG_FILE] [-timeout TIMEOUT]</p>
<h2>Description</h2>
<p>netplan try takes a <a href="/docs/linux/man/5-netplan/">netplan</a>(5) configuration, applies it, and automatically rolls it back if the user does not confirm the configuration within a time limit. </p>
<p> This may be especially useful on remote systems, to prevent an administrator being permanently locked out of systems in the case of a network configuration error.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, -help</code></p>
<dd>Print basic help.</p>
<dt><code>-debug</code></p>
<dd>Print debugging output during the process.</p>
<dt><code>-config-file </code>CONFIG_FILE</p>
<dd>In addition to the usual configuration, apply CONFIG_FILE. It must be a YAML file in the <a href="/docs/linux/man/5-netplan/">netplan</a>(5) format.</p>
<dt><code>-timeout </code>TIMEOUT</p>
<dd>Wait for TIMEOUT seconds before reverting. Defaults to 120 seconds. Note that some network configurations (such as STP) may take over a minute to settle.</dl>
<h2>Known Issues</h2>
<p>netplan try uses similar procedures to netplan apply, so some of the same caveats apply around virtual devices. </p>
<p> There are also some known bugs: if netplan try times out or is cancelled, make sure to verify if the network configuration has in fact been reverted. </p>
<p> As with netplan apply, a reboot should fix any issues. However, be sure to verify that the config on disk is in the state you expect before rebooting!</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-netplan/">netplan</a>(5), <a href="/docs/linux/man/8-netplan-generate/">netplan-generate</a>(8), <a href="/docs/linux/man/8-netplan-apply/">netplan-apply</a>(8)</p>
<h2>Authors</h2>
<p>Daniel Axtens (&lt;daniel.axtens [at] canonical.com&gt;).</p>
