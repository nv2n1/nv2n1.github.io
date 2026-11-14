---
title: "snap-confine(8)"
name: "snap-confine"
section: "8"
letter: "s"
url: "/docs/linux/man/8-snap-confine/"
description: "snap-confine – internal tool for confining snappy applications"
---

<p>snap-confine &#8211; internal tool for confining snappy applications</p>
<h2>Synopsis</h2>
<p>snap-confine [&#8211;classic] [&#8211;base BASE] SECURITY_TAG COMMAND [&#8230;ARGUMENTS]</p>
<h2>Description</h2>
<p>The <i>snap-confine</i> is a program used internally by <i>snapd</i> to construct the execution environment for snap applications.</p>
<h2>Options</h2>
<p>The <i>snap-confine</i> program accepts two options: <i>&#8211;classic</i> requests the so-called _classic_ _confinement_ in which applications are not confined at all (like in classic systems, hence the name). This disables the use of a dedicated, per-snap mount namespace. The <i>snapd</i> service generates permissive apparmor and seccomp profiles that allow everything. </p>
<p> <i>&#8211;base BASE</i> directs snap-confine to use the given base snap as the root filesystem. If omitted it defaults to the <i>core</i> snap. This is derived from snap meta-data by <i>snapd</i> when starting the application process.</p>
<h2>Features</h2>
<h3>Apparmor profiles</h3>
<p><i>snap-confine</i> switches to the apparmor profile <i>$SECURITY_TAG</i>. The profile is <code>mandatory</code> and <i>snap-confine</i> will refuse to run without it. </p>
<p> The profile has to be loaded into the kernel prior to using <i>snap-confine</i>. Typically this is arranged for by <i>snapd</i>. The profile contains rich description of what the application process is allowed to do, this includes system calls, file paths, access patterns, linux capabilities, etc. The apparmor profile can also do extensive dbus mediation. Refer to apparmor documentation for more details.</p>
<h3>Seccomp profiles</h3>
<p><i>snap-confine</i> looks for the <i>/var/lib/snapd/seccomp/bpf/$SECURITY_TAG.bin</i> file. This file is <code>mandatory</code> and <i>snap-confine</i> will refuse to run without it. This file contains the seccomp bpf binary program that is loaded into the kernel by snap-confine. </p>
<p> The file is generated with the <i>/usr/lib/snapd/snap-seccomp</i> compiler from the <i>$SECURITY_TAG.src</i> file that uses a custom syntax that describes the set of allowed system calls and optionally their arguments. The profile is then used to confine the started application. </p>
<p> As a security precaution disallowed system calls cause the started application executable to be killed by the kernel. In the future this restriction may be lifted to return <i>EPERM</i> instead.</p>
<h3>Mount profiles</h3>
<p><i>snap-confine</i> uses a helper process, <i>snap-update-ns</i>, to apply the mount namespace profile to freshly constructed mount namespace. That tool looks for the <i>/var/lib/snapd/mount/snap.$SNAP_NAME.fstab</i> file. If present it is read, parsed and treated like a mostly-typical <i><a href="/docs/linux/man/5-fstab/">fstab</a>(5)</i> file. The mount directives listed there are executed in order. All directives must succeed as any failure will abort execution. </p>
<p> By default all mount entries start with the following flags: <i>bind</i>, <i>ro</i>, <i>nodev</i>, <i>nosuid</i>. Some of those flags can be reversed by an appropriate option (e.g. <i>rw</i> can cause the mount point to be writable). </p>
<p> Certain additional features are enabled and conveyed through the use of mount options prefixed with <i>x-snapd-</i>. </p>
<p> As a security precaution only <i>bind</i> mounts are supported at this time.</p>
<h3>Sharing of the mount namespace</h3>
<p>As of version 1.0.41 all the applications from the same snap will share the same mount namespace. Applications from different snaps continue to use separate mount namespaces.</p>
<h2>Environment</h2>
<p><i>snap-confine</i> responds to the following environment variables</p>
<dl>
<dt><i>SNAP_CONFINE_DEBUG</i>:</p>
<dd>When defined the program will print additional diagnostic information about the actions being performed. All the output goes to stderr. </p>
<p> The following variables are only used when <i>snap-confine</i> is not setuid root. This is only applicable when testing the program itself.</p>
<dt><i>SNAPPY_LAUNCHER_INSIDE_TESTS</i>:</p>
<dd>Internal variable that should not be relied upon.</p>
<dt><i>SNAPPY_LAUNCHER_SECCOMP_PROFILE_DIR</i>:</p>
<dd>Internal variable that should not be relied upon.</p>
<dt><i>SNAP_USER_DATA</i>:</p>
<dd>Full path to the directory like /home/$LOGNAME/snap/$SNAP_NAME/$SNAP_REVISION. </p>
<p> This directory is created by snap-confine on startup. This is a temporary feature that will be merged into snapd&#8217;s snap-run command. The set of directories that can be created is confined with apparmor.</dl>
<h2>Files</h2>
<p><i>snap-confine</i> and <i>snap-update-ns</i> use the following files: </p>
<p> <i>/var/lib/snapd/mount/snap.*.fstab</i>: Description of the mount profile. </p>
<p> <i>/var/lib/snapd/seccomp/bpf/*.src</i>: Input for the /usr/lib/snapd/snap-seccomp profile compiler. </p>
<p> <i>/var/lib/snapd/seccomp/bpf/*.bin</i>: Compiled seccomp bpf profile programs. </p>
<p> <i>/run/snapd/ns/</i>: Directory used to keep shared mount namespaces. </p>
<p> <i>snap-confine</i> internally converts this directory to a private bind mount. Semantically the behavior is identical to the following mount commands: </p>
<p> mount &#8211;bind /run/snapd/ns /run/snapd/ns mount &#8211;make-private /run/snapd/ns </p>
<p> <i>/run/snapd/ns/.lock</i>: A <i><a href="/docs/linux/man/2-flock/">flock</a>(2)</i>-based lock file acquired to create and convert <i>/run/snapd/ns/</i> to a private bind mount. </p>
<p> <i>/run/snapd/ns/$SNAP_NAME.lock</i>: A <i><a href="/docs/linux/man/2-flock/">flock</a>(2)</i>-based lock file acquired to create or join the mount namespace represented as <i>/run/snaps/ns/$SNAP_NAME.mnt</i>. </p>
<p> <i>/run/snapd/ns/$SNAP_NAME.mnt</i>: This file can be either:</p>
<dl>
<dt>&bull;</p>
<dd>An empty file that may be seen before the mount namespace is preserved or when the mount namespace is unmounted.</p>
<dt>&bull;</p>
<dd>A file belonging to the <i>nsfs</i> file system, representing a fully populated mount namespace of a given snap. The file is bind mounted from <i>/proc/self/ns/mnt</i> from the first process in any snap. </p>
<p> <i>/proc/self/mountinfo</i>: This file is read to decide if <i>/run/snapd/ns/</i> needs to be created and converted to a private bind mount, as described above. </p>
<p> Note that the apparmor profile is external to <i>snap-confine</i> and is loaded directly into the kernel. The actual apparmor profile is managed by <i>snapd</i>.</dl>
<h2>Bugs</h2>
<p>Please report all bugs with <i><a rel="nofollow" href="https://bugs.launchpad.net/snapd/+filebug">https://bugs.launchpad.net/snapd/+filebug</a></i></p>
<h2>Author</h2>
<p>zygmunt.krynicki [at] canonical.com</p>
<h2>Copyright</h2>
<p>Canonical Ltd.</p>
