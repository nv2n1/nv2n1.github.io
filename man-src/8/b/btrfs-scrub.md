---
title: "btrfs-scrub(8)"
name: "btrfs-scrub"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-scrub/"
description: "btrfs-scrub – scrub btrfs filesystem, verify block checksums"
---

<p>btrfs-scrub &#8211; scrub btrfs filesystem, verify block checksums</p>
<h2>Synopsis</h2>
<p><code>btrfs scrub</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs scrub</code> is used to scrub a btrfs filesystem, which will read all data and metadata blocks from all devices and verify checksums. Automatically repair corrupted blocks if there&#8217;s a correct copy available.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Scrub is not a filesystem checker (fsck) and does not verify nor repair structural damage in the filesystem. It really only checks checksums of data and tree blocks, it doesn&#8217;t ensure the content of tree blocks is valid and consistent. There&#8217;s some validation performed when metadata blocks are read from disk but it&#8217;s not extensive and cannot substitute full <i>btrfs check</i> run.  The user is supposed to run it manually or via a periodic system service. The recommended period is a month but could be less. The estimated device bandwidth utilization is about 80% on an idle filesystem. The IO priority class is by default <i>idle</i> so background scrub should not significantly interfere with normal filesystem operation. The scrubbing status is recorded in <i>/var/lib/btrfs/</i> in textual files named <i>scrub.status.UUID</i> for a filesystem identified by the given UUID. (Progress state is communicated through a named pipe in file <i>scrub.progress.UUID</i> in the same directory.) The status file is updated every 5 seconds. A resumed scrub will continue from the last saved position.</p>
<h2>Subcommand</h2>
<p><code>cancel</code> <i>&lt;path&gt;</i>|<i>&lt;device&gt;</i></p>
<dl>
<dd>If a scrub is running on the filesystem identified by <i>path</i> cancel it. </p>
<p> If a <i>device</i> is specified, the corresponding filesystem is found and <code>btrfs scrub cancel</code> behaves as if it was called on that filesystem.</dl>
<p> <code>resume</code> [-BdqrR] [-c <i>&lt;ioprio_class&gt;</i> -n <i>&lt;ioprio_classdata&gt;</i>] <i>&lt;path&gt;</i>|<i>&lt;device&gt;</i></p>
<dl>
<dd>Resume a cancelled or interrupted scrub on the filesystem identified by <i>path</i> or on a given <i>device</i>. </p>
<p> Does not start a new scrub if the last scrub finished successfully. </p>
<p> <code>Options</code> </p>
<p> see <code>scrub start</code>.</dl>
<p> <code>start</code> [-BdqrRf] [-c <i>&lt;ioprio_class&gt;</i> -n <i>&lt;ioprio_classdata&gt;</i>] <i>&lt;path&gt;</i>|<i>&lt;device&gt;</i></p>
<dl>
<dd>Start a scrub on all devices of the filesystem identified by <i>path</i> or on a single <i>device</i>. If a scrub is already running, the new one fails. </p>
<p> Without options, scrub is started as a background process. </p>
<p> The default IO priority of scrub is the idle class. The priority can be configured similar to the <code><a href="/docs/linux/man/1-ionice/">ionice</a></code>(1) syntax using <i>-c</i> and <i>-n</i> options. </p>
<p> <code>Options</code> </p>
<p> -B</p>
<dl>
<dd>do not background and print scrub statistics when finished</dl>
<p> -d</p>
<dl>
<dd>print separate statistics for each device of the filesystem (<i>-B</i> only) at the end</dl>
<p> -q</p>
<dl>
<dd>be quiet, omit error messages and statistics</dl>
<p> -r</p>
<dl>
<dd>run in read-only mode, do not attempt to correct anything, can be run on a read-only filesystem</dl>
<p> -R</p>
<dl>
<dd>raw print mode, print full data instead of summary</dl>
<p> -c <i>&lt;ioprio_class&gt;</i></p>
<dl>
<dd>set IO priority class (see <code><a href="/docs/linux/man/1-ionice/">ionice</a></code>(1) manpage)</dl>
<p> -n <i>&lt;ioprio_classdata&gt;</i></p>
<dl>
<dd>set IO priority classdata (see <code><a href="/docs/linux/man/1-ionice/">ionice</a></code>(1) manpage)</dl>
<p> -f</p>
<dl>
<dd>force starting new scrub even if a scrub is already running, this can useful when scrub status file is damaged and reports a running scrub although it is not, but should not normally be necessary</dl>
</dl>
<p> <code>status</code> [-d] <i>&lt;path&gt;</i>|<i>&lt;device&gt;</i></p>
<dl>
<dd>Show status of a running scrub for the filesystem identified by <i>path</i> or for the specified <i>device</i>. </p>
<p> If no scrub is running, show statistics of the last finished or cancelled scrub for that filesystem or device. </p>
<p> <code>Options</code> </p>
<p> -d</p>
<dl>
<dd>print separate statistics for each device of the filesystem</dl>
</dl>
<h2>Exit Status</h2>
<p><code>btrfs scrub</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure: </p>
<p> 1</p>
<dl>
<dd>scrub couldn&#8217;t be performed</dl>
<p> 2</p>
<dl>
<dd>there is nothing to resume</dl>
<p> 3</p>
<dl>
<dd>scrub found uncorrectable errors</dl>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/1-ionice/">ionice</a></code>(1) </p>
