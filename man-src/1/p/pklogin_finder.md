---
title: "pklogin_finder(1)"
name: "pklogin_finder"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pklogin_finder/"
description: "pklogin_finder – maps certificates into a user"
---

<h2>NAME</h2>
<p> pklogin_finder &#8211; maps certificates into a user</p>
<h2>SYNTAX</h2>
<p> <code>pklogin_finder</code> [<code>debug</code>] [<code>config_file=</code><i>&lt;filename&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pklogin_finder</code> uses the pam_pkcs11 library infrastructure to interactively map a PKCS#11 provided certificate to a user. </p>
<p> <code>pklogin_finder</code> uses the the same configuration file and arguments than <code><a href="/docs/linux/man/8-pam_pkcs11/">pam_pkcs11</a></code>(8) PAM module. Load defined mapper modules, and try to find a map between found certificates and a user login.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>debug </code></p>
<dd> Enable debugging output. Default is no debug.</p>
<dt><code>config_file=</code><i>&lt;configuration file&gt;</i></p>
<dd> Sets the configuration file to use. Default value is <i>/etc/pam_pkcs11/pam_pkcs11.conf</i>.</dl>
<p> As it uses the same configuration file than pam_pkcs11, all pam_pkcs11 options are also available. Note that some of them has no sense in a non-PAM environment, so they will be ignored.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>pklogin_finder</code> prints on stdout the login name and exits returns 0. </p>
<p> On user mapping error it returns 1. </p>
<p> On no user match it prints nothing and returns 2.</p>
<h2>FILES</h2>
<p> <i>/etc/pam_pkcs11/pam_pkcs11.conf</i></p>
<h2>EXAMPLES</h2>
<p> To run this program the standard way, insert a smart card into the reader and type:<br />
&nbsp;<wbr>pklogin_finder&nbsp;<wbr> </p>
<p> Alternatively you can specify options:<br />
&nbsp;<wbr>pklogin_finder debug config_file=${HOME}/.pam_pkcs11.conf</p>
<h2>AUTHORS</h2>
<p> Juan Antonio Martinez &lt;jonsito [at] teleline.es&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pam_pkcs11/">pam_pkcs11</a></code>(8), <code><a href="/docs/linux/man/1-pkcs11_inspect/">pkcs11_inspect</a></code>(1), PAM-PKCS11 User Manual </p>
<h2>Index</h2>
