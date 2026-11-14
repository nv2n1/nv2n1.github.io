---
title: "krb5_c_make_checksum(3)"
name: "krb5_c_make_checksum"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_c_make_checksum/"
description: "krb5_c_block_size krb5_c_decrypt krb5_c_encrypt krb5_c_encrypt_length krb5_c_enctype_compare krb5_c_get_checksum krb5_c_is_coll_proof_cksum krb5_c_is_keyed_cksum krb5_c_keylength krb5_c_make_checks..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_c_block_size</code> <code>krb5_c_decrypt</code> <code>krb5_c_encrypt</code> <code>krb5_c_encrypt_length</code> <code>krb5_c_enctype_compare</code> <code>krb5_c_get_checksum</code> <code>krb5_c_is_coll_proof_cksum</code> <code>krb5_c_is_keyed_cksum</code> <code>krb5_c_keylength</code> <code>krb5_c_make_checksum</code> <code>krb5_c_make_random_key</code> <code>krb5_c_set_checksum</code> <code>krb5_c_valid_cksumtype</code> <code>krb5_c_valid_enctype</code> <code>krb5_c_verify_checksum</code> <code>krb5_c_checksum_length</code> &#8211; Kerberos 5 crypto API </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> Ft krb5_error_code Fo krb5_c_block_size Fa krb5_context context Fa krb5_enctype enctype Fa size_t *blocksize Fc Ft krb5_error_code Fo krb5_c_decrypt Fa krb5_context context Fa const krb5_keyblock key Fa krb5_keyusage usage Fa const krb5_data *ivec Fa krb5_enc_data *input Fa krb5_data *output Fc Ft krb5_error_code Fo krb5_c_encrypt Fa krb5_context context Fa const krb5_keyblock *key Fa krb5_keyusage usage Fa const krb5_data *ivec Fa const krb5_data *input Fa krb5_enc_data *output Fc Ft krb5_error_code Fo krb5_c_encrypt_length Fa krb5_context context Fa krb5_enctype enctype Fa size_t inputlen Fa size_t *length Fc Ft krb5_error_code Fo krb5_c_enctype_compare Fa krb5_context context Fa krb5_enctype e1 Fa krb5_enctype e2 Fa krb5_boolean *similar Fc Ft krb5_error_code Fo krb5_c_make_random_key Fa krb5_context context Fa krb5_enctype enctype Fa krb5_keyblock *random_key Fc Ft krb5_error_code Fo krb5_c_make_checksum Fa krb5_context context Fa krb5_cksumtype cksumtype Fa const krb5_keyblock *key Fa krb5_keyusage usage Fa const krb5_data *input Fa krb5_checksum *cksum Fc Ft krb5_error_code Fo krb5_c_verify_checksum Fa krb5_context context Fa const krb5_keyblock *key Fa krb5_keyusage usage Fa const krb5_data *data Fa const krb5_checksum *cksum Fa krb5_boolean *valid Fc Ft krb5_error_code Fo krb5_c_checksum_length Fa krb5_context context Fa krb5_cksumtype cksumtype Fa size_t *length Fc Ft krb5_error_code Fo krb5_c_get_checksum Fa krb5_context context Fa const krb5_checksum *cksum Fa krb5_cksumtype *type Fa krb5_data **data Fc Ft krb5_error_code Fo krb5_c_set_checksum Fa krb5_context context Fa krb5_checksum *cksum Fa krb5_cksumtype type Fa const krb5_data *data Fc Ft krb5_boolean Fo krb5_c_valid_enctype Fa krb5_enctype etype Fc Ft krb5_boolean Fo krb5_c_valid_cksumtype Fa krb5_cksumtype ctype Fc Ft krb5_boolean Fo krb5_c_is_coll_proof_cksum Fa krb5_cksumtype ctype Fc Ft krb5_boolean Fo krb5_c_is_keyed_cksum Fa krb5_cksumtype ctype Fc Ft krb5_error_code Fo krb5_c_keylengths Fa krb5_context context Fa krb5_enctype enctype Fa size_t *inlength Fa size_t *keylength Fc</p>
<h2>DESCRIPTION</h2>
<p> The functions starting with krb5_c are compat functions with MIT kerberos. </p>
<p> The <code>krb5_enc_data</code> structure holds and encrypted data. There are two public accessable members of <code>krb5_enc_data</code> <code>enctype</code> that holds the encryption type of the data encrypted and <code>ciphertext</code> that is a Ft krb5_data that might contain the encrypted data. </p>
<p> Fn krb5_c_block_size returns the blocksize of the encryption type. </p>
<p> Fn krb5_c_decrypt decrypts Fa input and store the data in Fa output. If Fa ivec is <code>NULL</code> the default initialization vector for that encryption type will be used. </p>
<p> Fn krb5_c_encrypt encrypts the plaintext in Fa input and store the ciphertext in Fa output . </p>
<p> Fn krb5_c_encrypt_length returns the length the encrypted data given the plaintext length. </p>
<p> Fn krb5_c_enctype_compare compares to encryption types and returns if they use compatible encryption key types. </p>
<p> Fn krb5_c_make_checksum creates a checksum Fa cksum with the checksum type Fa cksumtype of the data in Fa data . Fa key and Fa usage are used if the checksum is a keyed checksum type. Returns 0 or an error code. </p>
<p> Fn krb5_c_verify_checksum verifies the checksum of Fa data in Fa cksum that was created with Fa key using the key usage Fa usage . Fa verify is set to non-zero if the checksum verifies correctly and zero if not. Returns 0 or an error code. </p>
<p> Fn krb5_c_checksum_length returns the length of the checksum. </p>
<p> Fn krb5_c_set_checksum sets the <code>krb5_checksum</code> structure given Fa type and Fa data . The content of Fa cksum should be freeed with Fn krb5_c_free_checksum_contents . </p>
<p> Fn krb5_c_get_checksum retrieves the components of the <code>krb5_checksum</code> structure. Fa data should be free with Fn krb5_free_data . If some either of Fa data or Fa checksum is not needed for the application, <code>NULL</code> can be passed in. </p>
<p> Fn krb5_c_valid_enctype returns true if Fa etype is a valid encryption type. </p>
<p> Fn krb5_c_valid_cksumtype returns true if Fa ctype is a valid checksum type. </p>
<p> Fn krb5_c_is_keyed_cksum return true if Fa ctype is a keyed checksum type. </p>
<p> Fn krb5_c_is_coll_proof_cksum returns true if Fa ctype is a collision proof checksum type. </p>
<p> Fn krb5_c_keylengths return the minimum length Fa ( inlength ) bytes needed to create a key and the length Fa ( keylength ) of the resulting key for the Fa enctype .</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_create_checksum3, krb5_free_data3, <a href="/docs/linux/man/8-kerberos/">kerberos</a>(8) </p>
<h2>Index</h2>
