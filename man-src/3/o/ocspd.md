---
title: "ocspd(3)"
name: "ocspd"
section: "3"
letter: "o"
url: "/docs/linux/man/3-ocspd/"
---

<pre>
        ocspd.conf - OCSP Daemon configuration file
</pre>
<h2>Description</h2>
<p> A configuration file is divided into a number of sections. Each section starts with a line <code>[ section_name ]</code> and ends when a new section is started or end of file is reached. A section name can consist of alphanumeric characters and underscores. </p>
<p> The first section of a configuration file is special and is referred to as the <code>default</code> section this is usually unnamed and is from the start of file until the first named section. When a name is being looked up it is first looked up in a named section (if any) and then the default section. </p>
<p> The environment is mapped onto a section called <font SIZE="-1"><code>ENV</code></font>. </p>
<p> Comments can be included by preceding them with the <code>#</code> character </p>
<p> Each section in a configuration file consists of a number of name and value pairs of the form <code>name=value</code> </p>
<p> The <code>name</code> string can contain any alphanumeric characters as well as a few punctuation symbols such as <code>.</code> <code>,</code> <code>;</code> and <code>_</code>. </p>
<p> The <code>value</code> string consists of the string following the <code>=</code> character until end of line with any leading and trailing white space removed. </p>
<p> The value string undergoes variable expansion. This can be done by including the form $var or <code>${var}</code>: this will substitute the value of the named variable in the current section. It is also possible to substitute a value from another section using the syntax $section::name or <code>${section::name}</code>. By using the form $ENV::name environment variables can be substituted. It is also possible to assign values to environment variables by using the name <code>ENV::name</code>, this will work if the program looks up environment variables using the <font SIZE="-1"><code>CONF</code></font> library instead of calling getenv() directly. </p>
<p> It is possible to escape certain characters by using any kind of quote or the <code>\</code> character. By making the last character of a line a <code>\</code> a <code>value</code> string can be spread across multiple lines. In addition the sequences <code>
</code>, <code></code>, <code></code> and <code>	</code> are recognized.</p>
<h2>Notes</h2>
<p> If a configuration file attempts to expand a variable that doesn&#8217;t exist then an error is flagged and the file will not load. This can happen if an attempt is made to expand an environment variable that doesn&#8217;t exist. For example the default OpenSSL master configuration file used the value of <font SIZE="-1"><code>HOME</code></font> which may not be defined on non Unix systems.</p>
<h2>Example</h2>
<p> Following is a sample configuration file: </p>
<pre>
 # OCSPd example configuration file.
 # (c) 2001 by Massimiliano Pala - OpenCA Project.
 # All rights reserved
 [ ocspd ]
 default_ocspd   = OCSPD_default
 
 
 [ OCSPD_default ]
 dir              = /etc/ocspd
 md               = sha1
 
 ocspd_certificate = $dir/certs/ocspd_cert.pem
 ocspd_key         = $dir/private/ocspd_key.pem
 pidfile           = $dir/ocspd.pid
 
 user                    = ocspd
 group                   = daemon
 bind                    = *
 port                    = 2560
 max_childs_num          = 5
 max_req_size            = 8192
 
 request          = ocsp_req
 response         = ocsp_response
 
 dbms                    = dbms_ldap     # Example using the LDAP for CRL
                                         # retrivial
 #dbms                   = dbms_file     # Example using file for CRL
 engine = HSM                            # ENGINE section
 
 ####################################################################
 [ ocsp_req ]
 default_keyfile         = key.pem
 
 ####################################################################
 [ ocsp_response ]
 dir                     = /etc/ocspd
 ocsp_add_response_certs = $dir/certs/chain_certs.pem
 ocsp_add_response_keyid = yes
 next_update_days        = 0
 next_update_mins        = 5
 ####################################################################
 [ dbms_ldap ]
 # It is possible to use an URI to identify a CRL and/or the
 # CA certificate, the general format is:
 #
 #      [protocol]://[user[:pwd]@]server[:port]/[path]
 #
 # where:
 #   protocol - specifies the protocol to be used, supported are
 #              file, ldap, http
 #   user     - is the user for auth (meaningful only if ldap or
 #              http is used)
 #   pwd      - password used for auth (meaningful only if ldap
 #              or http is used)
 #   port     - port to connect to (meaningful only if ldap or
 #              http is used)
 #   path     - complete path to the object (meaningful only if
 #              http is used)
 #
 # You can have the CRLs/CA certificates on a simple file
 #    crl_url = file:///etc/ocspd/crl.pem
 #
 # You can retrieve the CRLs/CA certificates from a web server
 #    crl_urt = <a rel="nofollow" href="http://server/ca/cacert.der">http://server/ca/cacert.der</a>
 #
 # You can store the CRL into an LDAP server, simply
 # store it in certificateRevocationList;binary attribute
 #
 # There are different way, all legal, to specify the CRL
 # URL address:
 # crl_url = <a href="ldap://user:pwd@ldap.server.org:389">ldap://user:pwd@ldap.server.org:389</a>
 # crl_url = <a href="ldap://ldap.server.org:389">ldap://ldap.server.org:389</a>
 crl_url = <a href="ldap://localhost">ldap://localhost</a>
 # The CRL entry DN is the DN to look for when retrieving the
 # date from the LDAP server. Put here the complete DN (usually
 # the DN of the CA's certificate).
 crl_entry_dn = &quot;email=email [at] address, cn=Certification Auth, \
                                             o=Organization, c=IT&quot;
 ####################################################################
 [ dbms_file ]
 # You can have the CRL on a simple file in PEM format
 crl_url = file:///etc/ocspd/crl.pem
 [ HSM ]
 # Hardware accelerators support via the ENGINE interface
 engine_id = MyAccelerator
 0.engine_pre = login:1:10:11:myPassword
 # 0.engine_post = logout:1:10:11
