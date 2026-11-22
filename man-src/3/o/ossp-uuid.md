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
<p>OSSP uuid 1.6.2 (04-Jul-2008)</p>
<h2>Description</h2>
<p><code>OSSP</code><code> uuid</code> is a ISO-C:1999 application programming interface (API) and corresponding command line interface (CLI) for the generation of DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 compliant <i>Universally Unique Identifier</i> (UUID). It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3 (name based, MD5), version 4 (random number based) and version 5 (name based, SHA-1). Additional API bindings are provided for the languages ISO-C++:1998, Perl:5 and PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1 and Perl Data::UUID APIs. UUIDs are 128 bit numbers which are intended to have a high likelihood of uniqueness over space and time and are computationally difficult to guess. They are globally unique identifiers which can be locally generated without contacting a global registration authority. UUIDs are intended as unique identifiers for both mass tagging objects with an extremely short lifetime and to reliably identifying very persistent objects across a network. This is the ISO-C application programming interface (API) of <code>OSSP</code><code> uuid</code>.<br/>
 <code>UUID Binary Representation</code> According to the DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 standards, a DCE 1.1 variant UUID is a 128 bit number defined out of 7 fields, each field a multiple of an octet in size and stored in network byte order: </p>
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
<p>An example of a UUID binary representation is the octet stream <tt> 0xF8 0x1D 0x4F 0xAE 0x7D 0xEC 0x11 0xD0 0xA7 0x65 0x00 0xA0 0xC9 0x1E 0x6B 0xF6<br/>
 </tt>. The binary representation format is exactly what the <code>OSSP</code><code> uuid</code> API functions <code>uuid_import</code>() and <code>uuid_export</code>() deal with under <tt> UUID_FMT_BIN<br/>
 </tt>.<br/>
 <code>UUID ASCII String Representation</code> According to the DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 standards, a DCE 1.1 variant UUID is represented as an ASCII string consisting of 8 hexadecimal digits followed by a hyphen, then three groups of 4 hexadecimal digits each followed by a hyphen, then 12 hexadecimal digits. Formally, the string representation is defined by the following grammar: </p>
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
<p> An example of a UUID string representation is the ASCII string &quot;<tt> f81d4fae-7dec-11d0-a765-00a0c91e6bf6<br/>
 </tt>&quot;. The string representation format is exactly what the <code>OSSP</code><code> uuid</code> API functions <code>uuid_import</code>() and <code>uuid_export</code>() deal with under <tt> UUID_FMT_STR<br/>
 </tt>. Notice: a corresponding URL can be generated out of a ASCII string representation of an UUID by prefixing with &quot;<tt> urn:uuid:<br/>
 </tt>&#8220; as in &#8221;<tt> urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6<br/>
 </tt>&quot;.<br/>
 <code>UUID Single Integer Value Representation</code> According to the ISO/IEC 11578:1996 and ITU-T Rec. X.667 standards, a DCE 1.1 variant UUID can be also represented as a single integer value consisting of a decimal number with up to 39 digits. An example of a UUID single integer value representation is the decimal number &quot;<tt>329800735698586629295641978511506172918</tt>&quot;. The string representation format is exactly what the <code>OSSP</code><code> uuid</code> API functions <code>uuid_import</code>() and <code>uuid_export</code>() deal with under <tt> UUID_FMT_SIV<br/>
 </tt>. Notice: a corresponding ISO OID can be generated under the &#8220;{<i>joint-iso-itu-t</i>(2) uuid(25)}&#8221; arc out of a single integer value representation of a UUID by prefixing with &quot;<tt>2.25.</tt>&#8220;. An example OID is &#8221;<tt>2.25.329800735698586629295641978511506172918</tt>&#8220;. Additionally, an URL can be generated by further prefixing with &#8221;<tt> urn:oid:<br/>
 </tt>&#8220; as in &#8221;<tt> urn:oid:2.25.329800735698586629295641978511506172918<br/>
 </tt>&quot;.<br/>
 <code>UUID Variants and Versions</code> A UUID has a variant and version. The variant defines the layout of the UUID. The version defines the content of the UUID. The UUID variant supported in <code>OSSP</code><code> uuid</code> is the DCE 1.1 variant only. The DCE 1.1 UUID variant versions supported in <code>OSSP</code><code> uuid</code> are:</p>
