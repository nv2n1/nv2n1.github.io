---
title: "pam_oddjob_mkhomedir(8)"
name: "pam_oddjob_mkhomedir"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_oddjob_mkhomedir/"
description: "pam_oddjob_mkhomedir.so – PAM module to create users home directory via oddjob"
---

<p>pam_oddjob_mkhomedir.so &#8211; PAM module to create users home directory via oddjob</p>
<h2>Synopsis</h2>
<p>session optional /lib/security/pam_oddjob_mkhomedir.so </p>
<h2>Description</h2>
<p>The <i>pam_oddjob_mkhomedir.so</i> module checks if the user&#8217;s home directory exists, and if it does not, it invokes the <i>mkhomedirfor</i> method of the <i>com.redhat.oddjob_mkhomedir</i> service for the <code>PAM_USER</code> if the module is running with superuser privileges. Otherwise, it invokes the <i>mkmyhomedir</i> method. The location of the skeleton directory and the default umask are determined by the configuration for the corresponding service in <code>oddjobd-mkhomedir.conf</code>, so they can not be specified as arguments to this module. If <i>D-Bus</i> has not been configured to allow the calling application to invoke these methods provided as part of the <i>com.redhat.oddjob_mkhomedir</i> interface of the <i>/</i> object provided by the <i>com.redhat.oddjob_mkhomedir</i> service, then <i>oddjobd</i> will not receive the request and an error will be returned by <i>D-Bus</i>. If <i>oddjobd</i> has not been configured to provide these methods, or the user is not authorized to use them, then <i>oddjobd</i> will ignore the module&#8217;s requests. </p>
<h2>Options</h2>
<p>The module takes no options. What <i>oddjobd</i> does in response to the module&#8217;s request is controlled by the daemon&#8217;s configuration file, typically <i>/etc/oddjobd.conf.d/oddjobd-mkhomedir.conf</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oddjob_request/">oddjob_request</a></code>(1) <code><a href="/docs/linux/man/5-oddjob-conf/">oddjob.conf</a></code>(5) <code><a href="/docs/linux/man/5-oddjobd-conf/">oddjobd.conf</a></code>(5) <code><a href="/docs/linux/man/8-oddjobd/">oddjobd</a></code>(8) </p>
