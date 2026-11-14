---
title: "pam_wrapper(1)"
name: "pam_wrapper"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pam_wrapper/"
description: "pam_wrapper – A preloadable wrapper to test PAM applications and PAM Modules"
---

<h2 class="name">NAME</h2>
<p> pam_wrapper &#8211; A preloadable wrapper to test PAM applications and PAM Modules </p>
<h2>SYNOPSIS</h2>
<p> LD_PRELOAD=libpam_wrapper.so PAM_WRAPPER=1 PAM_WRAPPER_SERVICE_DIR=/path_to_config <code>./myapplication</code></p>
<h2>DESCRIPTION</h2>
<p> This tool allows you to either test your PAM application or module. For testing PAM applications we have written a simple PAM module called pam_matrix (see below). If you plan to test a PAM module you can use the pamtest library we have implemented. It simplifies testing of modules. You can be combine it with the cmocka unit testing framework or you can use the provided Python bindings to write tests for your module in Python.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> pam_wrapper is activated and controlled by environment variables. You can set the following variables: </p>
<p> <code>PAM_WRAPPER</code></p>
<dl>
<dt>
<dd> If you load the pam_wrapper and enable it with setting PAM_WRAPPER=1 all PAM calls will be wrapped so you are able to specify a directory with the service files pam_wrapper should be using.</dl>
<p> <code>PAM_WRAPPER_SERVICE_DIR</code></p>
<dl>
<dt>
<dd> The directory to read PAM service files from.</dl>
<p> If you want to use pam_matrix (see below) or want to test your own PAM module you need to specify the absolute path to your module in the service files. </p>
<p> <code>PAM_WRAPPER_DEBUGLEVEL</code></p>
<dl>
<dt>
<dd> If you need to see what is going on in pam_wrapper itself or try to find a bug, you can enable logging support in pam_wrapper if you built it with debug symbols. </p>
<dl>
<dt>
<dd> &bull; 0 = ERROR</dl>
<dl>
<dt>
<dd> &bull; 1 = WARNING</dl>
<dl>
<dt>
<dd> &bull; 2 = DEBUG</dl>
<dl>
<dt>
<dd> &bull; 3 = TRACE</dl>
</dl>
<p> <code>PAM_WRAPPER_KEEP_DIR</code></p>
<dl>
<dt>
<dd> If this option is set to 1, then pam_wrapper won&#8217;t delete its temporary directories. Mostly useful for pam_wrapper development.</dl>
<h2>EXAMPLE</h2>
<p> A service file for pam_wrapper should look like this: </p>
<dl>
<dt>
<dd>
<pre>
auth            required        /usr/lib/pam_wrapper/pam_matrix.so passdb=/path/to/pdb
account         required        /usr/lib/pam_wrapper/pam_matrix.so passdb=/path/to/pdb
password        required        /usr/lib/pam_wrapper/pam_matrix.so passdb=/path/to/pdb
session         required        /usr/lib/pam_wrapper/pam_matrix.so passdb=/path/to/pdb
</pre>
</dl>
<p> The name of the file should represent the service name used by your PAM application. </p>
<p> LD_PRELOAD=./libpam_wrapper.so PAM_WRAPPER=1 PAM_WRAPPER_SERVICE_DIR=pam_services/ ./my_pam_app</p>
<h2>PAM_MATRIX</h2>
<p> We offer a module to make testing of PAM applications easier. You find more information in the <a href="/docs/linux/man/8-pam_matrix/">pam_matrix</a>(8) manpage. </p>
<h2>Index</h2>
