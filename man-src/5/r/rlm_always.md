---
title: "rlm_always(5)"
name: "rlm_always"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_always/"
description: "rlm_always – FreeRADIUS Module"
---

<p>rlm_always &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_always</i> module provides a simple way to &quot;always&quot; return a value during the processing of a configuration section. The module does nothing other than return a configured value. </p>
<p> The main configuration item to be aware of is:</p>
<dl>
<dt>rcode</dt>
<dd>This module will always return with the rcode specified. The default, if none specified is: fail (RLM_MODULE_FAIL).</dd></dl>
<p> The valid options are:</p>
<dl>
<dt>reject</dt>
<dd>RLM_MODULE_REJECT</dd>
<dt>fail</dt>
<dd>RLM_MODULE_FAIL</dd>
<dt>ok</dt>
<dd>RLM_MODULE_OK</dd>
<dt>handled</dt>
<dd>RLM_MODULE_HANDLED</dd>
<dt>invalid</dt>
<dd>RLM_MODULE_INVALID</dd>
<dt>userlock</dt>
<dd>RLM_MODULE_USERLOCK</dd>
<dt>notfound</dt>
<dd>RLM_MODULE_NOTFOUND</dd>
<dt>noop</dt>
<dd>RLM_MODULE_NOOP</dd>
<dt>updated</dt>
<dd>RLM_MODULE_UPDATED</dd></dl>
<h2>Configuration</h2>
<dl>
<dd>
<pre>modules {
 ...
<br>
 always ok {
<br>
 rcode = ok
<br>
 }
<br>
 ...
<br>
}
<br>
 ...
<br>
authorize {
 ...
<br>
 redundant {
 sql1 # try to find the user in sql1
<br>
 sql2 # try to find the user in sql2
<br>
 ok # if still not found, it's OK.
<br>
 }
 ...
<br>
}</pre>
</dd></dl>
<h2>Sections</h2>
<p><code>authorization,</code> <code>authentication,</code> <code>postauthentication,</code> <code>preaccounting,</code> <code>accounting,</code> <code>preproxy,</code> <code>postproxy</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Chris Parker, cparker [at] segv.org</p>
