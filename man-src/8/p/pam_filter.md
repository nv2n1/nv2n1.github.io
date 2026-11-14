---
title: "pam_filter(8)"
name: "pam_filter"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_filter/"
description: "pam_filter – PAM filter module"
---

<p>pam_filter &#8211; PAM filter module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_filter.so</code> [debug] [new_term] [non_term] run1|run2 <i>filter</i> [<i>&#8230;</i>]</dl>
<h2>Description</h2>
<dd>This module is intended to be a platform for providing access to all of the input/output that passes between the user and the application. It is only suitable for tty-based and (stdin/stdout) applications. </p>
<p> To function this module requires <i>filters</i> to be installed on the system. The single filter provided with the module simply transposes upper and lower case letters in the input and output streams. (This can be very annoying and is not kind to termcap based editors). </p>
<p> Each component of the module has the potential to invoke the desired filter. The filter is always <code><a href="/docs/linux/man/2-execv/">execv</a></code>(2) with the privilege of the calling application and <i>not</i> that of the user. For this reason it cannot usually be killed by the user without closing their session.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>new_term</code></p>
<dl>
<dd>The default action of the filter is to set the <i>PAM_TTY</i> item to indicate the terminal that the user is using to connect to the application. This argument indicates that the filter should set <i>PAM_TTY</i> to the filtered pseudo-terminal.</dl>
<p> <code>non_term</code></p>
<dl>
<dd>don&#8217;t try to set the <i>PAM_TTY</i> item.</dl>
<p> <code>runX</code></p>
<dl>
<dd>In order that the module can invoke a filter it should know when to invoke it. This argument is required to tell the filter when to do this. </p>
<p> Permitted values for <i>X</i> are <i>1</i> and <i>2</i>. These indicate the precise time that the filter is to be run. To understand this concept it will be useful to have read the <code><a href="/docs/linux/man/3-pam/">pam</a></code>(3) manual page. Basically, for each management group there are up to two ways of calling the module&#8217;s functions. In the case of the <i>authentication</i> and <i>session</i> components there are actually two separate functions. For the case of authentication, these functions are <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3) and <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3), here <code>run1</code> means run the filter from the <code>pam_authenticate</code> function and <code>run2</code> means run the filter from <code>pam_setcred</code>. In the case of the session modules, <i>run1</i> implies that the filter is invoked at the <code><a href="/docs/linux/man/3-pam_open_session/">pam_open_session</a></code>(3) stage, and <i>run2</i> for <code><a href="/docs/linux/man/3-pam_close_session/">pam_close_session</a></code>(3). </p>
<p> For the case of the account component. Either <i>run1</i> or <i>run2</i> may be used. </p>
<p> For the case of the password component, <i>run1</i> is used to indicate that the filter is run on the first occasion of <code><a href="/docs/linux/man/3-pam_chauthtok/">pam_chauthtok</a></code>(3) (the <i>PAM_PRELIM_CHECK</i> phase) and <i>run2</i> is used to indicate that the filter is run on the second occasion (the <i>PAM_UPDATE_AUTHTOK</i> phase).</dl>
<p> <code>filter</code></p>
<dl>
<dd>The full pathname of the filter to be run and any command line arguments that the filter might expect.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>auth</code>, <code>account</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The new filter was set successfully.</dl>
<p> PAM_ABORT</p>
<dl>
<dd>Critical error, immediate abort.</dl>
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/login to see how to configure login to transpose upper and lower case letters once the user has logged in:</p>
<dl>
<dd>
<pre> session required pam_filter.so run1 /lib/security/pam_filter/upperLOWER</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_filter was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
