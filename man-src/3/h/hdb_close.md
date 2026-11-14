---
title: "hdb_close(3)"
name: "hdb_close"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hdb_close/"
description: "HDB –"
---

<h2 class="name">NAME</h2>
<p> HDB &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hdb.h&gt;</p>
<h3>Data Fields</h3>
<p> char * <code>hdb_name</code> </p>
<p> krb5_error_code(* <code>hdb_open</code> )(krb5_context, struct <code>HDB</code> *, int, mode_t) </p>
<p> krb5_error_code(* <code>hdb_close</code> )(krb5_context, struct <code>HDB</code> *) </p>
<p> void(* <code>hdb_free</code> )(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *) </p>
<p> krb5_error_code(* <code>hdb_fetch_kvno</code> )(krb5_context, struct <code>HDB</code> *, krb5_const_principal, unsigned, krb5_kvno, <code>hdb_entry_ex</code> *) </p>
<p> krb5_error_code(* <code>hdb_store</code> )(krb5_context, struct <code>HDB</code> *, unsigned, <code>hdb_entry_ex</code> *) </p>
<p> krb5_error_code(* <code>hdb_remove</code> )(krb5_context, struct <code>HDB</code> *, krb5_const_principal) </p>
<p> krb5_error_code(* <code>hdb_firstkey</code> )(krb5_context, struct <code>HDB</code> *, unsigned, <code>hdb_entry_ex</code> *) </p>
<p> krb5_error_code(* <code>hdb_nextkey</code> )(krb5_context, struct <code>HDB</code> *, unsigned, <code>hdb_entry_ex</code> *) </p>
<p> krb5_error_code(* <code>hdb_lock</code> )(krb5_context, struct <code>HDB</code> *, int) </p>
<p> krb5_error_code(* <code>hdb_unlock</code> )(krb5_context, struct <code>HDB</code> *) </p>
<p> krb5_error_code(* <code>hdb_rename</code> )(krb5_context, struct <code>HDB</code> *, const char *) </p>
<p> krb5_error_code(* <code>hdb__get</code> )(krb5_context, struct <code>HDB</code> *, krb5_data, krb5_data *) </p>
<p> krb5_error_code(* <code>hdb__put</code> )(krb5_context, struct <code>HDB</code> *, int, krb5_data, krb5_data) </p>
<p> krb5_error_code(* <code>hdb__del</code> )(krb5_context, struct <code>HDB</code> *, krb5_data) </p>
<p> krb5_error_code(* <code>hdb_destroy</code> )(krb5_context, struct <code>HDB</code> *) </p>
<p> krb5_error_code(* <code>hdb_get_realms</code> )(krb5_context, struct <code>HDB</code> *, krb5_realm **) </p>
<p> krb5_error_code(* <code>hdb_password</code> )(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, const char *, int) </p>
<p> krb5_error_code(* <code>hdb_auth_status</code> )(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, int) </p>
<p> krb5_error_code(* <code>hdb_check_constrained_delegation</code> )(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, krb5_const_principal) </p>
<p> krb5_error_code(* <code>hdb_check_pkinit_ms_upn_match</code> )(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, krb5_const_principal) </p>
<p> krb5_error_code(* <code>hdb_check_s4u2self</code> )(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, krb5_const_principal) </p>
<h2>Detailed Description</h2>
<p> <code>HDB</code> backend function pointer structure </p>
<p> The <code>HDB</code> structure is what the KDC and kadmind framework uses to query the backend database when talking about principals.</p>
<h2>Field Documentation</h2>
<h3>krb5_error_code(* HDB::hdb__del)(krb5_context, struct <code>HDB</code> *, krb5_data)</h3>
<p> Delete and hdb_entry from a classical DB backend </p>
<p> Same discussion as in <code>HDB::hdb__get</code></p>
<h3>krb5_error_code(* HDB::hdb__get)(krb5_context, struct <code>HDB</code> *, krb5_data, krb5_data *)</h3>
<p> Get an hdb_entry from a classical DB backend </p>
<p> If the database is a classical DB (ie BDB, NDBM, GDBM, etc) backend, this function will take a principal key (krb5_data) and return all data related to principal in the return krb5_data. The returned encoded entry is of type hdb_entry or hdb_entry_alias.</p>
<h3>krb5_error_code(* HDB::hdb__put)(krb5_context, struct <code>HDB</code> *, int, krb5_data, krb5_data)</h3>
<p> Store an hdb_entry from a classical DB backend </p>
<p> Same discussion as in <code>HDB::hdb__get</code></p>
<h3>krb5_error_code(* HDB::hdb_auth_status)(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, int)</h3>
<p> Auth feedback </p>
<p> This is a feedback call that allows backends that provides lockout functionality to register failure and/or successes. </p>
<p> In case the entry is locked out, the backend should set the hdb_entry.flags.locked-out flag.</p>
<h3>krb5_error_code(* HDB::hdb_check_constrained_delegation)(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, krb5_const_principal)</h3>
<p> Check if delegation is allowed.</p>
<h3>krb5_error_code(* HDB::hdb_check_pkinit_ms_upn_match)(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, krb5_const_principal)</h3>
<p> Check if this name is an alias for the supplied client for PKINIT userPrinicpalName logins</p>
<h3>krb5_error_code(* HDB::hdb_check_s4u2self)(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, krb5_const_principal)</h3>
<p> Check if s4u2self is allowed from this client to this server</p>
<h3>krb5_error_code(* HDB::hdb_close)(krb5_context, struct <code>HDB</code> *)</h3>
<p> Close the database for transaction </p>
<p> Closes the database for further transactions, wont release any permanant resources. the database can be -&gt;hdb_open-ed again.</p>
<h3>krb5_error_code(* HDB::hdb_destroy)(krb5_context, struct <code>HDB</code> *)</h3>
<p> Destroy the handle to the database. </p>
<p> Destroy the handle to the database, deallocate all memory and related resources. Does not remove any permanent data. Its the logical reverse of hdb_create() function that is the entry point for the module.</p>
<h3>krb5_error_code(* HDB::hdb_fetch_kvno)(krb5_context, struct <code>HDB</code> *, krb5_const_principal, unsigned, krb5_kvno, <code>hdb_entry_ex</code> *)</h3>
<p> Fetch an entry from the backend </p>
<p> Fetch an entry from the backend, flags are what type of entry should be fetch: client, server, krbtgt. knvo (if specified and flags HDB_F_KVNO_SPECIFIED set) is the kvno to get</p>
<h3>krb5_error_code(* HDB::hdb_firstkey)(krb5_context, struct <code>HDB</code> *, unsigned, <code>hdb_entry_ex</code> *)</h3>
<p> As part of iteration, fetch one entry</p>
<h3>void(* HDB::hdb_free)(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *)</h3>
<p> Free an entry after use.</p>
<h3>krb5_error_code(* HDB::hdb_get_realms)(krb5_context, struct <code>HDB</code> *, krb5_realm **)</h3>
<p> Get the list of realms this backend handles. This call is optional to support. The returned realms are used for announcing the realms over bonjour. Free returned array with krb5_free_host_realm().</p>
<h3>krb5_error_code(* HDB::hdb_lock)(krb5_context, struct <code>HDB</code> *, int)</h3>
<p> Lock database </p>
<p> A lock can only be held by one consumers. Transaction can still happen on the database while the lock is held, so the entry is only useful for syncroning creation of the database and renaming of the database.</p>
<h3>char* HDB::hdb_name</h3>
<p> don&#8217;t use, only for DB3</p>
<h3>krb5_error_code(* HDB::hdb_nextkey)(krb5_context, struct <code>HDB</code> *, unsigned, <code>hdb_entry_ex</code> *)</h3>
<p> As part of iteration, fetch next entry</p>
<h3>krb5_error_code(* HDB::hdb_open)(krb5_context, struct <code>HDB</code> *, int, mode_t)</h3>
<p> Open (or create) the a Kerberos database. </p>
<p> Open (or create) the a Kerberos database that was resolved with hdb_create(). The third and fourth flag to the function are the same as open(), thus passing O_CREAT will create the data base if it doesn&#8217;t exists. </p>
<p> Then done the caller should call <code>hdb_close()</code>, and to release all resources <code>hdb_destroy()</code>.</p>
<h3>krb5_error_code(* HDB::hdb_password)(krb5_context, struct <code>HDB</code> *, <code>hdb_entry_ex</code> *, const char *, int)</h3>
<p> Change password. </p>
<p> Will update keys for the entry when given password. The new keys must be written into the entry and will then later be -&gt;<code>hdb_store()</code> into the database. The backend will still perform all other operations, increasing the kvno, and update modification timestamp. </p>
<p> The backend needs to call _kadm5_set_keys() and perform password quality checks.</p>
<h3>krb5_error_code(* HDB::hdb_remove)(krb5_context, struct <code>HDB</code> *, krb5_const_principal)</h3>
<p> Remove an entry from the database.</p>
<h3>krb5_error_code(* HDB::hdb_rename)(krb5_context, struct <code>HDB</code> *, const char *)</h3>
<p> Rename the data base. </p>
<p> Assume that the database is not hdb_open&#8217;ed and not locked.</p>
<h3>krb5_error_code(* HDB::hdb_store)(krb5_context, struct <code>HDB</code> *, unsigned, <code>hdb_entry_ex</code> *)</h3>
<p> Store an entry to database</p>
<h3>krb5_error_code(* HDB::hdb_unlock)(krb5_context, struct <code>HDB</code> *)</h3>
<p> Unlock database </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalhdblibrary from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBC">Author</a></p>
<dd></dl>
