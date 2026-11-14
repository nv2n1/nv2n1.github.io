---
title: "tracker-preferences(1)"
name: "tracker-preferences"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-preferences/"
description: "tracker-preferences – Preferences editor for tracker-miner-fs"
---

<h2 class="name">NAME</h2>
<p> tracker-preferences &#8211; Preferences editor for tracker-miner-fs</p>
<h2>SYNOPSIS</h2>
<p> <code>tracker-preferences</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>tracker-preferences</code> is a graphical configuration front end for the <code>tracker-miner-fs</code> which crawls and mines data from the filesystem to be stored in the Tracker databases. </p>
<p> Importantly, the <code>TRACKER_USE_CONFIG_FILES</code> environment variable which can be used by the <code>tracker-miner-fs</code> and other binaries for switching from GSettings to config files is not supported by <code>tracker-preferences.</code> This means that configuration changes (usually stored in <i>$HOME/.config/tracker</i>) must be manually updated when not using GSettings.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-miner-fs/">tracker-miner-fs</a></code>(1), <code><a href="/docs/linux/man/1-tracker-control/">tracker-control</a></code>(1), <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1). </p>
<h2>Index</h2>
