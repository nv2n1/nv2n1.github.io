---
title: "matchpathcon_checkmatches(3)"
name: "matchpathcon_checkmatches"
section: "3"
letter: "m"
url: "/docs/linux/man/3-matchpathcon_checkmatches/"
description: "matchpathcon_checkmatches, matchpathcon_filespec_add, matchpathcon_filespec_destroy, matchpathcon_filespec_eval – check and report whether any specification index has no matches with any inode. Mai..."
---

<h2 class="name">NAME</h2>
<p> matchpathcon_checkmatches, matchpathcon_filespec_add, matchpathcon_filespec_destroy, matchpathcon_filespec_eval &#8211; check and report whether any specification index has no matches with any inode. Maintenance and statistics on inode associations </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>void matchpathcon_checkmatches(char *</code><i>str</i><code>);</code> </p>
<p> <code>int matchpathcon_filespec_add(ino_t </code><i>ino</i><code>, int </code><i>specind</i><code>, const char *</code><i>file</i><code>);</code> </p>
<p> <code>void matchpathcon_filespec_destroy(void);</code> </p>
<p> <code>void matchpathcon_filespec_eval(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>matchpathcon_checkmatches</code>() checks whether any specification has no matches and reports them. The <i>str</i> argument is used as a prefix for any warning messages. </p>
<p> <code>matchpathcon_filespec_add</code>() maintains an association between an inode <i>ino</i> and a specification index <i>specind</i>, and checks whether a conflicting specification is already associated with the same inode (e.g. due to multiple hard links). If so, then it uses the latter of the two specifications based on their order in the <i>file</i> context configuration. Returns the specification index used or -1 on error. </p>
<p> <code>matchpathcon_filespec_destroy</code>() destroys any inode associations that have been added, e.g. to restart for a new filesystem. </p>
<p> <code>matchpathcon_filespec_eval</code>() displays statistics on the hash table usage for the inode associations.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero on success or -1 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-matchpathcon/">matchpathcon</a></code>(3), <code><a href="/docs/linux/man/3-matchpathcon_index/">matchpathcon_index</a></code>(3), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-setfilecon/">setfilecon</a></code>(3), <code><a href="/docs/linux/man/3-setfscreatecon/">setfscreatecon</a></code>(3) </p>
<h2>Index</h2>
