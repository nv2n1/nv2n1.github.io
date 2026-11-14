---
title: "heim_ntlm_encode_targetinfo(3)"
name: "heim_ntlm_encode_targetinfo"
section: "3"
letter: "h"
url: "/docs/linux/man/3-heim_ntlm_encode_targetinfo/"
description: "Heimdal NTLM library –"
---

<h2 class="name">NAME</h2>
<p> Heimdal NTLM library &#8211; </p>
<h3>Functions</h3>
<p> int <code>heim_ntlm_build_ntlm1_master</code> (void *, size_t, struct <code>ntlm_buf</code> *, struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_build_ntlm2_master</code> (void *, size_t, struct <code>ntlm_buf</code> *, struct <code>ntlm_buf</code> *, struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_calculate_lm2</code> (const void *, size_t, const char *, const char *, const unsigned char serverchallenge[8], unsigned char ntlmv2[16], struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_calculate_ntlm1</code> (void *, size_t, unsigned char challenge[8], struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_calculate_ntlm2</code> (const void *, size_t, const char *, const char *, const unsigned char serverchallenge[8], const struct <code>ntlm_buf</code> *, unsigned char ntlmv2[16], struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_decode_targetinfo</code> (const struct <code>ntlm_buf</code> *, int, struct ntlm_targetinfo *) </p>
<p> int <code>heim_ntlm_encode_targetinfo</code> (const struct ntlm_targetinfo *, int, struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_encode_type1</code> (const struct <code>ntlm_type1</code> *, struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_encode_type2</code> (const struct <code>ntlm_type2</code> *, struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_encode_type3</code> (const struct <code>ntlm_type3</code> *, struct <code>ntlm_buf</code> *, size_t *) </p>
<p> void <code>heim_ntlm_free_buf</code> (struct <code>ntlm_buf</code> *) </p>
<p> void <code>heim_ntlm_free_targetinfo</code> (struct ntlm_targetinfo *) </p>
<p> void <code>heim_ntlm_free_type1</code> (struct <code>ntlm_type1</code> *) </p>
<p> void <code>heim_ntlm_free_type2</code> (struct <code>ntlm_type2</code> *) </p>
<p> void <code>heim_ntlm_free_type3</code> (struct <code>ntlm_type3</code> *) </p>
<p> int <code>heim_ntlm_keyex_unwrap</code> (struct <code>ntlm_buf</code> *, struct <code>ntlm_buf</code> *, struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_nt_key</code> (const char *, struct <code>ntlm_buf</code> *) </p>
<p> int <code>heim_ntlm_ntlmv2_key</code> (const void *, size_t, const char *, const char *, int, unsigned char ntlmv2[16]) </p>
<p> int <code>heim_ntlm_verify_ntlm2</code> (const void *, size_t, const char *, const char *, time_t, const unsigned char serverchallenge[8], const struct <code>ntlm_buf</code> *, struct <code>ntlm_buf</code> *, unsigned char ntlmv2[16]) </p>
<h2>Detailed Description</h2>
<p> The NTLM core functions implement the string2key generation function, message encode and decode function, and the hash function functions.</p>
<h2>Function Documentation</h2>
<h3>int heim_ntlm_build_ntlm1_master (void *key, size_tlen, struct <code>ntlm_buf</code> *session, struct <code>ntlm_buf</code> *master)</h3>
<p> Generates an NTLMv1 session random with assosited session master key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the ntlm v1 key<br />
 <i>len</i> length of key<br />
 <i>session</i> generated session nonce, should be freed with <code>heim_ntlm_free_buf()</code>.<br />
 <i>master</i> calculated session master key, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<h3>int heim_ntlm_build_ntlm2_master (void *key, size_tlen, struct <code>ntlm_buf</code> *blob, struct <code>ntlm_buf</code> *session, struct <code>ntlm_buf</code> *master)</h3>
<p> Generates an NTLMv2 session random with associated session master key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the NTLMv2 key<br />
 <i>len</i> length of key<br />
 <i>blob</i> the NTLMv2 &#8216;blob&#8217;<br />
 <i>session</i> generated session nonce, should be freed with <code>heim_ntlm_free_buf()</code>.<br />
 <i>master</i> calculated session master key, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<h3>int heim_ntlm_calculate_lm2 (const void *key, size_tlen, const char *username, const char *target, const unsigned charserverchallenge[8], unsigned charntlmv2[16], struct <code>ntlm_buf</code> *answer)</h3>
<p> Calculate LMv2 response </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the ntlm key<br />
 <i>len</i> length of key<br />
 <i>username</i> name of the user, as sent in the message, assumed to be in UTF8.<br />
 <i>target</i> the name of the target, assumed to be in UTF8.<br />
 <i>serverchallenge</i> challenge as sent by the server in the type2 message.<br />
 <i>infotarget</i> infotarget as sent by the server in the type2 message.<br />
 <i>ntlmv2</i> calculated session key<br />
 <i>answer</i> ntlm response answer, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<h3>int heim_ntlm_calculate_ntlm1 (void *key, size_tlen, unsigned charchallenge[8], struct <code>ntlm_buf</code> *answer)</h3>
<p> Calculate NTLMv1 response hash </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the ntlm v1 key<br />
 <i>len</i> length of key<br />
 <i>challenge</i> sent by the server<br />
 <i>answer</i> calculated answer, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>int heim_ntlm_calculate_ntlm2 (const void *key, size_tlen, const char *username, const char *target, const unsigned charserverchallenge[8], const struct <code>ntlm_buf</code> *infotarget, unsigned charntlmv2[16], struct <code>ntlm_buf</code> *answer)</h3>
<p> Calculate NTLMv2 response </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the ntlm key<br />
 <i>len</i> length of key<br />
 <i>username</i> name of the user, as sent in the message, assumed to be in UTF8.<br />
 <i>target</i> the name of the target, assumed to be in UTF8.<br />
 <i>serverchallenge</i> challenge as sent by the server in the type2 message.<br />
 <i>infotarget</i> infotarget as sent by the server in the type2 message.<br />
 <i>ntlmv2</i> calculated session key<br />
 <i>answer</i> ntlm response answer, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>int heim_ntlm_decode_targetinfo (const struct <code>ntlm_buf</code> *data, intucs2, struct ntlm_targetinfo *ti)</h3>
<p> Decodes an NTLM targetinfo message </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> input data buffer with the encode NTLM targetinfo message<br />
 <i>ucs2</i> if the strings should be encoded with ucs2 (selected by flag in message).<br />
 <i>ti</i> the decoded target info, should be freed with <code>heim_ntlm_free_targetinfo()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>int heim_ntlm_encode_targetinfo (const struct ntlm_targetinfo *ti, intucs2, struct <code>ntlm_buf</code> *data)</h3>
<p> Encodes a ntlm_targetinfo message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ti</i> the ntlm_targetinfo message to encode.<br />
 <i>ucs2</i> ignored<br />
 <i>data</i> is the return buffer with the encoded message, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>int heim_ntlm_encode_type1 (const struct <code>ntlm_type1</code> *type1, struct <code>ntlm_buf</code> *data)</h3>
<p> Encodes an <code>ntlm_type1</code> message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>type1</i> the <code>ntlm_type1</code> message to encode.<br />
 <i>data</i> is the return buffer with the encoded message, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>int heim_ntlm_encode_type2 (const struct <code>ntlm_type2</code> *type2, struct <code>ntlm_buf</code> *data)</h3>
<p> Encodes an <code>ntlm_type2</code> message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>type2</i> the <code>ntlm_type2</code> message to encode.<br />
 <i>data</i> is the return buffer with the encoded message, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>int heim_ntlm_encode_type3 (const struct <code>ntlm_type3</code> *type3, struct <code>ntlm_buf</code> *data, size_t *mic_offset)</h3>
<p> Encodes an <code>ntlm_type3</code> message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>type3</i> the <code>ntlm_type3</code> message to encode.<br />
 <i>data</i> is the return buffer with the encoded message, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>void heim_ntlm_free_buf (struct <code>ntlm_buf</code> *p)</h3>
<p> heim_ntlm_free_buf frees the ntlm buffer </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>p</i> buffer to be freed</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>void heim_ntlm_free_targetinfo (struct ntlm_targetinfo *ti)</h3>
<p> Frees the ntlm_targetinfo message </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ti</i> targetinfo to be freed</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>void heim_ntlm_free_type1 (struct <code>ntlm_type1</code> *data)</h3>
<p> Frees the <code>ntlm_type1</code> message </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> message to be freed</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>void heim_ntlm_free_type2 (struct <code>ntlm_type2</code> *data)</h3>
<p> Frees the <code>ntlm_type2</code> message </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> message to be freed</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>void heim_ntlm_free_type3 (struct <code>ntlm_type3</code> *data)</h3>
<p> Frees the <code>ntlm_type3</code> message </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> message to be freed</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>int heim_ntlm_keyex_unwrap (struct <code>ntlm_buf</code> *baseKey, struct <code>ntlm_buf</code> *encryptedSession, struct <code>ntlm_buf</code> *session)</h3>
<p> Given a key and encrypted session, unwrap the session key </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>baseKey</i> the sessionBaseKey<br />
 <i>encryptedSession</i> encrypted session, type3.session field.<br />
 <i>session</i> generated session nonce, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<h3>int heim_ntlm_nt_key (const char *password, struct <code>ntlm_buf</code> *key)</h3>
<p> Calculate the NTLM key, the password is assumed to be in UTF8. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>password</i> password to calcute the key for.<br />
 <i>key</i> calcuted key, should be freed with <code>heim_ntlm_free_buf()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>int heim_ntlm_ntlmv2_key (const void *key, size_tlen, const char *username, const char *target, intupper_case_target, unsigned charntlmv2[16])</h3>
<p> Generates an NTLMv2 session key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the ntlm key<br />
 <i>len</i> length of key<br />
 <i>username</i> name of the user, as sent in the message, assumed to be in UTF8.<br />
 <i>target</i> the name of the target, assumed to be in UTF8.<br />
 <i>upper_case_target</i> upper case the target, should not be used only for legacy systems<br />
 <i>ntlmv2</i> the ntlmv2 session key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, or an error code on failure.</dl>
<h3>int heim_ntlm_verify_ntlm2 (const void *key, size_tlen, const char *username, const char *target, time_tnow, const unsigned charserverchallenge[8], const struct <code>ntlm_buf</code> *answer, struct <code>ntlm_buf</code> *infotarget, unsigned charntlmv2[16])</h3>
<p> Verify NTLMv2 response. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the ntlm key<br />
 <i>len</i> length of key<br />
 <i>username</i> name of the user, as sent in the message, assumed to be in UTF8.<br />
 <i>target</i> the name of the target, assumed to be in UTF8.<br />
 <i>now</i> the time now (0 if the library should pick it up itself)<br />
 <i>serverchallenge</i> challenge as sent by the server in the type2 message.<br />
 <i>answer</i> ntlm response answer, should be freed with <code>heim_ntlm_free_buf()</code>.<br />
 <i>infotarget</i> infotarget as sent by the server in the type2 message.<br />
 <i>ntlmv2</i> calculated session key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of success 0 is return, an errors, a errno in what went wrong.</dl>
<p> First check with the domain as the client passed it to the function. </p>
<p> Second check with domain uppercased. </p>
<p> Third check with empty domain. </p>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalntlmlibrary from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAY">Author</a></p>
<dd></dl>
