---
title: "ldif(5)"
name: "ldif"
section: "5"
letter: "l"
url: "/docs/linux/man/5-ldif/"
description: "ldif – LDAP Data Interchange Format"
---

<p>ldif &#8211; LDAP Data Interchange Format</p>
<h2>Description</h2>
<p>The LDAP Data Interchange Format (LDIF) is used to represent LDAP entries and change records in text form. LDAP tools, such as <code><a href="/docs/linux/man/1-ldapadd/">ldapadd</a></code>(1) and <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1), read and write LDIF entry records. <code><a href="/docs/linux/man/1-ldapmodify/">ldapmodify</a></code>(1) reads LDIF change records. </p>
<p> This manual page provides a basic description of LDIF. A formal specification of LDIF is published in RFC 2849.</p>
<h2>Entry Records</h2>
<p>LDIF entry records are used to represent directory entries. The basic form of an entry record is: </p>
<pre> dn: &lt;distinguished name&gt;
 &lt;attrdesc&gt;: &lt;attrvalue&gt;
 &lt;attrdesc&gt;: &lt;attrvalue&gt;
 &lt;attrdesc&gt;:: &lt;base64-encoded-value&gt;
 &lt;attrdesc&gt;:&lt; &lt;URL&gt;
 ...</pre>
<p>The value may be specified as UTF-8 text or as base64 encoded data, or a URI may be provided to the location of the attribute value. </p>
<p> A line may be continued by starting the next line with a single space or tab, e.g., </p>
<pre> dn: cn=Barbara J Jensen,dc=exam
 ple,dc=com</pre>
