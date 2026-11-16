---
title: "nilfs_cleanerd(5)"
name: "nilfs_cleanerd"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nilfs_cleanerd/"
description: "nilfs_cleanerd.conf – nilfs_cleanerd(8) configuration file"
---

<p>nilfs_cleanerd.conf &#8211; <a href="/docs/linux/man/8-nilfs_cleanerd/">nilfs_cleanerd</a>(8) configuration file</p>
<h2>Description</h2>
<p>The <i>nilfs_cleanerd.conf</i> file is the configuration file for the <code><a href="/docs/linux/man/8-nilfs_cleanerd/">nilfs_cleanerd</a></code>(8) which reclaims disk space of the NILFS2 filesystem. This file specifies the parameters related to garbage collection (GC) and behaviour of the daemon program. </p>
<p> The file contains keyword argument pairs or keyword-only directives, one per line. Lines starting with &#8216;#&#8217; are interpreted as comments. The comment lines and empty lines are ignored.</p>
<h2>Parameters</h2>
<p>The possible keywords and their meanings are as follows (keywords and arguments are both case-sensitive):</p>
<dl>
<dt><code>protection_period</code></dt>
<dd>Specify the period during which each checkpoint is protected from the garbage collector (in seconds). NILFS2 GC never deletes checkpoints and their blocks whose duration time is less than the value. The default value is 3600, meaning one hour.</dd>
<dt><code>selection_policy</code></dt>
<dd>Specify the GC policy. At present, only the `<code>timestamp</code>&#8216; policy, which reclaims segments in order from oldest to newest, is support.</dd>
<dt><code>nsegments_per_clean</code></dt>
<dd>Specify the number of segments reclaimed by a single cleaning step. The default value is 2.</dd>
<dt><code>cleaning_interval</code></dt>
<dd>Specify the cleaning interval in seconds. The default value is 5.</dd>
<dt><code>retry_interval</code></dt>
<dd>Specify retry interval in seconds. This value provides the retry interval of GC in case of resource shortages. The default value is 60.</dd>
<dt><code>use_mmap</code></dt>
<dd>Specify whether to use <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for reading segments. At present, this option is enabled if supported regardless of this directive.</dd>
<dt><code>log_priority</code></dt>
<dd>Gives the verbosity level that is used when logging messages from <code><a href="/docs/linux/man/8-nilfs_cleanerd/">nilfs_cleanerd</a></code>(8). The possible values are: <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, and <code>debug</code>. The default is <code>info</code>.</dd></dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/nilfs_cleanerd.conf</i></dt>
<dd>Configuration file for <code><a href="/docs/linux/man/8-nilfs_cleanerd/">nilfs_cleanerd</a></code>(8).</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nilfs_cleanerd/">nilfs_cleanerd</a></code>(8). </p>
