---
title: "systemd-sysusers(8)"
name: "systemd-sysusers"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-sysusers/"
description: "systemd-sysusers, systemd-sysusers.service – Allocate system users and groups"
---

<p>systemd-sysusers, systemd-sysusers.service &#8211; Allocate system users and groups</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>systemd-sysusers</code> [OPTIONS&#8230;] [<i>CONFIGFILE</i>&#8230;]</dl>
<dd>systemd-sysusers.service</p>
<h2>Description</h2>
<p><code>systemd-sysusers</code> creates system users and groups, based on the file format and location specified in <code><a href="/docs/linux/man/5-sysusers-d/">sysusers.d</a></code>(5). </p>
<p> If invoked with no arguments, it applies all directives from all files found in the directories specified by <code><a href="/docs/linux/man/5-sysusers-d/">sysusers.d</a></code>(5). When invoked with positional arguments, if option <code>&#8211;replace=</code><i>PATH</i> is specified, arguments specified on the command line are used instead of the configuration file <i>PATH</i>. Otherwise, just the configuration specified by the command line arguments is executed. The string &quot;-&quot; may be specified instead of a filename to instruct <code>systemd-sysusers</code> to read the configuration from standard input. If only the basename of a file is specified, all configuration directories are searched for a matching file and the file found that has the highest priority is executed.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;root=</code><i>root</i></p>
<dl>
<dd>Takes a directory path as an argument. All paths will be prefixed with the given alternate <i>root</i> path, including config search paths.</dl>
<p> <code>&#8211;image=</code><i>image</i></p>
<dl>
<dd>Takes a path to a disk image file or block device node. If specified all operations are applied to file system in the indicated disk image. This is similar to <code>&#8211;root=</code> but operates on file systems stored in disk images or block devices. The disk image should either contain just a file system or a set of file systems within a GPT partition table, following the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[1]</font>. For further information on supported disk images, see <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1)&#8217;s switch of the same name.</dl>
<p> <code>&#8211;replace=</code><i>PATH</i></p>
<dl>
<dd>When this option is given, one ore more positional arguments must be specified. All configuration files found in the directories listed in <code><a href="/docs/linux/man/5-sysusers-d/">sysusers.d</a></code>(5) will be read, and the configuration given on the command line will be handled instead of and with the same priority as the configuration file <i>PATH</i>. </p>
<p> This option is intended to be used when package installation scripts are running and files belonging to that package are not yet available on disk, so their contents must be given on the command line, but the admin configuration might already exist and should be given higher priority. </p>
<p> <code>Example 1. RPM installation script for radvd</code> </p>
<dl>
<dd>
<pre>echo 'u radvd - &quot;radvd daemon&quot;' | \
 systemd-sysusers --replace=/usr/lib/sysusers.d/radvd.conf -</pre>
</dl>
<p> This will create the radvd user as if /usr/lib/sysusers.d/radvd.conf was already on disk. An admin might override the configuration specified on the command line by placing /etc/sysusers.d/radvd.conf or even /etc/sysusers.d/00-overrides.conf. </p>
<p> Note that this is the expanded form, and when used in a package, this would be written using a macro with &quot;radvd&quot; and a file containing the configuration line as arguments.</dl>
<p> <code>&#8211;inline</code></p>
<dl>
<dd>Treat each positional argument as a separate configuration line instead of a file name.</dl>
<p> <code>&#8211;cat-config</code></p>
<dl>
<dd>Copy the contents of config files to standard output. Before each file, the filename is printed as a comment.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dd>Do not pipe output into a pager.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Credentials</h2>
<p><code>systemd-sysusers</code> supports the service credentials logic as implemented by <i>LoadCredential=</i>/<i>SetCredential=</i> (see <code><a href="/docs/linux/man/1-systemd-exec/">systemd.exec</a></code>(1) for details). The following credentials are used when passed in: </p>
<p> &quot;passwd.hashed-password.<i>user</i>&quot;</p>
<dl>
<dd>A UNIX hashed password string to use for the specified user, when creating an entry for it. This is particularly useful for the &quot;root&quot; user as it allows provisioning the default root password to use via a unit file drop-in or from a container manager passing in this credential. Note that setting this credential has no effect if the specified user account already exists. This credential is hence primarily useful in first boot scenarios or systems that are fully stateless and come up with an empty /etc/ on every boot.</dl>
<p> &quot;passwd.plaintext-password.<i>user</i>&quot;</p>
<dl>
<dd>Similar to &quot;passwd.hashed-password.<i>user</i>&quot; but expect a literal, plaintext password, which is then automatically hashed before used for the user account. If both the hashed and the plaintext credential are specified for the same user the former takes precedence. It&#8217;s generally recommended to specify the hashed version; however in test environments with weaker requirements on security it might be easier to pass passwords in plaintext instead.</dl>
<p> &quot;passwd.shell.<i>user</i>&quot;</p>
<dl>
<dd>Specifies the shell binary to use for the specified account when creating it.</dl>
<p> Note that by default the systemd-sysusers.service unit file is set up to inherit the &quot;passwd.hashed-password.root&quot;, &quot;passwd.plaintext-password.root&quot; and &quot;passwd.shell.root&quot; credentials from the service manager. Thus, when invoking a container with an unpopulated /etc/ for the first time it is possible to configure the root user&#8217;s password to be &quot;systemd&quot; like this: </p>
<dl>
<dd>
<pre># systemd-nspawn --image=... --set-credential=password.hashed-password.root:'$y$j9T$yAuRJu1o5HioZAGDYPU5d.$F64ni6J2y2nNQve90M/p0ZP0ECP/qqzipNyaY9fjGpC' ...</pre>
</dl>
<p> Note again that the data specified in these credentials is consulted only when creating an account for the first time, it may not be used for changing the password or shell of an account that already exists. </p>
<p> Use <code><a href="/docs/linux/man/1-mkpasswd/">mkpasswd</a></code>(1) for generating UNIX password hashes from the command line.</p>
<h2>Exit Status</h2>
<p>On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-sysusers-d/">sysusers.d</a></code>(5), m[blue]<code>Users, Groups, UIDs and GIDs on systemd systems</code>m[]<font SIZE="-2">[2]</font>, <code><a href="/docs/linux/man/1-systemd-exec/">systemd.exec</a></code>(1), <code><a href="/docs/linux/man/1-mkpasswd/">mkpasswd</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Discoverable Partitions Specification</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/DISCOVERABLE_PARTITIONS">https://systemd.io/DISCOVERABLE_PARTITIONS</a></dl>
<dt> 2.</p>
<dd>Users, Groups, UIDs and GIDs on systemd systems</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/UIDS-GIDS">https://systemd.io/UIDS-GIDS</a></dl>
