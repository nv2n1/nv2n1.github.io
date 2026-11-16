---
title: "runc-restore(8)"
name: "runc-restore"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-restore/"
description: "runc-restore – restore a container from a previous checkpoint"
---

<p><code>runc-restore</code> &#8211; restore a container from a previous checkpoint </p>
<h2>Synopsis</h2>
<p><code>runc restore</code> [<i>option</i> &#8230;] <i>container-id</i> </p>
<h2>Description</h2>
<p>Restores the container instance from a previously performed <code>runc checkpoint</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;console-socket</code> <i>path</i></dt>
<dd>Path to an <code>AF_UNIX</code> socket which will receive a file descriptor referencing the master end of the console&#8217;s pseudoterminal. See docs/terminals &lt;<a rel="nofollow" href="https://github.com/opencontainers/runc/blob/master/docs/terminals.md">https://github.com/opencontainers/runc/blob/master/docs/terminals.md</a>&gt;. </dd>
<dt><code>&#8211;image-path</code> <i>path</i></dt>
<dd>Set path to get criu image files to restore from. </dd>
<dt><code>&#8211;work-path</code> <i>path</i></dt>
<dd>Set path for saving criu work files and logs. The default is to reuse the image files directory. </dd>
<dt><code>&#8211;tcp-established</code></dt>
<dd>Allow checkpoint/restore of established TCP connections. See criu &#8211;tcp-establised option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--tcp-established">https://criu.org/CLI/opt/&#8211;tcp-established</a>&gt;. </dd>
<dt><code>&#8211;ext-unix-sk</code></dt>
<dd>Allow checkpoint/restore of external unix sockets. See criu &#8211;ext-unix-sk option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--ext-unix-sk">https://criu.org/CLI/opt/&#8211;ext-unix-sk</a>&gt;. </dd>
<dt><code>&#8211;shell-job</code></dt>
<dd>Allow checkpoint/restore of shell jobs. </dd>
<dt><code>&#8211;file-locks</code></dt>
<dd>Allow checkpoint/restore of file locks. See criu &#8211;file-locks option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--file-locks">https://criu.org/CLI/opt/&#8211;file-locks</a>&gt;. </dd>
<dt><code>&#8211;manage-cgroups-mode</code> <code>soft</code>|<code>full</code>|<code>strict</code>.</dt>
<dd>Cgroups mode. Default is <code>soft</code>. See criu &#8211;manage-cgroups option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--manage-cgroups">https://criu.org/CLI/opt/&#8211;manage-cgroups</a>&gt;. </dd>
<dt><code>&#8211;bundle</code>|<code>-b</code> <i>path</i></dt>
<dd>Path to the root of the bundle directory. Default is current directory. </dd>
<dt><code>&#8211;detach</code>|<code>-d</code></dt>
<dd>Detach from the container&#8217;s process. </dd>
<dt><code>&#8211;pid-file</code> <i>path</i></dt>
<dd>Specify the file to write the initial container process&#8217; PID to. </dd>
<dt><code>&#8211;no-subreaper</code></dt>
<dd>Disable the use of the subreaper used to reap reparented processes. </dd>
<dt><code>&#8211;no-pivot</code></dt>
<dd>Do not use pivot root to jail process inside rootfs. This should not be used except in exceptional circumstances, and may be unsafe from the security standpoint. </dd>
<dt><code>&#8211;empty-ns</code> <i>namespace</i></dt>
<dd>Create a <i>namespace</i>, but don&#8217;t restore its properties. See criu &#8211;empty-ns option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--empty-ns">https://criu.org/CLI/opt/&#8211;empty-ns</a>&gt;. </dd>
<dt><code>&#8211;auto-dedup</code></dt>
<dd>Enable auto deduplication of memory images. See criu &#8211;auto-dedup option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--auto-dedup">https://criu.org/CLI/opt/&#8211;auto-dedup</a>&gt;. </dd>
<dt><code>&#8211;lazy-pages</code></dt>
<dd>Use lazy migration mechanism. This requires a running <code>criu lazy-pages</code> daemon. See criu &#8211;lazy-pages option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--lazy-pages">https://criu.org/CLI/opt/&#8211;lazy-pages</a>&gt;. </dd>
<dt><code>&#8211;lsm-profile</code> <i>type</i>:<i>label</i></dt>
<dd>Specify an LSM profile to be used during restore. Here <i>type</i> can either be <code>apparamor</code> or <code>selinux</code>, and <i>label</i> is a valid LSM label. For example, <code>&#8211;lsm-profile &quot;selinux:system_u:system_r:container_t:s0:c82,c137&quot;</code>. By default, the checkpointed LSM profile is used upon restore. </dd>
<dt><code>&#8211;lsm-mount-context</code> <i>context</i></dt>
<dd>Specify an LSM mount context to be used during restore. Only mounts with an existing context will have their context replaced. With this option it is possible to change SELinux mount options. Instead of mounting with the checkpointed context, the specified <i>context</i> will be used. For example, <code>&#8211;lsm-mount-context &quot;system_u:object_r:container_file_t:s0:c82,c137&quot;</code>. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-criu/">criu</a></code>(8), <code><a href="/docs/linux/man/8-runc-checkpoint/">runc-checkpoint</a></code>(8), <code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
