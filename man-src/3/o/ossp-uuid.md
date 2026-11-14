---
title: "ossp-uuid(3)"
name: "ossp-uuid"
section: "3"
letter: "o"
url: "/docs/linux/man/3-ossp-uuid/"
description: "uuid – OSSP Universally Unique Identifier"
---

<p><code>uuid</code> &#8211; <code>OSSP Universally Unique Identifier</code></p>
<h2>Version</h2>
<p><font SIZE="-1">OSSP</font> uuid <font SIZE="-1">1.6.2 (04-Jul-2008)</font></p>
<h2>Description</h2>
<p><font SIZE="-1"><code>OSSP</code></font><code> uuid</code> is a <font SIZE="-1">ISO-C:1999</font> application programming interface (<font SIZE="-1">API</font>) and corresponding command line interface (<font SIZE="-1">CLI</font>) for the generation of <font SIZE="-1">DCE</font> 1.1, <font SIZE="-1">ISO/IEC</font> 11578:1996 and <font SIZE="-1">IETF</font> <font SIZE="-1">RFC-4122</font> compliant <i>Universally Unique Identifier</i> (<font SIZE="-1">UUID</font>). It supports <font SIZE="-1">DCE</font> 1.1 variant UUIDs of version 1 (time and node based), version 3 (name based, <font SIZE="-1">MD5</font>), version 4 (random number based) and version 5 (name based, <font SIZE="-1">SHA-1</font>). Additional <font SIZE="-1">API</font> bindings are provided for the languages <font SIZE="-1">ISO-C<font SIZE="-2">++</font>:1998</font>, Perl:5 and <font SIZE="-1">PHP:4/5</font>. Optional backward compatibility exists for the ISO-C <font SIZE="-1">DCE-1</font>.1 and Perl Data::UUID APIs. UUIDs are 128 bit numbers which are intended to have a high likelihood of uniqueness over space and time and are computationally difficult to guess. They are globally unique identifiers which can be locally generated without contacting a global registration authority. UUIDs are intended as unique identifiers for both mass tagging objects with an extremely short lifetime and to reliably identifying very persistent objects across a network. This is the ISO-C application programming interface (<font SIZE="-1">API</font>) of <font SIZE="-1"><code>OSSP</code></font><code> uuid</code>.<br />
 <code><font SIZE="-1">UUID</font> Binary Representation</code> According to the <font SIZE="-1">DCE</font> 1.1, <font SIZE="-1">ISO/IEC</font> 11578:1996 and <font SIZE="-1">IETF</font> <font SIZE="-1">RFC-4122</font> standards, a <font SIZE="-1">DCE</font> 1.1 variant <font SIZE="-1">UUID</font> is a 128 bit number defined out of 7 fields, each field a multiple of an octet in size and stored in network byte order: </p>
<pre> [4]
 version
 --&gt;| |&lt;--
 | |
 | | [16]
 [32] [16] | |time_hi
 time_low time_mid | _and_version
 |&lt;----------------------------&gt;||&lt;------------&gt;||&lt;------------&gt;|
 | MSB || || | |
 | / || || | |
 |/ || || | |
 +------++------++------++------++------++------++------++------+~~
 | 15 || 14 || 13 || 12 || 11 || 10 |####9 || 8 |
 | MSO || || || || || |#### || |
 +------++------++------++------++------++------++------++------+~~
 7654321076543210765432107654321076543210765432107654321076543210
 ~~+------++------++------++------++------++------++------++------+
 ##* 7 || 6 || 5 || 4 || 3 || 2 || 1 || 0 |
 ##* || || || || || || || LSO |
 ~~+------++------++------++------++------++------++------++------+
 7654321076543210765432107654321076543210765432107654321076543210
 | | || || /|
 | | || || / |
 | | || || LSB |
 |&lt;----&gt;||&lt;----&gt;||&lt;--------------------------------------------&gt;|
 |clk_seq clk_seq node
 |_hi_res _low [48]
 |[5-6] [8]
 | |
 --&gt;| |&lt;--
 variant
 [2-3]</pre>
