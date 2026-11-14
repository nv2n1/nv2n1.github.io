---
title: "pam_set_data(3)"
name: "pam_set_data"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_set_data/"
description: "pam_set_data – set module internal data"
---

<p>pam_set_data &#8211; set module internal data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_modules.h&gt;

int pam_set_data(pam_handle_t *pamh, const char *module_data_name, void *data, void (*cleanup)(pam_handle_t *pamh, void *data, int error_status));</code></pre>
<h2>Description</h2>
<dd>The <code>pam_set_data</code> function associates a pointer to an object with the (hopefully) unique string <i>module_data_name</i> in the PAM context specified by the <i>pamh</i> argument. </p>
<p> PAM modules may be dynamically loadable objects. In general such files should not contain <i>static</i> variables. This function and its counterpart <code><a href="/docs/linux/man/3-pam_get_data/">pam_get_data</a></code>(3), provide a mechanism for a module to associate some data with the handle <i>pamh</i>. Typically a module will call the <code>pam_set_data</code> function to register some data under a (hopefully) unique <i>module_data_name</i>. The data is available for use by other modules too but <i>not</i> by an application. Since this functions stores only a pointer to the <i>data</i>, the module should not modify or free the content of it. </p>
<p> The function <code>cleanup()</code> is associated with the <i>data</i> and, if non-NULL, it is called when this data is over-written or following a call to <code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3). </p>
<p> The <i>error_status</i> argument is used to indicate to the module the sort of action it is to take in cleaning this data item. As an example, Kerberos creates a ticket file during the authentication phase, this file might be associated with a data item. When <code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3) is called by the module, the <i>error_status</i> carries the return value of the <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3) or other <i>libpam</i> function as appropriate. Based on this value the Kerberos module may choose to delete the ticket file (<i>authentication failure</i>) or leave it in place. </p>
<p> The <i>error_status</i> may have been logically OR&#8217;d with either of the following two values: </p>
<p> PAM_DATA_REPLACE</p>
<dl>
<dd>When a data item is being replaced (through a second call to <code>pam_set_data</code>) this mask is used. Otherwise, the call is assumed to be from <code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3).</dl>
<p> PAM_DATA_SILENT</p>
<dl>
<dd>Which indicates that the process would prefer to perform the <code>cleanup()</code> quietly. That is, discourages logging/messages to the user.</dl>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Data was successful stored.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>A NULL pointer was submitted as PAM handle or the function was called by an application.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_data/">pam_get_data</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) </p>
