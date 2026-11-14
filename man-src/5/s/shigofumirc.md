---
title: "shigofumirc(5)"
name: "shigofumirc"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shigofumirc/"
description: "shigofumirc – Configuration file for Shigofumi"
---

<p>shigofumirc &#8211; Configuration file for Shigofumi</p>
<h2>Description</h2>
<p>Configuration for shigofumi is loaded from .shigofumirc in user&#8217;s home directory by default. </p>
<p> The file is plain text file with simple syntax: Setting is stored in <i>option</i> = <i>value</i> format. If value is a type of string, it must be delimited by quotation marks. Boolean values can be expressed as &quot;true&quot; or non-zero integer (1) for affirmation, or &quot;false&quot; or zero integer (0) for negation. Simple numeric values are unquoted. Commentary starts with hash sign (#) and continues to the end of the line. </p>
<p> If an option accepts list of values, the syntax is traditional mathematical set notation: { <i>value1</i> , <i>value2</i> }.</p>
<h2>Options</h2>
<p>Following options are recognized. Not all of them must present. Missing options fall to default value back.</p>
<h3>Account Options</h3>
<p>base_url</p>
<dl>
<dd>Base URL for ISDS server. Be careful when setting this value: This can reveal your password to bad guys running fake server (if you do not verify server identity preciously) and different host names are used with different log-in mechanism. In addition, there are two system instances administrated by Czech government: official one and testing one. </p>
<p> E.g. use &quot;<a rel="nofollow" href="https://ws1.czebox.cz/">https://ws1.czebox.cz/</a>&quot; for testing instance of ISDS or &quot;<a rel="nofollow" href="https://ws1.mojedatovaschranka.cz/">https://ws1.mojedatovaschranka.cz/</a>&quot; for official instance with valid and legal data when logging in without TLS client certificate. Otherwise, with client certificate in use, replace the ws1 domain with ws1c domain. Or, with OTP authentication, replace with www domain. I.e. &quot;<a rel="nofollow" href="https://ws1c.czebox.cz/">https://ws1c.czebox.cz/</a>&quot; for testing instance with certificate authentication or &quot;<a rel="nofollow" href="https://www.mojedatovaschranka.cz/">https://www.mojedatovaschranka.cz/</a>&quot; for official instance with OTP authentication. </p>
<p> Do not forget on leading protocol schema and trailing slash. Default value is official instance locator suitable for selected authentication method provided by libisds library.</dl>
<p> certificate_format</p>
<dl>
<dd>Format of client certificate used to authenticate user into ISDS. Three distinct values are recognized: PEM for Base64 serialization to file, DER for binary serialization to file, and ENG to specify the certificate is stored in cryptographic engine. Default value is empty string.</dl>
<p> certificate_path</p>
<dl>
<dd>File where client certificate used to authenticate user into ISDS is, if certificate_format option is set to PEM or DER. If certificate_format is ENG, this is an identifier of the certificate inside the cryptograhic engine. NSS library uses this option as certificate nickname. Default value is empty string signaling not to authenticate user by a certificate.</dl>
<p> key_engine</p>
<dl>
<dd>Cryptographic engine holding client private key and/or certificate used to authenticate user into ISDS. The value identifies a device (e.g. a smart card) known to underlying cryptographic library where key and/or certificate is stored. Interpretation depends on the cryptographic library. This option takes effect only if key_format or certificate_format is ENG. Default value is empty string.</dl>
<p> key_format</p>
<dl>
<dd>Format of client key used to authenticate user into ISDS. Three distinct values are recognized: PEM for Base64 serialization to file, DER for binary serialization to file, and ENG to specify the key is stored in cryptographic engine. Default value is empty string.</dl>
<p> key_path</p>
<dl>
<dd>File where client key used to authenticate user into ISDS is, if key_format option is set to PEM or DER. If key_format is ENG, this is an identifier of the key inside the cryptograhic engine. NSS library uses this option as certificate nickname. Default value is empty string. This can mean the key is stored along the certificate.</dl>
<p> key_password</p>
<dl>
<dd>Password protecting private key used for client authentication using asymetric cryptography. Default value is empty string. Underlying cryptographic library can raise its own password query or require to obtain the code in other way (e.g. typing PIN on smart card reader key pad).</dl>
<p> otp_method</p>
<dl>
<dd>One-time password authentication method. Default value is undefined string what means do not use OTP authentication. If this option is defined, OTP will be used for authentication. Two methods are recognised: HOTP for HMAC-based One-Time Password method and TOTP for Time-based One-Time Password method.</dl>
<p> otp_code</p>
<dl>
<dd>One-time code for OTP authentication. </p>
<p> If HMAC-based method is used, this code will be computed in a device or a piece of software which should be in exclusive possession of its user. </p>
<p> If Time-based method is used, the code will be generated by ISDS server and delivered to the user by a side channel. (The channel is an SMS currently. Because the delivery is specialy charged, the time code generation is protected by plain password too. User sends standard password without OTP code first, then server delivers code by the SMS message and finally user will retry log-in with both password and both OTP code.) </p>
<p> Default value is empty string and user will be asked interactively for the OTP code when needed. Because of dynamic nature of this code, setting the value in a configuration file is pointless. However you could rewrite this value for each shigofumi run in batch mode.</dl>
<p> password</p>
<dl>
<dd>Password assigned to given user-name. User must keep it in secret. This password is used while HTTP authentication and is passed to underlying network libraries. Make sure this configuration file or your swap partition (network library together with password can be swapped out during physical memory outage) will not get to bad guys. Encrypt them before. Default value is empty string.</dl>
<p> username</p>
<dl>
<dd>ISDS user log-in name. Identifies a user in ISDS. One person can have more identities. Default value is empty string.</dl>
<h3>TLS Options</h3>
<p>ca_directory</p>
<dl>
<dd>Path to directory with trusted authorities certificates stored in separate files (files must have special names usually). Default value is provided by underlying cryptographic library. Exact meaning of this option depends on interpretation by used cryptographic library.</dl>
<p> ca_file</p>
<dl>
<dd>Path to file with trusted authorities certificates (concatenated list of PEM-formatted certificates). Default value is provided by underlying cryptographic library. Exact meaning of this option depends on interpretation by used cryptographic library.</dl>
<p> crl_file</p>
<dl>
<dd>Path to file with certificate revocation lists (concatenated list of CRLs in PEM format usually). Default value is provided by underlying cryptographic library. Exact meaning of this option depends on interpretation by used cryptographic library.</dl>
<p> verify_server</p>
<dl>
<dd>Boolean switch deciding whether server identity should be verified. When using HTTPS connection to the server, the identity of server can be verified in TLS negotiation phase by validating server certificate against trusted certificate authority certificate and certificate revocation list. Default value is true. It&#8217;s strongly recommended to keep it on.</dl>
<h3>Network Options</h3>
<p>timeout</p>
<dl>
<dd>Non-negative integer setting network time-out in milliseconds. Use 0 not to limit any network operation. Default value is 10,000 ms.</dl>
<h3>Log Options</h3>
<p>log_facilities</p>
<dl>
<dd>List of string values selecting libisds facility to log. Valid values are: none, http, soap, isds, file, sec, xml, all. Default set is {&quot;none&quot;}.</dl>
<p> log_file</p>
<dl>
<dd>String value selecting file to append ISDS log. The log catches libisds internal debugging protocol. It does not cover messages produces by shigofumi itself. This feature is designed to debug underlying libraries and protocols like ISDS, SOAP, or cURL&#8217;s HTTP(S). If undefined, shigofumi logs to standard error output.</dl>
<p> log_level</p>
<dl>
<dd>Integer value setting log verbosity of libisds from interval &lt;0;100&gt;. 0 is no logging, 10 is critical messages, 20 errors, 30 warnings, 40 informative messages, 50 debug messages, 100 messages of all severities. Default log level is 20.</dl>
<h3>Other Options</h3>
<p>clean_temporary_files</p>
<dl>
<dd>Boolean switch deciding whether to remove temporary files at shigofumi exit. This applies to files created for <code>opendoc</code> command, as external utility can access the file after quiting shigofumi. Default value is true.</dl>
<p> confirm_send</p>
<dl>
<dd>Boolean switch deciding whether to require confirmation before sending composed message. Default value is true.</dl>
<p> mark_message_read</p>
<dl>
<dd>Boolean switch deciding whether right downloaded incoming messages should be marked as read automatically. If true, change message state to read on the server. Otherwise keep message state intact. Default value is false. </p>
<p> You can change the state to read state by <code>read</code> command manually latter. </p>
<p> Be ware ISDS web portal marks messages as read automatically. Note, there is no way to unmark a message to unread state back.</dl>
<p> normalize_mime_type</p>
<dl>
<dd>Boolean switch deciding whether MIME type of documents retrieved from a message should be normalized to standard values. Default value is true. </p>
<p> ISDS does not check document MIME type a client supplies. Unfortunately, official client sends invalid values (file name extension usually). This option allows Shigofumi to fix the type on-the-fly. Be ware the original value stored in ISDS or locally saved message keeps untouched.</dl>
<p> open_command</p>
<dl>
<dd>List of string values defining external utility to execute when opening a document. </p>
<p> First value is command, other values are command arguments in order. If command is not absolute file name, it&#8217;s located according <code>PATH</code> environment variable. If value contains %f substring, it will be expanded to name of file to open. If value contains %t substring, it will be expanded to MIME type of document to open. Use %% sequence to escape per-cent character. </p>
<p> Default value is {&quot;xdg-open&quot;, &quot;%f&quot;}.</dl>
<p> overwrite_files</p>
<dl>
<dd>Boolean switch deciding whether newly created files should overwrite existing ones. If true, existing files will be overwritten silently. Otherwise error wil be raised. Default value is true. </p>
<p> This does not apply to log file. Its new content is appended always.</dl>
<h2>Notice On Cryptographic Library</h2>
<p>Shigofumi uses libisds that utilizes cURL library that can use three different cryptographic libraries at this time: OpenSSL, GnuTLS and NSS. Each library has different set of features and different configuration. Thus exact meaning of some Shigofumi configuration options can be slightly shifted (e.g. the name of client certificate and key). Some options cannot be understood at all (e.g. GnuTLS does not support directory of certificates). </p>
<p> Current cryptographic library can be determined from <code>shigofumi -V</code> output.</p>
<h2>Files</h2>
<p>~/.shigofumirc</p>
<dl>
<dd>Default location of the configuration file.</dl>
<h2>Example</h2>
<pre><code>base_url = &quot;https://ws1.czebox.cz/&quot;
# These credentials are invalid
username = 1s79vd
password = XY123456
verify_server = true
ca_file = /etc/ssl/certs/ca-certificates.crt
ca_directory = /etc/ssl/certs
crl_file = /etc/ssl/crl
log_facilities = {&quot;http&quot;, &quot;soap&quot;}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-shigofumi/">shigofumi</a></code>(1)</p>
<h2>Author</h2>
<p><code>Petr Písař</code></p>
<dl>
<dd>He&#8217;s written Shigofumi and libisds.</dl>
