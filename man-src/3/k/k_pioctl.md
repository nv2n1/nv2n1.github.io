---
title: "k_pioctl(3)"
name: "k_pioctl"
section: "3"
letter: "k"
url: "/docs/linux/man/3-k_pioctl/"
description: "k_hasafs k_hasafs_recheck k_pioctl k_unlog k_setpag k_afs_cell_of_file kafs_set_verbose kafs_settoken_rxkad kafs_settoken krb_afslog krb_afslog_uid kafs_settoken5 krb5_afslog krb5_afslog_uid – AFS ..."
---

<h2>NAME</h2>
<p> <code>k_hasafs</code> <code>k_hasafs_recheck</code> <code>k_pioctl</code> <code>k_unlog</code> <code>k_setpag</code> <code>k_afs_cell_of_file</code> <code>kafs_set_verbose</code> <code>kafs_settoken_rxkad</code> <code>kafs_settoken</code> <code>krb_afslog</code> <code>krb_afslog_uid</code> <code>kafs_settoken5</code> <code>krb5_afslog</code> <code>krb5_afslog_uid</code> &#8211; AFS library</p>
<h2>LIBRARY</h2>
<p> AFS cache manager access library (libkafs, -lkafs)</p>
<h2>SYNOPSIS</h2>
<p> In kafs.h Ft int Fn k_afs_cell_of_file const char *path char *cell int len Ft int Fn k_hasafs void Ft int Fn k_hasafs_recheck void Ft int Fn k_pioctl char *a_path int o_opcode struct ViceIoctl *a_paramsP int a_followSymlinks Ft int Fn k_setpag void Ft int Fn k_unlog void Ft void Fn kafs_set_verbose void (*func)(void *, const char *, int) void * Ft int Fn kafs_settoken_rxkad const char *cell struct ClearToken *token void *ticket size_t ticket_len Ft int Fn kafs_settoken const char *cell uid_t uid CREDENTIALS *c Fn krb_afslog char *cell char *realm Ft int Fn krb_afslog_uid char *cell char *realm uid_t uid Ft krb5_error_code Fn krb5_afslog_uid krb5_context context krb5_ccache id const char *cell krb5_const_realm realm uid_t uid Ft int Fn kafs_settoken5 const char *cell uid_t uid krb5_creds *c Ft krb5_error_code Fn krb5_afslog krb5_context context krb5_ccache id const char *cell krb5_const_realm realm</p>
<h2>DESCRIPTION</h2>
<p> Fn k_hasafs initializes some library internal structures, and tests for the presence of AFS in the kernel, none of the other functions should be called before Fn k_hasafs is called, or if it fails. </p>
<p> Fn k_hasafs_recheck forces a recheck if a AFS client has started since last time Fn k_hasafs or Fn k_hasafs_recheck was called. </p>
<p> Fn kafs_set_verbose set a log function that will be called each time the kafs library does something important so that the application using libkafs can output verbose logging. Calling the function Fa kafs_set_verbose with the function argument set to <code>NULL</code> will stop libkafs from calling the logging function (if set). </p>
<p> Fn kafs_settoken_rxkad set <code>rxkad</code> with the Fa token and Fa ticket (that have the length Fa ticket_len ) for a given Fa cell . </p>
<p> Fn kafs_settoken and Fn kafs_settoken5 work the same way as Fn kafs_settoken_rxkad but internally converts the Kerberos 4 or 5 credential to a afs cleartoken and ticket. </p>
<p> Fn krb_afslog , and Fn krb_afslog_uid obtains new tokens (and possibly tickets) for the specified Fa cell and Fa realm . If Fa cell is <code>NULL</code> the local cell is used. If Fa realm is <code>NULL</code> the function tries to guess what realm to use. Unless you have some good knowledge of what cell or realm to use, you should pass <code>NULL</code> Fn krb_afslog will use the real user-id for the <code>ViceId </code>field in the token, Fn krb_afslog_uid will use Fa uid . </p>
<p> Fn krb5_afslog , and Fn krb5_afslog_uid are the Kerberos 5 equivalents of Fn krb_afslog , and Fn krb_afslog_uid . </p>
<p> Fn krb5_afslog , Fn kafs_settoken5 can be configured to behave differently via a <code>krb5_appdefault</code> option <code>afs-use-524</code> in krb5.conf Possible values for <code>afs-use-524</code> are:</p>
<dl>
<dt><code>yes</code></p>
<dd> use the 524 server in the realm to convert the ticket</p>
<dt><code>no</code></p>
<dd> use the Kerberos 5 ticket directly, can be used with if the afs cell support 2b token.</p>
<dt><code>local, 2b</code></p>
<dd> convert the Kerberos 5 credential to a 2b token locally (the same work as a 2b 524 server should have done).</dl>
<p> Example: </p>
<pre><code>
[appdefaults] SU.SE = {afs - use - 524 = local} PDC.KTH.SE = {afs - use - 524 = yes} afs - use - 524 = yes
</code></pre>
<p> libkafs will use the <code>libkafs</code> as application name when running the <code>krb5_appdefault</code> function call. </p>
<p> The (uppercased) cell name is used as the realm to the <code>krb5_appdefault function.</code> </p>
<p> Fn k_afs_cell_of_file will in Fa cell return the cell of a specified file, no more than Fa len characters is put in Fa cell . </p>
<p> Fn k_pioctl does a Fn pioctl system call with the specified arguments. This function is equivalent to Fn lpioctl . </p>
<p> Fn k_setpag initializes a new PAG. </p>
<p> Fn k_unlog removes destroys all tokens in the current PAG.</p>
<h2>RETURN VALUES</h2>
<p> Fn k_hasafs returns 1 if AFS is present in the kernel, 0 otherwise. Fn krb_afslog and Fn krb_afslog_uid returns 0 on success, or a Kerberos error number on failure. Fn k_afs_cell_of_file , Fn k_pioctl , Fn k_setpag , and Fn k_unlog all return the value of the underlaying system call, 0 on success.</p>
<h2>ENVIRONMENT</h2>
<p> The following environment variable affect the mode of operation of <code>kafs</code></p>
<dl>
<dt><code>AFS_SYSCALL</code></p>
<dd> Normally, <code>kafs</code> will try to figure out the correct system call(s) that are used by AFS by itself. If it does not manage to do that, or does it incorrectly, you can set this variable to the system call number or list of system call numbers that should be used.</dl>
<h2>EXAMPLES</h2>
<p> The following code from <code>login</code> will obtain a new PAG and tokens for the local cell and the cell of the users home directory. </p>
<pre><code>
if (k_hasafs()) {
    char cell[64];
    k_setpag();
    if (k_afs_cell_of_file(pwd-&gt;pw_dir, cell, sizeof(cell)) == 0)
        krb_afslog(cell, NULL);
    krb_afslog(NULL, NULL);
}
</code></pre>
<h2>ERRORS</h2>
<p> If any of these functions (apart from Fn k_hasafs ) is called without AFS being present in the kernel, the process will usually (depending on the operating system) receive a SIGSYS signal.</p>
<h2>SEE ALSO</h2>
<p> krb5_appdefault3, krb5.conf5</p>
<dl>
<dt>
<dd> Transarc Corporation <i>AFS-3 Programmer&#8217;s Reference</i> <i>File Server/Cache Manager Interface</i> 1991</dl>
<h2>FILES</h2>
<p> libkafs will search for ThisCell and TheseCells in the following locations: /usr/vice/etc /etc/openafs /var/db/openafs/etc /usr/arla/etc /etc/arla and /etc/afs</p>
<h2>BUGS</h2>
<p> <code>AFS_SYSCALL</code> has no effect under AIX. </p>
<h2>Index</h2>
