---
title: "saml_assertion_init(1)"
name: "saml_assertion_init"
section: "1"
letter: "s"
url: "/docs/linux/man/1-saml_assertion_init/"
description: "saml_assertion_init – ARC client to voms saml service, or arc aa service"
---

<h2>DESCRIPTION</h2>
<p> The <code>saml_assertion_init</code> command is a prototype client which is used for sending an attribute query request to a voms saml service or arc aa service. </p>
<h2>SYNOPSIS</h2>
<p> <code>saml_assertion_init [options] [filename &#8230;]</code> </p>
<p> saml_assertion_init -c saml_assertion_init_client.xml -d DEBUG <a rel="nofollow" href="https://squark.uio.no:8443/voms/saml/knowarc/services/AttributeAuthorityPortType">https://squark.uio.no:8443/voms/saml/knowarc/services/AttributeAuthorityPortType</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> [-]<i>configurefile</i>, <code>-conf</code> [-]<i>configurefile</i></dt>
<dd> specify the configuration file of this client</dd>
<dt><code>-d</code> <i>debuglevel</i>, <code>-debug</code> <i>debuglevel</i></dt>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</dd>
<dt><code>-v</code>, <code>-version</code></dt>
<dd> print version information</dd>
<dt><code>-?</code>, <code>-help</code></dt>
<dd> print help</dd></dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>serviceurl</code> &#8230;</dt>
<dd> url to saml aa service</dd></dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>saml_assertion_init</code> command is a prototype client which is used for sending an attribute query request to a saml aa service. </p>
<p> <i>Examples</i>:</p>
<dl>
<dt><code>saml_assertion_init -c saml_assertion_init_client.xml -d DEBUG <a rel="nofollow" href="https://squark.uio.no:8443/voms/saml/knowarc/services/AttributeAuthorityPortType">https://squark.uio.no:8443/voms/saml/knowarc/services/AttributeAuthorityPortType</a></code> &#8230;</dt>
<dd> send the attribute query request to <a rel="nofollow" href="https://squark.uio.no:8443/voms/saml/knowarc/services/AttributeAuthorityPortType">https://squark.uio.no:8443/voms/saml/knowarc/services/AttributeAuthorityPortType</a></dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>.arc/config.xml</code></dt>
<dd> Some options can be given default values by specifying them in the ARC configuration file. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>ARC_LOCATION</code></dt>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </dd>
<dt><code>ARC_PLUGIN_PATH</code></dt>
<dd> The location of ARC plugins can be specified by this variable. Multiple locations can be specified by separating them by : (; in Windows). The default location is <code>$ARC_LOCATION</code>/lib/arc (\ in Windows). </dd>
</dl>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
