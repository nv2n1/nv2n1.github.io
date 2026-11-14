---
title: "pam_debug(8)"
name: "pam_debug"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_debug/"
description: "pam_debug – PAM module to debug the PAM stack"
---

<p>pam_debug &#8211; PAM module to debug the PAM stack</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_debug.so</code> [auth=<i>value</i>] [cred=<i>value</i>] [acct=<i>value</i>] [prechauthtok=<i>value</i>] [chauthtok=<i>value</i>] [auth=<i>value</i>] [open_session=<i>value</i>] [close_session=<i>value</i>]</dl>
<h2>Description</h2>
<dd>The pam_debug PAM module is intended as a debugging aide for determining how the PAM stack is operating. This module returns what its module arguments tell it to return.</p>
<h2>Options</h2>
<p><code>auth=</code><i>value</i></p>
<dl>
<dd>The <code><a href="/docs/linux/man/3-pam_sm_authenticate/">pam_sm_authenticate</a></code>(3) function will return <i>value</i>.</dl>
<p> <code>cred=</code><i>value</i></p>
<dl>
<dd>The <code><a href="/docs/linux/man/3-pam_sm_setcred/">pam_sm_setcred</a></code>(3) function will return <i>value</i>.</dl>
<p> <code>acct=</code><i>value</i></p>
<dl>
<dd>The <code><a href="/docs/linux/man/3-pam_sm_acct_mgmt/">pam_sm_acct_mgmt</a></code>(3) function will return <i>value</i>.</dl>
<p> <code>prechauthtok=</code><i>value</i></p>
<dl>
<dd>The <code><a href="/docs/linux/man/3-pam_sm_chauthtok/">pam_sm_chauthtok</a></code>(3) function will return <i>value</i> if the <i>PAM_PRELIM_CHECK</i> flag is set.</dl>
<p> <code>chauthtok=</code><i>value</i></p>
<dl>
<dd>The <code><a href="/docs/linux/man/3-pam_sm_chauthtok/">pam_sm_chauthtok</a></code>(3) function will return <i>value</i> if the <i>PAM_PRELIM_CHECK</i> flag is <code>not</code> set.</dl>
<p> <code>open_session=</code><i>value</i></p>
<dl>
<dd>The <code><a href="/docs/linux/man/3-pam_sm_open_session/">pam_sm_open_session</a></code>(3) function will return <i>value</i>.</dl>
<p> <code>close_session=</code><i>value</i></p>
<dl>
<dd>The <code><a href="/docs/linux/man/3-pam_sm_close_session/">pam_sm_close_session</a></code>(3) function will return <i>value</i>.</dl>
<p> Where <i>value</i> can be one of: success, open_err, symbol_err, service_err, system_err, buf_err, perm_denied, auth_err, cred_insufficient, authinfo_unavail, user_unknown, maxtries, new_authtok_reqd, acct_expired, session_err, cred_unavail, cred_expired, cred_err, no_module_data, conv_err, authtok_err, authtok_recover_err, authtok_lock_busy, authtok_disable_aging, try_again, ignore, abort, authtok_expired, module_unknown, bad_item, conv_again, incomplete.</p>
<h2>Module Types Provided</h2>
<p>All module types (<code>auth</code>, <code>account</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>Default return code if no other value was specified, else specified return value.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>auth requisite pam_permit.so
auth [success=2 default=ok] pam_debug.so auth=perm_denied cred=success
auth [default=reset] pam_debug.so auth=success cred=perm_denied
auth [success=done default=die] pam_debug.so
auth optional pam_debug.so auth=perm_denied cred=perm_denied
auth sufficient pam_debug.so auth=success cred=success</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_debug was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
