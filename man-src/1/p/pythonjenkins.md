---
title: "pythonjenkins(1)"
name: "pythonjenkins"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pythonjenkins/"
description: "pythonjenkins – Python Jenkins Documentation"
---

<h2>NAME</h2>
<p> pythonjenkins &#8211; Python Jenkins Documentation </p>
<p> Python Jenkins is a python wrapper for the <i>Jenkins</i> REST API which aims to provide a more conventionally pythonic way of controlling a Jenkins server. It provides a higher-level API containing a number of convenience functions. </p>
<p> We like to use python-jenkins to automate our Jenkins servers. Here are some of the things you can use it for:</p>
<dl>
<dt>&bull;</p>
<dd> Create new jobs</p>
<dt>&bull;</p>
<dd> Copy existing jobs</p>
<dt>&bull;</p>
<dd> Delete jobs</p>
<dt>&bull;</p>
<dd> Update jobs</p>
<dt>&bull;</p>
<dd> Get a job&#8217;s build information</p>
<dt>&bull;</p>
<dd> Get Jenkins master version information</p>
<dt>&bull;</p>
<dd> Get Jenkins plugin information</p>
<dt>&bull;</p>
<dd> Start a build on a job</p>
<dt>&bull;</p>
<dd> Create nodes</p>
<dt>&bull;</p>
<dd> Enable/Disable nodes</p>
<dt>&bull;</p>
<dd> Get information on nodes</p>
<dt>&bull;</p>
<dd> Create/delete/reconfig views</p>
<dt>&bull;</p>
<dd> and many more.. </p>
<p> To install: </p>
<pre>
$ sudo python setup.py install
</pre>
<p> Online documentation:</p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow" href="http://python-jenkins.readthedocs.org/en/latest/">http://python-jenkins.readthedocs.org/en/latest/</a></i></dl>
<h2>DEVELOPERS</h2>
<p> Bug report:</p>
<dl>
<dt>&bull;</p>
<dd> <i><a rel="nofollow" href="https://bugs.launchpad.net/python-jenkins">https://bugs.launchpad.net/python-jenkins</a></i> </p>
<p> Repository:</p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow" href="https://git.openstack.org/cgit/stackforge/python-jenkins">https://git.openstack.org/cgit/stackforge/python-jenkins</a></i> </p>
<p> Cloning:</p>
<dt>&bull;</p>
<dd> git clone <i><a rel="nofollow" href="https://git.openstack.org/stackforge/python-jenkins">https://git.openstack.org/stackforge/python-jenkins</a></i> </p>
<p> Patches are submitted via Gerrit at:</p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow" href="https://review.openstack.org/">https://review.openstack.org/</a></i> </p>
<p> Please do not submit GitHub pull requests, they will be automatically closed. </p>
<p> More details on how you can contribute is available on our wiki at:</p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow" href="http://docs.openstack.org/infra/manual/developers.html">http://docs.openstack.org/infra/manual/developers.html</a></i></dl>
<h2>WRITING A PATCH</h2>
<p> We ask that all code submissions be <i>flake8</i> clean. The easiest way to do that is to run <i>tox</i> before submitting code for review in Gerrit. It will run <code>flake8</code> in the same manner as the automated test suite that will run on proposed patchsets.</p>
<h2>INSTALLING WITHOUT SETUP.PY</h2>
<p> Then install the required python packages using <i>pip</i>: </p>
<pre>
$ sudo pip install python-jenkins
</pre>
<h2>API REFERENCE</h2>
<p> See examples at <code>example</code></p>
<dl>
<dt><code>exception jenkins.JenkinsException</code></p>
<dd> General exception type for jenkins-API-related failures.</p>
<dt><code>exception jenkins.NotFoundException</code></p>
<dd> A special exception to call out the case of receiving a 404.</p>
<dt><code>exception jenkins.EmptyResponseException</code></p>
<dd> A special exception to call out the case receiving an empty response.</p>
<dt><code>exception jenkins.BadHTTPException</code></p>
<dd> A special exception to call out the case of a broken HTTP response.</p>
<dt><code>jenkins.auth_headers(username, password)</code></p>
<dd> Simple implementation of HTTP Basic Authentication. </p>
<p> Returns the &#8216;Authentication&#8217; header value.</p>
<dt><code>class jenkins.Jenkins(url, username=None, password=None, timeout=&lt;object object at 0x7f5587ade220&gt;)</code></p>
<dd> Create handle to Jenkins instance. </p>
<p> All methods will raise <code>JenkinsException</code> on failure.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; Server username, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>password</code> &#8212; Server password, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>url</code> &#8212; URL of Jenkins server, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>timeout</code> &#8212; Server connection timeout in secs (default: not set), <code>int</code></p>
<dt><code>Jenkins.maybe_add_crumb(req)</code></p>
<dd>
<dt><code>Jenkins.get_job_info(name, depth=0)</code></p>
<dd> Get job information dictionary.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Job name, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>depth</code> &#8212; JSON depth, <code>int</code></p>
<dt><code>Returns</code></p>
<dd> dictionary of job information</p>
<dt><code>Jenkins.get_job_info_regex(pattern, depth=0)</code></p>
<dd> Get a list of jobs information that contain names which match the regex pattern.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>pattern</code> &#8212; regex pattern, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>depth</code> &#8212; JSON depth, <code>int</code></p>
<dt><code>Returns</code></p>
<dd> List of jobs info, <code>list</code></p>
<dt><code>Jenkins.get_job_name(name)</code></p>
<dd> Return the name of a job using the API. </p>
<p> That is roughly an identity method which can be used to quickly verify a job exist or is accessible without causing too much stress on the server side.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Job name, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> Name of job or None</p>
<dt><code>Jenkins.debug_job_info(job_name)</code></p>
<dd> Print out job info in more readable format.</p>
<dt><code>Jenkins.jenkins_open(req, add_crumb=True)</code></p>
<dd> Utility routine for opening an HTTP request to a Jenkins server. </p>
<p> This should only be used to extends the <code>Jenkins</code> API.</p>
<dt><code>Jenkins.get_build_info(name, number, depth=0)</code></p>
<dd> Get build information dictionary.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Job name, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Build number, <code>int</code></p>
<dt>&bull;</p>
<dd> <code>depth</code> &#8212; JSON depth, <code>int</code></p>
<dt><code>Returns</code></p>
<dd> dictionary of build information, <code>dict</code> </p>
<p> Example: </p>
<pre><code>
&gt;&gt;&gt; j = Jenkins() &gt;&gt;&gt; next_build_number = j.get_job_info('build_name')['nextBuildNumber'] &gt;&gt;&gt; output = j.build_job('build_name') &gt;&gt;&gt; from time import sleep;
sleep(10) &gt;&gt;&gt; build_info = j.get_build_info('build_name', next_build_number) &gt;&gt;&gt; print(build_info)
{
    u'building' : False, u'changeSet' : {u'items' : [ {u'date' : u'2011-12-19T18:01:52.540557Z', u'msg' : u'test', u'revision' : 66, u'user' : u'unknown', u'paths' : [ {u'editType' : u'edit', u'file' : u'/branches/demo/index.html'} ]} ], u'kind' : u'svn', u'revisions' : [ {u'module' : u'http://eaas-svn01.i3.level3.com/eaas', u'revision' : 66} ]}, u'builtOn' : u'', u'description' : None, u'artifacts' : [ {u'relativePath' : u'dist/eaas-87-2011-12-19_18-01-57.war', u'displayPath' : u'eaas-87-2011-12-19_18-01-57.war', u'fileName' : u'eaas-87-2011-12-19_18-01-57.war'}, {u'relativePath' : u'dist/eaas-87-2011-12-19_18-01-57.war.zip', u'displayPath' : u'eaas-87-2011-12-19_18-01-57.war.zip', u'fileName' : u'eaas-87-2011-12-19_18-01-57.war.zip'} ], u'timestamp' : 1324317717000, u'number' : 87, u'actions' : [ {u'parameters' : [ {u'name' : u'SERVICE_NAME', u'value' : u'eaas'}, {u'name' : u'PROJECT_NAME', u'value' : u'demo'} ]}, {u'causes' : [ {u'userName' : u'anonymous', u'shortDescription' : u'Started by user anonymous'} ]}, {}, {}, {} ], u'id' : u'2011-12-19_18-01-57', u'keepLog' : False, u'url' : u'http://eaas-jenkins01.i3.level3.com:9080/job/build_war/87/', u'culprits' : [ {u'absoluteUrl' : u'http://eaas-jenkins01.i3.level3.com:9080/user/unknown', u'fullName' : u'unknown'} ], u'result' : u'SUCCESS', u'duration' : 8826, u'fullDisplayName' : u'build_war #87'
}
</code></pre>
<dt><code>Jenkins.get_queue_info()</code></p>
<dd>
<dt><code>Returns</code></p>
<dd> list of job dictionaries, <code>[dict]</code></p>
<dt><code>Example::</code></p>
<dd>
<p>&gt;&gt;&gt; j = Jenkins() &gt;&gt;&gt; queue_info = j.get_queue_info() &gt;&gt;&gt; print(queue_info[0])<br />
{<br />
    u&#8217;task&#8217; : {u&#8217;url&#8217; : u&#8217;http://your_url/job/my_job/&#8217;, u&#8217;color&#8217; : u&#8217;aborted_anime&#8217;, u&#8217;name&#8217; : u&#8217;my_job&#8217;}, u&#8217;stuck&#8217; : False, u&#8217;actions&#8217; : [ {u&#8217;causes&#8217; : [ {u&#8217;shortDescription&#8217; : u&#8217;Started by timer&#8217;} ]} ], u&#8217;buildable&#8217; : False, u&#8217;params&#8217; : u&#8221;, u&#8217;buildableStartMilliseconds&#8217; : 1315087293316, u&#8217;why&#8217; : u&#8217;Build #2,532 is already in progress (ETA:10 min)&#8217;, u&#8217;blocked&#8217; : True<br />
}</p>
<dt><code>Jenkins.cancel_queue(id)</code></p>
<dd> Cancel a queued build.</p>
<dt><code>Parameters</code></p>
<dd> <code>id</code> &#8212; Jenkins job id number for the build, <code>int</code></p>
<dt><code>Jenkins.get_info()</code></p>
<dd> Get information on this Master. </p>
<p> This information includes job list and view information.</p>
<dt><code>Returns</code></p>
<dd> dictionary of information about Master, <code>dict</code> </p>
<p> Example: </p>
<p>&gt;&gt;&gt; j = Jenkins() &gt;&gt;&gt; info = j.get_info() &gt;&gt;&gt; jobs = info[&#8216;jobs&#8217;] &gt;&gt;&gt; print(jobs[0])<br />
{<br />
    u&#8217;url&#8217; : u&#8217;http://your_url_here/job/my_job/&#8217;, u&#8217;color&#8217; : u&#8217;blue&#8217;, u&#8217;name&#8217; : u&#8217;my_job&#8217;<br />
}</p>
<dt><code>Jenkins.get_version()</code></p>
<dd> Get the version of this Master.</p>
<dt><code>Returns</code></p>
<dd> This master&#8217;s version number <code>str</code> </p>
<p> Example: </p>
<pre>
&gt;&gt;&gt; j = Jenkins()
&gt;&gt;&gt; info = j.get_version()
&gt;&gt;&gt; print info
&gt;&gt;&gt; 1.541
</pre>
<dt><code>Jenkins.get_plugins_info(depth=2)</code></p>
<dd> Get all installed plugins information on this Master. </p>
<p> This method retrieves information about each plugin that is installed on master.</p>
<dt><code>Parameters</code></p>
<dd> <code>depth</code> &#8212; JSON depth, <code>int</code></p>
<dt><code>Returns</code></p>
<dd> info on all plugins <code>[dict]</code> </p>
<p> Example: </p>
<p>&gt;&gt;&gt; j = Jenkins() &gt;&gt;&gt; info = j.get_plugins_info() &gt;&gt;&gt; print(info)<br />
                                                          [{u&#8217;backupVersion&#8217; : None, u&#8217;version&#8217; : u&#8217;0.0.4&#8242;, u&#8217;deleted&#8217; : False, u&#8217;supportsDynamicLoad&#8217; : u&#8217;MAYBE&#8217;, u&#8217;hasUpdate&#8217; : True, u&#8217;enabled&#8217; : True, u&#8217;pinned&#8217; : False, u&#8217;downgradable&#8217; : False, u&#8217;dependencies&#8217; : [], u&#8217;url&#8217; : u&#8217;http://wiki.jenkins-ci.org/display/JENKINS/Gearman+Plugin&#8217;, u&#8217;longName&#8217; : u&#8217;Gearman Plugin&#8217;, u&#8217;active&#8217; : True, u&#8217;shortName&#8217; : u&#8217;gearman-plugin&#8217;, u&#8217;bundled&#8217; : False}, ..]</p>
<dt><code>Jenkins.get_plugin_info(name, depth=2)</code></p>
<dd> Get an installed plugin information on this Master. </p>
<p> This method retrieves information about a speicifc plugin. The passed in plugin name (short or long) must be an exact match.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name (short or long) of plugin, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>depth</code> &#8212; JSON depth, <code>int</code></p>
<dt><code>Returns</code></p>
<dd> a specific plugin <code>dict</code> </p>
<p> Example: </p>
<p>&gt;&gt;&gt; j = Jenkins() &gt;&gt;&gt; info = j.get_plugin_info(&#8220;Gearman Plugin&#8221;) &gt;&gt;&gt; print(info)<br />
{<br />
    u&#8217;backupVersion&#8217; : None, u&#8217;version&#8217; : u&#8217;0.0.4&#8242;, u&#8217;deleted&#8217; : False, u&#8217;supportsDynamicLoad&#8217; : u&#8217;MAYBE&#8217;, u&#8217;hasUpdate&#8217; : True, u&#8217;enabled&#8217; : True, u&#8217;pinned&#8217; : False, u&#8217;downgradable&#8217; : False, u&#8217;dependencies&#8217; : [], u&#8217;url&#8217; : u&#8217;http://wiki.jenkins-ci.org/display/JENKINS/Gearman+Plugin&#8217;, u&#8217;longName&#8217; : u&#8217;Gearman Plugin&#8217;, u&#8217;active&#8217; : True, u&#8217;shortName&#8217; : u&#8217;gearman-plugin&#8217;, u&#8217;bundled&#8217; : False<br />
}</p>
<dt><code>Jenkins.get_jobs()</code></p>
<dd> Get list of jobs running. </p>
<p> Each job is a dictionary with &#8216;name&#8217;, &#8216;url&#8217;, and &#8216;color&#8217; keys.</p>
<dt><code>Returns</code></p>
<dd> list of jobs, <code>[ { str: str} ]</code></p>
<dt><code>Jenkins.copy_job(from_name, to_name)</code></p>
<dd> Copy a Jenkins job</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>from_name</code> &#8212; Name of Jenkins job to copy from, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>to_name</code> &#8212; Name of Jenkins job to copy to, <code>str</code></p>
<dt><code>Jenkins.rename_job(from_name, to_name)</code></p>
<dd> Rename an existing Jenkins job</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>from_name</code> &#8212; Name of Jenkins job to rename, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>to_name</code> &#8212; New Jenkins job name, <code>str</code></p>
<dt><code>Jenkins.delete_job(name)</code></p>
<dd> Delete Jenkins job permanently.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt><code>Jenkins.enable_job(name)</code></p>
<dd> Enable Jenkins job.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt><code>Jenkins.disable_job(name)</code></p>
<dd> Disable Jenkins job. </p>
<p> To re-enable, call <code>Jenkins.enable_job()</code>.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt><code>Jenkins.job_exists(name)</code></p>
<dd> Check whether a job exists</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> <code>True</code> if Jenkins job exists</p>
<dt><code>Jenkins.jobs_count()</code></p>
<dd> Get the number of jobs on the Jenkins server</p>
<dt><code>Returns</code></p>
<dd> Total number of jobs, <code>int</code></p>
<dt><code>Jenkins.assert_job_exists(name, exception_message=&#8217;job[%s] does not exist&#8217;)</code></p>
<dd> Raise an exception if a job does not exist</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>exception_message</code> &#8212; Message to use for the exception. Formatted with <code>name</code></p>
<dt><code>Throws </code></p>
<dd> <code>JenkinsException</code> whenever the job does not exist</p>
<dt><code>Jenkins.create_job(name, config_xml)</code></p>
<dd> Create a new Jenkins job</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>config_xml</code> &#8212; config file text, <code>str</code></p>
<dt><code>Jenkins.get_job_config(name)</code></p>
<dd> Get configuration of existing Jenkins job.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> job configuration (XML format)</p>
<dt><code>Jenkins.reconfig_job(name, config_xml)</code></p>
<dd> Change configuration of existing Jenkins job. </p>
<p> To create a new job, see <code>Jenkins.create_job()</code>.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>config_xml</code> &#8212; New XML configuration, <code>str</code></p>
<dt><code>Jenkins.build_job_url(name, parameters=None, token=None)</code></p>
<dd> Get URL to trigger build job. </p>
<p> Authenticated setups may require configuring a token on the server side.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>parameters</code> &#8212; parameters for job, or None., <code>dict</code></p>
<dt>&bull;</p>
<dd> <code>token</code> &#8212; (optional) token for building job, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> URL for building job</p>
<dt><code>Jenkins.build_job(name, parameters=None, token=None)</code></p>
<dd> Trigger build job.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; name of job</p>
<dt>&bull;</p>
<dd> <code>parameters</code> &#8212; parameters for job, or <code>None</code>, <code>dict</code></p>
<dt>&bull;</p>
<dd> <code>token</code> &#8212; Jenkins API token</p>
<dt><code>Jenkins.run_script(script)</code></p>
<dd> Execute a groovy script on the jenkins master.</p>
<dt><code>Parameters</code></p>
<dd> <code>script</code> &#8212; The groovy script, <code>string</code></p>
<dt><code>Returns</code></p>
<dd> The result of the script run.</p>
<dt><code>Example::</code></p>
<dd>
<pre>
&gt;&gt;&gt; j = Jenkins()
&gt;&gt;&gt; info = j.run_script(&quot;println(Jenkins.instance.pluginManager.plugins)&quot;)
&gt;&gt;&gt; print(info)
u'[Plugin:windows-slaves, Plugin:ssh-slaves, Plugin:translation,
Plugin:cvs, Plugin:nodelabelparameter, Plugin:external-monitor-job,
Plugin:mailer, Plugin:jquery, Plugin:antisamy-markup-formatter,
Plugin:maven-plugin, Plugin:pam-auth]'
</pre>
<dt><code>Jenkins.stop_build(name, number)</code></p>
<dd> Stop a running Jenkins build.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name of Jenkins job, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>number</code> &#8212; Jenkins build number for the job, <code>int</code></p>
<dt><code>Jenkins.get_nodes()</code></p>
<dd> Get a list of nodes connected to the Master </p>
<p> Each node is a dict with keys &#8216;name&#8217; and &#8216;offline&#8217;</p>
<dt><code>Returns</code></p>
<dd> List of nodes, <code>[ { str: str, str: bool} ]</code></p>
<dt><code>Jenkins.get_node_info(name, depth=0)</code></p>
<dd> Get node information dictionary</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Node name, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>depth</code> &#8212; JSON depth, <code>int</code></p>
<dt><code>Returns</code></p>
<dd> Dictionary of node info, <code>dict</code></p>
<dt><code>Jenkins.node_exists(name)</code></p>
<dd> Check whether a node exists</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins node, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> <code>True</code> if Jenkins node exists</p>
<dt><code>Jenkins.assert_node_exists(name, exception_message=&#8217;node[%s] does not exist&#8217;)</code></p>
<dd> Raise an exception if a node does not exist</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name of Jenkins node, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>exception_message</code> &#8212; Message to use for the exception. Formatted with <code>name</code></p>
<dt><code>Throws </code></p>
<dd> <code>JenkinsException</code> whenever the node does not exist</p>
<dt><code>Jenkins.delete_node(name)</code></p>
<dd> Delete Jenkins node permanently.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins node, <code>str</code></p>
<dt><code>Jenkins.disable_node(name, msg=&#8221;)</code></p>
<dd> Disable a node</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Jenkins node name, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>msg</code> &#8212; Offline message, <code>str</code></p>
<dt><code>Jenkins.enable_node(name)</code></p>
<dd> Enable a node</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Jenkins node name, <code>str</code></p>
<dt><code>Jenkins.create_node(name, numExecutors=2, nodeDescription=None, remoteFS=&#8217;/var/lib/jenkins&#8217;, labels=None, exclusive=False, launcher=&#8217;hudson.slaves.CommandLauncher&#8217;, launcher_params={})</code></p>
<dd> Create a node</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; name of node to create, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>numExecutors</code> &#8212; number of executors for node, <code>int</code></p>
<dt>&bull;</p>
<dd> <code>nodeDescription</code> &#8212; Description of node, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>remoteFS</code> &#8212; Remote filesystem location to use, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>labels</code> &#8212; Labels to associate with node, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>exclusive</code> &#8212; Use this node for tied jobs only, <code>bool</code></p>
<dt>&bull;</p>
<dd> <code>launcher</code> &#8212; The launch method for the slave, <code>jenkins.LAUNCHER_COMMAND</code>, <code>jenkins.LAUNCHER_SSH</code>, <code>jenkins.LAUNCHER_JNLP</code>, <code>jenkins.LAUNCHER_WINDOWS_SERVICE</code></p>
<dt>&bull;</p>
<dd> <code>launcher_params</code> &#8212; Additional parameters for the launcher, <code>dict</code></p>
<dt><code>Jenkins.get_node_config(name)</code></p>
<dd> Get the configuration for a node.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Jenkins node name, <code>str</code></p>
<dt><code>Jenkins.reconfig_node(name, config_xml)</code></p>
<dd> Change the configuration for an existing node.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Jenkins node name, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>config_xml</code> &#8212; New XML configuration, <code>str</code></p>
<dt><code>Jenkins.get_build_console_output(name, number)</code></p>
<dd> Get build console text.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Job name, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Build number, <code>int</code></p>
<dt><code>Returns</code></p>
<dd> Build console output, <code>str</code></p>
<dt><code>Jenkins.get_view_name(name)</code></p>
<dd> Return the name of a view using the API. </p>
<p> That is roughly an identity method which can be used to quickly verify a view exists or is accessible without causing too much stress on the server side.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; View name, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> Name of view or None</p>
<dt><code>Jenkins.assert_view_exists(name, exception_message=&#8217;view[%s] does not exist&#8217;)</code></p>
<dd> Raise an exception if a view does not exist</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name of Jenkins view, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>exception_message</code> &#8212; Message to use for the exception. Formatted with <code>name</code></p>
<dt><code>Throws </code></p>
<dd> <code>JenkinsException</code> whenever the view does not exist</p>
<dt><code>Jenkins.view_exists(name)</code></p>
<dd> Check whether a view exists</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins view, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> <code>True</code> if Jenkins view exists</p>
<dt><code>Jenkins.get_views()</code></p>
<dd> Get list of views running. </p>
<p> Each view is a dictionary with &#8216;name&#8217; and &#8216;url&#8217; keys.</p>
<dt><code>Returns</code></p>
<dd> list of views, <code>[ { str: str} ]</code></p>
<dt><code>Jenkins.delete_view(name)</code></p>
<dd> Delete Jenkins view permanently.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins view, <code>str</code></p>
<dt><code>Jenkins.create_view(name, config_xml)</code></p>
<dd> Create a new Jenkins view</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name of Jenkins view, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>config_xml</code> &#8212; config file text, <code>str</code></p>
<dt><code>Jenkins.reconfig_view(name, config_xml)</code></p>
<dd> Change configuration of existing Jenkins view. </p>
<p> To create a new view, see <code>Jenkins.create_view()</code>.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; Name of Jenkins view, <code>str</code></p>
<dt>&bull;</p>
<dd> <code>config_xml</code> &#8212; New XML configuration, <code>str</code></p>
<dt><code>Jenkins.get_view_config(name)</code></p>
<dd> Get configuration of existing Jenkins view.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> &#8212; Name of Jenkins view, <code>str</code></p>
<dt><code>Returns</code></p>
<dd> view configuration (XML format)</dl>
<h2>EXAMPLE USAGE</h2>
<p> Example usage: </p>
<pre><code>
import jenkins j = jenkins.Jenkins('http://your_url_here', 'username', 'password') j.get_jobs() j.create_job('empty', jenkins.EMPTY_CONFIG_XML) j.disable_job('empty') j.copy_job('empty', 'empty_copy') j.enable_job('empty_copy') j.reconfig_job('empty_copy', jenkins.RECONFIG_XML) j.delete_job('empty') j.delete_job('empty_copy') j.get_views() j.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML) j.view_exists('EMPTY') j.delete_view('EMPTY')
#build a parameterized job
#requires setting up api - test job to accept 'param1' &amp; 'param2'
                                                                                                                                                                                                                                                                                                                                                                                                                                                     j.build_job('api-test', {'param1' : 'test value 1', 'param2' : 'test value 2' }) last_build_number = j.get_job_info('api-test')['lastCompletedBuild']['number'] build_info = j.get_job_info('api-test', last_build_number) print(build_info)
</code></pre>
<p> Look at the <code>api</code> for more details.</p>
<h2>INSTALLING</h2>
<p> The module is known to pip and Debian-based distributions as <code>python-jenkins</code>. </p>
<p> <code>pip</code>: </p>
<pre>
pip install python-jenkins
</pre>
<p> <code>easy_install</code>: </p>
<pre>
easy_install python-jenkins
</pre>
<p> The module has been packaged since Ubuntu Oneiric (11.10): </p>
<pre>
apt-get install python-jenkins
</pre>
<p> And on Fedora 19 and later: </p>
<pre>
yum install python-jenkins
</pre>
<p> For development: </p>
<pre>
python setup.py develop
</pre>
<h3>Documentation</h3>
<p> Documentation is included in the <code>doc</code> folder. To generate docs locally execute the command: </p>
<pre>
tox -e docs
</pre>
<p> The generated documentation is then available under <code>doc/build/html/index.html</code>.</p>
<h3>Unit Tests</h3>
<p> Unit tests have been included and are in the <code>tests</code> folder. We recently started including unit tests as examples in our documentation so to keep the examples up to date it is very important that we include unit tests for every module. To run the unit tests, execute the command: </p>
<pre>
tox -e py27
</pre>
<dl>
<dt>&bull;</p>
<dd> Note: View <code>tox.ini</code> to run tests on other versions of Python.</dl>
<h3>Test Coverage</h3>
<p> To measure test coverage, execute the command: </p>
<pre>
tox -e cover
</pre>
<dl>
<dt>&bull;</p>
<dd> <i>genindex</i></p>
<dt>&bull;</p>
<dd> <i>modindex</i></p>
<dt>&bull;</p>
<dd> <i>search</i></dl>
<h2>AUTHOR</h2>
<p> Ken Conley, James Page, Tully Foote, Matthew Gertner</p>
<h2>COPYRIGHT</h2>
<p> 2010, Willow Garage </p>
<h2>Index</h2>
