---
title: "ipa(1)"
name: "ipa"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa/"
description: "ipa – IPA command-line interface"
---

<h2>NAME</h2>
<p> ipa &#8211; IPA command-line interface</p>
<h2>SYNOPSIS</h2>
<pre><code>
ipa[options][-c FILE][-e KEY = VAL] COMMAND[parameters]
</code></pre>
<h2>DESCRIPTION</h2>
<p> IPA is an integrated security information management solution based on 389 Directory Server (formerly know as Fedora Directory Server), MIT Kerberos, Dogtag Certificate System, NTP and DNS. It includes a web interface and command-line administration tools for managing identity data. </p>
<p> This manual page focuses on the <i>ipa</i> script that serves as the main command-line interface (CLI) for IPA administration. </p>
<p> More information about the project is available on its homepage located at <a rel="nofollow" href="http://www.freeipa.org.">http://www.freeipa.org.</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>FILE</i></dt>
<dd> Load configuration from <i>FILE</i>.</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> Produce full debugging output.</dd>
<dt><code>&#8211;delegate</code></dt>
<dd> Delegate the user&#8217;s TGT to the IPA server</dd>
<dt><code>-e</code> <i>KEY=VAL</i></dt>
<dd> Set environmental variable <i>KEY</i> to the value <i>VAL</i>. This option overrides configuration files.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display a help message with a list of options.</dd>
<dt><code>-n</code>, <code>&#8211;no-prompt</code></dt>
<dd> Don&#8217;t prompt for any parameters of <code>COMMAND</code>, even if they are required.</dd>
<dt><code>-a</code>, <code>&#8211;prompt-all</code></dt>
<dd> Prompt for all parameters of <i>COMMAND</i>, even if they are optional.</dd>
<dt><code>-f</code>, <code>&#8211;no-fallback</code></dt>
<dd> Don&#8217;t fall back to other IPA servers if the default doesn&#8217;t work.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Produce verbose output. A second -v pretty-prints the JSON request and response. A third -v displays the HTTP request and response.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display the IPA version and API version.</dd></dl>
<h2>COMMANDS</h2>
<p> The principal function of the CLI is to execute administrative commands specified by the <i>COMMAND</i> argument. The majority of commands are executed remotely over XML-RPC on a IPA server listed in the configuration file (see FILES section of this manual page). </p>
<p> From the implementation perspective, the CLI distinguishes two types of commands &#8211; built-ins and plugin provided. </p>
<p> Built-in commands are static and are all available in all installations of IPA. There are two of them:</p>
<dl>
<dt><code>console</code></dt>
<dd> Start the IPA interactive Python console.</dd>
<dt><code>help</code> [<i>TOPIC</i> | <i>COMMAND</i> | <code>topics</code> | <code>commands</code>]</dt>
<dd> Display help for a command or topic. </dd>
<p> The <code>help</code> command invokes the built-in documentation system. Without parameters a list of built-in commands and help topics is displayed. Help topics are generated from loaded IPA plugin modules. Executing <code>help</code> with the name of an available topic displays a help message provided by the corresponding plugin module and list of commands it contains.</dl>
<p> Plugin provided commands, as the name suggests, originate from IPA plugin modules. The available set may vary depending on your configuration and can be listed using the built-in <code>help</code> command (see above). </p>
<p> Most plugin provided commands are tied to a certain type of IPA object. IPA objects encompass common abstractions such as users (user identities/accounts), hosts (machine identities), services, password policies, etc. Commands associated with an object are easily identified thanks to the enforced naming convention; the command names are composed of two parts separated with a dash: the name of the corresponding IPA object type and the name of action performed on it. For example all commands used to manage user identities start with &quot;user-&quot; (e.g. user-add, user-del). </p>
<p> The following actions are available for most IPA object types:</p>
<dl>
<dt><code>add</code> [<i>PRIMARYKEY</i>] [options]</dt>
<dd> Create a new object.</dd>
<dt><code>show</code> [<i>PRIMARYKEY</i>] [options]</dt>
<dd> Display an existing object.</dd>
<dt><code>mod</code> [<i>PRIMARYKEY</i>] [options]</dt>
<dd> Modify an existing object.</dd>
<dt><code>del</code> [<i>PRIMARYKEY</i>]</dt>
<dd> Delete an existing object.</dd>
<dt><code>find</code> [<i>CRITERIA</i>] [options]</dt>
<dd> Search for existing objects.</dd></dl>
<p> The above types of commands except <code>find</code> take the objects primary key (e.g. user name for users) as their only positional argument unless there can be only one object of the given type. They can also take a number of options (some of which might be required in the case of <code>add</code>) that represent the objects attributes. </p>
<p> <code>find</code> commands take an optional criteria string as their only positional argument. If present, all objects with an attribute that contains the criteria string are displayed. If an option representing an attribute is set, only object with the attribute exactly matching the specified value are displayed. Options with empty values are ignored. Without parameters all objects of the corresponding type are displayed. </p>
<p> For IPA objects with attributes that can contain references to other objects (e.g. groups), the following action are usually available:</p>
<dl>
<dt><code>add-member</code> [<i>PRIMARYKEY</i>] [options]</dt>
<dd> Add references to other objects.</dd>
<dt><code>remove-member</code> [<i>PRIMARYKEY</i>] [options]</dt>
<dd> Remove references to other objects.</dd></dl>
<p> The above types of commands take the objects primary key as their only positional argument unless there can be only one object of the given type. They also take a number of options that represent lists of other object primary keys. Each of these options represent one type of object. </p>
<p> For some types of objects, these commands might need to take more than one primary key. This applies to IPA objects organized in hierarchies where the parent object needs to be identified first. Parent primary keys are always aligned to the left (higher in the hierarchy = more to the left). For example the automount IPA plugin enables users to manage automount maps per location, as a result all automount commands take an automountlocation primary key as their first positional argument. </p>
<p> All commands that display objects have three special options for controlling output:</p>
<dl>
<dt><code>&#8211;all</code></dt>
<dd> Display all attributes. Without this option only the most relevant attributes are displayed.</dd>
<dt><code>&#8211;raw</code></dt>
<dd> Display objects as they are stored in the backing store. Disables formatting and attribute labels.</dd>
<dt><code>&#8211;rights</code></dt>
<dd> Display effective rights on all attributes of the entry. You also have to specify <code>&#8211;all</code> for this to work. User rights are returned as Python dictionary where index is the name of an attribute and value is a unicode string composed (hence the u&#8217;xxxx&#8217; format) of letters specified below. Note that user rights are primarily used for internal purposes of CLI and WebUI. </dd>
<p> r &#8211; read<br />
 s &#8211; search<br />
 w &#8211; write<br />
 o &#8211; obliterate (delete)<br />
 c &#8211; compare<br />
 W &#8211; self-write<br />
 O &#8211; self-obliterate </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>ipa help commands</code></dt>
