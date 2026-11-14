---
title: "games_selinux(8)"
name: "games_selinux"
section: "8"
letter: "g"
url: "/docs/linux/man/8-games_selinux/"
description: "games_selinux – Security Enhanced Linux Policy for the games processes"
---

<p>games_selinux &#8211; Security Enhanced Linux Policy for the games processes</p>
<h2>Description</h2>
<p>Security-Enhanced Linux secures the games processes via flexible mandatory access control. The games processes execute with the games_t SELinux type. You can check if you have these processes running by executing the <code>ps</code> command with the <code>-Z</code> qualifier. For example: <code>ps -eZ | grep games_t</code> </p>
<h2>Entrypoints</h2>
<p>The games_t SELinux type can be entered via the <code>games_exec_t</code> file type. </p>
<p> The default entrypoint paths for the games_t domain are the following: </p>
<p> /usr/games/.*, /usr/lib/games(/.*)?, /usr/bin/civclient.*, /usr/bin/civserver.*, /usr/bin/sol, /usr/bin/kolf, /usr/bin/kpat, /usr/bin/micq, /usr/bin/gnect, /usr/bin/gtali, /usr/bin/iagno, /usr/bin/ksame, /usr/bin/ktron, /usr/bin/kwin4, /usr/bin/lskat, /usr/bin/gataxx, /usr/bin/glines, /usr/bin/klines, /usr/bin/kmines, /usr/bin/kpoker, /usr/bin/ksnake, /usr/bin/gnomine, /usr/bin/gnotski, /usr/bin/katomic, /usr/bin/kbounce, /usr/bin/kshisen, /usr/bin/ksirtet, /usr/bin/atlantik, /usr/bin/gnibbles, /usr/bin/gnobots2, /usr/bin/kenolaba, /usr/bin/klickety, /usr/bin/konquest, /usr/bin/kreversi, /usr/bin/ksokoban, /usr/bin/mahjongg, /usr/bin/blackjack, /usr/bin/gnotravex, /usr/bin/kblackbox, /usr/bin/kfouleggs, /usr/bin/kmahjongg, /usr/bin/kwin4proc, /usr/bin/lskatproc, /usr/bin/Maelstrom, /usr/bin/kasteroids, /usr/bin/ksmiletris, /usr/bin/kspaceduel, /usr/bin/ktuberling, /usr/bin/same-gnome, /usr/bin/kbackgammon, /usr/bin/kbattleship, /usr/bin/kgoldrunner, /usr/bin/gnome-stones, /usr/bin/kjumpingcube</p>
<h2>Process Types</h2>
<p>SELinux defines process types (domains) for each process running on the system </p>
<p> You can see the context of a process using the <code>-Z</code> option to <code>psP Policy governs the access confined processes have to files. SELinux games policy is very flexible allowing users to setup their games processes in as secure a method as possible. </p>
<p> The following process types are defined for games: </p>
<p> games_t, games_srv_t</code> </p>
<p> Note: <code>semanage permissive -a games_t</code> can be used to make the process type games_t permissive. SELinux does not deny access to permissive process types, but the AVC (SELinux denials) messages are still generated.</p>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. games policy is extremely flexible and has several booleans that allow you to manipulate the policy and run games with the tightest access possible. </p>
<p> If you want to deny user domains applications to map a memory region as both executable and writable, this is dangerous and the executable should be reported in bugzilla, you must turn on the deny_execmem boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_execmem 1</code> </p>
<p> If you want to deny any process from ptracing or debugging any other processes, you must turn on the deny_ptrace boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_ptrace 1</code> </p>
<p> If you want to allow all domains to use other domains file descriptors, you must turn on the domain_fd_use boolean. Enabled by default. </p>
<p> <code>setsebool -P domain_fd_use 1</code> </p>
<p> If you want to allow all domains to have the kernel load modules, you must turn on the domain_kernel_load_modules boolean. Disabled by default. </p>
<p> <code>setsebool -P domain_kernel_load_modules 1</code> </p>
<p> If you want to allow all domains to execute in fips_mode, you must turn on the fips_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P fips_mode 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
<p> If you want to allow confined applications to use nscd shared memory, you must turn on the nscd_use_shm boolean. Disabled by default. </p>
<p> <code>setsebool -P nscd_use_shm 1</code> </p>
<p> If you want to allow regular users direct dri device access, you must turn on the selinuxuser_direct_dri_enabled boolean. Enabled by default. </p>
<p> <code>setsebool -P selinuxuser_direct_dri_enabled 1</code> </p>
<p> If you want to support NFS home directories, you must turn on the use_nfs_home_dirs boolean. Disabled by default. </p>
<p> <code>setsebool -P use_nfs_home_dirs 1</code> </p>
<p> If you want to allows clients to write to the X server shared memory segments, you must turn on the xserver_clients_write_xshm boolean. Disabled by default. </p>
<p> <code>setsebool -P xserver_clients_write_xshm 1</code> </p>
<p> If you want to support X userspace object manager, you must turn on the xserver_object_manager boolean. Enabled by default. </p>
<p> <code>setsebool -P xserver_object_manager 1</code></p>
<h2>Managed Files</h2>
<p>The SELinux process type games_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <code>games_data_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/games(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/lib/games(/.*)?</p>
<p> <code>games_tmp_t</code> </p>
<p> <code>games_tmpfs_t</code> </p>
<p> <code>user_fonts_cache_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/root/.fonts.cache-.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fontconfig(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts/auto(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.fonts.cache-.*</p>
<p> <code>user_tmp_t</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/shm/mono.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/run/user(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/.X11-unix(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/.ICE-unix(/.*)?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/shm/pulse-shm.*</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/.X0-lock</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/hsperfdata_root</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/tmp/hsperfdata_root</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/tmp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/[^/]+/.tmp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/tmp/gconfd-[^/]+</p>
<p> <code>xserver_tmpfs_t</code></p>
<h2>File Contexts</h2>
<p>SELinux requires files to have an extended attribute to define the file type. </p>
<p> You can see the context of a file using the <code>-Z</code> option to <code>lsP Policy governs the access confined processes have to these files. SELinux games policy is very flexible allowing users to setup their games processes in as secure a method as possible. </p>
<p> STANDARD FILE CONTEXT</code> </p>
<p> SELinux defines the file context types for the games, if you wanted to store files with these types in a diffent paths, you need to execute the semanage command to sepecify alternate labeling and then use restorecon to put the labels on disk. </p>
<p> <code>semanage fcontext -a -t games_tmpfs_t &#8216;/srv/mygames_content(/.*)?&#8217;</code><br />
 <code>restorecon -R -v /srv/mygames_content</code> </p>
<p> Note: SELinux often uses regular expressions to specify labels that match multiple files. </p>
<p> <i>The following file types are defined for games:</i> </p>
<p> <code>games_data_t</code> </p>
<p> &#8211; Set files with the games_data_t type, if you want to treat the files as games content. </p>
<dl>
<dt>Paths:</p>
<dd>/var/games(/.*)?, /var/lib/games(/.*)? </p>
</dl>
<p> <code>games_exec_t</code> </p>
<p> &#8211; Set files with the games_exec_t type, if you want to transition an executable to the games_t domain. </p>
<dl>
<dt>Paths:</p>
<dd>/usr/games/.*, /usr/lib/games(/.*)?, /usr/bin/civclient.*, /usr/bin/civserver.*, /usr/bin/sol, /usr/bin/kolf, /usr/bin/kpat, /usr/bin/micq, /usr/bin/gnect, /usr/bin/gtali, /usr/bin/iagno, /usr/bin/ksame, /usr/bin/ktron, /usr/bin/kwin4, /usr/bin/lskat, /usr/bin/gataxx, /usr/bin/glines, /usr/bin/klines, /usr/bin/kmines, /usr/bin/kpoker, /usr/bin/ksnake, /usr/bin/gnomine, /usr/bin/gnotski, /usr/bin/katomic, /usr/bin/kbounce, /usr/bin/kshisen, /usr/bin/ksirtet, /usr/bin/atlantik, /usr/bin/gnibbles, /usr/bin/gnobots2, /usr/bin/kenolaba, /usr/bin/klickety, /usr/bin/konquest, /usr/bin/kreversi, /usr/bin/ksokoban, /usr/bin/mahjongg, /usr/bin/blackjack, /usr/bin/gnotravex, /usr/bin/kblackbox, /usr/bin/kfouleggs, /usr/bin/kmahjongg, /usr/bin/kwin4proc, /usr/bin/lskatproc, /usr/bin/Maelstrom, /usr/bin/kasteroids, /usr/bin/ksmiletris, /usr/bin/kspaceduel, /usr/bin/ktuberling, /usr/bin/same-gnome, /usr/bin/kbackgammon, /usr/bin/kbattleship, /usr/bin/kgoldrunner, /usr/bin/gnome-stones, /usr/bin/kjumpingcube </p>
</dl>
<p> <code>games_srv_var_run_t</code> </p>
<p> &#8211; Set files with the games_srv_var_run_t type, if you want to store the games srv files under the /run or /var/run directory. </p>
<p> <code>games_tmp_t</code> </p>
<p> &#8211; Set files with the games_tmp_t type, if you want to store games temporary files in the /tmp directories. </p>
<p> <code>games_tmpfs_t</code> </p>
<p> &#8211; Set files with the games_tmpfs_t type, if you want to store games files on a tmpfs file system. </p>
<p> Note: File context can be temporarily modified with the chcon command. If you want to permanently change the file context you need to use the <code>semanage fcontext</code> command. This will modify the SELinux labeling database. You will need to use <code>restorecon</code> to apply the labels.</p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-games/">games</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-games_srv_selinux/">games_srv_selinux</a>(8), <a href="/docs/linux/man/8-games_srv_selinux/">games_srv_selinux</a>(8) </p>
