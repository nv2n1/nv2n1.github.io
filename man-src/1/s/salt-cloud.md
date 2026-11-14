---
title: "salt-cloud(1)"
name: "salt-cloud"
section: "1"
letter: "s"
url: "/docs/linux/man/1-salt-cloud/"
description: "salt-cloud – Salt Cloud Command"
---

<h2>NAME</h2>
<p> salt-cloud &#8211; Salt Cloud Command </p>
<p> Provision virtual machines in the cloud with Salt</p>
<h2>SYNOPSIS</h2>
<pre>
salt-cloud -m /etc/salt/cloud.map
salt-cloud -m /etc/salt/cloud.map NAME
salt-cloud -m /etc/salt/cloud.map NAME1 NAME2
salt-cloud -p PROFILE NAME
salt-cloud -p PROFILE NAME1 NAME2 NAME3 NAME4 NAME5 NAME6
</pre>
<h2>DESCRIPTION</h2>
<p> Salt Cloud is the system used to provision virtual machines on various public clouds via a cleanly controlled profile and mapping system.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the version of Salt that is running.</p>
<dt><code>&#8211;versions-report</code></p>
<dd> Show program&#8217;s dependencies and version number, and then exit</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the help message and exit</p>
<dt><code>-c CONFIG_DIR, &#8211;config-dir=CONFIG_dir</code></p>
<dd> The location of the Salt configuration directory. This directory contains the configuration files for Salt master and minions. The default location on most systems is <code>/etc/salt</code>.</dl>
<h3>Execution Options</h3>
<dl>
<dt><code>-L LOCATION, &#8211;location=LOCATION</code></p>
<dd> Specify which region to connect to.</p>
<dt><code>-a ACTION, &#8211;action=ACTION</code></p>
<dd> Perform an action that may be specific to this cloud provider. This argument requires one or more instance names to be specified.</p>
<dt><code>-f &lt;FUNC-NAME&gt; &lt;PROVIDER&gt;, &#8211;function=&lt;FUNC-NAME&gt; &lt;PROVIDER&gt;</code></p>
<dd> Perform an function that may be specific to this cloud provider, that does not apply to an instance. This argument requires a provider to be specified (i.e.: nova).</p>
<dt><code>-p PROFILE, &#8211;profile=PROFILE</code></p>
<dd> Select a single profile to build the named cloud VMs from. The profile must be defined in the specified profiles file.</p>
<dt><code>-m MAP, &#8211;map=MAP</code></p>
<dd> Specify a map file to use. If used without any other options, this option will ensure that all of the mapped VMs are created. If the named VM already exists then it will be skipped.</p>
<dt><code>-H, &#8211;hard</code></p>
<dd> When specifying a map file, the default behavior is to ensure that all of the VMs specified in the map file are created. If the &#8211;hard option is set, then any VMs that exist on configured cloud providers that are not specified in the map file will be destroyed. Be advised that this can be a destructive operation and should be used with care.</p>
<dt><code>-d, &#8211;destroy</code></p>
<dd> Pass in the name(s) of VMs to destroy, salt-cloud will search the configured cloud providers for the specified names and destroy the VMs. Be advised that this is a destructive operation and should be used with care. Can be used in conjunction with the -m option to specify a map of VMs to be deleted.</p>
<dt><code>-P, &#8211;parallel</code></p>
<dd> Normally when building many cloud VMs they are executed serially. The -P option will run each cloud vm build in a separate process allowing for large groups of VMs to be build at once. </p>
<p> Be advised that some cloud provider&#8217;s systems don&#8217;t seem to be well suited for this influx of vm creation. When creating large groups of VMs watch the cloud provider carefully.</p>
<dt><code>-u, &#8211;update-bootstrap</code></p>
<dd> Update salt-bootstrap to the latest develop version on GitHub.</p>
<dt><code>-y, &#8211;assume-yes</code></p>
<dd> Default yes in answer to all confirmation questions.</p>
<dt><code>-k, &#8211;keep-tmp</code></p>
<dd> Do not remove files from /tmp/ after deploy.sh finishes.</p>
<dt><code>&#8211;show-deploy-args</code></p>
<dd> Include the options used to deploy the minion in the data returned.</p>
<dt><code>&#8211;script-args=SCRIPT_ARGS</code></p>
<dd> Script arguments to be fed to the bootstrap script when deploying the VM.</dl>
<h3>Query Options</h3>
<dl>
<dt><code>-Q, &#8211;query</code></p>
<dd> Execute a query and return some information about the nodes running on configured cloud providers</p>
<dt><code>-F, &#8211;full-query</code></p>
<dd> Execute a query and print out all available information about all cloud VMs. Can be used in conjunction with -m to display only information about the specified map.</p>
<dt><code>-S, &#8211;select-query</code></p>
<dd> Execute a query and print out selected information about all cloud VMs. Can be used in conjunction with -m to display only information about the specified map.</p>
<dt><code>&#8211;list-providers</code></p>
<dd> Display a list of configured providers.</p>
<dt><code>&#8211;list-profiles</code></p>
<dd> New in version 2014.7.0. </p>
<p> Display a list of configured profiles. Pass in a cloud provider to view the provider&#8217;s associated profiles, such as <code>digital_ocean</code>, or pass in <code>all</code> to list all the configured profiles.</dl>
<h3>Cloud Providers Listings</h3>
<dl>
<dt><code>&#8211;list-locations=LIST_LOCATIONS</code></p>
<dd> Display a list of locations available in configured cloud providers. Pass the cloud provider that available locations are desired on, aka &quot;linode&quot;, or pass &quot;all&quot; to list locations for all configured cloud providers</p>
<dt><code>&#8211;list-images=LIST_IMAGES</code></p>
<dd> Display a list of images available in configured cloud providers. Pass the cloud provider that available images are desired on, aka &quot;linode&quot;, or pass &quot;all&quot; to list images for all configured cloud providers</p>
<dt><code>&#8211;list-sizes=LIST_SIZES</code></p>
<dd> Display a list of sizes available in configured cloud providers. Pass the cloud provider that available sizes are desired on, aka &quot;AWS&quot;, or pass &quot;all&quot; to list sizes for all configured cloud providers</dl>
<h3>Cloud Credentials</h3>
<dl>
<dt><code>&#8211;set-password=&lt;USERNAME&gt; &lt;PROVIDER&gt;</code></p>
<dd> Configure password for a cloud provider and save it to the keyring. PROVIDER can be specified with or without a driver, for example: &quot;&#8211;set-password bob rackspace&quot; or more specific &quot;&#8211;set-password bob rackspace:openstack&quot; DEPRECATED!</dl>
<h3>Output Options</h3>
<dl>
<dt><code>&#8211;out</code></p>
<dd> Pass in an alternative outputter to display the return of data. This outputter can be any of the available outputters: <code>grains</code>, <code>highstate</code>, <code>json</code>, <code>key</code>, <code>overstatestage</code>, <code>pprint</code>, <code>raw</code>, <code>txt</code>, <code>yaml</code> </p>
<p> Some outputters are formatted only for data returned from specific functions; for instance, the <code>grains</code> outputter will not work for non-grains data. </p>
<p> If an outputter is used that does not support the data passed into it, then Salt will fall back on the <code>pprint</code> outputter and display the return data using the Python <code>pprint</code> standard library module. </p>
<p> <code>NOTE:</code> If using <code>&#8211;out=json</code>, you will probably want <code>&#8211;static</code> as well. Without the static option, you will get a separate JSON string per minion which makes JSON output invalid as a whole. This is due to using an iterative outputter. So if you want to feed it to a JSON parser, use <code>&#8211;static</code> as well.</p>
<dt><code>&#8211;out-indent OUTPUT_INDENT, &#8211;output-indent OUTPUT_INDENT</code></p>
<dd> Print the output indented by the provided value in spaces. Negative values disable indentation. Only applicable in outputters that support indentation.</p>
<dt><code>&#8211;out-file=OUTPUT_FILE, &#8211;output-file=OUTPUT_FILE</code></p>
<dd> Write the output to the specified file.</p>
<dt><code>&#8211;no-color</code></p>
<dd> Disable all colored output</p>
<dt><code>&#8211;force-color</code></p>
<dd> Force colored output </p>
<p> <code>NOTE:</code> When using colored output the color codes are as follows: </p>
<p> <code>green</code> denotes success, <code>red</code> denotes failure, <code>blue</code> denotes changes and success and <code>yellow</code> denotes a expected future change in configuration.</dl>
<h2>EXAMPLES</h2>
<p> To create 4 VMs named web1, web2, db1, and db2 from specified profiles: </p>
<pre>
salt-cloud -p fedora_rackspace web1 web2 db1 db2
</pre>
<p> To read in a map file and create all VMs specified therein: </p>
<pre>
salt-cloud -m /path/to/cloud.map
</pre>
<p> To read in a map file and create all VMs specified therein in parallel: </p>
<pre>
salt-cloud -m /path/to/cloud.map -P
</pre>
<p> To delete any VMs specified in the map file: </p>
<pre>
salt-cloud -m /path/to/cloud.map -d
</pre>
<p> To delete any VMs NOT specified in the map file: </p>
<pre>
salt-cloud -m /path/to/cloud.map -H
</pre>
<p> To display the status of all VMs specified in the map file: </p>
<pre>
salt-cloud -m /path/to/cloud.map -Q
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-salt-cloud/">salt-cloud</a>(7)</i> <i><a href="/docs/linux/man/7-salt/">salt</a>(7)</i> <i><a href="/docs/linux/man/1-salt-master/">salt-master</a>(1)</i> <i><a href="/docs/linux/man/1-salt-minion/">salt-minion</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Thomas S. Hatch &lt;thatch45 [at] gmail.com&gt; and many others, please see the Authors file</p>
<h2>COPYRIGHT</h2>
<p> 2016 SaltStack, Inc. </p>
<h2>Index</h2>
