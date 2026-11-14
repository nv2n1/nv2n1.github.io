---
title: "shadow(3)"
name: "shadow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-shadow/"
description: "shadow, getspnam – encrypted password file routines"
---

<p>shadow, getspnam &#8211; encrypted password file routines</p>
<h2>Syntax</h2>
<p><i>#include &lt;shadow.h&gt;</i> </p>
<p> <i>struct spwd *getspent();</i> </p>
<p> <i>struct spwd *getspnam(char</i><i>*name</i><i>);</i> </p>
<p> <i>void setspent();</i> </p>
<p> <i>void endspent();</i> </p>
<p> <i>struct spwd *fgetspent(FILE</i><i>*fp</i><i>);</i> </p>
<p> <i>struct spwd *sgetspent(char</i><i>*cp</i><i>);</i> </p>
<p> <i>int putspent(struct spwd</i><i>*p,</i><i>FILE</i><i>*fp</i><i>);</i> </p>
<p> <i>int lckpwdf();</i> </p>
<p> <i>int ulckpwdf();</i></p>
<h2>Description</h2>
<pre><code>shadow
    manipulates the contents of the shadow password file,
    / etc / shadow.The structure in the
#include
                file is : struct spwd {
    char *sp_namp;             /* user login name */
    char *sp_pwdp;             /* encrypted password */
    long int sp_lstchg;        /* last password change */
    long int sp_min;           /* days until change allowed. */
    long int sp_max;           /* days before change required */
    long int sp_warn;          /* days warning for expiration */
    long int sp_inact;         /* days before account inactive */
    long int sp_expire;        /* date when account expires */
    unsigned long int sp_flag; /* reserved for future use */
}</code></pre>
<p> The meanings of each field are:</p>
<dl>
<dd>&bull; sp_namp &#8211; pointer to null-terminated user name</dl>
<dl>
<dd>&bull; sp_pwdp &#8211; pointer to null-terminated password</dl>
<dl>
<dd>&bull; sp_lstchg &#8211; days since Jan 1, 1970 password was last changed</dl>
<dl>
<dd>&bull; sp_min &#8211; days before which password may not be changed</dl>
<dl>
<dd>&bull; sp_max &#8211; days after which password must be changed</dl>
<dl>
<dd>&bull; sp_warn &#8211; days before password is to expire that user is warned of pending password expiration</dl>
<dl>
<dd>&bull; sp_inact &#8211; days after password expires that account is considered inactive and disabled</dl>
<dl>
<dd>&bull; sp_expire &#8211; days since Jan 1, 1970 when account will be disabled</dl>
<dl>
<dd>&bull; sp_flag &#8211; reserved for future use</dl>
<h2>Description</h2>
<p><i>getspent</i>, <i>getspname</i>, <i>fgetspent</i>, and <i>sgetspent</i> each return a pointer to a <i>struct spwd</i>. <i>getspent</i> returns the next entry from the file, and <i>fgetspent</i> returns the next entry from the given stream, which is assumed to be a file of the proper format. <i>sgetspent</i> returns a pointer to a <i>struct spwd</i> using the provided string as input. <i>getspnam</i> searches from the current position in the file for an entry matching <i>name</i>. </p>
<p> <i>setspent</i> and <i>endspent</i> may be used to begin and end, respectively, access to the shadow password file. </p>
<p> The <i>lckpwdf</i> and <i>ulckpwdf</i> routines should be used to insure exclusive access to the /etc/shadow file. <i>lckpwdf</i> attempts to acquire a lock using <i>pw_lock</i> for up to 15 seconds. It continues by attempting to acquire a second lock using <i>spw_lock</i> for the remainder of the initial 15 seconds. Should either attempt fail after a total of 15 seconds, <i>lckpwdf</i> returns -1. When both locks are acquired 0 is returned.</p>
<h2>Diagnostics</h2>
<p>Routines return NULL if no more entries are available or if an error occurs during processing. Routines which have <i>int</i> as the return value return 0 for success and -1 for failure.</p>
<h2>Caveats</h2>
<p>These routines may only be used by the superuser as access to the shadow password file is restricted.</p>
<h2>Files</h2>
<p>/etc/shadow</p>
<dl>
<dd>Secure user account information.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5). </p>
