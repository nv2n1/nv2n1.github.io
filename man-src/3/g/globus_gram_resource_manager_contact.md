---
title: "globus_gram_resource_manager_contact(3)"
name: "globus_gram_resource_manager_contact"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_resource_manager_contact/"
---

<h2 class="name">NAME</h2>
 

 globus_gram_resource_manager_contact - Resource Manager Contact The resource manager contact string is used by the GRAM Client to connect to, authenticate to, and request service from a GRAM resource manager. The simplest contact string is just a host name, but additional fields may be present in the name to qualify the TCP port number it is listening on, the service name (for example, to choose a specific scheduler), and the subject name (security identity) of the resource manager. 

 For those resource manager contacts which omit the port, service or subject field the following defaults are used: 

 

 <pre>
port = 2119 (assigned by IANA)
service = jobmanager 
subject = subject based on hostname
</pre> 

 

 The following contain all of the acceptable formats of a GRAM Resource Manager Contact: 

<dl>
<dt>&bull;
<dd> host
<dt>&bull;
<dd> host:port
<dt>&bull;
<dd> host:port/service
<dt>&bull;
<dd> host/service
<dt>&bull;
<dd> host:/service
<dt>&bull;
<dd> host::subject
<dt>&bull;
<dd> host:port:subject
<dt>&bull;
<dd> host/service:subject
<dt>&bull;
<dd> host:/service:subject
<dt>&bull;
<dd> host:port/service:subject</dl>
 

 

 Note: Any of the above forms may be preceded by an optional '&lt;b&gt;https&lt;/b&gt;&lt;b&gt;://&lt;/b&gt;'. 

 <hr> 

<h2>Index</h2>


