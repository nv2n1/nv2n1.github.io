---
title: "pam_set_item(3)"
name: "pam_set_item"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_set_item/"
description: "pam_set_item – set and update PAM informations"
---

<p>pam_set_item &#8211; set and update PAM informations</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_modules.h&gt;

int pam_set_item(pam_handle_t *pamh, int item_type, const void *item);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_set_item</code> function allows applications and PAM service modules to access and to update PAM informations of <i>item_type</i>. For this a copy of the object pointed to by the <i>item</i> argument is created. The following <i>item_type</i>s are supported: </p>
<p> PAM_SERVICE</p>
<dl>
<dd>The service name (which identifies that PAM stack that the PAM functions will use to authenticate the program).</dl>
<p> PAM_USER</p>
<dl>
<dd>The username of the entity under whose identity service will be given. That is, following authentication, <i>PAM_USER</i> identifies the local entity that gets to use the service. Note, this value can be mapped from something (eg., &quot;anonymous&quot;) to something else (eg. &quot;guest119&quot;) by any module in the PAM stack. As such an application should consult the value of <i>PAM_USER</i> after each call to a PAM function.</dl>
<p> PAM_USER_PROMPT</p>
<dl>
<dd>The string used when prompting for a user&#8217;s name. The default value for this string is a localized version of &quot;login: &quot;.</dl>
<p> PAM_TTY</p>
<dl>
<dd>The terminal name: prefixed by /dev/ if it is a device file; for graphical, X-based, applications the value for this item should be the <i>$DISPLAY</i> variable.</dl>
<p> PAM_RUSER</p>
<dl>
<dd>The requesting user name: local name for a locally requesting user or a remote user name for a remote requesting user. </p>
<p> Generally an application or module will attempt to supply the value that is most strongly authenticated (a local account before a remote one. The level of trust in this value is embodied in the actual authentication stack associated with the application, so it is ultimately at the discretion of the system administrator. </p>
<p> <i>PAM_RUSER [at] PAM_RHOST</i> should always identify the requesting user. In some cases, <i>PAM_RUSER</i> may be NULL. In such situations, it is unclear who the requesting entity is.</dl>
<p> PAM_RHOST</p>
<dl>
<dd>The requesting hostname (the hostname of the machine from which the <i>PAM_RUSER</i> entity is requesting service). That is <i>PAM_RUSER [at] PAM_RHOST</i> does identify the requesting user. In some applications, <i>PAM_RHOST</i> may be NULL. In such situations, it is unclear where the authentication request is originating from.</dl>
<p> PAM_AUTHTOK</p>
<dl>
<dd>The authentication token (often a password). This token should be ignored by all module functions besides <code><a href="/docs/linux/man/3-pam_sm_authenticate/">pam_sm_authenticate</a></code>(3) and <code><a href="/docs/linux/man/3-pam_sm_chauthtok/">pam_sm_chauthtok</a></code>(3). In the former function it is used to pass the most recent authentication token from one stacked module to another. In the latter function the token is used for another purpose. It contains the currently active authentication token.</dl>
<p> PAM_OLDAUTHTOK</p>
<dl>
<dd>The old authentication token. This token should be ignored by all module functions except <code><a href="/docs/linux/man/3-pam_sm_chauthtok/">pam_sm_chauthtok</a></code>(3).</dl>
<p> PAM_CONV</p>
<dl>
<dd>The pam_conv structure. See <code><a href="/docs/linux/man/3-pam_conv/">pam_conv</a></code>(3).</dl>
<p> The following additional items are specific to Linux-PAM and should not be used in portable applications: </p>
<p> PAM_FAIL_DELAY</p>
<dl>
<dd>A function pointer to redirect centrally managed failure delays. See <code><a href="/docs/linux/man/3-pam_fail_delay/">pam_fail_delay</a></code>(3).</dl>
<p> PAM_XDISPLAY</p>
<dl>
<dd>The name of the X display. For graphical, X-based applications the value for this item should be the <i>$DISPLAY</i> variable. This value may be used independently of <i>PAM_TTY</i> for passing the name of the display.</dl>
<p> PAM_XAUTHDATA</p>
<dl>
<dd>A pointer to a structure containing the X authentication data required to make a connection to the display specified by <i>PAM_XDISPLAY</i>, if such information is necessary. See <code><a href="/docs/linux/man/3-pam_xauth_data/">pam_xauth_data</a></code>(3).</dl>
<p> PAM_AUTHTOK_TYPE</p>
<dl>
<dd>The default action is for the module to use the following prompts when requesting passwords: &quot;New UNIX password: &quot; and &quot;Retype UNIX password: &quot;. The example word <i>UNIX</i> can be replaced with this item, by default it is empty. This item is used by <code><a href="/docs/linux/man/3-pam_get_authtok/">pam_get_authtok</a></code>(3).</dl>
<p> For all <i>item_type</i>s, other than PAM_CONV and PAM_FAIL_DELAY, <i>item</i> is a pointer to a &lt;NUL&gt; terminated character string. In the case of PAM_CONV, <i>item</i> points to an initialized <i>pam_conv</i> structure. In the case of PAM_FAIL_DELAY, <i>item</i> is a function pointer: <code>void (*delay_fn)(int retval, unsigned usec_delay, void *appdata_ptr)</code> </p>
<p> Both, PAM_AUTHTOK and PAM_OLDAUTHTOK, will be reseted before returning to the application. Which means an application is not able to access the authentication tokens.</p>
<h2>Return Values</h2>
<p>PAM_BAD_ITEM</p>
<dl>
<dd>The application attempted to set an undefined or inaccessible item.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Data was successful updated.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>The <i>pam_handle_t</i> passed as first argument was invalid.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) </p>
