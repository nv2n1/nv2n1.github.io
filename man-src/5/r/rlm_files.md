---
title: "rlm_files(5)"
name: "rlm_files"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_files/"
description: "rlm_files – FreeRADIUS Module"
---

<p>rlm_files &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_files</i> module uses the &#8216;users&#8217; file for accessing authorization information for users. Additionally, it supports a &#8216;users&#8217; file syntax to be applied to the accounting and pre-proxy sections. </p>
<p> The main configuration items to be aware of are:</p>
<dl>
<dt>usersfile</p>
<dd>The filename of the &#8216;users&#8217; file, which is parsed during the authorization stage of this module.</p>
<dt>acctusersfile</p>
<dd>The filename of the &#8216;users&#8217; file, which is parsed during the accounting stage of this module.</p>
<dt>preproxy_usersfile</p>
<dd>The filename of the &#8216;users&#8217; file, which is parsed during the pre_proxy stage of this module.</p>
<dt>compat</p>
<dd>This option allows FreeRADIUS to parse an old style Cistron syntax. The default is &#8216;no&#8217;. If you need to parse an old style Cistron file, set this option to &#8216;cistron&#8217;.</p>
<dt>key</p>
<dd>This option lets you set the attribute to use as a key to find entries. The default is &quot;%{%{Stripped-User-Name}:-%{User-Name}}&quot;. Note that the key MUST supply real data. Dynamic attributes like &quot;Group&quot; will not work, because the &quot;Group&quot; attribute can only be used as a comparison, to see if a user is in a Unix group. It will not return the name of the Unix group that a user is in.</dl>
<p> If you want to use groups as a key, see the <i>rlm_passwd</i>, which will create a real attribute that contains the group name. </p>
<p> This configuration entry enables you to have configurations that perform per-group checks, and return per-group attributes, where the group membership is dynamically defined by a previous module. It also lets you do things like key off of attributes in the reply, and express policies like like &quot;when I send replies containing attribute FOO with value BAR, do more checks, and maybe send additional attributes&quot;.</p>
<h2>Configuration</h2>
<dl>
<dd>
<pre>modules {
 ... stuff here ...
<br>
 files {
<br>
 usersfile = %{confdir}/users
<br>
 acctusersfile = %{confdir}/acct_users
<br>
 preproxy_usersfile = %{confdir}/preproxy_users
<br>
 compat = no
<br>
 key = %{%{Stripped-User-Name}:-%{User-Name}}
<br>
 }
<br>
 ... stuff here ...
<br>
}</pre>
</dl>
<h2>Sections</h2>
<p><code>authorization,</code> <code>accounting,</code> <code>pre_proxy</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf,</i> <i>/etc/raddb/users,</i> <i>/etc/raddb/acct_users,</i> <i>/etc/raddb/preproxy_users</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5), <code><a href="/docs/linux/man/5-users/">users</a></code>(5)</p>
<h2>Authors</h2>
<p>Chris Parker, cparker [at] segv.org</p>
