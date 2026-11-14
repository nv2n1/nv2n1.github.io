---
title: "ipactl(8)"
name: "ipactl"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipactl/"
description: "ipactl – IPA Server Control Interface"
---

<p>ipactl &#8211; IPA Server Control Interface</p>
<h2>Synopsis</h2>
<p>ipactl <i>command</i></p>
<h2>Description</h2>
<p>A tool to help an administer control an IPA environment. </p>
<p> IPA glues several discrete services together to work in concert and the order that these services are started and stopped is important. ipactl ensures that they are started and stopped in the correct order. </p>
<p> IPA stores the available masters and the services configured on each one. The first thing ipactl does is start (if it is not already running) the IPA 389-ds instance to query what services it controls. The hostname used in the query needs to match the hostname of the value stored in LDAP. This can be controlled with the host option in <i>/etc/ipa/default.conf</i>. This should be a fully-qualified hostname.</p>
<h2>Options</h2>
<dl>
<dt>start</p>
<dd>Start all of the services that make up IPA</p>
<dt>stop</p>
<dd>Stop all of the services that make up IPA</p>
<dt>restart</p>
<dd>Stop then start all of the services that make up IPA</p>
<dt>status</p>
<dd>Provides status of all the services that make up IPA</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Display debugging information</p>
<dt><code>&#8211;skip-version-check</code></p>
<dd>Skip version check</p>
<dt><code>&#8211;ignore-service-failures</code></p>
<dd>If any service start fails, do not rollback the services, continue with the operation</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Force IPA to start. Combine options &#8211;skip-version-check and &#8211;ignore-service-failures </p>
</dl>
