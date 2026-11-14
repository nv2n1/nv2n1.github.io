---
title: "atomic-push(1)"
name: "atomic-push"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-push/"
description: "atomic-push – push Image to repository"
---

<h2 class="name">NAME</h2>
<p> atomic-push &#8211; push Image to repository </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic push</code> [<code>-a</code>][<code>&#8211;activation_key</code>[=<i>ACTIVATION_KEY</i>]] [<code>&#8211;debug</code>] [<code>-h</code>|<code>&#8211;help</code>] [<code>&#8211;pulp</code>] [<code>-p</code>][<code>&#8211;password</code>[=<i>PASSWORD</i>]] [<code>-r</code>][<code>&#8211;repository_id</code>[=<i>REPOSITORY_ID</i>]] [<code>&#8211;satellite</code>] [<code>&#8211;sign-by</code>] [<code>&#8211;t</code>][<code>&#8211;type</code>] [<code>-u</code>][<code>&#8211;username</code>[=<i>USERNAME</i>]] [<code>-U</code>][<code>&#8211;url</code>[=<i>URL</i>]] [<code>&#8211;verify_ssl</code>[=<i>VERIFY_SSL</i>]] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic push</code> will push the image to the repository. Defaults to docker repository; can also upload to satellite or pulp repository. </p>
<h2>OPTIONS:</h2>
<p> <code>-a ACTIVATION_KEY</code> <code>&#8211;activation_key ACTIVATION_KEY</code><br />
&nbsp;<wbr>&nbsp;<wbr>Activation Key </p>
<p> <code>&#8211;debug</code><br />
&nbsp;<wbr>&nbsp;<wbr>Debug mode </p>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-p PASSWORD</code> <code>&#8211;password PASSWORD</code><br />
&nbsp;<wbr>&nbsp;<wbr>Password for remote registry </p>
<p> <code>&#8211;pulp</code><br />
&nbsp;<wbr>&nbsp;<wbr>Push using the pulp protocol, defaults to using docker push </p>
<p> <code>&#8211;r REPO_ID</code> <code>&#8211;repository_id REPO_ID</code><br />
&nbsp;<wbr>&nbsp;<wbr>Repository ID </p>
<p> <code>&#8211;satellite</code><br />
&nbsp;<wbr>&nbsp;<wbr>Upload using the satellite protocol;&nbsp;<wbr>defaults to using docker push </p>
<p> <code>&#8211;sign-by</code><br />
&nbsp;<wbr>&nbsp;<wbr>Override the default signing identity defined in&nbsp;<wbr>/etc/atomic.conf. Atomic push will always sign if there is a default<br />
&nbsp;<wbr>&nbsp;<wbr>identity or you pass an indentity here.&nbsp;<wbr>&nbsp;<wbr>If there is a default identity, you can pass&nbsp;<wbr><code>None</code>&nbsp;<wbr>to&nbsp;<wbr><code>&#8211;sign-by</code>&nbsp;<wbr>and<br />
signing will be disabled. </p>
<p> <code>-t REGISTRY_TYPE</code> <code>&#8211;type REGISTRY_TYPE</code><br />
&nbsp;<wbr>&nbsp;<wbr>Change the registry type,&nbsp;<wbr><code>docker|atomic</code>.&nbsp;<wbr>&nbsp;<wbr>atomic registry type is an OpenShift-based registry with an API supporting image signatures. Default is&nbsp;<wbr><code>docker</code>. </p>
<p> <code>-u USERNAME</code> <code>&#8211;username USERNAME</code><br />
&nbsp;<wbr>&nbsp;<wbr>Username for remote registry </p>
<p> <code>-U URL</code> <code>&#8211;url URL</code><br />
&nbsp;<wbr>&nbsp;<wbr>URL for remote registry </p>
<p> <code>&#8211;verify_ssl</code><br />
&nbsp;<wbr>&nbsp;<wbr>Flag to verify ssl of registry </p>
<h2>HISTORY</h2>
<p> April 2015, Originally compiled by Daniel Walsh (dwalsh at redhat dot com) </p>
<p> July 2015, Edited by Jenny Ramseyer (jramseye at redhat dot com) </p>
<p> September 2015, Edited by Daniel Walsh (dwalsh at redhat dot com) </p>
<p> September 2016, Updated by Brent Baude (bbaude at redhat dot com) </p>
<h2>Index</h2>
