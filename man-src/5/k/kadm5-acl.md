---
title: "kadm5-acl(5)"
name: "kadm5-acl"
section: "5"
letter: "k"
url: "/docs/linux/man/5-kadm5-acl/"
description: "kadm5.acl – Kerberos ACL file"
---

<p>kadm5.acl &#8211; Kerberos ACL file</p>
<h2>Description</h2>
<p>The Kerberos <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> daemon uses an Access Control List (ACL) file to manage access rights to the Kerberos database. For operations that affect principals, the ACL file also controls which principals can operate on which other principals. </p>
<p> The default location of the Kerberos ACL file is <code>/var/kerberos</code><code>/krb5kdc</code><code>/kadm5.acl</code> unless this is overridden by the <i>acl_file</i> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</p>
<h2>Syntax</h2>
<p>Empty lines and lines starting with the sharp sign (<code>#</code>) are ignored. Lines containing ACL entries have the format: </p>
<pre>principal permissions [target_principal [restrictions] ]</pre>
<p><code>NOTE:</code> Line order in the ACL file is important. The first matching entry will control access for an actor principal on a target principal.</p>
<dl>
<dt><i>principal</i></p>
<dd>(Partially or fully qualified Kerberos principal name.) Specifies the principal whose permissions are to be set. </p>
<p> Each component of the name may be wildcarded using the <code>*</code> character.</p>
<dt><i>permissions</i></p>
<dd>Specifies what operations may or may not be performed by a <i>principal</i> matching a particular entry. This is a string of one or more of the following list of characters or their upper-case counterparts. If the character is <i>upper-case</i>, then the operation is disallowed. If the character is <i>lower-case</i>, then the operation is permitted. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> a </td>
<td> [Dis]allows the addition of principals or policies
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> c </td>
<td> [Dis]allows the changing of passwords for principals
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> d </td>
<td> [Dis]allows the deletion of principals or policies
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> i </td>
<td> [Dis]allows inquiries about principals or policies
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> l </td>
<td> [Dis]allows the listing of all principals or policies
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> m </td>
<td> [Dis]allows the modification of principals or policies
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> p </td>
<td> [Dis]allows the propagation of the principal database (used in <i>incr_db_prop</i>)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> s </td>
<td> [Dis]allows the explicit setting of the key for a principal
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> x </td>
<td> Short for admcilsp. All privileges
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> * </td>
<td> Same as x.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><i>target_principal</i></p>
<dd>(Optional. Partially or fully qualified Kerberos principal name.) Specifies the principal on which <i>permissions</i> may be applied. Each component of the name may be wildcarded using the <code>*</code> character. </p>
<p> <i>target_principal</i> can also include back-references to <i>principal</i>, in which <code>*number</code> matches the corresponding wildcard in <i>principal</i>.</p>
<dt><i>restrictions</i></p>
<dd>(Optional) A string of flags. Allowed restrictions are:</p>
<dt><code>{+|-}</code><i>flagname</i></p>
<dd>flag is forced to the indicated value. The permissible flags are the same as those for the <code>default_principal_flags</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</p>
<dt><i>-clearpolicy</i></p>
<dd>policy is forced to be empty.</p>
<dt><i>-policy pol</i></p>
<dd>policy is forced to be <i>pol</i>.</p>
<dt><code>-{</code><i>expire, pwexpire, maxlife, maxrenewlife</i>} <i>time</i></p>
<dd>(<i>getdate</i> string) associated value will be forced to MIN(<i>time</i>, requested value). </p>
<p> The above flags act as restrictions on any add or modify operation which is allowed due to that ACL line. </p>
<p> <code>WARNING:</code> If the kadmind ACL file is modified, the kadmind daemon needs to be restarted for changes to take effect.</dl>
<h2>Example</h2>
<p>Here is an example of a kadm5.acl file: </p>
<pre>*/admin [at] ATHENA.MIT.EDU * # line 1
joeadmin [at] ATHENA.MIT.EDU ADMCIL # line 2
joeadmin/*@ATHENA.MIT.EDU i */root [at] ATHENA.MIT.EDU # line 3
*/root [at] ATHENA.MIT.EDU ci *1@ATHENA.MIT.EDU # line 4
*/root [at] ATHENA.MIT.EDU l * # line 5
sms [at] ATHENA.MIT.EDU x * -maxlife 9h -postdateable # line 6</pre>
<p>(line 1) Any principal in the <code>ATHENA.MIT.EDU</code> realm with an <code>admin</code> instance has all administrative privileges. </p>
<p> (lines 1-3) The user <code>joeadmin</code> has all permissions with his <code>admin</code> instance, <code>joeadmin/admin [at] ATHENA.MIT.EDU</code> (matches line 1). He has no permissions at all with his null instance, <code>joeadmin [at] ATHENA.MIT.EDU</code> (matches line 2). His <code>root</code> and other non-<code>admin</code>, non-null instances (e.g., <code>extra</code> or <code>dbadmin</code>) have inquire permissions with any principal that has the instance <code>root</code> (matches line 3). </p>
<p> (line 4) Any <code>root</code> principal in <code>ATHENA.MIT.EDU</code> can inquire or change the password of their null instance, but not any other null instance. (Here, <code>*1</code> denotes a back-reference to the component matching the first wildcard in the actor principal.) </p>
<p> (line 5) Any <code>root</code> principal in <code>ATHENA.MIT.EDU</code> can generate the list of principals in the database, and the list of policies in the database. This line is separate from line 4, because list permission can only be granted globally, not to specific target principals. </p>
<p> (line 6) Finally, the Service Management System principal <code>sms [at] ATHENA.MIT.EDU</code> has all permissions, but any principal that it creates or modifies will not be able to get postdateable tickets or tickets with a life of longer than 9 hours.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>, <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
