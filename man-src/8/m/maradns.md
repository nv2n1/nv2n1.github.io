---
title: "maradns(8)"
name: "maradns"
section: "8"
letter: "m"
url: "/docs/linux/man/8-maradns/"
description: "maradns – DNS server"
---

<pre>Erre con erre cigarro
Erre con erre barril
R'apido ruedan los carros
En el ferrocarril</pre>
<h2>Name</h2>
<p>maradns &#8211; DNS server</p>
<h2>Synopsis</h2>
<p><code>maradns [ -v | -f mararc_file_location ]</code></p>
<h2>Table Of Contents</h2>
<p>This man page has the following sections: </p>
<dl>
<dd>
<pre>Name 
Synopsis
Table of Contents
Description
Usage
Firewall Configuration
Frequently Asked Questions
Bugs
Unimplemented Features
Legal Disclaimer
Authors</pre>
</dl>
<h2>Description</h2>
<p><code>maradns</code> is a DNS server written with security, simplicity, and performance in mind. </p>
<p> <code>maradns</code> has two forms of arguments, both of which are optional. </p>
<p> The first is the location of a <code>mararc</code> file which MaraDNS obtains all configuration information from. The default location of this file is <code>/etc/mararc</code>. This is specified in the form <code>maradns -f mararc_file_location</code>; <i>mararc_file_location</i> is the location of the mararc file. </p>
<p> It is also possible to have MaraDNS display the version number and exit. This is specified by invoking maradns in the form <code>maradns -v</code> or <code>maradns &#8211;version</code></p>
<h2>Usage</h2>
<p>If MaraDNS is functioning only as a recursive nameserver, just one file needs to be set up: The mararc file. </p>
<p> In order for MaraDNS to function as an authoritative nameserver, two or more files need to be set up: the mararc file and one or more &quot;csv1&quot; zone files. </p>
<p> The configuration formation of a csv1 zone file can be obtained from the <code><a href="/docs/linux/man/5-csv1/">csv1</a>(5)</code> manual page. The configuration format of the mararc file can be obtained from the <code><a href="/docs/linux/man/5-mararc/">mararc</a>(5)</code> manual page. </p>
<p> In order to have MaraDNS run as a daemon, the duende program is used to daemonize MaraDNS. See the <code><a href="/docs/linux/man/8-duende/">duende</a>(8)</code> manual page for details.</p>
<h2>Firewall Configuration</h2>
<p>If MaraDNS is being used as an authoritative nameserver, allow UDP connections from all hosts on the internet to UDP port 53 for the IP that the authoritative nameserver uses. </p>
<p> If MaraDNS is being used as a recursive nameserver, the firewall needs to allow the following packets to go to and from the IP the recursive nameserver uses:</p>
<dl>
<dt>*</p>
<dd>Allow UDP connections from the MaraDNS-running server to any machine on the internet where the UDP destination port is 53</p>
<dt>*</p>
<dd>Allow UDP connections from any machine on the internet to the IP of the recursive server, where the source port from the remote server is 53, and the destination port is between 15000 and 19095 (inclusive)</p>
<dt>*</p>
<dd>Allow UDP connections from IPs that use MaraDNS as a recursive DNS server to port 53 of the MaraDNS server</dl>
<p> MaraDNS uses a strong secure RNG for both the query (16 bits of entropy) and the source port of the query (12 bits of entropy). This makes spoofing replies to a MaraDNS server more difficult, since the attacker has only a one in 250 million chance that a given spoofed reply will be considered valid.</p>
<h2>Frequently Asked Questions</h2>
<p><code>INDEX</code> </p>
<dl>
<dd>1. Iaqm still using version 1.0 of MaraDNS </p>
<p> 2. How do I try out MaraDNS? </p>
<p> 3. What license is MaraDNS released under? </p>
<p> 4. How do I report bugs in MaraDNS? </p>
<p> 5. Some of the postings to the mailing list do not talk about MaraDNS! </p>
<p> 6. How do I get off the mailing list? </p>
<p> 7. How do I set up reverse DNS on MaraDNS? </p>
<p> 8. I am on a slow network, and MaraDNS can not process recursive queries </p>
<p> 9. When I try to run MaraDNS, I get a cryptic error message. </p>
<p> 10. After I start MaraDNS, I can not see the process when I run netstat -na </p>
<p> 11. What string library does MaraDNS use? </p>
<p> 12. Why does MaraDNS use a multi-threaded model? </p>
<p> 13. I feel that XXX feature should be added to MaraDNS </p>
<p> 14. I feel that MaraDNS should use another documentation format </p>
<p> 15. Is there any process I need to follow to add a patch to MaraDNS? </p>
<p> 16. Can MaraDNS act as a primary nameserver? </p>
<p> 17. Can MaraDNS act as a secondary nameserver? </p>
<p> 18. What is the difference between an authoritative and a recursive DNS server? </p>
<p> 19. The getzone client isnaqt allowing me to add certain hostnames to my zone </p>
<p> 20. Is MaraDNS portable? </p>
<p> 21. Can I use MaraDNS in Windows? </p>
<p> 22. MaraDNS freezes up after being used for a while </p>
<p> 23. What kind of Python integration does MaraDNS have </p>
<p> 24. Doesnaqt &quot;kvar&quot; mean &quot;four&quot; in Esperanto? </p>
<p> 25. How scalable is MaraDNS? </p>
<p> 26. I am having problems setting upstream_servers </p>
<p> 27. Why doesnaqt the MaraDNS.org web page validate? </p>
<p> 28. How do MX records work? </p>
<p> 29. Does MaraDNS have support for SPF? </p>
<p> 30. Iaqm having problems resolving CNAMES I have set up. </p>
<p> 31. I have a NS delegation, and MaraDNS is doing strange things. </p>
<p> 32. I am transferring a zone from another server, but the NS records are these strange &quot;synth-ip&quot; records. </p>
<p> 33. Where is the root.hints file? </p>
<p> 34. Are there any plans to use autoconf to build MaraDNS? </p>
<p> 35. How do I change the compiler or compile-time flags with MaraDNSaq build process? </p>
<p> 36. Will you make a package for the particular Linux distribution I am using? </p>
<p> 37. I am using the native Windows port of MaraDNS, and some features are not working. </p>
<p> 38. MaraDNS isnaqt starting up </p>
<p> 39. You make a lot of releases of MaraDNS; at our ISP/IT department, updating software is non-trivial.</dl>
<p> <code>ANSWERS</code> </p>
<p> <code>1. Iaqm still using version 1.0 of MaraDNS</code> </p>
<p> MaraDNS 1.0 will continue to be supported until December 21, 2007; this means that MaraDNS 1.0 bug fixes will still be applied. After 2007/12/21, MaraDNS 1.0 will no longer be fully supported; the only updates, at that point, would be bugtraq-worthy critical security fixes. Not even these security updates will be applied after December 21, 2010. </p>
<p> People who wish to run MaraDNS 1.0 unsupported after 2010/12/21 need to keep in mind that MaraDNS 1.0 is <i>not</i> Y2038 compliant, and will have problems starting in 2036 or so. MaraDNS 1.2, on the other hand, is fully Y2038 compliant. </p>
<p> There is still a FAQ for version 1.0 of MaraDNS available here. </p>
<p> Updating from 1.0 to 1.2 requires a minimum number of changes; with most configurations, MaraDNS 1.2 is fully compatible with MaraDNS 1.0 data files. Details are in the updating document in the tutorial. </p>
<p> While csv1 zone files are fully supported in MaraDNS 1.2, there is a Perl script for updating from CSV1 to CSV2 zone files in the tools/ directory of MaraDNS 1.2. </p>
<p> <code>2. How do I try out MaraDNS?</code> </p>
<p> Read the quick start guide, which is the file named 0QuickStart in the MaraDNS distribution. </p>
<p> <code>3. What license is MaraDNS released under?</code> </p>
<p> MaraDNS 1.2 is released with the following two-clause BSD-type license: </p>
<dl>
<dd>Copyright (c) 2002-2007 Sam Trenholme </p>
<p> TERMS </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. </p>
<p> This software is provided aqas isaq with no guarantees of correctness or fitness for purpose.</dl>
<p> <code>4. How do I report bugs in MaraDNS?</code> </p>
<p> Please contact me; my email address is at <a rel="nofollow" href="http://www.maradns.org/contact.html.">http://www.maradns.org/contact.html.</a> Please be sure to include all information requested there, including the operating system you are using, the version of MaraDNS you are using, your mararc configuration file, and all relevant zone files. </p>
<p> <code>5. Some of the postings to the mailing list do not talk about MaraDNS!</code> </p>
<p> In cases where I post something to the mailing list which does not directly talk about MaraDNS, the subject line will not have [MARA] in it, but will have some form of the word CHATTER in it. </p>
<p> This way, people who do not like this can set up mail filters to filter out anything that comes from this list and doesnaqt have [MARA] in the subject line, or simply unsubscribe from the list and read the list from the archives; if one needs to report a bug, they can subscribe to the list again, post their bug, then unsubscribe after a week. </p>
<p> Another option is to set up oneaqs Freshmeat preferences to be notified in email every time I update MaraDNS at Freshmeat. This will give one email notice of any critical bug fixes without needing to be subscribed to the mailing list. </p>
<p> The web page <a rel="nofollow" href="http://www.maradns.org/">http://www.maradns.org/</a> has a link to the mailing list archives. </p>
<p> <code>6. How do I get off the mailing list?</code> </p>
<p> Send an email to list-request [at] maradns.org with &quot;unsubscribe&quot; as the subject line. </p>
<p> <code>7. How do I set up reverse DNS on MaraDNS?</code> </p>
<p> Reverse DNS (sometimes called &quot;reverse mapping&quot;) is set up by using PTR (pointer) records. For example, the PTR record which performs the reverse DNS lookup for the ip 10.2.3.4 looks like this in a CSV2 zone file: </p>
<dl>
<dd>4.3.2.10.in-addr.arpa. PTR <a rel="nofollow" href="http://www.example.com">www.example.com</a>. ~</dl>
<p> It is also possible, on MaraDNS 1.2.05 and more recent releases, to use a special &quot;FQDN4&quot; which automatically sets up the reverse mapping of a given record: </p>
<dl>
<dd><a rel="nofollow" href="http://www.example.com">www.example.com</a>. FQDN6 10.2.3.4 ~</dl>
<p> If you wish to have a PTR (reverse DNS lookup; getting a DNS name from a numeric IP) record work on the internet at large, it is not a simple matter of just adding a record like this to a MaraDNS zonefile. One also needs control of the appropriate in-addr.arpa. domain. </p>
<p> While it can make logical sense to contact the IP 10.11.12.13 when trying to get the reverse DNS lookup (fully qualified domain name) for a given IP, DNS servers donaqt do this. DNS server, instead, contact the root DNS servers for a given in-addr.arpa name to get the reverse DNS lookup, just like they do with any other record type. </p>
<p> When an internet service provider is given a block of IPs, they are also given control of the DNS zones which allow them to control reverse DNS lookups for those IPs. While it is possible to obtain a domain and run a DNS server without the knowledge or intervention of an ISP, being able to control reverse DNS lookups for those IPs requires ISP intervention. </p>
<p> <code>8. I am on a slow network, and MaraDNS can not process recursive queries</code> </p>
<p> MaraDNS, by default, only waits two seconds for a reply from a remote DNS server. This default can be increased by adding a line like this in the mararc file: </p>
<dl>
<dd>
<pre>timeout_seconds = 5 </pre>
</dl>
<p> Note that making this too high will slow MaraDNS down when DNS servers are down, which is, alas, all too common on todayaqs internet. </p>
<p> <code>9. When I try to run MaraDNS, I get a cryptic error message.</code> </p>
<p> There is usually some context of where there is a syntax error in a data file before the cryptic error message. For example, when there is a syntax error in a csv2 zone file, MaraDNS will tell you exactly at what point it had to terminate parsing of the zone file. </p>
<p> If MaraDNS does return a cryptic error message without letting you know what is wrong, let me know so that I can fix the bug. MaraDNS is designed to be easy to use; cryptic error messages go against this spirit. </p>
<p> <code>10. After I start MaraDNS, I can not see the process when I run netstat -na </code> </p>
<p> Udp services do not have a prominent &quot;LISTEN&quot; when netstat is run. </p>
<p> When MaraDNS is up, the relevant line in the netstat output looks like this: udp 0 0 127.0.0.1:53 0.0.0.0:* </p>
<p> While on the topic of netstat, if you run netstat -nap as root on Linux and some other *nix operating systems, you can see the names of the processes which are providing internet services. </p>
<p> <code>11. What string library does MaraDNS use?</code> </p>
<p> MaraDNS uses its own string library, which is called the &quot;js_string&quot; library. Man pages for most of the functions in the js_string library are in the folder doc/man of the MaraDNS distribution </p>
<p> <code>12. Why does MaraDNS use a multi-threaded model?</code> </p>
<p> The multi-threaded model is, plain and simple, the simplest way to write a functioning recursive DNS server. There is a reason why MaraDNS, pdnsd, and BIND 9 all use the multi-threaded model. </p>
<p> I am planning on improving MaraDNSaq threaded model to not spawn a thread for each and every uncached request. </p>
<p> <code>13. I feel that XXX feature should be added to MaraDNS</code> </p>
<p> The only thing that will convince me to implement a given feature for MaraDNS is cold, hard cash. If you want me to keep a given feature proprietary, you better have lots of cold hard cash. If youaqre willing to opensource your feature, less cash should be sufficient. </p>
<p> Keep in mind that both the BIND and NSD name servers were developed by having the programmers paid to work on the programs. PowerDNS was originally commercial software with the author only reluctantly made GPL after seeing that the market for a commercial DNS server is very small. All of the other DNS servers which have been developed as hobbyist projects (Posadis, Pdnsd, and djbdns) are no longer being actively worked on by the primary developer. </p>
<p> My current plans for MaraDNS are visible on the roadmap page for MaraDNS. </p>
<p> If I see a large MaraDNS community and a strong demand for new features from that community, I will consider their wishes. Especially if some of the members of the community have large bank accounts. Should ipv6 start to become dominant, I will update MaraDNS to have full ipv6 support. Should some other technology come along that will require an update to MaraDNS for MaraDNS to continue to function as a DNS server, I may very well update MaraDNS to use that technology. </p>
<p> <code>14. I feel that MaraDNS should use another documentation format</code> </p>
<p> The reason that MaraDNS uses its own documentation format is to satisfy both the needs of translators to have a unified document format and my own need to use a documentation format that is simple enough to be readily understood and which I can add features on an as needed basis. </p>
<p> The documentation format is essentially simplified HTML with some special tags added to meet MaraDNSaq special needs. </p>
<p> This gives me more flexibility to adapt the documentation format to changing needs. For example, when someone pointed out that itaqs not a good idea to have man pages with hi-bit characters, it was a simple matter to add a new HIBIT tag which allows man pages to be without hi-bit characters, and other document formats to retain hi-bit characters. </p>
<p> Having a given program have its own documentation format is not without precedent; Perl uses its own &quot;pod&quot; documentation format. </p>
<p> <code>15. Is there any process I need to follow to add a patch to MaraDNS?</code> </p>
<p> Yes. </p>
<p> Here is the procedure for making a proper patch: </p>
<dl>
<dt>*</p>
<dd>Enter the directory that the file is in, for example maradns-1.2.00/server</p>
<dt>*</p>
<dd>Copy over the file that you wish to modify to another file name. For example: cp MaraDNS.c MaraDNS.c.orig</p>
<dt>*</p>
<dd>Edit the file in question, e.g: vi MaraDNS.c</p>
<dt>*</p>
<dd>After editing, do something like this:<br />
 diff -u MaraDNS.c.orig MaraDNS.c &gt; maradns.patch</p>
