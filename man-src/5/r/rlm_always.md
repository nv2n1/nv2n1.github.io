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
<dt>rcode</p>
<dd>This module will always return with the rcode specified. The default, if none specified is: fail (RLM_MODULE_FAIL).</dl>
<p> The valid options are:</p>
<dl>
<dt>reject</p>
<dd>RLM_MODULE_REJECT</p>
<dt>fail</p>
<dd>RLM_MODULE_FAIL</p>
<dt>ok</p>
<dd>RLM_MODULE_OK</p>
<dt>handled</p>
<dd>RLM_MODULE_HANDLED</p>
<dt>invalid</p>
<dd>RLM_MODULE_INVALID</p>
<dt>userlock</p>
<dd>RLM_MODULE_USERLOCK</p>
<dt>notfound</p>
<dd>RLM_MODULE_NOTFOUND</p>
<dt>noop</p>
<dd>RLM_MODULE_NOOP</p>
<dt>updated</p>
<dd>RLM_MODULE_UPDATED</dl>
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
</dl>
<h2>Sections</h2>
<p><code>authorization,</code> <code>authentication,</code> <code>postauthentication,</code> <code>preaccounting,</code> <code>accounting,</code> <code>preproxy,</code> <code>postproxy</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Chris Parker, cparker [at] segv.org</p>
