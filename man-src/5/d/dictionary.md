---
title: "dictionary(5)"
name: "dictionary"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dictionary/"
description: "dictionary – RADIUS dictionary file"
---

<p>dictionary &#8211; RADIUS dictionary file</p>
<h2>Description</h2>
<p>The master RADIUS dictionary file resides in <i>/etc/raddb/dictionary</i>. It references other <i>dictionary</i> files located in <i>/usr/local/share/freeradius/</i>. Each dictionary file contains a list of RADIUS attributes and values, which the server uses to map between descriptive names and on-the-wire data. The names have no meaning outside of the RADIUS server itself, and are never exchanged between server and clients. That is, editing the dictionaries will have NO EFFECT on anything other than the server that is reading those files. Adding new attributes to the dictionaries will have NO EFFECT on RADIUS clients, and will not make RADIUS clients magically understand those attributes. The dictionaries are solely for local administrator convenience, and are specific to each version of FreeRADIUS. The dictionaries in <i>/usr/local/share</i> SHOULD NOT be edited unless you know exactly what you are doing. Changing them will most likely break your RADIUS deployment. If you need to add new attributes, please edit the <i>/etc/raddb/dictionary</i> file. It&#8217;s sole purpose is to contain site-local defintions that are added by the local administrator. </p>
<h2>Format</h2>
<p>Every line starting with a hash sign (&#8216;<code>#</code>&#8216;) is treated as comment and ignored. </p>
<p> Each line of the file can contain one of the following strings:</p>
<dl>
<dt><code>ATTRIBUTE name oid type [flags]</code></p>
<dd>Define a RADIUS attribute name to number mapping. </p>
<p> The <i>name</i> field is a printable field, taken from various specifications or vendor definitions. It is most commonly used as a series of words, separated by hyphens. e.g. &quot;User-Name&quot;. Vendor-specific attributes (VSAs) are prefixed by the vendor name, e.g. &quot;Cisco-AVPair&quot;. The names should be globally unique, as they are used as a key to look up the properties of the attribute. </p>
<p> The <i>oid</i> field is taken from the relevant specification for that name. In most cases, it is a decimal number, such as &quot;256&quot;. For certain attributes, a &quot;dotted number&quot; notation is used, e.g. &quot;1.2&quot;. The &quot;dotted number&quot; notation is used only for certain attributes. </p>
<p> The <i>type</i> field can be one of the standard types: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>string&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>UTF-8 printable text&nbsp;<wbr>(the RFCs call this&nbsp;<wbr>&quot;text&quot;)<br />
&nbsp;<wbr>&nbsp;<wbr>octets&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>opaque binary data&nbsp;<wbr>(the RFCs call this&nbsp;<wbr>&quot;string&quot;)<br />
&nbsp;<wbr>&nbsp;<wbr>ipaddr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>IPv4 address<br />
&nbsp;<wbr>&nbsp;<wbr>date&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Seconds since January 1, 1970&nbsp;<wbr>(32-bits)<br />
&nbsp;<wbr>&nbsp;<wbr>integer&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>32-bit unsigned integer<br />
&nbsp;<wbr>&nbsp;<wbr>ipv6addr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>IPv6 Address<br />
&nbsp;<wbr>&nbsp;<wbr>ipv6prefix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>IPV6 prefix, with mask<br />
&nbsp;<wbr>&nbsp;<wbr>ifid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Interface Id&nbsp;<wbr>(hex:hex:hex:hex)<br />
&nbsp;<wbr>&nbsp;<wbr>integer64<tt>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>64-bit unsigned integer</p>
<p> The <i>type</i> field can be one of the following non-standard types: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ether&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Ethernet MAC address<br />
&nbsp;<wbr>&nbsp;<wbr>abinary&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Ascend binary filter format<br />
&nbsp;<wbr>&nbsp;<wbr>byte&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8-bit unsigned integer<br />
&nbsp;<wbr>&nbsp;<wbr>short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>16-bit unsigned integer<br />
&nbsp;<wbr>&nbsp;<wbr>signed&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>31-bit signed integer&nbsp;<wbr>(packed into 32-bit field)<br />
&nbsp;<wbr>&nbsp;<wbr>tlv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Type-Length-Value&nbsp;<wbr>(allows nested attributes)<br />
&nbsp;<wbr>&nbsp;<wbr>ipv4prefix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>IPv4 Prefix as given in RFC 6572. </p>
<p> The last (optional) field of an attribute definition are additional flags for that attribute, in a comma-separated list. Previous versions of the server allowed these flags to include a vendor name. This behavior may still work, but it is deprecated, and is not recommended. </p>
<p> The options are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>encrypt=#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>set encryption type 1, 2, or 3.<br />
&nbsp;<wbr>&nbsp;<wbr>has_tag&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The attribute can have an RFC 2868 style tag </p>
<p> The &quot;encrypt&quot; flag marks the attribute as being encrypted with one of three possible methods. &quot;1&quot; means that the attribute is encrypted with the method as defined in <i>RFC2865</i> for the User-Password attribute. &quot;2&quot; means that the password is encrypted with the method as defined in <i>RFC2868</i> for the Tunnel-Password attribute. &quot;3&quot; means that the attribute is encrypted as per Ascend&#8217;s definitions for the Ascend-Send-Secret attribute. </p>
<p> The &quot;has_tag&quot; flag marks the attribute as being permitted to have a tag, as defined in <i>RFC2868</i>. The purpose of the tag is to allow grouping of attributes for tunneled users. See <i>RFC2868</i> for more details. </p>
<p> When the server receives an encoded attribute in a RADIUS packet, it looks up that attribute by number in the dictionary, and uses the definition found there for printing diagnostic and log messages. When the server sees an attribute name in a configuration file, it looks up that attribute by name in the dictionary, and uses the definition found there. </p>
<dt><code>VALUE attribute-name value-name number</code></p>
<dd>Define an attribute value name to number mapping, for an attribute of type <i>integer</i>. The <i>attribute-name</i> field MUST be previously defined by an <i>ATTRIBUTE</i> entry. The <i>value-name</i> field can be any non-space text, but is usually taken from <i>RFC2865</i>, or other documents.. The <i>number</i> field is also taken from the relevant documents, for that name. </p>
<p> When the server receives an encoded value in a RADIUS packet, it looks up the value of that attribute by number in the dictionary, and uses the name found there for printing diagnostic and log messages.</p>
<dt><code>VENDOR vendor-name number [format=&#8230;]</code></p>
<dd>Define a Vendor Specific Attribute encapsulation for <i>vendor-name</i> to <i>number</i>. For a list of vendor names and numbers, see <a rel="nofollow" href="http://www.iana.org/enterprise-numbers.txt.">http://www.iana.org/enterprise-numbers.txt.</a> </p>
<p> The &quot;format=t,l&quot; statement tells the server how many octets to use to encode/decode the vendor &quot;type&quot; and &quot;length&quot; fields in the attributes. The default is &quot;format=1,1&quot;, which does not have to be specified. For USR VSA&#8217;s, the format is &quot;format=4,0&quot;, for Lucent VSA&#8217;s it&#8217;s &quot;format=2,1&quot;, and for Starent VSA&#8217;s it&#8217;s &quot;format=2,2&quot;. </p>
<p> The supported values for the number of type octets (i.e. the first digit) are 1, 2, and 4. The support values for the number of length octets (i.e. the second digit) are 0, 1, and 2. Any combination of those values will work. </p>
<p> You can also use &quot;format=Extended-Vendor-Specific-1&quot;, through &quot;format=Extended-Vendor-Specific-6&quot;. These define VSAs in the &quot;extended vendor-specific&quot; space.</p>
<dt><code>BEGIN-VENDOR vendor-name</code></p>
<dd>Define the start of a block of Vendor-Specific attributes. All of the following <i>ATTRIBUTE</i> definitions are interpreted as being for the named vendor, until the block is closed by an &quot;END-VENDOR&quot; statement. </p>
<p> This practice is preferred to placing the vendor name at the end of an <i>ATTRIBUTE</i> definition.</p>
<dt><code>END-VENDOR vendor-name</code></p>
<dd>End a previously defined BEGIN-VENDOR block. The &quot;vendor-name&quot; must match.</p>
<dt><code>$INCLUDE filename</code></p>
<dd>Include dictionary entries from the file <i>filename</i>. The <i>filename</i> is taken as relative to the location of the file which is asking for the inclusion.</p>
<dt><code>BEGIN-TLV name</code></p>
<dd>This feature is supported for backwards compatibility with older dictionaries. It should not be used. The new &quot;oid&quot; form for defining the attribute number should be used instead.</p>
<dt><code>END-TLV name</code></p>
<dd>This feature is supported for backwards compatibility with older dictionaries. It should not be used. The new &quot;oid&quot; form for defining the attribute number should be used instead.</dl>
<h2>Files</h2>
<p><i>/etc/raddb/dictionary,</i> <i>/usr/share/freeradius/dictionary.*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code>RFC2865,</code> <code>RFC2866,</code> <code>RFC2868</code> </p>
