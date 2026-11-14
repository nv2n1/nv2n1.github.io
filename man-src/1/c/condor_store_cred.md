---
title: "condor_store_cred(1)"
name: "condor_store_cred"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_store_cred/"
description: "condor_store_cred securely stash a password"
---

<h2>Name</h2>
<p> <i>condor_store_cred</i> securely stash a password </p>
<h2>Synopsis</h2>
<p> <i>condor_store_cred</i> [ <code>-help</code> ] </p>
<p> <i>condor_store_cred</i> <i>add</i> [ <code>-c</code><br />
&nbsp;<wbr>|&nbsp;<wbr> <code>-u </code> <i>username</i> ] [ <code>-p </code> <i>password</i> ] [ <code>-n </code> <i>machinename</i> ] [ <code>-f </code> <i>filename</i> ] </p>
<p> <i>condor_store_cred</i> <i>delete</i> [ <code>-c</code><br />
&nbsp;<wbr>|&nbsp;<wbr> <code>-u </code> <i>username</i> ] [ <code>-n </code> <i>machinename</i> ] </p>
<p> <i>condor_store_cred</i> <i>query</i> [ <code>-c</code><br />
&nbsp;<wbr>|&nbsp;<wbr> <code>-u </code> <i>username</i> ] [ <code>-n </code> <i>machinename</i> ] </p>
<h2>Description</h2>
<p> <i>condor_store_cred</i> stores passwords in a secure manner. There are two separate uses of <i>condor_store_cred</i> :</p>
<dl>
<dt>
<dd> 1. A shared pool password is needed in order to implement the PASSWORD authentication method. <i>condor_store_cred</i> using the <code>-c</code> option deals with the password for the implied condor_pool@$(UID_DOMAIN) user name.</p>
<dt>
<dd> On a Unix machine, <i>condor_store_cred</i> with the <code>-f</code> option is used to set the pool password, as needed when used with the PASSWORD authentication method. The pool password is placed in a file specified by the SEC_PASSWORD_FILE configuration variable.</p>
<dt>
<dd>
<dt>
<dd> 2. In order to submit a job from a Windows platform machine, or to execute a job on a Windows platform machine utilizing the <code>run_as_owner</code> functionality, <i>condor_store_cred</i> stores the password of a user/domain pair securely in the Windows registry. Using this stored password, HTCondor may act on behalf of the submitting user to access files, such as writing output or log files. HTCondor is able to run jobs with the user ID of the submitting user. The password is stored in the same manner as the system does when setting or changing account passwords.</dl>
<p> Passwords are stashed in a persistent manner; they are maintained across system reboots. </p>
<p> The <i>add</i> argument on the Windows platform stores the password securely in the registry. The user is prompted to enter the password twice for confirmation, and characters are not echoed. If there is already a password stashed, the old password will be overwritten by the new password. </p>
<p> The <i>delete</i> argument deletes the current password, if it exists. </p>
<p> The <i>query</i> reports whether the password is stored or not. </p>
<h2>Options</h2>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Operations refer to the pool password, as used in the PASSWORD authentication method.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-f </code> <i>filename</i></p>
<dl>
<dt>
<dd> For Unix machines only, generates a pool password file named <i>filename</i> that may be used with the PASSWORD authentication method.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Displays a brief summary of command options.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-n </code> <i>machinename</i></p>
<dl>
<dt>
<dd> Apply the command on the given machine.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-p </code> <i>password</i></p>
<dl>
<dt>
<dd> Stores <i>password</i> , rather than prompting the user to enter a password.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-u </code> <i>username</i></p>
<dl>
<dt>
<dd> Specify the user name.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_store_cred</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
