---
title: "ulckpwdf(3)"
name: "ulckpwdf"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ulckpwdf/"
description: "getspnam, getspnam_r, getspent, getspent_r, setspent, endspent, fgetspent, fgetspent_r, sgetspent, sgetspent_r, putspent, lckpwdf, ulckpwdf – get shadow password file entry"
---

<p>getspnam, getspnam_r, getspent, getspent_r, setspent, endspent, fgetspent, fgetspent_r, sgetspent, sgetspent_r, putspent, lckpwdf, ulckpwdf &#8211; get shadow password file entry</p>
<h2>Synopsis</h2>
<pre><code>/* General shadow password file API */
#include &lt;shadow.h&gt;

struct spwd *getspnam(const char *name);

struct spwd *getspent(void);

void setspent(void);

void endspent(void);

struct spwd *fgetspent(FILE *stream);

struct spwd *sgetspent(const char *s);

int putspent(const struct spwd *p, FILE *stream);

int lckpwdf(void);

int ulckpwdf(void);

/* GNU extension */
#include &lt;shadow.h&gt;

int getspent_r(struct spwd *spbuf,
               char *buf, size_t buflen, struct spwd **spbufp);

int getspnam_r(const char *name, struct spwd *spbuf,
               char *buf, size_t buflen, struct spwd **spbufp);

int fgetspent_r(FILE *stream, struct spwd *spbuf,
                char *buf, size_t buflen, struct spwd **spbufp);

int sgetspent_r(const char *s, struct spwd *spbuf,
                char *buf, size_t buflen, struct spwd **spbufp);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>getspent_r</code>(), <code>getspnam_r</code>(), <code>fgetspent_r</code>(), <code>sgetspent_r</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>Long ago it was considered safe to have encrypted passwords openly visible in the password file. When computers got faster and people got more security-conscious, this was no longer acceptable. Julianne Frances Haugh implemented the shadow password suite that keeps the encrypted passwords in the shadow password database (e.g., the local shadow password file <i>/etc/shadow</i>, NIS, and LDAP), readable only by root. The functions described below resemble those for the traditional password database (e.g., see <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3) and <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3)). The <code>getspnam</code>() function returns a pointer to a structure containing the broken-out fields of the record in the shadow password database that matches the username <i>name</i>. The <code>getspent</code>() function returns a pointer to the next entry in the shadow password database. The position in the input stream is initialized by <code>setspent</code>(). When done reading, the program may call <code>endspent</code>() so that resources can be deallocated. The <code>fgetspent</code>() function is similar to <code>getspent</code>() but uses the supplied stream instead of the one implicitly opened by <code>setspent</code>(). The <code>sgetspent</code>() function parses the supplied string <i>s</i> into a struct <i>spwd</i>. The <code>putspent</code>() function writes the contents of the supplied struct <i>spwd</i> <i>*p</i> as a text line in the shadow password file format to <i>stream</i>. String entries with value NULL and numerical entries with value -1 are written as an empty string. The <code>lckpwdf</code>() function is intended to protect against multiple simultaneous accesses of the shadow password database. It tries to acquire a lock, and returns 0 on success, or -1 on failure (lock not obtained within 15 seconds). The <code>ulckpwdf</code>() function releases the lock again. Note that there is no protection against direct access of the shadow password file. Only programs that use <code>lckpwdf</code>() will notice the lock. These were the functions that formed the original shadow API. They are widely available.</p>
<h3>Reentrant versions</h3>
<p>Analogous to the reentrant functions for the password database, glibc also has reentrant functions for the shadow password database. The <code>getspnam_r</code>() function is like <code>getspnam</code>() but stores the retrieved shadow password structure in the space pointed to by <i>spbuf</i>. This shadow password structure contains pointers to strings, and these strings are stored in the buffer <i>buf</i> of size <i>buflen</i>. A pointer to the result (in case of success) or NULL (in case no entry was found or an error occurred) is stored in <i>*spbufp</i>. The functions <code>getspent_r</code>(), <code>fgetspent_r</code>(), and <code>sgetspent_r</code>() are similarly analogous to their nonreentrant counterparts. Some non-glibc systems also have functions with these names, often with different prototypes.</p>
<h3>Structure</h3>
<p>The shadow password structure is defined in <i>&lt;shadow.h&gt;</i> as follows: </p>
<pre><code>struct spwd {
    char *sp_namp;         /* Login name */
    char *sp_pwdp;         /* Encrypted password */
    long sp_lstchg;        /* Date of last change
                              (measured in days since
                              1970-01-01 00:00:00 +0000 (UTC)) */
    long sp_min;           /* Min # of days between changes */
    long sp_max;           /* Max # of days between changes */
    long sp_warn;          /* # of days before password expires
                              to warn user to change it */
    long sp_inact;         /* # of days after password expires
                              until account is disabled */
    long sp_expire;        /* Date when account expires
                              (measured in days since
                              1970-01-01 00:00:00 +0000 (UTC)) */
    unsigned long sp_flag; /* Reserved */
};</code></pre>
<h2>Return Value</h2>
<p>The functions that return a pointer return NULL if no more entries are available or if an error occurs during processing. The functions which have <i>int</i> as the return value return 0 for success and -1 for failure, with <i>errno</i> set to indicate the cause of the error. </p>
<p> For the nonreentrant functions, the return value may point to static area, and may be overwritten by subsequent calls to these functions. </p>
<p> The reentrant functions return zero on success. In case of error, an error number is returned.</p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>The caller does not have permission to access the shadow password file.</p>
<dt><code>ERANGE</code></p>
<dd>Supplied buffer is too small.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/shadow</i></p>
<dd>local shadow password database file</p>
<dt><i>/etc/.pwd.lock</i></p>
<dd>lock file</dl>
<p> The include file <i>&lt;paths.h&gt;</i> defines the constant <code>_PATH_SHADOW</code> to the pathname of the shadow password file.</p>
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
<td> <code>getspnam</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:getspnam locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getspent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:getspent<br />
 race:spentbuf locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>setspent</code>(),<br />
 <code>endspent</code>(),<br />
 <code>getspent_r</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:getspent locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>fgetspent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:fgetspent
</td>
</tr>
<tr VALIGN=top>
<td> <code>sgetspent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:sgetspent
</td>
</tr>
<tr VALIGN=top>
<td> <code>putspent</code>(),<br />
 <code>getspnam_r</code>(),<br />
 <code>sgetspent_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>lckpwdf</code>(),<br />
 <code>ulckpwdf</code>(),<br />
 <code>fgetspent_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<p> In the above table, <i>getspent</i> in <i>race:getspent</i> signifies that if any of the functions <code>setspent</code>(), <code>getspent</code>(), <code>getspent_r</code>(), or <code>endspent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>Conforming To</h2>
<p>The shadow password database and its associated API are not specified in POSIX.1. However, many other systems provide a similar API.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3), <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3), <code><a href="/docs/linux/man/3-getpwnam_r/">getpwnam_r</a></code>(3), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
