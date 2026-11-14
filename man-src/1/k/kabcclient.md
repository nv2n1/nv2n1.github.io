---
title: "kabcclient(1)"
name: "kabcclient"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kabcclient/"
description: "kabcclient – commandline client for the KDE addressbook"
---

<h2 class="name">NAME</h2>
<p> kabcclient &#8211; commandline client for the KDE addressbook </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kabcclient</code> [[-A] | [-R] | [-M] | [-S] | [-L]] [&#8211;match-case] [&#8211;nosave] [-ic&nbsp;<wbr><i>codec</i>] [-if&nbsp;<wbr><i>format</i>] [-if-opts&nbsp;<wbr><i>format-options</i>] [-oc&nbsp;<wbr><i>codec</i>] [-of&nbsp;<wbr><i>format</i>] [-of-opts&nbsp;<wbr><i>format-options</i>] [input-data]</dl>
<h2>DESCRIPTION</h2>
<p> <code>kabcclient</code></p>
<dd>allows commandline access to the KDE addressbook, for example in shell scripts. It supports input from stdin or through additional commandline arguments. Output is always written to stdout.</p>
<h2>OPTIONS</h2>
<p> <i>Operation modes</i></p>
<dl>
<dt>
<dd>
<p> <code>-A, &#8211;add</code></p>
<dl>
<dt>
<dd> Add a new contact entry to the addressbook</dl>
<p> <code>-R, &#8211;remove</code></p>
<dl>
<dt>
<dd> Removes an existing contact entry from the addressbook</dl>
<p> <code>-M, &#8211;merge</code></p>
<dl>
<dt>
<dd> Merges input data with an existing contact entry from the addressbook. This appends any new information to the already existing one</dl>
<p> <code>-S, &#8211;search</code></p>
<dl>
<dt>
<dd> Searches the addressbook for matching contact entries</dl>
<p> <code>-L, &#8211;list</code></p>
<dl>
<dt>
<dd> Lists all contact entries of the addressbook</dl>
</dl>
<p> <i>Input options</i></p>
<dl>
<dt>
<dd>
<p> <code>-ic, &#8211;input-codec</code></p>
<dl>
<dt>
<dd> Pass input text through a specified text encoding. See <code>-ic</code><i> help</i> for additional information about input codecs. Default is <i>local</i> which will use the codec for the current <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5) settings</dl>
<p> <code>-if, &#8211;input-format</code></p>
<dl>
<dt>
<dd> Parses the input text according to given formatting rules. See <code>-if</code><i> help</i> for available formats. Default is <i>search</i></dl>
<p> Instead of reading input text kabcclient can show a dialog for selecting contacts using the input format</p>
<dl>
<dt>
<dd> <i>dialog</i></dl>
<p> <code>-if-opts, &#8211;input-format-options</code></p>
<dl>
<dt>
<dd> Additional options for the chosen input format. Can be optional as well as mandatory depending on the format. See <code>-if-opts</code><i> help</i> for available format options</dl>
</dl>
<p> <i>Output options</i></p>
<dl>
<dt>
<dd>
<p> <code>-oc, &#8211;output-codec</code></p>
<dl>
<dt>
<dd> Pass output text through a specified text encoding. See <code>-oc</code><i> help</i> for additional information about output codecs. Default is <i>local</i> which will use the codec for the current <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5) settings.</dl>
<p> <code>-of, &#8211;output-format</code></p>
<dl>
<dt>
<dd> Formats the output text according to given formatting rules. See <code>-of</code><i> help</i> for available formats. Default is <i>vcard</i></dl>
<p> <code>-of-opts, &#8211;output-format-options</code></p>
<dl>
<dt>
<dd> Additional options for the chosen output format. Can be optional as well as mandatory depending on the format. See <code>-of-opts</code><i> help</i> for available format options</dl>
</dl>
<p> <i>Additional options</i></p>
<dl>
<dt>
<dd>
<p> <code>&#8211;match-case</code></p>
<dl>
<dt>
<dd> Use case sensitive text matching when comparing input text with contact entries</dl>
<p> <code>&#8211;nosave</code></p>
<dl>
<dt>
<dd> Perform information changing operations like <code>-A, -R</code> or <code>-M</code> only in memory but do not write the changes back to the addressbook</dl>
</dl>
<h2>DIAGNOSTICS</h2>
<p> As usual an exit status of zero indicates success. Depending on the chosen operation mode a non-zero exit status indicates a certain problem the application encountered </p>
<p> <i>ADD</i></p>
<dl>
<dt>
<dd>
<p> 1</p>
<dl>
<dt>
<dd> Reading the input text failed</dl>
<p> 2</p>
<dl>
<dt>
<dd> Creating a suitable contact entry from the input text failed, e.g. not data or wrongly formatted input for the chosen input format</dl>
<p> 3</p>
<dl>
<dt>
<dd> Saving the addressbook changes failed. This can be caused for example by other applications currently locking the addressbook.</dl>
</dl>
<p> <i>REMOVE</i></p>
<dl>
<dt>
<dd>
<p> 1</p>
<dl>
<dt>
<dd> Reading the input text failed</dl>
<p> 2</p>
<dl>
<dt>
<dd> The program could not remove any contact entry from the addressbook. This can be caused by failing to parse the input text, failing to find a matching contact entry in the addressbook or finding more than one matching contact entry in the addressbook. In the latter case an error message is written to stderr</dl>
<p> 3</p>
<dl>
<dt>
<dd> Saving the addressbook changes failed. This can be caused for example by other applications currently locking the addressbook.</dl>
</dl>
<p> <i>MERGE</i></p>
<dl>
<dt>
<dd>
<p> 1</p>
<dl>
<dt>
<dd> Reading the input text failed</dl>
<p> 2</p>
<dl>
<dt>
<dd> The program could not merge the input with any contact entry from the addressbook. This can be caused by failing to parse the input text, failing to find a matching contact entry in the addressbook or finding more than one matching contact entry in the addressbook. In the latter case an error message is written to stderr</dl>
<p> 3</p>
<dl>
<dt>
<dd> Saving the addressbook changes failed. This can be caused for example by other applications currently locking the addressbook.</dl>
<p> <i>SEARCH</i>, 1</p>
<dl>
<dt>
<dd> Reading the input text failed</dl>
<p> 2</p>
<dl>
<dt>
<dd> The program could not find any matching contact entry in the addressbook. This can be caused by failing to parse the input text or failing to find a matching contact entry in the addressbook</dl>
</dl>
<h2>EXAMPLES</h2>
<p> <i>Look for contact entries with Joe in either name or email addresses</i> </p>
<dl>
<dt>
<dd>
<pre>
kabcclient -S Joe
</pre>
</dl>
<p> <i>Do the same but use case sensitive matching</i> </p>
<dl>
<dt>
<dd>
<pre>
kabcclient --match-case -S Joe
</pre>
</dl>
<p> <i>Do the same but read input text from stdin</i> </p>
<dl>
<dt>
<dd>
<pre>
echo &quot;Joe&quot; | kabcclient --match-case -S
</pre>
</dl>
<p> <i>Try to add a new contact entry using data from a formatted email address</i> </p>
<dl>
<dt>
<dd>
<pre><code>
kabcclient-- nosave-- add - if email "Marilyn Monroe &lt;mmonroe [at] moviestars.com&gt;"
</code></pre>
</dl>
<p> <i>Do the same but this time really save the changed addressbook</i> </p>
<dl>
<dt>
<dd>
<pre><code>
kabcclient-- add - if email "Marilyn Monroe &lt;mmonroe [at] moviestars.com&gt;"
</code></pre>
</dl>
<p> <i>Listing the available input formats</i> </p>
<dl>
<dt>
<dd>
<pre>
kabcclient -if help
</pre>
</dl>
<p> <i>Listing the available output formats</i> </p>
<dl>
<dt>
<dd>
<pre>
kabcclient -of help
</pre>
</dl>
<p> <i>Listing the available options for the &#8217;email&#8217; output format</i> </p>
<dl>
<dt>
<dd>
<pre>
kabcclient -of email -of-opts help
</pre>
</dl>
<p> <i>Listing all email addresses for all contacts containing &#8216;Marilyn&#8217;</i> </p>
<dl>
<dt>
<dd>
<pre>
kabcclient -of email -of-opts allemails -S Marilyn
</pre>
</dl>
<p> <i>Remove all contacts the user selected in the contact selection dialog</i> </p>
<dl>
<dt>
<dd>
<pre>
kabcclient --remove -if dialog
</pre>
</dl>
<p> <i>Export selected contacts to a VCard (default output format) file</i> </p>
<dl>
<dt>
<dd>
<pre>
kabcclient -S -if dialog &gt; contacts.vcf
</pre>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Kevin Krammer &lt;kevin.krammer [at] gmx.at&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>AUTHOR</h2>
<p> <code>Kevin Krammer</code> &lt;kevin.krammer [at] gmx.at&gt;</p>
<dl>
<dt>
<dd> Author</dl>
<h2>Index</h2>