<dd> Display a list of available commands <code>ipa help topics</code> Display a high-level list of help topics <code>ipa help user</code> Display documentation and list of commands in the &quot;user&quot; topic.</dd>
<dt><code>ipa env</code></dt>
<dd> List IPA environmental variables and their values.</dd>
<dt><code>ipa user-add foo &#8211;first foo &#8211;last bar</code></dt>
<dd> Create a new user with username &quot;foo&quot;, first name &quot;foo&quot; and last name &quot;bar&quot;.</dd>
<dt><code>ipa group-add bar &#8211;desc &quot;this is an example group&quot;</dt>
<dd> Create a new group with name &quot;bar&quot; and description &quot;this is an example group&quot;.</dd>
<dt>ipa group-add-member bar &#8211;users=foo</code></dt>
<dd> Add user &quot;foo&quot; to the group &quot;bar&quot;.</dd>
<dt><code>ipa group-add-member bar &#8211;users={admin,foo}</code></dt>
<dd> Add users &quot;admin&quot; and &quot;foo&quot; to the group &quot;bar&quot;. This approach depends on shell expansion feature.</dd>
<dt><code>ipa user-show foo &#8211;raw</code></dt>
<dd> Display user &quot;foo&quot; as (s)he is stored on the server.</dd>
<dt><code>ipa group-show bar &#8211;all</code></dt>
<dd> Display group &quot;bar&quot; and all of its attributes.</dd>
<dt><code>ipa config-mod &#8211;maxusername 20</code></dt>
<dd> Set maximum user name length to 20 characters.</dd>
<dt><code>ipa user-find foo</code></dt>
<dd> Search for all users with &quot;foo&quot; in either uid, first name, last name, full name, etc. A user with uid &quot;foobar&quot; would match the search criteria.</dd>
<dt><code>ipa user-find foo &#8211;first bar</code></dt>
<dd> Same as the previous example, except this time the users first name has to be exactly &quot;bar&quot;. A user with uid &quot;foobar&quot; and first name &quot;bar&quot; would match the search criteria.</dd>
<dt><code>ipa user-find foo &#8211;first bar &#8211;last foo</code></dt>
<dd> A user with uid &quot;foobar&quot;, first name &quot;bar&quot; and last name &quot;foo&quot; would match the search criteria.</dd>
<dt><code>ipa user-find</code></dt>
<dd> All users would match the search criteria (as there are none).</dd></dl>
<h2>SERVERS</h2>
<p> The ipa client will determine which server to connect to in this order: </p>
<dl>
<dt>1. The server configured in <code>/etc/ipa/default.conf</code> in the <i>xmlrpc_uri</i> directive.</dt>
<dd>
</dd><dt>2. An unordered list of servers from the ldap DNS SRV records.</dt>
<dd>
</dd><dt>If a kerberos error is raised by any of the requests then it will stop processing and display the error message.</dt>
<dd></dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>IPA_CONFDIR</code></dt>
<dd> Override path to confdir (default: <code>/etc/ipa</code>).</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/ipa/default.conf</code></dt>
<dd> IPA default configuration file.</dd></dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<p> 2 If an entry is not found</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ipa-client-install/">ipa-client-install</a>(1), <a href="/docs/linux/man/1-ipa-compat-manage/">ipa-compat-manage</a>(1), ipactl(1), <a href="/docs/linux/man/1-ipa-dns-install/">ipa-dns-install</a>(1), <a href="/docs/linux/man/1-ipa-getcert/">ipa-getcert</a>(1), <a href="/docs/linux/man/1-ipa-getkeytab/">ipa-getkeytab</a>(1), <a href="/docs/linux/man/1-ipa-join/">ipa-join</a>(1), <a href="/docs/linux/man/1-ipa-ldap-updater/">ipa-ldap-updater</a>(1), <a href="/docs/linux/man/1-ipa-nis-manage/">ipa-nis-manage</a>(1), <a href="/docs/linux/man/1-ipa-replica-install/">ipa-replica-install</a>(1), <a href="/docs/linux/man/1-ipa-replica-manage/">ipa-replica-manage</a>(1), <a href="/docs/linux/man/1-ipa-replica-prepare/">ipa-replica-prepare</a>(1), <a href="/docs/linux/man/1-ipa-rmkeytab/">ipa-rmkeytab</a>(1), ipa-server-certinstall(2), <a href="/docs/linux/man/1-ipa-server-install/">ipa-server-install</a>(1), <a href="/docs/linux/man/1-ipa-server-upgrade/">ipa-server-upgrade</a>(1) </p>
<h2>Index</h2>
