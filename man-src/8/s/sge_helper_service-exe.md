---
title: "sge_helper_service-exe(8)"
name: "sge_helper_service-exe"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sge_helper_service-exe/"
description: "SGE_Helper_Service.exe – xxQS_NAMExx job execution agent helper service"
---

<p>SGE_Helper_Service.exe &#8211; xxQS_NAMExx job execution agent helper service</p>
<h2>Synopsis</h2>
<p><code>SGE_Helper_Service.exe</code> [ <code>-help</code> | <code>-install </code> | <code>-uninstall</code> ]</p>
<h2>Description</h2>
<p><i>SGE_Helper_Service.exe helps the </i> to run Windows jobs that request to be allowed to display their GUI on the visible Desktop. It is a Win32 service that is started at boot time under the SYSTEM account, giving it the permissions to give any process the permissions to access the visible Desktop.<br />
 This service runs independently of the (i.e. it is not started and stopped together with the execution daemon) and there can be only one <i>SGE_Helper_Service.exe</i> per host. </p>
<p> Jobs can request to be allowed to display their GUI on the visible desktop by requesting the resource &quot;display_win_gui&quot; (qsub -l display_win_gui=1). See option &quot;-v&quot;, for information on how to set a job environment variable.<br />
 When running GUI jobs, the environment variable SGE_BACKGND_MODE can be used to direct where the output of the GUI will be displayed. If the environment variable SGE_BACKGND_MODE is set to &quot;TRUE&quot; or &quot;1&quot; and &quot;-l display_win_gui=true&quot; is requested, the job is started by the helper service, but the GUI is not opened on the execution host&#8217;s screen. Instead it is opened on a virtual screen. </p>
<p> The Windows administrator can operate this service using the usual Windows Service Control Manager or the &quot;net&quot; command. The &quot;start&quot; method starts the service if possible, the &quot;stop&quot; method stops it regardless of any jobs that might be still running. For a graceful shutdown, first run the &quot;pause&quot; method. This will start the shutdown procedure of the service and prevent it from accepting any further jobs. After this, the &quot;resume&quot; (aka &quot;continue&quot;) method will fail as long as there are jobs running in the <i>SGE_Helper_Service.exe</i>. If no job is left in the service, the &quot;resume&quot; method will succeed and the service will stop.</p>
<h2>Options</h2>
<h3><code>-help</code></h3>
<p>Prints a listing of all options.</p>
<h3><code>-install</code></h3>
<p>Installs the service. Only the local Administrator has the permissions to install the service.</p>
<h3><code>-uninstall</code></h3>
<p>Uninstalls the service. Only the local Administrator has the permissions to uninstall the service. Only a stopped service can be uninstalled. See the Windows command net.exe for information on how to stop a service.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
