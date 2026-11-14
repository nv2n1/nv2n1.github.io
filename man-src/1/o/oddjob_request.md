---
title: "oddjob_request(1)"
name: "oddjob_request"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oddjob_request/"
description: "oddjob_request – send requests to oddjobd from the command line"
---

<h2 class="name">NAME</h2>
<p> oddjob_request &#8211; send requests to oddjobd from the command line</p>
<h2>SYNOPSIS</h2>
<p> oddjob_request [-s service] [-o object] [-i interface] [-S] [ [request [arg1 &#8230;]] | -I ] </p>
<h2>DESCRIPTION</h2>
<p> The <i>oddjob_request</i> application is a simple <i>oddjob</i> client application which can be used to invoke a particular method provided by the <i>oddjobd</i> server. </p>
<p> If no request is given as a command-line argument, <i>oddjob_request</i> will attempt to invoke the <i>list</i> method, which should list all methods for which the invoking user is authorized. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>-S</code></p>
<dd> Connect to the session bus instead of the system bus. This option is primarily intended for use in testing. <i>com.redhat.oddjob</i>.</p>
<dt><code>-s</code> service</p>
<dd> The object is provided by the named service instead of <i>com.redhat.oddjob</i>.</p>
<dt><code>-o</code> object</p>
<dd> Invoke a method on the named object instead of <i>/com/redhat/oddjob</i>.</p>
<dt><code>-i</code> interface</p>
<dd> The method is part of the named interface instead of <i>com.redhat.oddjob</i>.</p>
<dt><code>-I</code></p>
<dd> Default to the method and interface names used for D-Bus introspection (<i>Introspect</i> and <i>org.freedesktop.DBus.Introspectable</i>, respectively).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-oddjob-conf/">oddjob.conf</a></code>(5) <code><a href="/docs/linux/man/5-oddjobd-conf/">oddjobd.conf</a></code>(5) <code><a href="/docs/linux/man/8-oddjobd/">oddjobd</a></code>(8) </p>
<h2>Index</h2>
