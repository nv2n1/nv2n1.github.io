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
<dt> &#8211;<code>-ccache= </code><i>string</i></p>
<dd>
<dd>credential cache</p>
<dt> &#8211;<code>-version</code></p>
<dd>
<dd>print version</p>
<dt> &#8211;<code>-help</code></p>
<dd></dl>
<dd>Available commands are:</p>
<dl>
<dt><code> digest-probe</code> [-<code>-realm= </code><i>string</i> ] [-<code>h | &#8211;help</code> ]</p>
<dd>
<dl>
<dt> &#8211;<code>-realm= </code><i>string</i></p>
<dd>
<dd>Kerberos realm to communicate with</dl>
<dt><code> digest-server-init</code> [-<code>-type= </code><i>string</i> ] [-<code>-kerberos-realm= </code><i>realm</i> ] [-<code>-digest= </code><i>digest-type</i> ] [-<code>-cb-type= </code><i>type</i> ] [-<code>-cb-value= </code><i>value</i> ] [-<code>-hostname= </code><i>hostname</i> ] [-<code>-realm= </code><i>string</i> ]</p>
<dd>
<dl>
<dt> &#8211;<code>-type= </code><i>string</i></p>
<dd>
<dd>digest type</p>
<dt> &#8211;<code>-kerberos-realm= </code><i>realm</i></p>
<dd>
<dt> &#8211;<code>-digest= </code><i>digest-type</i></p>
<dd>
<dd>digest type to use in the algorithm</p>
<dt> &#8211;<code>-cb-type= </code><i>type</i></p>
<dd>
<dd>type of channel bindings</p>
<dt> &#8211;<code>-cb-value= </code><i>value</i></p>
<dd>
<dd>value of channel bindings</p>
<dt> &#8211;<code>-hostname= </code><i>hostname</i></p>
<dd>
<dd>hostname of the server</p>
<dt> &#8211;<code>-realm= </code><i>string</i></p>
<dd>
<dd>Kerberos realm to communicate with</dl>
<dt><code> digest-server-request</code> [-<code>-type= </code><i>string</i> ] [-<code>-kerberos-realm= </code><i>realm</i> ] [-<code>-username= </code><i>name</i> ] [-<code>-server-nonce= </code><i>nonce</i> ] [-<code>-server-identifier= </code><i>nonce</i> ] [-<code>-client-nonce= </code><i>nonce</i> ] [-<code>-client-response= </code><i>response</i> ] [-<code>-opaque= </code><i>string</i> ] [-<code>-authentication-name= </code><i>name</i> ] [-<code>-realm= </code><i>realm</i> ] [-<code>-method= </code><i>method</i> ] [-<code>-uri= </code><i>uri</i> ] [-<code>-nounce-count= </code><i>count</i> ] [-<code>-qop= </code><i>qop</i> ] [-<code>-ccache= </code><i>ccache</i> ]</p>
<dd>
<dl>
<dt> &#8211;<code>-type= </code><i>string</i></p>
<dd>
<dd>digest type</p>
<dt> &#8211;<code>-kerberos-realm= </code><i>realm</i></p>
<dd>
<dt> &#8211;<code>-username= </code><i>name</i></p>
<dd>
<dd>digest type</p>
<dt> &#8211;<code>-server-nonce= </code><i>nonce</i></p>
<dd>
<dt> &#8211;<code>-server-identifier= </code><i>nonce</i></p>
<dd>
<dt> &#8211;<code>-client-nonce= </code><i>nonce</i></p>
<dd>
<dt> &#8211;<code>-client-response= </code><i>response</i></p>
<dd>
<dt> &#8211;<code>-opaque= </code><i>string</i></p>
<dd>
<dt> &#8211;<code>-authentication-name= </code><i>name</i></p>
<dd>
<dt> &#8211;<code>-realm= </code><i>realm</i></p>
<dd>
<dt> &#8211;<code>-method= </code><i>method</i></p>
<dd>
<dt> &#8211;<code>-uri= </code><i>uri</i></p>
<dd>
<dt> &#8211;<code>-nounce-count= </code><i>count</i></p>
<dd>
<dt> &#8211;<code>-qop= </code><i>qop</i></p>
<dd>
<dt> &#8211;<code>-ccache= </code><i>ccache</i></p>
<dd>
<dd>Where the the credential cache is created when the KDC returns tickets</dl>
<dt><code> digest-client-request</code> [-<code>-type= </code><i>string</i> ] [-<code>-username= </code><i>name</i> ] [-<code>-password= </code><i>password</i> ] [-<code>-server-nonce= </code><i>nonce</i> ] [-<code>-server-identifier= </code><i>nonce</i> ] [-<code>-client-nonce= </code><i>nonce</i> ] [-<code>-opaque= </code><i>string</i> ] [-<code>-realm= </code><i>realm</i> ] [-<code>-method= </code><i>method</i> ] [-<code>-uri= </code><i>uri</i> ] [-<code>-nounce-count= </code><i>count</i> ] [-<code>-qop= </code><i>qop</i> ]</p>
<dd>
<dl>
<dt> &#8211;<code>-type= </code><i>string</i></p>
<dd>
<dd>digest type</p>
<dt> &#8211;<code>-username= </code><i>name</i></p>
<dd>
<dd>digest type</p>
<dt> &#8211;<code>-password= </code><i>password</i></p>
<dd>
<dt> &#8211;<code>-server-nonce= </code><i>nonce</i></p>
<dd>
<dt> &#8211;<code>-server-identifier= </code><i>nonce</i></p>
<dd>
<dt> &#8211;<code>-client-nonce= </code><i>nonce</i></p>
<dd>
<dt> &#8211;<code>-opaque= </code><i>string</i></p>
<dd>
<dt> &#8211;<code>-realm= </code><i>realm</i></p>
<dd>
<dt> &#8211;<code>-method= </code><i>method</i></p>
<dd>
<dt> &#8211;<code>-uri= </code><i>uri</i></p>
<dd>
<dt> &#8211;<code>-nounce-count= </code><i>count</i></p>
<dd>
<dt> &#8211;<code>-qop= </code><i>qop</i></p>
<dd></dl>
<dt><code> ntlm-server-init</code> [-<code>-version= </code><i>integer</i> ] [-<code>-kerberos-realm= </code><i>string</i> ]</p>
<dd>
<dl>
<dt> &#8211;<code>-version= </code><i>integer</i></p>
<dd>
<dd>ntlm version</p>
<dt> &#8211;<code>-kerberos-realm= </code><i>string</i></p>
<dd>
<dd>Kerberos realm to communicate with</dl>
