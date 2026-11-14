---
title: "krb5_decrypt_ticket(3)"
name: "krb5_decrypt_ticket"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_decrypt_ticket/"
description: "krb5_crypto_getblocksize krb5_crypto_getconfoundersize krb5_crypto_getenctype krb5_crypto_getpadsize krb5_crypto_overhead krb5_decrypt krb5_decrypt_EncryptedData krb5_decrypt_ivec krb5_decrypt_tick..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_crypto_getblocksize</code> <code>krb5_crypto_getconfoundersize</code> <code>krb5_crypto_getenctype</code> <code>krb5_crypto_getpadsize</code> <code>krb5_crypto_overhead</code> <code>krb5_decrypt</code> <code>krb5_decrypt_EncryptedData</code> <code>krb5_decrypt_ivec</code> <code>krb5_decrypt_ticket</code> <code>krb5_encrypt</code> <code>krb5_encrypt_EncryptedData</code> <code>krb5_encrypt_ivec</code> <code>krb5_enctype_disable</code> <code>krb5_enctype_keysize</code> <code>krb5_enctype_to_string</code> <code>krb5_enctype_valid</code> <code>krb5_get_wrapped_length</code> <code>krb5_string_to_enctype</code> &#8211; encrypt and decrypt data, set and get encryption type parameters </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_encrypt Fa krb5_context context Fa krb5_crypto crypto Fa unsigned usage Fa void *data Fa size_t len Fa krb5_data *result Fc Ft krb5_error_code Fo krb5_encrypt_EncryptedData Fa krb5_context context Fa krb5_crypto crypto Fa unsigned usage Fa void *data Fa size_t len Fa int kvno Fa EncryptedData *result Fc Ft krb5_error_code Fo krb5_encrypt_ivec Fa krb5_context context Fa krb5_crypto crypto Fa unsigned usage Fa void *data Fa size_t len Fa krb5_data *result Fa void *ivec Fc Ft krb5_error_code Fo krb5_decrypt Fa krb5_context context Fa krb5_crypto crypto Fa unsigned usage Fa void *data Fa size_t len Fa krb5_data *result Fc Ft krb5_error_code Fo krb5_decrypt_EncryptedData Fa krb5_context context Fa krb5_crypto crypto Fa unsigned usage Fa EncryptedData *e Fa krb5_data *result Fc Ft krb5_error_code Fo krb5_decrypt_ivec Fa krb5_context context Fa krb5_crypto crypto Fa unsigned usage Fa void *data Fa size_t len Fa krb5_data *result Fa void *ivec Fc Ft krb5_error_code Fo krb5_decrypt_ticket Fa krb5_context context Fa Ticket *ticket Fa krb5_keyblock *key Fa EncTicketPart *out Fa krb5_flags flags Fc Ft krb5_error_code Fo krb5_crypto_getblocksize Fa krb5_context context Fa size_t *blocksize Fc Ft krb5_error_code Fo krb5_crypto_getenctype Fa krb5_context context Fa krb5_crypto crypto Fa krb5_enctype *enctype Fc Ft krb5_error_code Fo krb5_crypto_getpadsize Fa krb5_context context Fa size_t *padsize Fc Ft krb5_error_code Fo krb5_crypto_getconfoundersize Fa krb5_context context Fa krb5_crypto crypto Fa size_t *confoundersize Fc Ft krb5_error_code Fo krb5_enctype_keysize Fa krb5_context context Fa krb5_enctype type Fa size_t *keysize Fc Ft krb5_error_code Fo krb5_crypto_overhead Fa krb5_context context Fa size_t *padsize Fc Ft krb5_error_code Fo krb5_string_to_enctype Fa krb5_context context Fa const char *string Fa krb5_enctype *etype Fc Ft krb5_error_code Fo krb5_enctype_to_string Fa krb5_context context Fa krb5_enctype etype Fa char **string Fc Ft krb5_error_code Fo krb5_enctype_valid Fa krb5_context context Fa krb5_enctype etype Fc Ft void Fo krb5_enctype_disable Fa krb5_context context Fa krb5_enctype etype Fc Ft size_t Fo krb5_get_wrapped_length Fa krb5_context context Fa krb5_crypto crypto Fa size_t data_len Fc</p>
<h2>DESCRIPTION</h2>
<p> These functions are used to encrypt and decrypt data. </p>
<p> Fn krb5_encrypt_ivec puts the encrypted version of Fa data (of size Fa len ) in Fa result . If the encryption type supports using derived keys, Fa usage should be the appropriate key-usage. Fa ivec is a pointer to a initial IV, it is modified to the end IV at the end of the round. Ivec should be the size of If <code>NULL</code> is passed in, the default IV is used. Fn krb5_encrypt does the same as Fn krb5_encrypt_ivec but with Fa ivec being <code>NULL</code> Fn krb5_encrypt_EncryptedData does the same as Fn krb5_encrypt , but it puts the encrypted data in a Fa EncryptedData structure instead. If Fa kvno is not zero, it will be put in the (optional) Fa kvno field in the Fa EncryptedData . </p>
<p> Fn krb5_decrypt_ivec , Fn krb5_decrypt , and Fn krb5_decrypt_EncryptedData works similarly. </p>
<p> Fn krb5_decrypt_ticket decrypts the encrypted part of Fa ticket with Fa key . Fn krb5_decrypt_ticket also verifies the timestamp in the ticket, invalid flag and if the KDC haven&#8217;t verified the transited path, the transit path. </p>
<p> Fn krb5_enctype_keysize , Fn krb5_crypto_getconfoundersize , Fn krb5_crypto_getblocksize , Fn krb5_crypto_getenctype , Fn krb5_crypto_getpadsize , Fn krb5_crypto_overhead all returns various (sometimes) useful information from a crypto context. Fn krb5_crypto_overhead is the combination of krb5_crypto_getconfoundersize, krb5_crypto_getblocksize and krb5_crypto_getpadsize and return the maximum overhead size. </p>
<p> Fn krb5_enctype_to_string converts a encryption type number to a string that can be printable and stored. The strings returned should be freed with <a href="/docs/linux/man/3-free/">free</a>(3). </p>
<p> Fn krb5_string_to_enctype converts a encryption type strings to a encryption type number that can use used for other Kerberos crypto functions. </p>
<p> Fn krb5_enctype_valid returns 0 if the encrypt is supported and not disabled, otherwise and error code is returned. </p>
<p> Fn krb5_enctype_disable (globally, for all contextes) disables the Fa enctype . </p>
<p> Fn krb5_get_wrapped_length returns the size of an encrypted packet by Fa crypto of length Fa data_len .</p>
<h2>SEE ALSO</h2>
<p> krb5_create_checksum3, krb5_crypto_init3 </p>
<h2>Index</h2>
