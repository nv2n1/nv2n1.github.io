---
title: "pkcs11_inspect(1)"
name: "pkcs11_inspect"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcs11_inspect/"
description: "pkcs11_inspect – print certificate contents"
---

<h2>NAME</h2>
<p> pkcs11_inspect &#8211; print certificate contents</p>
<h2>SYNOPSIS</h2>
<p> <code>pkcs11_inspect</code> [<code>debug</code>] [<code>config_file=</code><i>&lt;filename&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pkcs11_inspect</code> uses the pam_pkcs11 library infrastructure to get the content of a certificate and display it. </p>
<p> <code>pkcs11_inspect</code> uses the same configuration file and arguments than <code><a href="/docs/linux/man/8-pam_pkcs11/">pam_pkcs11</a></code>(8) PAM module. It loads defined mapper modules, and use them to look into the certificate for required entries (ie: ms_mapper looks for ms UPN entries, and so on). </p>
<p> When a mapper module finds a proper entry in the certificate, it converts to UTF-8 and print it to stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>debug</code></p>
<dd> Enable debugging output.</p>
<dt><code>config_file=</code><i>&lt;filename&gt;</i></p>
<dd> Sets the configuration file to use. Default value is <i>/etc/pam_pkcs11/pam_pkcs11.conf</i>.</dl>
<p> As it uses the same configuration file as pam_pkcs11, all pam_pkcs11 options are also available. Note that some of them have no sense in a non-PAM environment, so they will be ignored. Some mapper options (mapfile, ignorecase) have no effect on certificate contents, so they will be ignored too.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>pkcs11_inspect</code> prints on stdout all certificate contents that are found for mappers and returns 0. </p>
<p> On error it returns 1.</p>
<h2>FILES</h2>
<p> <i>/etc/pam_pkcs11/pam_pkcs11.conf</i></p>
<h2>EXAMPLES</h2>
<p> To run this program the standard way, insert a smart card in the reader and type: </p>
<p>&nbsp;<wbr>pkcs11_inspect </p>
<p> Alternatively you can specify options: </p>
<p>&nbsp;<wbr>pkcs11_inspect debug config_file=${HOME}/.pam_pkcs11.conf</p>
<h2>AUTHORS</h2>
<p> Juan Antonio Martinez &lt;jonsito [at] teleline.es&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pam_pkcs11/">pam_pkcs11</a></code>(8), <code><a href="/docs/linux/man/1-pklogin_finder/">pklogin_finder</a></code>(1)<br />
 PAM-PKCS11 User Manual </p>
<h2>Index</h2>
