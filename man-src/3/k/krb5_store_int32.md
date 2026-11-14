---
title: "krb5_store_int32(3)"
name: "krb5_store_int32"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_store_int32/"
description: "Heimdal Kerberos 5 storage functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 storage functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_address</code> (krb5_storage *, krb5_address *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_addrs</code> (krb5_storage *, krb5_addresses *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_authdata</code> (krb5_storage *, krb5_authdata *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_creds</code> (krb5_storage *, krb5_creds *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_creds_tag</code> (krb5_storage *, krb5_creds *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_data</code> (krb5_storage *, krb5_data *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_int16</code> (krb5_storage *, int16_t *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_int32</code> (krb5_storage *, int32_t *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_int8</code> (krb5_storage *, int8_t *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_keyblock</code> (krb5_storage *, krb5_keyblock *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_principal</code> (krb5_storage *, krb5_principal *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_string</code> (krb5_storage *, char **)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_stringz</code> (krb5_storage *, char **)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_times</code> (krb5_storage *, krb5_times *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_uint16</code> (krb5_storage *, uint16_t *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_uint32</code> (krb5_storage *, uint32_t *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ret_uint8</code> (krb5_storage *, uint8_t *)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_storage_clear_flags</code> (krb5_storage *, krb5_flags)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_storage<br />
 *KRB5_LIB_CALL <code>krb5_storage_emem</code> (void)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_storage_free</code> (krb5_storage *)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_storage<br />
 *KRB5_LIB_CALL <code>krb5_storage_from_data</code> (krb5_data *)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_storage<br />
 *KRB5_LIB_CALL <code>krb5_storage_from_fd</code> (int)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_storage<br />
 *KRB5_LIB_CALL <code>krb5_storage_from_mem</code> (void *, size_t)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_storage<br />
 *KRB5_LIB_CALL <code>krb5_storage_from_readonly_mem</code> (const void *, size_t)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_storage<br />
 *KRB5_LIB_CALL <code>krb5_storage_from_socket</code> (krb5_socket_t)&quot; </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_storage_fsync</code> (krb5_storage *) </p>
<p> KRB5_LIB_FUNCTION krb5_flags<br />
 KRB5_LIB_CALL <code>krb5_storage_get_byteorder</code> (krb5_storage *)&quot; </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_storage_get_eof_code</code> (krb5_storage *) </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_storage_is_flags</code> (krb5_storage *, krb5_flags)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_ssize_t<br />
 KRB5_LIB_CALL <code>krb5_storage_read</code> (krb5_storage *, void *, size_t)&quot; </p>
