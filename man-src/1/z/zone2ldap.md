---
title: "zone2ldap(1)"
name: "zone2ldap"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zone2ldap/"
---

<h2>NAME</h2>

 zone2ldap /- Load BIND 9 Zone files into LDAP Directory

<h2>SYNOPSIS</h2>

 zone2ldap [-D Bind DN] [-w Bind Password] [-b Base DN] [-z Zone] [-f Zone File ] [-h Ldap Host] [-cd] [-v]

<h2>DESCRIPTION</h2>

 zone2ldap will parse a complete BIND 9 format DNS zone file, and load the contents into an LDAP directory, for use with the LDAP sdb back-end. 

 If the zone already exists, zone2ldap will exit succesfully. If the zone does not exists, or partially exists, zone2ldap will attempt to add all/missing zone data. 

<h3>Options</h3>

<dl>
<dt>-b
<dd> LDAP Base DN. LDAP systems require a &quot;base dn&quot;, which is generally considered the LDAP Directory root. If the zone you are loading is different from the base, then you will need to tell zone2ldap what your LDAP base is.
<dt>-v
<dd> Print version information, and immediatly exit.
<dt>-f
<dd> Zone file. Bind 9.1 compatible zone file, from which zone information will be read.
<dt>-d
<dd> Dump debug information to standard out.
<dt>-w
<dd> LDAP Bind password, corresponding the the value of &quot;-b&quot;.
<dt>-h
<dd> LDAP Directory host. This is the hostname of the LDAP system you wish to store zone information on. An LDAP server should be listening on port 389 of the target system. This may be ommited, and will default to &quot;localhost&quot;.
<dt>-c
<dd> This will create the zone portion of the DN you are importing. For instance, if you are creating a domain.com zone, zone2ldap should first create &quot;dc=domain,dc=com&quot;. This is useful if you are creating multiple domains.
<dt>-z
<dd> This is the name of the zone specified in the SOA record.</dl>

<h2>EXAMPLES</h2>

 Following are brief examples of how to import a zone file into your LDAP DIT.

<h3>Loading zone domain.com, with an LDAP Base DN of dc=domain,dc=com</h3>

 zone2ldap -D dc=root -w secret -h localhost -z domain.com -f domain.com.zone 

 This will add Resource Records into an ALREADY EXISTING dc=domain,dc=com. The final SOA DN in this case, will be dc=@,dc=domain,dc=com 

<h3>Loading customer.com, if your LDAP Base DN is dc=provider,dc=net.</h3>

 zone2ldap -D dc=root -w secret -h localhost -z customer.com -b dc=provider,dc=net -f customer.com.zone -c 

 This will create dc=customer,dc=com under dc=provider,dc=net, and add all necessary Resource Records. The final root DN to the SOA will be dc=@,dc=customer,dc=com,dc=provider,dc=net. 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/8-named/">named</a>(8) <a HREF="/docs/linux/man/3-ldap/">ldap</a>(3) <a rel="nofollow" HREF="http://www.venaas.no/ldap/bind-sdb/">http://www.venaas.no/ldap/bind-sdb/</a>

<h2>BUGS</h2>

 Send all bug reports to Jeff McNeil &lt;jeff [at] snapcase.g-rock.net&gt;

<h2>AUTHOR</h2>

 Jeff McNeil &lt;jeff [at] snapcase.g-rock.net&gt; 

 

<h2>Index</h2>


