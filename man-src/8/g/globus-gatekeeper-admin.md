---
title: "globus-gatekeeper-admin(8)"
name: "globus-gatekeeper-admin"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-gatekeeper-admin/"
description: "globus-gatekeeper-admin – Manage globus-gatekeeper services"
---

<p>globus-gatekeeper-admin &#8211; Manage globus-gatekeeper services</p>
<h2>Synopsis</h2>
<p><code>globus-gatekeeper-admin</code> [-h] </p>
<p> <code>globus-gatekeeper-admin</code> -l [-n <i>NAME</i>] </p>
<p> <code>globus-gatekeeper-admin</code> -e <i>SERVICE</i> [-n <i>NAME</i>] </p>
<p> <code>globus-gatekeeper-admin</code> -E </p>
<p> <code>globus-gatekeeper-admin</code> -d <i>SERVICE</i></p>
<h2>Description</h2>
<p>The <code>globus-gatekeeper-admin</code> program manages service entries which are used by the <code>globus-gatekeeper</code> to execute services. Service entries are located in the /etc/grid-services directory. The <code>globus-gatekeeper-admin</code> can list, enable, or disable specific services, or set a service as the default. The <i>-h</i> command-line option shows a brief usage message. </p>
<p> The <code>-l</code> command-line option to <code>globus-gatekeeper-admin</code> will cause it to list all of the services which are available to be run by the <code>globus-gatekeeper</code>. In the output, the service name will be followed by its status in brackets. Possible status strings are <code>ENABLED</code>, <code>DISABLED</code>, and <code>ALIAS to </code><i>NAME</i>, where <i>NAME</i> is another service name. </p>
<p> If the <code>-n </code><i>NAME</i> is used, then only information about the service named <i>NAME</i> is printed. </p>
<p> The <code>-e </code><i>SERVICE</i> command-line option to <code>globus-gatekeeper-admin</code> will cause it to enable a service so that it may be run by the <code>globus-gatekeeper</code>. </p>
<p> If the <code>-n </code><i>NAME</i> option is used as well, then the service will be enabled with the alias <i>NAME</i>. </p>
<p> The <code>-E</code> command-line option to <code>globus-gatekeeper-admin</code> will cause it to enable a service alias with the name jobmanager. The <code>globus-gatekeeper-admin</code> program will choose the first service it finds as the default. To enable a particular service as the default, use the <code>-e</code> parameter described above with the <code>-n</code> parameter. </p>
<p> The <code>-d </code><i>SERVICE</i> command-line option to <code>globus-gatekeeper-admin</code> will cause it to disable a service so that it may not be run by the <code>globus-gatekeeper</code>. All aliases to a disabled service are also disabled.</p>
<h2>Files</h2>
<p>The following files affect <code>globus-gatekeeper-admin</code> execution: </p>
<p> <code>/etc/grid-services</code></p>
<dl>
<dd>Default location of enabled gatekeeper service descriptions.</dl>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
