---
title: "krb5_checksum_is_collision_proof(3)"
name: "krb5_checksum_is_collision_proof"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_checksum_is_collision_proof/"
description: "krb5_checksum krb5_checksum_disable krb5_checksum_is_collision_proof krb5_checksum_is_keyed krb5_checksumsize krb5_cksumtype_valid krb5_copy_checksum krb5_create_checksum krb5_crypto_get_checksum_t..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_checksum</code> <code>krb5_checksum_disable</code> <code>krb5_checksum_is_collision_proof</code> <code>krb5_checksum_is_keyed</code> <code>krb5_checksumsize</code> <code>krb5_cksumtype_valid</code> <code>krb5_copy_checksum</code> <code>krb5_create_checksum</code> <code>krb5_crypto_get_checksum_type</code> <code>krb5_free_checksum</code> <code>krb5_free_checksum_contents</code> <code>krb5_hmac</code> <code>krb5_verify_checksum</code> &#8211; creates, handles and verifies checksums </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> <code>typedef Checksum krb5_checksum;</code> Ft void Fo krb5_checksum_disable Fa krb5_context context Fa krb5_cksumtype type Fc Ft krb5_boolean Fo krb5_checksum_is_collision_proof Fa krb5_context context Fa krb5_cksumtype type Fc Ft krb5_boolean Fo krb5_checksum_is_keyed Fa krb5_context context Fa krb5_cksumtype type Fc Ft krb5_error_code Fo krb5_cksumtype_valid Fa krb5_context context Fa krb5_cksumtype ctype Fc Ft krb5_error_code Fo krb5_checksumsize Fa krb5_context context Fa krb5_cksumtype type Fa size_t *size Fc Ft krb5_error_code Fo krb5_create_checksum Fa krb5_context context Fa krb5_crypto crypto Fa krb5_key_usage usage Fa int type Fa void *data Fa size_t len Fa Checksum *result Fc Ft krb5_error_code Fo krb5_verify_checksum Fa krb5_context context Fa krb5_crypto crypto Fa krb5_key_usage usage Fa void *data Fa size_t len Fa Checksum *cksum Fc Ft krb5_error_code Fo krb5_crypto_get_checksum_type Fa krb5_context context Fa krb5_crypto crypto Fa krb5_cksumtype *type Fc Ft void Fo krb5_free_checksum Fa krb5_context context Fa krb5_checksum *cksum Fc Ft void Fo krb5_free_checksum_contents Fa krb5_context context Fa krb5_checksum *cksum Fc Ft krb5_error_code Fo krb5_hmac Fa krb5_context context Fa krb5_cksumtype cktype Fa const void *data Fa size_t len Fa unsigned usage Fa krb5_keyblock *key Fa Checksum *result Fc Ft krb5_error_code Fo krb5_copy_checksum Fa krb5_context context Fa const krb5_checksum *old Fa krb5_checksum **new Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>krb5_checksum</code> structure holds a Kerberos checksum. There is no component inside <code>krb5_checksum</code> that is directly referable. </p>
<p> The functions are used to create and verify checksums. Fn krb5_create_checksum creates a checksum of the specified data, and puts it in Fa result . If Fa crypto is <code>NULL</code> Fa usage_or_type specifies the checksum type to use; it must not be keyed. Otherwise Fa crypto is an encryption context created by Fn krb5_crypto_init , and Fa usage_or_type specifies a key-usage. </p>
<p> Fn krb5_verify_checksum verifies the Fa checksum against the provided data. </p>
<p> Fn krb5_checksum_is_collision_proof returns true is the specified checksum is collision proof (that it&#8217;s very unlikely that two strings has the same hash value, and that it&#8217;s hard to find two strings that has the same hash). Examples of collision proof checksums are MD5, and SHA1, while CRC32 is not. </p>
<p> Fn krb5_checksum_is_keyed returns true if the specified checksum type is keyed (that the hash value is a function of both the data, and a separate key). Examples of keyed hash algorithms are HMAC-SHA1-DES3, and RSA-MD5-DES. The &#8220;plain&#8221; hash functions MD5, and SHA1 are not keyed. </p>
<p> Fn krb5_crypto_get_checksum_type returns the checksum type that will be used when creating a checksum for the given Fa crypto context. This function is useful in combination with Fn krb5_checksumsize when you want to know the size a checksum will use when you create it. </p>
<p> Fn krb5_cksumtype_valid returns 0 or an error if the checksumtype is implemented and not currently disabled in this kerberos library. </p>
<p> Fn krb5_checksumsize returns the size of the outdata of checksum function. </p>
<p> Fn krb5_copy_checksum returns a copy of the checksum Fn krb5_free_checksum should use used to free the Fa new checksum. </p>
<p> Fn krb5_free_checksum free the checksum and the content of the checksum. </p>
<p> Fn krb5_free_checksum_contents frees the content of checksum in Fa cksum . </p>
<p> Fn krb5_hmac calculates the HMAC over Fa data (with length Fa len ) using the keyusage Fa usage and keyblock Fa key . Note that keyusage is not always used in checksums. </p>
<p> <code>krb5_checksum_disable</code> globally disables the checksum type.</p>
<h2>SEE ALSO</h2>
<p> krb5_crypto_init3, krb5_c_encrypt3, krb5_encrypt3 </p>
<h2>Index</h2>
