---
title: "krb5_auth_getkeytype(3)"
name: "krb5_auth_getkeytype"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_auth_getkeytype/"
description: "krb5_auth_con_addflags krb5_auth_con_free krb5_auth_con_genaddrs krb5_auth_con_generatelocalsubkey krb5_auth_con_getaddrs krb5_auth_con_getauthenticator krb5_auth_con_getflags krb5_auth_con_getkey ..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_auth_con_addflags</code> <code>krb5_auth_con_free</code> <code>krb5_auth_con_genaddrs</code> <code>krb5_auth_con_generatelocalsubkey</code> <code>krb5_auth_con_getaddrs</code> <code>krb5_auth_con_getauthenticator</code> <code>krb5_auth_con_getflags</code> <code>krb5_auth_con_getkey</code> <code>krb5_auth_con_getlocalsubkey</code> <code>krb5_auth_con_getrcache</code> <code>krb5_auth_con_getremotesubkey</code> <code>krb5_auth_con_getuserkey</code> <code>krb5_auth_con_init</code> <code>krb5_auth_con_initivector</code> <code>krb5_auth_con_removeflags</code> <code>krb5_auth_con_setaddrs</code> <code>krb5_auth_con_setaddrs_from_fd</code> <code>krb5_auth_con_setflags</code> <code>krb5_auth_con_setivector</code> <code>krb5_auth_con_setkey</code> <code>krb5_auth_con_setlocalsubkey</code> <code>krb5_auth_con_setrcache</code> <code>krb5_auth_con_setremotesubkey</code> <code>krb5_auth_con_setuserkey</code> <code>krb5_auth_context</code> <code>krb5_auth_getcksumtype</code> <code>krb5_auth_getkeytype</code> <code>krb5_auth_getlocalseqnumber</code> <code>krb5_auth_getremoteseqnumber</code> <code>krb5_auth_setcksumtype</code> <code>krb5_auth_setkeytype</code> <code>krb5_auth_setlocalseqnumber</code> <code>krb5_auth_setremoteseqnumber</code> <code>krb5_free_authenticator</code> &#8211; manage authentication on connection level </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_auth_con_init Fa krb5_context context Fa krb5_auth_context *auth_context Fc Ft void Fo krb5_auth_con_free Fa krb5_context context Fa krb5_auth_context auth_context Fc Ft krb5_error_code Fo krb5_auth_con_setflags Fa krb5_context context Fa krb5_auth_context auth_context Fa int32_t flags Fc Ft krb5_error_code Fo krb5_auth_con_getflags Fa krb5_context context Fa krb5_auth_context auth_context Fa int32_t *flags Fc Ft krb5_error_code Fo krb5_auth_con_addflags Fa krb5_context context Fa krb5_auth_context auth_context Fa int32_t addflags Fa int32_t *flags Fc Ft krb5_error_code Fo krb5_auth_con_removeflags Fa krb5_context context Fa krb5_auth_context auth_context Fa int32_t removelags Fa int32_t *flags Fc Ft krb5_error_code Fo krb5_auth_con_setaddrs Fa krb5_context context Fa krb5_auth_context auth_context Fa krb5_address *local_addr Fa krb5_address *remote_addr Fc Ft krb5_error_code Fo krb5_auth_con_getaddrs Fa krb5_context context Fa krb5_auth_context auth_context Fa krb5_address **local_addr Fa krb5_address **remote_addr Fc Ft krb5_error_code Fo krb5_auth_con_genaddrs Fa krb5_context context Fa krb5_auth_context auth_context Fa int fd Fa int flags Fc Ft krb5_error_code Fo krb5_auth_con_setaddrs_from_fd Fa krb5_context context Fa krb5_auth_context auth_context Fa void *p_fd Fc Ft krb5_error_code Fo krb5_auth_con_getkey Fa krb5_context context Fa krb5_auth_context auth_context Fa krb5_keyblock **keyblock Fc Ft krb5_error_code Fo krb5_auth_con_getlocalsubkey Fa krb5_context context Fa krb5_auth_context auth_context Fa krb5_keyblock **keyblock Fc Ft krb5_error_code Fo krb5_auth_con_getremotesubkey Fa krb5_context context Fa krb5_auth_context auth_context Fa krb5_keyblock **keyblock Fc Ft krb5_error_code Fo krb5_auth_con_generatelocalsubkey Fa krb5_context context Fa krb5_auth_context auth_context Fa krb5_keyblock *key Fc Ft krb5_error_code Fo krb5_auth_con_initivector Fa krb5_context context Fa krb5_auth_context auth_context Fc Ft krb5_error_code Fo krb5_auth_con_setivector Fa krb5_context context Fa krb5_auth_context *auth_context Fa krb5_pointer ivector Fc Ft void Fo krb5_free_authenticator Fa krb5_context context Fa krb5_authenticator *authenticator Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>krb5_auth_context</code> structure holds all context related to an authenticated connection, in a similar way to <code>krb5_context</code> that holds the context for the thread or process. <code>krb5_auth_context</code> is used by various functions that are directly related to authentication between the server/client. Example of data that this structure contains are various flags, addresses of client and server, port numbers, keyblocks (and subkeys), sequence numbers, replay cache, and checksum-type. </p>
<p> Fn krb5_auth_con_init allocates and initializes the <code>krb5_auth_context</code> structure. Default values can be changed with Fn krb5_auth_con_setcksumtype and Fn krb5_auth_con_setflags . The <code>auth_context</code> structure must be freed by Fn krb5_auth_con_free . </p>
<p> Fn krb5_auth_con_getflags , Fn krb5_auth_con_setflags , Fn krb5_auth_con_addflags and Fn krb5_auth_con_removeflags gets and modifies the flags for a <code>krb5_auth_context</code> structure. Possible flags to set are:</p>
<dl>
<dt><code>KRB5_AUTH_CONTEXT_DO_SEQUENCE</code></p>
<dd> Generate and check sequence-number on each packet.</p>
<dt><code>KRB5_AUTH_CONTEXT_DO_TIME</code></p>
<dd> Check timestamp on incoming packets.</p>
<dt><code>KRB5_AUTH_CONTEXT_RET_SEQUENCE , KRB5_AUTH_CONTEXT_RET_TIME</code></p>
<dd> Return sequence numbers and time stamps in the outdata parameters.</p>
<dt><code>KRB5_AUTH_CONTEXT_CLEAR_FORWARDED_CRED</code></p>
<dd> will force Fn krb5_get_forwarded_creds and Fn krb5_fwd_tgt_creds to create unencrypted ) <code>KRB5_ENCTYPE_NULL</code> credentials. This is for use with old MIT server and JAVA based servers as they can&#8217;t handle encrypted <code>KRB-CRED</code> Note that sending such <code>KRB-CRED</code> is clear exposes crypto keys and tickets and is insecure, make sure the packet is encrypted in the protocol. krb5_rd_cred3, krb5_rd_priv3, krb5_rd_safe3, krb5_mk_priv3 and krb5_mk_safe3. Setting this flag requires that parameter to be passed to these functions. </p>
<p> The flags <code>KRB5_AUTH_CONTEXT_DO_TIME</code> also modifies the behavior the function Fn krb5_get_forwarded_creds by removing the timestamp in the forward credential message, this have backward compatibility problems since not all versions of the heimdal supports timeless credentional messages. Is very useful since it always the sender of the message to cache forward message and thus avoiding a round trip to the KDC for each time a credential is forwarded. The same functionality can be obtained by using address-less tickets.</dl>
<p> Fn krb5_auth_con_setaddrs , Fn krb5_auth_con_setaddrs_from_fd and Fn krb5_auth_con_getaddrs gets and sets the addresses that are checked when a packet is received. It is mandatory to set an address for the remote host. If the local address is not set, it iss deduced from the underlaying operating system. Fn krb5_auth_con_getaddrs will call Fn krb5_free_address on any address that is passed in Fa local_addr or Fa remote_addr . Fn krb5_auth_con_setaddr allows passing in a <code>NULL</code> pointer as Fa local_addr and Fa remote_addr , in that case it will just not set that address. </p>
<p> Fn krb5_auth_con_setaddrs_from_fd fetches the addresses from a file descriptor. </p>
<p> Fn krb5_auth_con_genaddrs fetches the address information from the given file descriptor Fa fd depending on the bitmap argument Fa flags . </p>
<p> Possible values on Fa flags are:</p>
<dl>
<dt><i>KRB5_AUTH_CONTEXT_GENERATE_LOCAL_ADDR</i></p>
<dd> fetches the local address from Fa fd .</p>
<dt><i>KRB5_AUTH_CONTEXT_GENERATE_REMOTE_ADDR</i></p>
<dd> fetches the remote address from Fa fd .</dl>
<p> Fn krb5_auth_con_setkey , Fn krb5_auth_con_setuserkey and Fn krb5_auth_con_getkey gets and sets the key used for this auth context. The keyblock returned by Fn krb5_auth_con_getkey should be freed with Fn krb5_free_keyblock . The keyblock send into Fn krb5_auth_con_setkey is copied into the <code>krb5_auth_context</code> and thus no special handling is needed. <code>NULL</code> is not a valid keyblock to Fn krb5_auth_con_setkey . </p>
<p> Fn krb5_auth_con_setuserkey is only useful when doing user to user authentication. Fn krb5_auth_con_setkey is equivalent to Fn krb5_auth_con_setuserkey . </p>
<p> Fn krb5_auth_con_getlocalsubkey , Fn krb5_auth_con_setlocalsubkey , Fn krb5_auth_con_getremotesubkey and Fn krb5_auth_con_setremotesubkey gets and sets the keyblock for the local and remote subkey. The keyblock returned by Fn krb5_auth_con_getlocalsubkey and Fn krb5_auth_con_getremotesubkey must be freed with Fn krb5_free_keyblock . </p>
<p> Fn krb5_auth_setcksumtype and Fn krb5_auth_getcksumtype sets and gets the checksum type that should be used for this connection. </p>
<p> Fn krb5_auth_con_generatelocalsubkey generates a local subkey that have the same encryption type as Fa key . </p>
<p> Fn krb5_auth_getremoteseqnumber Fn krb5_auth_setremoteseqnumber , Fn krb5_auth_getlocalseqnumber and Fn krb5_auth_setlocalseqnumber gets and sets the sequence-number for the local and remote sequence-number counter. </p>
<p> Fn krb5_auth_setkeytype and Fn krb5_auth_getkeytype gets and gets the keytype of the keyblock in <code>krb5_auth_context</code> </p>
<p> Fn krb5_auth_con_getauthenticator Retrieves the authenticator that was used during mutual authentication. The <code>authenticator</code> returned should be freed by calling Fn krb5_free_authenticator . </p>
<p> Fn krb5_auth_con_getrcache and Fn krb5_auth_con_setrcache gets and sets the replay-cache. </p>
<p> Fn krb5_auth_con_initivector allocates memory for and zeros the initial vector in the Fa auth_context keyblock. </p>
<p> Fn krb5_auth_con_setivector sets the i_vector portion of Fa auth_context to Fa ivector . </p>
<p> Fn krb5_free_authenticator free the content of Fa authenticator and Fa authenticator itself.</p>
<h2>SEE ALSO</h2>
<p> krb5_context3, <a href="/docs/linux/man/8-kerberos/">kerberos</a>(8) </p>
<h2>Index</h2>
