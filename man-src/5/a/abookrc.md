---
title: "abookrc(5)"
name: "abookrc"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abookrc/"
description: "$HOME/.abook/abookrc – configuration file for abook address book program"
---

<p><code>$HOME/.abook/abookrc</code> &#8211; configuration file for abook address book program</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>abookrc</code> file.<br />
 <code>abookrc</code> is the (optional) configuration file for use with the <code><a href="/docs/linux/man/1-abook/">abook</a>(1)</code> address book program. <code>abookrc</code> is stored in a user&#8217;s $HOME/.abook directory. It follows a format of lq<code>set option=value</code>rq. The following information lists each of these options and the values they may take. If a variable is not set in <code>abookrc</code> , a sensible default, as listed with the description below, will be used. Comments in <code>abookrc</code> are on lines beginning with &#8216;#&#8217;. </p>
<h2>Commands</h2>
<dl>
<dt><code>set</code> <i>option</i> = <i>value</i></p>
<dd>
<dt><code>field</code> <i>identifier</i> = <i>human_readable_name</i> [ , <i>type</i> ]</p>
<dd>Defines a new custom field. <i>type</i> can be one of &#8216;string&#8217; (default) , &#8217;emails&#8217;, &#8216;list&#8217;, or &#8216;date&#8217;. </p>
<dt><code>view</code> <i>view name</i> = <i>field1</i> [ , <i>field2</i>, &#8230; ]</p>
<dd>Defines a view/tab, with <i>fieldN</i> being the identifier of a field declared with the <code>field</code> command, or the identifier of a standard field.</p>
<dd>Standard fields:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>name, email,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>address, address2, city, state, zip, country,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>phone, workphone, fax, mobile,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>nick, url, notes, anniversary</p>
<dd>Note: if you don&#8217;t define any view, abook will use a default display based on the above standard fields. </p>
</dl>
<h2>Variables</h2>
<dl>
<dt><code>autosave</code>=[true|false]</p>
<dd>Defines whether the addressbook is automatically saved on exit. Default is true. </p>
<dt><code>preserve_fields</code>=[all|standard|none]</p>
<dd>Specifies how fields not declared with the <code>field</code> command nor in a view should be preserved while loading an abook database.</p>
<dl>
<dd>
<dl>
<dt><code>all</code></p>
<dd>preserve any completely unknown field.</p>
<dt><code>standard</code></p>
<dd>only preserve the standard fields (see a list in the<br />
&nbsp;<wbr>&nbsp;<wbr>description of the&nbsp;<wbr><code>view</code>&nbsp;<wbr>command)&nbsp;<wbr>and the legacy<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;custom[1-5]&#8217;&nbsp;<wbr>fields.</p>
<dt><code>none</code></p>
<dd>discards any unknown field.</dl>
</dl>
<dd>Default is <i>standard</i>. </p>
<dt><code>index_format</code>=format_string</p>
<dd>Defines the way entries are displayed in the main list. This is a string containing field names enclosed between braces, with an optional width limit specified by a number (right alignment if negative) after the field name and a colon, and an arbitrary number of alternative fields (first with non empty content is to be displayed) separated by vertical bars. For instance:</p>
<dl>
<dd>
<dl>
<dt><i>{name:22}</i></p>
<dd>displays the <i>name</i> field with a maximal width of 22 characters.</p>
<dt><i>{phone:-13|workphone|mobile}</i></p>
<dd>displays (right aligned within a width of 13 characters), either the <i>phone</i>, <i>workphone</i> or <i>mobile</i> field, whichever being the first to be non-empty.</dl>
</dl>
<dd>Default is <i>&quot; {name:22} {email:40} {phone:12|workphone|mobile}&quot;</i> </p>
<dt><code>show_all_emails</code>=[true|false]</p>
<dd>Defines whether all email addresses for a contact are shown in the main list view. Default is true. </p>
<dd><code>emailpos</code></p>
<dd><code>extra_column</code></p>
<dd><code>extra_alternative</code></p>
<dd><code>extrapos</code> Obsoleted by <code>index_format</code>. </p>
<dt><code>mutt_return_all_emails</code>=[true|false]</p>
<dd>Defines whether to return all email addresses matching the search criteria to a mutt query. Default is true. </p>
<dt><code>print_command</code>=command</p>
<dd>Defines the command to used when printing the addressbook. Default is &quot;lpr&quot;. </p>
<dt><code>www_command</code>=command</p>
<dd>Defines the command used to start the web browser to view a contact&#8217;s URL. Default is &quot;lynx&quot;. </p>
<dt><code>address_style</code>=[eu|uk|us]</p>
<dd>Defines the style of address formatting to be used when exporting as text / printing the database (European, UK, or USA). Default is European (&quot;eu&quot;). </p>
<dt><code>use_ascii_only</code>=[true|false]</p>
<dd>This option allows you to force Abook use only ASCII characters. This option is useful if your terminal doesn&#8217;t support non-ASCII characters. Default is false. </p>
<dt><code>add_email_prevent_duplicates</code>=[true|false]</p>
<dd>Defines whether to avoid adding addresses already in data. Default is false. </p>
<dt><code>sort_field</code>=field</p>
<dd>Defines the field to be used by the &quot;sort by field&quot; command. Default is &quot;nick&quot; (Nickname/Alias). </p>
<dt><code>show_cursor</code>=[true|false]</p>
<dd>Defines if the cursor is visible in main display. Default is false. </p>
</dl>
<h2>Sample Configuration File</h2>
<pre># sample abook configuration file
#
# Declare a few custom fields
field pager = Pager
field address_lines = Address, list
field birthday = Birthday, date
# Define how fields should be displayed in tabs
view CONTACT = name, email
view ADDRESS = address_lines, city, state, zip, country
view PHONE = phone, workphone, pager, mobile, fax
view OTHER = url, birthday
# Preserve any unknown field while loading an abook database
set preserve_fields=all
# Automatically save database on exit
set autosave=true
# Format of entries lines in list
set index_format=&quot; {name:22} {email:40} {phone:12|workphone|mobile}&quot;
# Show all email addresses in list
set show_all_emails=true
# Command used to start mutt
set mutt_command=mutt
# Return all email addresses to a mutt query
set mutt_return_all_emails=true
# Command used to print
set print_command=lpr
# Command used to start the web browser
set www_command=lynx
# Address style [eu|us|uk]
set address_style=eu
# Use ASCII characters only
set use_ascii_only=false
# Prevent double entry
set add_email_prevent_duplicates=false
# Field to be used with &quot;sort by field&quot; command
set sort_field=nick
# Show cursor in main display
set show_cursor=false</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-abook/">abook</a></code>(1).</p>
<h2>Authors</h2>
<p>This manual page was written by Alan Ford &lt;alan [at] whirlnet.co.uk&gt; and expanded by Cedric Duval &lt;cedricduval [at] free.fr&gt;. </p>
<p> <code>abook</code> was written by Jaakko Heinonen &lt;jheinonen [at] users.sourceforge.net&gt;</p>
