---
title: "rquotad(8)"
name: "rquotad"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rquotad/"
description: "rquotad, rpc.rquotad – remote quota server"
---

<p>rquotad, rpc.rquotad &#8211; remote quota server</p>
<h2>Synopsis</h2>
<p><code>rpc.rquotad</code> [ <code>-sSFI</code> ] [ <code>-p </code><i>port</i> ]</p>
<h2>Description</h2>
<p><code>rquotad</code> is an <code><a href="/docs/linux/man/3-rpc/">rpc</a></code>(3) server which returns quotas for a user of a local filesystem which is mounted by a remote machine over the <font SIZE="-1">NFS</font>. It also allows setting of quotas on <font SIZE="-1">NFS</font> mounted filesystem (if configured during compilation and allowed by a command line option <code>-S</code>). The results are used by <code><a href="/docs/linux/man/1-quota/">quota</a></code>(1) to display user quotas for remote filesystems and by <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8) to set quotas on remote filesystems. <code>rquotad</code> daemon uses tcp-wrappers library (under service name <i>rquotad</i>) which allows you to specify hosts allowed/disallowed to use the daemon (see <code><a href="/docs/linux/man/5-hosts-allow/">hosts.allow</a></code>(5) manpage for more information). The <code>rquotad</code> daemon is normally started at boot time from the system startup scripts.</p>
<h2>Options</h2>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd>Shows version of quota tools.</p>
<dt><code>-s, &#8211;no-setquota</code></p>
<dd>Don&#8217;t allow setting of quotas (default). This option is available only if utilities were compiled with the <i>rpcsetquota</i> option.</p>
<dt><code>-S, &#8211;setquota</code></p>
<dd>Allow setting of quotas. This option is available only if utilities were compiled with the <i>rpcsetquota</i> option.</p>
<dt><code>-F, &#8211;foreground</code></p>
<dd>Run daemon in foreground (may be useful for debugging purposes).</p>
<dt><code>-I, &#8211;autofs</code></p>
<dd>Do not ignore autofs mountpoints.</p>
<dt><code>-p </code><i>port</i><code>, &#8211;port </code><i>port</i></p>
<dd>Listen on alternate port <i>port.</i></p>
<dt><code>-x </code><i>path</i><code>, &#8211;xtab </code><i>path</i></p>
<dd>Set an alternative file with NFSD export table. This file is used to determine pseudoroot of NFSv4 exports. The pseudoroot is then prepended to each relative path (i.e. a path not beginning by &#8216;/&#8217;) received in a quota RPC request. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>aquota.user or aquota.group</code></p>
<dd>quota file at the filesystem root (version 2 quota, non-XFS filesystems)</p>
<dt><code>quota.user or quota.group</code></p>
<dd>quota file at the filesystem root (version 1 quota, non-XFS filesystems)</p>
<dt><code>/etc/mtab</code></p>
<dd>default filesystems</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/3-rpc/">rpc</a></code>(3), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/5-services/">services</a></code>(5), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) </p>