<dl>
<dt><code>Version 1</code> (time and node based)</dt>
<dd>These are the classical UUIDs, created out of a 60-bit system time, a 14-bit local clock sequence and 48-bit system MAC address. The MAC address can be either the real one of a physical network interface card (NIC) or a random multi-cast MAC address. Version 1 UUIDs are usually used as one-time global unique identifiers.</dd>
<dt><code>Version 3</code> (name based, MD5)</dt>
<dd>These are UUIDs which are based on the 128-bit MD5 message digest of the concatenation of a 128-bit namespace UUID and a name string of arbitrary length. Version 3 UUIDs are usually used for non-unique but repeatable message digest identifiers.</dd>
<dt><code>Version 4</code> (random data based)</dt>
<dd>These are UUIDs which are based on just 128-bit of random data. Version 4 UUIDs are usually used as one-time local unique identifiers.</dd>
<dt><code>Version 5</code> (name based, SHA-1)</dt>
<dd>These are UUIDs which are based on the 160-bit SHA-1 message digest of the concatenation of a 128-bit namespace UUID and a name string of arbitrary length. Version 5 UUIDs are usually used for non-unique but repeatable message digest identifiers.
</dd></dl>
<p> <code>UUID Uniqueness</code> Version 1 UUIDs are guaranteed to be unique through combinations of hardware addresses, time stamps and random seeds. There is a reference in the UUID to the hardware (MAC) address of the first network interface card (NIC) on the host which generated the UUID &#8212; this reference is intended to ensure the UUID will be unique in space as the MAC address of every network card is assigned by a single global authority (IEEE) and is guaranteed to be unique. The next component in a UUID is a timestamp which, as clock always (should) move forward, will be unique in time. Just in case some part of the above goes wrong (the hardware address cannot be determined or the clock moved steps backward), there is a random clock sequence component placed into the UUID as a &#8220;catch-all&#8221; for uniqueness. Version 3 and version 5 UUIDs are guaranteed to be inherently globally unique if the combination of namespace and name used to generate them is unique. Version 4 UUIDs are not guaranteed to be globally unique, because they are generated out of locally gathered pseudo-random numbers only. Nevertheless there is still a high likelihood of uniqueness over space and time and that they are computationally difficult to guess.<br/>
 <code>Nil UUID</code> There is a special <i>Nil</i> UUID consisting of all octets set to zero in the binary representation. It can be used as a special UUID value which does not conflict with real UUIDs.</p>
