---
title: "lxc-usernsexec(1)"
name: "lxc-usernsexec"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-usernsexec/"
description: "lxc-usernsexec – Run a task as root in a new user namespace."
---

<h2>NAME</h2>
<p> lxc-usernsexec &#8211; Run a task as root in a new user namespace.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-usernsexec</code> [-m <i>uid-map</i>] {&#8211; command}</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-usernsexec</code> can be used to run a task as root in a new user namespace.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m </code><i>uid-map</i></p>
<dd> The uid map to use in the user namespace. Each map consists of four colon-separate values. First a character &#8216;u&#8217;, &#8216;g&#8217; or &#8216;b&#8217; to specify whether this map pertains to user ids, group ids, or both; next the first userid in the user namespace; next the first userid as seen on the host; and finally the number of ids to be mapped. </p>
<p> More than one map can be specified. If no map is specified, then by default the full uid and gid ranges granted by /etc/subuid and /etc/subgid will be mapped to the uids and gids starting at 0 in the container. </p>
<p> Note that <i>lxc-usernsexec</i> always tries to setuid and setgid to 0 in the namespace. Therefore uid 0 in the namespace must be mapped.</dl>
<h2>EXAMPLES</h2>
<p> To spawn a shell with the full allotted subuids mapped into the container, use </p>
<pre>
          lxc-usernsexec
        
</pre>
<p> To run a different shell than <i>/bin/sh</i>, use </p>
<pre>
          lxc-usernsexec -- /bin/bash
        
</pre>
<p> If your user id is 1000, root in a container is mapped to 190000, and you wish to chown a file you own to root in the container, you can use: </p>
<pre>
          lxc-usernsexec -m b:0:1000:1 -m b:1:190000:1 -- /bin/chown 1:1 $file
        
</pre>
<p> This maps your userid to root in the user namespace, and 190000 to uid 1. Since root in the user namespace is privileged over all userids mapped into the namespace, you are allowed to change the file ownership, which you could not do on the host using a simple chown.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Serge Hallyn &lt;serge.hallyn [at] ubuntu.com&gt; </p>
<h2>Index</h2>
