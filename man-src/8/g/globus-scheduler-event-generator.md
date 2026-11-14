---
title: "globus-scheduler-event-generator(8)"
name: "globus-scheduler-event-generator"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-scheduler-event-generator/"
description: "globus-scheduler-event-generator – Process job state change events"
---

<p>globus-scheduler-event-generator &#8211; Process job state change events</p>
<h2>Synopsis</h2>
<p><code>globus-scheduler-event-generator</code> -h </p>
<p> <code>globus-scheduler-event-generator</code> -s <i>LRM_NAME</i> [OPTIONS]</p>
<h2>Description</h2>
<p>The <code>globus-scheduler-event-generator</code> (SEG) is a program which uses local resource manager-specific monitoring modules to generate job state change events. At the SEG level, the state change events correspond to changes in any jobs which are managed by the scheduler, even if they do not correspond to jobs initiated by the GRAM5 Service. These state change events are propagated to the Job State Monitor. </p>
<p> Depending on scheduler-specific requirements, the SEG may need to run with privileges to enable it to obtain scheduler event notifications. As such, one SEG runs per scheduler resource. For example, on a host which provides access to both PBS and fork jobs, two SEGs, running at (potentially) different privilege levels will be running. </p>
<p> When executed, the SEG is able to start issuing events from some time in the past. The SEG will, in general, not require any persistent state between invocations. One SEG instance exists for any particular scheduled resource instance (one for all homogeneous PBS queues, one for all fork jobs, etc). </p>
<p> The SEG is implemented in an executable called the <code>globus-scheduler-event-generator</code>, located in the Globus Toolkit&#8217;s sbin directory. </p>
<p> When begun, it loads the LRM-specific module based on the <i>LRM_NAME</i> parameter, and then defers to it for most functionality. When it detects an error writing to stdout or reading stdin, it terminates. The LRM-specific code uses the SEG API to emit events to the GRAM5 service.</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display a help message and exit.</dl>
<p> <code>-s </code><i>LRM_NAME</i></p>
<dl>
<dd>Load the LRM-specific module for <i>LRM_NAME</i>. This is translated to loading the dynamic library libglobus_seg_&#8217;LRM_NAME&#8217;.</dl>
<p> <code>-t </code><i>TIMESTAMP</i></p>
<dl>
<dd>Process events starting at <i>TIMESTAMP</i>. This is the only way to get the globus-scheduler-event-generator to process events that occur before the process begins. If not specified, it will generate events from the current timestamp only.</dl>
<p> <code>-d </code><i>DIRECTORY</i></p>
<dl>
<dd>Write job state change events to files in <i>DIRECTORY</i>, named by the day that the event occurred (DIRECTORY/YYYYMMDD); if not specified, the events will be written to standard output.</dl>
<p> <code>-b</code></p>
<dl>
<dd>Run in the background. This only works if the <code>-d</code> option above is used.</dl>
<p> <code>-p </code><i>PIDFILE</i></p>
<dl>
<dd>Write the process id of the globus-scheduler-event-generator to <i>PIDFILE</i>.</dl>
<h2>Author</h2>
<p>Copyright (c) 1999-2014 University of Chicago</p>
