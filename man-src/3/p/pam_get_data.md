---
title: "pam_get_data(3)"
name: "pam_get_data"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_get_data/"
description: "pam_get_data – get module internal data"
---

<p>pam_get_data &#8211; get module internal data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_modules.h&gt;

int pam_get_data(const pam_handle_t *pamh, const char *module_data_name, const void **data);</code></pre>
<h2>Description</h2>
<dd>This function together with the <code><a href="/docs/linux/man/3-pam_set_data/">pam_set_data</a></code>(3) function is useful to manage module-specific data meaningful only to the calling PAM module. </p>
<p> The <code>pam_get_data</code> function looks up the object associated with the (hopefully) unique string <i>module_data_name</i> in the PAM context specified by the <i>pamh</i> argument. A successful call to <code>pam_get_data</code> will result in <i>data</i> pointing to the object. Note, this data is <i>not</i> a copy and should be treated as <i>constant</i> by the module.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>Data was successful retrieved.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>A NULL pointer was submitted as PAM handle or the function was called by an application.</dl>
<p> PAM_NO_MODULE_DATA</p>
<dl>
<dd>Module data not found or there is an entry, but it has the value NULL.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3), <code><a href="/docs/linux/man/3-pam_set_data/">pam_set_data</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) </p>
