---
title: "capsh(1)"
name: "capsh"
section: "1"
letter: "c"
url: "/docs/linux/man/1-capsh/"
description: "capsh – capability shell wrapper"
---

<h2 class="name">NAME</h2>
<p> capsh &#8211; capability shell wrapper </p>
<h2>SYNOPSIS</h2>
<p> <code>capsh</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Linux capability support and use can be explored and constrained with this tool. This tool provides a handy wrapper for certain types of capability testing and environment creation. It also provides some debugging features useful for summarizing capability state.</p>
<h2>OPTIONS</h2>
<p> <code>capsh</code> takes a number of optional arguments, acting on them in the order they are provided. They are as follows:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display the list of commands supported by <code>capsh</code>.</p>
<dt><code>&#8211;print</code></p>
<dd> Display prevailing capability and related state.</p>
<dt><code>&#8212;</code><i> [args]</i></p>
<dd> Execute <code>/bin/bash</code> with trailing arguments. Note, you can use <code>-c &#8216;command to execute&#8217;</code> for specific commands.</p>
<dt><code>==</code></p>
<dd> Execute <code>capsh</code> again with the remaining arguments. Useful for testing <code>exec</code>() behavior.</p>
<dt><code>&#8211;caps=</code><i>cap-set</i></p>
<dd> Set the prevailing process capabilities to those specified by <i>cap-set</i>. Where <i>cap-set</i> is a text-representation of capability state as per <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3).</p>
<dt><code>&#8211;drop=</code><i>cap-list</i></p>
<dd> Remove the listed capabilities from the prevailing bounding set. The capabilities are a comma-separated list of capabilities as recognized by the <code><a href="/docs/linux/man/3-cap_from_name/">cap_from_name</a></code>(3) function. Use of this feature requires that <code>capsh</code> is operating with <code>CAP_SETPCAP</code> in its effective set.</p>
<dt><code>&#8211;inh=</code><i>cap-list</i></p>
<dd> Set the inheritable set of capabilities for the current process to equal those provided in the comma separated list. For this action to succeed, the prevailing process should already have each of these capabilities in the union of the current inheritable and permitted capability sets, or <code>capsh</code> should be operating with <code>CAP_SETPCAP</code> in its effective set.</p>
<dt><code>&#8211;user=</code><i>username</i></p>
<dd> Assume the identity of the named user. That is, look up the user&#8217;s UID and GID with <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3) and their group memberships with <code><a href="/docs/linux/man/3-getgrouplist/">getgrouplist</a></code>(3) and set them all using <code><a href="/docs/linux/man/3-cap_setuid/">cap_setuid</a></code>(3) and <code><a href="/docs/linux/man/3-cap_setgroups/">cap_setgroups</a></code>(3). Following this command, the effective capabilities will be cleared, but the permitted set will not be, so the running program is still privileged.</p>
<dt><code>&#8211;modes</code></p>
<dd> Lists all of the libcap modes supported by <code>&#8211;mode</code>.</p>
<dt><code>&#8211;mode=</code>&lt;mode&gt;</p>
<dd> Force the program into a <code><a href="/docs/linux/man/3-cap_set_mode/">cap_set_mode</a></code>(3) security mode. This is a set of securebits and prevailing capability arrangement recommended for its pre-determined security stance.</p>
<dt><code>&#8211;inmode=</code>&lt;mode&gt;</p>
<dd> Confirm that the prevailing mode is that specified in <i>&lt;mode&gt;</i>, or exit with a status 1.</p>
<dt><code>&#8211;uid=</code><i>id</i></p>
<dd> Force all UID values to equal <i>id</i> using the <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2) system call. This argument may require explicit preparation of the effective set.</p>
<dt><code>&#8211;cap-uid=</code>&lt;uid&gt;</p>
<dd> use the <code><a href="/docs/linux/man/3-cap_setuid/">cap_setuid</a></code>(3) function to set the UID of the current process. This performs all preparations for setting the UID without dropping capabilities in the process. Following this command the prevailing effective capabilities will be lowered.</p>
<dt><code>&#8211;is-uid=</code><i>&lt;id&gt;</i></p>
<dd> Exit with status 1 unless the current UID equals <i>&lt;id&gt;</i>.</p>
<dt><code>&#8211;gid=</code><i>&lt;id&gt;</i></p>
<dd> Force all GID values to equal <i>id</i> using the <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2) system call.</p>
<dt><code>&#8211;is-gid=</code><i>&lt;id&gt;</i></p>
<dd> Exit with status 1 unless the current GIQ equals <i>&lt;id&gt;</i>.</p>
<dt><code>&#8211;groups=</code><i>&lt;gid-list&gt;</i></p>
<dd> Set the supplementary groups to the numerical list provided. The groups are set with the <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) system call. See <code>&#8211;user</code> for a more convenient way of doing this.</p>
<dt><code>&#8211;keep=</code><i>&lt;0|1&gt;</i></p>
<dd> In a non-pure capability mode, the kernel provides liberal privilege to the super-user. However, it is normally the case that when the super-user changes UID to some lesser user, then capabilities are dropped. For these situations, the kernel can permit the process to retain its capabilities after a <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2) system call. This feature is known as <i>keep-caps</i> support. The way to activate it using this program is with this argument. Setting the value to 1 will cause <i>keep-caps</i> to be active. Setting it to 0 will cause keep-caps to deactivate for the current process. In all cases, <i>keep-caps</i> is deactivated when an <code>exec</code>() is performed. See <code>&#8211;secbits</code> for ways to disable this feature.</p>
<dt><code>&#8211;secbits=</code><i>N</i></p>
<dd> Set the security-bits for the program. This is done using the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_SECUREBITS</code> operation. The list of supported bits and their meaning can be found in the <code>&lt;sys/secbits.h&gt;</code> header file. The program will list these bits via the <code>&#8211;print</code> command. The argument is expressed as a numeric bitmask, in any of the formats permitted by <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3).</p>
<dt><code>&#8211;chroot=</code><i>path</i></p>
<dd> Execute the <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) system call with the new root-directory (/) equal to <i>path</i>. This operation requires <code>CAP_SYS_CHROOT</code> to be in effect.</p>
<dt><code>&#8211;forkfor=</code><i>sec</i></p>
<dd> This command causes the program to fork a child process for so many seconds. The child will sleep that long and then exit with status 0. The purpose of this command is to support exploring the way processes are killable in the face of capability changes. See the <code>&#8211;killit</code> command. Only one fork can be active at a time.</p>
<dt><code>&#8211;killit=</code><i>sig</i></p>
<dd> This commands causes a <code>&#8211;forkfor</code> child to be <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)d with the specified signal. The command then waits for the child to exit. If the exit status does not match the signal being used to kill it, the <code>capsh</code> program exits with status 1.</p>
<dt><code>&#8211;decode=</code><i>N</i></p>
<dd> This is a convenience feature. If you look at <code>/proc/1/status</code> there are some capability related fields of the following form: </p>
<pre>
CapInh: 0000000000000000
CapPrm: 0000003fffffffff
CapEff: 0000003fffffffff
CapBnd: 0000003fffffffff
CapAmb: 0000000000000000
</pre>
<p> This option provides a quick way to decode a capability vector represented in this hexadecimal form. Here&#8217;s an example that decodes the two lowest capability bits:</p>
<dt>
<dd>
<pre>
$ <code>capsh --decode=3</code>
0x0000000000000003=cap_chown,cap_dac_override
</pre>
<dt><code>&#8211;supports=</code><i>xxx</i></p>
<dd> As the kernel evolves, more capabilities are added. This option can be used to verify the existence of a capability on the system. For example, <code>&#8211;supports=</code><i>cap_syslog</i> will cause <code>capsh</code> to promptly exit with a status of 1 when run on kernel 2.6.27. However, when run on kernel 2.6.38 it will silently succeed.</p>
<dt><code>&#8211;has-p=</code><i>xxx</i></p>
<dd> Exit with status 1 unless the <i>permitted</i> vector has capability <code>xxx</code> raised.</p>
<dt><code>&#8211;has-ambient</code></p>
<dd> Performs a check to see if the running kernel supports ambient capabilities. If not, <code>capsh</code> exits with status 1.</p>
<dt><code>&#8211;has-a=</code><i>xxx</i></p>
<dd> Exit with status 1 unless the <i>ambient</i> vector has capability <code>xxx</code> raised.</p>
<dt><code>&#8211;addamb=</code><i>xxx</i></p>
<dd> Adds the specified ambient capability to the running process.</p>
<dt><code>&#8211;delamb=</code><i>xxx</i></p>
<dd> Removes the specified ambient capability from the running process.</p>
<dt><code>&#8211;noamb</code></p>
<dd> Drops all ambient capabilities from the running process.</dl>
<h2>EXIT STATUS</h2>
<p> Following successful execution, <code>capsh</code> exits with status 0. Following an error, <code>capsh</code> immediately exits with status 1.</p>
<h2>AUTHOR</h2>
<p> Written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs via:</p>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.kernel.org/buglist.cgi?component=libcap">https://bugzilla.kernel.org/buglist.cgi?component=libcap</a>&amp;list_id=1047723&amp;product=Tools&amp;resolution=&#8212;</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3), <code><a href="/docs/linux/man/8-getcap/">getcap</a></code>(8), <code><a href="/docs/linux/man/8-setcap/">setcap</a></code>(8) and <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7). </p>
<h2>Index</h2>
