---
title: "zarmour(3)"
name: "zarmour"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zarmour/"
description: "zarmour – armoured text encoding and decoding"
---

<p>zarmour &#8211; armoured text encoding and decoding</p>
<h2>Synopsis</h2>
<pre><code>//  Enumeration defining different encoding modes
typedef enum {
    ZARMOUR_MODE_BASE64_STD //  Standard base 64
    ,
    ZARMOUR_MODE_BASE64_URL //  URL and filename friendly base 64
    ,
    ZARMOUR_MODE_BASE32_STD //  Standard base 32
    ,
    ZARMOUR_MODE_BASE32_HEX //  Extended hex base 32
    ,
    ZARMOUR_MODE_BASE16 //  Standard base 16
#if (ZMQ_VERSION &gt;= ZMQ_MAKE_VERSION(3, 3, 0))
    ,
    ZARMOUR_MODE_Z85 //  Z85 from ZeroMQ RFC 32
#endif
} zarmour_mode_t;

//  Create a new zarmour
CZMQ_EXPORT zarmour_t *
zarmour_new();

//  Destroy the zarmour
CZMQ_EXPORT void
zarmour_destroy(zarmour_t **self_p);

//  Print properties of object
CZMQ_EXPORT void
zarmour_print(zarmour_t *self);

//  Get printable string for mode
CZMQ_EXPORT const char *
zarmour_mode_str(zarmour_t *self);

//  Encode a stream of bytes into an armoured string.
CZMQ_EXPORT char *
zarmour_encode(zarmour_t *self, const byte *data, size_t data_size);

//  Decode an armoured string into a string of bytes.
//  The decoded output is null-terminated, so it may be treated
//  as a string, if that's what it was prior to encoding.
CZMQ_EXPORT byte *
zarmour_decode(zarmour_t *self, const char *data, size_t *decode_size);

//  Get/set the mode property
CZMQ_EXPORT zarmour_mode_t
zarmour_mode(zarmour_t *self);
CZMQ_EXPORT void
zarmour_set_mode(zarmour_t *self, zarmour_mode_t mode);

//  Get/set the pad property
CZMQ_EXPORT bool
zarmour_pad(zarmour_t *self);
CZMQ_EXPORT void
zarmour_set_pad(zarmour_t *self, bool pad);

//  Get/set the pad_char property
CZMQ_EXPORT char
zarmour_pad_char(zarmour_t *self);
CZMQ_EXPORT void
zarmour_set_pad_char(zarmour_t *self, char pad_char);

//  Get/set the line_breaks property
CZMQ_EXPORT bool
zarmour_line_breaks(zarmour_t *self);
CZMQ_EXPORT void
zarmour_set_line_breaks(zarmour_t *self, bool line_breaks);

//  Get/set the line_length property
CZMQ_EXPORT size_t
zarmour_line_length(zarmour_t *self);
CZMQ_EXPORT void
zarmour_set_line_length(zarmour_t *self, size_t line_length);

//  Self test of this class
CZMQ_EXPORT int
zarmour_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>zarmour &#8211; armoured text encoding and decoding </p>
<p> The zarmour class implements encoding and decoding of armoured text data. The following codecs are implemented: * RFC 4648 (m[blue]<code><a rel="nofollow" href="http://www.ietf.org/rfc/rfc4648.txt">http://www.ietf.org/rfc/rfc4648.txt</a></code>m[]) &#8211; base64 &#8211; base64url &#8211; base32 &#8211; base32hex &#8211; base16 * Z85 (m[blue]<code><a href="http://rfc.zeromq.org/spec:32">http://rfc.zeromq.org/spec:32</a></code>m[]) All RFC4648 base64 and base32 variants support padding the output. The pad character is configurable. Default is padding on, with character <i>=</i>. Additionally, in some cases (e.g. MIME), splitting the output into lines of a specific length is required. This feature is also supported, though turned off by default. The z85 mode does neither padding nor line breaks; it is merely a wrapping of the corresponding libzmq methods. Encoding will assert if input length is not divisible by 4 and decoding will assert if input length is not divisible by 5.</p>
<h2>Example</h2>
<p><code>From zarmour_test method</code>. </p>
<pre><code>zarmour_t *self = zarmour_new();
assert(self);

zarmour_mode_t mode = zarmour_mode(self);
assert(mode == ZARMOUR_MODE_BASE64_STD);

zarmour_set_mode(self, ZARMOUR_MODE_BASE64_URL);
mode = zarmour_mode(self);
assert(mode == ZARMOUR_MODE_BASE64_URL);

assert(zarmour_pad(self));
zarmour_set_pad(self, false);
assert(!zarmour_pad(self));

assert(zarmour_pad_char(self) == '=');
zarmour_set_pad_char(self, '!');
assert(zarmour_pad_char(self) == '!');
zarmour_set_pad_char(self, '=');
assert(zarmour_pad_char(self) == '=');

assert(!zarmour_line_breaks(self));
zarmour_set_line_breaks(self, true);
assert(zarmour_line_breaks(self));

assert(zarmour_line_length(self) == 72);
zarmour_set_line_length(self, 64);
assert(zarmour_line_length(self) == 64);

//  Test against test vectors from RFC4648.
zarmour_set_mode(self, ZARMOUR_MODE_BASE64_STD);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;Zg&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;Zm8&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;Zm9v&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;Zm9vYg&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;Zm9vYmE&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;Zm9vYmFy&quot;, verbose);
zarmour_set_pad(self, true);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;Zg==&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;Zm8=&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;Zm9v&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;Zm9vYg==&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;Zm9vYmE=&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;Zm9vYmFy&quot;, verbose);

