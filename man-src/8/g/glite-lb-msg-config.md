---
title: "glite-lb-msg-config(8)"
name: "glite-lb-msg-config"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glite-lb-msg-config/"
description: "glite-lb-msg-config – glite-lb-logger messaging plugin configuration generator"
---

<p>glite-lb-msg-config &#8211; glite-lb-logger messaging plugin configuration generator </p>
<h2>Synopsis</h2>
<p><code>glite-lb-msg-config</code> <i>TEMPLATE</i> [<i>TARGET</i>] </p>
<h2>Description</h2>
<p><code>glite-lb-msg-config</code> is a script for generating or updating glite-lb-logger messaging plugin configuration. Configuration parameters can be specified by environment variables. <i>TEMPLATE</i> is the original configuration file, basic content is generated in case the original doesn&#8217;t exist. <i>TARGET</i> is the target configuration file. If <i>TARGET</i> is not specified, the <i>TEMPLATE</i> is modified instead. This script is intended primarily to be run by cron, but can be run manually by site admins to avoid waiting for the next cron cycle. </p>
<h2>Environment</h2>
<dl>
<dt><code>GLITE_LOCATION </code>[prefix]</p>
<dd>Standard prefix (typically /usr). </p>
<dt><code>GLITE_LB_MSG_BROKER </code>[]</p>
<dd>The special values are: <code>false</code> (do nothing), <code>auto</code> (refresh messaging brokers from BDII), <code>once</code> (refresh messaging brokers only when <code>$GLITE_LB_SETUP</code> is not set). Empty value means <code>auto</code>, any other values means broker URL list. </p>
<p> For refreshing messaging brokers the <code><a href="/docs/linux/man/8-glite-lb-msg-brokers/">glite-lb-msg-brokers</a></code>(8) utility is called. </p>
<dt><code>GLITE_LB_MSG_NETWORK </code>[PROD]</p>
<dd>Let <code><a href="/docs/linux/man/8-glite-lb-msg-brokers/">glite-lb-msg-brokers</a></code>(8) search only in specified network. Typical values are PROD or TEST-NWOB. </p>
<dt><code>LCG_GFAL_INFOSYS </code>[lcg-bdii.cern.ch:2170]</p>
<dd><i>host</i>[:<i>port</i>] of the BDII server. </p>
<dt><code>GLITE_LB_SETUP </code>[]</p>
<dd>Helper variable. It should be set, when this configuration generator is called during setup stage (when <code>once</code> value in <code>$GLITE_LB_MSG_BROKER</code> should trigger BDII search). </p>
</dl>
<h2>Bugs</h2>
<p>Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>Authors</h2>
<p>L&amp;B Product Team, CESNET.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-glite-lb-msg-brokers/">glite-lb-msg-brokers</a></code>(8) </p>