<h2>Application Programming Interface</h2>
<p>The ISO-C Application Programming Interface (API) of <code>OSSP</code><code> uuid</code> consists of the following components. </p>
<p> <code>CONSTANTS</code> </p>
<p> The following constants are provided:</p>
<dl>
<dt><code>UUID_VERSION</code></dt>
<dd>The hexadecimal encoded <code>OSSP</code><code> uuid</code> version. This allows compile-time checking of the <code>OSSP</code><code> uuid</code> version. For run-time checking use <code>uuid_version</code>() instead. </dd>
<p> The hexadecimal encoding for a version &quot;$<i>v</i>.$<i>r</i>$<i>t</i>$<i>l</i>&quot; is calculated with the <code>GNU</code><code> shtool</code> <code>version</code> command and is (in Perl-style for concise description) &quot;sprintf(&#8216;0x%x%02x%d%02x&#8217;, $<i>v</i>, $<i>r</i>, {qw(s 9 . 2 b 1 a 0)}-&gt;{$<i>t</i>}, ($<i>t</i> eq &#8216;s&#8217; ? 99 : $<i>l</i>))&#8220;, i.e., the version 0.9.6 is encoded as &#8221;0x009206&quot;.</p>
<dt><code>UUID_LEN_BIN</code>, <code>UUID_LEN_STR</code>, <code>UUID_LEN_SIV</code></dt>
<dd>The number of octets of the UUID binary and string representations. Notice that the lengths of the string representation (<code>UUID_LEN_STR</code>) and the lengths of the single integer value representation (<code>UUID_LEN_SIV</code>) does <i>not</i> include the necessary <tt> NUL<br/>
 </tt> termination character.</dd>
<dt><code>UUID_MAKE_V1</code>, <code>UUID_MAKE_V3</code>, <code>UUID_MAKE_V4</code>, <code>UUID_MAKE_V5</code>, <code>UUID_MAKE_MC</code></dt>
<dd>The <i>mode</i> bits for use with <code>uuid_make</code>(). The <code>UUID_MAKE_V</code><i>N</i> specify which UUID version to generate. The <code>UUID_MAKE_MC</code> forces the use of a random multi-cast MAC address instead of the real physical MAC address in version 1 UUIDs.</dd>
<dt><code>UUID_RC_OK</code>, <code>UUID_RC_ARG</code>, <code>UUID_RC_MEM</code>, <code>UUID_RC_SYS</code>, <code>UUID_RC_INT</code>, <code>UUID_RC_IMP</code></dt>
<dd>The possible numerical return-codes of API functions. The <tt> UUID_RC_OK<br/>
 </tt> indicates success, the others indicate errors. Use <code>uuid_error</code>() to translate them into string versions.</dd>
<dt><code>UUID_FMT_BIN</code>, <code>UUID_FMT_STR</code>, <code>UUID_FMT_SIV</code>, <code>UUID_FMT_TXT</code></dt>
<dd>The <i>fmt</i> formats for use with <code>uuid_import</code>() and <code>uuid_export</code>(). The <code>UUID_FMT_BIN</code> indicates the UUID binary representation (of length <code>UUID_LEN_BIN</code>), the <code>UUID_FMT_STR</code> indicates the UUID string representation (of length <code>UUID_LEN_STR</code>), the <code>UUID_FMT_SIV</code> indicates the UUID single integer value representation (of maximum length <code>UUID_LEN_SIV</code>) and the <code>UUID_FMT_TXT</code> indicates the textual description (of arbitrary length) of a UUID.
</dd></dl>
<p> <code>FUNCTIONS</code> </p>
<p> The following functions are provided:</p>
<dl>
<dt>uuid_rc_t <code>uuid_create</code>(uuid_t **<i>uuid</i>);</dt>
<dd>Create a new UUID object and store a pointer to it in <tt> *<br/>
 </tt><i>uuid</i>. A UUID object consists of an internal representation of a UUID, the internal PRNG and MD5 generator contexts, and cached MAC address and timestamp information. The initial UUID is the <i>Nil</i> UUID.</dd>
<dt>uuid_rc_t <code>uuid_destroy</code>(uuid_t *<i>uuid</i>);</dt>
<dd>Destroy UUID object <i>uuid</i>.</dd>
<dt>uuid_rc_t <code>uuid_clone</code>(const uuid_t *<i>uuid</i>, uuid_t **<i>uuid_clone</i>);</dt>
<dd>Clone UUID object <i>uuid</i> and store new UUID object in <i>uuid_clone</i>.</dd>
<dt>uuid_rc_t <code>uuid_isnil</code>(const uuid_t *<i>uuid</i>, int *<i>result</i>);</dt>
<dd>Checks whether the UUID in <i>uuid</i> is the <i>Nil</i> UUID. If this is the case, it returns <i>true</i> in <tt> *<br/>
 </tt><i>result</i>. Else it returns <i>false</i> in <tt> *<br/>
 </tt><i>result</i>.</dd>
<dt>uuid_rc_t <code>uuid_compare</code>(const uuid_t *<i>uuid</i>, const uuid_t *<i>uuid2</i>, int *<i>result</i>);</dt>
<dd>Compares the order of the two UUIDs in <i>uuid1</i> and <i>uuid2</i> and returns the result in <tt> *<br/>
 </tt><i>result</i>: <tt> -1<br/>
 </tt> if <i>uuid1</i> is smaller than <i>uuid2</i>, <tt>0</tt> if <i>uuid1</i> is equal to <i>uuid2</i> and <tt>+1</tt> if <i>uuid1</i> is greater than <i>uuid2</i>.</dd>
<dt>uuid_rc_t <code>uuid_import</code>(uuid_t *<i>uuid</i>, uuid_fmt_t <i>fmt</i>, const void *<i>data_ptr</i>, size_t <i>data_len</i>);</dt>
<dd>Imports a UUID <i>uuid</i> from an external representation of format <i>fmt</i>. The data is read from the buffer at <i>data_ptr</i> which contains at least <i>data_len</i> bytes. </dd>
<p> The format of the external representation is specified by <i>fmt</i> and the minimum expected length in <i>data_len</i> depends on it. Valid values for <i>fmt</i> are <code>UUID_FMT_BIN</code>, <code>UUID_FMT_STR</code> and <code>UUID_FMT_SIV</code>.</p>
<dt>uuid_rc_t <code>uuid_export</code>(const uuid_t *<i>uuid</i>, uuid_fmt_t <i>fmt</i>, void *<i>data_ptr</i>, size_t *<i>data_len</i>);</dt>
<dd>Exports a UUID <i>uuid</i> into an external representation of format <i>fmt</i>. Valid values for <i>fmt</i> are <code>UUID_FMT_BIN</code>, <code>UUID_FMT_STR</code>, <code>UUID_FMT_SIV</code> and <code>UUID_FMT_TXT</code>. </dd>
<p> The data is written to the buffer whose location is obtained by dereferencing <i>data_ptr</i> after a &#8220;cast&#8221; to the appropriate pointer-to-pointer type. Hence the generic pointer argument <i>data_ptr</i> is expected to be a pointer to a &#8220;pointer of a particular type&#8221;, i.e., it has to be of type &quot;<tt> unsigned char **<br/>
 </tt>&quot; for <code>UUID_FMT_BIN</code> and &quot;<tt> char **<br/>
 </tt>&quot; for <code>UUID_FMT_STR</code>, <code>UUID_FMT_SIV</code> and <code>UUID_FMT_TXT</code>. </p>
<p> The buffer has to be room for at least <tt> *<br/>
 </tt><i>data_len</i> bytes. If the value of the pointer after &#8220;casting&#8221; and dereferencing <i>data_ptr</i> is <tt> NULL<br/>
 </tt>, <i>data_len</i> is ignored as input and a new buffer is allocated and returned in the pointer after &#8220;casting&#8221; and dereferencing <i>data_ptr</i> (the caller has to <i><a href="/docs/linux/man/3-free/">free</a></i>(3) it later on). </p>
<p> If <i>data_len</i> is not <tt> NULL<br/>
 </tt>, the number of available bytes in the buffer has to be provided in <tt> *<br/>
 </tt><i>data_len</i> and the number of actually written bytes are returned in <tt> *<br/>
 </tt><i>data_len</i> again. The minimum required buffer length depends on the external representation as specified by <i>fmt</i> and is at least <code>UUID_LEN_BIN</code> for <code>UUID_FMT_BIN</code>, <code>UUID_LEN_STR</code> for <code>UUID_FMT_STR</code> and <code>UUID_LEN_SIV</code> for <code>UUID_FMT_SIV</code>. For <code>UUID_FMT_TXT</code> a buffer of unspecified length is required and hence it is recommended to allow <code>OSSP</code><code> uuid</code> to allocate the buffer as necessary.</p>
<dt>uuid_rc_t <code>uuid_load</code>(uuid_t *<i>uuid</i>, const char *<i>name</i>);</dt>
<dd>Loads a pre-defined UUID value into the UUID object <i>uuid</i>. The following <i>name</i> arguments are currently known:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>name</i> <i></i><i>UUID</i><i></i></dt>
<dd>
</dd><dt>nil 00000000-0000-0000-0000-000000000000</dt>
<dd>
</dd><dt>ns:DNS 6ba7b810-9dad-11d1-80b4-00c04fd430c8</dt>
<dd>
</dd><dt>ns:URL 6ba7b811-9dad-11d1-80b4-00c04fd430c8</dt>
<dd>
</dd><dt>ns:OID 6ba7b812-9dad-11d1-80b4-00c04fd430c8</dt>
<dd>
</dd><dt>ns:X500 6ba7b814-9dad-11d1-80b4-00c04fd430c8</dt>
<dd></dd></dl>
</dl>
<dl>
<dd>The &quot;<tt> ns:<br/>
 </tt><i></i><i>XXX</i><i></i>&quot; are names of pre-defined name-space UUIDs for use in the generation of DCE 1.1 version 3 and version 5 UUIDs.</dd></dl>
<dt>uuid_rc_t <code>uuid_make</code>(uuid_t *<i>uuid</i>, unsigned int <i>mode</i>, &#8230;);</dt>
<dd>Generates a new UUID in <i>uuid</i> according to <i>mode</i> and optional arguments (dependent on <i>mode</i>). </dd>
<p> If <i>mode</i> contains the <tt> UUID_MAKE_V1<br/>
 </tt> bit, a DCE 1.1 variant UUID of version 1 is generated. Then optionally the bit <tt> UUID_MAKE_MC<br/>
 </tt> forces the use of random multi-cast MAC address instead of the real physical MAC address (the default). The UUID is generated out of the 60-bit current system time, a 12-bit clock sequence and the 48-bit MAC address. </p>
<p> If <i>mode</i> contains the <tt> UUID_MAKE_V3<br/>
 </tt> or <tt> UUID_MAKE_V5<br/>
 </tt> bit, a DCE 1.1 variant UUID of version 3 or 5 is generated and two additional arguments are expected: first, a namespace UUID object (<tt> uuid_t *<br/>
 </tt>). Second, a name string of arbitrary length (<tt> const char *<br/>
 </tt>). The UUID is generated out of the 128-bit MD5 or 160-bit SHA-1 from the concatenated octet stream of namespace UUID and name string. </p>
<p> If <i>mode</i> contains the <tt> UUID_MAKE_V4<br/>
 </tt> bit, a DCE 1.1 variant UUID of version 4 is generated. The UUID is generated out of 128-bit random data.</p>
<dt>char *<code>uuid_error</code>(uuid_rc_t <i>rc</i>);</dt>
<dd>Returns a constant string representation corresponding to the return-code <i>rc</i> for use in displaying <code>OSSP</code><code> uuid</code> errors.</dd>
<dt>unsigned long <code>uuid_version</code>(void);</dt>
<dd>Returns the hexadecimal encoded <code>OSSP</code><code> uuid</code> version as compiled into the library object files. This allows run-time checking of the <code>OSSP</code><code> uuid</code> version. For compile-time checking use <tt> UUID_VERSION<br/>
 </tt> instead.</dd></dl>
<h2>Example</h2>
<p>The following shows an example usage of the API. Error handling is omitted for code simplification and has to be re-added for production code. </p>
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
<p>The following are references to <code>UUID</code> documentation and specifications:</p>
<dl>
<dt>&bull;</dt>
<dd><code>A Universally Unique IDentifier (</code><code>UUID</code><code>) </code><code>URN</code><code> Namespace</code>, P. Leach, M. Mealling, R. Salz, IETF RFC-4122, July 2005, 32 pages, <a rel="nofollow" href="http://www.ietf.org/rfc/rfc4122.txt">http://www.ietf.org/rfc/rfc4122.txt</a></dd>
<dt>&bull;</dt>
<dd>Information Technology &#8212; Open Systems Interconnection (OSI), <code>Procedures for the operation of </code><code>OSI</code><code> Registration Authorities: Generation and Registration of Universally Unique Identifiers (UUIDs) and their Use as </code><code>ASN</code><code>.1 Object Identifier Components</code>, ISO/IEC 9834-8:2004 / ITU-T Rec. X.667, 2004, December 2004, 25 pages, <a rel="nofollow" href="http://www.itu.int/ITU-T/studygroups/com17/oid/X.667-E.pdf">http://www.itu.int/ITU-T/studygroups/com17/oid/X.667-E.pdf</a></dd>
<dt>&bull;</dt>
<dd><code>DCE</code><code> 1.1: Remote Procedure Call</code>, appendix <code>Universally Unique Identifier</code>, Open Group Technical Standard Document Number C706, August 1997, 737 pages, (supersedes C309 DCE: Remote Procedure Call 8/1994, which was basis for ISO/IEC 11578:1996 specification), <a rel="nofollow" href="http://www.opengroup.org/publications/catalog/c706.htm">http://www.opengroup.org/publications/catalog/c706.htm</a></dd>
<dt>&bull;</dt>
<dd>Information technology &#8212; Open Systems Interconnection (OSI), <code>Remote Procedure Call (</code><code>RPC</code><code>)</code>, ISO/IEC 11578:1996, August 2001, 570 pages, (CHF 340,00), <a rel="nofollow" href="http://www.iso.ch/cate/d2229.html">http://www.iso.ch/cate/d2229.html</a></dd>
<dt>&bull;</dt>
<dd><code>HTTP</code><code> Extensions for Distributed Authoring (WebDAV)</code>, section <code>6.4.1 Node Field Generation Without the </code><code>IEEE</code><code> 802 Address</code>, IETF RFC-2518, February 1999, 94 pages, <a rel="nofollow" href="http://www.ietf.org/rfc/rfc2518.txt">http://www.ietf.org/rfc/rfc2518.txt</a></dd>
<dt>&bull;</dt>
<dd><code>DCE</code><code> 1.1 compliant </code><code>UUID</code><code> functions</code>, FreeBSD manual pages <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) and <i>uuidgen</i>(2), <a rel="nofollow" href="http://www.freebsd.org/cgi/man.cgi?query=uuid">http://www.freebsd.org/cgi/man.cgi?query=uuid</a>&amp;manpath=FreeBSD+6.0-RELEASE</dd></dl>
<h2>History</h2>
<p><code>OSSP</code><code> uuid</code> was implemented in January 2004 by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt;. It was prompted by the use of UUIDs in the <code>OSSP</code><code> as</code> and <code>OpenPKG</code> projects. It is a clean room implementation intended to be strictly standards compliant and maximum portable.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-uuid/">uuid</a></i>(1), <i><a href="/docs/linux/man/1-uuid-config/">uuid-config</a></i>(1), <i>OSSP::uuid</i>(3). </p>