<p>An example of a <font SIZE="-1">UUID</font> binary representation is the octet stream <tt> 0xF8 0x1D 0x4F 0xAE 0x7D 0xEC 0x11 0xD0 0xA7 0x65 0x00 0xA0 0xC9 0x1E 0x6B 0xF6<br />
 </tt>. The binary representation format is exactly what the <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> <font SIZE="-1">API</font> functions <code>uuid_import</code>() and <code>uuid_export</code>() deal with under <tt> UUID_FMT_BIN<br />
 </tt>.<br />
 <code><font SIZE="-1">UUID</font> <font SIZE="-1">ASCII</font> String Representation</code> According to the <font SIZE="-1">DCE</font> 1.1, <font SIZE="-1">ISO/IEC</font> 11578:1996 and <font SIZE="-1">IETF</font> <font SIZE="-1">RFC-4122</font> standards, a <font SIZE="-1">DCE</font> 1.1 variant <font SIZE="-1">UUID</font> is represented as an <font SIZE="-1">ASCII</font> string consisting of 8 hexadecimal digits followed by a hyphen, then three groups of 4 hexadecimal digits each followed by a hyphen, then 12 hexadecimal digits. Formally, the string representation is defined by the following grammar: </p>
<pre><code>uuid                        = &lt;time_low&gt; &quot;-&quot;
&lt;time_mid&gt; &quot;-&quot;
&lt;time_high_and_version&gt; &quot;-&quot;
&lt;clock_seq_high_and_reserved&gt;
&lt;clock_seq_low&gt; &quot;-&quot;
&lt;node&gt;
time_low                    = 4*&lt;hex_octet&gt;
time_mid                    = 2*&lt;hex_octet&gt;
time_high_and_version       = 2*&lt;hex_octet&gt;
clock_seq_high_and_reserved = &lt;hex_octet&gt;
clock_seq_low               = &lt;hex_octet&gt;
node                        = 6*&lt;hex_octet&gt;
hex_octet                   = &lt;hex_digit&gt; &lt;hex_digit&gt;
hex_digit                   = &quot;0&quot;|&quot;1&quot;|&quot;2&quot;|&quot;3&quot;|&quot;4&quot;|&quot;5&quot;|&quot;6&quot;|&quot;7&quot;|&quot;8&quot;|&quot;9&quot;
|&quot;a&quot;|&quot;b&quot;|&quot;c&quot;|&quot;d&quot;|&quot;e&quot;|&quot;f&quot;
|&quot;A&quot;|&quot;B&quot;|&quot;C&quot;|&quot;D&quot;|&quot;E&quot;|&quot;F&quot;</code></pre>
<p> An example of a <font SIZE="-1">UUID</font> string representation is the <font SIZE="-1">ASCII</font> string &quot;<tt> f81d4fae-7dec-11d0-a765-00a0c91e6bf6<br />
 </tt>&quot;. The string representation format is exactly what the <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> <font SIZE="-1">API</font> functions <code>uuid_import</code>() and <code>uuid_export</code>() deal with under <tt> UUID_FMT_STR<br />
 </tt>. Notice: a corresponding <font SIZE="-1">URL</font> can be generated out of a <font SIZE="-1">ASCII</font> string representation of an <font SIZE="-1">UUID</font> by prefixing with &quot;<tt> urn:uuid:<br />
 </tt>&#8220; as in &#8221;<tt> urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6<br />
 </tt>&quot;.<br />
 <code><font SIZE="-1">UUID</font> Single Integer Value Representation</code> According to the <font SIZE="-1">ISO/IEC</font> 11578:1996 and ITU-T Rec. X.667 standards, a <font SIZE="-1">DCE</font> 1.1 variant <font SIZE="-1">UUID</font> can be also represented as a single integer value consisting of a decimal number with up to 39 digits. An example of a <font SIZE="-1">UUID</font> single integer value representation is the decimal number &quot;<tt>329800735698586629295641978511506172918</tt>&quot;. The string representation format is exactly what the <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> <font SIZE="-1">API</font> functions <code>uuid_import</code>() and <code>uuid_export</code>() deal with under <tt> UUID_FMT_SIV<br />
 </tt>. Notice: a corresponding <font SIZE="-1">ISO</font> <font SIZE="-1">OID</font> can be generated under the &#8220;{<i><a href="/docs/linux/man/2-joint-iso-itu-t/">joint-iso-itu-t</a></i>(2) uuid(25)}&#8221; arc out of a single integer value representation of a <font SIZE="-1">UUID</font> by prefixing with &quot;<tt>2.25.</tt>&#8220;. An example <font SIZE="-1">OID</font> is &#8221;<tt>2.25.329800735698586629295641978511506172918</tt>&#8220;. Additionally, an <font SIZE="-1">URL</font> can be generated by further prefixing with &#8221;<tt> urn:oid:<br />
 </tt>&#8220; as in &#8221;<tt> urn:oid:2.25.329800735698586629295641978511506172918<br />
 </tt>&quot;.<br />
 <code><font SIZE="-1">UUID</font> Variants and Versions</code> A <font SIZE="-1">UUID</font> has a variant and version. The variant defines the layout of the <font SIZE="-1">UUID</font>. The version defines the content of the <font SIZE="-1">UUID</font>. The <font SIZE="-1">UUID</font> variant supported in <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> is the <font SIZE="-1">DCE</font> 1.1 variant only. The <font SIZE="-1">DCE</font> 1.1 <font SIZE="-1">UUID</font> variant versions supported in <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> are:</p>
