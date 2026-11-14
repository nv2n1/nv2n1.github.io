---
title: "ocf_pacemaker_healthsmart(7)"
name: "ocf_pacemaker_healthsmart"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_healthsmart/"
---

ocf_pacemaker_HealthSMART - SMART health status

<h2>Synopsis</h2>

<b>OCF_RESKEY_state</b>=string [<b>OCF_RESKEY_drives</b>=string] [<b>OCF_RESKEY_devices</b>=string] [<b>OCF_RESKEY_temp_lower_limit</b>=string] [<b>OCF_RESKEY_temp_upper_limit</b>=string] [<b>OCF_RESKEY_temp_warning</b>=string] <b>HealthSMART</b> [start | stop | monitor | meta-data | validate-all]

<h2>Description</h2>

Systhem health agent that checks the S.M.A.R.T. status of the given drives and updates the #health-smart attribute.

<h2>Supported Parameters</h2>

<b>OCF_RESKEY_state</b> = string [/HealthSMART-.state]
<dl><dd>State file 

 Location to store the resource state in.</dl>
 

 <b>OCF_RESKEY_drives</b> = string [/dev/sda]
<dl><dd>Drives to check 

 The drive(s) to check as a SPACE separated list. Enter the full path to the device, e.g. &quot;/dev/sda&quot;.</dl>
 

 <b>OCF_RESKEY_devices</b> = string
<dl><dd>Device types 

 The device type(s) to assume for the drive(s) being tested as a SPACE separated list.</dl>
 

 <b>OCF_RESKEY_temp_lower_limit</b> = string [0]
<dl><dd>Lower limit for the red smart attribute 

 Lower limit of the temperature in deg C of the drive(s). Below this limit the status will be red.</dl>
 

 <b>OCF_RESKEY_temp_upper_limit</b> = string [60]
<dl><dd>Upper limit for red smart attribute 

 Upper limit of the temperature if deg C of the drives(s). If the drive reports a temperature higher than this value the status of #health-smart will be red.</dl>
 

 <b>OCF_RESKEY_temp_warning</b> = string [5]
<dl><dd>Deg C below/above the upper limits for yellow smart attribute 

 Number of deg C below/above the upper/lower temp limits at which point the status of #health-smart will change to yellow.</dl>

<h2>Author</h2>

<b>Andrew Beekhof</b> &lt;andrew [at] beekhof.net&gt;
<dl><dd>Author.</dl>
