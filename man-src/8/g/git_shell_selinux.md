---
title: "git_shell_selinux(8)"
name: "git_shell_selinux"
section: "8"
letter: "g"
url: "/docs/linux/man/8-git_shell_selinux/"
description: "git_shell_u – git_shell user role – Security Enhanced Linux Policy"
---

<p>git_shell_u &#8211; <code>git_shell user role</code> &#8211; Security Enhanced Linux Policy </p>
<h2>Description</h2>
<p><code>git_shell_u</code> is an SELinux User defined in the SELinux policy. SELinux users have default roles, <code>git_shell_r</code>. The default role has a default type, <code>git_shell_t</code>, associated with it. The SELinux user will usually login to a system with a context that looks like: <code>git_shell_u:git_shell_r:git_shell_u:s0-s0:c0.c1023</code> Linux users are automatically assigned an SELinux users at login. Login programs use the SELinux User to assign initial context to the user&#8217;s shell. SELinux policy uses the context to control the user&#8217;s access. By default all users are assigned to the SELinux user via the <code>__default__</code> flag On Targeted policy systems the <code>__default__</code> user is assigned to the <code>unconfined_u</code> SELinux user. You can list all Linux User to SELinux user mapping using: <code>semanage login -l</code> If you wanted to change the default user mapping to use the git_shell_u user, you would execute: <code>semanage login -m -s git_shell_u __default__</code> </p>
<h2>User Description</h2>
<p>The SELinux user git_shell_u is defined in policy as a unprivileged user. SELinux prevents unprivileged users from doing administration tasks without transitioning to a different role.</p>
<h2>Sudo</h2>
<p>The SELinux type git_shell_t is not allowed to execute sudo.</p>
<h2>X Windows Login</h2>
<p>The SELinux user git_shell_u is not able to X Windows login.</p>
<h2>Terminal Login</h2>
<p>The SELinux user git_shell_u is not able to terminal login.</p>
<h2>Network</h2>
<dl>
<dt>The SELinux user git_shell_u is able to connect to the following tcp ports.</p>
<dd><code>dns_port_t: 53</code> </p>
<p> <code>ocsp_port_t: 9080</code> </p>
<p> <code>kerberos_port_t: 88,750,4444</code> </p>
</dl>
<h2>Booleans</h2>
<p>SELinux policy is customizable based on least access required. git_shell_t policy is extremely flexible and has several booleans that allow you to manipulate the policy and run git_shell_t with the tightest access possible. </p>
<p> If you want to allow users to connect to the local mysql server, you must turn on the allow_user_mysql_connect boolean. </p>
<p> <code>setsebool -P allow_user_mysql_connect 1</code> </p>
<p> If you want to control users use of ping and traceroute, you must turn on the user_ping boolean. </p>
<p> <code>setsebool -P user_ping 1</code> </p>
<p> If you want to allow w to display everyone, you must turn on the user_ttyfile_stat boolean. </p>
<p> <code>setsebool -P user_ttyfile_stat 1</code> </p>
<p> If you want to allow user music sharing, you must turn on the user_share_music boolean. </p>
<p> <code>setsebool -P user_share_music 1</code> </p>
<p> If you want to allow regular users direct dri device access, you must turn on the user_direct_dri boolean. </p>
<p> <code>setsebool -P user_direct_dri 1</code> </p>
<p> If you want to allow user to r/w files on filesystems that do not have extended attributes (FAT, CDROM, FLOPPY), you must turn on the user_rw_noexattrfile boolean. </p>
<p> <code>setsebool -P user_rw_noexattrfile 1</code> </p>
<p> If you want to allow users to run TCP servers (bind to ports and accept connection from the same domain and outside users) disabling this forces FTP passive mode and may change other protocols, you must turn on the user_tcp_server boolean. </p>
<p> <code>setsebool -P user_tcp_server 1</code> </p>
<p> If you want to allow regular users direct mouse access, you must turn on the user_direct_mouse boolean. </p>
<p> <code>setsebool -P user_direct_mouse 1</code> </p>
<p> If you want to allow user processes to change their priority, you must turn on the user_setrlimit boolean. </p>
<p> <code>setsebool -P user_setrlimit 1</code> </p>
<p> If you want to allow users to connect to PostgreSQL, you must turn on the allow_user_postgresql_connect boolean. </p>
<p> <code>setsebool -P allow_user_postgresql_connect 1</code> </p>
<p> If you want to allow users to read system messages, you must turn on the user_dmesg boolean. </p>
<p> <code>setsebool -P user_dmesg 1</code></p>
<h2>Home_Exec</h2>
<p>The SELinux user git_shell_u is able execute home content files.</p>
<h2>Transitions</h2>
<p>Three things can happen when git_shell_t attempts to execute a program. </p>
<p> <code>1.</code> SELinux Policy can deny git_shell_t from executing the program. </p>
<dl>
<dd><code>2.</code> SELinux Policy can allow git_shell_t to execute the program in the current user type. </p>
<p> Execute the following to see the types that the SELinux user git_shell_t can execute without transitioning: </p>
<p> <code>sesearch -A -s git_shell_t -c file -p execute_no_trans</code> </p>
<dd><code>3.</code> SELinux can allow git_shell_t to execute the program and transition to a new type. </p>
<p> Execute the following to see the types that the SELinux user git_shell_t can execute and transition: </p>
<p> <code>$ sesearch -A -s git_shell_t -c process -p transition</code> </p>
</dl>
<h2>Commands</h2>
<p><code>semanage login</code> can also be used to manipulate the Linux User to SELinux User mappings </p>
<p> <code>semanage user</code> can also be used to manipulate SELinux user definitions. </p>
<p> <code>system-config-selinux </code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was autogenerated by genuserman.py.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8). </p>
