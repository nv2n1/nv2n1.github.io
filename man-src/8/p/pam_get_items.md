---
title: "pam_get_items(8)"
name: "pam_get_items"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_get_items/"
description: "pam_get_items – A PAM test module to retrieve module-specific PAM items"
---

<p>pam_get_items &#8211; A PAM test module to retrieve module-specific PAM items</p>
<h2>Synopsis</h2>
<p>pam_get_items.so</p>
<h2>Description</h2>
<p>PAM modules store data in PAM <i>items</i>. These items are only accessible from module context, not application context as they might include private data (PAM_AUTHTOK normally contains the password). But when testing PAM modules, it&#8217;s often nice to make sure a PAM module under test sets items for the next module the way it&#8217;s supposed to. The pam_get_items module makes this possible by exporting all PAM items as environment variables using pam_putenv. The environment variable name is the same as the constant name of the PAM item.</p>
<h2>Options</h2>
<p>None</p>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Example</h2>
<p>Consider an example that tests that pam_unix puts the password it reads onto PAM stack. The test service file would contain:</p>
<dl>
<dd>
<pre>auth required pam_unix.so
auth required pam_get_items.so</pre>
</dl>
<p> Then the test would run the PAM conversation and afterwards call:</p>
<dl>
<dd>
<pre>pam_getenv(pamh, &quot;PAM_AUTHTOK&quot;);</pre>
</dl>
<p> To retrieve the password. </p>
