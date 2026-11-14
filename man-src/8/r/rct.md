---
title: "rct(8)"
name: "rct"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rct/"
description: "rct – Displays information (headers) about or size and statistics of a entitlement, product, or identity certificate used by Red Hat Subscription Manager."
---

<p>rct &#8211; Displays information (headers) about or size and statistics of a entitlement, product, or identity certificate used by Red Hat Subscription Manager. </p>
<h2>Synopsis</h2>
<p>rct cat-cert [&#8211;no-content] [&#8211;no-products] /path/to/certificate.pem rct stat-cert /path/to/certificate.pem rct cat-manifest [&#8211;no-content] /path/to/consumer_export.zip rct dump-manifest [&#8211;destination /path] [&#8211;force] /path/to/consumer_export.zip </p>
<h2>Description</h2>
<p>Red Hat Subscription Manager uses X.509 certificates to identify a registered system (identity certificate), the products installed on that system (product certificates), and the subscriptions attached to the system (entitlement certificates), including available content repositories, products, and support levels. All of the information that Subscription Manager requires is contained in the body of the certificate. </p>
<h2>Commands</h2>
<dl>
<dt><code>stat-cert</code></p>
<dd>Prints the size of the certificate and other details about the certificate. The precise details depend on the type of certificate being checked. </p>
<dt><code>cat-cert</code></p>
<dd>Prints the information that is contained in the certificate itself, such as the certificate headers, serial numbers, products, and content sets. Two options, <code>&#8211;no-content</code> and <code>&#8211;no-products</code>, can be used to shorten the output to include only header and descriptive information. </p>
<dt><code>cat-manifest</code></p>
<dd>Prints the information that is contained in the subscription service manifest. The manifest is an archive of JSON files which contain all of the subscription information for subscriptions allocated to the on-premise service. The <code>&#8211;no-content</code> option can be used to reduce the detail shown in the output. </p>
<dt><code>dump-manifest</code></p>
<dd>Extracts the contents of the manifest archive. </p>
</dl>
<h2>The Stat-Cert Command</h2>
<p>The <code>rct</code> tool is used to gather information about the already-issued certificates being used by Subscription Manager. The main reason for that is that certificate sizes, for a number of reasons, impact content delivery service performance. </p>
<p> For large accounts and organizations, there can be a very large number of products and content sets available. Older versions of entitlement certificates (version 1.0) used different (less efficient) DER encoding, so that large amounts of information results in very large certificates. (This is what caused timeouts or crashes when dealing with some content services.) Newer entitlement certificate versions (version 3.0) use more efficient encoding on large content sets, , resulting in smaller certificate content sizes and better service performance. </p>
<p> If there are problems with the content service timing out or returning errors, then the <code>rct stat-cert</code> command can be used to check the size and version of a given entitlement certificate quickly. </p>
<p> A large number of content sets is anything over 185 total sets. Both the total number of content sets and the size of the DER encoding in the certificate could affect performance.</p>
<h3>Options</h3>
<dl>
<dt><i>/path/to/cert.pem</i></p>
<dd>Gives the full path and filename to the PEM certificate for the given subscription, product, or system. This is required. </p>
</dl>
<h3>Examples</h3>
<p>The statistics for an entitlement certificate show both the DER size and the number of content sets, among other information:</p>
<dl>
<dd>* Type (entitlement certificate)</p>
<dd>* Version (of the certificate style); newer versions will be 3.x, with better performance for handling large content sets</p>
<dd>* DER size, which gives the size of the certificate contents (not the size of the certificate file itself)</p>
<dd>* Key size, for the associated key file, in bytes</p>
<dd>* The total number of available content sets in the subscription </p>
</dl>
<p> For example:</p>
<dl>
<dd>
<pre>[root [at] server ~]# rct stat-cert /etc/pki/entitlement/2027912482659389239.pem
Type: Entitlement Certificate
Version: 1.0
DER size: 47555b
Subject Key ID size: 553b
Content sets: 100</pre>
</dl>
<p> While the size of the certificate is less of an issue for identity and product certificates (which are quite small), the <code>stat-cert</code> command can still be used to view the size and statistics of the certificates. </p>
<p> For a product certificate, the <code>stat-cert</code> command shows:</p>
<dl>
<dd>* Type (product certificate)</p>
<dd>* Version (of the certificate style)</p>
<dd>* DER size, which gives the size of the certificate contents (not the size of the certificate file itself) </p>
</dl>
<p> For example:</p>
<dl>
<dd>
<pre>[root [at] server ~]# rct stat-cert /etc/pki/product/69.pem
Type: Product Certificate
Version: 1.0
DER size: 1558b</pre>
</dl>
<p> For an identity certificate:</p>
<dl>
<dd>* Type (identity certificate)</p>
<dd>* Version (of the certificate style)</p>
<dd>* DER size, which gives the size of the certificate contents (not the size of the certificate file itself)</p>
<dd>* Key size, for the associated key file, in bytes </p>
</dl>
<p> For example:</p>
<dl>
<dd>
<pre>[root [at] server ~]# rct stat-cert /etc/pki/consumer/cert.pem
Type: Identity Certificate
Version: 1.0
DER size: 1488b
Subject Key ID size: 20b</pre>
</dl>
<h2>The Cat-Cert Command</h2>
<p>Each certificate contains a complete set of information with all of the details for whatever element is being identified. That information can be displayed, in pretty-print form, using the <code>cat-cert</code> command.</p>
<h3>Options</h3>
<dl>
<dt><i>/path/to/cert.pem</i></p>
<dd>Gives the full path and filename to the PEM certificate for the given subscription, product, or system. This is required. </p>
<dt><code>&#8211;no-content</code></p>
<dd>Returns all of the certification information, order information, and product information, but excludes all of the <code>Content</code> sections, which significantly reduced the information printed to stdout. <i>This is for an entitlement certificate only.</i> </p>
<dt><code>&#8211;no-products</code></p>
<dd>Returns all of the certification information, order information, and content (repository) information, but excludes all of the <code>Product</code> sections, which significantly reduced the information printed to stdout. <i>This is for an entitlement certificate only.</i> </p>
<dt><i>/path/to/cert.pem</i></p>
<dd>Gives the full path and filename to the PEM certificate for the given subscription, product, or system. </p>
</dl>
<h3>Output</h3>
<p>The command returns the most basic information about the certificate &#8212; such as its directory path, its serial number and subject name, and its validity period (start and end dates) &#8212; in the <i>Certificate</i> section:</p>
<dl>
<dd>* Path &#8212; the filesystem location where the certificate is installed</p>
<dd>* Version &#8212; the certificate format version <i>&#8212; P</i> * Serial &#8212; the serial number for the certificate</p>
<dd>* Start/End Date &#8212; the validity period for the certificate</p>
<dd>* Alt Name &#8212; the subject alternative name, which uses the hostname of the system rather than the UUID (for identity certificates only)</dl>
<p> The Subject DN of the certificate is in the <i>Subject</i> section. </p>
<p> For example, for the identity certificate:</p>
<dl>
<dd>
<pre>[root [at] server ~]# rct cat-cert /etc/pki/consumer/cert.pem
+-------------------------------------------+
 Identity Certificate
+-------------------------------------------+
Certificate:
 Path: /etc/pki/consumer/cert.pem
 Version: 1.0
 Serial: 824613308750035399
 Start Date: 2012-11-09 16:20:22+00:00
 End Date: 2013-11-09 16:20:22+00:00
 Alt Name: server.example.com
Subject:
 CN: e94bc90e-44a1-4f8c-b6fc-0a3e9d6fac2b</pre>
</dl>
<p> A product certificate contains additional information in a <code>Product</code> section, which defines the information for the specific installed product, such as its name, product version, and any yum tags used for that product. For example:</p>
<dl>
<dd>
<pre>[root [at] server ~]# rct cat-cert /etc/pki/product/69.pem
+-------------------------------------------+
 Product Certificate
+-------------------------------------------+
Certificate:
 Path: /etc/pki/product/69.pem
 Version: 1.0
 Serial: 12750047592154746449
 Start Date: 2012-10-04 18:45:02+00:00
 End Date: 2032-09-29 18:45:02+00:00
Subject:
 CN: Red Hat Product ID [b4f7ac9e-b7ed-45fa-9dcc-323beb20e916]
Product:
 ID: 69
 Name: Red Hat Enterprise Linux Server
 Version: 6.4
 Arch: x86_64
 Tags: rhel-6,rhel-6-server</pre>
</dl>
<p> The most information is contained in the entitlement certificate. Along with the <code>Certificate</code> and <code>Subject</code>, it also has a <code>Product</code> section that defines the product group that is covered by the subscription. </p>
<p> Then, it contains an <code>Order</code> section that details everything related to the purchase of the subscription (such as the contract number, service level, total quantity, quantities assigned to the system, and other details on the subscription). </p>
<p> A subscription for a product covers the version purchased <i>and</i> every previous version of the product. For example, when a subscription is purchased for Red Hat Enterprise Linux 6.4, the subscription provides full access to all RHEL 6 repositories, <code>plus</code> access to all RHEL 5 repositories and then other included product content repositories, like Subscription Asset Manager. Every available content repository is listed in a <code>Content</code> section that contains the repository name, associated tags, its URL, and a notice on whether the yum repository is enabled by default. For example:</p>
<dl>
<dd>
<pre>[root [at] server ~]# rct cat-cert /etc/pki/entitlement/2027912482659389239.pem
+-------------------------------------------+
 Entitlement Certificate
+-------------------------------------------+
Certificate:
 Path: /etc/pki/entitlement/2027912482659389239.pem
 Version: 1.0
 Serial: 2027912482659389239
 Start Date: 2011-12-31 05:00:00+00:00
 End Date: 2012-12-31 04:59:59+00:00
Subject:
 CN: 8a99f9843adc8b8f013ae5f9de022b73
Product:
 ID: 69
 Name: Red Hat Enterprise Linux Server
 Version:
 Arch: x86_64,ia64,x86
 Tags:
Order:
 Name: Red Hat Enterprise Linux Server, Premium (8 sockets) (Up to 4 guests)
 Number: 2673502
 SKU: RH0103708
 Contract: 10011052
 Account: 5206751
 Service Level: Premium
 Service Type: L1-L3
 Quantity: 100
 Quantity Used: 1
 Socket Limit: 8
 Virt Limit:
 Virt Only: False
 Subscription:
 Stacking ID:
 Warning Period: 0
 Provides Management: 0
Content:
 Type: yum
 Name: Red Hat Enterprise Linux 6 Server (RPMs)
 Label: rhel-6-server-rpms
 Vendor: Red Hat
 URL: /content/dist/rhel/server/6/$releasever/$basearch/os
 GPG: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
 Enabled: True
 Expires: 86400
 Required Tags: rhel-6-server</pre>
</dl>
<h2>The Cat-Manifest Command</h2>
<p>A subscription management service is allocated a specific bloc of subscriptions that are available to an account. This list of subscriptions is the <i>manifest</i> for the service. The <code>cat-manifest</code> command reads and prints the details of the manifest, such as the creation date, the system UUID and name, available products, and subscription details. </p>
<p> There are multiple JSON files in the archive, identifying different aspects of the subscription service and subscription configuration, such as the general manifest properties, subscription information, content and repository information, and product information.</p>
<h3>Options</h3>
<dl>
<dt><i>/path/to/consumer_export.zip</i></p>
<dd>Gives the path and filename (by default, <code>consumer_export.zip</code>) for the manifest file on the local system. This is required. </p>
</dl>
<h3>Examples</h3>
<p>The command pretty-prints all of the details about the manifest itself and the allocated subscriptions, products, and content.</p>
<dl>
<dd>
<pre>[root [at] server ~]# rct cat-manifest /tmp/consumer_export.zip
+-------------------------------------------+
 Manifest
+-------------------------------------------+
General:
 Server: candlepin
 Server Version: 1.3
 Date Created: 13 April 2013
 Creator: admin
Consumer:
 Name: server.example.com
 UUID:
 Type: system
Subscriptions:
 Name: Red Hat Enterprise Linux
 Quantity: 249237
 Created: 12/01/2011
 Start Date: 01/01/2012
 End Date: 01/01/2022
 Service Level: Premium
 Service Type: Physical
 Architectures: x86,x86_64
 SKU: SYS0395
 Contract: 12345678
 Order: 09876543
 Account: abcd1234
 Entitlement File: /etc/pki/entitlement/2027912482659389239.pem
 Certificate File: /etc/pki/product/69.pem
 Certificate Version: 3</pre>
</dl>
<h2>The Dump-Manifest Command</h2>
<p>A subscription management service is allocated a specific bloc of subscriptions that are available to an account. This list of subscriptions is the <i>manifest</i> for the service. The <code>cat-manifest</code> command prints the contents of the manifest.</p>
<h3>Options</h3>
<dl>
<dt><i>/path/to/consumer_export.zip</i></p>
<dd>Gives the path and filename (by default, <code>consumer_export.zip</code>) for the manifest file on the local system. This is required. </p>
<dt><code>&#8211;destination=PATH</code></p>
<dd>Specifies an export directory to which to extract and save the contents of the manifest archive. If no destination is given, then the archive is extracted to the local directory. </p>
<dt><code>&#8211;force, -f</code></p>
<dd>Overwrites any existing archive files. If a manifest archive already exists in the specified location (for example, if the manifest has already been dumped once), then attempting to dump the manifest to the same location will fail. Using the <code>&#8211;force</code> option forces the dump operation to complete and overwrites the previous file. </p>
</dl>
<h3>Examples</h3>
<p>This command simply extracts the manifest files to a given location (the working directory by default). The manifest itself contains multiple JSON files, with separate JSON files providing details on the manifest itself, each individual product, each individual subscription, and details for the specific, on-premise subscription management service. </p>
<p> For example:</p>
<dl>
<dd>
<pre>[root [at] server ~]# rct dump-manifest --destination /export/archives/sam/manifest /tmp/consumer_export.zip
The manifest has been dumped to the /export/archives/sam/manifest directory.</pre>
</dl>
<h2>Files</h2>
<dl>
<dd>* Product certificates: /etc/pki/product/*.pem</p>
<dd>* Subscription certificates: etc/pki/entitlement/&lt;serial#&gt;.pem</p>
<dd>* System identity certificates: /etc/pki/consumer/cert.pem</p>
<dd>* The manifest: consumer_export.zip </p>
</dl>
<h2>Bugs</h2>
<p>This tool is part of Red Hat Subscription Manager. To file bugs against this command-line tool, go to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com">https://bugzilla.redhat.com</a>&gt;, and select Red Hat &gt; Red Hat Enterprise Linux &gt; subscription-manager. </p>
<h2>Authors</h2>
<p>Deon Lackey &lt;dlackey [at] redhat.com&gt;, Michael Stead &lt;mstead [at] redhat.com&gt;, and James Bowes &lt;jbowes [at] redhat.com&gt;. The rct tool was written by James Bowes.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
