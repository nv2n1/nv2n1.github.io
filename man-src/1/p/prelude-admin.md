---
title: "prelude-admin(1)"
name: "prelude-admin"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prelude-admin/"
description: "prelude-admin – Manage agents accounts"
---

<h2>NAME</h2>
<p> prelude-admin &#8211; Manage agents accounts </p>
<h2>SYNOPSIS</h2>
<p> <code>prelude-admin </code> &lt;subcommand&gt; [options] [args] </p>
<p> <code>prelude-admin add &lt;profile name&gt; [&#8211;uid UID] [&#8211;gid GID]</code> </p>
<p> <code>prelude-admin chown &lt;profile name&gt; [&#8211;uid UID] [&#8211;gid GID]</code> </p>
<p> <code>prelude-admin del &lt;profile name&gt;</code> </p>
<p> <code>prelude-admin rename &lt;profile name&gt; &lt;profile name&gt;</code> </p>
<p> <code>prelude-admin register &lt;profile name&gt; &lt;wanted permission&gt; &lt;registration-server address&gt; [&#8211;uid UID] [&#8211;gid GID] [&#8211;passwd=PASSWD&gt;] [&#8211;passwd-file=&lt;FILE&gt;]</code> </p>
<p> <code>prelude-admin registration-server &lt;profile name&gt; [&#8211;uid UID] [&#8211;gid GID] [&#8211;prompt] [&#8211;passwd=PASSWD&gt;] [&#8211;passwd-file=&lt;FILE&gt;] [&#8211;keepalive] [&#8211;no-confirm] [&#8211;listen]</code> </p>
<p> <code>prelude-admin revoke &lt;profile&gt; &lt;analyzerID&gt; [&#8211;uid UID] [&#8211;gid GID]</code> </p>
<h2>DESCRIPTION</h2>
<p> In order for an agent to communicate with a manager, it must be registered. Registration involves several steps:<br />
&nbsp;<wbr>&#8211; Allocating an unique identity for the agent<br />
&nbsp;<wbr>&#8211; Creating directory to be used by the agent&nbsp;<wbr>(example: failover purpose)<br />
&nbsp;<wbr>&#8211; Registering to a remote&nbsp;<wbr>&#8216;prelude-manager&#8217;: get a signed X509 certificate that will allow communication between agent and manager using the specified permissions.&nbsp;<wbr> </p>
<p> All these informations are stored in an agent profile. </p>
<p> An agent profile is identified by its name. When an agent is started, it will load the profile of the same name as the program itself, that is, if your agent is named &quot;prelude-lml&quot;, the agent will load the profile named &quot;prelude-lml&quot;. </p>
<p> The name of the profile can be overriden using the &#8216;&#8211;prelude &#8211;profile name_of_my_profile&#8217; command line option. It is possible to define the profile name so that you can have several instances of one agent running with different permissions, using different profiles. </p>
<p> Note that profiles are not specific to agents, but are used in all programs of the Prelude suite (agents, managers, etc). </p>
<p> If you are not sure which permission your agent should get, just start it and default permissions will be displayed. </p>
<h2>OPTIONS</h2>
<p> <code>&lt;profile name&gt;</code> is the default name of the agent you are installing or your own defined name. </p>
<p> If you start your agent without prior registration, a warning is displayed including the default profile name on how to register the agent. </p>
<p> <code>&lt;requested permission&gt;</code> is the permission your agent needs. It is composed of permission attributes (idmef or admin) and access type: read/write (r/w). By default, an agent need permissions for writing IDMEF to a manager, and reading administrative command sent to it. That is : &quot;idmef:w admin:r&quot;. </p>
<p> <code>&lt;manager address&gt;</code> is the address of the prelude-manager you wish to register. this can either be its IP address or its hostname. If you made a local installation, you can write localhost to connect via unix socket. </p>
<p> Remember to use the correct uid/gid when registering your agent. For instance, if you want to register snort (running with snort euid / egid), use &#8211;uid snort &#8211;gid snort. </p>
<dl>
<dt><code>add &lt;analyzer profile&gt;</code></p>
<dd> Setup a new agent user. </p>
<p> <code>&#8211;uid=UID</code> UID or user to use to setup agent files. </p>
<p> <code>&#8211;gid=GID</code> GID or group to use to setup agent files.</p>
<dt>
<dd>
<p> <code>chown &lt;analyzer profile&gt;</code> Change analyzer owner. </p>
<p> <code>&#8211;uid=UID</code> UID or user to use to setup agent files. </p>
<p> <code>&#8211;gid=GID</code> GID or group to use to setup agent files.</p>
<dt>
<dd>
<p> <code>del &lt;analyzer profile&gt;</code> The delete command will remove the agent files created through &quot;add&quot; command. Once this is done, the analyzer can&#8217;t be used unless &quot;register&quot; or &quot;add&quot; is called again.</p>
<dt>
<dd>
<p> <code>rename &lt;analyzer profile&gt; &lt;analyzer profile&gt;</code> Rename an existing analyzer.</p>
<dt>
<dd>
<p> <code>register &lt;profile name&gt; &lt;wanted permission&gt; &lt;registration-server address&gt;</code> Register an analyzer. </p>
<p> Register and create the analyzer basic setup if needed. It will also configure communication of this analyzer with a receiving analyzer (like a Manager) through the specified registration-server. </p>
<p> <code>&#8211;uid=UID</code> UID or user to use to setup analyzer files. </p>
<p> <code>&#8211;gid=GID</code> GID or group to use to setup analyzer files. </p>
<p> <code>&#8211;passwd=PASSWD</code> Use provided password instead of prompting it. </p>
<p> <code>&#8211;passwd-file=-|FILE</code> Read password from file instead of prompting it (- for stdin).</p>
<dt>
<dd>
<p> <code>registration-server &lt;profile name&gt;</code> Start a registration server to register agents. This is used in order to register &#8216;sending&#8217; analyzer to &#8216;receiving&#8217; analyzer. &lt;profile name&gt; should be set to the profile name of the &#8216;receiving&#8217; analyzer, the one where &#8216;sending&#8217; analyzer will register to. </p>
<p> <code>&#8211;uid=UID</code> UID or user to use to setup &#8216;receiving&#8217; analyzer files. </p>
<p> <code>&#8211;gid=GID</code> GID or group to use to setup &#8216;receiving&#8217; analyzer files. </p>
<p> <code>&#8211;prompt</code> Prompt for a password instead of auto generating it. </p>
<p> <code>&#8211;passwd=PASSWD</code> Use provided password instead of auto generating it. </p>
<p> <code>&#8211;passwd-file=-|FILE</code> Read password from file instead of auto generating it (- for stdin). </p>
<p> <code>&#8211;keepalive</code> Register analyzer in an infinite loop. </p>
<p> <code>&#8211;no-confirm</code> Do not ask for confirmation on agent registration. </p>
<p> <code>&#8211;listen</code> Address to listen on for registration request (default is any:5553).</p>
<dt>
<dd> <code>revoke &lt;profile name&gt;</code> Revoke access to &lt;profile&gt; for the given analyzerID. </p>
<p> <code>&#8211;uid=UID</code> UID or user to use to setup analyzer files. </p>
<p> <code>&#8211;gid=GID</code> GID to group to use to setup analyzer files.</p>
<dt>
<dd> <code>&#8211;help</code> Print help </p>
</dl>
<h2>AUTHOR</h2>
<p> This man page has been written by Frederic Motte </p>
<h2>Index</h2>
