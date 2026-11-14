---
title: "globus-gram-audit(8)"
name: "globus-gram-audit"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-gram-audit/"
description: "globus-gram-audit – Load GRAM5 audit records into a database"
---

<p>globus-gram-audit &#8211; Load GRAM5 audit records into a database</p>
<h2>Synopsis</h2>
<p><code>globus-gram-audit</code> [ &#8211;conf <i>CONFIG-FILE</i> ] [ &#8211;create | &#8211;update=<i>OLD-VERSION</i> ] [ &#8211;check ] [ &#8211;delete ] [ &#8211;audit-directory=<i>AUDITDIR</i> ] [ &#8211;quiet ]</p>
<h2>Description</h2>
<p>The <code>globus-gram-audit</code> program loads audit records to an SQL-based database. It reads /etc/globus-job-manager.conf by default to determine the audit directory and then uploads all files in that directory that contain valid audit records to the database configured by the <code>globus_gram_job_manager_auditing_setup_scripts</code> package. If the upload completes successfully, the audit files will be removed. </p>
<p> The full set of command-line options to <code>globus-gram-audit</code> consist of: </p>
<p> <code>&#8211;conf </code><i>CONFIG-FILE</i></p>
<dl>
<dd>Use <i>CONFIG-FILE</i> instead of the default from the configuration file for audit database configuration.</dl>
<p> <code>&#8211;check</code></p>
<dl>
<dd>Check whether the insertion of a record was successful by querying the database after inserting the records. This is used in tests.</dl>
<p> <code>&#8211;delete</code></p>
<dl>
<dd>Delete audit records from the database right after inserting them. This is used in tests to avoid filling the databse with test records.</dl>
<p> <code>&#8211;audit-directory </code><i>AUDITDIR</i></p>
<dl>
<dd>Look for audit records in <i>AUDITDIR</i>, instead of looking in the directory specified in the job manager configuration. This is used in tests to control which records are loaded to the database and then deleted.</dl>
<p> <code>&#8211;query </code><i>SQL</i></p>
<dl>
<dd>Perform the given SQL query on the audit database. This uses the database information from the configuration file to determine how to contact the database.</dl>
<p> <code>&#8211;quiet</code></p>
<dl>
<dd>Reduce the amount of output for common operations.</dl>
<h2>Files</h2>
<p>The <code>globus-gram-audit</code> uses the following files: </p>
<p> <code>/etc/globus-gram-job-manager.conf</code></p>
<dl>
<dd>GRAM5 job manager configuration. It includes the default path to the audit directory</dl>
<p> <code>/etc/globus-gram-audit.conf</code></p>
<dl>
<dd>Audit configuration. It includes the information needed to contact the audit database.</dl>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
