---
title: "mc-tool(1)"
name: "mc-tool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mc-tool/"
description: "mc-tool – manipulate Mission Control accounts from the command line"
---

<h2>NAME</h2>
<p> mc-tool &#8211; manipulate Mission Control accounts from the command line</p>
<h2>SYNOPSIS</h2>
<p> <code>mc-tool list</code> </p>
<p> <code>mc-tool add</code> <i>PROFILE</i> <i>DISPLAY-NAME</i> <i></i>[<i>PARAMETER-SETTINGS</i>&#8230;] </p>
<p> <code>mc-tool add</code> <i>MANAGER</i>/<i>PROTOCOL</i> [<i>PARAMETER-SETTINGS</i>&#8230;] </p>
<p> <code>mc-tool update</code> <i>ACCOUNT</i> [<i>PARAMETER-SETTINGS</i>&#8230;] </p>
<p> <code>mc-tool display</code> <i>ACCOUNT DISPLAY-NAME</i> </p>
<p> <code>mc-tool nick</code> <i>ACCOUNT NICKNAME</i> </p>
<p> <code>mc-tool service</code> <i>ACCOUNT SERVICE-NAME</i> </p>
<p> <code>mc-tool icon</code> <i>ACCOUNT ICON</i> </p>
<p> <code>mc-tool show</code> <i>ACCOUNT</i> </p>
<p> <code>mc-tool get</code> <i>ACCOUNT</i> <i>PARAMETER</i> [<i>PARAMETER</i>&#8230;] </p>
<p> <code>mc-tool auto-presence</code> <i>ACCOUNT</i> <i>STATUS</i> [<i>MESSAGE</i>] </p>
<p> <code>mc-tool request</code> <i>ACCOUNT</i> <i>STATUS</i> [<i>MESSAGE</i>] </p>
<p> <code>mc-tool auto-connect</code> <i>ACCOUNT</i> <code>on</code>|<code>off</code> </p>
<p> <code>mc-tool remove</code> <i>ACCOUNT</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>mc-tool</code>&#8216;s usage depends on its first argument (the &quot;command&quot;) </p>
<h3>SPECIFYING ACCOUNTS</h3>
<p> Where an account name is needed, it may be given as a full object path (e.g. <code>/org/freedesktop/Telepathy/Account/gabble/jabber/example</code>), or as the unique account-specific suffix (e.g. <code>gabble/jabber/example</code>). </p>
<h3>SPECIFYING PARAMETER SETTINGS</h3>
<p> Many commands take arguments that represent Telepathy connection manager parameters (see the Telepathy Specification for details of these). Each argument has the following form: </p>
<p> <i>TYPE</i><code>:</code><i>NAME</i><code>=</code><i>VALUE</i> </p>
<p> where <i>TYPE</i> is either <code>int</code>, <code>uint</code>, <code>bool</code>, or <code>string</code> (other parameter types exist, but are currently unsupported by <code>mc-tool</code>), <i>NAME</i> is the name of the connection manager parameter (e.g. <code>account</code> or <code>password</code>), and <i>VALUE</i> is the parameter&#8217;s value (with integers in decimal, and booleans as <code>0</code> or <code>1</code>). </p>
<p> The <code>update</code> command also accepts arguments of the form <code>clear:</code><i>NAME</i> which delete the named parameter from the account configuration.</p>
<h3>LIST</h3>
<p> <code>mc-tool list</code> lists the available accounts. </p>
<h3>ADD</h3>
<p> <code>mc-tool add</code> adds an account. The connection manager and protocol can either be given as the name of a Mission Control <i>profile</i>, (e.g. <code>gtalk</code>), or as a slash-separated connection manager name and protocol (e.g. <code>gabble/jabber</code>). </p>
<h3>DISPLAY</h3>
<p> <code>mc-tool display</code> <i>ACCOUNT DISPLAY-NAME</i> sets the <code>DisplayName</code> property of <i>ACCOUNT</i> to <i>DISPLAY-NAME.</i> </p>
<h3>NICK</h3>
<p> <code>mc-tool nick</code> <i>ACCOUNT NICKNAME</i> sets the <code>Nickname</code> property of <i>ACCOUNT</i> to <i>NICKNAME</i>. </p>
<h3>SERVICE</h3>
<p> <code>mc-tool service</code> <i>ACCOUNT SERVICE-NAME</i> sets the <code>Service</code> property of <i>ACCOUNT</i> to <i>SERVICE-NAME</i>. </p>
<h3>ICON</h3>
<p> <code>mc-tool icon</code> <i>ACCOUNT ICON</i> sets the <code>Icon</code> property of <i>ACCOUNT</i> to <i>ICON</i>. </p>
<h3>SHOW</h3>
<p> <code>mc-tool show</code> <i>ACCOUNT</i> shows information about <i>ACCOUNT</i>. </p>
<h3>GET</h3>
<p> <code>mc-tool get</code> <i>ACCOUNT</i> <i>PARAMETER</i> [<i>PARAMETER</i>&#8230;] shows the values of the given parameters of <i>ACCOUNT</i>. </p>
<h3>ENABLE</h3>
<p> <code>mc-tool enable</code> <i>ACCOUNT</i> sets the <code>Enabled</code> property of <i>ACCOUNT</i> to <code>True</code>. </p>
<h3>DISABLE</h3>
<p> <code>mc-tool disable</code> <i>ACCOUNT</i> sets the <code>Enabled</code> property of <i>ACCOUNT</i> to <code>False</code>. </p>
<h3>AUTO-PRESENCE</h3>
<p> <code>mc-tool auto-presence</code> <i>ACCOUNT</i> <i>STATUS</i> [<i>MESSAGE</i>] sets the <code>AutomaticPresence</code> property of <i>ACCOUNT</i> to <i>STATUS</i> with optional message <i>MESSAGE</i>. </p>
<h3>REQUEST</h3>
<p> <code>mc-tool request</code> <i>ACCOUNT</i> <i>STATUS</i> [<i>MESSAGE</i>] sets the <code>RequestedPresence</code> property of <i>ACCOUNT</i> to <i>STATUS</i> with optional message <i>MESSAGE</i>; this is how you tell an account to connect or go offline, for example. </p>
<h3>AUTO-CONNECT</h3>
<p> <code>mc-tool auto-connect</code> <i>ACCOUNT</i> <code>on</code> sets the <code>ConnectAutomatically</code> property of <i>ACCOUNT</i> to <code>True</code>. <code>mc-tool auto-connect</code> <i>ACCOUNT</i> <code>off</code> sets it to <code>False</code>. </p>
<h2>Index</h2>
