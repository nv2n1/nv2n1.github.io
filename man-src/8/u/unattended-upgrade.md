---
title: "unattended-upgrade(8)"
name: "unattended-upgrade"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unattended-upgrade/"
description: "unattended-upgrade – automatic installation of security (and other) upgrades"
---

<p>unattended-upgrade &#8211; automatic installation of security (and other) upgrades</p>
<h2>Synopsis</h2>
<p><code>unattended-upgrade</code> [options]</p>
<h2>Description</h2>
<p>This program can download and install security upgrades automatically and unattended, taking care to only install packages from the configured APT source, and checking for dpkg prompts about configuration file changes. All operations are logged to /var/log/unattended-upgrades/unattended-upgrades.log and the package manager (dpkg) output is logged to /var/log/unattended-upgrades/unattended-upgrades-dpkg.log </p>
<p> This script is the backend for the APT::Periodic::Unattended-Upgrade option and designed to be run periodically by APT&#8217;s systemd service (apt-daily-upgrade.service) or from cron (e.g. via /etc/cron.daily/apt).</p>
<h2>Options</h2>
<p>unattended-upgrade accepts the following options:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>help output</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>extra debug output into /var/log/unattended-upgrades/unattended-upgrades.log</p>
<dt><code>&#8211;apt-debug</code></p>
<dd>detailed APT/LibAPT output for debugging</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>show verbose output</p>
<dt><code>&#8211;dry-run</code></p>
<dd>Just simulate installing updates, do not actually do it</p>
<dt><code>&#8211;minimal-upgrade-steps</code></p>
<dd>perform upgrade in minimal steps (cancel with SIGINT). This is the default now.</p>
<dt><code>&#8211;no-minimal-upgrade-steps</code></p>
<dd>do not perform upgrade in minimal steps </p>
</dl>
<h2>Configuration</h2>
<p>The configuration is done via the apt configuration mechanism. The default configuration file can be found at /etc/apt/apt.conf.d/50unattended-upgrades</p>
<h2>Authors</h2>
<p>unattended-upgrade is written by Michael Vogt &lt;mvo [at] ubuntu.com&gt; </p>
<p> This manual page was originally written by Michael Vogt &lt;mvo [at] ubuntu.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 2005-2009 Canonical </p>
<p> There is NO warranty. You may redistribute this software under the terms of the GNU General Public License. For more information about these matters, see the files named COPYING.</p>
