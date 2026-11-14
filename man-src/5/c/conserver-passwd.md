---
title: "conserver-passwd(5)"
name: "conserver-passwd"
section: "5"
letter: "c"
url: "/docs/linux/man/5-conserver-passwd/"
description: "conserver.passwd – user access information for conserver(8)"
---

<p>conserver.passwd &#8211; user access information for <code><a href="/docs/linux/man/8-conserver/">conserver</a></code>(8)</p>
<h2>Synopsis</h2>
<p><i>username</i><code>:</code><i>password</i></p>
<h2>Description</h2>
<p>The <code>conserver.passwd</code> file is the user authentication and authorization file for <code><a href="/docs/linux/man/8-conserver/">conserver</a></code>(8). Upon each incoming client connection, <code>conserver</code> opens and reads the <code>conserver.passwd</code> file, so edits to the file take effect immediately. It reads only until the first <i>username</i> match. </p>
<p> Blank lines and comment lines (those beginning with a &#8220;#&#8221; and optional leading whitespace) are ignored. Non-ignored lines beginning with whitespace are considered continuations of the previous line. This allows you to span one logical line over many physical lines and insert comments wherever appropriate. </p>
<p> Each logical line consists of two colon-separated fields. Leading and trailing white space in each field is ignored.</p>
<dl>
<dt><i>username</i></p>
<dd>the login name of the authorized user, or the string &#8220;<code>*any*</code>&#8221; to match any user. This is compared against the name sent by the <code>console</code> client, based either on the user&#8217;s identity or on the <code>-l option.</code> Since <code>conserver</code> only uses the first <i>username</i> match, a &#8220;<code>*any*</code>&#8221; entry will apply to any user without an entry earlier in the file.</p>
<dt><i>password</i></p>
<dd>the encrypted password, or the string &#8220;<code>*passwd*</code>&#8221; to indicate that <code>conserver</code> should look up the user&#8217;s password in the system <code>passwd</code> (or <code>shadow</code>) database. If PAM support has been enabled (<code>&#8211;with-pam</code>), PAM lookups will be done instead of <code>passwd</code> (or <code>shadow</code>) lookups (you may need to edit /etc/pam.conf or create /etc/pam.d/conserver). If this field is empty, password checking is bypassed for this user.</dl>
<h2>Example</h2>
<dl>
<dt><code>mary:r71mXjfALB5Ak</code></p>
<dd>Mary uses the password specified above; it does not matter whether she has a login on the conserver host.</p>
<dt><code>fred:*passwd*</code></p>
<dd>Fred may connect only with his regular login password on the conserver host.</p>
<dt><code>bozo:*</code></p>
<dd>Bozo is only allowed to access a console if his password isn&#8217;t used (since it&#8217;s invalid) which means he needs to come from a <code>trusted</code> host.</p>
<dt><code>*any*:*passwd*</code></p>
<dd>Anyone not listed above uses their regular login and password.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-console/">console</a></code>(1), <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5), <code><a href="/docs/linux/man/8-conserver/">conserver</a></code>(8)</p>
<h2>Bugs</h2>
<p>There is currently no way provided by the conserver package to generate the encrypted password strings besides copying them from the system <code>passwd</code> database or running <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) via C or perl or some other language that supports it. </p>