<dl>
<dt><code>Version 1</code> (time and node based)</p>
<dd>These are the classical UUIDs, created out of a 60-bit system time, a 14-bit local clock sequence and 48-bit system <font SIZE="-1">MAC</font> address. The <font SIZE="-1">MAC</font> address can be either the real one of a physical network interface card (<font SIZE="-1">NIC</font>) or a random multi-cast <font SIZE="-1">MAC</font> address. Version 1 UUIDs are usually used as one-time global unique identifiers.</p>
<dt><code>Version 3</code> (name based, <font SIZE="-1">MD5</font>)</p>
<dd>These are UUIDs which are based on the 128-bit <font SIZE="-1">MD5</font> message digest of the concatenation of a 128-bit namespace <font SIZE="-1">UUID</font> and a name string of arbitrary length. Version 3 UUIDs are usually used for non-unique but repeatable message digest identifiers.</p>
<dt><code>Version 4</code> (random data based)</p>
<dd>These are UUIDs which are based on just 128-bit of random data. Version 4 UUIDs are usually used as one-time local unique identifiers.</p>
<dt><code>Version 5</code> (name based, <font SIZE="-1">SHA-1</font>)</p>
<dd>These are UUIDs which are based on the 160-bit <font SIZE="-1">SHA-1</font> message digest of the concatenation of a 128-bit namespace <font SIZE="-1">UUID</font> and a name string of arbitrary length. Version 5 UUIDs are usually used for non-unique but repeatable message digest identifiers.
</dl>
<p> <code><font SIZE="-1">UUID</font> Uniqueness</code> Version 1 UUIDs are guaranteed to be unique through combinations of hardware addresses, time stamps and random seeds. There is a reference in the <font SIZE="-1">UUID</font> to the hardware (<font SIZE="-1">MAC</font>) address of the first network interface card (<font SIZE="-1">NIC</font>) on the host which generated the <font SIZE="-1">UUID</font> &#8212; this reference is intended to ensure the <font SIZE="-1">UUID</font> will be unique in space as the <font SIZE="-1">MAC</font> address of every network card is assigned by a single global authority (<font SIZE="-1">IEEE</font>) and is guaranteed to be unique. The next component in a <font SIZE="-1">UUID</font> is a timestamp which, as clock always (should) move forward, will be unique in time. Just in case some part of the above goes wrong (the hardware address cannot be determined or the clock moved steps backward), there is a random clock sequence component placed into the <font SIZE="-1">UUID</font> as a &#8220;catch-all&#8221; for uniqueness. Version 3 and version 5 UUIDs are guaranteed to be inherently globally unique if the combination of namespace and name used to generate them is unique. Version 4 UUIDs are not guaranteed to be globally unique, because they are generated out of locally gathered pseudo-random numbers only. Nevertheless there is still a high likelihood of uniqueness over space and time and that they are computationally difficult to guess.<br />
 <code>Nil <font SIZE="-1">UUID</font></code> There is a special <i>Nil</i> <font SIZE="-1">UUID</font> consisting of all octets set to zero in the binary representation. It can be used as a special <font SIZE="-1">UUID</font> value which does not conflict with real UUIDs.</p>
