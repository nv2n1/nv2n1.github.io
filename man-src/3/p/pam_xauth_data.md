---
title: "pam_xauth_data(3)"
name: "pam_xauth_data"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_xauth_data/"
description: "pam_xauth_data – structure containing X authentication data"
---

<p>pam_xauth_data &#8211; structure containing X authentication data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;
struct pam_xauth_data {
    int namelen;
    char *name;
    int datalen;
    char *data;
};</code></pre>
<h2>Description</h2>
<p>The <code>pam_xauth_data</code> structure contains X authentication data used to make a connection to an X display. Using this mechanism, an application can communicate X authentication data to PAM service modules. This allows modules to make a connection to the user&#8217;s X display in order to label the user&#8217;s session on login, display visual feedback or for other purposes. </p>
<p> The <i>name</i> field contains the name of the authentication method, such as &quot;MIT-MAGIC-COOKIE-1&quot;. The <i>namelen</i> field contains the length of this string, not including the trailing NUL character. </p>
<p> The <i>data</i> field contains the authentication method-specific data corresponding to the specified name. The <i>datalen</i> field contains its length in bytes. </p>
<p> The X authentication data can be changed with the <i>PAM_XAUTH_DATA</i> item. It can be queried and set with <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3) and <code>pam_set_item </code>(3) respectively. The value used to set it should be a pointer to a pam_xauth_data structure. An internal copy of both the structure itself and its fields is made by PAM when setting the item.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3),</p>
<h2>Standards</h2>
<p>The <code>pam_xauth_data</code> structure and <i>PAM_XAUTH_DATA</i> item are Linux-PAM extensions.</p>
