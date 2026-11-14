---
title: "globus_gass_transfer_listenerattr_get_backlog(3)"
name: "globus_gass_transfer_listenerattr_get_backlog"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_listenerattr_get_backlog/"
description: "Listener attributes –"
---

<h2 class="name">NAME</h2>
<p> Listener attributes &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_gass_transfer_listenerattr_init</code> (globus_gass_transfer_listenerattr_t *attr, char *url_scheme) </p>
<h3>Listener Backlog</h3>
<p> int <code>globus_gass_transfer_listenerattr_set_backlog</code> (globus_gass_transfer_listenerattr_t *attr, int backlog) </p>
<p> int <code>globus_gass_transfer_listenerattr_get_backlog</code> (globus_gass_transfer_listenerattr_t *attr, int *backlog) </p>
<h3>Listener Port</h3>
<p> int <code>globus_gass_transfer_listenerattr_set_port</code> (globus_gass_transfer_listenerattr_t *attr, unsigned short port) </p>
<p> int <code>globus_gass_transfer_listenerattr_get_port</code> (globus_gass_transfer_listenerattr_t *attr, unsigned short *port) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int globus_gass_transfer_listenerattr_init (globus_gass_transfer_listenerattr_t *attr, char *url_scheme)</h3>
<p> Initialize a listener attribute. </p>
<p> This function initializes the <i>attr</i> to contain a new protocol-specific listener attribute. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to be initialized.<br />
 <i>url_scheme</i> The scheme which which the attribute will be used for.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully initialized.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> Either <i>attr</i> or <i>url_scheme</i> was GLOBUS_NULL.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> No protocol module currently registered with GASS Transfer Library handles URLs with the specified <i>url_scheme</i>.</dl>
<h3>int globus_gass_transfer_listenerattr_set_backlog (globus_gass_transfer_listenerattr_t *attr, intbacklog)</h3>
<p> Set/Get the backlog attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to control then number of pending connections which may exist for this listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>backlog</i> The number of outstanding connections to allow.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h3>int globus_gass_transfer_listenerattr_set_port (globus_gass_transfer_listenerattr_t *attr, unsigned shortport)</h3>
<p> Set/Get the port attribute for a GASS transfer attribute set. </p>
<p> This attribute allows the user to set the port to be used by a GASS Transfer listener. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query or modify.<br />
 <i>port</i> The TCP or UDP port number to use.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The attribute was successfully updated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The <i>attr</i> was GLOBUS_NULL.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
