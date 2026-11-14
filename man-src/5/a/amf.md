---
title: "amf(5)"
name: "amf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-amf/"
description: "amf.conf – corosync AMF configuration file"
---

<p>amf.conf &#8211; corosync AMF configuration file</p>
<h2>Description</h2>
<p><code>amf.conf</code> is the configuration file that determines the behaviour of the AIS Availability Management Framework service, AMF in the corosync implementation. Entries in this file will for example determine what applications AMF will start and how to supervise them. By default AMF opens /etc/ais/amf.conf. The environment variable <code>OPENAIS_AMF_CONFIG_FILE</code> can be set to the pathname of an AMF configuration file to override the default behaviour. Any line whose first non-white-space character is a &#8216;#&#8217; is considered a comment line. Empty lines are ignored. The file contains object entries of the form:</p>
<dl>
<dd>
<pre><code>&lt;Object Class&gt; = &lt;Object Name&gt; {
<dl><dt><dd>&lt;attribute&gt; = &lt;value&gt;
</dl>
}
</code></pre>
</dl>
<p> Object entries are nested, one entry contains another entry. This way relations between objects are built up. For example a component object defined inside a Software Unit (SU) object means that the component belongs to the SU. In other words, the SU is composed of the component. See the example configuration file. The relation between objects has to comply with the AMF model specified in [5]. Object names shall use only printable ASCII characters. Object names shall be unique within its context, i.e. two components within the same service unit has to have different names, but can have the same name as another component within another service unit. Attribute names are consistent with the naming of the configuration attributes in [5]. AMF object attributes are either configuration or runtime attributes. The AMF configuration file is used to specify configuration attributes. Some configuration attributes have default values and does not need to be specified. Others are not valid in certain redundancy models and so on. The type of an attribute value is either a string, a number, a time or an enumeration. Enumeration values are specified according to the type definition in the AIS specification. Time values are specified in milliseconds. Multivalue attributes are specified using multiple entries with the same attribute name but different values. See the example configuration file. The (RDN) value of &#8216;safAmfNode&#8217; is a logical name for an AMF node. It is mapped to a real physical node using the attribute &#8216;saAmfNodeClmNode&#8217;. The value of the attribute &#8216;saAmfNodeClmNode&#8217; should be the hostname (without domain name) as given to the host at boot time. This name is returned by the shell command &#8216;hostname&#8217;. Currently, AMF is enabled/disabled by an entry in the corosync.conf file, see [1]. It is default disabled. The following list of attributes is currently supported:</p>
<dl>
<dt><code>safAmfCluster</code></p>
<dd>
<dt><code>saAmfClusterStartupTimeout</code></p>
<dd>
<dt><code>safAmfNode</code></p>
<dd>
<dt><code>saAmfNodeClmNode</code></p>
<dd>Host name, required</p>
<dt><code>saAmfNodeSuFailOverProb</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfNodeSuFailoverMax</code></p>
<dd>Required but not used.</p>
<dt><code>safApp</code></p>
<dd>
<dt><code>clccli_path</code></p>
<dd>A path added to all CLC-CLI scripts</p>
<dt><code>saAmfSIProtectedbySG</code></p>
<dd>Required when several SGs are specified</p>
<dt><code>safSg</code></p>
<dd>
<dt><code>safSi</code></p>
<dd>
<dt><code>saAmfSINumCSIs</code></p>
<dd>Required but not used.</p>
<dt><code>safCSType</code></p>
<dd>
<dt><code>saAmfSGRedundancyModel</code></p>
<dd>Currently only &#8216;nplusm&#8217; is supported, required.</p>
<dt><code>saAmfSGNumPrefActiveSUs</code></p>
<dd>
<dt><code>saAmfSGNumPrefStandbySUs</code></p>
<dd>
<dt><code>saAmfSGMaxActiveSIsperSUs</code></p>
<dd>
<dt><code>saAmfSGMaxStandbySIsperSUs</code></p>
<dd>
<dt><code>saAmfSGCompRestartProb</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfSGCompRestartMax</code></p>
<dd>
<dt><code>saAmfSGSuRestartProb</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfSGAutoAdjustProb</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfSGSuRestartMax</code></p>
<dd>
<dt><code>safSu</code></p>
<dd>
<dt><code>saAmfSUNumComponents</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfSUIsExternal</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfSUFailover</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfSUHostedByNode</code></p>
<dd>Required. Set to AMF node name. Note: this is a deviation from the specification.</p>
<dt><code>safComp</code></p>
<dd>
<dt><code>saAmfCompCsTypes</code></p>
<dd>Multivalue</p>
<dt><code>saAmfCompCategory</code></p>
<dd>
<dt><code>saAmfCompCapability</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfCompNumMaxActiveCsi</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfCompNumMaxStandbyCsi</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfCompCmdEnv</code></p>
<dd>Multivalue</p>
<dt><code>saAmfCompDefaultClcCliTimeout</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfCompDefaultCallbackTimeOut</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfCompInstantiateCmdArgv</code></p>
<dd>
<dt><code>saAmfCompInstantiateCmd</code></p>
<dd>
<dt><code>saAmfCompTerminateCmdArgv</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfCompTerminateCmd</code></p>
<dd>Required but not used.</p>
<dt><code>saAmfCompCleanupCmdArgv</code></p>
<dd>
<dt><code>saAmfCompCleanupCmd</code></p>
<dd>
<dt><code>saAmfCompRecoveryOnError</code></p>
<dd>Required but not used.</p>
<dt><code>safHealthcheckKey</code></p>
<dd>
<dt><code>saAmfHealthcheckPeriod</code></p>
<dd>
<dt><code>saAmfHealthcheckMaxDuration</code></p>
<dd>
<dt><code>safCsi</code></p>
<dd>
<dt><code>saAmfSIPrefActiveAssignments</code></p>
<dd>
<dt><code>saAmfSIPrefStandbyAssignments</code></p>
<dd>
<dt><code>saAmfCSTypeName</code></p>
<dd>
<dt><code>safCSIAttr</code></p>
<dd>Multivalue </p>
<h2>Author</h2>
<p>Hans.Feldt at ericsson.com</p>
<h2>Example</h2>
<p>For an AMF configuration file example, see the amf.conf file under the corosync <code>conf</code> directory. </p>
<h2>Files</h2>
<dl>
<dt>/etc/ais/amf.conf</p>
<dd>
<dt>/etc/ais/corosync.conf</p>
<dd></dl>
<h2>See Also</h2>
<p>[1] corosync_conf (5)</p>
<dl>
<dt>[2] corosync_overview (8)</p>
<dd>
<dt>[3] README.amf</p>
<dd>
<dt>[4] <a rel="nofollow" href="http://www.saforum.org">www.saforum.org</a> &#8211; SAI-XMI-A.01.01.xml.xip</p>
<dd>
<dt>[5] <a rel="nofollow" href="http://www.saforum.org">www.saforum.org</a> &#8211; SAI-Overview.B.02.01.pdf</p>
<dd>
<dt>[6] <a rel="nofollow" href="http://www.saforum.org">www.saforum.org</a> &#8211; SAI-AIS-AMF-B.02.01.pdf</p>
<dd></dl>