<h2>Application Programming Interface</h2>
<p>The ISO-C Application Programming Interface (<font SIZE="-1">API</font>) of <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> consists of the following components. </p>
<p> <code><font SIZE="-1">CONSTANTS</font></code> </p>
<p> The following constants are provided:</p>
<dl>
<dt><font SIZE="-1"><code>UUID_VERSION</code></font></p>
<dd>The hexadecimal encoded <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> version. This allows compile-time checking of the <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> version. For run-time checking use <code>uuid_version</code>() instead. </p>
<p> The hexadecimal encoding for a version &quot;$<i>v</i>.$<i>r</i>$<i>t</i>$<i>l</i>&quot; is calculated with the <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>version</code> command and is (in Perl-style for concise description) &quot;sprintf(&#8216;0x%x%02x%d%02x&#8217;, $<i>v</i>, $<i>r</i>, {qw(s 9 . 2 b 1 a 0)}-&gt;{$<i>t</i>}, ($<i>t</i> eq &#8216;s&#8217; ? 99 : $<i>l</i>))&#8220;, i.e., the version 0.9.6 is encoded as &#8221;0x009206&quot;.</p>
<dt><font SIZE="-1"><code>UUID_LEN_BIN</code></font>, <font SIZE="-1"><code>UUID_LEN_STR</code></font>, <font SIZE="-1"><code>UUID_LEN_SIV</code></font></p>
<dd>The number of octets of the <font SIZE="-1">UUID</font> binary and string representations. Notice that the lengths of the string representation (<font SIZE="-1"><code>UUID_LEN_STR</code></font>) and the lengths of the single integer value representation (<font SIZE="-1"><code>UUID_LEN_SIV</code></font>) does <i>not</i> include the necessary <tt> NUL<br />
 </tt> termination character.</p>
<dt><font SIZE="-1"><code>UUID_MAKE_V1</code></font>, <font SIZE="-1"><code>UUID_MAKE_V3</code></font>, <font SIZE="-1"><code>UUID_MAKE_V4</code></font>, <font SIZE="-1"><code>UUID_MAKE_V5</code></font>, <font SIZE="-1"><code>UUID_MAKE_MC</code></font></p>
<dd>The <i>mode</i> bits for use with <code>uuid_make</code>(). The <font SIZE="-1"><code>UUID_MAKE_V</code></font><i>N</i> specify which <font SIZE="-1">UUID</font> version to generate. The <font SIZE="-1"><code>UUID_MAKE_MC</code></font> forces the use of a random multi-cast <font SIZE="-1">MAC</font> address instead of the real physical <font SIZE="-1">MAC</font> address in version 1 UUIDs.</p>
<dt><font SIZE="-1"><code>UUID_RC_OK</code></font>, <font SIZE="-1"><code>UUID_RC_ARG</code></font>, <font SIZE="-1"><code>UUID_RC_MEM</code></font>, <font SIZE="-1"><code>UUID_RC_SYS</code></font>, <font SIZE="-1"><code>UUID_RC_INT</code></font>, <font SIZE="-1"><code>UUID_RC_IMP</code></font></p>
<dd>The possible numerical return-codes of <font SIZE="-1">API</font> functions. The <tt> UUID_RC_OK<br />
 </tt> indicates success, the others indicate errors. Use <code>uuid_error</code>() to translate them into string versions.</p>
<dt><font SIZE="-1"><code>UUID_FMT_BIN</code></font>, <font SIZE="-1"><code>UUID_FMT_STR</code></font>, <font SIZE="-1"><code>UUID_FMT_SIV</code></font>, <font SIZE="-1"><code>UUID_FMT_TXT</code></font></p>
<dd>The <i>fmt</i> formats for use with <code>uuid_import</code>() and <code>uuid_export</code>(). The <font SIZE="-1"><code>UUID_FMT_BIN</code></font> indicates the <font SIZE="-1">UUID</font> binary representation (of length <font SIZE="-1"><code>UUID_LEN_BIN</code></font>), the <font SIZE="-1"><code>UUID_FMT_STR</code></font> indicates the <font SIZE="-1">UUID</font> string representation (of length <font SIZE="-1"><code>UUID_LEN_STR</code></font>), the <font SIZE="-1"><code>UUID_FMT_SIV</code></font> indicates the <font SIZE="-1">UUID</font> single integer value representation (of maximum length <font SIZE="-1"><code>UUID_LEN_SIV</code></font>) and the <font SIZE="-1"><code>UUID_FMT_TXT</code></font> indicates the textual description (of arbitrary length) of a <font SIZE="-1">UUID</font>.
</dl>
<p> <code><font SIZE="-1">FUNCTIONS</font></code> </p>
<p> The following functions are provided:</p>
<dl>
<dt>uuid_rc_t <code>uuid_create</code>(uuid_t **<i>uuid</i>);</p>
<dd>Create a new <font SIZE="-1">UUID</font> object and store a pointer to it in <tt> *<br />
 </tt><i>uuid</i>. A <font SIZE="-1">UUID</font> object consists of an internal representation of a <font SIZE="-1">UUID</font>, the internal <font SIZE="-1">PRNG</font> and <font SIZE="-1">MD5</font> generator contexts, and cached <font SIZE="-1">MAC</font> address and timestamp information. The initial <font SIZE="-1">UUID</font> is the <i>Nil</i> <font SIZE="-1">UUID</font>.</p>
<dt>uuid_rc_t <code>uuid_destroy</code>(uuid_t *<i>uuid</i>);</p>
<dd>Destroy <font SIZE="-1">UUID</font> object <i>uuid</i>.</p>
<dt>uuid_rc_t <code>uuid_clone</code>(const uuid_t *<i>uuid</i>, uuid_t **<i>uuid_clone</i>);</p>
<dd>Clone <font SIZE="-1">UUID</font> object <i>uuid</i> and store new <font SIZE="-1">UUID</font> object in <i>uuid_clone</i>.</p>
<dt>uuid_rc_t <code>uuid_isnil</code>(const uuid_t *<i>uuid</i>, int *<i>result</i>);</p>
<dd>Checks whether the <font SIZE="-1">UUID</font> in <i>uuid</i> is the <i>Nil</i> <font SIZE="-1">UUID</font>. If this is the case, it returns <i>true</i> in <tt> *<br />
 </tt><i>result</i>. Else it returns <i>false</i> in <tt> *<br />
 </tt><i>result</i>.</p>
<dt>uuid_rc_t <code>uuid_compare</code>(const uuid_t *<i>uuid</i>, const uuid_t *<i>uuid2</i>, int *<i>result</i>);</p>
<dd>Compares the order of the two UUIDs in <i>uuid1</i> and <i>uuid2</i> and returns the result in <tt> *<br />
 </tt><i>result</i>: <tt> -1<br />
 </tt> if <i>uuid1</i> is smaller than <i>uuid2</i>, <tt>0</tt> if <i>uuid1</i> is equal to <i>uuid2</i> and <tt>+1</tt> if <i>uuid1</i> is greater than <i>uuid2</i>.</p>
<dt>uuid_rc_t <code>uuid_import</code>(uuid_t *<i>uuid</i>, uuid_fmt_t <i>fmt</i>, const void *<i>data_ptr</i>, size_t <i>data_len</i>);</p>
<dd>Imports a <font SIZE="-1">UUID</font> <i>uuid</i> from an external representation of format <i>fmt</i>. The data is read from the buffer at <i>data_ptr</i> which contains at least <i>data_len</i> bytes. </p>
<p> The format of the external representation is specified by <i>fmt</i> and the minimum expected length in <i>data_len</i> depends on it. Valid values for <i>fmt</i> are <font SIZE="-1"><code>UUID_FMT_BIN</code></font>, <font SIZE="-1"><code>UUID_FMT_STR</code></font> and <font SIZE="-1"><code>UUID_FMT_SIV</code></font>.</p>
<dt>uuid_rc_t <code>uuid_export</code>(const uuid_t *<i>uuid</i>, uuid_fmt_t <i>fmt</i>, void *<i>data_ptr</i>, size_t *<i>data_len</i>);</p>
<dd>Exports a <font SIZE="-1">UUID</font> <i>uuid</i> into an external representation of format <i>fmt</i>. Valid values for <i>fmt</i> are <font SIZE="-1"><code>UUID_FMT_BIN</code></font>, <font SIZE="-1"><code>UUID_FMT_STR</code></font>, <font SIZE="-1"><code>UUID_FMT_SIV</code></font> and <font SIZE="-1"><code>UUID_FMT_TXT</code></font>. </p>
<p> The data is written to the buffer whose location is obtained by dereferencing <i>data_ptr</i> after a &#8220;cast&#8221; to the appropriate pointer-to-pointer type. Hence the generic pointer argument <i>data_ptr</i> is expected to be a pointer to a &#8220;pointer of a particular type&#8221;, i.e., it has to be of type &quot;<tt> unsigned char **<br />
 </tt>&quot; for <font SIZE="-1"><code>UUID_FMT_BIN</code></font> and &quot;<tt> char **<br />
 </tt>&quot; for <font SIZE="-1"><code>UUID_FMT_STR</code></font>, <font SIZE="-1"><code>UUID_FMT_SIV</code></font> and <font SIZE="-1"><code>UUID_FMT_TXT</code></font>. </p>
<p> The buffer has to be room for at least <tt> *<br />
 </tt><i>data_len</i> bytes. If the value of the pointer after &#8220;casting&#8221; and dereferencing <i>data_ptr</i> is <tt> NULL<br />
 </tt>, <i>data_len</i> is ignored as input and a new buffer is allocated and returned in the pointer after &#8220;casting&#8221; and dereferencing <i>data_ptr</i> (the caller has to <i><a href="/docs/linux/man/3-free/">free</a></i>(3) it later on). </p>
<p> If <i>data_len</i> is not <tt> NULL<br />
 </tt>, the number of available bytes in the buffer has to be provided in <tt> *<br />
 </tt><i>data_len</i> and the number of actually written bytes are returned in <tt> *<br />
 </tt><i>data_len</i> again. The minimum required buffer length depends on the external representation as specified by <i>fmt</i> and is at least <font SIZE="-1"><code>UUID_LEN_BIN</code></font> for <font SIZE="-1"><code>UUID_FMT_BIN</code></font>, <font SIZE="-1"><code>UUID_LEN_STR</code></font> for <font SIZE="-1"><code>UUID_FMT_STR</code></font> and <font SIZE="-1"><code>UUID_LEN_SIV</code></font> for <font SIZE="-1"><code>UUID_FMT_SIV</code></font>. For <font SIZE="-1"><code>UUID_FMT_TXT</code></font> a buffer of unspecified length is required and hence it is recommended to allow <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> to allocate the buffer as necessary.</p>
<dt>uuid_rc_t <code>uuid_load</code>(uuid_t *<i>uuid</i>, const char *<i>name</i>);</p>
<dd>Loads a pre-defined <font SIZE="-1">UUID</font> value into the <font SIZE="-1">UUID</font> object <i>uuid</i>. The following <i>name</i> arguments are currently known:</p>
<dl>
<dd>
<dl>
<dt><i>name</i> <i></i><font SIZE="-1"><i>UUID</i></font><i></i></p>
<dd>
<dt>nil 00000000-0000-0000-0000-000000000000</p>
<dd>
<dt>ns:DNS 6ba7b810-9dad-11d1-80b4-00c04fd430c8</p>
<dd>
<dt>ns:URL 6ba7b811-9dad-11d1-80b4-00c04fd430c8</p>
<dd>
<dt>ns:OID 6ba7b812-9dad-11d1-80b4-00c04fd430c8</p>
<dd>
<dt>ns:X500 6ba7b814-9dad-11d1-80b4-00c04fd430c8</p>
<dd></dl>
</dl>
<dl>
<dd>The &quot;<tt> ns:<br />
 </tt><i></i><font SIZE="-1"><i>XXX</i></font><i></i>&quot; are names of pre-defined name-space UUIDs for use in the generation of <font SIZE="-1">DCE</font> 1.1 version 3 and version 5 UUIDs.</dl>
<dt>uuid_rc_t <code>uuid_make</code>(uuid_t *<i>uuid</i>, unsigned int <i>mode</i>, &#8230;);</p>
<dd>Generates a new <font SIZE="-1">UUID</font> in <i>uuid</i> according to <i>mode</i> and optional arguments (dependent on <i>mode</i>). </p>
<p> If <i>mode</i> contains the <tt> UUID_MAKE_V1<br />
 </tt> bit, a <font SIZE="-1">DCE</font> 1.1 variant <font SIZE="-1">UUID</font> of version 1 is generated. Then optionally the bit <tt> UUID_MAKE_MC<br />
 </tt> forces the use of random multi-cast <font SIZE="-1">MAC</font> address instead of the real physical <font SIZE="-1">MAC</font> address (the default). The <font SIZE="-1">UUID</font> is generated out of the 60-bit current system time, a 12-bit clock sequence and the 48-bit <font SIZE="-1">MAC</font> address. </p>
<p> If <i>mode</i> contains the <tt> UUID_MAKE_V3<br />
 </tt> or <tt> UUID_MAKE_V5<br />
 </tt> bit, a <font SIZE="-1">DCE</font> 1.1 variant <font SIZE="-1">UUID</font> of version 3 or 5 is generated and two additional arguments are expected: first, a namespace <font SIZE="-1">UUID</font> object (<tt> uuid_t *<br />
 </tt>). Second, a name string of arbitrary length (<tt> const char *<br />
 </tt>). The <font SIZE="-1">UUID</font> is generated out of the 128-bit <font SIZE="-1">MD5</font> or 160-bit <font SIZE="-1">SHA-1</font> from the concatenated octet stream of namespace <font SIZE="-1">UUID</font> and name string. </p>
<p> If <i>mode</i> contains the <tt> UUID_MAKE_V4<br />
 </tt> bit, a <font SIZE="-1">DCE</font> 1.1 variant <font SIZE="-1">UUID</font> of version 4 is generated. The <font SIZE="-1">UUID</font> is generated out of 128-bit random data.</p>
<dt>char *<code>uuid_error</code>(uuid_rc_t <i>rc</i>);</p>
<dd>Returns a constant string representation corresponding to the return-code <i>rc</i> for use in displaying <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> errors.</p>
<dt>unsigned long <code>uuid_version</code>(void);</p>
<dd>Returns the hexadecimal encoded <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> version as compiled into the library object files. This allows run-time checking of the <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> version. For compile-time checking use <tt> UUID_VERSION<br />
 </tt> instead.</dl>
<h2>Example</h2>
<p>The following shows an example usage of the <font SIZE="-1">API</font>. Error handling is omitted for code simplification and has to be re-added for production code. </p>
<pre><code>/* generate a DCE 1.1 v1 UUID from system environment */
char *uuid_v1(void)
{
    uuid_t *uuid;
    char *str;

    uuid_create(&amp;uuid);
    uuid_make(uuid, UUID_MAKE_V1);
    str = NULL;
    uuid_export(uuid, UUID_FMT_STR, &amp;str, NULL);
    uuid_destroy(uuid);
    return str;
}

/* generate a DCE 1.1 v3 UUID from an URL */
char *uuid_v3(const char *url)
{
    uuid_t *uuid;
    uuid_t *uuid_ns;
    char *str;

    uuid_create(&amp;uuid);
    uuid_create(&amp;uuid_ns);
    uuid_load(uuid_ns, &quot;ns:URL&quot;);
    uuid_make(uuid, UUID_MAKE_V3, uuid_ns, url);
    str = NULL;
    uuid_export(uuid, UUID_FMT_STR, &amp;str, NULL);
    uuid_destroy(uuid_ns);
    uuid_destroy(uuid);
    return str;
}</code></pre>
<h2>See Also</h2>
<p>The following are references to <font SIZE="-1"><code>UUID</code></font> documentation and specifications:</p>
<dl>
<dt>&bull;</p>
<dd><code>A Universally Unique IDentifier (</code><font SIZE="-1"><code>UUID</code></font><code>) </code><font SIZE="-1"><code>URN</code></font><code> Namespace</code>, P. Leach, M. Mealling, R. Salz, <font SIZE="-1">IETF</font> <font SIZE="-1">RFC-4122</font>, July 2005, 32 pages, <a rel="nofollow" href="http://www.ietf.org/rfc/rfc4122.txt">http://www.ietf.org/rfc/rfc4122.txt</a></p>
<dt>&bull;</p>
<dd>Information Technology &#8212; Open Systems Interconnection (<font SIZE="-1">OSI</font>), <code>Procedures for the operation of </code><font SIZE="-1"><code>OSI</code></font><code> Registration Authorities: Generation and Registration of Universally Unique Identifiers (UUIDs) and their Use as </code><font SIZE="-1"><code>ASN</code></font><code>.1 Object Identifier Components</code>, <font SIZE="-1">ISO/IEC</font> 9834-8:2004 / ITU-T Rec. X.667, 2004, December 2004, 25 pages, <a rel="nofollow" href="http://www.itu.int/ITU-T/studygroups/com17/oid/X.667-E.pdf">http://www.itu.int/ITU-T/studygroups/com17/oid/X.667-E.pdf</a></p>
<dt>&bull;</p>
<dd><font SIZE="-1"><code>DCE</code></font><code> 1.1: Remote Procedure Call</code>, appendix <code>Universally Unique Identifier</code>, Open Group Technical Standard Document Number C706, August 1997, 737 pages, (supersedes C309 <font SIZE="-1">DCE:</font> Remote Procedure Call 8/1994, which was basis for <font SIZE="-1">ISO/IEC</font> 11578:1996 specification), <a rel="nofollow" href="http://www.opengroup.org/publications/catalog/c706.htm">http://www.opengroup.org/publications/catalog/c706.htm</a></p>
<dt>&bull;</p>
<dd>Information technology &#8212; Open Systems Interconnection (<font SIZE="-1">OSI</font>), <code>Remote Procedure Call (</code><font SIZE="-1"><code>RPC</code></font><code>)</code>, <font SIZE="-1">ISO/IEC</font> 11578:1996, August 2001, 570 pages, (<font SIZE="-1">CHF</font> 340,00), <a rel="nofollow" href="http://www.iso.ch/cate/d2229.html">http://www.iso.ch/cate/d2229.html</a></p>
<dt>&bull;</p>
<dd><font SIZE="-1"><code>HTTP</code></font><code> Extensions for Distributed Authoring (WebDAV)</code>, section <code>6.4.1 Node Field Generation Without the </code><font SIZE="-1"><code>IEEE</code></font><code> 802 Address</code>, <font SIZE="-1">IETF</font> <font SIZE="-1">RFC-2518</font>, February 1999, 94 pages, <a rel="nofollow" href="http://www.ietf.org/rfc/rfc2518.txt">http://www.ietf.org/rfc/rfc2518.txt</a></p>
<dt>&bull;</p>
<dd><font SIZE="-1"><code>DCE</code></font><code> 1.1 compliant </code><font SIZE="-1"><code>UUID</code></font><code> functions</code>, FreeBSD manual pages <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) and <i><a href="/docs/linux/man/2-uuidgen/">uuidgen</a></i>(2), <a rel="nofollow" href="http://www.freebsd.org/cgi/man.cgi?query=uuid">http://www.freebsd.org/cgi/man.cgi?query=uuid</a>&amp;manpath=FreeBSD+6.0-RELEASE</dl>
<h2>History</h2>
<p><font SIZE="-1"><code>OSSP</code></font><code> uuid</code> was implemented in January 2004 by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt;. It was prompted by the use of UUIDs in the <font SIZE="-1"><code>OSSP</code></font><code> as</code> and <code>OpenPKG</code> projects. It is a clean room implementation intended to be strictly standards compliant and maximum portable.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-uuid/">uuid</a></i>(1), <i><a href="/docs/linux/man/1-uuid-config/">uuid-config</a></i>(1), <i><a href="/docs/linux/man/3-ossp--uuid/">OSSP::uuid</a></i>(3). </p>
