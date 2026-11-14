---
title: "autofs(5)"
name: "autofs"
section: "5"
letter: "a"
url: "/docs/linux/man/5-autofs/"
description: "autofs – Format of the automounter maps"
---

<p>autofs &#8211; Format of the automounter maps</p>
<h2>Description</h2>
<p>The automounter maps are FILE, NIS, NISPLUS or LDAP maps referred to by the master map of the automounter (see <code><a href="/docs/linux/man/5-auto-master/">auto.master</a></code>(5)). These maps describe how file systems below the mount point of the map (given in the master map) are to be mounted. This page describes the <code>sun</code> map format; if another map format, other than <code>amd ,</code> is specified (e.g. <code>hesiod</code>), this documentation does not apply. </p>
<p> Indirect maps, except for the internal hosts map, can be changed on the fly and the automouter will recognize those changes on the next operation it performs on that map. Direct maps require a HUP signal be sent to the daemon to refresh their contents as does the master map.</p>
<h2>Sun Format</h2>
<p>This is a description of the text file format. Other methods of specifying these files may exist. All empty lines or lines beginning with # are ignored. The basic format of one line in such maps is: </p>
<p> <code>key&nbsp;<wbr></code>[<code>-options</code>]&nbsp;<wbr><code>location</code></p>
<dl>
<dt><code>key</code></p>
<dd>For indirect mounts this is the part of the path name between the mount point and the path into the filesystem when it is mounted. Usually you can think about the key as a sub-directory name below the autofs managed mount point. </p>
<p> For direct mounts this is the full path of each mount point. This map is always associated with the /- mount point in the master map.</p>
<dt><code>options</code></p>
<dd>Zero or more options may be given. Options can also be given in the <code>auto.master</code> file in which case both values are cumulative (this is a difference from SunOS). The options are a list of comma separated options as customary for the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command. </p>
<p> There are several special options</p>
<dl>
<dd>
<dl>
<dt><code>-fstype=</code></p>
<dd>is used to specify a filesystem type if the filesystem is not of the default NFS type. This option is processed by the automounter and not by the mount command.</p>
<dt><code>-strict</code></p>
<dd>is used to treat errors when mounting file systems as fatal. This is important when multiple file systems should be mounted (`multi-mounts&#8217;). If this option is given, no file system is mounted at all if at least one file system can&#8217;t be mounted.</p>
<dt><code>-use-weight-only</code></p>
<dd>is used to make the weight the sole factor in selecting a server when multiple servers are present in a map entry. and</p>
<dt><code>-no-use-weight-only</code></p>
<dd>can be used to negate the option if it is present in the master map entry for the map but is not wanted for the given mount.</dl>
</dl>
<dt><code>location</code></p>
<dd>The location specifies from where the file system is to be mounted. In the most cases this will be an NFS volume and the usual notation <i>host:pathname</i> is used to indicate the remote filesystem and path to be mounted. If the filesystem to be mounted begins with a / (such as local <i>/dev</i> entries or smbfs shares) a : needs to be prefixed (e.g. <i>:/dev/sda1</i>).</dl>
<h2>Example</h2>
<p>Indirect map:</p>
<dl>
<dd>
<pre>kernel -ro,soft,intr <a href="ftp://ftp.kernel.org">ftp.kernel.org</a>:/pub/linux
boot -fstype=ext2 :/dev/hda1
windoze -fstype=smbfs ://windoze/c
removable -fstype=ext2 :/dev/hdd
cd -fstype=iso9660,ro :/dev/hdc
floppy -fstype=auto :/dev/fd0
server -rw,hard,intr / -ro myserver.me.org:/ \
 /usr myserver.me.org:/usr \
 /home myserver.me.org:/home</pre>
</dl>
<p> In the first line we have a NFS remote mount of the kernel directory on <i><a href="ftp://ftp.kernel.org">ftp.kernel.org</a></i>. This is mounted read-only. The second line mounts an ext2 volume from a local ide drive. The third makes a share exported from a Windows machine available for automounting. The rest should be fairly self-explanatory. The last entry (the last three lines) is an example of a multi-map (see below). If you use the automounter for a filesystem without access permissions (like <code>vfat</code>), users usually can&#8217;t write on such a filesystem because it is mounted as user <code>root</code>. You can solve this problem by passing the option <i>gid=&lt;gid&gt;</i>, e.g. <i>gid=floppy</i>. The filesystem is then mounted as group <code>floppy</code> instead of <code>root</code>. Then you can add the users to this group, and they can write to the filesystem. Here&#8217;s an example entry for an autofs map:</p>
<dl>
<dd>
<pre>floppy-vfat -fstype=vfat,sync,gid=floppy,umask=002 :/dev/fd0</pre>
</dl>
<p> Direct map:</p>
<dl>
<dd>
<pre>/nfs/apps/mozilla bogus:/usr/local/moxill
/nfs/data/budgets tiger:/usr/local/budgets
/tst/sbin bogus:/usr/sbin</pre>
</dl>
<h2>Features</h2>
<h3>Map Key Substitution</h3>
<p>An &amp; character in the <code>location</code> is expanded to the value of the <code>key</code> field that matched the line (which probably only makes sense together with a wildcard key).</p>
<h3>Wildcard Key</h3>
<p>A map key of * denotes a wild-card entry. This entry is consulted if the specified key does not exist in the map. A typical wild-card entry looks like this: </p>
<dl>
<dd>
<pre>* server:/export/home/&amp;</pre>
</dl>
<p> The special character &#8216;&amp;&#8217; will be replaced by the provided key. So, in the example above, a lookup for the key &#8216;foo&#8217; would yield a mount of server:/export/home/foo.</p>
<h3>Variable Substitution</h3>
<p>The following special variables will be substituted in the location field of an automounter map entry if prefixed with $ as customary from shell scripts (curly braces can be used to separate the field name): </p>
<dl>
<dd>
<pre>ARCH Architecture (uname -m)
CPU Processor Type
HOST Hostname (uname -n)
OSNAME Operating System (uname -s)
OSREL Release of OS (uname -r)
OSVERS Version of OS (uname -v)</pre>
</dl>
<p> autofs provides additional variables that are set based on the user requesting the mount: </p>
<dl>
<dd>
<pre>USER The user login name
UID The user login ID
GROUP The user group name
GID The user group ID
HOME The user home directory
SHOST Short hostname (domain part removed if present)</pre>
</dl>
<p> If a program map is used these standard environment variables will have a prefix of &quot;AUTOFS_&quot; to prevent interpreted languages like python from being able to load and execute arbitray code from a user home directory. </p>
<p> Additional entries can be defined with the -Dvariable=Value map-option to <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8).</p>
<h3>Executable Maps</h3>
<p>A map can be marked as executable. A <code>program</code> map will be called with the key as an argument. It may return no lines of output if there&#8217;s an error, or one or more lines containing a map entry (with \ quoting line breaks). The map entry corresponds to what would normally follow a map key. </p>
<p> An executable map can return an error code to indicate the failure in addition to no output at all. All output sent to stderr is logged into the system logs.</p>
<h3>Multiple Mounts</h3>
<p>A <code>multi-mount map</code> can be used to name multiple filesystems to mount. It takes the form: </p>
<dl>
<dd>
<pre><code>key [ -options ] [[/] location [/relative-mount-point [ -options ] location...]...</code></pre>
</dl>
<p> This may extend over multiple lines, quoting the line-breaks with `\&#8217;. If present, the per-mountpoint mount-options are appended to the default mount-options. This behaviour may be overridden by the append_options configuration setting.</p>
<h3>Replicated Server</h3>
<p>A mount location can specify multiple hosts for a location, portentially with a different export path for the same file system. Historically these different locations are read-only and provide the same replicated file system. </p>
<dl>
<dd>
<pre>Multiple replicated hosts, same path:
&lt;path&gt; host1,host2,hostn:/path/path
Multiple hosts, some with same path, some with another
&lt;path&gt; host1,host2:/blah host3:/some/other/path
Multiple replicated hosts, different (potentially) paths:
&lt;path&gt; host1:/path/pathA host2:/path/pathB
Mutliple weighted, replicated hosts same path:
&lt;path&gt; <a href="//www.systutorials.com/docs/linux/man/5-host1/">host1</a>(5),<a href="//www.systutorials.com/docs/linux/man/6-host2/">host2</a>(6),<a href="//www.systutorials.com/docs/linux/man/1-host3/">host3</a>(1):/path/path
Multiple weighted, replicated hosts different (potentially) paths:
&lt;path&gt; <a href="//www.systutorials.com/docs/linux/man/3-host1/">host1</a>(3):/path/pathA <a href="//www.systutorials.com/docs/linux/man/5-host2/">host2</a>(5):/path/pathB
Anything else is questionable and unsupported, but these variations will also work:
&lt;path&gt; <a href="//www.systutorials.com/docs/linux/man/3-host1/">host1</a>(3),host:/blah</pre>
</dl>
<h2>Unsupported</h2>
<p>This version of the automounter supports direct maps stored in FILE, NIS, NISPLUS and LDAP only.</p>
<h2>Amd Format</h2>
<p>This is a description of the text file format. Other methods of specifying mount map entries may be required for different map sources. All empty lines or lines beginning with # are ignored. The basic format of one line in such maps is: </p>
<p> <code>key location-list</code></p>
<dl>
<dt><code>key</code></p>
<dd>A <code>key</code> is a path (or a single path component alone) that may end in the wildcard key, &quot;*&quot;, or the wildcard key alone and must not begin with the &quot;/&quot; character.</p>
<dt><code>location-list</code></p>
<dd>Following the <code>key</code> is a mount <code>location-list</code>.</p>
<dt>A <code>location-list</code> list has the following syntax:</p>
<dd>
<dt><code>location[&nbsp;<wbr>location[&nbsp;<wbr>&#8230;&nbsp;<wbr>]]&nbsp;<wbr>[|| location[&nbsp;<wbr>location[&nbsp;<wbr>&#8230;&nbsp;<wbr>]]</code></p>
<dd></dl>
<p> A mount <code>location-list</code> can use the cut operator, <code>||</code>, to specify locations that should be tried if none of the locations to the left of it where selected for a mount attempt. </p>
<p> A mount <code>location</code> consists of an optional colon seperated list of <code>selectors</code>, followed by a colon seperated list of <code>option:=value</code> pairs. </p>
<p> The <code>selectors</code> that may be used return a value or boolean result. Those that return a value may be to used with the comparison operators <code>==</code> and <code>!=</code> and those that return a boolean result may be negated with the <code>!</code>. </p>
<p> For a <code>location</code> to be selected for a mount attempt all of its <code>selectors</code> must evaluate to true. If a <code>location</code> is selected for a mount attempt and succeeds the lookup is completed and returns success. If the mount attempt fails the proceedure continues with the next <code>location</code> until they have all been tried. </p>
<p> In addition some <code>selectors</code> take no argumenets, some one argument and others optionally take two arguments. </p>
<p> The <code>selectors</code> that take no arguments are:</p>
<dl>
<dd>
<dl>
<dt><code>arch</code></p>
<dd>The machine architecture which, if not set in the confugration, is obtained using <a href="/docs/linux/man/2-uname/">uname</a>(2).</p>
<dt><code>karch</code></p>
<dd>The machine kernel architecture which, if not set in the confugration, is obtained using <a href="/docs/linux/man/2-uname/">uname</a>(2).</p>
<dt><code>os</code></p>
<dd>The operating system name, if not set in the confugration, is obtained using <a href="/docs/linux/man/2-uname/">uname</a>(2).</p>
<dt><code>osver</code></p>
<dd>The operating system version, if not set in the confugration, is obtained using <a href="/docs/linux/man/2-uname/">uname</a>(2).</p>
<dt><code>full_os</code></p>
<dd>The full operating system name, if not set in the confugration this selector has no value.</p>
<dt><code>vendor</code></p>
<dd>The operating system vendor name, if not set in the confugration this selector has the value &quot;unknown&quot;.</p>
<dt><code>byte</code></p>
<dd>The endianess of the hardware.</p>
<dt><code>cluster</code></p>
<dd>The name of the local cluster. It has a value only if it is set in the configuration.</p>
<dt><code>autodir</code></p>
<dd>The base path under which external mounts are done if they are needed. Most mounts are done in place but some can&#8217;t be and this is the base path under which those mounts will be done.</p>
<dt><code>domain</code></p>
<dd>The local domain name. It is set to the value of the configuration option <code>sub_domain</code>. If sub_domain is not given in the configuration it is set to the domain part of the local host name, as given by <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2).</p>
<dt><code>host</code></p>
<dd>The local host name, without the domain part, as given by <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2).</p>
<dt><code>hostd</code></p>
<dd>The full host name. If <code>sub_domain</code> is given in the configuration this is set to the contatenation of <code>host</code> and <code>sub_domain</code> deperated by a <code>.</code>. If <code>sub_domain</code> is not set in the configuration the value of <code>domain</code> is used instead of <code>sub_domain</code>.</p>
<dt><code>uid</code></p>
<dd>The numeric value of the uid of the user that first requested the mount. Note this is usual the same as that used by amd but can be different within autofs.</p>
<dt><code>gid</code></p>
<dd>The numeric value of the gid of the user that first requested the mount. Note this is usual the same as that used by amd but can be different within autofs.</p>
<dt><code>key</code></p>
<dd>The string value of the key being looked up.</p>
<dt><code>map</code></p>
<dd>The string value of the map name used to lookup <code>key</code>s.</p>
<dt><code>path</code></p>
<dd>The string value of the full path to the mount being requested.</p>
<dt><code>dollar</code></p>
<dd>Evaluates to the string &quot;$&quot;.</dl>
</dl>
<dl>
<dt>The <code>selectors</code> that take one argument are:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>in_network(network) , network(network) , netnumber(network) , wire(network)</code></p>
<dd>These <code>selectors</code> are all the same. <code>in_network()</code> is the preferred usage. The <code>network</code> argument is an address (which may include a subnet mask) or network name. The function compares <code>network</code> against each interface and returns true if <code>network</code> belongs to the network the interface is connected to.</p>
<dt><code>xhost(hostname)</code></p>
<dd>The <code>xhost()</code> selector compares <code>hostname</code> to the <code>${host}</code> and if it doesn&#8217;t match it attempts to lookup the cannonical name of <code>hostname</code> and compares it to {host} as well.</p>
<dt><code>exists(filename)</code></p>
<dd>Returns true if <code>filename</code> exits as determined by <a href="/docs/linux/man/2-lstat/">lstat</a>(2).</p>
<dt><code>true()</code></p>
<dd>Evaluates to true, the argument is ignored and may be empty.</p>
<dt><code>false()</code></p>
<dd>Evaluates to false, the argument is ignored and may be empty.</dl>
</dl>
<dt>The <code>selectors</code> that take up to two arguments are:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>netgrp(netgroup[,hostname])</code></p>
<dd>The <code>netgrp()</code> selector returns true if hostname is a member of the netgroup <code>netgroup</code>. If <code>hostname</code> is not given <code>${host}</code> is used for the comparison.</p>
<dt><code>netgrpd(netgroup[,hostname])</code></p>
<dd>The <code>netgrpd()i</code> selector behaves the same as <code>netgrp()</code> except that if <code>hostname</code> is not given <code>${hostd}</code>, the fully qualified hostname, is used instead of <code>${host}</code>.</dl>
</dl>
<dt>The <code>options</code> that may be used are:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>type</code></p>
<dd>This is the mount filesystem <code>type</code>. It can have a value of <code>auto</code>, <code>link</code>, <code>linkx</code>, <code>host</code>, <code>lofs</code>, <code>ext2-4</code>, <code>xfs</code>, <code>nfs</code>, <code>nfsl</code> or <code>cdfs</code>. Other types that are not yet implemented or are not available iin autofs are <code>nfsx</code>, <code>lustre</code>, <code>jfs</code>, <code>program</code>, <code>cachefs</code> and <code>direct</code>.</p>
<dt><code>maptype</code></p>
<dd>The <code>maptype</code> option specifies the type of the map source and can have a value of <code>file</code>, <code>nis</code>, <code>nisplus</code>, <code>exec</code>, <code>ldap</code> or <code>hesiod</code>. Map sources either not yet implemented or not available in autofs are <code>sss</code>, <code>ndbm</code>, <code>passwd</code> and <code>union</code>.</p>
<dt><code>fs</code></p>
<dd>The option <code>fs</code> is used to specify the local filesystem. The meaning of this option (and whether or not it is used) is dependent on the mount filesystem <code>type</code>.</p>
<dt><code>rhost</code></p>
<dd>The remote host name for network mount requests.</p>
<dt><code>rfs</code></p>
<dd>The remote host filesystem path for network mount requests.</p>
<dt><code>dev</code></p>
<dd>Must resolve to the device file for local device mount requests.</p>
<dt><code>sublink</code></p>
<dd>The <code>sublink</code> option is used to specify a subdirectory within the mount location to which this entry will point.</p>
<dt><code>pref</code></p>
<dd>The <code>pref</code> option is used to specify a prefix that is prepended to the lookup key before looking up the map entry key.</p>
<dt><code>opts</code></p>
<dd>The <code>opts</code> option is used to specify mount options to be used for the mount. If a &quot;<code>&#8211;</code>&quot; is given it is ignored. Options that may be used are dependend on the mount filesystem.</p>
<dt><code>addopts</code></p>
<dd>The <code>addopts</code> option is used to specify additional mount options used in addition to the default mount options for the mount location.</p>
<dt><code>remopts</code></p>
<dd>The <code>addopts</code> option is used to specify mount options used instead the options given in <code>opts</code> when the mount location is on a remote retwork.</dl>
</dl>
<dt>A number of <code>options</code> aren&#8217;t available or aren&#8217;t yet implemented</p>
<dd>within autofs, these are:</p>
<dl>
<dd>
<dl>
<dt><code>cache</code></p>
<dd>The <code>cache option</code> isn&#8217;t used by autofs. The map entry cache is continually updated and stale entries cleaned on re-load when map changes are detected so these configuration entries are not used. The <code>regex</code> map key matching is not implemented and may not be due to the potential overhead of the full map scans needed on every key lookup.</p>
<dt><code>cachedir</code></p>
<dd>The <code>cachefs</code> filesystem is not available on Linux, a different implementation is used for caching network mounted file systems.</p>
<dt><code>mount , unmount , umount</code></p>
<dd>These <code>options</code> are used by the amd <code>program</code> mount type which is not yet implemented.</p>
<dt><code>delay</code></p>
<dd>This <code>option</code> is not used by the autofs implementation and is ignored.</dl>
</dl>
</dl>
<h2>Features</h2>
<h3>Key Matching</h3>
<p>The amd parser key matching is unusual. </p>
<p> The key string to be looked up is constructed by prepending the prefix, if there is one. </p>
<p> The resulting relative path string is matched by first trying the sting itself. If no match is found the last component of the key string is replaced with the wilcard match cahracter (&quot;*&quot;) and a wildcard match is attemted. This process continues until a match is found or until the last match, against the wilcard match key alone, fails to match a map entry and the key lookup fails.</p>
<h3>Macro Usage</h3>
<p>Macros are used a lot in the autofs amd implementation. </p>
<p> Many of the option values are set as macro variables corresponding to the option name during the map entry parse. So they may be used in subsequent option values. Beware though, the order in which option values is not necessarily left to right so you may get unexpected results.</p>
<h2>Example</h2>
<p>Example NFS mount map: </p>
<p> Assuming we have the autofs master map entry: </p>
<dl>
<dd>
<pre>/test file,amd:/etc/amd.test</pre>
</dl>
<p> And the following map in /etc/amd.test: </p>
<dl>
<dd>
<pre>/defaults type:=nfs;rhost:=bilbo
apps rfs:=/autofs
util rhost:=zeus;rfs:=/work/util
local rfs:=/shared;sublink:=local</pre>
</dl>
<p> In the first line we have an NFS remote mount of the exported directory /autofs from host bilbo which would be mounted on /test/apps. Next another nfs mount for the exported directory /work/util from host zeus. This would be mounted on /test/util. </p>
<p> Finally we have an example of the use of the <code>sublink</code> option. In this case the filesystem bilbo:/shared would be mounted on a path external the automount directory (under the direcory given by configuration option auto_dir) and the path /test/local either symlinked or bind mounted (depending on the setting autofs_use_lofs) to the &quot;local&quot; subdirectory of the external mount.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-automount/">automount</a></code>(8), <code><a href="/docs/linux/man/5-auto-master/">auto.master</a></code>(5), <code><a href="/docs/linux/man/8-autofs/">autofs</a></code>(8), <code><a href="/docs/linux/man/5-autofs-conf/">autofs.conf</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). <code><a href="/docs/linux/man/5-autofs_ldap_auth-conf/">autofs_ldap_auth.conf</a></code>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Christoph Lameter &lt;chris [at] waterf.org&gt;, for the Debian GNU/Linux system. Edited by H. Peter Avian &lt;hpa [at] transmeta.com&gt;, Jeremy Fitzhardinge &lt;jeremy [at] goop.org&gt; and Ian Kent &lt;raven [at] themaw.net&gt;.</p>
