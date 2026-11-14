---
title: "ipa-ldap-updater(1)"
name: "ipa-ldap-updater"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-ldap-updater/"
description: "ipa-ldap-updater – Update the IPA LDAP configuration"
---

<h2>NAME</h2>
<p> ipa-ldap-updater &#8211; Update the IPA LDAP configuration</p>
<h2>SYNOPSIS</h2>
<p> ipa-ldap-updater [options] input_file(s)</p>
<h2>DESCRIPTION</h2>
<p> ipa-ldap-updater is utility which can be used to update the IPA LDAP server. </p>
<p> An update file describes an LDAP entry and a set of operations to be performed on that entry. It can be used to add new entries or modify existing entries. </p>
<p> Blank lines and lines beginning with # are ignored. </p>
<p> There are 7 keywords: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>default: the starting value<br />
&nbsp;<wbr>*&nbsp;<wbr>add: add a value to an attribute<br />
&nbsp;<wbr>*&nbsp;<wbr>remove: remove a value from an attribute<br />
&nbsp;<wbr>*&nbsp;<wbr>only: set an attribute to this<br />
&nbsp;<wbr>*&nbsp;<wbr>onlyifexist: set an attribute to this only if the entry exists<br />
&nbsp;<wbr>*&nbsp;<wbr>deleteentry: remove the entry<br />
&nbsp;<wbr>*&nbsp;<wbr>replace: replace an existing value, format is old::new<br />
&nbsp;<wbr>*&nbsp;<wbr>addifnew: add a new attribute and value only if the attribute doesn&#8217;t already exist. Only works with single-value attributes.<br />
&nbsp;<wbr>*&nbsp;<wbr>addifexist: add a new attribute and value only if the entry exists. This is used to update optional entries. </p>
<p> The difference between the default and add keywords is if the DN of the entry exists then default is ignored. So for updating something like schema, which will be under cn=schema, you must always use add (because cn=schema is guaranteed to exist). It will not re-add the same information again and again. </p>
<p> It also provides some things that can be templated such as architecture (for plugin paths), realm and domain name. </p>
<p> The available template variables are: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>$REALM &#8211; the kerberos realm&nbsp;<wbr>(EXAMPLE.COM)<br />
&nbsp;<wbr>*&nbsp;<wbr>$FQDN &#8211; the fully-qualified domain name of the IPA server being updated&nbsp;<wbr>(ipa.example.com)<br />
&nbsp;<wbr>*&nbsp;<wbr>$DOMAIN &#8211; the domain name&nbsp;<wbr>(example.com)<br />
&nbsp;<wbr>*&nbsp;<wbr>$SUFFIX &#8211; the IPA LDAP suffix&nbsp;<wbr>(dc=example,dc=com)<br />
&nbsp;<wbr>*&nbsp;<wbr>$ESCAPED_SUFFIX &#8211; the ldap-escaped IPA LDAP suffix<br />
&nbsp;<wbr>*&nbsp;<wbr>$LIBARCH &#8211; set to 64 on x86_64 systems to be used for plugin paths<br />
&nbsp;<wbr>*&nbsp;<wbr>$TIME &#8211; an integer representation of current time </p>
<p> For base64 encoded values a double colon (&#8216;::&#8217;) must be used between attribute and value. </p>
<p> Base64 format examples:<br />
&nbsp;<wbr>add:binaryattr::d2UgbG92ZSBiYXNlNjQ=<br />
&nbsp;<wbr>replace:binaryattr::SVBBIGlzIGdyZWF0::SVBBIGlzIHJlYWxseSBncmVhdA== </p>
<p> A few rules: </p>
<p>1. Only one rule per line<br />
2. Each line stands alone&nbsp;<wbr>(e.g. an only followed by an only results in the last only being used)<br />
3. Adding a value that exists is ok. The request is ignored, duplicate values are not added<br />
4. Removing a value that doesn&#8217;t exist is ok. It is simply ignored.<br />
5. If a DN doesn&#8217;t exist it is created from the&nbsp;<wbr>&#8216;default&#8217;&nbsp;<wbr>entry and all updates are applied<br />
6. If a DN does exist the default values are skipped<br />
7. Only the first rule on a line is respected </p>
<p> ipa-ldap-updater allows to execute update plugins. Plugins to be executed are specified with following keyword, in update files:<br />
&nbsp;<wbr>*&nbsp;<wbr>plugin: name of plugin </p>
<p> This keyword is not bounded to DN, and plugin names have to be registered in API. </p>
<p> Additionally, ipa-ldap-updater can update the schema based on LDIF files. Any missing object classes and attribute types are added, and differing ones are updated to match the LDIF file. To enable this behavior, use the &#8211;schema-file options. Schema files should be in LDIF format, and may only specify attributeTypes and objectClasses attributes of cn=schema. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Enable debug logging when more verbose output is needed</p>
<dt><code>-u</code>, <code>&#8211;upgrade</code></p>
<dd> Upgrade an installed server in offline mode (implies &#8211;schema)</p>
<dt><code>-S</code>, <code>&#8211;schema-file</code></p>
<dd> Specify a schema file. May be used multiple times. Implies &#8211;schema.</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
