---
title: "strongswan_scepclient(8)"
name: "strongswan_scepclient"
section: "8"
letter: "s"
url: "/docs/linux/man/8-strongswan_scepclient/"
description: "ipsec scepclient – Client for the SCEP protocol"
---

<p>ipsec scepclient &#8211; Client for the SCEP protocol</p>
<h2>Synopsis</h2>
<p><code>ipsec scepclient [argument &#8230;]</code> </p>
<p> <code>ipsec scepclient</code> <code>&#8211;help</code><br />
 <code>ipsec scepclient</code> <code>&#8211;version</code></p>
<h2>Description</h2>
<p><code>scepclient</code> is a client implementation of Cisco System&#8217;s Simple Certificate Enrollment Protocol (SCEP) written for Linux strongSwan &lt;<a rel="nofollow" href="http://www.strongswan.org">http://www.strongswan.org</a>&gt;. <code>scepclient</code> is designed to be used for certificate enrollment on machines using the OpenSource IPsec solution <i>strongSwan.</i></p>
<h2>Features</h2>
<p><code>scepclient</code> implements the following features of SCEP: </p>
<dl>
<dt>&#8211;</dt>
<dd>Automatic enrollment of client certificate using a preshared secret</dd>
<dt>&#8211;</dt>
<dd>Manual enrollment of client certificate. Offline fingerprint check required!</dd>
<dt>&#8211;</dt>
<dd>Acquisition of CA certificate(s)</dd></dl>
<h2>Options</h2>
<h3>Basic Startup Options</h3>
<p><code>-v, &#8211;version</code></p>
<dl>
<dd>Display the version of ipsec scepclient. </dd>
</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dd>Display usage of ipsec scepclient.</dd></dl>
<h3>General Options</h3>
<p><code>-u, &#8211;url </code><i>url</i></p>
<dl>
<dd>Full HTTP URL of the SCEP server to be used for certificate enrollment and CA certificate acquisition.</dd></dl>
<p> <code>-+, &#8211;optionsfrom </code><i>filename</i></p>
<dl>
<dd>Reads additional options from <i>filename</i>.</dd></dl>
<p> <code>-f, &#8211;force</code></p>
<dl>
<dd>Overwrite existing output file[s].</dd></dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dd>Do not write log output to stderr.</dd></dl>
<h3>Options for CA Certificate Acquisition</h3>
<p><code>-o, &#8211;out cacert[=</code><i>filename</i>]</p>
<dl>
<dd>Output file of acquired CA certificate. If more then one CA certificate is available, <i>filename</i> is used as prefix for the resulting files (refer to EXAMPLES below for details).<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/cacerts/caCert.der.</dd></dl>
<h3>Options For Certificate Enrollment</h3>
<p><code>-i, &#8211;in </code><i>type</i>[=<i>filename</i>]</p>
<dl>
<dd>Input file for certificate enrollment. This option can be specified multiple times to specify input files for every <i>type</i>. Input files can be either DER or PEM encoded. </dd>
<p> Supported values for <i>type</i>:</p>
<dl>
<dt><code>pkcs1</code></dt>
<dd>RSA private key in PKCS#1 file format. If no input of this type is specified, a RSA key gets generated.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/private/myKey.der.</dd>
<dt><code>pkcs10</code></dt>
<dd>PKCS#10 certificate request to be used in the SCEP request. If no input of this type is specified, a request is generated.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/req/myReq.der.</dd>
<dt><code>cacert-enc</code></dt>
<dd>CA certificate to encrypt the SCEP request. Has to be specified for certificate enrollment.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/cacerts/caCert.der.</dd>
<dt><code>cacert-sig</code></dt>
<dd>CA certificate to check signature of SCEP reply. Has to be specified for certificate enrollment.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/cacerts/caCert.der.</dd>
<dt><code>cert-self</code></dt>
<dd>Certificate to be used in the SCEP request. If it is not specified a self-signed certificate is generated automatically.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/certs/selfCert.der.</dd></dl>
</dl>
<p> <code>-k, &#8211;keylength </code><i>bits</i></p>
<dl>
<dd>sets the key length for RSA key generation. The default length for a generated rsa key is set to 2048 bit.</dd></dl>
<p> <code>-D, &#8211;days </code><i>days</i></p>
<dl>
<dd>Validity of the self-signed X.509 certificate in days. The default is 1825 days (5 years).</dd></dl>
<p> <code>-S, &#8211;startdate </code><i>YYMMDDHHMMSS</i>Z</p>
<dl>
<dd>defines the <code>notBefore</code> date when the X.509 certificate becomes valid. The date has the format <i>YYMMDDHHMMSS</i> and must be specified in UTC (Zulu time). If the <code>&#8211;startdate</code> option is not specified then the current date is taken as a default.</dd></dl>
<p> <code>-E, &#8211;enddate </code><i>YYMMDDHHMMSS</i>Z</p>
<dl>
<dd>defines the <code>notAfter</code> date when the X.509 certificate will expire. The date has the format <i>YYMMDDHHMMSS</i> and must be specified in UTC (Zulu time). If the <code>&#8211;enddate</code> option is not specified then the default <code>notAfter</code> value is computed by adding the validity interval specified by the <code>&#8211;days</code> option to the <code>notBefore</code> date.</dd></dl>
<p> <code>-d, &#8211;dn </code><i>dn</i></p>
<dl>
<dd>Distinguished name as comma separated list of relative distinguished names. Use quotation marks for a distinguished name containing spaces. If the <code>&#8211;dn</code> parameter is missing then the default &quot;C=CH, O=Linux strongSwan, CN=<i>hostname</i>&quot; is used with <i>hostname</i> being the return value of the <i>gethostname</i>() function.</dd></dl>
<p> <code>-s, &#8211;subjectAltName </code><i>type</i>=<i>value</i></p>
<dl>
<dd>Include subjectAltName in certificate request. This option can be specified multiple times to specify a subjectAltName for every <i>type</i>. </dd>
<p> Supported values for <i>type</i>:</p>
<dl>
<dt><code>email</code></dt>
<dd>subjectAltName is a email address.</dd>
<dt><code>dns</code></dt>
<dd>subjectAltName is a hostname.</dd>
<dt><code>ip</code></dt>
<dd>subjectAltName is a IP address.</dd></dl>
</dl>
<p> <code>-p, &#8211;password </code><i>pw</i></p>
<dl>
<dd>Password to be included as a <i>challenge password</i> in SCEP request. If <i>pw</i> is <code>%prompt</code>&#8216;, the password gets prompted for on the command line.</dd>
<dl>
<dd>&#8211; In automatic mode, this password corresponds to the preshared secret for the given enrollment.</dd>
<dd>&#8211; In manual mode, this password can be used to later revoke the corresponding certificate.</dd></dl>
</dl>
<p> <code>-a, &#8211;algorithm [</code><i>type</i>=]<i>algo</i></p>
<dl>
<dd>Change the algorithms to be used when generating and transporting (PKCS#7) certificate requests (PKCS#10). </dd>
<p> Supported values for <i>type</i>:</p>
<dl>
<dt><code>enc</code></dt>
<dd>symmetric encryption algorithm in PKCS#7</dd>
<dt><code>dgst</code></dt>
<dd>hash algorithm for message digest in PKCS#7</dd>
<dt><code>sig</code></dt>
<dd>hash algorithm for the signature in PKCS#10</dd></dl>
<p> If <i>type</i> is not specified <code>enc</code> is assumed. </p>
<p> Supported values for <i>algo</i> (<code>enc</code>):</p>
<dl>
<dt><code>des</code></dt>
<dd>DES-CBC encryption (key size = 56 bit). Default.</dd>
<dt><code>3des</code></dt>
<dd>Triple DES-EDE-CBC encryption (key size = 168 bit).</dd>
<dt><code>aes128</code></dt>
<dd>AES-CBC encryption (key size = 128 bit).</dd>
<dt><code>aes192</code></dt>
<dd>AES-CBC encryption (key size = 192 bit).</dd>
<dt><code>aes256</code></dt>
<dd>AES-CBC encryption (key size = 256 bit).</dd>
<dt><code>camellia128</code></dt>
<dd>Camellia-CBC encryption (key size = 128 bit).</dd>
<dt><code>camellia192</code></dt>
<dd>Camelllia-CBC encryption (key size = 192 bit).</dd>
<dt><code>camellia256</code></dt>
<dd>Camellia-CBC encryption (key size = 256 bit).</dd></dl>
<p> Supported values for <i>algo</i> (<code>dgst</code> or <code>sig</code>): </p>
<p> <code>md5</code> (default), <code>sha1</code>, <code>sha256</code>, <code>sha384</code>, <code>sha512</code></dl>
<p> <code>-o, &#8211;out </code><i>type</i>[=<i>filename</i>]</p>
<dl>
<dd>Output file for certificate enrollment. This option can be specified multiple times to specify output files for every <i>type</i>. </dd>
<p> Supported values for <i>type</i>:</p>
<dl>
<dt><code>pkcs1</code></dt>
<dd>RSA private key in PKCS#1 file format. If specified, the RSA key used for enrollment is stored in file <i>filename</i>. If none of the <i>types</i> listed below are specified, <code>scepclient</code> will stop after outputting this file.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/private/myKey.der.</dd>
<dt><code>pkcs10</code></dt>
<dd>PKCS#10 certificate request. If specified, the PKCS#10 request used or certificate enrollment is stored in file <i>filename</i>. If none of the <i>types</i> listed below are specified, <code>scepclient</code> will stop after outputting this file.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/req/myReq.der.</dd>
<dt><code>pkcs7</code></dt>
<dd>PKCS#7 SCEP request as it is sent using HTTP to the SCEP server. If specified, this SCEP request is stored in file <i>filename</i>. If none of <i>types</i> listed below is not specified, <code>scepclient</code> will stop after outputting this file.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/req/pkcs7.der.</dd>
<dt><code>cert-self</code></dt>
<dd>Self-signed certificate. If specified the self-signed certificate is stored in file <i>filename</i>.<br />
 The default <i>filename</i> is $CONFDIR/ipsec.d/certs/selfCert.der.</dd>
<dt><code>cert</code></dt>
<dd>Enrolled certificate. This <i>type</i> must be specified for certificate enrollment. The enrolled certificate is stored in file <i>filename</i>.<br />
 The default <i>filename</i> is set to $CONFDIR/ipsec.d/certs/myCert.der.</dd></dl>
</dl>
<p> <code>-m, &#8211;method </code><i>method</i></p>
<dl>
<dd>Change HTTP request method for certificate enrollment. Default is <code>get</code>. </dd>
<p> Supported values for <i>method</i>:</p>
<dl>
<dt><code>post</code></dt>
<dd>Certificate enrollment using HTTP POST. Must be supported by the given SCEP server.</dd>
<dt><code>get</code></dt>
<dd>Certificate enrollment using HTTP GET.</dd></dl>
</dl>
<p> <code>-t, &#8211;interval </code><i>seconds</i></p>
<dl>
<dd>Set interval time in seconds when polling in manual mode. The default interval is set to 5 seconds.</dd></dl>
<p> <code>-x, &#8211;maxpolltime </code><i>seconds</i></p>
<dl>
<dd>Set max time in seconds to poll in manual mode. The default max time is set to unlimited.</dd></dl>
<h3>Debugging Output Options:</h3>
<p><code>-l, &#8211;debug </code><i>level</i></p>
<dl>
<dd>Changes the log level (-1..4, default: 1)</dd></dl>
<h2>Examples</h2>
<p><code>ipsec scepclient &#8211;out caCert &#8211;url <a rel="nofollow" href="http://scepserver/cgi-bin/pkiclient.exe">http://scepserver/cgi-bin/pkiclient.exe</a> -f</code></p>
<dl>
<dd>Acquire CA certificate from SCEP server and store it in the default file $CONFDIR/ipsec.d/cacerts/caCert.der. If more then one CA certificate is returned, store them in files named &#8216;caCert-1.der&#8217;, &#8216;caCert-2.der&#8217;, etc. If an RA certificate is returned, store it in a file named &#8216;caCert-ra.der&#8217;. If more than one RA certificate is returned, store them in files named &#8216;caCert-ra-1.der&#8217;, &#8216;caCert-ra-2.der&#8217;, etc.</dd></dl>
<p> <code>ipsec scepclient &#8211;out pkcs1=joeKey.der -k 1024</code></p>
<dl>
<dd>Generate RSA private key with key length of 1024 bit and store it in file joeKey.der.</dd></dl>
<p> <code>ipsec scepclient &#8211;in pkcs1=joeKey.der &#8211;out pkcs10=joeReq.der \</code><br />
 <code>&#8211;dn &#8221;C=AT, CN=John Doe&#8221; -s email=john [at] doe.com -p mypassword</code></p>
<dl>
<dd>Generate a PKCS#10 request and store it in file joeReq.der. Use the RSA private key joeKey.der created earlier to sign the PKCS#10-Request. In addition to the distinguished name include a email-subjectAltName and a challenge password in the request.</dd></dl>
<p> <code>ipsec scepclient &#8211;out pkcs1=joeKey.der &#8211;out cert==joeCert.der \</code><br />
 <code>&#8211;dn &#8221;C=CH, CN=John Doe&#8221; -k 512 -p 5xH2pnT7wq \</code><br />
 <code>&#8211;url <a rel="nofollow" href="http://scep.hsr.ch/cgi-bin/pkiclient.exe">http://scep.hsr.ch/cgi-bin/pkiclient.exe</a> \</code><br />
 <code>&#8211;in cacert-enc=caCert.der &#8211;in cacert-sig=caCert.der</code></p>
<dl>
<dd>Generate a new RSA key for the request and store it in joeKey.der. Then enroll a certificate and store as joeCert.der. The challenge password is &#8216;5xH2pnT7wq&#8217;. The encryption and signature check has to be made with the same CA certificate caCert.der.</dd></dl>
<h2>Bugs</h2>
<p><code>&#8211;optionsfrom</code> seems to have parsing problems reading option files containing strings in quotation marks. </p>
