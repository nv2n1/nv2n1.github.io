---
title: "pam_krb5_storetmp(8)"
name: "pam_krb5_storetmp"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_krb5_storetmp/"
description: "/$LIB/security/pam_krb5/pam_krb5_storetmp – Temporary file helper"
---

<p>/$LIB/security/pam_krb5/pam_krb5_storetmp &#8211; Temporary file helper</p>
<h2>Synopsis</h2>
<p><code>pam_krb5_storetmp pattern [uid] [gid]</code> </p>
<h2>Description</h2>
<p>The pam_krb5.so module uses pam_krb5_storetmp to create and remove temporary files. It is not intended for any other use. </p>
<h2>Arguments</h2>
<dl>
<dt>pattern</p>
<dd>A filename pattern of the form <i>/tmp/fooXXXXXX</i>. A temporary file will be created using <a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3) and any data provided to standard input will be piped to the file. Upon reading an end-of-file, the helper will print the name of the created file.<br />
 If the pattern does not end with the distinctive patterh <i>XXXXXX</i>, then the file is simply deleted. </p>
<dt>uid</p>
<dd>An optional numeric UID which the helper will attempt to switch to before creating the file. The helper continues in its task if the attempt fails. </p>
<dt>gid</p>
<dd>An optional numeric GID which the helper will attempt to switch to before creating the file. The helper continues in its task if the attempt fails. </p>
</dl>
<h2>Files</h2>
<p><i>/$LIB/security/pam_krb5.so</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) <code><a href="/docs/linux/man/5-pam_krb5/">pam_krb5</a></code>(5) <code><a href="/docs/linux/man/8-pam_krb5/">pam_krb5</a></code>(8) </p>
<h2>Bugs</h2>
<p>Probably, but let&#8217;s hope not. If you find any, please file them in the bug database at <a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a> against the &quot;pam_krb5&quot; component. </p>
<h2>Author</h2>
<p>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;</p>
