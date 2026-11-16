---
title: "runc-checkpoint(8)"
name: "runc-checkpoint"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-checkpoint/"
description: "runc-checkpoint – checkpoint a running container"
---

<p><code>runc-checkpoint</code> &#8211; checkpoint a running container </p>
<h2>Synopsis</h2>
<p><code>runc checkpoint</code> [<i>option</i> &#8230;] <i>container-id</i> </p>
<h2>Description</h2>
<p>The <code>checkpoint</code> command saves the state of the running container instance with the help of <code><a href="/docs/linux/man/8-criu/">criu</a></code>(8) tool, to be restored later. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;image-path</code> <i>path</i></dt>
<dd>Set path for saving criu image files. The default is <i>./checkpoint</i>. </dd>
<dt><code>&#8211;work-path</code> <i>path</i></dt>
<dd>Set path for saving criu work files and logs. The default is to reuse the image files directory. </dd>
<dt><code>&#8211;parent-path</code> <i>path</i></dt>
<dd>Set path for previous criu image files, in pre-dump. </dd>
<dt><code>&#8211;leave-running</code></dt>
<dd>Leave the process running after checkpointing. </dd>
<dt><code>&#8211;tcp-established</code></dt>
<dd>Allow checkpoint/restore of established TCP connections. See criu &#8211;tcp-establised option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--tcp-established">https://criu.org/CLI/opt/&#8211;tcp-established</a>&gt;. </dd>
<dt><code>&#8211;ext-unix-sk</code></dt>
<dd>Allow checkpoint/restore of external unix sockets. See criu &#8211;ext-unix-sk option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--ext-unix-sk">https://criu.org/CLI/opt/&#8211;ext-unix-sk</a>&gt;. </dd>
<dt><code>&#8211;shell-job</code></dt>
<dd>Allow checkpoint/restore of shell jobs. </dd>
<dt><code>&#8211;lazy-pages</code></dt>
<dd>Use lazy migration mechanism. See criu &#8211;lazy-pages option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--lazy-pages">https://criu.org/CLI/opt/&#8211;lazy-pages</a>&gt;. </dd>
<dt><code>&#8211;status-fd</code> <i>fd</i></dt>
<dd>Pass a file descriptor <i>fd</i> to <code>criu</code>. Once <code>lazy-pages</code> server is ready, <code>criu</code> writes <code>
</dd></dl>
</code>
