---
title: "sfcbrepos(1)"
name: "sfcbrepos"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfcbrepos/"
description: "sfcbrepos – Script to rebuild the Small-Footprint CIM Broker (sfcb) class repository"
---

<h2>NAME</h2>
<p> sfcbrepos &#8211; Script to rebuild the Small-Footprint CIM Broker (sfcb) class repository</p>
<h2>SYNOPSIS</h2>
<p> <code>sfcbrepos</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> sfcbrepos rebuilds the sfcb class repository from the staging files. Rebuilding is done offline and the sfcb CIMOM must be restarted for changes to take effect.</p>
<h2>OPTIONS</h2>
<p> Supported command line options are:</p>
<dl>
<dt><code>-c</code> <i>schemadir</i></p>
<dd> Path to obtain the CIM Schema classes. Default is <i>/usr/share/mof/cim-current</i></p>
<dt><code>-s</code> <i>stagingdir</i></p>
<dd> Path to sfcb staging area containing class MOFs and registration files Default is <i>/var/lib/sfcb/stage</i></p>
<dt><code>-r</code> <i>registrationdir</i></p>
<dd> Path to the sfcb registration directory, containing the root of the class repository directory tree. Default is <i>/var/lib/sfcb/registration</i></p>
<dt><code>-f</code></p>
<dd> Force option. Without this option you will be prompted to confirm creating a new class repository (and delete the old one). Setting this option will rebuild the new sfcb repository without prompting.</p>
<dt><code>-i</code></p>
<dd> Do <i>not</i> migrate instances from previous repository</p>
<dt><code>-b</code> <i>backendopts</i></p>
<dd> Set special backend options for sfcbmof. Valid options are: <code>P32</code> &#8211; compile for PowerPC target; <code>Q</code> &#8211; skip qualifiers in output file; <code>q</code> &#8211; skip Description, ValueMap, and Values qualifiers in output file. Note: eliminating qualifiers will often significantly reduce the size of the class repository.</p>
<dt><code>-X</code> <i>platform</i></p>
<dd> Alias of <code>-b</code></p>
<dt><code>-h</code></p>
<dd> Display usage information and exit.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/mof/cim-current/CIM_Schema.mof</i></p>
<dd> CIM Schema</p>
<dt><i>/var/lib/sfcb/registration/providerRegister</i></p>
<dd> Contains registration data for all installed providers.</p>
<dt><i>/var/lib/sfcb/registration/providerRegister.previous</i></p>
<dd> Contains registration data for all installed providers from previous time sfcbrepos was run. This can be used to restore an earlier class repository in case sfcbrepos generates a corrupt one.</p>
<dt><i>/var/lib/sfcb/registration/repository</i></p>
<dd> Contain class repository directory for all supported CIM namespaces.</p>
<dt><i>/var/lib/sfcb/registration/repository.previous</i></p>
<dd> Contain class repository directory for all supported CIM namespaces from the previous time sfcbrepos was run. This can be used to restore an earlier class repository in case sfcbrepos generates a corrupt one.</p>
<dt><i>/var/lib/sfcb/registration/repository/&#8230;/classSchemas</i></p>
<dd> Class data for a namespace.</p>
<dt><i>/var/lib/sfcb/stage/default.reg</i></p>
<dd> Registration data for the default built-in sfcb internal providers.</p>
<dt><i>/var/lib/sfcb/stage/mofs/root/interop/interop.mof</i></p>
<dd> Dummy classes used to added CIM indication support to the default interop namespace.</p>
<dt><i>/var/lib/sfcb/registration/stage/mofs/&#8230;/*.mof</i></p>
<dd> Class definitions for all installed providers.</p>
<dt><i>/var/lib/sfcb/registration/stage/regs/*.reg</i></p>
<dd> Registration info for all installed providers.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DESTDIR</code></p>
<dd> If set, the value of this variable is prepended to the registration directory names. This can be useful to store the repository in a different location, i.e. when cross-compiling providers.</dl>
<h2>LIBRARIES</h2>
<p> Requires libsfcBrokerCore.a</p>
<h2>AUTHOR</h2>
<p> Adrian Schuur &lt;schuur [at] de.ibm.com&gt;</p>
<h2>BUGS</h2>
<p> The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-issues">http://lists.sourceforge.net/lists/listinfo/sblim-issues</a></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dl>
<h2>COPYRIGHT</h2>
<p> (C) Copyright IBM Corp. 2004, 2005, 2009</p>
<h2>AVAILABILITY</h2>
<p> The Small-Footprint CIM Broker (sfcb) is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sfcbd/">sfcbd</a>(1),</code> <code><a href="/docs/linux/man/1-sfcbstage/">sfcbstage</a></code>(1), <code><a href="/docs/linux/man/1-sfcbunstage/">sfcbunstage</a></code>(1), <code><a href="/docs/linux/man/1-getschema/">getSchema</a></code>(1) </p>
<h2>Index</h2>
