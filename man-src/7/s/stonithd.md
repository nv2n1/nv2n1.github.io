---
title: "stonithd(7)"
name: "stonithd"
section: "7"
letter: "s"
url: "/docs/linux/man/7-stonithd/"
description: "stonithd – Options available for all stonith resources"
---

<p>stonithd &#8211; Options available for all stonith resources</p>
<h2>Synopsis</h2>
<p>[<code>priority</code>=integer] [<code>pcmk_host_argument</code>=string] [<code>pcmk_host_map</code>=string] [<code>pcmk_host_list</code>=string] [<code>pcmk_host_check</code>=string] [<code>pcmk_delay_max</code>=time] [<code>pcmk_action_limit</code>=integer] [<code>pcmk_reboot_action</code>=string] [<code>pcmk_reboot_timeout</code>=time] [<code>pcmk_reboot_retries</code>=integer] [<code>pcmk_off_action</code>=string] [<code>pcmk_off_timeout</code>=time] [<code>pcmk_off_retries</code>=integer] [<code>pcmk_list_action</code>=string] [<code>pcmk_list_timeout</code>=time] [<code>pcmk_list_retries</code>=integer] [<code>pcmk_monitor_action</code>=string] [<code>pcmk_monitor_timeout</code>=time] [<code>pcmk_monitor_retries</code>=integer] [<code>pcmk_status_action</code>=string] [<code>pcmk_status_timeout</code>=time] [<code>pcmk_status_retries</code>=integer]</p>
<h2>Description</h2>
<p>This is a fake resource that details the instance attributes handled by stonithd.</p>
<h2>Supported Parameters</h2>
<p><code>priority</code> = integer [0]</p>
<dl>
<dd>The priority of the stonith resource. Devices are tried in order of highest priority to lowest. </p>
</dl>
<p> <code>pcmk_host_argument</code> = string [port]</p>
<dl>
<dd>Advanced use only: An alternate parameter to supply instead of &#8216;port&#8217; </p>
<p> Some devices do not support the standard &#8216;port&#8217; parameter or may provide additional ones. Use this to specify an alternate, device-specific, parameter that should indicate the machine to be fenced. A value of &#8216;none&#8217; can be used to tell the cluster not to supply any additional parameters.</dl>
<p> <code>pcmk_host_map</code> = string []</p>
<dl>
<dd>A mapping of host names to ports numbers for devices that do not support host names. </p>
<p> Eg. node1:1;node2:2,3 would tell the cluster to use port 1 for node1 and ports 2 and 3 for node2</dl>
<p> <code>pcmk_host_list</code> = string []</p>
<dl>
<dd>A list of machines controlled by this device (Optional unless pcmk_host_check=static-list). </p>
</dl>
<p> <code>pcmk_host_check</code> = string [dynamic-list]</p>
<dl>
<dd>How to determine which machines are controlled by the device. </p>
<p> Allowed values: dynamic-list (query the device), static-list (check the pcmk_host_list attribute), none (assume every device can fence every machine)</dl>
<p> <code>pcmk_delay_max</code> = time [0s]</p>
<dl>
<dd>Enable random delay for stonith actions and specify the maximum of random delay </p>
<p> This prevents double fencing when using slow devices such as sbd. Use this to enable random delay for stonith actions and specify the maximum of random delay.</dl>
<p> <code>pcmk_action_limit</code> = integer [1]</p>
<dl>
<dd>The maximum number of actions can be performed in parallel on this device </p>
<p> Pengine property concurrent-fencing=true needs to be configured first. Then use this to specify the maximum number of actions can be performed in parallel on this device. -1 is unlimited.</dl>
<p> <code>pcmk_reboot_action</code> = string [reboot]</p>
<dl>
<dd>Advanced use only: An alternate command to run instead of &#8216;reboot&#8217; </p>
<p> Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the &#8216;reboot&#8217; action.</dl>
<p> <code>pcmk_reboot_timeout</code> = time [60s]</p>
<dl>
<dd>Advanced use only: Specify an alternate timeout to use for reboot actions instead of stonith-timeout </p>
<p> Some devices need much more/less time to complete than normal. Use this to specify an alternate, device-specific, timeout for &#8216;reboot&#8217; actions.</dl>
<p> <code>pcmk_reboot_retries</code> = integer [2]</p>
<dl>
<dd>Advanced use only: The maximum number of times to retry the &#8216;reboot&#8217; command within the timeout period </p>
<p> Some devices do not support multiple connections. Operations may &#8216;fail&#8217; if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries &#8216;reboot&#8217; actions before giving up.</dl>
<p> <code>pcmk_off_action</code> = string [off]</p>
<dl>
<dd>Advanced use only: An alternate command to run instead of &#8216;off&#8217; </p>
<p> Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the &#8216;off&#8217; action.</dl>
<p> <code>pcmk_off_timeout</code> = time [60s]</p>
<dl>
<dd>Advanced use only: Specify an alternate timeout to use for off actions instead of stonith-timeout </p>
<p> Some devices need much more/less time to complete than normal. Use this to specify an alternate, device-specific, timeout for &#8216;off&#8217; actions.</dl>
<p> <code>pcmk_off_retries</code> = integer [2]</p>
<dl>
<dd>Advanced use only: The maximum number of times to retry the &#8216;off&#8217; command within the timeout period </p>
<p> Some devices do not support multiple connections. Operations may &#8216;fail&#8217; if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries &#8216;off&#8217; actions before giving up.</dl>
<p> <code>pcmk_list_action</code> = string [list]</p>
<dl>
<dd>Advanced use only: An alternate command to run instead of &#8216;list&#8217; </p>
<p> Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the &#8216;list&#8217; action.</dl>
<p> <code>pcmk_list_timeout</code> = time [60s]</p>
<dl>
<dd>Advanced use only: Specify an alternate timeout to use for list actions instead of stonith-timeout </p>
<p> Some devices need much more/less time to complete than normal. Use this to specify an alternate, device-specific, timeout for &#8216;list&#8217; actions.</dl>
<p> <code>pcmk_list_retries</code> = integer [2]</p>
<dl>
<dd>Advanced use only: The maximum number of times to retry the &#8216;list&#8217; command within the timeout period </p>
<p> Some devices do not support multiple connections. Operations may &#8216;fail&#8217; if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries &#8216;list&#8217; actions before giving up.</dl>
<p> <code>pcmk_monitor_action</code> = string [monitor]</p>
<dl>
<dd>Advanced use only: An alternate command to run instead of &#8216;monitor&#8217; </p>
<p> Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the &#8216;monitor&#8217; action.</dl>
<p> <code>pcmk_monitor_timeout</code> = time [60s]</p>
<dl>
<dd>Advanced use only: Specify an alternate timeout to use for monitor actions instead of stonith-timeout </p>
<p> Some devices need much more/less time to complete than normal. Use this to specify an alternate, device-specific, timeout for &#8216;monitor&#8217; actions.</dl>
<p> <code>pcmk_monitor_retries</code> = integer [2]</p>
<dl>
<dd>Advanced use only: The maximum number of times to retry the &#8216;monitor&#8217; command within the timeout period </p>
<p> Some devices do not support multiple connections. Operations may &#8216;fail&#8217; if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries &#8216;monitor&#8217; actions before giving up.</dl>
<p> <code>pcmk_status_action</code> = string [status]</p>
<dl>
<dd>Advanced use only: An alternate command to run instead of &#8216;status&#8217; </p>
<p> Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the &#8216;status&#8217; action.</dl>
<p> <code>pcmk_status_timeout</code> = time [60s]</p>
<dl>
<dd>Advanced use only: Specify an alternate timeout to use for status actions instead of stonith-timeout </p>
<p> Some devices need much more/less time to complete than normal. Use this to specify an alternate, device-specific, timeout for &#8216;status&#8217; actions.</dl>
<p> <code>pcmk_status_retries</code> = integer [2]</p>
<dl>
<dd>Advanced use only: The maximum number of times to retry the &#8216;status&#8217; command within the timeout period </p>
<p> Some devices do not support multiple connections. Operations may &#8216;fail&#8217; if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries &#8216;status&#8217; actions before giving up.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
