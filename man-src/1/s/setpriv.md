---
title: "setpriv(1)"
name: "setpriv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setpriv/"
description: "setpriv – run a program with different Linux privilege settings"
---

<h2 class="name">NAME</h2>
<p> setpriv &#8211; run a program with different Linux privilege settings </p>
<h2>SYNOPSIS</h2>
<p> <code>setpriv</code> [options] <i>program</i> [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> Sets or queries various Linux privilege settings that are inherited across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> In comparison to <code><a href="/docs/linux/man/1-su/">su</a></code>(1) and <code><a href="/docs/linux/man/1-runuser/">runuser</a></code>(1), <code>setpriv</code> neither uses PAM, nor does it prompt for a password. It is a simple, non-set-user-ID wrapper around <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), and can be used to drop privileges in the same way as <code><a href="/docs/linux/man/8-setuidgid/">setuidgid</a></code>(8) from <code>daemontools</code>, <code><a href="/docs/linux/man/8-chpst/">chpst</a></code>(8) from <code>runit</code>, or similar tools shipped by other service managers.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;clear-groups</code></p>
<dl>
<dt>
<dd> Clear supplementary groups.</dl>
<p> <code>-d</code>, <code>&#8211;dump</code></p>
<dl>
<dt>
<dd> Dump the current privilege state. This option can be specified more than once to show extra, mostly useless, information. Incompatible with all other options.</dl>
<p> <code>&#8211;groups</code> <i>group</i>&#8230;</p>
<dl>
<dt>
<dd> Set supplementary groups. The argument is a comma-separated list of GIDs or names.</dl>
<p> <code>&#8211;inh-caps</code> (<code>+</code>|<code>&#8211;</code>)<i>cap</i>&#8230;, <code>&#8211;ambient-caps</code> (<code>+</code>|<code>&#8211;</code>)<i>cap</i>&#8230;, <code>&#8211;bounding-set</code> (<code>+</code>|<code>&#8211;</code>)<i>cap</i>&#8230;</p>
<dl>
<dt>
<dd> Set the inheritable capabilities, ambient capabilities or the capability bounding set. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7). The argument is a comma-separated list of <code>+</code><i>cap</i> and <code>&#8211;</code><i>cap</i> entries, which add or remove an entry respectively. <i>cap</i> can either be a human-readable name as seen in <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) without the <i>cap_</i> prefix or of the format <code>cap_N</code>, where <i>N</i> is the internal capability index used by Linux. <code>+all</code> and <code>-all</code> can be used to add or remove all caps. </p>
<p> The set of capabilities starts out as the current inheritable set for <code>&#8211;inh-caps</code>, the current ambient set for <code>&#8211;ambient-caps</code> and the current bounding set for <code>&#8211;bounding-set</code>. </p>
<p> Note the following restrictions (detailed in <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)) regarding modifications to these capability sets: </p>
<dl>
<dt>
<dd> &bull; A capability can be added to the inheritable set only if it is currently present in the bounding set.</dl>
<dl>
<dt>
<dd> &bull; A capability can be added to the ambient set only if it is currently present in both the permitted and inheritable sets.</dl>
<dl>
<dt>
<dd> &bull; Notwithstanding the syntax offered by <code>setpriv</code>, the kernel does not permit capabilities to be added to the bounding set.</dl>
</dl>
<p> If you drop a capability from the bounding set without also dropping it from the inheritable set, you are likely to become confused. Do not do that. </p>
<p> <code>&#8211;keep-groups</code></p>
<dl>
<dt>
<dd> Preserve supplementary groups. Only useful in conjunction with <code>&#8211;rgid</code>, <code>&#8211;egid</code>, or <code>&#8211;regid</code>.</dl>
<p> <code>&#8211;init-groups</code></p>
<dl>
<dt>
<dd> Initialize supplementary groups using initgroups3. Only useful in conjunction with <code>&#8211;ruid</code> or <code>&#8211;reuid</code>.</dl>
<p> <code>&#8211;list-caps</code></p>
<dl>
<dt>
<dd> List all known capabilities. This option must be specified alone.</dl>
<p> <code>&#8211;no-new-privs</code></p>
<dl>
<dt>
<dd> Set the <i>no_new_privs</i> bit. With this bit set, <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) will not grant new privileges. For example, the set-user-ID and set-group-ID bits as well as file capabilities will be disabled. (Executing binaries with these bits set will still work, but they will not gain privileges. Certain LSMs, especially AppArmor, may result in failures to execute certain programs.) This bit is inherited by child processes and cannot be unset. See <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) and <i>Documentation/prctl/no_new_privs.txt</i> in the Linux kernel source. </p>
<p> The <i>no_new_privs</i> bit is supported since Linux 3.5.</dl>
<p> <code>&#8211;rgid</code> <i>gid</i>, <code>&#8211;egid</code> <i>gid</i>, <code>&#8211;regid</code> <i>gid</i></p>
<dl>
<dt>
<dd> Set the real, effective, or both GIDs. The <i>gid</i> argument can be given as a textual group name. </p>
<p> For safety, you must specify one of <code>&#8211;clear-groups</code>, <code>&#8211;groups</code>, <code>&#8211;keep-groups</code>, or <code>&#8211;init-groups</code> if you set any primary <i>gid</i>.</dl>
<p> <code>&#8211;ruid</code> <i>uid</i>, <code>&#8211;euid</code> <i>uid</i>, <code>&#8211;reuid</code> <i>uid</i></p>
<dl>
<dt>
<dd> Set the real, effective, or both UIDs. The <i>uid</i> argument can be given as a textual login name. </p>
<p> Setting a <i>uid</i> or <i>gid</i> does not change capabilities, although the exec call at the end might change capabilities. This means that, if you are root, you probably want to do something like: </p>
<p> <code>setpriv &#8211;reuid=1000 &#8211;regid=1000 &#8211;inh-caps=-all</code></dl>
<p> <code>&#8211;securebits</code> (<code>+</code>|<code>&#8211;</code>)<i>securebit</i>&#8230;</p>
<dl>
<dt>
<dd> Set or clear securebits. The argument is a comma-separated list. The valid securebits are <i>noroot</i>, <i>noroot_locked</i>, <i>no_setuid_fixup</i>, <i>no_setuid_fixup_locked</i>, and <i>keep_caps_locked</i>. <i>keep_caps</i> is cleared by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) and is therefore not allowed.</dl>
<p> <code>&#8211;pdeathsig keep</code>|<code>clear</code>|<code>&lt;signal&gt;</code></p>
<dl>
<dt>
<dd> Keep, clear or set the parent death signal. Some LSMs, most notably SELinux and AppArmor, clear the signal when the process&#8217; credentials change. Using <code>&#8211;pdeathsig keep</code> will restore the parent death signal after changing credentials to remedy that situation.</dl>
<p> <code>&#8211;selinux-label</code> <i>label</i></p>
<dl>
<dt>
<dd> Request a particular SELinux transition (using a transition on exec, not dyntrans). This will fail and cause <code>setpriv</code> to abort if SELinux is not in use, and the transition may be ignored or cause <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) to fail at SELinux&#8217;s whim. (In particular, this is unlikely to work in conjunction with <i>no_new_privs</i>.) This is similar to <code><a href="/docs/linux/man/1-runcon/">runcon</a></code>(1).</dl>
<p> <code>&#8211;apparmor-profile</code> <i>profile</i></p>
<dl>
<dt>
<dd> Request a particular AppArmor profile (using a transition on exec). This will fail and cause <code>setpriv</code> to abort if AppArmor is not in use, and the transition may be ignored or cause <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) to fail at AppArmor&#8217;s whim.</dl>
<p> <code>&#8211;reset-env</code></p>
<dl>
<dt>
<dd> Clears all the environment variables except <code>TERM</code>; initializes the environment variables <code>HOME</code>, <code>SHELL</code>, <code>USER</code>, <code>LOGNAME</code> according to the user&#8217;s passwd entry; sets <code>PATH</code> to <i>/usr/local/bin:/bin:/usr/bin</i> for a regular user and to <i>/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin</i> for root. </p>
<p> The environment variable <code>PATH</code> may be different on systems where <i>/bin</i> and <i>/sbin</i> are merged into <i>/usr</i>. The environment variable <code>SHELL</code> defaults to <code>/bin/sh</code> if none is given in the user&#8217;s passwd entry.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>NOTES</h2>
<p> If applying any specified option fails, <i>program</i> will not be run and <code>setpriv</code> will return with exit status 127. </p>
<p> Be careful with this tool &#8212; it may have unexpected security consequences. For example, setting <i>no_new_privs</i> and then execing a program that is SELinux-confined (as this tool would do) may prevent the SELinux restrictions from taking effect.</p>
<h2>EXAMPLES</h2>
<p> If you&#8217;re looking for behavior similar to <code><a href="/docs/linux/man/1-su/">su</a></code>(1)/<code><a href="/docs/linux/man/1-runuser/">runuser</a></code>(1), or <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) (without the <code>-g</code> option), try something like: </p>
<p> <code>setpriv &#8211;reuid=1000 &#8211;regid=1000 &#8211;init-groups</code> </p>
<p> If you want to mimic daemontools&#8217; <code><a href="/docs/linux/man/8-setuid/">setuid</a></code>(8), try: </p>
<p> <code>setpriv &#8211;reuid=1000 &#8211;regid=1000 &#8211;clear-groups</code></p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-runuser/">runuser</a></code>(1), <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>setpriv</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
