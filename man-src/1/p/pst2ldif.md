---
title: "pst2ldif(1)"
name: "pst2ldif"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pst2ldif/"
description: "pst2ldif – extract contacts from a MS Outlook .pst file in .ldif format"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pst2ldif</code> [<code>-V</code>] [<code>-b&nbsp;<wbr></code><i>ldap-base</i>] [<code>-c&nbsp;<wbr></code><i>class</i>] [<code>-d&nbsp;<wbr></code><i>debug-file</i>] [<code>-l&nbsp;<wbr></code><i>extra-line</i>] [<code>-o</code>] [<code>-h</code>] pstfilename</dt></dl>
<h2>OPTIONS</h2>
<p> -V</p>
<dl>
<dd>Show program version. Subsequent options are then ignored.</dd></dl>
<p> -b <i>ldap-base</i></p>
<dl>
<dt>
</dt><dd> Sets the ldap base value used in the dn records. You probably want to use something like &quot;o=organization, c=US&quot;.</dd></dl>
<p> -c <i>class</i></p>
<dl>
<dt>
</dt><dd> Sets the objectClass values for the contact items. This class needs to be defined in the schema used by your LDAP server, and at a minimum it must contain the ldap attributes given below. This option may be specified multiple times to generate entries with multiple object classes.</dd></dl>
<p> -d <i>debug-file</i></p>
<dl>
<dt>
</dt><dd> Specify name of debug log file. The log file is now an ascii file, instead of the binary file used in previous versions.</dd></dl>
<p> -l <i>extra-line</i></p>
<dl>
<dt>
</dt><dd> Specify an extra line to be added to each ldap entry. This option may be specified multiple times to add multiple lines to each ldap entry.</dd></dl>
<p> -o</p>
<dl>
<dt>
</dt><dd> Use the old ldap schema, rather than the default new ldap schema. The old schema generates multiple postalAddress attributes for a single entry. The new schema generates a single postalAddress (and homePostalAddress when available) attribute with $ delimiters as specified in RFC4517. Using the old schema also generates two extra leading entries, one for &quot;dn:ldap base&quot;, and one for &quot;dn: cn=root, ldap base&quot;.</dd></dl>
<p> -h</p>
<dl>
<dt>
</dt><dd> Show summary of options. Subsequent options are then ignored.</dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>pst2ldif</code> reads the contact information from a MS Outlook .pst file and produces a .ldif file that may be used to import those contacts into an LDAP database. The following ldap attributes are generated for the old ldap schema:</p>
<dl>
<dt>
</dt><dd> cn</dd></dl>
<dl>
<dt>
</dt><dd> givenName</dd></dl>
<dl>
<dt>
</dt><dd> sn</dd></dl>
<dl>
<dt>
</dt><dd> personalTitle</dd></dl>
<dl>
<dt>
</dt><dd> company</dd></dl>
<dl>
<dt>
</dt><dd> mail</dd></dl>
<dl>
<dt>
</dt><dd> postalAddress</dd></dl>
<dl>
<dt>
</dt><dd> l</dd></dl>
<dl>
<dt>
</dt><dd> st</dd></dl>
<dl>
<dt>
</dt><dd> postalCode</dd></dl>
<dl>
<dt>
</dt><dd> c</dd></dl>
<dl>
<dt>
</dt><dd> homePhone</dd></dl>
<dl>
<dt>
</dt><dd> telephoneNumber</dd></dl>
<dl>
<dt>
</dt><dd> facsimileTelephoneNumber</dd></dl>
<dl>
<dt>
</dt><dd> mobile</dd></dl>
<dl>
<dt>
</dt><dd> description</dd></dl>
<p> The following attributes are generated for the new ldap schema:</p>
<dl>
<dt>
</dt><dd> cn</dd></dl>
<dl>
<dt>
</dt><dd> givenName</dd></dl>
<dl>
<dt>
</dt><dd> sn</dd></dl>
<dl>
<dt>
</dt><dd> title</dd></dl>
<dl>
<dt>
</dt><dd> o</dd></dl>
<dl>
<dt>
</dt><dd> mail</dd></dl>
<dl>
<dt>
</dt><dd> postalAddress</dd></dl>
<dl>
<dt>
</dt><dd> homePostalAddress</dd></dl>
<dl>
<dt>
</dt><dd> l</dd></dl>
<dl>
<dt>
</dt><dd> st</dd></dl>
<dl>
<dt>
</dt><dd> postalCode</dd></dl>
<dl>
<dt>
</dt><dd> c</dd></dl>
<dl>
<dt>
</dt><dd> homePhone</dd></dl>
<dl>
<dt>
</dt><dd> telephoneNumber</dd></dl>
<dl>
<dt>
</dt><dd> facsimileTelephoneNumber</dd></dl>
<dl>
<dt>
</dt><dd> mobile</dd></dl>
<dl>
<dt>
</dt><dd> description</dd></dl>
<dl>
<dt>
</dt><dd> labeledURI</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2008 by 510 Software Group &lt;carl [at] five-ten-sg.com&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> You should have received a copy of the GNU General Public License along with this program; see the file COPYING. If not, please write to the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>VERSION</h2>
<p> 0.6.59 </p>
