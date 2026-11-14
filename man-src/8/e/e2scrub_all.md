---
title: "e2scrub_all(8)"
name: "e2scrub_all"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e2scrub_all/"
description: "e2scrub_all – check all mounted ext[234] file systems for errors."
---

<p>e2scrub_all &#8211; check all mounted ext[234] file systems for errors.</p>
<h2>Synopsys</h2>
<p><code>e2scrub_all [OPTION]</code></p>
<h2>Description</h2>
<p>Searches the system for all LVM logical volumes containing an ext2, ext3, or ext4 file system, and checks them for problems. The checking is performed by invoking the <code>e2scrub</code> tool, which will look for corruptions. Corrupt file systems will be tagged as having errors so that fsck will be invoked before the next mount. If no errors are encountered, <code>fstrim</code> will be called on the file system if it is mounted. See the <code>e2scrub</code> manual page for more information about how the checking is performed.</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>Print what commands <code>e2scrub_all</code> would execute to initiate the e2scrub operations. (Note: these commands will not actually be executed; however, since <code>e2scrub_all</code> needs to run some additional, privileged commands to query the system to determine which <code>e2scrub</code> commands would be executed, it still needs to be run as root.)</p>
<dt><code>-r</code></p>
<dd>Remove e2scrub snapshots but do not check anything.</p>
<dt><code>-A</code></p>
<dd>Scrub all ext[234] file systems even if they are not mounted.</p>
<dt><code>-V</code></p>
<dd>Print version information and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-e2scrub/">e2scrub</a></code>(8)</p>
<h2>Author</h2>
<p>Darrick J. Wong &lt;darrick.wong [at] oracle.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169;2018 Oracle. License is GPLv2+. &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-2.0.html">http://www.gnu.org/licenses/gpl-2.0.html</a>&gt;</p>