<dt>*</p>
<dd>Make sure the modified version compiles cleanly</dl>
<p> Send a patch to me in email, along with a statement that you place the contents of the patch under MaraDNSaq BSD license. If I find that the patch works well, I will integrate it in to MaraDNS. </p>
<p> <code>16. Can MaraDNS act as a primary nameserver?</code> </p>
<p> Yes. </p>
<p> The zoneserver program serves zones so that other DNS servers can be secondaries for zones which MaraDNS serves. This is a separate program from the maradns server, which processes both authoritative and recursive UDP DNS queries. </p>
<p> See the DNS master document in the MaraDNS tutorial for details. </p>
<p> <code>17. Can MaraDNS act as a secondary nameserver?</code> </p>
<p> Yes. </p>
<p> Please read the DNS slave document, which is part of the MaraDNS tutorial. </p>
<p> <code>18. What is the difference between an authoritative and a recursive DNS server?</code> </p>
<p> A recursive DNS server is a DNS server that is able to contact other DNS servers in order to resolve a given domain name label. This is the kind of DNS server one points to in /etc/resolve.conf </p>
<p> An authoritative DNS server is a DNS server that a recursive server contacts in order to find out the answer to a given DNS query. </p>
<p> <code>19. The fetchzone client isnaqt allowing me to add certain hostnames to my zone</code> </p>
<p> For security reasons, MaraDNSaq fetchzone client does not add records which are not part of the zone in question. For example, if someone has a zone for example.com, and this record in the zone: </p>
<p> 1.1.1.10.in-addr.arpa. PTR dns.example.com. </p>
<p> MaraDNS will not add the record, since the record is out-of-bailiwick. In other words, it is a host name that does not end in .example.com. </p>
<p> There are two workarounds for this issue:</p>
<dl>
<dt>*</p>
<dd>Create a zone file for 1.1.10.in-addr.arpa., and put the PTR records there.</p>
<dt>*</p>
<dd>Use rcp, rsync, or another method to copy over the zone files in question.</dl>
<p> <code>20. Is MaraDNS portable?</code> </p>
<p> MaraDNS is developed on a CentOS 3 and Windows XP dual boot laptop. MaraDNS may compile or run on other systems&#8211;there are official MaraDNS ports for Debian/Ubuntu, Slackware, FreeBSD, and NetBSD. Note that MaraDNS needs a system with a robust threading library, which some systems do not have. </p>
<p> <code>21. Can I use MaraDNS in Windows?</code> </p>
<p> Yes. There is both a partial mingw32 (native win32 binary) port and a full Cygwin port of MaraDNS; both of these ports are part of the native build of MaraDNS. </p>
<p> <code>22. MaraDNS freezes up after being used for a while</code> </p>
<p> If you are using MaraDNS 1.2.03.1 (or any 1.1 release, for that matter) on Linux, upgrade to version 1.2.03.2. There is a bug with the Linux kernel which causes UDP clients to freeze unless code is written to work around the kernel bug. This workaround was first introduced in MaraDNS 1.0.28 and 1.1.35 and accidently disabled in 1.2.03.1. </p>
<p> If using your ISPaqs name servers or some other name servers which are not, in fact, root name servers, please make sure that you are using the upstream_servers dictionary variable instead of the root_servers dictionary variable. </p>
<p> If you still see MaraDNS freeze up after making this correction, please send a bug report to the mailing list. </p>
<p> <code>23. What kind of Python integration does MaraDNS have</code> </p>
<p> The mararc file uses the same syntax that Python uses; in fact, Python can parse a properly formatted mararc file. </p>
<p> There is currently no other integration with Python. </p>
<p> <code>24. Doesnaqt &quot;kvar&quot; mean &quot;four&quot; in Esperanto?</code> </p>
<p> Indeed, it does. However the use of &quot;kvar&quot; in the MaraDNS source code only coincidentally is an Esperanto word. &quot;kvar&quot; is short for &quot;Kiwi variable&quot;; a lot of the parsing code comes from the code used in the Kiwi spam filter project. </p>
<p> <code>25. How scalable is MaraDNS?</code> </p>
<p> MaraDNS is optimized for serving a small number of domains as quickly as possible. That said, MaraDNS is remarkably efficnent for serving a large number of domains, as long as the server MaraDNS is on has the memory to fit all of the domains, and as long as the startup time for loading a large number of domains can be worked around. </p>
<p> The &quot;big-O&quot; or &quot;theta&quot; growth rates for various MaraDNS functions are as follows, where N is the number of authoritative host names being served: </p>
<pre>Startup time N
Memory usage N
Processing incoming DNS requests 1</pre>
<p>As can be seen, MaraDNS will process 1 or 100000 domains in the same amount of time, once the domain names are loaded in to memory. </p>
<p> <code>26. I am having problems setting upstream_servers</code> </p>
<p> The upstream_servers mararc variable is set thusly: </p>
<dl>
<dd>upstream_servers[&quot;.&quot;] = &quot;10.3.28.79, 10.2.19.83&quot;</dl>
<p> Note the [&quot;.&quot;]. The reason for this is so future versions of MaraDNS may have more fine-grained control over the upstream_servers and root_servers values. </p>
<p> Note that the upstream_servers variable needs to be initialized before being used via upstream_servers = {} (the reason for this is so that a mararc file has 100% Python-compatible syntax). A complete mararc file that uses upstream_servers may look like this: </p>
<pre>ipv4_bind_addresses = &quot;127.0.0.1&quot;
chroot_dir = &quot;/etc/maradns&quot;
recursive_acl = &quot;127.0.0.1/8&quot;
upstream_servers = {}
upstream_servers[&quot;.&quot;] = &quot;10.1.2.3, 10.2.4.6&quot;</pre>
<p><code>27. Why doesnaqt the MaraDNS.org web page validate?</code> </p>
<p> HTML pages on the MaraDNS.org web site should validate as HTML 4.0 Transitional. However, the CSS will not validate. </p>
<p> I have designed MaraDNSaq web page to be usable and as attractive as possible in any major browser released in the last ten years. Cross-browser support is more important than strict W3 validation. The reason why the CSS does not validate is because I need a way to make sure there is always a scrollbar on the web page, even if the content is not big enough to merit one; this is to avoid the content jumping from page to page. There is no standard CSS tag that lets me do this. Iaqm using a non-standard tag to enable this in Gecko (Firefoxaqs rendering engine); this is enabled by default in Trident (Internet Exploreraqs rendering engine). The standards are deficient and blind adherence to them would result in an inferior web site. </p>
<p> There are also two validation warnings generated by redefinitions which are needed as part of the CSS filters used to make the site attractive on older browsers with limited CSS support. </p>
<p> On a related note, the reason why I use tables instead of CSS for some of the layout is because Microsoft Internet Explorer 6 and other browsers do not have support for the max-width CSS property. Without this property, the web page will not scale down correctly without using tables. Additionally, tables allow a reasonably attractive header in browsers without CSS support. </p>
<p> <code>28. How do MX records work?</code> </p>
<p> How MX records work:</p>
<dl>
<dt>*</p>
<dd>The mail transport agent (Sendmail, Postfix, Qmail, MS Exchange, etc.) looks up the MX record for the domain</p>
<dt>*</p>
<dd>For each of the records returned, the MTA (mail transport agent) looks up the IP for the names.</p>
<dt>*</p>
<dd>It will choose, at random, any of the MXes with the lowest priority number.</p>
<dt>*</p>
<dd>Should that server fail, it will try another server with the same priority number.</p>
<dt>*</p>
<dd>Should all MX records with a given priority number fail, the MTA will try sending email to any of the MX records with the second-lowest priority value.</dl>
<p> As an aside, do not have MX records point to CNAMEs. </p>
<p> <code>29. Does MaraDNS have support for SPF?</code> </p>
<p> SPF, or sender policy framework, is method of using DNS that makes it more difficult to forge email. MaraDNS has full support for SPF, both via TXT records and, starting with MaraDNS 1.2.08, via RFC4408 SPF records. </p>
<p> SPF configuration is beyond the scope of MaraDNSaq documentation. However, at the time of this FAQ entry being written (June, 2006), information and documentation concerning SPF is available at <a rel="nofollow" href="http://openspf.org.">http://openspf.org.</a> The BIND examples will work in MaraDNS csv2 zone files as long as the double quotes (&quot;) are replaced by single quotes (aq). For example, a SPF TXT record that looks like example.net. IN TXT &quot;v=spf1 +mx a:colo.example.com/28 -all&quot; in a BIND zone file will look like example.net. TXT aqv=spf1 +mx a:colo.example.com/28 -allaq in a MaraDNS zone file. MaraDNS version 1.2.08 and higher can also make the corresponding SPF record, which will have the syntax example.net. SPF aqv=spf1 +mx a:colo.example.com/28 -allaq. </p>
<p> <code>30. Iaqm having problems resolving CNAMES I have set up.</code> </p>
<p> This is probably because you have set up what MaraDNS calls a dangling CNAME record. </p>
<p> Let us suppose we have a CNAME record without an A record in the local DNS serveraqs database, such as: </p>
<pre> google.example.com. CNAME <a rel="nofollow" href="http://www.google.com">www.google.com</a>. ~</pre>
<p>This record, which is a CNAME record for &quot;google.example.com&quot;, points to &quot;<a rel="nofollow" href="http://www.google.com">www.google.com</a>&quot;. Some DNS servers will recursively look up <a rel="nofollow" href="http://www.google.com">www.google.com</a>, and render the above record like this: </p>
<pre> google.example.com. CNAME <a rel="nofollow" href="http://www.google.com">www.google.com</a>. ~
 <a rel="nofollow" href="http://www.google.com">www.google.com</a>. CNAME 66.102.7.104 ~</pre>
