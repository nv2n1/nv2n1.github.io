---
title: "runc-checkpoint(8)"
name: "runc-checkpoint"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-checkpoint/"
description: "runc-checkpoint – checkpoint a running container"
---
<h2 class="name">NAME</h2>
<p> <code>runc-checkpoint</code> - checkpoint a running container </p>
<h2>SYNOPSIS</h2>
<p> <code>runc checkpoint</code> [<i>option</i> ...] <i>container-id</i> </p>
<h2>DESCRIPTION</h2>
<p>The <code>checkpoint</code> command saves the state of the running container instance with the help of <code><a href="/docs/linux/man/8-criu/">criu</a></code>(8) tool, to be restored later. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--image-path</code><i>path</i></dt>
<dd> <p> Set path for saving criu image files. The default is <i>./checkpoint</i>. </p>
 </dd>
<dt><code>--work-path</code><i>path</i></dt>
<dd> <p> Set path for saving criu work files and logs. The default is to reuse the image files directory. </p>
 </dd>
<dt><code>--parent-path</code><i>path</i></dt>
<dd> <p> Set path for previous criu image files, in pre-dump. </p>
 </dd>
<dt><code>--leave-running</code></dt>
<dd> <p> Leave the process running after checkpointing. </p>
 </dd>
<dt><code>--tcp-established</code></dt>
<dd> <p> Allow checkpoint/restore of established TCP connections. See criu --tcp-establised option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--tcp-established">https://criu.org/CLI/opt/--tcp-established</a>&gt;. </p>
 </dd>
<dt><code>--ext-unix-sk</code></dt>
<dd> <p> Allow checkpoint/restore of external unix sockets. See criu --ext-unix-sk option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--ext-unix-sk">https://criu.org/CLI/opt/--ext-unix-sk</a>&gt;. </p>
 </dd>
<dt><code>--shell-job</code></dt>
<dd> <p> Allow checkpoint/restore of shell jobs. </p>
 </dd>
<dt><code>--lazy-pages</code></dt>
<dd> <p> Use lazy migration mechanism. See criu --lazy-pages option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--lazy-pages">https://criu.org/CLI/opt/--lazy-pages</a>&gt;. </p>
 </dd>
<dt><code>--status-fd</code><i>fd</i></dt>
<dd> <p> Pass a file descriptor <i>fd</i> to <code>criu</code>. Once <code>lazy-pages</code> server is ready, <code>criu</code> writes <code>\0</code> (a zero byte) to that <i>fd</i>. Used together with <code>--lazy-pages</code>. </p>
 </dd>
<dt><code>--page-server</code><i>IP-address</i>:<i>port</i></dt>
<dd> <p> Start a page server at the specified <i>IP-address</i> and <i>port</i>. This is used together with <code>criu lazy-pages</code>. See criu lazy migration &lt;<a rel="nofollow" href="https://criu.org/Lazy_migration">https://criu.org/Lazy_migration</a>&gt;. </p>
 </dd>
<dt><code>--file-locks</code></dt>
<dd> <p> Allow checkpoint/restore of file locks. See criu --file-locks option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--file-locks">https://criu.org/CLI/opt/--file-locks</a>&gt;. </p>
 </dd>
<dt><code>--pre-dump</code></dt>
<dd> <p> Do a pre-dump, i.e. dump container&#8217;s memory information only, leaving the container running. See criu iterative migration &lt;<a rel="nofollow" href="https://criu.org/Iterative_migration">https://criu.org/Iterative_migration</a>&gt;. </p>
 </dd>
<dt><code>--manage-cgroups-mode</code><code>soft</code>|<code>full</code>|<code>strict</code>.</dt>
<dd> <p> Cgroups mode. Default is <code>soft</code>. See criu --manage-cgroups option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--manage-cgroups">https://criu.org/CLI/opt/--manage-cgroups</a>&gt;. </p>
 </dd>
<dt><code>--empty-ns</code><i>namespace</i></dt>
<dd> <p> Checkpoint a <i>namespace</i>, but don&#8217;t save its properties. See criu --empty-ns option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--empty-ns">https://criu.org/CLI/opt/--empty-ns</a>&gt;. </p>
 </dd>
<dt><code>--auto-dedup</code></dt>
<dd> <p> Enable auto deduplication of memory images. See criu --auto-dedup option &lt;<a rel="nofollow" href="https://criu.org/CLI/opt/--auto-dedup">https://criu.org/CLI/opt/--auto-dedup</a>&gt;. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-criu/">criu</a></code>(8), <code><a href="/docs/linux/man/8-runc-restore/">runc-restore</a></code>(8), <code><a href="/docs/linux/man/8-runc/">runc</a></code>(8), <code><a href="/docs/linux/man/8-criu/">criu</a></code>(8). </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">SEE ALSO</a></dt>
<dd>  </dd></dl>
