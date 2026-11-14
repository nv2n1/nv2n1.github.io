---
title: "update-ca-trust(8)"
name: "update-ca-trust"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-ca-trust/"
description: "update-ca-trust – manage consolidated and dynamic configuration of CA certificates and associated trust"
---

<p>update-ca-trust &#8211; manage consolidated and dynamic configuration of CA certificates and associated trust</p>
<h2>Synopsis</h2>
<p><code>update-ca-trust</code> [<i>COMMAND</i>]</p>
<h2>Description</h2>
<p><a href="/docs/linux/man/8-update-ca-trust/">update-ca-trust</a>(8) is used to manage a consolidated and dynamic configuration feature of Certificate Authority (CA) certificates and associated trust. </p>
<p> The feature is available for new applications that read the consolidated configuration files found in the /etc/pki/ca-trust/extracted directory or that load the PKCS#11 module p11-kit-trust.so </p>
<p> Parts of the new feature are also provided in a way to make it useful for legacy applications. </p>
<p> Many legacy applications expect CA certificates and trust configuration in a fixed location, contained in files with particular path and name, or by referring to a classic PKCS#11 trust module provided by the NSS cryptographic library. </p>
<p> The dynamic configuration feature provides functionally compatible replacements for classic configuration files and for the classic NSS trust module named libnssckbi. </p>
<p> In order to enable legacy applications, that read the classic files or access the classic module, to make use of the new consolidated and dynamic configuration feature, the classic filenames have been changed to symbolic links. The symbolic links refer to dynamically created and consolidated output stored below the /etc/pki/ca-trust/extracted directory hierarchy. </p>
<p> The output is produced using the <i>update-ca-trust</i> command (without parameters), or using the <i>update-ca-trust extract</i> command. In order to produce the output, a flexible set of source configuration is read, as described in section SOURCE CONFIGURATION. </p>
<p> In addition, the classic PKCS#11 module is replaced with a new PKCS#11 module (p11-kit-trust.so) that dynamically reads the same source configuration.</p>
<h2>Source Configuration</h2>
<p>The dynamic configuration feature uses several source directories that will be scanned for any number of source files. <code>It is important to select the correct subdirectory for adding files, as the subdirectory defines how contained certificates will be trusted or distrusted, and which file formats are read.</code> </p>
<p> Files in <code>subdirectories below the directory hierarchy /usr/share/pki/ca-trust-source/</code> contain CA certificates and trust settings in the PEM file format. The trust settings found here will be interpreted with a <code>low priority</code>. </p>
<p> Files in <code>subdirectories below the directory hierarchy /etc/pki/ca-trust/source/</code> contain CA certificates and trust settings in the PEM file format. The trust settings found here will be interpreted with a <code>high priority</code>. </p>
<p> <code>You may use the following rules of thumb to decide, whether your configuration files should be added to the /etc or rather to the /usr directory hierarchy:</code> </p>
<dl>
<dd>&bull; If you are manually adding a configuration file to a system, you probably want it to override any other default configuration, and you most likely should add it to the respective subdirectory in the /etc hierarchy.</dl>
<dl>
<dd>&bull; If you are creating a package that provides additional root CA certificates, that is intended for distribution to several computer systems, but you still want to allow the administrator to override your list, then your package should add your files to the respective subdirectory in the /usr hierarchy.</dl>
<dl>
<dd>&bull; If you are creating a package that is supposed to override the default system trust settings, that is intended for distribution to several computer systems, then your package should install the files to the respective subdirectory in the /etc hierarchy.</dl>
<p> <code>QUICK HELP 1</code><code>: To add a certificate in the simple PEM or DER file formats to the list of CAs trusted on the system:</code> </p>
<dl>
<dd>&bull; add it as a new file to directory /etc/pki/ca-trust/source/anchors/</dl>
<dl>
<dd>&bull; run <i>update-ca-trust extract</i></dl>
<p> <code>QUICK HELP 2</code><code>: If your certificate is in the extended BEGIN TRUSTED file format (which may contain distrust/blacklist trust flags, or trust flags for usages other than TLS) then:</code> </p>
<dl>
<dd>&bull; add it as a new file to directory /etc/pki/ca-trust/source/</dl>
<dl>
<dd>&bull; run <i>update-ca-trust extract</i></dl>
<p> <code>In order to offer simplicity and flexibility, the way certificate files are treated depends on the subdirectory they are installed to.</code> </p>
<dl>
<dd>&bull; simple trust anchors subdirectory: /usr/share/pki/ca-trust-source/anchors/ or /etc/pki/ca-trust/source/anchors/</dl>
<dl>
<dd>&bull; simple blacklist (distrust) subdirectory: /usr/share/pki/ca-trust-source/blacklist/ or /etc/pki/ca-trust/source/blacklist/</dl>
<dl>
<dd>&bull; extended format directory: /usr/share/pki/ca-trust-source/ or /etc/pki/ca-trust/source/</dl>
<p> <code>In the main directories /usr/share/pki/ca-trust-source/ or /etc/pki/ca-trust/source/ you may install one or multiple files in the following file formats:</code> </p>
<dl>
<dd>&bull; certificate files that include trust flags, in the BEGIN/END TRUSTED CERTIFICATE file format (any file name), which have been created using the openssl x509 tool and the -addreject -addtrust options. Bundle files with multiple certificates are supported.</dl>
<dl>
<dd>&bull; files in the p11-kit file format using the .p11-kit file name extension, which can (e.g.) be used to distrust certificates based on serial number and issuer name, without having the full certificate available. (This is currently an undocumented format, to be extended later. For examples of the supported formats, see the files shipped with the ca-certificates package.)</dl>
<dl>
<dd>&bull; certificate files without trust flags in either the DER file format or in the PEM (BEGIN/END CERTIFICATE) file format (any file name). Such files will be added with neutral trust, neither trusted nor distrusted. They will simply be known to the system, which might be helpful to assist cryptographic software in constructing chains of certificates. (If you want a CA certificate in these file formats to be trusted, you should remove it from this directory and move it to the ./anchors subdirectory instead.)</dl>
<p> In the anchors subdirectories /usr/share/pki/ca-trust-source/anchors/ or /etc/pki/ca-trust/source/anchors/ you may install one or multiple certificates in either the DER file format or in the PEM (BEGIN/END CERTIFICATE) file format. Each certificate will be treated as <code>trusted</code> for all purposes. </p>
<p> In the blacklist subdirectories /usr/share/pki/ca-trust-source/blacklist/ or /etc/pki/ca-trust/source/blacklist/ you may install one or multiple certificates in either the DER file format or in the PEM (BEGIN/END CERTIFICATE) file format. Each certificate will be treated as <code>distrusted</code> for all purposes. </p>
<p> Please refer to the <a href="/docs/linux/man/1-x509/">x509</a>(1) manual page for the documentation of the BEGIN/END CERTIFICATE and BEGIN/END TRUSTED CERTIFICATE file formats. </p>
<p> Applications that rely on a static file for a list of trusted CAs may load one of the files found in the /etc/pki/ca-trust/extracted directory. After modifying any file in the /usr/share/pki/ca-trust-source/ or /etc/pki/ca-trust/source/ directories or in any of their subdirectories, or after adding a file, it is necessary to run the <i>update-ca-trust extract</i> command, in order to update the consolidated files in /etc/pki/ca-trust/extracted/ . </p>
<p> Applications that load the classic PKCS#11 module using filename libnssckbi.so (which has been converted into a symbolic link pointing to the new module) and any application capable of loading PKCS#11 modules and loading p11-kit-trust.so, will benefit from the dynamically merged set of certificates and trust information stored in the /usr/share/pki/ca-trust-source/ and /etc/pki/ca-trust/source/ directories.</p>
<h2>Extracted Configuration</h2>
<p>The directory /etc/pki/ca-trust/extracted/ contains generated CA certificate bundle files which are created and updated, based on the SOURCE CONFIGURATION by running the <i>update-ca-trust extract</i> command. </p>
<p> If your application isn&#8217;t able to load the PKCS#11 module p11-kit-trust.so, then you can use these files in your application to load a list of global root CA certificates. </p>
<p> Please never manually edit the files stored in this directory, because your changes will be lost and the files automatically overwritten, each time the <i>update-ca-trust extract</i> command gets executed. </p>
<p> In order to install new trusted or distrusted certificates, please rather install them in the respective subdirectory below the /usr/share/pki/ca-trust-source/ or /etc/pki/ca-trust/source/ directories, as described in the SOURCE CONFIGURATION section. </p>
<p> The directory /etc/pki/ca-trust/extracted/java/ contains a CA certificate bundle in the java keystore file format. Distrust information cannot be represented in this file format, and distrusted certificates are missing from these files. File cacerts contains CA certificates trusted for TLS server authentication. </p>
<p> The directory /etc/pki/ca-trust/extracted/openssl/ contains CA certificate bundle files in the extended BEGIN/END TRUSTED CERTIFICATE file format, as described in the <a href="/docs/linux/man/1-x509/">x509</a>(1) manual page. File ca-bundle.trust.crt contains the full set of all trusted or distrusted certificates, including the associated trust flags. </p>
<p> The directory /etc/pki/ca-trust/extracted/pem/ contains CA certificate bundle files in the simple BEGIN/END CERTIFICATE file format, as described in the <a href="/docs/linux/man/1-x509/">x509</a>(1) manual page. Distrust information cannot be represented in this file format, and distrusted certificates are missing from these files. File tls-ca-bundle.pem contains CA certificates trusted for TLS server authentication. File email-ca-bundle.pem contains CA certificates trusted for E-Mail protection. File objsign-ca-bundle.pem contains CA certificates trusted for code signing.</p>
<h2>Commands</h2>
<p>(absent/empty command)</p>
<dl>
<dd>Same as the <code>extract</code> command described below. (However, the command may print fewer warnings, as this command is being run during rpm package installation, where non-fatal status output is undesired.)</dl>
<p> <code>extract</code></p>
<dl>
<dd>Instruct update-ca-trust to scan the SOURCE CONFIGURATION and produce updated versions of the consolidated configuration files stored below the /etc/pki/ca-trust/extracted directory hierarchy.</dl>
<h2>Files</h2>
<p>/etc/pki/tls/certs/ca-bundle.crt</p>
<dl>
<dd>Classic filename, file contains a list of CA certificates trusted for TLS server authentication usage, in the simple BEGIN/END CERTIFICATE file format, without distrust information. This file is a symbolic link that refers to the consolidated output created by the update-ca-trust command.</dl>
<p> /etc/pki/tls/certs/ca-bundle.trust.crt</p>
<dl>
<dd>Classic filename, file contains a list of CA certificates in the extended BEGIN/END TRUSTED CERTIFICATE file format, which includes trust (and/or distrust) flags specific to certificate usage. This file is a symbolic link that refers to the consolidated output created by the update-ca-trust command.</dl>
<p> /etc/pki/java/cacerts</p>
<dl>
<dd>Classic filename, file contains a list of CA certificates trusted for TLS server authentication usage, in the Java keystore file format, without distrust information. This file is a symbolic link that refers to the consolidated output created by the update-ca-trust command.</dl>
<p> /usr/share/pki/ca-trust-source</p>
<dl>
<dd>Contains multiple, low priority source configuration files as explained in section SOURCE CONFIGURATION. Please pay attention to the specific meanings of the respective subdirectories.</dl>
<p> /etc/pki/ca-trust/source</p>
<dl>
<dd>Contains multiple, high priority source configuration files as explained in section SOURCE CONFIGURATION. Please pay attention to the specific meanings of the respective subdirectories.</dl>
<p> /etc/pki/ca-trust/extracted</p>
<dl>
<dd>Contains consolidated and automatically generated configuration files for consumption by applications, which are created using the <i>update-ca-trust extract</i> command. Don&#8217;t edit files in this directory, because they will be overwritten. See section EXTRACTED CONFIGURATION for additional details.</dl>
<h2>Author</h2>
<p>Written by Kai Engert and Stef Walter.</p>
