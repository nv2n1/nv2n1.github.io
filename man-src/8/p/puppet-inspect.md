---
title: "puppet-inspect(8)"
name: "puppet-inspect"
section: "8"
letter: "p"
url: "/docs/linux/man/8-puppet-inspect/"
description: "puppet-inspect – Send an inspection report"
---

<p><code>puppet-inspect</code> &#8211; Send an inspection report</p>
<h2>Synopsis</h2>
<p>Prepares and submits an inspection report to the puppet master.</p>
<h2>Usage</h2>
<p>puppet inspect [&#8211;archive_files] [&#8211;archive_file_server]</p>
<h2>Description</h2>
<p>This command uses the cached catalog from the previous run of &#8216;puppet agent&#8217; to determine which attributes of which resources have been marked as auditable with the &#8216;audit&#8217; metaparameter. It then examines the current state of the system, writes the state of the specified resource attributes to a report, and submits the report to the puppet master. </p>
<p> Puppet inspect does not run as a daemon, and must be run manually or from cron.</p>
<h2>Options</h2>
<p>Any configuration setting which is valid in the configuration file is also a valid long argument, e.g. &#8216;&#8211;server=master.domain.com&#8217;. See the configuration file documentation at <a rel="nofollow" href="http://docs.puppetlabs.com/references/latest/configuration.html">http://docs.puppetlabs.com/references/latest/configuration.html</a> for the full list of acceptable settings.</p>
<dl>
<dt>&#8211;archive_files</p>
<dd>During an inspect run, whether to archive files whose contents are audited to a file bucket.</p>
<dt>&#8211;archive_file_server</p>
<dd>During an inspect run, the file bucket server to archive files to if archive_files is set. The default value is &#8216;$server&#8217;.</dl>
<h2>Author</h2>
<p>Puppet Labs</p>
<h2>Copyright</h2>
<p>Copyright (c) 2011 Puppet Labs, LLC Licensed under the Apache 2.0 License</p>
