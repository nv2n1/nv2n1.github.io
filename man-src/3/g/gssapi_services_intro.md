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
</dt><dd> delegation
</dd><dt>&bull;
</dt><dd> mutual authentication
</dd><dt>&bull;
</dt><dd> anonymous
</dd><dt>&bull;
</dt><dd> use per message before context creation has completed</dd></dl>
 

 

 return status:
<dl>
<dt>&bull;
</dt><dd> support conf
</dd><dt>&bull;
</dt><dd> support int</dd></dl>
 

<h3>Context creation flags</h3>

<dl>
<dt>&bull;
</dt><dd> GSS_C_DELEG_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_MUTUAL_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_REPLAY_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_SEQUENCE_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_CONF_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_INTEG_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_ANON_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_PROT_READY_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_TRANS_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_DCE_STYLE
</dd><dt>&bull;
</dt><dd> GSS_C_IDENTIFY_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_EXTENDED_ERROR_FLAG
</dd><dt>&bull;
</dt><dd> GSS_C_DELEG_POLICY_FLAG</dd></dl>
 

<h3>Per-message services</h3>

<dl>
<dt>&bull;
</dt><dd> conf
</dd><dt>&bull;
</dt><dd> int
</dd><dt>&bull;
</dt><dd> message integrity
</dd><dt>&bull;
</dt><dd> replay detection
</dd><dt>&bull;
</dt><dd> out of sequence</dd></dl>
 

 

 

<h2>Index</h2>


