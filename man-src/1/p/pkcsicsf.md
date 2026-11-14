---
title: "pkcsicsf(1)"
name: "pkcsicsf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcsicsf/"
description: "pkcsicsf – configuration utility for the ICSF token"
---

<h2>NAME</h2>
<p> pkcsicsf &#8211; configuration utility for the ICSF token </p>
<h2>SYNOPSIS</h2>
<p> <code>pkcsicsf</code> [<code>-h</code>] [<code>-l|-a</code> <i>token name</i>] [<code>-b</code> <i>BINDDN</i>] [<code>-c</code> <i>client-cert-file</i>] [<code>-C</code> <i>CA-cert-file</i>] [<code>-k</code> <i>privatekey</i>] [<code>-m</code> <i>mechanism</i>] [<code>-u</code> <i>URI</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>pkcsicsf</code> utility lists available ICSF tokens and allows user to add one specific ICSF token to opencryptoki. </p>
<p> The ICSF token must be added first to opencryptoki. This creates an entry in the opencryptoki.conf file for the ICSF token. It also creates<br />
&nbsp;<wbr>a&nbsp;<wbr><i>token_name.conf</i>&nbsp;<wbr>configuration file in the same directory as the opencryptoki.conf file, containing ICSF specific information. This information is read by the ICSF token. </p>
<p> The ICSF token must bind and authenticate to an LDAP server. The supported authentication mechanisms are simple and sasl. One of these mechanisms must be entered when listing the available ICSF tokens or when adding an ICSF token. Opencryptoki currently supports adding only one ICSF token. </p>
<p> The system admin can either allow the ldap calls to utilize exisiting ldap configs, such as ldap.conf or .ldaprc for bind and authentication information or set the bind and authentication information within opencryptoki by using this utility and its options. The information will then be placed in the <i>token_name.conf</i> file to be used in the ldap calls. When using simple authentication, the user will be prompted for the racf password when listing or adding a token. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> <i>token name</i></p>
<dd> add the specified ICSF token to opencryptoki.</p>
<dt><code>-b</code> <i>BINDND</i></p>
<dd> the distinguish name to bind when using simple authentication</p>
<dt><code>-c</code> <i>client-cert-file</p>
<dd> the client certificate file when using SASL authentication</p>
<dt></i><code>-C</code> <i>CA-cert-file</i></p>
<dd> the CA certificate file when using SASL authentication</p>
<dt><code>-h</code></p>
<dd> show usage information</p>
<dt><code>-k</code> <i>privatekey</i></p>
<dd> the client private key file when using SASL authentication</p>
<dt><code>-m</code> <i>mechanism</i></p>
<dd> the authentication mechanism to use when binding to the LDAP server (this should be either <code>simple</code> or <code>sasl</code>)</p>
<dt><code>-l</code></p>
<dd> list available ICSF tokens</p>
<dt><code>-h</code></p>
<dd> show usage information </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/opencryptoki/opencryptoki.conf</p>
<dd> the opencryptoki config file containing token configuration information</p>
<dt>/etc/opencryptoki/<i>token_name.conf</i></p>
<dd> contains ICSF configuration information for the ICSF token </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-opencryptoki/">opencryptoki</a></code>(7),</p>
<dd>
<dt><code><a href="/docs/linux/man/8-pkcsslotd/">pkcsslotd</a></code>(8).</p>
<dd>
<dt><code><a href="/docs/linux/man/8-pkcsconf/">pkcsconf</a></code>(8).</p>
<dd>
</dl>
<h2>Index</h2>
