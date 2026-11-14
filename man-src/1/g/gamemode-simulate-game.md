---
title: "gamemode-simulate-game(1)"
name: "gamemode-simulate-game"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gamemode-simulate-game/"
description: "gamemode-simulate-game – simulate a game using gamemode"
---

<h2 class="name">NAME</h2>
<p> gamemode-simulate-game &#8211; simulate a game using gamemode </p>
<h2>SYNOPSIS</h2>
<p> <code>gamemode-simulate-game</code></p>
<h2>DESCRIPTION</h2>
<p> <code>GameMode</code> is a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS. </p>
<p> The design has a clear cut abstraction between the host daemon and library (<code>gamemoded</code> and <code>libgamemode</code>), and the client loaders (<code>libgamemodeauto</code> and <code>gamemode_client.h</code>) that allows for safe usage without worrying about whether the daemon is installed or running. This design also means that while the host library currently relies on systemd for exchanging messages with the daemon, it&#8217;s entirely possible to implement other internals that still work with the same clients. </p>
<p> <code>GameMode</code> was designed primarily as a stop-gap solution to problems with the Intel and AMD CPU powersave or ondemand governors, but is intended to be expanded beyond just CPU governor states, as there are a wealth of automation tasks one might want to apply. </p>
<h2>USAGE</h2>
<p> The executable starts gamemode, sleeps for 10 seconds and stops it. It will exit with zero if everything works fine, else it will print an error and exit with one. </p>
<p> To use this with a CI you might need to start a dbus session by hand. This can be done with: </p>
<dl>
<dt>
<dd> dbus-run-session &#8212; gamemode-simulate-game</dl>
<p> Note that this might output to stderr, even if it exits with zero. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-gamemoded/">gamemoded</a>(8), <a href="/docs/linux/man/1-gamemoderun/">gamemoderun</a>(1), <a href="/docs/linux/man/1-dbus-run-session/">dbus-run-session</a>(1) </p>
<h2>ABOUT</h2>
<p> GameMode source can be found at <i><a rel="nofollow" href="https://github.com/FeralInteractive/gamemode.git">https://github.com/FeralInteractive/gamemode.git</a></i> </p>
<h2>AUTHOR</h2>
<p> Feral Interactive (linux-contact [at] feralinteractive.com) </p>
<h2>Index</h2>