zarmour_set_pad(self, false);
zarmour_set_mode(self, ZARMOUR_MODE_BASE64_URL);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;Zg&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;Zm8&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;Zm9v&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;Zm9vYg&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;Zm9vYmE&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;Zm9vYmFy&quot;, verbose);
zarmour_set_pad(self, true);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;Zg==&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;Zm8=&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;Zm9v&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;Zm9vYg==&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;Zm9vYmE=&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;Zm9vYmFy&quot;, verbose);

zarmour_set_pad(self, false);
zarmour_set_mode(self, ZARMOUR_MODE_BASE32_STD);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;MY&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;MZXQ&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;MZXW6&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;MZXW6YQ&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;MZXW6YTB&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;MZXW6YTBOI&quot;, verbose);
s_armour_decode(self, &quot;my&quot;, &quot;f&quot;, verbose);
s_armour_decode(self, &quot;mzxq&quot;, &quot;fo&quot;, verbose);
s_armour_decode(self, &quot;mzxw6&quot;, &quot;foo&quot;, verbose);
s_armour_decode(self, &quot;mzxw6yq&quot;, &quot;foob&quot;, verbose);
s_armour_decode(self, &quot;mzxw6ytb&quot;, &quot;fooba&quot;, verbose);
s_armour_decode(self, &quot;mzxw6ytboi&quot;, &quot;foobar&quot;, verbose);
zarmour_set_pad(self, true);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;MY======&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;MZXQ====&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;MZXW6===&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;MZXW6YQ=&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;MZXW6YTB&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;MZXW6YTBOI======&quot;, verbose);
s_armour_decode(self, &quot;my======&quot;, &quot;f&quot;, verbose);
s_armour_decode(self, &quot;mzxq====&quot;, &quot;fo&quot;, verbose);
s_armour_decode(self, &quot;mzxw6===&quot;, &quot;foo&quot;, verbose);
s_armour_decode(self, &quot;mzxw6yq=&quot;, &quot;foob&quot;, verbose);
s_armour_decode(self, &quot;mzxw6ytb&quot;, &quot;fooba&quot;, verbose);
s_armour_decode(self, &quot;mzxw6ytboi======&quot;, &quot;foobar&quot;, verbose);

zarmour_set_pad(self, false);
zarmour_set_mode(self, ZARMOUR_MODE_BASE32_HEX);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;CO&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;CPNG&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;CPNMU&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;CPNMUOG&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;CPNMUOJ1&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;CPNMUOJ1E8&quot;, verbose);
s_armour_decode(self, &quot;co&quot;, &quot;f&quot;, verbose);
s_armour_decode(self, &quot;cpng&quot;, &quot;fo&quot;, verbose);
s_armour_decode(self, &quot;cpnmu&quot;, &quot;foo&quot;, verbose);
s_armour_decode(self, &quot;cpnmuog&quot;, &quot;foob&quot;, verbose);
s_armour_decode(self, &quot;cpnmuoj1&quot;, &quot;fooba&quot;, verbose);
s_armour_decode(self, &quot;cpnmuoj1e8&quot;, &quot;foobar&quot;, verbose);
zarmour_set_pad(self, true);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;CO======&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;CPNG====&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;CPNMU===&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;CPNMUOG=&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;CPNMUOJ1&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;CPNMUOJ1E8======&quot;, verbose);
s_armour_decode(self, &quot;co======&quot;, &quot;f&quot;, verbose);
s_armour_decode(self, &quot;cpng====&quot;, &quot;fo&quot;, verbose);
s_armour_decode(self, &quot;cpnmu===&quot;, &quot;foo&quot;, verbose);
s_armour_decode(self, &quot;cpnmuog=&quot;, &quot;foob&quot;, verbose);
s_armour_decode(self, &quot;cpnmuoj1&quot;, &quot;fooba&quot;, verbose);
s_armour_decode(self, &quot;cpnmuoj1e8======&quot;, &quot;foobar&quot;, verbose);
zarmour_set_pad(self, true);

