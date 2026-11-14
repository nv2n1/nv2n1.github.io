---
title: "getmntent_r(3)"
name: "getmntent_r"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getmntent_r/"
description: "getmntent, setmntent, addmntent, endmntent, hasmntopt, getmntent_r – get filesystem descriptor file entry"
---

<h2 class="name">NAME</h2>
<p> getmntent, setmntent, addmntent, endmntent, hasmntopt, getmntent_r &#8211; get filesystem descriptor file entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;mntent.h&gt;
#include &lt;stdio.h&gt;
FILE *setmntent(const char *filename, const char *type);
struct mntent *getmntent(FILE *stream);
int addmntent(FILE *stream, const struct mntent *mnt);
int endmntent(FILE *streamp);
char *hasmntopt(const struct mntent *mnt, const char *opt);
/* GNU extension */
#include &lt;mntent.h&gt;
struct mntent *getmntent_r(FILE *streamp, struct mntent *mntbuf,
                           char *buf, int buflen);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getmntent_r</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> These routines are used to access the filesystem description file <i>/etc/fstab</i> and the mounted filesystem description file <i>/etc/mtab</i>. </p>
<p> The <code>setmntent</code>() function opens the filesystem description file <i>filename</i> and returns a file pointer which can be used by <code>getmntent</code>(). The argument <i>type</i> is the type of access required and can take the same values as the <i>mode</i> argument of <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3). The returned stream should be closed using <code>endmntent</code>() rather than <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3). </p>
<p> The <code>getmntent</code>() function reads the next line of the filesystem description file from <i>stream</i> and returns a pointer to a structure containing the broken out fields from a line in the file. The pointer points to a static area of memory which is overwritten by subsequent calls to <code>getmntent</code>(). </p>
<p> The <code>addmntent</code>() function adds the <i>mntent</i> structure <i>mnt</i> to the end of the open <i>stream</i>. </p>
<p> The <code>endmntent</code>() function closes the <i>stream</i> associated with the filesystem description file. </p>
<p> The <code>hasmntopt</code>() function scans the <i>mnt_opts</i> field (see below) of the <i>mntent</i> structure <i>mnt</i> for a substring that matches <i>opt</i>. See <i>&lt;mntent.h&gt;</i> and <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) for valid mount options. </p>
<p> The reentrant <code>getmntent_r</code>() function is similar to <code>getmntent</code>(), but stores the <i>struct mount</i> in the provided <i>*mntbuf</i> and stores the strings pointed to by the entries in that struct in the provided array <i>buf</i> of size <i>buflen</i>. </p>
<p> The <i>mntent</i> structure is defined in <i>&lt;mntent.h&gt;</i> as follows: </p>
<p> struct mntent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*mnt_fsname;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;name of mounted filesystem&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*mnt_dir;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;filesystem path prefix&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*mnt_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;mount type&nbsp;(see mntent.h)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*mnt_opts;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;mount options&nbsp;(see mntent.h)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;mnt_freq;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;dump frequency in days&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;mnt_passno;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pass number on parallel fsck&nbsp;*/ }; </p>
<p> Since fields in the mtab and fstab files are separated by whitespace, octal escapes are used to represent the characters space ( ), tab (	), newline (
), and backslash (\) in those files when they occur in one of the four strings in a <i>mntent</i> structure. The routines <code>addmntent</code>() and <code>getmntent</code>() will convert from string representation to escaped representation and back. When converting from escaped representation, the sequence \134 is also converted to a backslash.</p>
<h2>RETURN VALUE</h2>
<p> The <code>getmntent</code>() and <code>getmntent_r</code>() functions return a pointer to the <i>mntent</i> structure or NULL on failure. </p>
<p> The <code>addmntent</code>() function returns 0 on success and 1 on failure. </p>
<p> The <code>endmntent</code>() function always returns 1. </p>
<p> The <code>hasmntopt</code>() function returns the address of the substring if a match is found and NULL otherwise.</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/fstab</i></p>
<dd> filesystem description file</p>
<dt><i>/etc/mtab</i></p>
<dd> mounted filesystem description file</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>setmntent</code>(), <code>endmntent</code>(), <code>hasmntopt</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>getmntent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:mntentbuf locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>addmntent</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:stream locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getmntent_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The nonreentrant functions are from SunOS 4.1.3. A routine <code>getmntent_r</code>() was introduced in HP-UX 10, but it returns an <i>int</i>. The prototype shown above is glibc-only.</p>
<h2>NOTES</h2>
<p> System V also has a <code>getmntent</code>() function but the calling sequence differs, and the returned structure is different. Under System V <i>/etc/mnttab</i> is used. 4.4BSD and Digital UNIX have a routine <code>getmntinfo</code>(), a wrapper around the system call <code>getfsstat</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
