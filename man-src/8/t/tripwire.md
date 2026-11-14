---
title: "tripwire(8)"
name: "tripwire"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tripwire/"
description: "tripwire – a file integrity checker for UNIX systems"
---

<p>tripwire &#8211; a file integrity checker for <font SIZE="-1">UNIX</font> systems</p>
<h2>Synopsis</h2>
<p><code>tripwire</code> { <code>-m i</code> | <code>&#8211;init</code> } [ <i>options&#8230;</i> ]<br />
 <code>tripwire</code> { <code>-m c</code> | <code>&#8211;check</code> } [ <i>options&#8230;</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <i>object1</i> [ <i>object2&#8230;</i> ]]<br />
 <code>tripwire</code> { <code>-m u</code> | <code>&#8211;update</code> } [ <i>options&#8230;</i> ]<br />
 <code>tripwire</code> { <code>-m p</code> | <code>&#8211;update-policy</code> } [ <i>options&#8230;</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>policyfile.txt</i><br />
 <code>tripwire</code> { <code>-m t</code> | <code>&#8211;test</code> } [ <i>options&#8230;</i> ]</p>
<h2>Description</h2>
<h3>Database Initialization Mode</h3>
<p>Running <code>tripwire</code> in Database Initialization mode is typically one of the first steps in setting up <i>Tripwire</i> for regular operation. This mode creates a baseline database in the location specified by the <tt>DBFILE</tt> variable in the <i>Tripwire</i> configuration file. The database is essentially a snapshot of the objects residing on the system. During later <i>Tripwire</i> integrity checks, this database serves as the basis for comparison. </p>
<p> When run in Database Initialization mode, <code>tripwire</code> reads the policy file, generates a database based on its contents, and then cryptographically signs the resulting database. Options can be entered on the command line to specify which policy, configuration, and key files are used to create the database. The filename for the database can be specified as well. If no options are specified, the default values from the current configuration file are used.</p>
<h3>Integrity Checking Mode</h3>
<p>After building the <i>Tripwire</i> database, the next step is typically to run <code>tripwire</code> in Integrity Checking mode. This mode scans the system for violations, as specified in the policy file. Using the policy file rules, <i>Tripwire</i> will compare the state of the current file system against the initial baseline database. An integrity checking report is printed to <i>stdout</i> and is saved in the location specified by the <tt>REPORTFILE</tt> setting in the <i>Tripwire</i> configuration file. </p>
<p> The generated report describes each policy file violation in detail, depending on whether the specified file system object was added, deleted, or changed. Each report item lists the properties of the object as it currently resides on the file system, and, if appropriate, the old value stored in the database. If there are differences between the database and the current system, the administrator can either fix the problem by replacing the current file with the correct file (e.g., an intruder replaced <i>/bin/login</i>), or update the database to reflect the new file (e.g., a fellow system administrator installed a new version of <i>/usr/local/bin/emacs</i>). The (<code>-I</code> or <code>&#8211;interactive</code>) option launches an editor that allows the user to update the database quickly. The Database Update mode of <code>tripwire</code> can also be used.</p>
<h3>Database Update Mode</h3>
<p>Running <code>tripwire</code> in Database Update mode allows any differences between the database and the current system to be reconciled. This will prevent the violation from showing up in future reports. If the reported change is unexpected and potentially malicious, then the changed file should be replaced with the original version. If there is a valid reason for the change, the database must be changed to match the current files. </p>
<p> In Database Update mode, the items to be changed are specified in a &quot;ballot box&quot; in the plain text report that is launched in an editor program. The entries to be updated are specified by leaving the &quot;x&quot; next to each policy violation. After the user exits the editor and provides the correct local passphrase, <code>tripwire</code> will update the database. Options to control this operation include the (<code>-Z</code>&nbsp;<wbr>or&nbsp;<wbr><code>&#8211;secure-mode</code>) and (<code>-a</code>&nbsp;<wbr>or&nbsp;<wbr><code>&#8211;accept-all</code>) flags.</p>
<h3>Policy Update Mode</h3>
<p>Policy update mode is used by <code>tripwire</code> to change or update the policy file and to synchronize an earlier database with new policy file information. The filename of the new clear text version of the policy file is specified on the command line. The new policy file is compared to the existing version, and the database is updated according to the new policy rules. Any changes in the database since the last integrity check will be detected and reported. How these violations are interpreted depends on the security mode specified with the (<code>-Z</code> or <code>&#8211;secure-mode</code>) option. In <code>high</code> security mode (the default), <i>Tripwire</i> will print a list of violations and exit without making changes to the database. In <code>low</code> security mode, the violations are still reported, but changes to the database are made automatically. </p>
<p> Because the policy and database files are binary-encoded and cryptographically signed, the user will be prompted for the site and local passphrases to change the policy settings. After the database is successfully updated, the database and policy files are re-encoded and signed.</p>
<h3>Test Mode</h3>
<p>Test mode is used to check the operation of the <i>Tripwire</i> email notification system. When run in this mode, <i>Tripwire</i> will use the email notification settings specified in the configuration file to send a test email message. If MAILMETHOD is set to SMTP, the SMTPHOST and SMTPPORT values will be used to send email. If MAILMETHOD is set to SENDMAIL, the MAILPROGRAM value will be used. If email notification is working correctly, the address specified on the command line will receive the following message: </p>
<pre><FONT SIZE="-1">To: user [at] domain.com 
From: user &lt;user [at] domain.com&gt; 
Subject: Test email message from Tripwire 
If you receive this message, email notification
from Tripwire is working correctly.
</FONT></pre>
<p>Test mode only tests email notification for the address specified on the command-line, and does not check for errors in the syntax used with the <tt>emailto</tt> attribute in the policy file.</p>
<h2>Options</h2>
<h3>Database Initialization mode:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m i</code></td>
<td><code>&#8211;init</code>
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
<td><code>-d <i>database</i></code></td>
<td><code>&#8211;dbfile <i>database</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-P <i>passphrase</i></code></td>
<td><code>&#8211;local-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-e</code></td>
<td><code>&#8211;no-encryption</code>
</td>
</tr>
</table>
</dl>
<dl>
<dt><code>-m i</code>, <code>&#8211;init</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-p</code><i> polfile</i>, <code>&#8211;polfile</code><i> polfile</i></p>
<dd>Use the specified policy file.</p>
<dt><code>-d</code><i> database</i>, <code>&#8211;dbfile</code><i> database</i></p>
<dd>Write to the specified database file.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Use the specified site key file to read the configuration and policy files.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Use the specified local key file to write the new database file. Mutually exclusive with (<code>-e</code>).</p>
<dt><code>-P</code><i> passphrase</i>, <code>&#8211;local-passphrase</code><i> passphrase</i></p>
<dd>Specifies passphrase to be used with local key to sign the new database. Mutually exclusive with (<code>-e</code>).</p>
<dt><code>-e</code>, <code>&#8211;no-encryption</code></p>
<dd>Do not sign the database being stored. The database file will still be compressed and will not be human-readable. Mutually exclusive with (<code>-L</code>) and (<code>-P</code>). </p>
<hr>
</dl>
<h3>Integrity Checking mode:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m c</code></td>
<td><code>&#8211;check</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-I</code></td>
<td><code>&#8211;interactive</code>
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
<td><code>-d <i>database</i></code></td>
<td><code>&#8211;dbfile <i>database</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-r <i>report</i></code></td>
<td><code>&#8211;twrfile <i>report</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-P <i>passphrase</i></code></td>
<td><code>&#8211;local-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-n</code></td>
<td><code>&#8211;no-tty-output</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-V <i>editor</i></code></td>
<td><code>&#8211;visual <i>editor</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-E</code></td>
<td><code>&#8211;signed-report</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-i <i>list</i></code></td>
<td><code>&#8211;ignore <i>list</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-l { <i>level</i> | <i>name</i> }</code></td>
<td><code>&#8211;severity { <i>level</i> | <i>name</i> }</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-R <i>rule</i></code></td>
<td><code>&#8211;rule-name <i>rule</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-x <i>section</i></code></td>
<td><code>&#8211;section <i>section</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-M</code></td>
<td><code>&#8211;email-report</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-t { 0|1|2|3|4 }</code></td>
<td><code>&#8211;email-report-level { 0|1|2|3|4 }</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-h</code></td>
<td><code>&#8211;hexadecimal</code>
</td>
</tr>
</table>
<p> [ <i>object1</i> [ <i>object2&#8230;</i> ]]</dl>
<dl>
<dt><code>-m c</code>, <code>&#8211;check</code></p>
<dd>Mode selector.</p>
<dt><code>-I</code>, <code>&#8211;interactive</code></p>
<dd>At the end of integrity checking, the resulting report is opened in an editor where database updates can be easily specified using the ballot boxes included in the report.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-p</code><i> polfile</i>, <code>&#8211;polfile</code><i> polfile</i></p>
<dd>Use the specified policy file.</p>
<dt><code>-d</code><i> database</i>, <code>&#8211;dbfile</code><i> database</i></p>
<dd>Use the specified database file.</p>
<dt><code>-r</code><i> report</i>, <code>&#8211;twrfile</code><i> report</i></p>
<dd>Write the specified report file.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Use the specified site key file to read the configuration and policy files.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Use the specified local key file to read the database file and, if (<code>-E</code>) is specified, to write the report file.</p>
<dt><code>-P</code><i> passphrase</i>, <code>&#8211;local-passphrase</code><i> passphrase</i></p>
<dd>Specifies passphrase to be used with local key to sign the database when (<code>-I</code>) is used, and to sign the report when (<code>-E</code>) is used. Valid only with (<code>-I</code>) or (<code>-E</code>).</p>
<dt><code>-n</code>, <code>&#8211;no-tty-output</code></p>
<dd>Suppress the report from being printed at the console.</p>
<dt><code>-V</code><i> editor</i>, <code>&#8211;visual</code><i> editor</i></p>
<dd>Use the specified editor to edit the update ballot boxes. Meaningful only with (<code>-I</code>).</p>
<dt><code>-E</code>, <code>&#8211;signed-report</code></p>
<dd>Specifies that the <i>Tripwire</i> report will be signed. If no passphrase is specified on the command line, <code>tripwire</code> will prompt for the local passphrase.</p>
<dt><code>-i</code><i> list</i>, <code>&#8211;ignore</code><i> list</i></p>
<dd>Do not compute or compare the properties specified in <i>list</i>. Any of the letter codes (abcdgimnprstulCHMS) specified in propertymasks can be excluded. Use of this option overrides information from the policy file. The format to be used for <i>list</i> is a double-quoted, comma-delimited list of properties (e.g.&nbsp;<wbr><i>&#8211;ignore&nbsp;<wbr>&quot;p,c,m&quot;</i>).</p>
<dt><code>-l </code>{ <i>level </i>| <i>name </i>}, <code>&#8211;severity </code>{ <i>level </i>| <i>name </i>}</p>
<dd>Check only policy rules with severity greater than or equal to the given level. The level may be specified as a number or as a name. Severity names are defined as follows: </p>
<pre> Low 33
 Medium 66
 High 100</pre>
<p>Mutually exclusive with (<code>-R</code>).</p>
<dt><code>-R</code><i> rule</i>, <code>&#8211;rule-name</code><i> rule</i></p>
<dd>Check only the specified policy rule. Mutually exclusive with (<code>-l</code>).</p>
<dt><code>-x</code><i> section</i>, <code>&#8211;section</code><i> section</i></p>
<dd>Only check the rules in the specified section of the policy file. For <i>Tripwire 2.4</i>, <tt>FS</tt> is the only meaningful argument for this flag.</p>
<dt><code>-M</code>, <code>&#8211;email-report</code></p>
<dd>Specifies that reports be emailed to the recipient(s) designated in the policy file.</p>
<dt><code>-t</code><i> level</i>, <code>&#8211;email-report-level</code><i> level</i></p>
<dd>Specifies the detail level of email reports, overriding the EMAILREPORTLEVEL variable in the configuration file. <i>level</i> must be a number from 0 to 4. Valid only with (<code>-M</code>).</p>
<dt><code>-h</code>, <code>&#8211;hexadecimal</code></p>
<dd>Display hash values as hexadecimal in email reports</p>
<dt>[ <i>object1</i> [ <i>object2&#8230;</i> ]]</p>
<dd>List of files and directories that should be integrity checked. Default is all files. If files are specified for checking, the <code>&#8211;severity</code> and <code>&#8211;rule-name</code> options will be ignored. </p>
<hr>
</dl>
<h3>Database Update mode:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m u</code></td>
<td><code>&#8211;update</code>
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
<td><code>-d <i>database</i></code></td>
<td><code>&#8211;dbfile <i>database</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-r <i>report</i></code></td>
<td><code>&#8211;twrfile <i>report</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-P <i>passphrase</i></code></td>
<td><code>&#8211;local-passphrase <i>passphrase</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-V <i>editor</i></code></td>
<td><code>&#8211;visual <i>editor</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-a</code></td>
<td><code>&#8211;accept-all</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-Z { low | high }</code></td>
<td><code>&#8211;secure-mode { low | high }</code>
</td>
</tr>
</table>
</dl>
<dl>
<dt><code>-m u</code>, <code>&#8211;update</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-p</code><i> polfile</i>, <code>&#8211;polfile</code><i> polfile</i></p>
<dd>Use the specified policy file.</p>
<dt><code>-d</code><i> database</i>, <code>&#8211;dbfile</code><i> database</i></p>
<dd>Update the specified database file.</p>
<dt><code>-r</code><i> report</i>, <code>&#8211;twrfile</code><i> report</i></p>
<dd>Read the specified report file.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Use the specified site key file to read the configuration and policy files.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Use the specified local key file to read the database file and report file, and to re-write the database file.</p>
<dt><code>-P</code><i> passphrase</i>, <code>&#8211;local-passphrase</code><i> passphrase</i></p>
<dd>Specifies passphrase to be used with local key to sign the database.</p>
<dt><code>-V</code><i> editor</i>, <code>&#8211;visual</code><i> editor</i></p>
<dd>Use the specified editor to edit the update ballot boxes. Mutually exclusive with (<code>-a</code>).</p>
<dt><code>-a</code>, <code>&#8211;accept-all</code></p>
<dd>Specifies that all the entries in the report file are updated without prompting. Mutually exclusive with (<code>-V</code>).</p>
<dt><code>-Z </code>{ low | high }, <code>&#8211;secure-mode </code>{ low | high }</p>
<dd>Specifies the security level, which affects how certain conditions are handled when inconsistent information is found between the report file and the current database: </p>
<p> High: In <code>high</code> security mode, if a file does not match the properties in the report file, Tripwire reports the differences as warnings, and exits without changing the database. </p>
<p> Low: In <code>low</code> security mode, inconsistencies are reported as warnings, but the changes are still made to the database. </p>
<hr>
</dl>
<h3>Policy Update mode:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m p</code></td>
<td><code>&#8211;update-policy</code>
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
<td><code>-d <i>database</i></code></td>
<td><code>&#8211;dbfile <i>database</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-S <i>sitekey</i></code></td>
<td><code>&#8211;site-keyfile <i>sitekey</i></code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-L <i>localkey</i></code></td>
<td><code>&#8211;local-keyfile <i>localkey</i></code>
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
<td><code>-Z { low | high }</code></td>
<td><code>&#8211;secure-mode { low | high }</code>
</td>
</tr>
</table>
<p> <i>policyfile.txt</i></dl>
<dl>
<dt><code>-m p</code>, <code>&#8211;update-policy</code></p>
<dd>Mode selector.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output mode. Mutually exclusive with (<code>-s</code>).</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd>Silent output mode. Mutually exclusive with (<code>-v</code>).</p>
<dt><code>-c</code><i> cfgfile</i>, <code>&#8211;cfgfile</code><i> cfgfile</i></p>
<dd>Use the specified configuration file.</p>
<dt><code>-p</code><i> polfile</i>, <code>&#8211;polfile</code><i> polfile</i></p>
<dd>Write the specified policy file.</p>
<dt><code>-d</code><i> database</i>, <code>&#8211;dbfile</code><i> database</i></p>
<dd>Use the specified database file.</p>
<dt><code>-S</code><i> sitekey</i>, <code>&#8211;site-keyfile</code><i> sitekey</i></p>
<dd>Use the specified site key file to read the configuration file, and read and write the policy file.</p>
<dt><code>-L</code><i> localkey</i>, <code>&#8211;local-keyfile</code><i> localkey</i></p>
<dd>Use the specified local key file to read and write the database file.</p>
<dt><code>-P</code><i> passphrase</i>, <code>&#8211;local-passphrase</code><i> passphrase</i></p>
<dd>Specifies passphrase to be used with local key to sign the database.</p>
<dt><code>-Q</code><i> passphrase</i>, <code>&#8211;site-passphrase</code><i> passphrase</i></p>
<dd>Specifies passphrase to be used with site key to sign the new policy file.</p>
<dt><code>-Z </code>{ low | high }, <code>&#8211;secure-mode </code>{ low | high }</p>
<dd>Specifies the security level, which affects how certain conditions are handled when the existing filesystem does not match the database information. Since the database produced at the end of a policy update becomes the baseline for future integrity checks, this consistency-checking ensures that no substantive filesystem changes have occurred since the last integrity check. </p>
<p> High: In <code>high</code> security mode, if a file on the filesystem does not match the properties in the database file, Tripwire reports the differences as warnings, and exits without changing the database or the policy file. </p>
<p> Low: In <code>low</code> security mode, inconsistencies are reported as warnings, but the changes are still made to the database and policy file.</p>
<dt><i>policyfile.txt</i></p>
<dd>Specifies the text policy file that will become the new policy file. </p>
<hr>
</dl>
<h3>Test mode:</h3>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>-m t</code></td>
<td><code>&#8211;test</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>-e <i>user [at] domain.com</i></code></td>
<td><code>&#8211;email <i>user [at] domain.com</i></code>
</td>
</tr>
</table>
</dl>
<dl>
<dt><code>-m t</code>, <code>&#8211;test</code></p>
<dd>Mode selector.</p>
<dt><code>-e</code><i> user [at] domain.com</i>, <code>&#8211;email</code><i> user [at] domain.com</i></p>
<dd>Use the specified email address. This parameter must be supplied when test mode is used. Only one address may be specified.</dl>
<h2>Version Information</h2>
<p>This man page describes <code>tripwire</code> version 2.4</p>
<h2>Authors</h2>
<p>Tripwire, Inc.</p>
<h2>Copying Permissions</h2>
<p>Permission is granted to make and distribute verbatim copies of this man page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this man page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this man page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by Tripwire, Inc. </p>
<p> Copyright 2000-2017 Tripwire, Inc. Tripwire is a registered trademark of Tripwire, Inc. in the United States and other countries. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-twintro/">twintro</a></code>(8), <code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8), <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8), <code><a href="/docs/linux/man/8-siggen/">siggen</a></code>(8), <code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4), <code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4), <code><a href="/docs/linux/man/5-twfiles/">twfiles</a></code>(5) <i>The Design and Implementation of Tripwire: A </i><font SIZE="-1"><i>UNIX</i></font><i> File Integrity Checker</i> by Gene Kim and Eugene Spafford. Purdue Technical Report CSD-TR-93-071. </p>