</pre>
<p> Let&#8217;s analyze the options in detail.</p>
<dl COMPACT>
<dt><code>default_ocspd section</code></p>
<dd> In this section of the configuration file are set the general options used by the responder, some of which are available using the command line options too ( see <i><a href="/docs/linux/man/3-ocspd/">ocspd</a></i>(3)).</p>
<dl COMPACT>
<dt>
<dd>
<dl COMPACT>
<dt><code>dir</code></p>
<dd> specifies the directory where everything is kept.</p>
<dt><code>md</code></p>
<dd> specifies the digest to be used. Default is sha1.</p>
<dt><code>ocspd_certificate</code></p>
<dd> path to the certificate to be used by the responder.</p>
<dt><code>ocspd_key</code></p>
<dd> path to the private key file to be used by the responder.</p>
<dt><code>pidfile</code></p>
<dd> path to the pid file where the responder will write its pid when starting.</p>
<dt><code>user</code></p>
<dd> user id the responder will try to run as, this must be a valid <font SIZE="-1">UID</font>. If not specified the responder will run as the user who started the daemon.</p>
<dt><code>group</code></p>
<dd> group id the responder will try to run as, this must be a valid <font SIZE="-1">GID</font>. If not specified the responder will run as the user who started the daemon.</p>
<dt><code>bind</code></p>
<dd> address to listen to. You can force the responder to listen to just one of the available addresses. If you want the responder to listen to every available interface, simply use &#8216;*&#8217; (default).</p>
<dt><code>port</code></p>
<dd> specifies the port to listen to.</p>
<dt><code>threads_num</code></p>
<dd> Number of threads that shall be created at startup time, the more threads, the better for handling very high traffic. We expect to have better performances on multi-threaded machines and processors. </p>
<p> From version 1.5+ the server is not pre-forked, instead it is a pre-threaded one. In order to run the server needs support for <font SIZE="-1">POSIX1</font>.c as found in most modern UNiX systems.</p>
<dt><code>max_client_num</code></p>
<dd> Size of the system socket queue: when all service threads are busy, up to this number of unserved requests are accepted in queue and will be processed as soon as a thread becomes available; additional connection requests will be denied. Default: 30.</p>
<dt><code>chroot_dir</code></p>
<dd> Chroot the application into the specified directory, watch out because if you chroot the application, all the paths should be relative to the new root for <font SIZE="-1">CRL</font> reloading or (better solution) you have to download the CRLs from <font SIZE="-1">HTTP</font> or <font SIZE="-1">LDAP</font>. If you chroot and you do not provide support for privileges dropping, privileges will not be dropped and an error will be written in the logfile, but the server will continue to run assuming the <i>chroot()</i> is sufficiently isolated to prevent abuse of the machine.</p>
<dt><code>max_req_size</code></p>
<dd> maximum size of received request, if a received request is bigger it will be trashed. Usually simple requests are 200/300 bytes long (more or less).</dl>
</dl>
<dl COMPACT>
<dt>
<dd></dl>
<dt><code>request section</code></p>
<dd> Currently not used</p>
<dt><code>response section</code></p>
<dd> Here are kept options tied to responses&#8217; building.</p>
<dt><code>dbms section</code></p>
<dd> Here are kept options tied to the revoked certificates&#8217; list.</p>
<dl COMPACT>
<dt>
<dd>
<dl COMPACT>
<dt><code>ocsp_add_response_certs</code></p>
<dd> specifies path to a file containing certificates to be added to the response (usually the whole certification chain). Certificates have to be in <font SIZE="-1">PEM</font> format one after another (a simple cat of the certificates will do fine).</p>
<dt><code>ocsp_add_response_keyid</code></p>
<dd> specifies if adding of the key id to the response.</p>
<dt><code>next_update_days</code></p>
<dd> specifies the number of days till next update is available. A response will be valid in the period following the request till the days+mins.</p>
<dt><code>next_update_mins</code></p>
<dd> specifies the number of minutes till next update is available. A response will be valid in the period following the request till the days+mins.</p>
<dt><code>ca_url</code></p>
<dd> specifies the <font SIZE="-1">URI</font> where the <font SIZE="-1">CA</font> certificate (which identifies the single <font SIZE="-1">CA</font>) is located. Three different protocols are implemented ( file:// http:// or ldap:// ). If file is chosen, then the parameter should carry the path to the <font SIZE="-1">CA</font> file (i.e. file:///etc/ocspd/certs/ca.pem). If ldap or http is chosen, you can specify the address, and the port of the server where to connect to (i.e. <a href="ldap://server.addr:port">ldap://server.addr:port</a>).</p>
<dt><code>crl_url</code></p>
<dd> specifies the <font SIZE="-1">URI</font> where the <font SIZE="-1">CRL</font> (list of revoked certificates, actually used for building responses) is located. Three different protocols are actually implemented ( file:// http:// or ldap:// ). If file is chosen, then the parameter should have the path to the crl file (i.e. file:///etc/ocspd/crls/cacrl.pem). If ldap or http is chosen, you can specify the address, and the port of the server where to connect to (i.e. <a href="ldap://server.addr:port">ldap://server.addr:port</a>).</p>
<dt><code>crl_entry_dn</code></p>
<dd> specifies, if ldap:// protocol is chosen within the <code>crl_url</code> parameter, the entry where to look for the certificateRevocationList attribute where the <font SIZE="-1">CRL</font> should be present (usually this is also the base of the <font SIZE="-1">LDAP</font> tree, but different installations are also possible).</dl>
</dl>
<dl COMPACT>
<dt>
<dd></dl>
<dt><font SIZE="-1"><code>ENGINE</code></font><code> section</code></p>
<dd>
<dl COMPACT>
<dt>
<dd>
<dl COMPACT>
<dt><code>engine_id</code></p>
<dd> Specifies the <font SIZE="-1">ENGINE</font> id to be used &#8211; check OpenSSL and your <font SIZE="-1">HSM</font> vendor to get more info about this parameter.</p>
<dt><code>engine_pre</code></p>
<dd> Some <font SIZE="-1">HSM</font> need initialisation before access to the crypto accelerated functions is granted. It is possible, by using the &#8216;engine_pre&#8217; options to issue needed commands directly to the <font SIZE="-1">HSM</font>. </p>
<p> The format is as follows:<br />
0.engine_pre&nbsp;<wbr>=&nbsp;<wbr>cmd:values<br />
1.engine_pre&nbsp;<wbr>=&nbsp;<wbr>cmd2:values<br />
&#8230; It is possible to have as many commands as needed.</p>
<dt><code>engine_post</code></p>
<dd> Some HSMs need to perform commands after the <font SIZE="-1">ENGINE</font> initialisation which are taken from the &#8216;engine_post&#8217; option. Usage and format is exactly the same as &#8216;engine_pre&#8217;, the difference is that commands are sent to the <font SIZE="-1">HSM</font> after the <i>ENGINE_init()</i> function. Refer to your <font SIZE="-1">HSM</font> documentation for more informations</dl>
</dl>
<dl COMPACT>
<dt>
<dd></dl>
</dl>
<h2>Author</h2>
<p> Massimiliano Pala &lt;madwolf [at] openca.org&gt;</p>
<h2>See Also</h2>
<p> <i><a href="/docs/linux/man/3-ocspd/">ocspd</a></i>(3),<i><a href="/docs/linux/man/3-openca/">openca</a></i>(3),<i><a href="/docs/linux/man/1-openssl/">openssl</a></i>(1), <i><a href="/docs/linux/man/1-ocsp/">ocsp</a></i>(1)</p>
<h2>Pod Errors</h2>
<p> Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl COMPACT>
<dt>Around line 162:</p>
<dd> &#8216;=item&#8217; outside of any &#8216;=over&#8217;</p>
<dt>Around line 348:</p>
<dd> You forgot a &#8216;=back&#8217; before &#8216;=head1&#8217; </p>
</dl>
