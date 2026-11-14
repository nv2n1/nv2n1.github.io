---
title: "misc_conv(3)"
name: "misc_conv"
section: "3"
letter: "m"
url: "/docs/linux/man/3-misc_conv/"
description: "misc_conv – text based conversation function"
---

<h2 class="name">NAME</h2>
<p> misc_conv &#8211; text based conversation function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;security/pam_misc.h&gt;
</code></pre>
<dl>
<dt> <code>int misc_conv(int&nbsp;<wbr></code><i>num_msg</i><code>, const struct pam_message&nbsp;<wbr>**</code><i>msgm</i><code>, struct pam_response&nbsp;<wbr>**</code><i>response</i><code>, void&nbsp;<wbr>*</code><i>appdata_ptr</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>misc_conv</code> function is part of <code>libpam_misc</code> and not of the standard <code>libpam</code> library. This function will prompt the user with the appropriate comments and obtain the appropriate inputs as directed by authentication modules. </p>
<p> In addition to simply slotting into the appropriate <code><a href="/docs/linux/man/3-pam_conv/">pam_conv</a></code>(3), this function provides some time-out facilities. The function exports five variables that can be used by an application programmer to limit the amount of time this conversation function will spend waiting for the user to type something. The five variabls are as follows: </p>
<p> <code>time_t</code> <i>pam_misc_conv_warn_time</i>;</p>
<dl>
<dt>
<dd> This variable contains the <i>time</i> (as returned by <code><a href="/docs/linux/man/2-time/">time</a></code>(2)) that the user should be first warned that the clock is ticking. By default it has the value 0, which indicates that no such warning will be given. The application may set its value to sometime in the future, but this should be done prior to passing control to the <i>Linux-PAM</i> library.</dl>
<p> <code>const char *</code><i>pam_misc_conv_warn_line</i>;</p>
<dl>
<dt>
<dd> Used in conjuction with <i>pam_misc_conv_warn_time</i>, this variable is a pointer to the string that will be displayed when it becomes time to warn the user that the timeout is approaching. Its default value is a translated version of &#8220;&#8230;Time is running out&#8230;&#8221;, but this can be changed by the application prior to passing control to <i>Linux-PAM</i>.</dl>
<p> <code>time_t</code> <i>pam_misc_conv_die_time</i>;</p>
<dl>
<dt>
<dd> This variable contains the <i>time</i> (as returned by <code><a href="/docs/linux/man/2-time/">time</a></code>(2)) that the will time out. By default it has the value 0, which indicates that the conversation function will not timeout. The application may set its value to sometime in the future, but this should be done prior to passing control to the <i>Linux-PAM</i> library.</dl>
<p> <code>const char *</code><i>pam_misc_conv_die_line</i>;</p>
<dl>
<dt>
<dd> Used in conjuction with <i>pam_misc_conv_die_time</i>, this variable is a pointer to the string that will be displayed when the conversation times out. Its default value is a translated version of &#8220;&#8230;Sorry, your time is up!&#8221;, but this can be changed by the application prior to passing control to <i>Linux-PAM</i>.</dl>
<p> <code>int</code> <i>pam_misc_conv_died</i>;</p>
<dl>
<dt>
<dd> Following a return from the <i>Linux-PAM</i> libraray, the value of this variable indicates whether the conversation has timed out. A value of 1 indicates the time-out occurred.</dl>
<p> The following two function pointers are available for supporting binary prompts in the conversation function. They are optimized for the current incarnation of the <code>libpamc</code> library and are subject to change. </p>
<p> <code>int</code> <i>(*pam_binary_handler_fn)</i>(<code>void *</code><i>appdata</i>, <code>pamc_bp_t *</code><i>prompt_p</i>);</p>
<dl>
<dt>
<dd> This function pointer is initialized to NULL but can be filled with a function that provides machine-machine (hidden) message exchange. It is intended for use with hidden authentication protocols such as RSA or Diffie-Hellman key exchanges. (This is still under development.)</dl>
<p> <code>int</code> <i>(*pam_binary_handler_free)</i>(<code>void *</code><i>appdata</i>, <code>pamc_bp_t *</code><i>delete_me</i>);</p>
<dl>
<dt>
<dd> This function pointer is initialized to <code>PAM_BP_RENEW(delete_me, 0, 0)</code>, but can be redefined as desired by the application.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pam_conv/">pam_conv</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>STANDARDS</h2>
<p> The <code>misc_conv</code> function is part of the <code>libpam_misc</code> Library and not defined in any standard. </p>
<h2>Index</h2>
