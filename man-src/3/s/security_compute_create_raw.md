---
title: "security_compute_create_raw(3)"
name: "security_compute_create_raw"
section: "3"
letter: "s"
url: "/docs/linux/man/3-security_compute_create_raw/"
description: "security_compute_av, security_compute_av_flags, security_compute_create, security_compute_create_name, security_compute_relabel, security_compute_member, security_compute_user, security_validatetra..."
---

<p>security_compute_av, security_compute_av_flags, security_compute_create, security_compute_create_name, security_compute_relabel, security_compute_member, security_compute_user, security_validatetrans, security_get_initial_context &#8211; query the SELinux policy database in the kernel</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int security_compute_av(char *scon, char *tcon, security_class_t tclass, access_vector_t requested, struct av_decision *avd);
int security_compute_av_raw(char *scon, char *tcon, security_class_t tclass, access_vector_t requested, struct av_decision *avd);
int security_compute_av_flags(char *scon, char *tcon, security_class_t tclass, access_vector_t requested, struct av_decision *avd);
int security_compute_av_flags_raw(char *scon, char *tcon, security_class_t tclass, access_vector_t requested, struct av_decision *avd);
int security_compute_create(char *scon, char *tcon, security_class_t tclass, char **newcon);
int security_compute_create_raw(char *scon, char *tcon, security_class_t tclass, char **newcon);
int security_compute_create_name(char *scon, char *tcon, security_class_t tclass, const char *objname, char **newcon);
int security_compute_create_name_raw(char *scon, char *tcon, security_class_t tclass, const char *objname, char **newcon);
int security_compute_relabel(char *scon, char *tcon, security_class_t tclass, char **newcon);
int security_compute_relabel_raw(char *scon, char *tcon, security_class_t tclass, char **newcon);
int security_compute_member(char *scon, char *tcon, security_class_t tclass, char **newcon);
int security_compute_member_raw(char *scon, char *tcon, security_class_t tclass, char **newcon);
int security_compute_user(char *scon, const char *username, char ***con);
int security_compute_user_raw(char *scon, const char *username, char ***con);
int security_validatetrans(char *scon, const char *tcon, security_class_t tclass, char *newcon);
int security_validatetrans_raw(char *scon, const char *tcon, security_class_t tclass, char *newcon);
int security_get_initial_context(const char *name, char **con);
int security_get_initial_context_raw(const char *name, char **con);
int selinux_check_access(const char *scon, const char *tcon, const char *class, const char *perm, void *auditdata);
int selinux_check_passwd_access(access_vector_t requested);
int checkPasswdAccess(access_vector_t requested);</code></pre>
<h2>Description</h2>
<p><code>security_compute_av</code>() queries whether the policy permits the source context <i>scon</i> to access the target context <i>tcon</i> via class <i>tclass</i> with the <i>requested</i> access vector. The decision is returned in <i>avd</i>. </p>
<p> <code>security_compute_av_flags</code>() is identical to <code>security_compute_av</code> but additionally sets the <i>flags</i> field of <i>avd</i>. Currently one flag is supported: <code>SELINUX_AVD_FLAGS_PERMISSIVE</code>, which indicates the decision is computed on a permissive domain. </p>
<p> <code>security_compute_create</code>() is used to compute a context to use for labeling a new object in a particular class based on a SID pair. </p>
<p> <code>security_compute_create_name</code>() is identical to <code>security_compute_create</code>() but also takes name of the new object in creation as an argument. When <code>TYPE_TRANSITION</code> rule on the given class and a SID pair has object name extension, we shall be able to obtain a correct <i>newcon</i> according to the security policy. Note that this interface is only supported on the linux 2.6.40 or later. In the older kernel, the object name will be simply ignored. </p>
<p> <code>security_compute_relabel</code>() is used to compute the new context to use when relabeling an object, it is used in the pam_selinux.so source and the newrole source to determine the correct label for the tty at login time, but can be used for other things. </p>
<p> <code>security_compute_member</code>() is used to compute the context to use when labeling a polyinstantiated object instance. </p>
<p> <code>security_compute_user</code>() is used to determine the set of user contexts that can be reached from a source context. It is mainly used by <code>get_ordered_context_list</code>(). </p>
<p> <code>security_validatetrans</code>() is used to determine if a transition from scon to newcon using tcon as the object is valid for object class tclass. This checks against the mlsvalidatetrans and validatetrans constraints in the loaded policy. Returns 0 if allowed, and -1 if an error occurred with errno set. </p>
<p> <code>security_get_initial_context</code>() is used to get the context of a kernel initial security identifier specified by <i>name</i> </p>
<p> <code>security_compute_av_raw</code>(), <code>security_compute_av_flags_raw</code>(), <code>security_compute_create_raw</code>(), <code>security_compute_create_name_raw</code>(), <code>security_compute_relabel_raw</code>(), <code>security_compute_member_raw</code>(), <code>security_compute_user_raw</code>() <code>security_validatetrans_raw</code>() and <code>security_get_initial_context_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. </p>
<p> <code>selinux_check_access</code>() is used to check if the source context has the access permission for the specified class on the target context. </p>
<p> <code>selinux_check_passwd_access</code>() is used to check for a permission in the <i>passwd</i> class. <code>selinux_check_passwd_access</code>() uses getprevcon() for the source and target security contexts. </p>
<p> <code>checkPasswdAccess</code>() is a deprecated alias of the <code>selinux_check_passwd_access</code>() function.</p>
<h2>Return Value</h2>
<p>Returns zero on success or -1 on error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3), <code><a href="/docs/linux/man/3-getfilecon/">getfilecon</a></code>(3), <code><a href="/docs/linux/man/3-get_ordered_context_list/">get_ordered_context_list</a></code>(3) </p>
