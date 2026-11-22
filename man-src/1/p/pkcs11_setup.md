---

title: "pkcs11_setup(1)"
name: "pkcs11_setup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcs11_setup/"
description: "pkcs11_setup – SmartCard PKCS#11 setup"
---

<p> pkcs11_setup &#8211; SmartCard PKCS#11 setup</p>
<h2>SYNTAX</h2>
<p> pkcs11_setup [<code>list_modules</code>] [<code>debug</code>] [<code>use_module</code>[<i>=&lt;module_name&gt;</i>]] [<code>ins_action</code>[<i>=&lt;executable,executable,&#8230;&gt;</i>]] [<code>rm_action</code>[<i>=&lt;executable,executable,&#8230;&gt;</i>]]</p>
<h2>DESCRIPTION</h2>
<p> pkcs11_setup display all the certificates.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>debug </code></dt>
<dd> Enable debugging output.</dd>
<dt><code>list_modules</code></dt>
<dd> List the modules available and configured in <i>/etc/pam_pkcs11/pam_pkcs11.conf</i>.</dd>
<dt><code>use_module</code></dt>
<dd> Display the module used by pam_pkcs11.</dd></dl>
<h2>AUTHORS</h2>
<p> Juan Antonio Martinez &lt;jonsito [at] teleline.es&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-pam_pkcs11/">pam_pkcs11</a>(8)<br/>
 PAM-PKCS11 User Manual </p>
