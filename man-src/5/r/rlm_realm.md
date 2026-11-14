---
title: "rlm_realm(5)"
name: "rlm_realm"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_realm/"
description: "rlm_realm – FreeRADIUS Module"
---

<p>rlm_realm &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_realm</i> module parses the User-Name attribute into a User section and a Realm section. This is used primarily in a proxy situation, however, Realms can also be used locally to provide different service profiles based on the Realm being used. </p>
<p> The main configuration items to be aware of are:</p>
<dl>
<dt>format</p>
<dd>This can be either &#8216;prefix&#8217; or &#8216;suffix&#8217;. It specifies whether the Realm is before or after the User portion in the User-Name string.</p>
<dt>delimiter</p>
<dd>A single character in quotes, which is used as the delimiting character that separates the Realm and User sections of the string.</p>
<dt>ignore_default</p>
<dd>This is set to either &#8216;yes&#8217; or &#8216;no&#8217;. If set to &#8216;yes&#8217;, this will prevent the module instance from matching a realm against the DEFAULT entry. This may be useful if you have multiple realm module instances. The default is &#8216;no&#8217;.</p>
<dt>ignore_null</p>
<dd>This is set to either &#8216;yes&#8217; or &#8216;no&#8217;. If set to &#8216;yes&#8217;, this will prevent the module instance from matching a realm against the NULL entry. This may be useful if you have multiple realm module instances. The default is &#8216;no&#8217;.</dl>
<p> This module parses the realm from the User-Name attrbiute according to the instance configuration, and then performs a lookup to find a matching realm in the &#8216;/etc/raddb/proxy.conf&#8217; file. Depending on the configuration of the Realm as matched in the file, the username may be rewritten in a &#8216;stripped&#8217; format, or with the Realm portion removed. In either case, a Realm attribute is created and added to the packet on a match, which can be used by other modules.</p>
<h2>Configuration</h2>
<dl>
<dd>
<pre>modules {
 ... stuff here ...
<br>
<br>
 # useranme [at] realm syntax
<br>
 realm suffix {
<br>
 format = suffix
<br>
 delimiter = &quot;@&quot;
<br>
 }
<br>
<br>
 # realm/username syntax
<br>
 realm prefix {
<br>
 format = prefix
<br>
 delimiter = &quot;/&quot;
<br>
 }
<br>
<br>
 ... stuff here ...
<br>
}</pre>
</dl>
<h2>Sections</h2>
<p><code>authorization,</code> <code>pre-accounting</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf,</i> <i>/etc/raddb/proxy.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5), <code><a href="/docs/linux/man/5-proxy-conf/">proxy.conf</a></code>(5)</p>
<h2>Authors</h2>
<p>Chris Parker, cparker [at] segv.org</p>