<p>For security reasons, MaraDNS doesnaqt do this. Instead, MaraDNS will simply output: </p>
<pre> google.example.com. CNAME <a rel="nofollow" href="http://www.google.com">www.google.com</a>. ~</pre>
<p>Some stub resolvers will be unable to resolve google.example.com as a consequence. </p>
<p> If you set up MaraDNS to resolve CNAMEs thusly, you will get a warning in your logs about having a dangling CNAME record. </p>
<p> If you want to remove these warnings, add the following to your mararc file: </p>
<pre> no_cname_warnings = 1</pre>
<p>Information about how to get MaraDNS to resolve dangling CNAME records is in the tutorial file dangling.html </p>
<p> <code>I have a NS delegation, and MaraDNS is doing strange things.</code> </p>
<p> In the case of there being a NS delegation, MaraDNS handles recursive queries and non-recursive DNS queries differently. Basically, unless you use askmara with the -n option, dig with the +norecuse option, or nslookup with the -norec option, MaraDNS will try to recursively resolve the record that is delegated. </p>
<p> The thinking is this: A normal recursive DNS query is usually one where one wants to know the final DNS output. So, if MaraDNS delegates a given record to another DNS server, and gets a recursive request for said query, MaraDNS will recursively resolve the query for you. </p>
<p> For example, let us suppose we have a mararc file that looks like this: </p>
<pre>chroot_dir = &quot;/etc/maradns&quot;
ipv4_bind_addresses = &quot;10.1.2.3&quot;
chroot_dir = &quot;/etc/maradns&quot;
recursive_acl = &quot;127.0.0.1/8, 10.0.0.0/8&quot;
csv2 = {}
csv2[&quot;example.com.&quot;] = &quot;db.example.com&quot;</pre>
<p>And a db.example.com file that looks like this: </p>
<pre><a rel="nofollow" href="http://www.example.com">www.example.com</a>. 10.1.2.3 ~
joe.example.com. NS ns.joe.example.com. ~
ns.joe.example.com. A 10.1.2.4 ~</pre>
<p>Next, you are trying to find out why <a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a> is not resolving. If you naively send a query to 10.1.2.3 for <a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a> as askmara A<a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a>. 10.1.2.3 or as dig @10.1.2.3 <a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a>. or as nslookup <a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a>. 10.1.2.3, you will <code>not</code> get any information that will help you solve the problem, since 10.1.2.3 will try to contact 10.1.2.4 to resolve <a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a>. </p>
<p> The solution is to run your DNS query client thusly:</p>
<dl>
<dt>*</p>
<dd>Askmara would be run thusly:</dl>
<p> askmara -n A<a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a>. 10.1.2.3 </p>
<dl>
<dt>*</p>
<dd>Dig would be run thusly:</dl>
<p> dig +norecurse @10.1.2.3 <a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a> </p>
<dl>
<dt>*</p>
<dd>Nslookup would be run thusly:</dl>
<p> nslookup -norec <a rel="nofollow" href="http://www.joe.example.com">www.joe.example.com</a> 10.1.2.3 </p>
<p> This will allow you to see that packets MaraDNS actually sends to a recursive DNS server. </p>
<p> As an aside, this particular problem will not happen if MaraDNS is run only as an authoritative nameserver. </p>
<p> <code>I am transferring a zone from another server, but the NS records are these strange &quot;synth-ip&quot; records. </code> </p>
<p> MaraDNS expects, in csv2 zone files, for all delegation NS records to be between the SOA record and the first non-NS record. </p>
<p> If a zone looks like this: </p>
<pre>example.net. +600 soa ns1.example.net. hostmaster [at] example.net 
10 10800 3600 604800 1080 ~
example.net. +600 mx 10 mail.example.net. ~
example.net. +600 a 10.2.3.5 ~
example.net. +600 ns ns1.example.net. ~
example.net. +600 ns ns3.example.net. ~
mail.example.net. +600 a 10.2.3.7 ~
<a rel="nofollow" href="http://www.example.net">www.example.net</a>. +600 a 10.2.3.11 ~</pre>
<p>Then the NS records will be &quot;synth-ip&quot; records. </p>
<p> The zone should look like this: </p>
<pre>example.net. +600 soa ns1.example.net. hostmaster [at] example.net 
10 10800 3600 604800 1080 ~
example.net. +600 ns ns1.example.net. ~
example.net. +600 ns ns3.example.net. ~
example.net. +600 mx 10 mail.example.net. ~
example.net. +600 a 10.2.3.5 ~
mail.example.net. +600 a 10.2.3.7 ~
<a rel="nofollow" href="http://www.example.net">www.example.net</a>. +600 a 10.2.3.11 ~</pre>
<p>This will remove the &quot;synth-ip&quot; records. </p>
<p> To automate this process, this awk script is useful: </p>
<pre>fetchzone whatever.zone.foo 10.1.2.3 | awk aq
{if($3 ~ /ns/ || $3 ~ /soa/){print}
else{a = a &quot;
&quot; $0}}
END{print a}aq &gt; zonefile.csv2</pre>
<p>Replace &quot;whatever.zone.foo&quot; with the name of the zone you are fetchin 10.1.2.3 with the IP address of the DNS master, and zonefile.csv2 with the name of the zone file MaraDNS loads. </p>
<p> <code>Where is the root.hints file?</code> </p>
<p> MaraDNS, unlike BIND, does not need a complicated root.hints file in order to have custom root servers. In order to change the root.hints file, add something like this to your mararc file: </p>
<pre>root_servers[&quot;.&quot;] = &quot;131.161.247.232,&quot;
root_servers[&quot;.&quot;] += &quot;208.185.249.250,&quot;
root_servers[&quot;.&quot;] += &quot;66.227.42.140,&quot;
root_servers[&quot;.&quot;] += &quot;66.227.42.149,&quot;
root_servers[&quot;.&quot;] += &quot;65.243.92.254&quot;</pre>
<p>Note that there is no &quot;+=&quot; in the first line, and the last line does not have a comma at the end. Read the recursive tutorial document for more information. </p>
<p> <code>Are there any plans to use autoconf to build MaraDNS?</code> </p>
<p> No. OK, let me qualify that: I wonaqt do it unless you pay me enough money. </p>
<p> In more detail, MaraDNS does not use autoconf for the following reasons:</p>
<dl>
<dt>*</p>
<dd>Autoconf is designed to solve a problem that existed in the mid 1990s but does not exist today: A large number of different incompatible C compilers and libc implementations. These days, most systems are using gcc as the compiler and some version of glibc as the libc. There is no longer a need, for example, to figure out whether a given implementation of getopt() allows aq&#8211;aq options. MaraDNSaqs ./configure script can be run in only a second or two; compare this to the 3-5 minute process autoconfaqs ./configure needs.</p>
<dt>*</p>
<dd>Autoconf leaves GPL-tained files in a programaqs build tree. MaraDNS is licensed under a BSD license that is <i>not</i> GPL-compatible, so MaraDNS can not be distributed with these GPL-licensed files.</dl>
<p> This leads us to the next question: </p>
<p> <code>How do I change the compiler or compile-time flags with MaraDNSaq build process?</code> </p>
<p> To change the compiler used by MaraDNS:</p>
<dl>
<dt>*</p>
<dd>Run the ./configure script</p>
<dt>*</p>
<dd>Open up the file Makefile with an editor</p>
<dt>*</p>
<dd>Look for a line that starts with CC</p>
<dt>*</p>
<dd>If there is no line that starts with CC, create one just before the line that starts with FLAGS</p>
<dt>*</p>
<dd>Change (or create) that line to look something like CC=gcc296 In this example, the 2.96 version of gcc is used to compile MaraDNS.</p>
<dt>*</p>
<dd>Note that it is important to <code>not</code> remove anything from this line you do not understand; doing so will make MaraDNS unable to compile or run. So, if the CC line looks like CC=gcc&amp;nbsp;$(LDFLAGS)&amp;nbsp;-DNO_FLOCK and you want to compile with gcc 2.96, change the line to look like CC=gcc296&amp;nbsp;$(LDFLAGS)&amp;nbsp;-DNO_FLOCK retaining the flags added by the configuration script.</dl>
<p> Changing compile-time flags is a similar process:</p>
<dl>
<dt>*</p>
<dd>Run the ./configure script</p>
<dt>*</p>
<dd>Open up the file Makefile with an editor</p>
<dt>*</p>
<dd>Look for a line that starts with FLAGS</p>
<dt>*</p>
<dd>Change (or create) that line to look something like FLAGS=-O3 In this example, MaraDNS is compiled with the -O3 option.</p>
<dt>*</p>
<dd>Note that it is important to <code>not</code> remove anything from this line you do not understand; doing so will make MaraDNS unable to compile or run. So, if the FLAGS line looks like FLAGS=-O2&amp;nbsp;-Wall&amp;nbsp;-DSELECT_PROBLEM and you want to compile at optimization level three, change this line to look like FLAGS=-O2&amp;nbsp;-Wall&amp;nbsp;-DSELECT_PROBLEM retaining the flags added by the configuration script. -DSELECT_PROBLEM for example, is needed in the Linux compile or MaraDNS will have problems with freezing up.</dl>
<p> <code>Will you make a package for the particular Linux distribution I am using?</code> </p>
<p> No. OK, let me qualify that: I wonaqt do it unless you pay me enough money. </p>
<p> There are MaraDNS packages for a number of different distributions of Linux and other operating systems. On the MaraDNS site, there is a MaraDNS package for CentOS/Red Hat Enterprise Linux available. There is also usually an up-to-date Slackware package available. In addition, there is a Debian package in the Debian packages collection, a FreeBSD port of MaraDNS, a Ubuntu package which is derived from the Debian package, and undoubtably other MaraDNS packages floating around the internet. </p>
<p> If you wish to have a package for your particular version of Linux (or MacOS X or BSD or&#8230;), you can use one of the above packages as a starting point for making your package. For example, other RPM-based distributions can use the CentOS RPM package as a baseline (the .spec file is in the build/ directory). I can not help you with any problems you may encounter making this package since I do not have your particular version of Linux installed on my computer. </p>
<p> As an aside, some of the MaraDNS packages floating around on the internet are out of date (*cough*, Debian, *cough*)&lt;sup&gt;&lt;font size=-2&gt;1&lt;/font&gt;&lt;/sup&gt;. Please make sure, that if you get a third-party package from the internet, the package is for either MaraDNS 1.0.41, MaraDNS 1.2.12.08, or MaraDNS 1.3.07.05. Older versions of MaraDNS are not supported. </p>
<p> Footnote 1: Debian has a somewhat silly policy that, once a package is declared &quot;stable&quot;, they will basically not update it unless there is a Bugtraq security advisory for the package in question. This policy is a good policy for programs made by pimply-faced 16-year-olds who donaqt know how to manage a release cycle nor a bugfix-only branch, but doesnaqt make sense for MaraDNS. As I write this, the Debianaqs &quot;stable&quot; version of MaraDNS is 1.2.12.04, which is about a year behind in terms of bugfixes. I, annoyingly enough, get bug reports from Debian users telling me about bugs I have already fixed in the 1.2 branch of MaraDNS. </p>
<p> Now, to be fair to Debian, their policies do allow me to backport bugfixes to the 1.2.12.04 release of MaraDNS, and the patches do get reviewed by somone else, which minimizes bugfixes introducing new bugs (Yes, I have done that), but there are not enough volunteers to review all of the bugfixes I have made since 1.2.12.04. So, Debian users get stuck with an old, buggy version of MaraDNS. The policy would work if there were enough volunteers to actually review all of my post-1.2.12.04 bugfixes, but the people who created the policy did not take in to account the logistics of volunteer work. </p>
<p> <code>I am using the native Windows port of MaraDNS, and some features are not working.</code> </p>
<p> Since Windows 32 does not have some features that *NIX OSes have, the native Windows port does not have all of the features of the *NIX version of MaraDNS. In particular, the following features are disabled:</p>
<dl>
<dt>*</p>
<dd>ipv6 (this is actually a mingw32, not a Windows deficiency)</p>
<dt>*</p>
<dd>The chroot_dir mararc variable</p>
<dt>*</p>
<dd>The maradns_gid and maradns_uid mararc variables</p>
<dt>*</p>
<dd>The maxprocs mararc variable</p>
<dt>*</p>
<dd>The synth_soa_serial variable can not have a value of 2</dl>
<p> If any of the above features are desired, try compiling MaraDNS using Cygwin. Note that the Cygwin port of MaraDNS does not have ipv6 support, and that while chroot_dir works in Cygwin, it does not have the security that the *NIX chroot() call has. </p>
<p> <code>MaraDNS isnaqt starting up</code> </p>
<p> This is usually caused by a syntax error in oneaqs mararc file, or by another MaraDNS process already running. To see what is happening, look at your system log (/var/log/messages in Centos 3) to see what errors MaraDNS reports. If you do not know how to look at a system log, you can also invoke MaraDNS from the command line as root; any errors will be visible when starting MaraDNS. </p>
<p> <code>You make a lot of releases of MaraDNS; at our ISP/IT department, updating software is non-trivial.</code> </p>
<p> The number of releases seen in the changelog is not an accurate reflection of how often someone using a stable branch of MaraDNS will need to update. </p>
<p> There were only three updates to the 1.0 legacy branch in 2006, and (so far) only two updates to the 1.0 branch in 2007. The 1.2 branch was updated frequently in the first half of 2006, since I felt MaraDNS 1.2 needed some features that didnaqt make it in to 1.2.00. During this update cycle, there was always a stable bugfix-only branch of MaraDNS. </p>
<p> In August of 2006, I stabilized the 1.2 branch and only five updates have been done since then. Unless there is a critical bug, I only will update the 1.2 branch approximately once every six months or so. </p>
<p> I go to a great deal of effort to make sure MaraDNS releases are as painless to update as possible. I ensure configuration file format compatibility, even between major versions of MaraDNS. With the exception of configuration file parser bugfixes, MaraDNS 1.0 configuration files are compatible with MaraDNS 1.2 and 1.3. </p>
<p> It is impossible to make code that is bug-free or without security problems. This is especially true with code that runs on the public internet.&lt;sup&gt;&lt;font size=-2&gt;1&lt;/font&gt;&lt;/sup&gt; Code has to be updated from time to time. What I do in order to minimize the disruption caused by an update is to always have a stable bugfix-only branch of MaraDNS (right now I have <i>three</i> bugfix-only branches), and to, as much as possible, evenly space out the bugfix updates. </p>
<p> Footnote 1: Even DJBaqs code has security problems. Both Qmail and DjbDNS have known security problems, and need to be patched before put on a public internet server.</p>
<h2>Bugs</h2>
<p>In the unusual case of having a csv2 zone file with Macintosh-style newlines (as opposed to DOS or UNIX newlines), while the file will parse, any errors in the file will be reported as being on line 1. </p>
<p> The maximum allowed number of threads is 5000. </p>
<p> The system startup script included with MaraDNS assumes that the only MaraDNS processes running are started by the script; it stops <i>all</i> MaraDNS processes running on the server when asked to stop MaraDNS. </p>
<p> When a resolver asks for an A record, and the A record is a CNAME which points to a list of IPs, MaraDNSaq recursive resolver only returns the first IP listed along with the CNAME. This is somewhat worked around by having a CNAME record only stay in the recursive cache for 15 minutes. </p>
<p> When a resolver asks for an A record, and the A record is a CNAME that points to another CNAME (and possibly a longer CNAME chain), while MaraDNS returns the correct IP (as long as the glueless level is not exceeded), MaraDNS will incorrectly state that the first CNAME in the chain directly points to the IP. </p>
<p> If a NS record points to a list of IPs, and the NS record in question is a &quot;glueless&quot; record (MaraDNS had to go back to the root servers to find out the IP of the machine in question), MaraDNSaq recursive resolver only uses the first listed IP as a name server. </p>
<p> When MaraDNSaq recursive resolver receives a &quot;host not there&quot; reply, instead of using the SOA minimum of the &quot;host not there&quot; reply as the TTL (Look at RFC1034 section 4.3.4), MaraDNS uses the TTL of the SOA reply. </p>
<p> MaraDNS keeps referral NS records in the cache for one day instead of the TTL specified by the remote server. </p>
<p> MaraDNS needs to use the <code>zoneserver</code> program to serve DNS records over TCP. See <code><a href="/docs/linux/man/8-zoneserver/">zoneserver</a>(8)</code> for usage information. </p>
<p> MaraDNS does not use the zone file (&quot;master file&quot;) format specified in chapter 5 of RFC1035. </p>
<p> MaraDNS default behavior with star records is not RFC-compliant. In more detail, if a wildcard MX record exists in the form &quot;*.example.com&quot;, and there is an A record for &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;, but no MX record for &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;, the correct behavior (based on RFC1034 section 4.3.3) is to return &quot;no host&quot; (nothing in the answer section, SOA in the authority section, 0 result code) for a MX request to &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;. Instead, MaraDNS returns the MX record attached to &quot;*.example.com&quot;. This can be changed by setting bind_star_handling to 1. </p>
<p> Star records (what RFC1034 calls &quot;wildcards&quot;) can not be attached to NS records. </p>
<p> MaraDNS recursive resolver treats any TTL shorter than min_ttl seconds (min_ttl_cname seconds when the record is a CNAME record) as if the TTL in question was min_ttl (or min_ttl_cname) seconds long when determining when to expire a record from MaraDNSaq cache. </p>
<p> TTLs which are shorter than 20 seconds long are given a TTL of 20 seconds; TTLs which are more than 63072000 (2 years) long are given a TTL of 2 years. </p>
<p> MaraDNSaq recursive resolveraqs method of deleting not recently accessed records from the cache when the cache starts to fill up can deleted records from the cache before they expire. Some people consider this undesirable behavior; I feel it is necessary behavior if one wishes to place a limit on the memory resources a DNS server may use. </p>
<p> MaraDNSaq recursive resolver stops resolving when it finds an answer in the AR section. This is a problem in the case where a given host name and IP is registered with the root name servers, and the registered IP is out of date. When this happens, a server &quot;closer&quot; to the root server will give an out-of-date IP, even though the authoritative DNS servers for the host in question have the correct IP. Note that resolving this will result in increased DNS traffic. </p>
<p> MaraDNS, like every other known DNS implementation, only supports a QDCOUNT of 0 or 1. </p>
<p> MaraDNS spawns a new thread for every single recursive DNS request when the data in question is not in MaraDNSaq cache; this makes MaraDNS an excellent stress tester for pthread implementations. Many pthread implementations can not handle this kind of load; symptoms include high memory usage and termination of the MaraDNS process. </p>
<p> MaraDNS does not handle the case of a glueless in-bailiwick NS referral very gracefully; this usually causes the zone pointed to by the offending NS record to be unreachable by MaraDNS, even if other DNS servers for the domain have correct NS referrals.</p>
<h2>Unimplemented Features</h2>
<p><i>These are features which will not be implemented in the 1.2 release of MaraDNS:</i> </p>
<p> MaraDNS does not have a disk-based caching scheme for authoritative zones. </p>
<p> MaraDNSaq UDP server only loads zone files while MaraDNS is first started. UDP Zone information can only be updated by stopping MaraDNS, and restarting MaraDNS again. Note that TCP zone files are loaded from the filesystem at the time the client requests a zone. </p>
<p> MaraDNS does not have support for allowing given host names to only resolve for a limited range of IPs querying the DNS server, or for host names to resolve differently, depending on the IP querying the host name. </p>
<p> MaraDNS only has limited authoritative-only support for IPv6. </p>
<p> MaraDNS only allows wildcards at the beginning or end of a host name. E.g. names with wildcards like &quot;foo.*.example.com&quot;. &quot;www.*&quot; will work, however, if a default zonefile is set up. </p>
<p> MaraDNS does not have support for MRTG or any other SNMP-based logging mechanism.</p>
<h2>Legal Disclaimer</h2>
<p>THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>Authors</h2>
<p>Sam Trenholme (<a rel="nofollow" href="http://www.samiam.org)">http://www.samiam.org)</a> is responsible for this man page. </p>
<p> MaraDNS is written by me, Sam Trenholme, with a little help from my friends. Naturally, all errors in MaraDNS are my own (but read the disclaimer above). </p>
<p> Here is a partial list of people who have provided assistance: </p>
<p> Floh has generously set up a FreeBSD 4, FreeBSD 6, and Mac OS X system so that I can port MaraDNS to more platforms. </p>
<p> Albert Lee has provided countless bug reports, and, nicely enough, patches to fix said bugs. He has also made improvements to the code in the tcp &quot;zoneserver&quot;. </p>
<p> Franky Van Liedekerke has provided much invaluable assistance. As just one example, he provided invaluable assistance in getting MaraDNS to compile on Solaris. In addition, he has provided much valuable SQA help. </p>
<p> Christian Kurz, who has provided invaluable bug reports, especially when I had to re-implement the core hashing algorithm. </p>
<p> Remmy, who is providing both the web space and a mailing list for maradns.org. </p>
<p> Phil Homewood, who provided invaluable assistance with finding and fixing bugs in the authoritative portion of the MaraDNS server. He helped me plug memory leaks, find uninitialized variables being used, and found a number of bugs I was unable to find. </p>
<p> Albert Prats kindly provided Spanish translations for various text files. </p>
<p> Shin Zukeran provided a patch to recursive.c which properly makes a normal null-terminated string from a js_string object, to send as an argument to open() so we can get the rijndael key for the PRNG. </p>
<p> D Richard Felker III has provided invaluable bug reports. By looking at his bug reports, I have been able to hunt down and fix many problems that the recursive nameserver had, in addition to at least one problem with the authoritative nameserver. </p>
<p> Ole Tange has also given me many valuable MaraDNS bug reports. </p>
<p> Florin Iucha provided a tip in the FAQ for how to compile MaraDNS on OpenBSD. </p>
<p> Roy Arends (one of the BIND developers, as it turns out) found a serious security problem with MaraDNS, where MaraDNS would answer answers, and pointed it out to me. </p>
<p> Code used as the basis for the psudo-random-number generator was written by Vincent Rijmen, Antoon Bosselaers, and Paulo Barreto. I appreciate these programmers making the code public domain, which is the only license under which I can add code to MaraDNS under. </p>
<p> Ross Johnson and others have made a Win32 port of the Pthreads library; this has made a native win32 port of MaraDNS possible. </p>
<p> I also appreciate the work of Dr. Brian Gladman and Fritz Schneider, who have both written independent implementations of AES from which I obtained test vectors. With the help of their hard work, I was able to discover a subtle security problem that previous releases of MaraDNS had.</p>
