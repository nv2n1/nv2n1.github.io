---
title: "rlm_counter(5)"
name: "rlm_counter"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_counter/"
description: "rlm_counter – FreeRADIUS Module"
---

<p>rlm_counter &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_counter</i> module provides a general framework to allow access based on accumulated usage of a resource, such as total time online in a given period, total data transferred in a given period, etc. This is very useful in a &#8216;Prepaid Service&#8217; situation, where a user has paid for a finite amount of usage and should not be allowed to use more than that service. Collection, monitoring, and replenishment of prepaid services are beyond the scope of this module. </p>
<p> The main configuration items to be aware of are:</p>
<dl>
<dt>filename</p>
<dd>The filename where the usage data is stored.</p>
<dt>key</p>
<dd>An attribute which will be present in the Access-Request to be used as the &#8216;index&#8217; value for the counter. A counter entry is tracked for each unique key. The most likely key you will want to use is User-Name.</p>
<dt>count_attribute</p>
<dd>An attribute which will be used to increment the counter value. If this attribute is Acct-Session-Time or an integer value the counter data is incremented by the Attribute value. For all other attribute types the counter is incremented by one.</p>
<dt>reset</p>
<dd>How frequently the counter data should be set back to 0. Valid values for this variable are: <code>hourly,</code> <code>daily,</code> <code>weekly,</code> <code>monthly,</code> <code>or</code>never Alternatively, it can be user defined, in the form: num[hdwm]. num is a numeric value, followed by one or none of the following letters. h: hours, d: days, w: weeks, m: months.</p>
<dt>check_name</p>
<dd>This defines an attribute name which will be registered by the counter module and can be used to set the maximum allowed value for the counter after which the user is rejected. If Daily-Session-Time is set, you can use the following syntax in the Users file to set a cap of 3600 seconds ( 8 hours ):</dl>
<dl>
<dd>
<pre>DEFAULT Max-Daily-Session := 3600</pre>
</dl>
<dl>
<dt>reply_name</p>
<dd>This is the name of the attribute which will contain the remaining value for the counter in the reply packet when the user is successfully authorized. The default attribute name is &quot;Session-Timeout&quot;.</p>
<dt>allowed_service_type</p>
<dd>This can be used to only apply the limitations to specific service types of sessions. For example, setting this to Framed-User will only apply the counter module to Framed sessions, excluding other types such as Telnet or Rlogin.</p>
<dt>cache_size</p>
<dd>The maximum size of the cache to be used by the module. The default is 1000.</dl>
<h2>Notes</h2>
<p>This module registers an attribute, so it should be added to the instantiate section, to be called on server startup. When used in the authorize section, it must come after any modules which set the &#8216;check_name&#8217; attribute. </p>
<h2>Sections</h2>
<p><code>instantiate,</code> <code>authorize,</code> <code>accounting</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5) <code><a href="/docs/linux/man/5-rlm_sqlcounter/">rlm_sqlcounter</a></code>(5)</p>
<h2>Author</h2>
<p>Chris Parker, cparker [at] segv.org</p>
