---
title: "pam(7)"
name: "pam"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pam/"
description: "PAM, pam – Pluggable Authentication Modules for Linux"
---

<p>PAM, pam &#8211; Pluggable Authentication Modules for Linux</p>
<h2>Description</h2>
<p>This manual is intended to offer a quick introduction to <code>Linux-PAM</code>. For more information the reader is directed to the <code>Linux-PAM system administrators&#8217; guide</code>. </p>
<p> <code>Linux-PAM</code> is a system of libraries that handle the authentication tasks of applications (services) on the system. The library provides a stable general interface (Application Programming Interface &#8211; API) that privilege granting programs (such as <code><a href="/docs/linux/man/1-login/">login</a></code>(1) and <code><a href="/docs/linux/man/1-su/">su</a></code>(1)) defer to to perform standard authentication tasks. </p>
<p> The principal feature of the PAM approach is that the nature of the authentication is dynamically configurable. In other words, the system administrator is free to choose how individual service-providing applications will authenticate users. This dynamic configuration is set by the contents of the single <code>Linux-PAM</code> configuration file /etc/pam.conf. Alternatively, the configuration can be set by individual configuration files located in the /etc/pam.d/ directory. The presence of this directory will cause <code>Linux-PAM</code> to <i>ignore</i> /etc/pam.conf. </p>
<p> Vendor-supplied PAM configuration files might be installed in the system directory /usr/lib/pam.d/ or a configurable vendor specific directory instead of the machine configuration directory /etc/pam.d/. If no machine configuration file is found, the vendor-supplied file is used. All files in /etc/pam.d/ override files with the same name in other directories. </p>
<p> From the point of view of the system administrator, for whom this manual is provided, it is not of primary importance to understand the internal behavior of the <code>Linux-PAM</code> library. The important point to recognize is that the configuration file(s) <i>define</i> the connection between applications (<code>services</code>) and the pluggable authentication modules (<code>PAM</code>s) that perform the actual authentication tasks. </p>
<p> <code>Linux-PAM</code> separates the tasks of <i>authentication</i> into four independent management groups: <code>account</code> management; <code>auth</code>entication management; <code>password</code> management; and <code>session</code> management. (We highlight the abbreviations used for these groups in the configuration file.) </p>
<p> Simply put, these groups take care of different aspects of a typical user&#8217;s request for a restricted service: </p>
<p> <code>account</code> &#8211; provide account verification types of service: has the user&#8217;s password expired?; is this user permitted access to the requested service? </p>
<p> <code>auth</code>entication &#8211; authenticate a user and set up user credentials. Typically this is via some challenge-response request that the user must satisfy: if you are who you claim to be please enter your password. Not all authentications are of this type, there exist hardware based authentication schemes (such as the use of smart-cards and biometric devices), with suitable modules, these may be substituted seamlessly for more standard approaches to authentication &#8211; such is the flexibility of <code>Linux-PAM</code>. </p>
<p> <code>password</code> &#8211; this group&#8217;s responsibility is the task of updating authentication mechanisms. Typically, such services are strongly coupled to those of the <code>auth</code> group. Some authentication mechanisms lend themselves well to being updated with such a function. Standard UN*X password-based access is the obvious example: please enter a replacement password. </p>
<p> <code>session</code> &#8211; this group of tasks cover things that should be done prior to a service being given and after it is withdrawn. Such tasks include the maintenance of audit trails and the mounting of the user&#8217;s home directory. The <code>session</code> management group is important as it provides both an opening and closing hook for modules to affect the services available to a user.</p>
<h2>Files</h2>
<p>/etc/pam.conf</p>
<dl>
<dd>the configuration file</dl>
<p> /etc/pam.d</p>
<dl>
<dd>the <code>Linux-PAM</code> configuration directory. Generally, if this directory is present, the /etc/pam.conf file is ignored.</dl>
<p> /usr/lib/pam.d</p>
<dl>
<dd>the <code>Linux-PAM</code> vendor configuration directory. Files in /etc/pam.d override files with the same name in this directory.</dl>
<p> &lt;vendordir&gt;/pam.d</p>
<dl>
<dd>the <code>Linux-PAM</code> vendor configuration directory. Files in /etc/pam.d and /usr/lib/pam.d override files with the same name in this directory. Only available if Linux-PAM was compiled with vendordir enabled.</dl>
<h2>Errors</h2>
<p>Typically errors generated by the <code>Linux-PAM</code> system of libraries, will be written to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>Conforming To</h2>
<p>DCE-RFC 86.0, October 1995. Contains additional features, but remains backwardly compatible with this RFC.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam/">pam</a></code>(3), <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3), <code><a href="/docs/linux/man/3-pam_sm_setcred/">pam_sm_setcred</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/7-pam/">PAM</a></code>(7) </p>
