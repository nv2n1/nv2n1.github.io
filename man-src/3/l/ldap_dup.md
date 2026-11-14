---
title: "ldap_dup(3)"
name: "ldap_dup"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_dup/"
description: "ldap_dup, ldap_destroy, – Duplicate and destroy LDAP session handles"
---

<h2 class="name">NAME</h2>
<p> ldap_dup, ldap_destroy, &#8211; Duplicate and destroy LDAP session handles </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
LDAP *ldap_dup(
    LDAP *old);

int ldap_destroy(
    LDAP *old);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ldap_dup()</code> duplicates an existing LDAP (<code>LDAP *</code>) session handle. The new session handle may be used concurrently with the original session handle. In a threaded environment, different threads may execute concurrent requests on the same connection/session without fear of contamination. Each session handle manages its own private error results. </p>
<p> <code>ldap_destroy()</code> destroys an existing session handle. </p>
<p> The <code>ldap_dup()</code> and <code>ldap_destroy()</code> functions are used in conjunction with a &quot;thread safe&quot; version of <code>libldap</code> (<code>libldap_r</code>) to enable operation thread safe API calls, so that a single session may be simultaneously used across multiple threads with consistent error handling. </p>
<p> When a session is created through the use of one of the session creation functions including <code><a href="/docs/linux/man/3-ldap_open/">ldap_open</a></code>(3), <code><a href="/docs/linux/man/3-ldap_init/">ldap_init</a></code>(3), <code><a href="/docs/linux/man/3-ldap_initialize/">ldap_initialize</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_init_fd/">ldap_init_fd</a></code>(3) an <code>LDAP *</code> session handle is returned to the application. The session handle may be shared amongst threads, however the error codes are unique to a session handle. Multiple threads performing different operations using the same session handle will result in inconsistent error codes and return values. </p>
<p> To prevent this confusion, <code>ldap_dup()</code> is used duplicate an existing session handle so that multiple threads can share the session, and maintain consistent error information and results. </p>
<p> The message queues for a session are shared between sibling session handles. Results of operations on a sibling session handles are accessible to all the sibling session handles. Applications desiring results associated with a specific operation should provide the appropriate msgid to <code>ldap_result()</code>. Applications should avoid calling <code>ldap_result()</code> with <code>LDAP_RES_ANY</code> as that may &quot;steal&quot; and return results in the calling thread that another operation in a different thread, using a different session handle, may require to complete. </p>
<p> When <code>ldap_unbind()</code> is called on a session handle with siblings, all the siblings become invalid. </p>
<p> Siblings must be destroyed using <code>ldap_destroy()</code>. Session handle resources associated with the original (<code>LDAP *</code>) will be freed when the last session handle is destroyed or when <code>ldap_unbind()</code> is called, if no other session handles currently exist.</p>
<h2>ERRORS</h2>
<p> If an error occurs, <code>ldap_dup()</code> will return NULL and <i>errno</i> should be set appropriately. <code>ldap_destroy()</code> will directly return the LDAP code associated to the error (or <i>LDAP_SUCCESS</i> in case of success); <i>errno</i> should be set as well whenever appropriate.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap_open/">ldap_open</a></code>(3), <code><a href="/docs/linux/man/3-ldap_init/">ldap_init</a></code>(3), <code><a href="/docs/linux/man/3-ldap_initialize/">ldap_initialize</a></code>(3), <code><a href="/docs/linux/man/3-ldap_init_fd/">ldap_init_fd</a></code>(3), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> This work is based on the previously proposed <code>LDAP C API Concurrency Extensions</code> draft <code>(</code>draft-zeilenga-ldap-c-api-concurrency-00.txt<code>)</code> effort. <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
