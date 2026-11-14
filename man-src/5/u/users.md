---
title: "users(5)"
name: "users"
section: "5"
letter: "u"
url: "/docs/linux/man/5-users/"
description: "users – user authorization file for the FreeRADIUS server"
---

<p>users &#8211; user authorization file for the FreeRADIUS server</p>
<h2>Description</h2>
<p>The <code>users</code> files reside in the files module configuration directory, by default <code>/etc/raddb/mods-config/files/</code>. It contains a series of configuration directives which are used by the <i>files</i> module to decide how to authorize and authenticate each user request. Every line starting with a hash sign (&#8216;<code>#</code>&#8216;) is treated as comment and ignored. Each entry of the file begins with a username, followed by a (possibly empty) list of check items, all on one line. The next line begins with a tab, and a (possibly empty) list of reply items. Each item in the check or reply item list is an attribute of the form <code>name = value</code>. Multiple items may be placed on one line, in which case they must be seperated by commas. The reply items may be specified over multiple lines, in which case each line must end with a comma, and the last line of the reply items must not end with a comma. The check items are a list of attributes used to match the incoming request. If the username matches, AND all of the check items match the incoming request, then the reply items are added to the list of attributes which will be used in the reply to that request. This process is repeated for all of the entries in the users file. If the incoming request matches NO entry, then the request is rejected. </p>
<h2>Caveats</h2>
<p>The special username <code>DEFAULT</code> matches any usernames. </p>
<p> The entries are processed in order, from the top of the <code>users</code> file, on down. If an entry contains the special item <code>Fall-Through = No</code> as a reply attribute, then the processing of the file stops, and no more entries are matched. Any reply item list without any <code>Fall-Through</code> attribute is treated as though it included a <code>Fall-Through = No</code> attribute. </p>
<p> If an entry contains the special item <code>Fall-Through = Yes</code> as a reply attribute, then the processing proceeds to the next entry in order. </p>
<p> Care should be taken when using <code>Fall-Through</code>. The server should be tested in debugging mode with a number of test requests, in order to verify that the configured entries behave as expected. </p>
<p> The special attribute <code>Auth-Type</code> is used to identify the authentication type to be used for that user. See the <code>dictionary</code> file for a list of permitted values for the <code>Auth-Type</code> attribute. </p>
<p> Once the <code>users</code> file has been processed, the request is authenticated, using the method given by <code>Auth-Type</code>.</p>
<h2>Operators</h2>
<p>Additional operators other than <code>=</code> may be used for the attributes in either the check item, or reply item list. The following is a list of operators, and their meaning. </p>
<dl>
<dt><code>Attribute = Value</code></p>
<dd>Not allowed as a check item for RADIUS protocol attributes. It is allowed for server configuration attributes (Auth-Type, etc), and sets the value of on attribute, only if there is no other item of the same attribute.<br />
 As a reply item, it means &quot;add the item to the reply list, but only if there is no other item of the same attribute.&quot; </p>
<dt><code>Attribute := Value</code></p>
<dd>Always matches as a check item, and replaces in the configuration items any attribute of the same name. If no attribute of that name appears in the request, then this attribute is added.<br />
 As a reply item, it has an identical meaning, but for the reply items, instead of the request items. </p>
<dt><code>Attribute == Value</code></p>
<dd>As a check item, it matches if the named attribute is present in the request, AND has the given value.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute += Value</code></p>
<dd>Always matches as a check item, and adds the current attribute with value to the list of configuration items.<br />
 As a reply item, it has an identical meaning, but the attribute is added to the reply items. </p>
<dt><code>Attribute != Value</code></p>
<dd>As a check item, matches if the given attribute is in the request, AND does not have the given value.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute &gt; Value</code></p>
<dd>As a check item, it matches if the request contains an attribute with a value greater than the one given.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute &gt;= Value</code></p>
<dd>As a check item, it matches if the request contains an attribute with a value greater than, or equal to the one given.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute &lt; Value</code></p>
<dd>As a check item, it matches if the request contains an attribute with a value less than the one given.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute &lt;= Value</code></p>
<dd>As a check item, it matches if the request contains an attribute with a value less than, or equal to the one given.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute =~ Expression</code></p>
<dd>As a check item, it matches if the request contains an attribute which matches the given regular expression. This operator may only be applied to string attributes.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute !~ Expression</code></p>
<dd>As a check item, it matches if the request contains an attribute which does not match the given regular expression. This operator may only be applied to string attributes.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute =* Value</code></p>
<dd>As a check item, it matches if the request contains the named attribute, no matter what the value is.<br />
 Not allowed as a reply item. </p>
<dt><code>Attribute !* Value</code></p>
<dd>As a check item, it matches if the request does not contain the named attribute, no matter what the value is.<br />
 Not allowed as a reply item. </p>
</dl>
<h2>Examples</h2>
<dl>
<dd>Requests containing the User-Name attribute, with value &quot;bob&quot;, will be authenticated using the &quot;known good&quot; password &quot;hello&quot;. There are no reply items, so the reply will be empty.</dl>
<dl>
<dd>
<pre>DEFAULT Auth-Type = System
<br>
 Fall-Through = Yes</pre>
</dl>
<dl>
<dd>For all users reaching this entry, perform authentication against the system, unless Auth-Type has already been set. Also, process any following entries which may match.</dl>
<dl>
<dd>
<pre>DEFAULT Service-Type == Framed-User, Framed-Protocol == PPP
<br>
 Service-Type = Framed-User,
<br>
 Framed-Protocol = PPP,
<br>
 Fall-Through = Yes</pre>
</dl>
<dl>
<dd>If the request packet contains the attributes Service-Type and Framed-Protocol, with the given values, then include those attributes in the reply. That is, give the user what they ask for. This entry also shows how to specify multiple reply items.</dl>
<p> See the <code>users</code> file supplied with the server for more examples and comments. </p>
<h2>Hints</h2>
<p>Run the server in debugging mode (<code>-X</code>), and use the <code>radclient</code> program to send it test packets which you think will match specific entries. The server will print out which entries were matched for that request, so you can verify your expectations. This should be the FIRST thing you do if you suspect problems with the file. </p>
<p> Care should be taken when writing entries for the <code>users</code> file. It is easy to misconfigure the server so that requests are accepted when you wish to reject them. The entries should be ordered, and the Fall-Through item should be used ONLY where it is required. </p>
<p> Entries rejecting certain requests should go at the top of the file, and should not have a Fall-Through item in their reply items. Entries for specific users, who do not have a Fall-Through item, should come next. Any DEFAULT entries should usually come last, except as fall-through entries that set reply attributes.</p>
<h2>Files</h2>
<p>/etc/raddb/mods-config/files/</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-radclient/">radclient</a></code>(1), <code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-dictionary/">dictionary</a></code>(5), </p>
<h2>Author</h2>
<p>The FreeRADIUS team.</p>
