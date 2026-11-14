---
title: "soapsuds(1)"
name: "soapsuds"
section: "1"
letter: "s"
url: "/docs/linux/man/1-soapsuds/"
description: "soapsuds – Mono’s Remoting Proxy Generator"
---

<h2>NAME</h2>
<p> soapsuds &#8211; Mono&#8217;s Remoting Proxy Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>soapsuds</code> [options] [inputs] [outputs]</p>
<h2>DESCRIPTION</h2>
<p> <i>soapsuds</i> is a tool for generating WSDL documents and client proxies for remoting services. A WSDL document describes the methods that a service provides together with XML schemas of all referenced data structures. A client proxy is a class which offers the same methods as the service it represents, but provides no implementation, it just forwards calls to the remote service. </p>
<p> Generated client proxies are not strictly necessary, since the runtime can automatically generate proxies from the original service types. However, it implies the need of distributing the service class to all clients. In some scenarios a better approach is to use soapsuds to generate a proxy class which has the same interface as the service, but without any implementation. </p>
<p> <i>soapsuds </i> can generate a WSDL document from a set of types specified with the option <i>-types</i> or can extract the types from an assembly specified with <i>-inputassemblyfile.</i> In this last case, soapsuds will include schemas for all serializable classes in the WSDL document. </p>
<p> Taking as input a WSDL document (or anything from which such document can be generated) the tool can generate source code for the client proxy (using the <i>-gc</i> option) or it can directly generate an assembly that implements the proxy (with the <i>-outputassemblyfile</i> option). soapsuds will also generate fake serializable classes for all types defined in the schema. However, beware that those classes will lack the semantics of the original classes, since only data structure is generated. </p>
<h2>INPUT SOURCES</h2>
<p> The following sources are available (only one can be specified):</p>
<dl>
<dt><i>-urltoschema:url -url:url</i></p>
<dd> Url from which to retrieve the WSDL document.</p>
<dt><i>-types:type1,assembly[,serviceEndPoint][;type2,assembly[,serviceEndPoint]]&#8230;</i></p>
<dd> Specifies types for which to generate a schema or proxy. If no service endpoint is provided, the one provided with the <i>-serviceendpoint</i> option is used.</p>
<dt><i>-inputassemblyfile:file, -ia:file</i></p>
<dd> Assembly that contains the types to export.</p>
<dt><i>-inputschemafile:schena, -is:schema</i></p>
<dd> Schema from which to generate proxy classes.</dl>
<h2>INPUT OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><i>-inputdirectory:directory, -id:directory</i></p>
<dd> Directory where DLLs are located.</p>
<dt><i>-serviceendpoint:url, -se:url</i></p>
<dd> Url of the service to be placed in the WSDL document.</dl>
<h2>OUTPUTS</h2>
<p> The following output options are available (more than one can be specified):</p>
<dl>
<dt><i>-outputassemblyfile:file, -oa:file</i></p>
<dd> Generates the proxy code and compiles it into an assembly with the provided name.</p>
<dt><i>-outputschemafile:file, -os:file</i></p>
<dd> Generates a WSDL document that represents the provided types.</p>
<dt><i>-generatecode, -gc</i></p>
<dd> Generates proxy source code for the provided WSDL document or types.</dl>
<h2>OUTPUT OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><i>-outputdirectory:directory, -od:directory</i></p>
<dd> Directory where generated files will be placed.</p>
<dt><i>-proxynamespace:namespace, -pn:namespace</i></p>
<dd> Namespace of the generated proxy.</p>
<dt><i>-nowrappedproxy, -nowp</i></p>
<dd> Do not generate a wrapped proxy.</p>
<dt><i>-wrappedproxy, -wp</i></p>
<dd> Generate a wrapped proxy.</p>
<dt><i>-strongnamefile:file, -sn:file</i></p>
<dd> Strong name file.</dl>
<h2>GENERAL OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><i>-nologo</i></p>
<dd> Supress the startup logo.</p>
<dt><i>-u:username, -user:username</i></p>
<dd> The user name to use when connecting to the server.</p>
<dt><i>-p:password, -password:password</i></p>
<dd> The password to use when connecting to the server.</p>
<dt><i>-d:domain, -domain:domain</i></p>
<dd> The domain to use when connecting to the server.</p>
<dt><i>-httpproxyname:name, -hpn:name</i></p>
<dd> Name of the http proxy.</p>
<dt><i>-httpproxyport:port, -hpp:port</i></p>
<dd> Port of the http proxy.</dl>
<h2>AUTHORS</h2>
<p> Lluis Sanchez Gual (lluis [at] ximian.com) </p>
<h2>LICENSE</h2>
<p> wsdl is released under the terms of the GNU GPL. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-wsdl/">wsdl</a>(1), <a href="/docs/linux/man/1-disco/">disco</a>(1), <a href="/docs/linux/man/1-mono/">mono</a>(1), <a href="/docs/linux/man/1-mcs/">mcs</a>(1) </p>
<h2>Index</h2>