zarmour_set_mode(self, ZARMOUR_MODE_BASE16);
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;f&quot;, &quot;66&quot;, verbose);
s_armour_test(self, &quot;fo&quot;, &quot;666F&quot;, verbose);
s_armour_test(self, &quot;foo&quot;, &quot;666F6F&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;666F6F62&quot;, verbose);
s_armour_test(self, &quot;fooba&quot;, &quot;666F6F6261&quot;, verbose);
s_armour_test(self, &quot;foobar&quot;, &quot;666F6F626172&quot;, verbose);
s_armour_decode(self, &quot;666f&quot;, &quot;fo&quot;, verbose);
s_armour_decode(self, &quot;666f6f&quot;, &quot;foo&quot;, verbose);
s_armour_decode(self, &quot;666f6f62&quot;, &quot;foob&quot;, verbose);
s_armour_decode(self, &quot;666f6f6261&quot;, &quot;fooba&quot;, verbose);
s_armour_decode(self, &quot;666f6f626172&quot;, &quot;foobar&quot;, verbose);

#ifdef _INCLUDE_Z85
//  Z85 test is homemade; using 0, 4 and 8 bytes, with precalculated
//  test vectors created with a libzmq test.
//  ----------------------------------------------------------------

//  Make a fake curve key from hex (base16) string, making sure
//  there are no null bytes inside, so we can use our test utility
zarmour_set_mode(self, ZARMOUR_MODE_BASE16);
zarmour_set_line_breaks(self, false);
size_t key_len;
byte *key_data = zarmour_decode(self,
                                &quot;4E6F87E2FB6EB22A1EF5E257B75D79124949565F0B8B36A878A4F03111C96E0B&quot;,
                                &amp;key_len);

zarmour_set_mode(self, ZARMOUR_MODE_Z85); //  Z85 mode does not support padding or line breaks
zarmour_set_pad(self, false);             //  so these two are superfluous;
zarmour_set_line_breaks(self, false);     //  just for consistency
if (verbose)
    zarmour_print(self);
s_armour_test(self, &quot;&quot;, &quot;&quot;, verbose);
s_armour_test(self, &quot;foob&quot;, &quot;w]zP%&quot;, verbose);
s_armour_test(self, &quot;foobar!!&quot;, &quot;w]zP%vr9Im&quot;, verbose);
s_armour_test(self, (char *)key_data, &quot;ph+{E}!&amp;X?9}!I]W{sm(nL8@&amp;3Yu{wC+&lt;*-5Y[[#&quot;, verbose);
free(key_data);
#endif

//  Armouring longer byte array to test line breaks
zarmour_set_pad(self, true);
zarmour_set_line_breaks(self, true);
byte test_data[256];
int i;
for (i = 0; i &lt; 256; ++i) {
    test_data[i] = i;
}
zarmour_set_mode(self, ZARMOUR_MODE_BASE64_STD);
s_armour_test_long(self, test_data, 256, verbose);
zarmour_set_mode(self, ZARMOUR_MODE_BASE64_URL);
s_armour_test_long(self, test_data, 256, verbose);
zarmour_set_mode(self, ZARMOUR_MODE_BASE32_STD);
s_armour_test_long(self, test_data, 256, verbose);
zarmour_set_mode(self, ZARMOUR_MODE_BASE32_HEX);
s_armour_test_long(self, test_data, 256, verbose);
zarmour_set_mode(self, ZARMOUR_MODE_BASE16);
s_armour_test_long(self, test_data, 256, verbose);
#ifdef _INCLUDE_Z85
zarmour_set_mode(self, ZARMOUR_MODE_Z85);
s_armour_test_long(self, test_data, 256, verbose);
#endif

zarmour_destroy(&amp;self);
</code></pre>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>
