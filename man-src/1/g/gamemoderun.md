---
title: "gamemoderun(1)"
name: "gamemoderun"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gamemoderun/"
description: "gamemoderun – invoke gamemode into any program"
---

<h2 class="name">NAME</h2>
<p> gamemoderun &#8211; invoke gamemode into any program </p>
<h2>SYNOPSIS</h2>
<p> <code>gamemoderun</code> PROGRAM</p>
<h2>DESCRIPTION</h2>
<p> <code>GameMode</code> is a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS. </p>
<p> The design has a clear cut abstraction between the host daemon and library (<code>gamemoded</code> and <code>libgamemode</code>), and the client loaders (<code>libgamemodeauto</code> and <code>gamemode_client.h</code>) that allows for safe usage without worrying about whether the daemon is installed or running. This design also means that while the host library currently relies on systemd for exchanging messages with the daemon, it&#8217;s entirely possible to implement other internals that still work with the same clients. </p>
<p> <code>GameMode</code> was designed primarily as a stop-gap solution to problems with the Intel and AMD CPU powersave or ondemand governors, but is intended to be expanded beyond just CPU governor states, as there are a wealth of automation tasks one might want to apply. </p>
<h2>USAGE</h2>
<p> <code>libgamemodeauto.so.0</code> can be pre-loaded into any program to request <code>gamemoded</code> begin or end the mode, like so: </p>
<dl>
<dt>
<dd> gamemoderun ./game</dl>
<p> Or by setting the Steam launch options for a game: </p>
<dl>
<dt>
<dd> gamemoderun %command%</dl>
<p> The library can be manually preloaded if needed: </p>
<dl>
<dt>
<dd> LD_PRELOAD=$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0 ./game</dl>
<h2>CONFIG</h2>
<p> It is possible to set additional start commands to gamemoderun by setting the environment variable: </p>
<dl>
<dt>
<dd> GAMEMODERUNEXEC=&quot;command&quot;</dl>
<p> When this is set, gamemoderun will execute the command given by that environment variable, and the command line passed to gamemoderun will be passed as arguments to that command. GameMode will not be applied to the wrapper command, just the game itself. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-gamemoded/">gamemoded</a>(8) </p>
<h2>ABOUT</h2>
<p> GameMode source can be found at <i><a rel="nofollow" href="https://github.com/FeralInteractive/gamemode.git">https://github.com/FeralInteractive/gamemode.git</a></i> </p>
<h2>AUTHOR</h2>
<p> Feral Interactive (linux-contact [at] feralinteractive.com) </p>
<h2>Index</h2>
