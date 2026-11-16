---
title: "kdigest(8)"
name: "kdigest"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kdigest/"
description: "kdigest – userland tool to access digest interface in the KDC"
---

<p><code>kdigest</code> &#8211; userland tool to access digest interface in the KDC</p>
<h2>Synopsis</h2>
<p>[-<code>-ccache= </code><i>string</i> ] [-<code>-version</code> ] [-<code>-help</code> ] command [arguments]</p>
<h2>Description</h2>
<p>Supported options:</p>
<dl>
<dt> &#8211;<code>-ccache= </code><i>string</i></dt>
<dd>
</dd><dd>credential cache</dd>
<dt> &#8211;<code>-version</code></dt>
<dd>
</dd><dd>print version</dd>
<dt> &#8211;<code>-help</code></dt>
<dd></dd></dl>
<dd>Available commands are:</dd>
<dl>
<dt><code> digest-probe</code> [-<code>-realm= </code><i>string</i> ] [-<code>h | &#8211;help</code> ]</dt>
<dd>
</dd><dl>
<dt> &#8211;<code>-realm= </code><i>string</i></dt>
<dd>
</dd><dd>Kerberos realm to communicate with</dd></dl>
<dt><code> digest-server-init</code> [-<code>-type= </code><i>string</i> ] [-<code>-kerberos-realm= </code><i>realm</i> ] [-<code>-digest= </code><i>digest-type</i> ] [-<code>-cb-type= </code><i>type</i> ] [-<code>-cb-value= </code><i>value</i> ] [-<code>-hostname= </code><i>hostname</i> ] [-<code>-realm= </code><i>string</i> ]</dt>
<dd>
</dd><dl>
<dt> &#8211;<code>-type= </code><i>string</i></dt>
<dd>
</dd><dd>digest type</dd>
<dt> &#8211;<code>-kerberos-realm= </code><i>realm</i></dt>
<dd>
</dd><dt> &#8211;<code>-digest= </code><i>digest-type</i></dt>
<dd>
</dd><dd>digest type to use in the algorithm</dd>
<dt> &#8211;<code>-cb-type= </code><i>type</i></dt>
<dd>
</dd><dd>type of channel bindings</dd>
<dt> &#8211;<code>-cb-value= </code><i>value</i></dt>
<dd>
</dd><dd>value of channel bindings</dd>
<dt> &#8211;<code>-hostname= </code><i>hostname</i></dt>
<dd>
</dd><dd>hostname of the server</dd>
<dt> &#8211;<code>-realm= </code><i>string</i></dt>
<dd>
</dd><dd>Kerberos realm to communicate with</dd></dl>
<dt><code> digest-server-request</code> [-<code>-type= </code><i>string</i> ] [-<code>-kerberos-realm= </code><i>realm</i> ] [-<code>-username= </code><i>name</i> ] [-<code>-server-nonce= </code><i>nonce</i> ] [-<code>-server-identifier= </code><i>nonce</i> ] [-<code>-client-nonce= </code><i>nonce</i> ] [-<code>-client-response= </code><i>response</i> ] [-<code>-opaque= </code><i>string</i> ] [-<code>-authentication-name= </code><i>name</i> ] [-<code>-realm= </code><i>realm</i> ] [-<code>-method= </code><i>method</i> ] [-<code>-uri= </code><i>uri</i> ] [-<code>-nounce-count= </code><i>count</i> ] [-<code>-qop= </code><i>qop</i> ] [-<code>-ccache= </code><i>ccache</i> ]</dt>
<dd>
</dd><dl>
<dt> &#8211;<code>-type= </code><i>string</i></dt>
<dd>
</dd><dd>digest type</dd>
<dt> &#8211;<code>-kerberos-realm= </code><i>realm</i></dt>
<dd>
</dd><dt> &#8211;<code>-username= </code><i>name</i></dt>
<dd>
</dd><dd>digest type</dd>
<dt> &#8211;<code>-server-nonce= </code><i>nonce</i></dt>
<dd>
</dd><dt> &#8211;<code>-server-identifier= </code><i>nonce</i></dt>
<dd>
</dd><dt> &#8211;<code>-client-nonce= </code><i>nonce</i></dt>
<dd>
</dd><dt> &#8211;<code>-client-response= </code><i>response</i></dt>
<dd>
</dd><dt> &#8211;<code>-opaque= </code><i>string</i></dt>
<dd>
</dd><dt> &#8211;<code>-authentication-name= </code><i>name</i></dt>
<dd>
</dd><dt> &#8211;<code>-realm= </code><i>realm</i></dt>
<dd>
</dd><dt> &#8211;<code>-method= </code><i>method</i></dt>
<dd>
</dd><dt> &#8211;<code>-uri= </code><i>uri</i></dt>
<dd>
</dd><dt> &#8211;<code>-nounce-count= </code><i>count</i></dt>
<dd>
</dd><dt> &#8211;<code>-qop= </code><i>qop</i></dt>
<dd>
</dd><dt> &#8211;<code>-ccache= </code><i>ccache</i></dt>
<dd>
</dd><dd>Where the the credential cache is created when the KDC returns tickets</dd></dl>
<dt><code> digest-client-request</code> [-<code>-type= </code><i>string</i> ] [-<code>-username= </code><i>name</i> ] [-<code>-password= </code><i>password</i> ] [-<code>-server-nonce= </code><i>nonce</i> ] [-<code>-server-identifier= </code><i>nonce</i> ] [-<code>-client-nonce= </code><i>nonce</i> ] [-<code>-opaque= </code><i>string</i> ] [-<code>-realm= </code><i>realm</i> ] [-<code>-method= </code><i>method</i> ] [-<code>-uri= </code><i>uri</i> ] [-<code>-nounce-count= </code><i>count</i> ] [-<code>-qop= </code><i>qop</i> ]</dt>
<dd>
</dd><dl>
<dt> &#8211;<code>-type= </code><i>string</i></dt>
<dd>
</dd><dd>digest type</dd>
<dt> &#8211;<code>-username= </code><i>name</i></dt>
<dd>
</dd><dd>digest type</dd>
<dt> &#8211;<code>-password= </code><i>password</i></dt>
<dd>
</dd><dt> &#8211;<code>-server-nonce= </code><i>nonce</i></dt>
<dd>
</dd><dt> &#8211;<code>-server-identifier= </code><i>nonce</i></dt>
<dd>
</dd><dt> &#8211;<code>-client-nonce= </code><i>nonce</i></dt>
<dd>
</dd><dt> &#8211;<code>-opaque= </code><i>string</i></dt>
<dd>
</dd><dt> &#8211;<code>-realm= </code><i>realm</i></dt>
<dd>
</dd><dt> &#8211;<code>-method= </code><i>method</i></dt>
<dd>
</dd><dt> &#8211;<code>-uri= </code><i>uri</i></dt>
<dd>
</dd><dt> &#8211;<code>-nounce-count= </code><i>count</i></dt>
<dd>
</dd><dt> &#8211;<code>-qop= </code><i>qop</i></dt>
<dd></dd></dl>
<dt><code> ntlm-server-init</code> [-<code>-version= </code><i>integer</i> ] [-<code>-kerberos-realm= </code><i>string</i> ]</dt>
<dd>
</dd><dl>
<dt> &#8211;<code>-version= </code><i>integer</i></dt>
<dd>
</dd><dd>ntlm version</dd>
<dt> &#8211;<code>-kerberos-realm= </code><i>string</i></dt>
<dd>
</dd><dd>Kerberos realm to communicate with</dd></dl>
</dl>