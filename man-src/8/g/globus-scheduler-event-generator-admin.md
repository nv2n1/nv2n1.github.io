---
title: "globus-scheduler-event-generator-admin(8)"
name: "globus-scheduler-event-generator-admin"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-scheduler-event-generator-admin/"
description: "globus-scheduler-event-generator-admin – Enable globus-scheduler-event-generator services"
---

<p>globus-scheduler-event-generator-admin &#8211; Enable globus-scheduler-event-generator services</p>
<h2>Synopsis</h2>
<p><code>globus-scheduler-event-generator-admin</code> OPTIONS</p>
<h2>Description</h2>
<p>The <code>globus-scheduler-event-generator-admin</code> program enables or disables the <code>globus-scheduler-event-generator</code> for a particular local resource manager. It can also be used to list available local resource managers.</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display a help message and exit.</dl>
<p> <code>-e </code><i>SERVICE</i></p>
<dl>
<dd>Enable the globus-scheduler-event-generator for <i>SERVICE</i>, such as pbs or sge.</dl>
<p> <code>-d </code><i>SERVICE</i></p>
<dl>
<dd>Enable the globus-scheduler-event-generator for <i>SERVICE</i>, such as pbs or sge.</dl>
<p> <code>-n </code><i>NAME</i></p>
<dl>
<dd>When used with the -l option below, only list services which match <i>NAME</i>.</dl>
<p> <code>-l</code></p>
<dl>
<dd>List the all the available LRM services and whether they are enabled.</dl>
<h2>Author</h2>
<p>Copyright (c) 1999-2014 University of Chicago</p>
