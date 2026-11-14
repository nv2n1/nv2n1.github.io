---
title: "twadmin(8)"
name: "twadmin"
section: "8"
letter: "t"
url: "/docs/linux/man/8-twadmin/"
description: "twadmin – Tripwire administrative and utility tool"
---

<p>twadmin &#8211; Tripwire administrative and utility tool</p>
<h2>Synopsis</h2>
<p><code>twadmin</code> { <code>-m F</code> | <code>&#8211;create-cfgfile</code> } <i> options&#8230; </i> </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>configfile.txt</i><br />
 <code>twadmin</code> { <code>-m f</code> | <code>&#8211;print-cfgfile</code> } [ <i>options&#8230;</i> ]<br />
 <code>twadmin</code> { <code>-m P</code> | <code>&#8211;create-polfile</code> } [ <i>options&#8230;</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>policyfile.txt</i><br />
 <code>twadmin</code> { <code>-m p</code> | <code>&#8211;print-polfile</code> } [ <i>options&#8230;</i> ]<br />
 <code>twadmin</code> { <code>-m R</code> | <code>&#8211;remove-encryption</code> } [ <i>options&#8230;</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>file1</i> [ <i>file2&#8230;</i> ]<br />
 <code>twadmin</code> { <code>-m E</code> | <code>&#8211;encrypt</code> } [ <i>options&#8230;</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>file1</i> [ <i>file2&#8230;</i> ]<br />
 <code>twadmin</code> { <code>-m e</code> | <code>&#8211;examine</code> } [ <i>options&#8230;</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>file1</i> [ <i>file2&#8230;</i> ]<br />
 <code>twadmin</code> { <code>-m G</code> | <code>&#8211;generate-keys</code> } <i>options&#8230;</i><br />
 <code>twadmin</code> { <code>-m C</code> | <code>&#8211;change-passphrases</code> } <i>options&#8230;</i></p>
<h2>Description</h2>
<p>The <code>twadmin</code> utility is used to perform certain administrative functions related to <i>Tripwire</i> files and configuration options. Specifically, <code>twadmin</code> allows encoding, decoding, signing, and verification of <i>Tripwire</i> files, and provides a means to generate and change local and site keys.</p>
<h3>Creating a configuration file (&#8211;create-cfgfile)</h3>
<p>This command mode designates an existing text file as the new configuration file for <i>Tripwire</i>. The plain text configuration file must be specified on the command line. Using the site key, the new configuration file is encoded and saved.</p>
<h3>Printing a configuration file (&#8211;print-cfgfile)</h3>
<p>This command mode prints the specified encoded and signed configuration file in clear-text form to standard output.</p>
<h3>Replacing a policy file (&#8211;create-polfile)</h3>
<p>This command mode designates an existing text file as the new policy file for <i>Tripwire</i>. The plain text policy file must be specified on the command line. Using the site key, the new policy file is encoded and saved.</p>
<h3>Printing a policy file (&#8211;print-polfile)</h3>
<p>This command mode prints the specified encoded and signed policy file in clear-text form to standard output.</p>
<h3>Removing encryption from a file (&#8211;remove-encryption)</h3>
<p>This command mode allows the user to remove signing from signed configuration, policy, database, or report files. Multiple files may be specified on the command line. The user will need to enter the appropriate local or site keyfile, or both if a combination of files is to be verified. Even with the cryptographic signing removed, these files will be in a binary encoded (non-human-readable) form.</p>
<h3>Encrypting a file (&#8211;encrypt)</h3>
<p>This command mode allows the user to sign configuration, policy, database files, or reports. Multiple files may be specified on the command line. The files will be signed using either the site or local key, as appropriate for the type of file. To automate the process, the passphrase for the key files can be included on the command line.</p>
<h3>Examining the signing status of a file (&#8211;examine)</h3>
<p>This command allows the user to examine the listed files and print a report of their signing status. This report displays the filename, file type, whether or not a file is signed, and what key (if any) is used to sign it.</p>
<h3>Generating keys (&#8211;generate-keys)</h3>
<p>This command mode generates site and/or local key files with names specified by the user.</p>
<h3>Changing passphrases (&#8211;change-passphrases)</h3>
<p>This command reencrypts the private part of the site and/or local key files using the key filenames and passphrases specified by the user.</p>
<h2>Options</h2>
<h3>Creating a configuration file:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m F</code></td>
<td><code>&#8211;create-cfgfile</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-Q <i>passphrase</i></code></td>
<td><code>&#8211;site-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-e</code></td>
<td><code>&#8211;no-encryption</code>
</td>
</tr>
</table>
<p> <i>configfile.txt</i></dl>
<dl>
<dt><code>-m F</code>, <code>&#8211;create-cfgfile</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Specify the destination of the encoded (and optionally signed) configuration file.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Use the specified site key file to encode and sign the new configuration file. Exactly one of (<code>-S</code>) or (<code>-e</code>) must be specified.</p>
<dt><code>-Q</code><i> passphrase</i>, <code>&#8211;site-passphrase</code><i> passphrase</i></p>
<dd>Specifies passphrase to be used with site key for configuration file encoding and signing. Valid only in conjunction with (<code>-S</code>).</p>
<dt><code>-e</code>, <code>&#8211;no-encryption</code></p>
<dd>Do not sign the configuration file being stored. The configuration file will still be compressed, and will not be human-readable. Mutually exclusive with (<code>-Q</code>) and (<code>-S</code>).</p>
<dt><i>configfile.txt</i></p>
<dd>Specifies the text configuration file that will become the new configuration file. </p>
<hr>
</dl>
<h3>Printing a configuration file:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m f</code></td>
<td><code>&#8211;print-cfgfile</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
</table>
</dl>
<dl>
<dt><code>-m f</code>, <code>&#8211;print-cfgfile</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Print the specified configuration file. </p>
<hr>
</dl>
<h3>Creating a policy file:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m P</code></td>
<td><code>&#8211;create-polfile</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-p <i>polfile</i></code></td>
<td><code>&#8211;polfile <i>polfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-Q <i>passphrase</i></code></td>
<td><code>&#8211;site-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-e</code></td>
<td><code>&#8211;no-encryption</code>
</td>
</tr>
</table>
<p> <i>policyfile.txt</i></dl>
<dl>
<dt><code>-m P</code>, <code>&#8211;create-polfile</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-p</code><i> polfile</i>, <code>&#8211;polfile</code><i> polfile</i></p>
<dd>Specify the destination of the encoded (and optionally signed) policy file.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Use the specified site key file. Mutually exclusive with (<code>-e</code>).</p>
<dt><code>-Q</code><i> passphrase</i>, <code>&#8211;site-passphrase</code><i> passphrase</i></p>
<dd>Specifies passphrase to be used with site key for policy signing. Mutually exclusive with (<code>-e</code>).</p>
<dt><code>-e</code>, <code>&#8211;no-encryption</code></p>
<dd>Do not sign the policy file being stored. The policy file will still be compressed, and will not be human-readable. Mutually exclusive with (<code>-Q</code>) and (<code>-S</code>).</p>
<dt><i>policyfile.txt</i></p>
<dd>Specifies the text policy file that will become the new policy file. </p>
<hr>
</dl>
<h3>Printing a policy file:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m p</code></td>
<td><code>&#8211;print-polfile</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-p <i>polfile</i></code></td>
<td><code>&#8211;polfile <i>polfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
</table>
</dl>
<dl>
<dt><code>-m p</code>, <code>&#8211;print-polfile</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-p</code><i> polfile</i>, <code>&#8211;polfile</code><i> polfile</i></p>
<dd>Print the specified policy file.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Use the specified site key file. </p>
<hr>
</dl>
<h3>Removing encryption from a file:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m R</code></td>
<td><code>&#8211;remove-encryption</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-P <i>passphrase</i></code></td>
<td><code>&#8211;local-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-Q <i>passphrase</i></code></td>
<td><code>&#8211;site-passphrase <i>passphrase</i></code>
</td>
</tr>
</table>
<p> <i>file1</i> [ <i>file2&#8230;</i> ]</dl>
<dl>
<dt><code>-m R</code>, <code>&#8211;remove-encryption</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Specify the local keyfile to use to verify database files and reports.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Specify the site keyfile to use to verify configuration and policy files.</p>
<dt><code>-P</code><i> passphrase</i>, <code>&#8211;local-passphrase</code><i> passphrase</i></p>
<dd>Specify the passphrase to use when verifying with the old local keyfile.</p>
<dt><code>-Q</code><i> passphrase</i>, <code>&#8211;site-passphrase</code><i> passphrase</i></p>
<dd>Specify the passphrase to use when verifying with the old site keyfile.</p>
<dt><i>file1</i> [ <i>file2&#8230;</i> ]</p>
<dd>List of files from which signing is to be removed. </p>
<hr>
</dl>
<h3>Encrypting a file:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m E</code></td>
<td><code>&#8211;encrypt</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-P <i>passphrase</i></code></td>
<td><code>&#8211;local-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-Q <i>passphrase</i></code></td>
<td><code>&#8211;site-passphrase <i>passphrase</i></code>
</td>
</tr>
</table>
<p> <i>file1</i> [ <i>file2&#8230;</i> ]</dl>
<dl>
<dt><code>-m E</code>, <code>&#8211;encrypt</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Specify the local keyfile to use to sign database files and reports.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Specify the site keyfile to use to sign configuration and policy files.</p>
<dt><code>-P</code><i> passphrase</i>, <code>&#8211;local-passphrase</code><i> passphrase</i></p>
<dd>Specify the passphrase to use when signing with the local keyfile.</p>
<dt><code>-Q</code><i> passphrase</i>, <code>&#8211;site-passphrase</code><i> passphrase</i></p>
<dd>Specify the passphrase to use when signing with the site keyfile.</p>
<dt><i>file1</i> [ <i>file2&#8230;</i> ]</p>
<dd>List of files to sign using the new key(s). </p>
<hr>
</dl>
<h3>Examining the encryption status of a file:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m e</code></td>
<td><code>&#8211;examine</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-c <i>cfgfile</i></code></td>
<td><code>&#8211;cfgfile <i>cfgfile</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
</table>
<p> <i>file1</i> [ <i>file2&#8230;</i> ]</dl>
<dl>
<dt><code>-m e</code>, <code>&#8211;examine</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Specifies the key to use as a local key.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Specifies the key to use as a site key.</p>
<dt><i>file1</i> [ <i>file2&#8230;</i> ]</p>
<dd>List of files to examine. </p>
<hr>
</dl>
<h3>Generating keys:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m G</code></td>
<td><code>&#8211;generate-keys</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-P <i>passphrase</i></code></td>
<td><code>&#8211;local-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-Q <i>passphrase</i></code></td>
<td><code>&#8211;site-passphrase <i>passphrase</i></code>
</td>
</tr>
</table>
</dl>
<dl>
<dt><code>-m G</code>, <code>&#8211;generate-keys</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Generate the local key into the specified file. At least one of (<code>-L</code>) or (<code>-S</code>) must be specified.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Generate the site key into the specified file. At least one of (<code>-S</code>) or (<code>-L</code>) must be specified.</p>
<dt><code>-P</code><i> passphrase</i>, <code>&#8211;local-passphrase</code><i> passphrase</i></p>
<dd>Specify local passphrase to be used when generating the local key.</p>
<dt><code>-Q</code><i> passphrase</i>, <code>&#8211;site-passphrase</code><i> passphrase</i></p>
<dd>Specify site passphrase to be used when generating the site key.</p>
<dt><code>-K</code><i> size</i>, <code>&#8211;key-size</code><i> size</i></p>
<dd>Specify the key size (1024 or 2048 bits) when generating keys. (Default is 1024.) </p>
<hr>
</dl>
<h3>Changing passphrases:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m C</code></td>
<td><code>&#8211;change-passphrases</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-v</code></td>
<td><code>&#8211;verbose</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td><code>&#8211;silent, &#8211;quiet</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-P <i>passphrase</i></code></td>
<td><code>&#8211;local-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-Q <i>passphrase</i></code></td>
<td><code>&#8211;site-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>&#8211;local-passphrase-old <i>passphraseOld</i></code>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>&#8211;site-passphrase-old <i>passphraseOld</i></code>
</td>
</tr>
</table>
</dl>
<dl>
<dt><code>-m C</code>, <code>&#8211;change-passphrases</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Change passphrase used to encrypt the private key in the specified localkey file. At least one of (<code>-L</code>) or (<code>-S</code>) must be specified.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Change passphrase used to encrypt the private key in the specified sitekey file. At least one of (<code>-L</code>) or (<code>-S</code>) must be specified.</p>
<dt><code>-P</code><i> passphrase</i>, <code>&#8211;local-passphrase</code><i> passphrase</i></p>
<dd>Specify passphrase used to encrypt the private key in the specified localkey file.</p>
<dt><code>-Q</code><i> passphrase</i>, <code>&#8211;site-passphrase</code><i> passphrase</i></p>
<dd>Specify passphrase used to encrypt the private key in the specified sitekey file.</p>
<dt><code>&#8211;local-passphrase-old</code><i> passphraseOld</i></p>
<dd>Specify passphrase used to decrypt the private key in the specified localkey file.</p>
<dt><code>&#8211;site-passphrase-old</code><i> passphraseOld</i></p>
<dd>Specify passphrase used to decrypt the private key in the specified sitekey file.</dl>
<h2>Version Information</h2>
<p>This man page describes <code>twadmin</code> version 2.4.</p>
<h2>Authors</h2>
<p>Tripwire, Inc.</p>
<h2>Copying Permissions</h2>
<p>Permission is granted to make and distribute verbatim copies of this man page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this man page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this man page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by Tripwire, Inc. </p>
<p> Copyright 2000-2017 Tripwire, Inc. Tripwire is a registered trademark of Tripwire, Inc. in the United States and other countries. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-twintro/">twintro</a></code>(8), <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8), <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8), <code><a href="/docs/linux/man/8-siggen/">siggen</a></code>(8), <code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4), <code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4), <code><a href="/docs/linux/man/5-twfiles/">twfiles</a></code>(5) </p>
