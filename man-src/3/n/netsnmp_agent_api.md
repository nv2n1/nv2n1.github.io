---
title: "netsnmp_agent_api(3)"
name: "netsnmp_agent_api"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_agent_api/"
description: "netsnmp_agent_api – embedding an agent into a external application"
---

<p>netsnmp_agent_api &#8211; embedding an agent into a external application</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/agent/net-snmp-agent-includes.h&gt;
#include &lt;net-snmp/net-snmp-config.h&gt;
#include &lt;net-snmp/net-snmp-includes.h&gt;

int main(int argc, char *argv[])
{
    int agentx_subagent = 1; /* Change this if you're a master agent.  */

    snmp_enable_stderrlog();

    /*  If we're an AgentX subagent...  */
    if (agentx_subagent) {
        /* ...make us an AgentX client.  */
        netsnmp_ds_set_boolean(NETSNMP_DS_APPLICATION_ID,
                               NETSNMP_DS_AGENT_ROLE, 1);
    }

    init_agent(&quot;yourappname&quot;);

    /*  Initialize your MIB code here.  */
    init_my_mib_code();

    /*  `yourappname' will be used to read yourappname.conf files.  */
    init_snmp(&quot;yourappname&quot;);

    /*  If we're going to be a SNMP master agent...  */
    if (!agentx_subagent)
        init_master_agent(); /*  Listen on default port (161).  */

    /*  Your main loop here...  */
    while (whatever) {
        /* if you use select(), see snmp_api(3) */
        /*     --- OR ---  */
        agent_check_and_process(0); /* 0 == don't block */
    }

    /*  At shutdown time:  */
    snmp_shutdown(&quot;yourappname&quot;);
}

Then : $(CC)... `net - snmp - config-- agent - libs`</code></pre>
<h2>Description</h2>
<p>Our goal is to create a easy to use interface to the Net-SNMP package such that you can take code that you have written that has been designed to be a Net-SNMP MIB module and embed it into an external application where you can either chose to be a SNMP master agent or an AgentX sub-agent using the same MIB module code. Our suggestion is that you use our (or another) SNMP agent as the AgentX master agent and chose to become an AgentX subagent which then attaches to the master. </p>
<p> The Net-SNMP package provides a pair of libraries that enables easy embedding of an SNMP or AgentX agent into an external software package. AgentX is an extensible protocol designed to allow multiple SNMP sub-agents all run on one machine under a single SNMP master agent. It is defined in RFC 2741. </p>
<p> You will need to perform a few tasks in order to accomplish this. First off, you will need to initialize both the SNMP library and the SNMP agent library. As indicated above, this is done slightly differently depending on whether or not you are going to perform as a master agent or an AgentX sub-agent.</p>
<h2>Configuration</h2>
<p>If you intend to operate as an AgentX sub-agent, you will have to configured the Net-SNMP package with agentx support (which is turned on by default, so just don&#8217;t turn it off) </p>
<p> Additionally, you will need to link against the Net-SNMP libraries (use the output of &quot;net-snmp-config &#8211;agent-libs&quot; to get a library list) and call subagent_pre_init() as indicated above.</p>
<h2>Compiling</h2>
<p>In order to make use of any of the above API, you will need to link against at least the four libraries listed above.</p>
<h2>Functions</h2>
<p>where to find out more information on them. It is certainly not a complete list of what is available within all the Net-SNMP libraries.</p>
<dl>
<dt>snmp_enable_stderrlog()</p>
<dd>Logs error output from the SNMP agent to the standard error stream.</p>
<dt>netsnmp_ds_set_boolean()</p>
<dd>Please see the <i><a href="/docs/linux/man/3-default_store/">default_store</a>(3)</i> manual page for more information about this API.</p>
<dt>init_agent(char *name)</p>
<dd>Initializes the embedded agent. This should be called before the <code>init_snmp()</code> call. <i>name</i> is used to dictate what .conf file to read when <code>init_snmp()</code> is called later.</p>
<dt>init_snmp(char *name)</p>
<dd>Initializes the SNMP library. Note that one of the things this will do will be to read configuration files in an effort to configure your application. It will attempt to read the configuration files named by the <i>name</i> string that you passed in. It can be used to configure access control, for instance. Please see the <i><a href="/docs/linux/man/3-netsnmp_config_api/">netsnmp_config_api</a>(3)</i>, <i><a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5)</i>, and <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> manual pages for further details on this subject.</p>
<dt>init_master_agent(void)</p>
<dd>Initializes the master agent and causes it to listen for SNMP requests on its default UDP port of 161.</p>
<dt>agent_check_and_process(int block)</p>
<dd>This checks for packets arriving on the SNMP port and processes them if some are found. If <i>block</i> is non-zero, the function call will block until a packet arrives or an alarm must be run (see <i><a href="/docs/linux/man/3-snmp_alarm/">snmp_alarm</a>(3)</i>). The return value from this function is a positive integer if packets were processed, zero if an alarm occurred and -1 if an error occured.</p>
<dt>snmp_shutdown(char *name);</p>
<dd>This shuts down the agent, saving any needed persistent storage, etc.</dl>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://www.net-snmp.org/tutorial-5/toolkit/">http://www.net-snmp.org/tutorial-5/toolkit/</a> <a href="/docs/linux/man/2-select/">select</a>(2), <a href="/docs/linux/man/3-snmp_api/">snmp_api</a>(3), <a href="/docs/linux/man/3-default_store/">default_store</a>(3), <a href="/docs/linux/man/3-snmp_alarm/">snmp_alarm</a>(3), <a href="/docs/linux/man/3-netsnmp_config_api/">netsnmp_config_api</a>(3), <a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5), <a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5) </p>
