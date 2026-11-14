---
title: "gssapi_services_intro(3)"
name: "gssapi_services_intro"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gssapi_services_intro/"
---

<h2 class="name">NAME</h2>
 

 gssapi_services_intro - Introduction to GSS-API services

<h2>GSS-API services</h2>

 

<h3>Context creation</h3>

<dl>
<dt>&bull;
<dd> delegation
<dt>&bull;
<dd> mutual authentication
<dt>&bull;
<dd> anonymous
<dt>&bull;
<dd> use per message before context creation has completed</dl>
 

 

 return status:
<dl>
<dt>&bull;
<dd> support conf
<dt>&bull;
<dd> support int</dl>
 

<h3>Context creation flags</h3>

<dl>
<dt>&bull;
<dd> GSS_C_DELEG_FLAG
<dt>&bull;
<dd> GSS_C_MUTUAL_FLAG
<dt>&bull;
<dd> GSS_C_REPLAY_FLAG
<dt>&bull;
<dd> GSS_C_SEQUENCE_FLAG
<dt>&bull;
<dd> GSS_C_CONF_FLAG
<dt>&bull;
<dd> GSS_C_INTEG_FLAG
<dt>&bull;
<dd> GSS_C_ANON_FLAG
<dt>&bull;
<dd> GSS_C_PROT_READY_FLAG
<dt>&bull;
<dd> GSS_C_TRANS_FLAG
<dt>&bull;
<dd> GSS_C_DCE_STYLE
<dt>&bull;
<dd> GSS_C_IDENTIFY_FLAG
<dt>&bull;
<dd> GSS_C_EXTENDED_ERROR_FLAG
<dt>&bull;
<dd> GSS_C_DELEG_POLICY_FLAG</dl>
 

<h3>Per-message services</h3>

<dl>
<dt>&bull;
<dd> conf
<dt>&bull;
<dd> int
<dt>&bull;
<dd> message integrity
<dt>&bull;
<dd> replay detection
<dt>&bull;
<dd> out of sequence</dl>
 

 

 

<h2>Index</h2>


