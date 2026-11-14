---
title: "nfs4_uid_to_name(3)"
name: "nfs4_uid_to_name"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nfs4_uid_to_name/"
description: "nfs4_uid_to_name, nfs4_gid_to_name, nfs4_name_to_uid, nfs4_name_to_gid, nfs4_init_name_mapping, nfs4_get_default_domain, nfs4_gss_princ_to_ids, nfs4_gss_princ_to_grouplist, nfs4_gss_princ_to_ids_ex..."
---

<p>nfs4_uid_to_name, nfs4_gid_to_name, nfs4_name_to_uid, nfs4_name_to_gid, nfs4_init_name_mapping, nfs4_get_default_domain, nfs4_gss_princ_to_ids, nfs4_gss_princ_to_grouplist, nfs4_gss_princ_to_ids_ex, nfs4_gss_princ_to_grouplist_ex, nfs4_set_debug &#8211; ID mapping routines used for NFSv4</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nfs4_idmap.h&gt;
int nfs4_init_name_mapping(char *conffile);
int nfs4_get_default_domain(char *server, char *domain, size_t len);
int nfs4_uid_to_name(uid_t uid, char *domain, char *name, size_t len);
int nfs4_uid_to_owner(uid_t uid, char *domain, char *name, size_t len);
int nfs4_gid_to_name(gid_t gid, char *domain, char *name, size_t len);
int nfs4_gid_to_owner(gid_t gid, char *domain, char *name, size_t len);
int nfs4_name_to_uid(char *name, uid_t *uid);
int nfs4_name_to_gid(char *name, gid_t *gid);
int nfs4_owner_to_uid(char *name, uid_t *uid);
int nfs4_owner_to_gid(char *name, gid_t *gid);
int nfs4_gss_princ_to_ids(char *secname, char *princ, uid_t *uid, gid_t *gid);
int nfs4_gss_princ_to_grouplist(char *secname, char *princ, gid_t *groups, int *ngroups);
int nfs4_gss_princ_to_ids_ex(char *secname, char *princ, uid_t *uid, gid_t *gid, extra_mapping_params **ex);
int nfs4_gss_princ_to_grouplist_ex(char *secname, char *princ, gid_t *groups, int *ngroups, extra_mapping_params **ex);
void nfs4_set_debug(int dbg_level, void (*logger)(const char *, ...));
</code></pre>
<h2>Description</h2>
<p>NFSv4 uses names of the form <i>user [at] domain</i>. To write code that helps the kernel map uid&#8217;s (as rpc.idmapd does) or that processes NFSv4 ACLs, you need to be able to convert between NFSv4 names and local uids and gids. </p>
<p> The <code>nfs4_uid_to_name()</code> and <code>nfs4_gid_to_name()</code> functions, given <i>uid </i> or <i>gid</i> and <i>domain</i> (as a null-terminated string), write the corresponding nfsv4 name into the buffer provided in <i>name</i>, which must be of length at least <i>len</i>. </p>
<p> The <code>nfs4_uid_to_owner()</code> and <code>nfs4_gid_to_group_owner()</code> functions, given <i>uid</i> or <i>gid</i> and <i>domain</i> (as a null-terminated string), write the corresponding nfsv4 name into the buffer provided in <i>name</i>, which must be of length at least <i>len</i>. If there is no valid mapping from <i>uid</i> or <i>gid</i> to <i>name</i>, then the numerical string representing uid or gid is returned instead. </p>
<p> The <code>nfs4_name_to_uid()</code> and <code>nfs4_name_to_gid()</code> functions, given <i>name</i> (as a null-terminated string), return the corresponding uid or gid in the second parameter. </p>
<p> The <code>nfs4_owner_to_uid()</code> and <code>nfs4_group_owner_to_gid()</code> functions, given <i>name</i> (as a null-terminated string), return the corresponding uid or gid in the second parameter. If there is no valid mapping from <i>name</i> to <i>uid</i> or <i>gid</i> the value for the user or group &quot;nobody&quot; will be returned instead. </p>
<p> The <code>nfs4_init_name_mapping()</code> function must be called before using any of these functions. It reads defaults from the configuration file at the provided path, usually &quot;etc/idmapd.conf&quot;. </p>
<p> The <i>domain</i> argument to the id-to-name functions is there to provide a hint to the name mapper in the case where an id might be mapped to names in multiple domains. In most cases, this argument should just be the name returned in the <i>domain</i> argument to <code>nfs4_get_default_domain()</code> which should be called with <i>server</i> set to NULL. The <i>domain</i> should be a buffer of length <i>len</i>. The constant NFS4_MAX_DOMAIN_LEN may be used to determine a reasonable value for that length. </p>
<p> The function <code>nfs4_get_grouplist()</code>, given a <i>name</i>, fills the provided array <i>groups</i> with up to <i>*ngroups</i> group IDs corresponding to which the user <i>name</i> belongs to, setting <i>*ngroups</i> to the actual number of such groups. If the user belongs to more than <i>*ngroups</i> groups, then an error is returned and the actual number of groups is stored in *ngroups. </p>
<p> Functions <code>nfs4_gss_princ_to_ids()</code>, <code>nfs4_gss_princ_to_grouplist()</code>, <code>nfs4_gss_princ_to_ids_ex()</code>, and <code>nfs4_gss_princ_to_grouplist_ex()</code> are used to convert from a gss principal name (as returned by <code>gss_display_name()</code>) to a uid and gid, or list of gids. </p>
<p> Finally, <code>nfs4_set_debug()</code> allows the application to set a debugging level to produce extra debugging information from within the library. The optional <i>logger</i> function specifies an alternative logging function to call for the debug messages rather than the default internal function within the library.</p>
<h2>Return Value</h2>
<p>All functions return 0 or, in the case of error, -ERRNO. </p>
