---
title: "krb5_ccache_intro(3)"
name: "krb5_ccache_intro"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_ccache_intro/"
---

<h2 class="name">NAME</h2>
 

 krb5_ccache_intro - The credential cache functions

<h2>Kerberos credential caches</h2>

 

 krb5_ccache structure holds a Kerberos credential cache. 

 Heimdal support the follow types of credential caches: 

<dl>
<dt>&bull;
<dd> SCC Store the credential in a database
<dt>&bull;
<dd> FILE Store the credential in memory
<dt>&bull;
<dd> MEMORY Store the credential in memory
<dt>&bull;
<dd> API A credential cache server based solution for Mac OS X
<dt>&bull;
<dd> KCM A credential cache server based solution for all platforms</dl>
 

<h3>Example</h3>

 This is a minimalistic version of klist: 

 <pre><code>
#include &lt;krb5.h&gt;
int main(int argc, char **argv)
{
    krb5_context context;
    krb5_cc_cursor cursor;
    krb5_error_code ret;
    krb5_ccache id;
    krb5_creds creds;
    if (krb5_init_context(&amp;context) != 0)
        errx(1, "krb5_context");
    ret = krb5_cc_default(context, &amp;id);
    if (ret)
        krb5_err(context, 1, ret, "krb5_cc_default");
    ret = krb5_cc_start_seq_get(context, id, &amp;cursor);
    if (ret)
        krb5_err(context, 1, ret, "krb5_cc_start_seq_get");
    while ((ret = krb5_cc_next_cred(context, id, &amp;cursor, &amp;creds)) == 0) {
        char *principal;
        krb5_unparse_name(context, creds.server, &amp;principal);
        printf("principal: %s\n", principal);
        free(principal);
        krb5_free_cred_contents(context, &amp;creds);
    }
    ret = krb5_cc_end_seq_get(context, id, &amp;cursor);
    if (ret)
        krb5_err(context, 1, ret, "krb5_cc_end_seq_get");
    krb5_cc_close(context, id);
    krb5_free_context(context);
    return 0;
}
*
</code></pre> 

 
&nbsp;<wbr> 

<h2>Index</h2>


