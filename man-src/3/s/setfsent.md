---
title: "setfsent(3)"
name: "setfsent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setfsent/"
description: "getfsent, getfsspec, getfsfile, setfsent, endfsent – handle fstab entries"
---

<p>getfsent, getfsspec, getfsfile, setfsent, endfsent &#8211; handle fstab entries</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;fstab.h&gt;
void endfsent(void);
struct fstab *getfsent(void);
struct fstab *getfsfile(const char *mount_point);
struct fstab *getfsspec(const char *special_file);
int setfsent(void);</code></pre>
<h2>Description</h2>
<p>These functions read from the file <i>/etc/fstab</i>. The <i>struct fstab</i> is defined by: </p>
<pre><code>struct fstab {
    char *fs_spec;       /* block device name */
    char *fs_file;       /* mount point */
    char *fs_vfstype;    /* file-system type */
    char *fs_mntops;     /* mount options */
    const char *fs_type; /* rw/rq/ro/sw/xx option */
    int fs_freq;         /* dump frequency, in days */
    int fs_passno;       /* pass number on parallel dump */
};</code></pre>
<p> Here the field <i>fs_type</i> contains (on a *BSD system) one of the five strings &quot;rw&quot;, &quot;rq&quot;, &quot;ro&quot;, &quot;sw&quot;, &quot;xx&quot; (read-write, read-write with quota, read-only, swap, ignore). The function <code>setfsent</code>() opens the file when required and positions it at the first line. The function <code>getfsent</code>() parses the next line from the file. (After opening it when required.) The function <code>endfsent</code>() closes the file when required. The function <code>getfsspec</code>() searches the file from the start and returns the first entry found for which the <i>fs_spec</i> field matches the <i>special_file</i> argument. The function <code>getfsfile</code>() searches the file from the start and returns the first entry found for which the <i>fs_file</i> field matches the <i>mount_point</i> argument.</p>
<h2>Return Value</h2>
<p>Upon success, the functions <code>getfsent</code>(), <code>getfsfile</code>(), and <code>getfsspec</code>() return a pointer to a <i>struct fstab</i>, while <code>setfsent</code>() returns 1. Upon failure or end-of-file, these functions return NULL and 0, respectively.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>endfsent</code>(),<br />
 <code>setfsent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:fsent
</td>
</tr>
<tr VALIGN=top>
<td> <code>getfsent</code>(),<br />
 <code>getfsspec</code>(),<br />
 <code>getfsfile</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:fsent locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are not in POSIX.1. Several operating systems have them, for example, *BSD, SunOS, Digital UNIX, AIX (which also has a <code>getfstype</code>()). HP-UX has functions of the same names, that however use a <i>struct checklist</i> instead of a <i>struct fstab</i>, and calls these functions obsolete, superseded by <code><a href="/docs/linux/man/3-getmntent/">getmntent</a></code>(3).</p>
<h2>Notes</h2>
<p>These functions are not thread-safe. </p>
<p> Since Linux allows mounting a block special device in several places, and since several devices can have the same mount point, where the last device with a given mount point is the interesting one, while <code>getfsfile</code>() and <code>getfsspec</code>() only return the first occurrence, these two functions are not suitable for use under Linux.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getmntent/">getmntent</a></code>(3), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
