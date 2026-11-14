---
title: "fgetspent_r(3)"
name: "fgetspent_r"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetspent_r/"
---

<h2 class="name">NAME</h2>
 

 getspnam, getspnam_r, getspent, getspent_r, setspent, endspent, fgetspent, fgetspent_r, sgetspent, sgetspent_r, putspent, lckpwdf, ulckpwdf - get shadow password file entry 

<h2>SYNOPSIS</h2>

 <pre><code>
/* General shadow password file API */
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
                char *buf, size_t buflen, struct spwd **spbufp);
</code></pre> 

 Feature Test Macro Requirements for glibc (see <b><a HREF="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></b>(7)): 

 <b>getspent_r</b>(), <b>getspnam_r</b>(), <b>fgetspent_r</b>(), <b>sgetspent_r</b>(): 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE

<h2>DESCRIPTION</h2>

 Long ago it was considered safe to have encrypted passwords openly visible in the password file. When computers got faster and people got more security-conscious, this was no longer acceptable. Julianne Frances Haugh implemented the shadow password suite that keeps the encrypted passwords in the shadow password database (e.g., the local shadow password file <i>/etc/shadow</i>, NIS, and LDAP), readable only by root. 

 The functions described below resemble those for the traditional password database (e.g., see <b><a HREF="/docs/linux/man/3-getpwnam/">getpwnam</a></b>(3) and <b><a HREF="/docs/linux/man/3-getpwent/">getpwent</a></b>(3)). 

 The <b>getspnam</b>() function returns a pointer to a structure containing the broken-out fields of the record in the shadow password database that matches the username <i>name</i>. 

 The <b>getspent</b>() function returns a pointer to the next entry in the shadow password database. The position in the input stream is initialized by <b>setspent</b>(). When done reading, the program may call <b>endspent</b>() so that resources can be deallocated. 

 The <b>fgetspent</b>() function is similar to <b>getspent</b>() but uses the supplied stream instead of the one implicitly opened by <b>setspent</b>(). 

 The <b>sgetspent</b>() function parses the supplied string <i>s</i> into a struct <i>spwd</i>. 

 The <b>putspent</b>() function writes the contents of the supplied struct <i>spwd</i> <i>*p</i> as a text line in the shadow password file format to <i>stream</i>. String entries with value NULL and numerical entries with value -1 are written as an empty string. 

 The <b>lckpwdf</b>() function is intended to protect against multiple simultaneous accesses of the shadow password database. It tries to acquire a lock, and returns 0 on success, or -1 on failure (lock not obtained within 15 seconds). The <b>ulckpwdf</b>() function releases the lock again. Note that there is no protection against direct access of the shadow password file. Only programs that use <b>lckpwdf</b>() will notice the lock. 

 These were the functions that formed the original shadow API. They are widely available.

<h3>Reentrant versions</h3>

 Analogous to the reentrant functions for the password database, glibc also has reentrant functions for the shadow password database. The <b>getspnam_r</b>() function is like <b>getspnam</b>() but stores the retrieved shadow password structure in the space pointed to by <i>spbuf</i>. This shadow password structure contains pointers to strings, and these strings are stored in the buffer <i>buf</i> of size <i>buflen</i>. A pointer to the result (in case of success) or NULL (in case no entry was found or an error occurred) is stored in <i>*spbufp</i>. 

 The functions <b>getspent_r</b>(), <b>fgetspent_r</b>(), and <b>sgetspent_r</b>() are similarly analogous to their nonreentrant counterparts. 

 Some non-glibc systems also have functions with these names, often with different prototypes.

<h3>Structure</h3>

 The shadow password structure is defined in <i>&lt;shadow.h&gt;</i> as follows: 

 struct spwd { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*sp_namp;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Login name&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*sp_pwdp;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Encrypted password&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;sp_lstchg;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Date of last change 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(measured in days since 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1970-01-01 00:00:00&nbsp;+0000&nbsp;(UTC))&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;sp_min;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Min&nbsp;#&nbsp;of days between changes&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;sp_max;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Max&nbsp;#&nbsp;of days between changes&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;sp_warn;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of days before password expires 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to warn user to change it&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;sp_inact;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of days after password expires 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;until account is disabled&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;sp_expire;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Date when account expires 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(measured in days since 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1970-01-01 00:00:00&nbsp;+0000&nbsp;(UTC))&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long sp_flag;&nbsp;<wbr>&nbsp;/*&nbsp;Reserved&nbsp;*/ };

<h2>RETURN VALUE</h2>

 The functions that return a pointer return NULL if no more entries are available or if an error occurs during processing. The functions which have <i>int</i> as the return value return 0 for success and -1 for failure, with <i>errno</i> set to indicate the cause of the error. 

 For the nonreentrant functions, the return value may point to static area, and may be overwritten by subsequent calls to these functions. 

 The reentrant functions return zero on success. In case of error, an error number is returned.

<h2>ERRORS</h2>

<dl>
<dt><b>EACCES</b>
<dd> The caller does not have permission to access the shadow password file.
<dt><b>ERANGE</b>
<dd> Supplied buffer is too small.</dl>

<h2>FILES</h2>

<dl>
<dt><i>/etc/shadow</i>
<dd> local shadow password database file
<dt><i>/etc/.pwd.lock</i>
<dd> lock file</dl>
 

 The include file <i>&lt;paths.h&gt;</i> defines the constant <b>_PATH_SHADOW</b> to the pathname of the shadow password file.

<h2>ATTRIBUTES</h2>

 For an explanation of the terms used in this section, see <b><a HREF="/docs/linux/man/7-attributes/">attributes</a></b>(7). <table BORDER> <tr VALIGN=top><td><b>Interface</b></td><td><b>Attribute</b></td><td><b>Value</b>
</td></tr> <tr VALIGN=top><td> <b>getspnam</b>() </td><td>Thread safety</td><td> MT-Unsafe race:getspnam locale 
</td></tr> <tr VALIGN=top><td> <b>getspent</b>() </td><td>Thread safety</td><td> MT-Unsafe race:getspent 
 race:spentbuf locale 
</td></tr> <tr VALIGN=top><td> <b>setspent</b>(), 
 <b>endspent</b>(), 
 <b>getspent_r</b>() </td><td>Thread safety</td><td> MT-Unsafe race:getspent locale 
</td></tr> <tr VALIGN=top><td> <b>fgetspent</b>() </td><td>Thread safety</td><td>MT-Unsafe race:fgetspent
</td></tr> <tr VALIGN=top><td> <b>sgetspent</b>() </td><td>Thread safety</td><td>MT-Unsafe race:sgetspent
</td></tr> <tr VALIGN=top><td> <b>putspent</b>(), 
 <b>getspnam_r</b>(), 
 <b>sgetspent_r</b>() </td><td>Thread safety</td><td>MT-Safe locale
</td></tr> <tr VALIGN=top><td> <b>lckpwdf</b>(), 
 <b>ulckpwdf</b>(), 
 <b>fgetspent_r</b>() </td><td>Thread safety</td><td>MT-Safe
</td></tr> </table> 

 In the above table, <i>getspent</i> in <i>race:getspent</i> signifies that if any of the functions <b>setspent</b>(), <b>getspent</b>(), <b>getspent_r</b>(), or <b>endspent</b>() are used in parallel in different threads of a program, then data races could occur.

<h2>CONFORMING TO</h2>

 The shadow password database and its associated API are not specified in POSIX.1. However, many other systems provide a similar API.

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/3-getgrnam/">getgrnam</a></b>(3), <b><a HREF="/docs/linux/man/3-getpwnam/">getpwnam</a></b>(3), <b><a HREF="/docs/linux/man/3-getpwnam_r/">getpwnam_r</a></b>(3), <b><a HREF="/docs/linux/man/5-shadow/">shadow</a></b>(5)

<h2>COLOPHON</h2>

 This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 

<h2>Index</h2>


