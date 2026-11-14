---
title: "rlm_acct_unique(5)"
name: "rlm_acct_unique"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_acct_unique/"
description: "rlm_acct_unique – FreeRADIUS Module"
---

<p>rlm_acct_unique &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_acct_unique</i> module creates a unique accounting session Id. </p>
<p> Many NAS vendors have their equipment supply an Acct-Session-Id attribute which is not unique over reboots. This makes accounting difficult, as there will be many independent sessions with the same Acct-Session-Id attribute. This module uses the Acct-Session-Id attribute, along with other attributes in the request, to create a more unique session ID, called Acct-Unique-Session-Id. </p>
<p> The main configuration items to be aware of are:</p>
<dl>
<dt>key</p>
<dd>A list of the attributes used in calculating an MD5 hash which is used as the value for the unique session id.</dl>
<h2>Configuration</h2>
<dl>
<dd>
<pre>modules {
 ...
<br>
 acct_unique {
<br>
 key = &quot;User-Name, Acct-Session-Id, NAS-IP-Address, NAS-Port&quot;
<br>
 }
<br>
 ...
<br>
}
<br>
 ...
<br>
preacct {
 ...
<br>
 acct_unique
 ...
<br>
}</pre>
</dl>
<p> After generating the MD5 hash, the module adds it to the accounting request packet received from the client. It will look something like this in your detail file: </p>
<dl>
<dd>
<pre> Acct-Unique-Session-Id = &quot;c66ef57e480b9d26&quot;</pre>
</dl>
<p> NOTE: Any attribute you specify that is not found in the &#8216;dictionary&#8217; file will cause the server to fail and exit with an error. </p>
<p> NOTE: If you want the Acct-Unique-Session-Id of the Start and the Stop packet of a particular session to match, you must use values for the key that will stay the same for the Start and Stop. The above example is a good start. Adding &#8216;Acct-Session-Time&#8217;, for example, would cause a mismatch because that value is not the same on the Start and Stop accounting packets.</p>
<h2>Sections</h2>
<p><code>authorization,</code> <code>pre-accounting,</code> <code>accounting</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Authors</h2>
<p>Chris Parker, cparker [at] segv.org</p>
