---
title: "ocf_pacemaker_dummy(7)"
name: "ocf_pacemaker_dummy"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_dummy/"
description: "ocf_pacemaker_Dummy – Example stateless resource agent"
---

<p>ocf_pacemaker_Dummy &#8211; Example stateless resource agent</p>
<h2>Synopsis</h2>
<p><code>OCF_RESKEY_state</code>=string <code>OCF_RESKEY_passwd</code>=string [<code>OCF_RESKEY_fake</code>=string] <code>OCF_RESKEY_op_sleep</code>=string [<code>OCF_RESKEY_fail_start_on</code>=string] <code>OCF_RESKEY_envfile</code>=string <code>Dummy</code> [start | stop | monitor | reload | migrate_to | migrate_from | validate-all | meta-data]</p>
<h2>Description</h2>
<p>This is a Dummy Resource Agent. It does absolutely nothing except keep track of whether its running or not. Its purpose in life is for testing and to serve as a template for RA writers. NB: Please pay attention to the timeouts specified in the actions section below. They should be meaningful for the kind of resource the agent manages. They should be the minimum advised timeouts, but they shouldn&#8217;t/cannot cover _all_ possible resource instances. So, try to be neither overly generous nor too stingy, but moderate. The minimum timeouts should never be below 10 seconds.</p>
<h2>Supported Parameters</h2>
<p><code>OCF_RESKEY_state</code> = string [/Dummy-.state]</p>
<dl>
<dd>State file </p>
<p> Location to store the resource state in.</dl>
<p> <code>OCF_RESKEY_passwd</code> = string []</p>
<dl>
<dd>Password </p>
<p> Fake password field</dl>
<p> <code>OCF_RESKEY_fake</code> = string [dummy]</p>
<dl>
<dd>Fake attribute that can be changed to cause a reload </p>
<p> Fake attribute that can be changed to cause a reload</dl>
<p> <code>OCF_RESKEY_op_sleep</code> = string [0]</p>
<dl>
<dd>Operation sleep duration in seconds. </p>
<p> Number of seconds to sleep during operations. This can be used to test how the cluster reacts to operation timeouts.</dl>
<p> <code>OCF_RESKEY_fail_start_on</code> = string []</p>
<dl>
<dd>Report bogus start failure on specified host </p>
<p> Start actions will return failure if running on the host specified here, but the resource will start successfully anyway (future monitor calls will find it running). This can be used to test on-fail=ignore.</dl>
<p> <code>OCF_RESKEY_envfile</code> = string []</p>
<dl>
<dd>Environment dump file </p>
<p> If this is set, the environment will be dumped to this file for every call.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
