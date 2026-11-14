---
title: "games_srv_selinux(8)"
name: "games_srv_selinux"
section: "8"
letter: "g"
url: "/docs/linux/man/8-games_srv_selinux/"
description: "games_srv_selinux – Security Enhanced Linux Policy for the games_srv processes"
---

<p>games_srv_selinux &#8211; Security Enhanced Linux Policy for the games_srv processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the games_srv processes via flexible mandatory access control. The games_srv processes execute with the games_srv_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep games_srv_t</code> </p>
<h2>Entrypoints</h2>
<p>The games_srv_t SELinux type can be entered via the <code>games_exec_t</code> file type. </p>
<p> The default entrypoint paths for the games_srv_t domain are the following: </p>
<p> /usr/games/.*, /usr/lib/games(/.*)?, /usr/bin/civclient.*, /usr/bin/civserver.*, /usr/bin/sol, /usr/bin/kolf, /usr/bin/kpat, /usr/bin/micq, /usr/bin/gnect, /usr/bin/gtali, /usr/bin/iagno, /usr/bin/ksame, /usr/bin/ktron, /usr/bin/kwin4, /usr/bin/lskat, /usr/bin/gataxx, /usr/bin/glines, /usr/bin/klines, /usr/bin/kmines, /usr/bin/kpoker, /usr/bin/ksnake, /usr/bin/gnomine, /usr/bin/gnotski, /usr/bin/katomic, /usr/bin/kbounce, /usr/bin/kshisen, /usr/bin/ksirtet, /usr/bin/atlantik, /usr/bin/gnibbles, /usr/bin/gnobots2, /usr/bin/kenolaba, /usr/bin/klickety, /usr/bin/konquest, /usr/bin/kreversi, /usr/bin/ksokoban, /usr/bin/mahjongg, /usr/bin/blackjack, /usr/bin/gnotravex, /usr/bin/kblackbox, /usr/bin/kfouleggs, /usr/bin/kmahjongg, /usr/bin/kwin4proc, /usr/bin/lskatproc, /usr/bin/Maelstrom, /usr/bin/kasteroids, /usr/bin/ksmiletris, /usr/bin/kspaceduel, /usr/bin/ktuberling, /usr/bin/same-gnome, /usr/bin/kbackgammon, /usr/bin/kbattleship, /usr/bin/kgoldrunner, /usr/bin/gnome-stones, /usr/bin/kjumpingcube</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux games_srv policy is very flexible allowing users to setup their games_srv processes in as secure a method as possible. </p>
<p> The following process types are defined for games_srv: </p>
<p> games_srv_t</code> </p>
<p> Note: <code>semanage permissive -a games_srv_t</code> can be used to make the process type games_srv_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. games_srv policy is extremely flexible and has several booleans that allow you to manipulate the policy and run games_srv with the tightest access possible. </p>
<p> If you want to allow all daemons the ability to read/write terminals, you must turn on the daemons_use_tty boolean. Disabled by default. </p>
<p> <code>setsebool -P daemons_use_tty 1</code> </p>
<p> If you want to deny any process from ptracing or debugging any other processes, you must turn on the deny_ptrace boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_ptrace 1</code> </p>
<p> If you want to allow all domains to use other domains file descriptors, you must turn on the domain_fd_use boolean. Enabled by default. </p>
<p> <code>setsebool -P domain_fd_use 1</code> </p>
<p> If you want to allow all domains to have the kernel load modules, you must turn on the domain_kernel_load_modules boolean. Disabled by default. </p>
<p> <code>setsebool -P domain_kernel_load_modules 1</code> </p>
<p> If you want to allow all domains to execute in fips_mode, you must turn on the fips_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P fips_mode 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type games_srv_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>games_data_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/games(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/games(/.*)?</p>
<p> <code>games_srv_var_run_t</code></p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-games_srv/">games_srv</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8) </p>
