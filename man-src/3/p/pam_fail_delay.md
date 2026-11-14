---
title: "pam_fail_delay(3)"
name: "pam_fail_delay"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_fail_delay/"
description: "pam_fail_delay – request a delay on failure"
---

<p>pam_fail_delay &#8211; request a delay on failure</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_fail_delay(pam_handle_t *pamh, unsigned int usec);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_fail_delay</code> function provides a mechanism by which an application or module can suggest a minimum delay of <i>usec</i> micro-seconds. The function keeps a record of the longest time requested with this function. Should <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3) fail, the failing return to the application is delayed by an amount of time randomly distributed (by up to 50%) about this longest value. Independent of success, the delay time is reset to its zero default value when the PAM service module returns control to the application. The delay occurs <i>after</i> all authentication modules have been called, but <i>before</i> control is returned to the service application. When using this function the programmer should check if it is available with:</p>
<dl>
<dd>
<pre>#ifdef HAVE_PAM_FAIL_DELAY
 ....
#endif /* HAVE_PAM_FAIL_DELAY */</pre>
</dl>
<p> For applications written with a single thread that are event driven in nature, generating this delay may be undesirable. Instead, the application may want to register the delay in some other way. For example, in a single threaded server that serves multiple authentication requests from a single event loop, the application might want to simply mark a given connection as blocked until an application timer expires. For this reason the delay function can be changed with the <i>PAM_FAIL_DELAY</i> item. It can be queried and set with <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3) and <code>pam_set_item </code>(3) respectively. The value used to set it should be a function pointer of the following prototype: </p>
<pre><code>void (*delay_fn)(int retval, unsigned usec_delay, void *appdata_ptr);</code></pre>
<p> The arguments being the <i>retval</i> return code of the module stack, the <i>usec_delay</i> micro-second delay that libpam is requesting and the <i>appdata_ptr</i> that the application has associated with the current <i>pamh</i>. This last value was set by the application when it called <code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3) or explicitly with <code><a href="/docs/linux/man/3-pam_set_item/">pam_set_item</a></code>(3). Note, if PAM_FAIL_DELAY item is unset (or set to NULL), then no delay will be performed.</p>
<h2>Rationale</h2>
<p>It is often possible to attack an authentication scheme by exploiting the time it takes the scheme to deny access to an applicant user. In cases of <i>short</i> timeouts, it may prove possible to attempt a <i>brute force</i> dictionary attack &#8212; with an automated process, the attacker tries all possible passwords to gain access to the system. In other cases, where individual failures can take measurable amounts of time (indicating the nature of the failure), an attacker can obtain useful information about the authentication process. These latter attacks make use of procedural delays that constitute a <i>covert channel</i> of useful information. </p>
<p> To minimize the effectiveness of such attacks, it is desirable to introduce a random delay in a failed authentication process. Preferable this value should be set by the application or a special PAM module. Standard PAM modules should not modify the delay unconditional.</p>
<h2>Example</h2>
<p>For example, a login application may require a failure delay of roughly 3 seconds. It will contain the following code: </p>
<dl>
<dd>
<pre> pam_fail_delay (pamh, 3000000 /* micro-seconds */ );
 pam_authenticate (pamh, 0);</pre>
</dl>
<p> if the modules do not request a delay, the failure delay will be between 1.5 and 4.5 seconds. </p>
<p> However, the modules, invoked in the authentication process, may also request delays: </p>
<dl>
<dd>
<pre>module #1: pam_fail_delay (pamh, 2000000);
module #2: pam_fail_delay (pamh, 4000000);</pre>
</dl>
<p> in this case, it is the largest requested value that is used to compute the actual failed delay: here between 2 and 6 seconds.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>Delay was successful adjusted.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>A NULL pointer was submitted as PAM handle.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3)</p>
<h2>Standards</h2>
<p>The <code>pam_fail_delay</code> function is an Linux-PAM extension.</p>
