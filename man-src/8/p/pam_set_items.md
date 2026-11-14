---
title: "pam_set_items(8)"
name: "pam_set_items"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_set_items/"
description: "pam_set_items – A PAM test module to set module-specific PAM items"
---

<p>pam_set_items &#8211; A PAM test module to set module-specific PAM items</p>
<h2>Synopsis</h2>
<p>pam_set_items.so</p>
<h2>Description</h2>
<p>PAM modules store data in PAM <i>items</i>. These items are only accessible from module context, not application context as they might include private data (PAM_AUTHTOK normally contains the password). But when testing PAM modules, it&#8217;s often nice to make sure a PAM module under test can retrieve data from the stack. The pam_set_items module makes this possible by reading environment variables and setting them as PAM items.</p>
<h2>Options</h2>
<p>None</p>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Example</h2>
<p>Consider an example that tests that pam_unix is able to read a provided password and doesn&#8217;t query on its own. The test service file would contain:</p>
<dl>
<dd>
<pre>auth required pam_set_items.so
auth required pam_unix.so</pre>
</dl>
<p> Then the test would put the item to the test environment with:</p>
<dl>
<dd>
<pre>setenv(&quot;PAM_AUTHTOK&quot;, &quot;secret&quot;);</pre>
</dl>
<p> Then run the PAM conversation. </p>
