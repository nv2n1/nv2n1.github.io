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
<dt><code>&#8211;image-path</code> <i>path</i></p>
<dd>Set path for saving criu image files. The default is <i>./checkpoint</i>. </p>
<dt><code>&#8211;work-path</code> <i>path</i></p>
<dd>Set path for saving criu work files and logs. The default is to reuse the image files directory. </p>
<dt><code>&#8211;parent-path</code> <i>path</i></p>
<dd>Set path for previous criu image files, in pre-dump. </p>
<dt><code>&#8211;leave-running</code></p>
<dd>Leave the process running after checkpointing. </p>
<dt><code>&#8211;tcp-established</code></p>
<dd>Allow checkpoint/restore of established TCP connections. See criu &#8211;tcp-establised option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--tcp-established">https://criu.org/CLI/opt/&#8211;tcp-established</a>&gt;. </p>
<dt><code>&#8211;ext-unix-sk</code></p>
<dd>Allow checkpoint/restore of external unix sockets. See criu &#8211;ext-unix-sk option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--ext-unix-sk">https://criu.org/CLI/opt/&#8211;ext-unix-sk</a>&gt;. </p>
<dt><code>&#8211;shell-job</code></p>
<dd>Allow checkpoint/restore of shell jobs. </p>
<dt><code>&#8211;lazy-pages</code></p>
<dd>Use lazy migration mechanism. See criu &#8211;lazy-pages option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--lazy-pages">https://criu.org/CLI/opt/&#8211;lazy-pages</a>&gt;. </p>
<dt><code>&#8211;status-fd</code> <i>fd</i></p>
<dd>Pass a file descriptor <i>fd</i> to <code>criu</code>. Once <code>lazy-pages</code> server is ready, <code>criu</code> writes <code>