<p>Lines beginning with a sharp sign (&#8216;#&#8217;) are ignored. </p>
<p> Multiple attribute values are specified on separate lines, e.g., </p>
<pre> cn: Barbara J Jensen
 cn: Babs Jensen</pre>
<p>If an value contains a non-printing character, or begins with a space or a colon &#8216;:&#8217;, the &lt;attrtype&gt; is followed by a double colon and the value is encoded in base 64 notation. e.g., the value &quot; begins with a space&quot; would be encoded like this: </p>
<pre> cn:: IGJlZ2lucyB3aXRoIGEgc3BhY2U=</pre>
<p>If the attribute value is located in a file, the &lt;attrtype&gt; is followed by a &#8216;:&lt;&#8216; and a file: URI. e.g., the value contained in the file /tmp/value would be listed like this: </p>
<pre> cn:&lt; file:///tmp/value</pre>
<p>Other URI schemes (ftp,http) may be supported as well. </p>
<p> Multiple entries within the same LDIF file are separated by blank lines.</p>
<h2>Entry Record Example</h2>
<p>Here is an example of an LDIF file containing three entries. </p>
<pre> dn: cn=Barbara J Jensen,dc=example,dc=com
 cn: Barbara J Jensen
 cn: Babs Jensen
 objectclass: person
 description:&lt; file:///tmp/babs
 sn: Jensen
 dn: cn=Bjorn J Jensen,dc=example,dc=com
 cn: Bjorn J Jensen
 cn: Bjorn Jensen
 objectclass: person
 sn: Jensen
 dn: cn=Jennifer J Jensen,dc=example,dc=com
 cn: Jennifer J Jensen
 cn: Jennifer Jensen
 objectclass: person
 sn: Jensen
 jpegPhoto:: /9j/4AAQSkZJRgABAAAAAQABAAD/2wBDABALD
 A4MChAODQ4SERATGCgaGBYWGDEjJR0oOjM9PDkzODdASFxOQ
 ERXRTc4UG1RV19iZ2hnPk1xeXBkeFxlZ2P/2wBDARESEhgVG
 ...</pre>
<p>Note that the description in Barbara Jensen&#8217;s entry is read from file:///tmp/babs and the jpegPhoto in Jennifer Jensen&#8217;s entry is encoded using base 64.</p>
<h2>Change Records</h2>
<p>LDIF change records are used to represent directory change requests. Each change record starts with line indicating the distinguished name of the entry being changed: </p>
<pre> dn: &lt;distinguishedname&gt;</pre>
<pre> changetype: &lt;[modify|add|delete|modrdn]&gt;</pre>
<p>Finally, the change information itself is given, the format of which depends on what kind of change was specified above. For a <i>changetype</i> of <i>modify</i>, the format is one or more of the following: </p>
<pre> add: &lt;attributetype&gt;
 &lt;attrdesc&gt;: &lt;value1&gt;
 &lt;attrdesc&gt;: &lt;value2&gt;
 ...
 -</pre>
<p>Or, for a replace modification: </p>
<pre> replace: &lt;attributetype&gt;
 &lt;attrdesc&gt;: &lt;value1&gt;
 &lt;attrdesc&gt;: &lt;value2&gt;
 ...
 -</pre>
<p>If no <i>attributetype</i> lines are given to replace, the entire attribute is to be deleted (if present). </p>
<p> Or, for a delete modification: </p>
<pre> delete: &lt;attributetype&gt;
 &lt;attrdesc&gt;: &lt;value1&gt;
 &lt;attrdesc&gt;: &lt;value2&gt;
 ...
 -</pre>
<p>If no <i>attributetype</i> lines are given to delete, the entire attribute is to be deleted. </p>
<p> For a <i>changetype</i> of <i>add</i>, the format is: </p>
<pre> &lt;attrdesc1&gt;: &lt;value1&gt;
 &lt;attrdesc1&gt;: &lt;value2&gt;
 ...
 &lt;attrdescN&gt;: &lt;value1&gt;
 &lt;attrdescN&gt;: &lt;value2&gt;</pre>
<p>For a <i>changetype</i> of <i>modrdn</i> or <i>moddn</i>, the format is: </p>
<pre> newrdn: &lt;newrdn&gt;
 deleteoldrdn: 0 | 1
 newsuperior: &lt;DN&gt;</pre>
<p>where a value of 1 for deleteoldrdn means to delete the values forming the old rdn from the entry, and a value of 0 means to leave the values as non-distinguished attributes in the entry. The newsuperior line is optional and, if present, specifies the new superior to move the entry to. </p>
<p> For a <i>changetype</i> of <i>delete</i>, no additional information is needed in the record. </p>
<p> Note that attribute values may be presented using base64 or in files as described for entry records. Lines in change records may be continued in the manner described for entry records as well.</p>
<h2>Change Record Example</h2>
<p>The following sample LDIF file contains a change record of each type of change. </p>
<pre> dn: cn=Babs Jensen,dc=example,dc=com
 changetype: add
 objectclass: person
 objectclass: extensibleObject
 cn: babs
 cn: babs jensen
 sn: jensen
 dn: cn=Babs Jensen,dc=example,dc=com
 changetype: modify
 add: givenName
 givenName: Barbara
 givenName: babs
 -
 replace: description
 description: the fabulous babs
 -
 delete: sn
 sn: jensen
 -
 dn: cn=Babs Jensen,dc=example,dc=com
 changetype: modrdn
 newrdn: cn=Barbara J Jensen
 deleteoldrdn: 0
 newsuperior: ou=People,dc=example,dc=com
 dn: cn=Barbara J Jensen,ou=People,dc=example,dc=com
 changetype: delete</pre>
<h2>Include Statement</h2>
<p>The LDIF parser has been extended to support an <code>include</code> statement for referencing other LDIF files. The <code>include</code> statement must be separated from other records by a blank line. The referenced file is specified using a file: URI and all of its contents are incorporated as if they were part of the original LDIF file. As above, other URI schemes may be supported. For example: </p>
<pre> dn: dc=example,dc=com
 objectclass: domain
 dc: example
 include: file:///tmp/example.com.ldif
 dn: dc=example,dc=org
 objectclass: domain
 dc: example</pre>
<p>This feature is not part of the LDIF specification in RFC 2849 but is expected to appear in a future revision of this spec. It is supported by the <code><a href="/docs/linux/man/1-ldapadd/">ldapadd</a></code>(1), <code><a href="/docs/linux/man/1-ldapmodify/">ldapmodify</a></code>(1), and <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8) commands.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1), <code><a href="/docs/linux/man/1-ldapadd/">ldapadd</a></code>(1), <code><a href="/docs/linux/man/1-ldapmodify/">ldapmodify</a></code>(1), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/5-slapd-ldif/">slapd-ldif</a></code>(5). </p>
<p> &quot;LDAP Data Interchange Format,&quot; Good, G., RFC 2849.</p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
