---
title: "systemd-readahead-replay-service(8)"
name: "systemd-readahead-replay-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-readahead-replay-service/"
description: "systemd-readahead-replay.service, systemd-readahead-collect.service, systemd-readahead-done.service, systemd-readahead-done.timer, systemd-readahead – Disk read ahead logic"
---

<p>systemd-readahead-replay.service, systemd-readahead-collect.service, systemd-readahead-done.service, systemd-readahead-done.timer, systemd-readahead &#8211; Disk read ahead logic</p>
<h2>Synopsis</h2>
<p>systemd-readahead-replay.service </p>
<p> systemd-readahead-collect.service </p>
<p> systemd-readahead-done.service </p>
<p> systemd-readahead-done.timer</p>
<dl>
<dt> <code>/usr/lib/systemd/systemd-readahead/systemd-readahead</code> [OPTIONS&#8230;] COMMAND [DIRECTORY | FILE]</dl>
<h2>Description</h2>
<dd>systemd-readahead-collect.service is a service that collects disk usage patterns at boot time. systemd-readahead-replay.service is a service that replays this access data collected at the subsequent boot. Since disks tend to be magnitudes slower than RAM, this is intended to improve boot speeds by pre-loading early at boot all data on disk that is known to be read for the complete boot process. </p>
<p> systemd-readahead-done.service is executed a short while after boot completed and signals systemd-readahead-collect.service to end data collection. On this signal, this service will then sort the collected disk accesses and store information about them in /.readahead. </p>
<p> Normally, both systemd-readahead-collect.service and systemd-readahead-replay.service are activated at boot so that access patterns from the preceding boot are replayed and new data collected for the subsequent boot. However, on read-only media where the collected data cannot be stored, it might be a good idea to disable systemd-readahead-collect.service. </p>
<p> On rotating media, when replaying disk accesses at early boot, systemd-readahead-replay.service will order read requests by their location on disk. On non-rotating media, they will be ordered by their original access timestamp. If the file system supports it, systemd-readahead-collect.service will also defragment and rearrange files on disk to optimize subsequent boot times.</p>
<h2>Options</h2>
<p>systemd-readahead understands the following options: </p>
<p> <code>&#8211;files-max=</code></p>
<dl>
<dd>Maximum number of files to read ahead. Only valid for thes <code>collect</code> command.</dl>
<p> <code>&#8211;file-size-max=</code></p>
<dl>
<dd>Maximum size of files in bytes to read ahead. Only valid for the <code>collect</code> and <code>replay</code> commands.</dl>
<p> <code>&#8211;timeout=</code></p>
<dl>
<dd>Maximum time in microseconds to spend collecting data. Only valid for the <code>collect</code> command.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Commands</h2>
<p>The following commands are understood by systemd-readahead: </p>
<p> <code>collect [</code><i>DIRECTORY</i><code>]</code></p>
<dl>
<dd>Collect read-ahead data on early boot. When terminating, it will write out a pack file to the indicated directory containing the read-ahead data.</dl>
<p> <code>replay [</code><i>DIRECTORY</i><code>]</code></p>
<dl>
<dd>Perform read-ahead on the specified directory tree.</dl>
<p> <code>analyze [</code><i>FILE</i><code>]</code></p>
<dl>
<dd>Dumps the content of the read-ahead pack file to the terminal. For each file, the output lists approximately how much will be read ahead by the <code>replay</code> command.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) </p>
