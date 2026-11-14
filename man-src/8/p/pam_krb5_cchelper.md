---
title: "pam_krb5_cchelper(8)"
name: "pam_krb5_cchelper"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_krb5_cchelper/"
description: "//usr/$LIB/security/pam_krb5/pam_krb5_cchelper – Credential cache helper"
---

<p>//usr/$LIB/security/pam_krb5/pam_krb5_cchelper &#8211; Credential cache helper</p>
<h2>Synopsis</h2>
<p><code>pam_krb5_cchelper [-c|-u|-d] [ccname] [uid] [gid]</code> </p>
<h2>Description</h2>
<p>The pam_krb5.so module uses pam_krb5_cchelper to create, update, and remove credential caches. </p>
<h2>Arguments</h2>
<dl>
<dt>-c|-u|-d</p>
<dd>A flag indicating whether the helper is expected to create, update, or destroy a ccache. When creating a ccache, the <i>ccname</i> argument should be a name or a pattern ending in XXXXXX. When updating or deleting a ccache, the <i>ccname</i> argument should be the name of an extant ccache. </p>
<dt>ccname</p>
<dd>A credential cache name or name pattern of the form <i>TYPE</i>:<i>/tmp/foo or TYPE</i>:<i>/tmp/fooXXXXXX</i>. </p>
<dt>uid</p>
<dd>An optional numeric UID which the helper will attempt to switch to before creating a ccache. The helper continues in its task if the attempt fails. </p>
<dt>gid</p>
<dd>An optional numeric GID which the helper will attempt to switch to before creating a ccache. The helper continues in its task if the attempt fails. </p>
</dl>
<h2>Operation</h2>
<p>The helper will read contents from its standard input.<br />
 If input of suitable length is not read, the specified credential cache is deleted.<br />
 If input of suitable length is read, a temporary file is created and the input is stored to the file. If TYPE is FILE, the file&#8217;s name will be based on the pattern and the name of this new credential cache will be printed. If TYPE is not FILE, a new credential cache will be created and the contents of the temporary file will be treated as a credential cache whose contents will be copied into the new credential cache, whose name will be printed.</p>
<h2>Files</h2>
<p><i>//usr/$LIB/security/pam_krb5.so</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) <code><a href="/docs/linux/man/5-pam_krb5/">pam_krb5</a></code>(5) <code><a href="/docs/linux/man/8-pam_krb5/">pam_krb5</a></code>(8) </p>
<h2>Bugs</h2>
<p>Probably, but let&#8217;s hope not. If you find any, please file them in the bug database at <a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a> against the &quot;pam_krb5&quot; component. </p>
<h2>Author</h2>
<p>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;</p>