<p> KRB5_LIB_FUNCTION off_t<br />
 KRB5_LIB_CALL <code>krb5_storage_seek</code> (krb5_storage *, off_t, int)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_storage_set_byteorder</code> (krb5_storage *, krb5_flags)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_storage_set_eof_code</code> (krb5_storage *, int)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_storage_set_flags</code> (krb5_storage *, krb5_flags)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_storage_set_max_alloc</code> (krb5_storage *, size_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_storage_to_data</code> (krb5_storage *, krb5_data *)&quot; </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_storage_truncate</code> (krb5_storage *, off_t) </p>
<p> KRB5_LIB_FUNCTION krb5_ssize_t<br />
 KRB5_LIB_CALL <code>krb5_storage_write</code> (krb5_storage *, const void *, size_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_address</code> (krb5_storage *, krb5_address)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_addrs</code> (krb5_storage *, krb5_addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_authdata</code> (krb5_storage *, krb5_authdata)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_creds</code> (krb5_storage *, krb5_creds *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_creds_tag</code> (krb5_storage *, krb5_creds *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_data</code> (krb5_storage *, krb5_data)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_int16</code> (krb5_storage *, int16_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_int32</code> (krb5_storage *, int32_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_int8</code> (krb5_storage *, int8_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_keyblock</code> (krb5_storage *, krb5_keyblock)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_principal</code> (krb5_storage *, krb5_const_principal)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_string</code> (krb5_storage *, const char *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_stringz</code> (krb5_storage *, const char *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_times</code> (krb5_storage *, krb5_times)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_uint16</code> (krb5_storage *, uint16_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_uint32</code> (krb5_storage *, uint32_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_store_uint8</code> (krb5_storage *, uint8_t)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_address (krb5_storage *sp, krb5_address *adr)</h3>
<p> Read a address block from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>adr</i> the address block read from storage</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_addrs (krb5_storage *sp, krb5_addresses *adr)</h3>
<p> Read a addresses block from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>adr</i> the addresses block read from storage</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_authdata (krb5_storage *sp, krb5_authdata *auth)</h3>
<p> Read a auth data from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>auth</i> the auth data block read from storage</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_creds (krb5_storage *sp, krb5_creds *creds)</h3>
<p> Read a credentials block from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>creds</i> the credentials block read from storage</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_creds_tag (krb5_storage *sp, krb5_creds *creds)</h3>
<p> Read a tagged credentials block from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>creds</i> the credentials block read from storage</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_data (krb5_storage *sp, krb5_data *data)</h3>
<p> Parse a data from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to read from<br />
 <i>data</i> the parsed data</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_int16 (krb5_storage *sp, int16_t *value)</h3>
<p> Read a int16 from storage, byte order is controlled by the settings on the storage, see <code>krb5_storage_set_byteorder()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value read from the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_int32 (krb5_storage *sp, int32_t *value)</h3>
<p> Read a int32 from storage, byte order is controlled by the settings on the storage, see <code>krb5_storage_set_byteorder()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value read from the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_int8 (krb5_storage *sp, int8_t *value)</h3>
<p> Read a int8 from storage </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value read from the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_keyblock (krb5_storage *sp, krb5_keyblock *p)</h3>
<p> Read a keyblock from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>p</i> the keyblock read from storage, free using <code>krb5_free_keyblock()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_principal (krb5_storage *sp, krb5_principal *princ)</h3>
<p> Parse principal from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to read from<br />
 <i>princ</i> the parsed principal</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_string (krb5_storage *sp, char **string)</h3>
<p> Parse a string from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to read from<br />
 <i>string</i> the parsed string</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_stringz (krb5_storage *sp, char **string)</h3>
<p> Parse zero terminated string from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to read from<br />
 <i>string</i> the parsed string</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_times (krb5_storage *sp, krb5_times *times)</h3>
<p> Read a times block from the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>times</i> the times block read from storage</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_uint16 (krb5_storage *sp, uint16_t *value)</h3>
<p> Read a int16 from storage, byte order is controlled by the settings on the storage, see <code>krb5_storage_set_byteorder()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value read from the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_uint32 (krb5_storage *sp, uint32_t *value)</h3>
<p> Read a uint32 from storage, byte order is controlled by the settings on the storage, see <code>krb5_storage_set_byteorder()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value read from the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ret_uint8 (krb5_storage *sp, uint8_t *value)</h3>
<p> Read a uint8 from storage </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value read from the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_storage_clear_flags (krb5_storage *sp, krb5_flagsflags)</h3>
<p> Clear the flags on a storage buffer </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to clear the flags on<br />
 <i>flags</i> the flags to clear</dl>
<h3>KRB5_LIB_FUNCTION krb5_storage *KRB5_LIB_CALL krb5_storage_emem (void)</h3>
<p> Create a elastic (allocating) memory storage backend. Memory is allocated on demand. Free returned krb5_storage with <code>krb5_storage_free()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A krb5_storage on success, or NULL on out of memory error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>krb5_storage_from_mem()</code> </p>
<p> <code>krb5_storage_from_readonly_mem()</code> </p>
<p> <code>krb5_storage_from_fd()</code> </p>
<p> <code>krb5_storage_from_data()</code> </p>
<p> <code>krb5_storage_from_socket()</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_storage_free (krb5_storage *sp)</h3>
<p> Free a krb5 storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An Kerberos 5 error code.</dl>
<h3>KRB5_LIB_FUNCTION krb5_storage *KRB5_LIB_CALL krb5_storage_from_data (krb5_data *data)</h3>
<p> Create a fixed size memory storage block </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A krb5_storage on success, or NULL on out of memory error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> krb5_storage_mem() </p>
<p> <code>krb5_storage_from_mem()</code> </p>
<p> <code>krb5_storage_from_readonly_mem()</code> </p>
<p> <code>krb5_storage_from_fd()</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_storage *KRB5_LIB_CALL krb5_storage_from_fd (intfd_in)</h3>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A krb5_storage on success, or NULL on out of memory error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>krb5_storage_emem()</code> </p>
<p> <code>krb5_storage_from_mem()</code> </p>
<p> <code>krb5_storage_from_readonly_mem()</code> </p>
<p> <code>krb5_storage_from_data()</code> </p>
<p> <code>krb5_storage_from_socket()</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_storage *KRB5_LIB_CALL krb5_storage_from_mem (void *buf, size_tlen)</h3>
<p> Create a fixed size memory storage block </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A krb5_storage on success, or NULL on out of memory error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> krb5_storage_mem() </p>
<p> <code>krb5_storage_from_readonly_mem()</code> </p>
<p> <code>krb5_storage_from_data()</code> </p>
<p> <code>krb5_storage_from_fd()</code> </p>
<p> <code>krb5_storage_from_socket()</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_storage *KRB5_LIB_CALL krb5_storage_from_readonly_mem (const void *buf, size_tlen)</h3>
<p> Create a fixed size memory storage block that is read only </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A krb5_storage on success, or NULL on out of memory error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> krb5_storage_mem() </p>
<p> <code>krb5_storage_from_mem()</code> </p>
<p> <code>krb5_storage_from_data()</code> </p>
<p> <code>krb5_storage_from_fd()</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_storage *KRB5_LIB_CALL krb5_storage_from_socket (krb5_socket_tsock_in)</h3>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A krb5_storage on success, or NULL on out of memory error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>krb5_storage_emem()</code> </p>
<p> <code>krb5_storage_from_mem()</code> </p>
<p> <code>krb5_storage_from_readonly_mem()</code> </p>
<p> <code>krb5_storage_from_data()</code> </p>
<p> <code>krb5_storage_from_fd()</code></dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_storage_fsync (krb5_storage *sp)</h3>
<p> Sync the storage buffer to its backing store. If there is no backing store this function will return success. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to sync</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A Kerberos 5 error code</dl>
<h3>KRB5_LIB_FUNCTION krb5_flags KRB5_LIB_CALL krb5_storage_get_byteorder (krb5_storage *sp)</h3>
<p> Return the current byteorder for the buffer. See <code>krb5_storage_set_byteorder()</code> for the list or byte order contants.</p>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_storage_get_eof_code (krb5_storage *sp)</h3>
<p> Get the return code that will be used when end of storage is reached. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> storage error code</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_storage_is_flags (krb5_storage *sp, krb5_flagsflags)</h3>
<p> Return true or false depending on if the storage flags is set or not. NB testing for the flag 0 always return true. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to check flags on<br />
 <i>flags</i> The flags to test for</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> true if all the flags are set, false if not.</dl>
<h3>KRB5_LIB_FUNCTION krb5_ssize_t KRB5_LIB_CALL krb5_storage_read (krb5_storage *sp, void *buf, size_tlen)</h3>
<p> Read to the storage buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to read from<br />
 <i>buf</i> the buffer to store the data in<br />
 <i>len</i> the length to read</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The length of data read (can be shorter then len), or negative on error.</dl>
<h3>KRB5_LIB_FUNCTION off_t KRB5_LIB_CALL krb5_storage_seek (krb5_storage *sp, off_toffset, intwhence)</h3>
<p> Seek to a new offset. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to seek in.<br />
 <i>offset</i> the offset to seek<br />
 <i>whence</i> relateive searching, SEEK_CUR from the current position, SEEK_END from the end, SEEK_SET absolute from the start.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The new current offset</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_storage_set_byteorder (krb5_storage *sp, krb5_flagsbyteorder)</h3>
<p> Set the new byte order of the storage buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to set the byte order for.<br />
 <i>byteorder</i> the new byte order.</dl>
<p> The byte order are: KRB5_STORAGE_BYTEORDER_BE, KRB5_STORAGE_BYTEORDER_LE and KRB5_STORAGE_BYTEORDER_HOST.</p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_storage_set_eof_code (krb5_storage *sp, intcode)</h3>
<p> Set the return code that will be used when end of storage is reached. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage<br />
 <i>code</i> the error code to return on end of storage</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_storage_set_flags (krb5_storage *sp, krb5_flagsflags)</h3>
<p> Add the flags on a storage buffer by or-ing in the flags to the buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to set the flags on<br />
 <i>flags</i> the flags to set</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_storage_set_max_alloc (krb5_storage *sp, size_tsize)</h3>
<p> Set the max alloc value </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer set the max allow for<br />
 <i>size</i> maximum size to allocate, use 0 to remove limit</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_storage_to_data (krb5_storage *sp, krb5_data *data)</h3>
<p> Copy the contnent of storage </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to copy to a data<br />
 <i>data</i> the copied data, free with <code>krb5_data_free()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_storage_truncate (krb5_storage *sp, off_toffset)</h3>
<p> Truncate the storage buffer in sp to offset. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to truncate.<br />
 <i>offset</i> the offset to truncate too.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An Kerberos 5 error code.</dl>
<h3>KRB5_LIB_FUNCTION krb5_ssize_t KRB5_LIB_CALL krb5_storage_write (krb5_storage *sp, const void *buf, size_tlen)</h3>
<p> Write to the storage buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>buf</i> the buffer to write to the storage buffer<br />
 <i>len</i> the length to write</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The length of data written (can be shorter then len), or negative on error.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_address (krb5_storage *sp, krb5_addressp)</h3>
<p> Write a address block to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>p</i> the address block to write.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_addrs (krb5_storage *sp, krb5_addressesp)</h3>
<p> Write a addresses block to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>p</i> the addresses block to write.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_authdata (krb5_storage *sp, krb5_authdataauth)</h3>
<p> Write a auth data block to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>auth</i> the auth data block to write.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_creds (krb5_storage *sp, krb5_creds *creds)</h3>
<p> Write a credentials block to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>creds</i> the creds block to write.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_creds_tag (krb5_storage *sp, krb5_creds *creds)</h3>
<p> Write a tagged credentials block to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>creds</i> the creds block to write.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_data (krb5_storage *sp, krb5_datadata)</h3>
<p> Store a data to the storage. The data is stored with an int32 as lenght plus the data (not padded). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>data</i> the buffer to store.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_int16 (krb5_storage *sp, int16_tvalue)</h3>
<p> Store a int16 to storage, byte order is controlled by the settings on the storage, see <code>krb5_storage_set_byteorder()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value to store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_int32 (krb5_storage *sp, int32_tvalue)</h3>
<p> Store a int32 to storage, byte order is controlled by the settings on the storage, see <code>krb5_storage_set_byteorder()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value to store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_int8 (krb5_storage *sp, int8_tvalue)</h3>
<p> Store a int8 to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value to store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_keyblock (krb5_storage *sp, krb5_keyblockp)</h3>
<p> Store a keyblock to the storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>p</i> the keyblock to write</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_principal (krb5_storage *sp, krb5_const_principalp)</h3>
<p> Write a principal block to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>p</i> the principal block to write.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_string (krb5_storage *sp, const char *s)</h3>
<p> Store a string to the buffer. The data is formated as an len:uint32 plus the string itself (not padded). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>s</i> the string to store.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_stringz (krb5_storage *sp, const char *s)</h3>
<p> Store a zero terminated string to the buffer. The data is stored one character at a time until a NUL is stored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>s</i> the string to store.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_times (krb5_storage *sp, krb5_timestimes)</h3>
<p> Write a times block to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage buffer to write to<br />
 <i>times</i> the times block to write.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_uint16 (krb5_storage *sp, uint16_tvalue)</h3>
<p> Store a uint16 to storage, byte order is controlled by the settings on the storage, see <code>krb5_storage_set_byteorder()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value to store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_uint32 (krb5_storage *sp, uint32_tvalue)</h3>
<p> Store a uint32 to storage, byte order is controlled by the settings on the storage, see <code>krb5_storage_set_byteorder()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value to store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_store_uint8 (krb5_storage *sp, uint8_tvalue)</h3>
<p> Store a uint8 to storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sp</i> the storage to write too<br />
 <i>value</i> the value to store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or a Kerberos 5 error code on failure.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
