---
title: "fetch-crl(8)"
name: "fetch-crl"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fetch-crl/"
description: "fetch-crl – retrieve certificate revocation lists"
---

<p>fetch-crl &#8211; retrieve certificate revocation lists</p>
<h2>Synopsis</h2>
<p><code>fetch-crl</code> [<code>-c config</code>] [<code>-v</code>[<code>v</code>..<code>]</code>] [<code>-q</code>] [<code>-h</code>] [<code>&#8211;inet6glue</code>] [<code>-l infopath</code>] [<code>-o outputpath</code>] [<code>-s statepath</code>] [<code>-a agingtolerance</code>] [<code>-T httptimeout</code>] [<code>-r randomwait</code>] [<code>-p parallelism</code>] [<code>&#8211;formats openssl</code>|<code>pem</code>|<code>der</code>|<code>nss</code>]&nbsp;<wbr>.. [<code>&#8211;define key</code>=<code>value</code>]&nbsp;<wbr>.. [<code>&#8211;cfgdir dirname</code>]</p>
<h2>Description</h2>
<p>The <i>fetch-crl</i> utility will retrieve certificate revocation lists (CRLs) for a set of installed trust anchors, based on crl_url files or IGTF-style info files. It will install these for use with OpenSSL, NSS or third-party tools. It works based on a list of trust anchors, for each of which one or more CRLs should be installed in a CRL store. And for each of these CRLs, one or more URLs can be specified from which the specific CRL can be retrieved. There are several supported formats for CRL stores:</p>
<dl>
<dt>openssl</p>
<dd>has a directory in which <i>hash.</i> <i>i</i> files are stored, one CRL per file, and all CRLs for the trust anchors whose subject distinguished name hashes to <i>hash</i> are read and evaluated for each certificate issues by the CAs whose subject name hash matches <i>hash</i> OpenSSL in version 1 changes its subject name hashing algorithm, though, so that for one trust anchor <code>two</code> hashes could be used, depending on the specific OpenSSL version at hand. If OpenSSL version 1 or higher is used by <i>fetch-crl</i> and the default mode is used, each CRL is written out twice, once for each possible hash value. This mode in controlled by the <i>opensslmode</i> = { <i>dual</i> | <i>single</i> } configuration option in the configuration file.</p>
<dt>pem</p>
<dd>writes out the CRL in PEM (RFC 1421) format.</p>
<dt>der</p>
<dd>writes out the CRL in binary under distinguished encoding rules</p>
<dt>nss</p>
<dd>will use the crlutil from the Mozilla NSS tools to add or replace a CRL in the NSS cert8.db database.  Each CRLs can be retrieved from one of several URLs. These URLs are listed by default in the trust anchor meta-data: the <i>.info</i> file or the <i>.crl_url</i> file, as shipped with the trust anchor. In the crl_url file, there is one URL per line; in the .info file, the <i>crl_url </i> attribute is a semi-colon separated list of URLs. These URLs are then tried in order to retrieve a fresh CRL. Once data has been successfully retrieved, this data is used as the CRL if it passes verification, signature checking and expiration checks. Http, https, ftp and file URLs are supported. If data for a CRL has been downloaded but this data fails any of the subsequent checks (signature validation, freshness), the CRL data is discarded and NO further URLs are tried for this CRL! URLs can be pre-pended or post-pended to the default list via the configuration file. This can be used to prefer a local mirror repository over any URLs shipped by the trust anchor provider, without the need to modify the trust anchor metadata. By post-pending a URL, a &#8216;last-resort&#8217; download location can be added in case the CA provided URLs cannot be used. The pre- and post-pended URLS are subject to token expansion of the tokens <i>@ALIAS@</i>, <i>@ANCHORNAME@</i>, and <i>@R@</i>, where <i>R</i> is the sequence number of the CRL on a per-trust anchor basis. Retrieved CRLs may be PEM (RFC1421) or DER encoded. They are automatically converted as needed by fetch-crl, using the OpenSSL command-line tool. Retrieving a CRL without having an accompanying CA root certificate in an OpenSSL-accessible form (like <i>@ALIAS@.0</i> or <i>@ANCHORNAME@.@R@</i> will result in a verification failures. The CA lookup directory and patterns can be configured via the configuration file </p>
<h2>Token Expansion</h2>
<p>In paths and name templates, tokens are expanded to allow a single pattern to be used for all trust anchors. The <i>nametemplate_*</i>, <i>catemplate</i>, <i>prepend_url</i>, and <i>postpend_url</i> configuration settings are subject to token expansion. </p>
<p> The following tokens are recognised</p>
<dl>
<dt>@ALIAS@</p>
<dd>The alias name of the trust anchor as defined in the <i>info</i> file. If there is no info file and the meta-data is retrieved from <i>crl_url</i> files, then the alias is set to the basename (excluding the .crl_url suffix) of the filename of the trust anchor.</p>
<dt>@ANCHORNAME@</p>
<dd>The file name of the trust anchor, without any .info or .url_crl suffix.</p>
<dt>@R@</p>
<dd>The CRL sequence number, counting from 0. Note that most trust anchors only have a single CRL, with sequence number &quot;0&quot;. </p>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>Show help text.</p>
<dt><code>-l &#8211;infodir metadata-directory</code></p>
<dd>The script will search this directory for files with the suffix &#8216;.info&#8217; or &#8216;.crl_url&#8217;. Note: the CRL files to download must be in either PEM or DER format. </p>
<dt><code>-o &#8211;out outputDirectory</code></p>
<dd>Directory where to put the downloaded and processed CRLs. The directory to be used as argument for this option is typically /etc/grid-security/certificates Default: infodir (meta-data directory) </p>
<dt><code>-a &#8211;agingtolerance hours</code></p>
<dd>The maximum age of the locally downloaded CRL before download failures trigger actual error messages. This error message suppression mechanism only works if the CRL has been downloaded at least once and either the crl_url files are named after the hash of the CRL issuer name, or a state directory is used to preserve state across invocations. </p>
<p> Default: 24 hour aging tolerance</p>
<dt><code>-q &#8211;quiet</code></p>
<dd>Quiet mode (do not print information messages) </p>
<dt><code>-r &#8211;randomwait s</code></p>
<dd>Wait up to <i>s</i> seconds before starting the retrieval process(es). </p>
<dt><code>-p &#8211;parallelism n</code></p>
<dd>Do the retrieval for several trust anchors in parallel, with up to <i>n</i> processes doing retrievals. At most <i>n</i> downloads will be active at any one time. Multiple CRLs for the same trust anchor are still downloaded sequentially.</p>
<dt><code>&#8211;inet6glue</code></p>
<dd>Load the Net::INET6Glue module to enable IPv6 support in LWP.</p>
<dt><code>&#8211;define&nbsp;<wbr></code><i>key</i><code>=</code><i>value</i></p>
<dd>Add definitions to the configuration at runtime. The key=value pair is appended to the main section of the configuration, unless a colon is used in the key: then the part before the colon is the config file section name, and the part thereafter the key inside that section. To merely set a valueless option, set to to the null-string &quot;&quot;.</dl>
<h2>Configuration</h2>
<p>See <code><a rel="nofollow" href="http://wiki.nikhef.nl/grid/FetchCRL3">http://wiki.nikhef.nl/grid/FetchCRL3</a></code> or the included example file for a description of the configuration options. The default location of the configuration file is <i>/etc/fetch-crl.conf</i>. Supplementary configuration is read from all files located in <i>/etc/fetch-crl.d/</i>, or the directory designated by the <i>cfgdir</i> directive, whose collated contents are added to the existing configuration data.</p>
<h2>Notes</h2>
<p>Defaults can be set in the fetch-crl system configuration file /etc/fetch-crl.conf. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-openssl/">openssl</a>(1), <a rel="nofollow" href="http://wiki.nikhef.nl/grid/FetchCRL3">http://wiki.nikhef.nl/grid/FetchCRL3</a> </p>
<h2>Diagnostics</h2>
<p>Exit status is normally 0; if an error occurs, exit status is 1 and diagnostics will be written to standard error.</p>
<h2>License</h2>
<p>Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); </p>
<p> <code><a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a></code></p>
<h2>Bugs</h2>
<p>Although fetch-crl3 will install multiple CRLs in the CRL stores (called &#8216;.r0&#8217;, &#8216;.r1&#8217;, or labelled appropriately in an NSS store), if the number of CRLs decreases the left-overs are not automatically removed. So if the number of CRLs for a particular CA does down from <i>n</i> to <i>n-1</i>, the file &#8216;.r<i>n</i>&#8216; must be removed manually. </p>
